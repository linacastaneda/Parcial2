grammar gramatica;

// ─── REGLAS SINTÁCTICAS ───────────────────────────────────────────

programa
    : sentencia* EOF
    ;

sentencia
    : create
    | read
    | update
    | delete
    ;

create
    : CREATE identificador documento
    ;

read
    : READ identificador whereOpcional
    ;

update
    : UPDATE identificador SET asignaciones whereOpcional
    ;

delete
    : DELETE identificador whereOpcional
    ;

whereOpcional
    : WHERE condicion
    |
    ;

documento
    : '{' listaCampos '}'
    ;

listaCampos
    : campo (',' campo)*
    |
    ;

campo
    : identificador ':' valor
    ;

asignaciones
    : asignacion (',' asignacion)*
    ;

asignacion
    : identificador '=' valor
    ;

// Condición con precedencia: NOT > AND > OR
condicion
    : NOT condicion                          # condNot
    | condicion AND condicion                # condAnd
    | condicion OR condicion                 # condOr
    | identificador operador valor           # condSimple
    | '(' condicion ')'                      # condAgrupada
    ;

operador
    : '='
    | '>'
    | '<'
    | '>='
    | '<='
    | '!='
    ;

valor
    : CADENA
    | NUMERO
    | BOOLEANO
    ;

identificador
    : ID
    ;

// ─── REGLAS LÉXICAS ──────────────────────────────────────────────

CREATE  : 'CREATE' ;
READ    : 'READ' ;
UPDATE  : 'UPDATE' ;
DELETE  : 'DELETE' ;
SET     : 'SET' ;
WHERE   : 'WHERE' ;
AND     : 'AND' ;
OR      : 'OR' ;
NOT     : 'NOT' ;

BOOLEANO : 'true' | 'false' ;

CADENA  : '"' (~["\r\n])* '"' ;

NUMERO  : [0-9]+ ('.' [0-9]+)? ;

ID      : [a-zA-Z_] [a-zA-Z0-9_]* ;

WS      : [ \t\r\n]+ -> skip ;