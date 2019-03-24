# Лабораторная работа №1

Исполнитель: Родионова Вера Алексеевна, група КП-81мп

## Задача:
Для произвольной библиотеки/модуля на C#/Java/C++/Python необходимо создатьутилиту, которая позволяет рассчитать:

* Количество строк кода
* Количество пустых строк
* Количество физических и логических строк
* Количество строк c комментариями и оценку уровня комментированности

Выбранная библиотека/модуль должна быть объемом не менее 50 KLOCs.

## Результаты:

Программа, написанная на Node.js

Для того, чтобы проверить, необходимо выполнить:

```
npm install

node lab1.js [<path>]
```

где `[<path>]` - путь к JS-модулю, который нужно проанадизировать. 

Для данной лабораторной работы был выбран модуль [`livr`](http://livr-spec.org/)

```
node lab1.js ./node_modules/livr/lib/LIVR
```

```
{
    num_of_lines: 845,
    num_of_empty_lines: 170,
    num_of_phisic_lines: 666,
    num_of_logic_lines: 1215,
    num_of_lines_with_comments: 9,
    F: -8
}
```

```
node lab1.js ./node_modules/livr/lib/LIVR/Rules/Modifiers.js
```

```
{
    num_of_lines: 62,
    num_of_empty_lines: 13,
    num_of_phisic_lines: 44,
    num_of_logic_lines: 95,
    num_of_lines_with_comments: 5,
    F: -1
}
```