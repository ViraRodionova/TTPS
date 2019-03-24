const path          = require('path');
const fs            = require('fs');
const FileProcessor = require('./FileProcessor.js');

const STATS = {};

if (process.argv.length < 3) {
    throw new Error('No path to file was defined');
}

const PATH = path.join(process.cwd(), process.argv[2]);

main(PATH);

async function main(_path) {
    await readdir(_path);
    console.log(STATS);
}

async function readfile(_path) {
    if (!_path.endsWith('.js')) return;

    try {
        const processor = new FileProcessor(_path);

        const values = await processor.run();

        for (const [ key, value ] of Object.entries(values)) {
            if (!STATS[key]) STATS[key] = 0;

            if (key === 'F') {
                STATS[key] += Math.sign(Number(value) - 0.1)
            } else STATS[key] += value;
        }
    } catch(e) {}
}

async function readdir(_path) {
    try {
        const arr = fs.readdirSync(_path);
        for (const value of arr) await readdir(path.join(_path, value));
    } catch(e) {
        await readfile(_path);
    }
}