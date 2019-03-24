const { Parser } = require('acorn');

const JStoASTParser = Parser.extend(
    require("acorn-jsx")(),
    require("acorn-bigint")
);

const {
    shouldSkipByType,
    shouldSkipByParentType,
    shouldSkipField
} = require('./utils.js');

class FileProcessor {
    constructor(fileName) {
        this.fileName = fileName;
        this.types = {};
        this.num_of_lines = 0;
        this.num_of_empty_lines = 0;
        this.num_of_lines_with_comments = 0;
        this.num_of_logic_lines = 0;
        this.file = '';
    }

    run(shouldShowTypes) {
        return new Promise((resolve) => {
            const lineReader = require('readline').createInterface({
                input: require('fs').createReadStream(this.fileName)
            });
    
            let _is_multiline_comment = false;
            
            lineReader.on('line', (_line) => {
                this.file += _line + '\n';
                let line = _line.trim();
                this.num_of_lines++;
                this.num_of_empty_lines += +(!line.length);
    
                _is_multiline_comment = this.processCommentedLine(line, _is_multiline_comment);
            });
            
            lineReader.on('close', () => {
                if (this.num_of_empty_lines > 0.25 * this.num_of_lines) this.num_of_empty_lines = Math.round(0.25 * this.num_of_lines);
            
                const parsedFile = JStoASTParser.parse(this.file);
            
                this.countTypes(parsedFile);
            
                for (const value of Object.values(this.types)) this.num_of_logic_lines += value;
                // this.printStats(shouldShowTypes);

                resolve({
                    num_of_lines : this.num_of_lines,
                    num_of_empty_lines : this.num_of_empty_lines,
                    num_of_phisic_lines : this.phisicLines(),
                    num_of_logic_lines  : this.num_of_logic_lines,
                    num_of_lines_with_comments : this.num_of_lines_with_comments,
                    F : Number(this.num_of_lines_with_comments / this.num_of_lines).toFixed(2)
                });
            });
        });
    }

    printStats(shouldShowTypes = false) {
        console.log(''.padStart(50, '-'));
        console.log('FILE: ', this.fileName);
        console.log('NUMBER OF LINES: ', this.num_of_lines);
        console.log('NUMBER OF EMPTY LINES: ', this.num_of_empty_lines);
        console.log('NUMBER OF PHISIC LINES (KLOC): ', this.phisicLines());
        console.log('NUMBER OF LOGIC LINES (SLOC): ', this.num_of_logic_lines);
        console.log('NUMBER OF LINES WITH COMMENTS: ', this.num_of_lines_with_comments);
        console.log('F = ', Number(this.num_of_lines_with_comments / this.num_of_lines).toFixed(2));
        console.log(''.padStart(50, '-'));
        if (shouldShowTypes) console.log(this.types);
        console.log(''.padStart(50, '-'));
    }

    phisicLines() {
        return this.num_of_lines - this.num_of_empty_lines - this.num_of_lines_with_comments;
    }

    processCommentedLine(line, _is_multiline_comment) {
        if (line.indexOf('/*') !== -1 && line.indexOf('*/') !== -1) {
            if (line.indexOf('/*') < line.indexOf('*/')) {
                this.num_of_lines_with_comments++;
            } else if (line.indexOf('/*') > line.indexOf('*/')) {
                this.num_of_lines_with_comments++;
            }
        } else if (line.indexOf('/*') !== -1 && line.indexOf('*/') === -1) {
            this.num_of_lines_with_comments++;
            _is_multiline_comment = true;
        } else if (line.indexOf('/*') === -1 && line.indexOf('*/') !== -1 && _is_multiline_comment) {
            this.num_of_lines_with_comments++;
            _is_multiline_comment = false;
        } else if (line.startsWith('*') && _is_multiline_comment) {
            this.num_of_lines_with_comments++;
        } else if (line.indexOf('//') !== -1) {
            this.num_of_lines_with_comments++;
        }
    }

    countTypes(obj, parentType) {
        if (!obj) return;
        if (Array.isArray(obj)) {
            for (const value of obj) {
                this.countTypes(value, parentType);
            }
        } else if (typeof obj === 'object') {
            const type = obj.type;
            for (const [ key, value ] of Object.entries(obj)) {
                if (shouldSkipField(parentType, key)) continue;
                if (key === 'type') {
                    if (shouldSkipByType(type)) continue;
                    else if (shouldSkipByParentType(parentType, type)) continue;

                    if (this.types[value]) this.types[value]++;
                    else this.types[value] = 1;
                } else {
                    this.countTypes(value, type);
                }
            }
        }
    }
}

module.exports = FileProcessor;
