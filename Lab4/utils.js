function shouldSkipByType(type) {
    const SKIP_STATEMENTS = [ 'Literal', 'Identifier', 'Program', 'VariableDeclarator', 'MemberExpression', 'ObjectExpression', 'Property', 'ExpressionStatement' ];

    return !!SKIP_STATEMENTS.includes(type);
}

function shouldSkipByParentType(parentType, type) {
    const SKIP_STATEMENTS = [
        { parentType: 'ForStatement', type: 'BlockStatement' },
        { parentType: 'DoWhileStatement', type: 'BlockStatement' },
        { parentType: 'WhileStatement', type: 'BlockStatement' },
    ];

    return !!SKIP_STATEMENTS.find(i => i.parentType === parentType && i.type === type);
}

function shouldSkipField(parentType, field) {
    const SKIP_STATEMENTS = [
        { parentType: 'ForStatement', field: 'init' },
        { parentType: 'ForStatement', field: 'test' },
        { parentType: 'ForStatement', field: 'update' },
    ];

    return !!SKIP_STATEMENTS.find(i => i.parentType === parentType && i.field === field);
}

module.exports = {
    shouldSkipByType,
    shouldSkipByParentType,
    shouldSkipField
};