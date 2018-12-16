# Практичне завдання №1

Для виконання даного практичного завдання було взято код з бакалаврського дипломного проекту. ()
Для аналізу було взято файл DiaryActions.js, що відповідає за маніпулювання записами різних типів у щоденнику.

**DiaryActions.js**

```javascript
import moment from 'moment';
import api from '../apiSingleton';

import { formattedDate }      from '../utils/dateUtils.js';
import { saveToAsyncStorage } from '../utils/asyncStorageUtils.js';

import { clearSelectedProducts } from './SearchBarActions.js';

export const ADD_FOOD_NOTE       = 'ADD_FOOD_NOTE';
export const REMOVE_FOOD_NOTE    = 'REMOVE_FOOD_NOTE';
export const ADD_GLUCOSE_NOTE    = 'ADD_GLUCOSE_NOTE';
export const REMOVE_GLUCOSE_NOTE = 'REMOVE_GLUCOSE_NOTE';
export const ADD_INSULIN_NOTE    = 'ADD_INSULIN_NOTE';
export const REMOVE_INSULIN_NOTE = 'REMOVE_INSULIN_NOTE';
export const GET_WEEK            = 'GET_WEEK';

export function addNote(date, time, timeType, water) {
    return async (dispatch, getState) => {
        if (water || getState().searchBar.products && getState().searchBar.products.length) {
            const diary = { ...getState().data.food };

            const products = (getState().searchBar.products || []).map(pr => ({
                id    : pr.id,
                value : pr.amount
            }));

            let item = { time, timeType, water: water || null, products };

            const id = await api.notes.createNote({ ...item, dateFrom: moment(`${date}T${time}`) }, 'product');

            item = { ...item, id };

            if (!diary[date]) diary[date] = {};

            const notes = [ ...(diary[date].notes || []), item ];

            await saveToAsyncStorage('food_diary', { ...diary, [date]: { notes } });

            await dispatch({
                type     : ADD_FOOD_NOTE,
                item     : { ...item, products },
                date,
                dataType : 'food'
            });

            dispatch(clearSelectedProducts());
        }
    };
}

export function removeFoodNote(date, id) {
    return async (dispatch, getState) => {
        const diary = { ...getState().data.food };
        const res = await api.notes.deleteNote({ id }, 'product');

        if (res) {
            diary[date].notes = (diary[date].notes || []).filter(item => item.id !== id);

            await saveToAsyncStorage('food_diary', diary);

            await dispatch({
                type : REMOVE_FOOD_NOTE,
                date,
                id
            });
        }
    };
}

export function addGlucoseNote(date, time, value) {
    return async (dispatch, getState) => {
        try {
            const diary = { ...getState().data.glucose };

            const id = await api.notes.createNote({ dateFrom: moment(`${date}T${time}`), value }, 'glucose');

            const item = { id, date: moment(`${date}T${time}`).toISOString(), value };

            diary[date] = [ ...(diary[date] || []), item ];

            await saveToAsyncStorage('glucose_diary', diary);

            dispatch({
                type     : ADD_GLUCOSE_NOTE,
                item,
                dataType : 'glucose',
                date
            });
        } catch (err) {
            console.log('add glucose note error: ', err);
        }
    };
}

export function addInsulinNote(date, time, value, type) {
    return async (dispatch, getState) => {
        try {
            // const insulinMan = getState().user.info[`${type}InsulinManId`];

            const manId = getState().user.info[`${type}Insulin`];
            const insulinMan = (getState().user.info.insulinMans || [])[manId];

            const diary = { ...getState().data.insulin };

            if (!diary[date]) diary[date] = { 'short': [], 'long': [] };

            let item = { date: moment(`${date}T${time}`).toISOString(), value, insulinMan, isLong: type === 'long' };

            const id = await api.notes.createNote({ ...item, dateFrom: moment(`${date}T${time}`) }, 'insulin');

            item = { ...item, id };

            diary[date] = [ ...diary[date], item ];

            await saveToAsyncStorage('insulin_diary', diary);

            dispatch({
                type        : ADD_INSULIN_NOTE,
                item,
                insulinType : type,
                date
            });
        } catch (err) {
            console.log('add insulin note error: ', err);
            console.warn(err);
        }
    };
}

export function removeInsulinNote(date, id) {
    return async (dispatch, getState) => {
        const diary = { ...getState().data.insulin };

        const res = await api.notes.deleteNote({ id }, 'insulin');

        if (res) {
            diary[date] = diary[date].filter(item => item.id !== id);

            await saveToAsyncStorage('insulin_diary', diary);

            dispatch({
                type : REMOVE_INSULIN_NOTE,
                date,
                id
            });
        }
    };
}

export function removeGlucoseNote(date, id) {
    return async (dispatch, getState) => {
        const diary = { ...getState().data.glucose };

        const res = await api.notes.deleteNote({ id }, 'glucose');

        if (res) {
            diary[date] = (diary[date] || []).filter(item => item.id !== id);

            await saveToAsyncStorage('glucose_diary', diary);

            dispatch({
                type : REMOVE_GLUCOSE_NOTE,
                date,
                id
            });
        }
    };
}

export function getWeek(date) {
    return {
        type : GET_WEEK,
        date : formattedDate(moment(date))
    };
}
```

Даний код має такі проблеми:
1. Дублювання коду – «Замусоварители»:
2. Альтернативні класи з різними інтерфейсами (методи) – «Нарушители ООД»:
    * addFoodNote, addGlucoseNote, addInsulinNote
    * removeFoodNote, removeGlucoseNote, removeInsulinNote
    * методи виконують одні й ті самі функції, але мають по реалізації для кожного типу даних. При додаванні нового типу даних буде необхідно дублювати код.
    * дані типів: ‘food’, ‘glucose’, ‘insulin’ – можуть бути приведені до однієї структури. Таким чином для додавання чи видалення даних типів можна буде використовувати один і той самий метод
3. Довгий список параметрів – «Раздувальщики»:
4. Довгий метод – «Раздувальщики»:
    * addFoodNote, addGlucoseNote, addInsulinNote
    * один метод виконує занадто багато операцій, тому є довгим і складним. На мою думку, метод додавання запису необхідно розбити на такі 3: створення об’єкту запису, додавання об’єкта запису до бази даних (запит на сервер), додавання об’єкта запису до локального щоденника (diary).
    * А параметри можна передавати у вигляді об’єкту, яким і є набір даних
5. Ланцюжок викликів – «Опутыватели связями»:
    * const manId = getState().user.info.insulinMans
    * const insulinMan = (getState().user.info.insulinMans || [])[manId]
    * Для того, щоб виправити цей недолік, необхідно створити метод getInsulinManByType()

**Також, слід зазначити, що деякі методи не обгорнуто у try {} catch () {} блоки, тому можуть спричиняти помилки на більш високому рівні.**
