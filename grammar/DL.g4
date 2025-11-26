grammar DL;

// ======================================================
//                 PARSER RULES (SINTAXIS)
// ======================================================

program: statement* EOF;

statement
    : varDeclaration SEMI      # StatVarDecl
    | assignment SEMI          # StatAssign
    | functionDef              # StatFuncDef
    // Eliminamos methodCall SEMI porque StatExpr ya lo cubre
    | ifStatement              # StatIf
    | whileStatement           # StatWhile
    | forStatement             # StatFor
    | returnStmt SEMI          # StatReturn
    | printStmt SEMI           # StatPrint
    | plotStmt SEMI            # StatPlot
    | expression SEMI          # StatExpr        // Cubre: model.add(...); y 5+5;
    ;

// --- DECLARACIONES Y ASIGNACIONES ---
varDeclaration
    : 'var' ID '=' expression
    ;

assignment
    : expression '=' expression
    ;

// --- FUNCIONES ---
functionDef
    : 'def' ID '(' (ID (',' ID)*)? ')' block
    ;

block
    : '{' statement* '}'
    ;

// --- CONTROL DE FLUJO ---
ifStatement
    : 'if' '(' expression ')' block ('else' block)?
    ;

whileStatement
    : 'while' '(' expression ')' block
    ;

forStatement
    : 'for' '(' ID 'in' expression ')' block
    ;

returnStmt
    : 'return' expression?
    ;

// --- FUNCIONES NATIVAS ---
printStmt
    : 'print' '(' expression ')'
    ;

plotStmt
    : 'plot' '(' expression (',' expression)? ')'
    ;

// (Regla methodCall ELIMINADA para evitar recursividad mutua)

// ======================================================
//                 EXPRESIONES (La Lógica)
// ======================================================

expression
    // Sintaxis de llamada a método (MOVIDA AQUÍ PARA ARREGLAR RECURSIVIDAD)
    // Esto es recursividad directa por izquierda, ANTLR4 sí la soporta.
    : expression '.' ID '(' (expression (',' expression)*)? ')' # ExprMethodCall

    | expression '[' expression ']'        # ExprIndex
    | expression '[' expression? ':' expression? ']' # ExprSlice
    | ID '(' (expression (',' expression)*)? ')' # ExprFuncCall
    | expression '^' expression            # ExprPower
    | '-' expression                       # ExprUnaryMinus
    | '!' expression                       # ExprNot
    | expression ('*' | '/' | '%') expression # ExprMultDiv
    | expression ('+' | '-') expression    # ExprAddSub
    | expression ('>' | '<' | '>=' | '<=') expression # ExprRelational
    | expression ('==' | '!=') expression  # ExprEquality
    | expression '&&' expression           # ExprAnd
    | expression '||' expression           # ExprOr
    | atom                                 # ExprAtom
    ;

atom
    : '(' expression ')'                   # AtomParen
    | ID                                   # AtomId
    | number                               # AtomNumber
    | STRING                               # AtomString
    | boolean                              # AtomBool
    | list                                 # AtomList
    | newExpr                              # AtomNew
    ;

list
    : '[' (expression (',' expression)*)? ']'
    ;

newExpr
    : 'new' ID '(' (expression (',' expression)*)? ')'
    ;

number
    : INT
    | FLOAT
    ;

boolean
    : TRUE | FALSE
    ;

// ======================================================
//                 LEXER RULES (TOKENS)
// ======================================================

IF      : 'if';
ELSE    : 'else';
WHILE   : 'while';
FOR     : 'for';
IN      : 'in';
DEF     : 'def';
RETURN  : 'return';
VAR     : 'var';
PRINT   : 'print';
PLOT    : 'plot';
NEW     : 'new';
TRUE    : 'true';
FALSE   : 'false';

ID      : [a-zA-Z_] [a-zA-Z_0-9]*;

INT     : [0-9]+;
FLOAT   : [0-9]+ '.' [0-9]+;
STRING  : '"' .*? '"';

// Operadores
PLUS    : '+';
MINUS   : '-';
MULT    : '*';
DIV     : '/';
MOD     : '%';
POW     : '^';
EQ      : '==';
NEQ     : '!=';
GT      : '>';
LT      : '<';
GTE     : '>=';
LTE     : '<=';
AND     : '&&';
OR      : '||';
NOT     : '!';
ASSIGN  : '=';
DOT     : '.';
COLON   : ':';

LPAREN  : '(';
RPAREN  : ')';
LBRACE  : '{';
RBRACE  : '}';
LBRACK  : '[';
RBRACK  : ']';
SEMI    : ';';
COMMA   : ',';

WS      : [ \t\r\n]+ -> skip;
COMMENT : '//' ~[\r\n]* -> skip;
BLOCK_COMMENT : '/*' .*? '*/' -> skip;