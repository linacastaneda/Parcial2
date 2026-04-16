# Generated from gramatica.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,26,131,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,1,0,5,0,34,8,0,10,0,12,0,37,9,0,1,0,1,0,1,1,
        1,1,1,1,1,1,3,1,45,8,1,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,4,1,4,1,
        4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,6,1,6,1,6,3,6,68,8,6,1,7,1,7,1,7,
        1,7,1,8,1,8,1,8,5,8,77,8,8,10,8,12,8,80,9,8,1,8,3,8,83,8,8,1,9,1,
        9,1,9,1,9,1,10,1,10,1,10,5,10,92,8,10,10,10,12,10,95,9,10,1,11,1,
        11,1,11,1,11,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,
        12,3,12,112,8,12,1,12,1,12,1,12,1,12,1,12,1,12,5,12,120,8,12,10,
        12,12,12,123,9,12,1,13,1,13,1,14,1,14,1,15,1,15,1,15,0,1,24,16,0,
        2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,0,2,2,0,5,5,8,12,1,0,22,
        24,126,0,35,1,0,0,0,2,44,1,0,0,0,4,46,1,0,0,0,6,50,1,0,0,0,8,54,
        1,0,0,0,10,60,1,0,0,0,12,67,1,0,0,0,14,69,1,0,0,0,16,82,1,0,0,0,
        18,84,1,0,0,0,20,88,1,0,0,0,22,96,1,0,0,0,24,111,1,0,0,0,26,124,
        1,0,0,0,28,126,1,0,0,0,30,128,1,0,0,0,32,34,3,2,1,0,33,32,1,0,0,
        0,34,37,1,0,0,0,35,33,1,0,0,0,35,36,1,0,0,0,36,38,1,0,0,0,37,35,
        1,0,0,0,38,39,5,0,0,1,39,1,1,0,0,0,40,45,3,4,2,0,41,45,3,6,3,0,42,
        45,3,8,4,0,43,45,3,10,5,0,44,40,1,0,0,0,44,41,1,0,0,0,44,42,1,0,
        0,0,44,43,1,0,0,0,45,3,1,0,0,0,46,47,5,13,0,0,47,48,3,30,15,0,48,
        49,3,14,7,0,49,5,1,0,0,0,50,51,5,14,0,0,51,52,3,30,15,0,52,53,3,
        12,6,0,53,7,1,0,0,0,54,55,5,15,0,0,55,56,3,30,15,0,56,57,5,17,0,
        0,57,58,3,20,10,0,58,59,3,12,6,0,59,9,1,0,0,0,60,61,5,16,0,0,61,
        62,3,30,15,0,62,63,3,12,6,0,63,11,1,0,0,0,64,65,5,18,0,0,65,68,3,
        24,12,0,66,68,1,0,0,0,67,64,1,0,0,0,67,66,1,0,0,0,68,13,1,0,0,0,
        69,70,5,1,0,0,70,71,3,16,8,0,71,72,5,2,0,0,72,15,1,0,0,0,73,78,3,
        18,9,0,74,75,5,3,0,0,75,77,3,18,9,0,76,74,1,0,0,0,77,80,1,0,0,0,
        78,76,1,0,0,0,78,79,1,0,0,0,79,83,1,0,0,0,80,78,1,0,0,0,81,83,1,
        0,0,0,82,73,1,0,0,0,82,81,1,0,0,0,83,17,1,0,0,0,84,85,3,30,15,0,
        85,86,5,4,0,0,86,87,3,28,14,0,87,19,1,0,0,0,88,93,3,22,11,0,89,90,
        5,3,0,0,90,92,3,22,11,0,91,89,1,0,0,0,92,95,1,0,0,0,93,91,1,0,0,
        0,93,94,1,0,0,0,94,21,1,0,0,0,95,93,1,0,0,0,96,97,3,30,15,0,97,98,
        5,5,0,0,98,99,3,28,14,0,99,23,1,0,0,0,100,101,6,12,-1,0,101,102,
        5,21,0,0,102,112,3,24,12,5,103,104,3,30,15,0,104,105,3,26,13,0,105,
        106,3,28,14,0,106,112,1,0,0,0,107,108,5,6,0,0,108,109,3,24,12,0,
        109,110,5,7,0,0,110,112,1,0,0,0,111,100,1,0,0,0,111,103,1,0,0,0,
        111,107,1,0,0,0,112,121,1,0,0,0,113,114,10,4,0,0,114,115,5,19,0,
        0,115,120,3,24,12,5,116,117,10,3,0,0,117,118,5,20,0,0,118,120,3,
        24,12,4,119,113,1,0,0,0,119,116,1,0,0,0,120,123,1,0,0,0,121,119,
        1,0,0,0,121,122,1,0,0,0,122,25,1,0,0,0,123,121,1,0,0,0,124,125,7,
        0,0,0,125,27,1,0,0,0,126,127,7,1,0,0,127,29,1,0,0,0,128,129,5,25,
        0,0,129,31,1,0,0,0,9,35,44,67,78,82,93,111,119,121
    ]

class gramaticaParser ( Parser ):

    grammarFileName = "gramatica.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'{'", "'}'", "','", "':'", "'='", "'('", 
                     "')'", "'>'", "'<'", "'>='", "'<='", "'!='", "'CREATE'", 
                     "'READ'", "'UPDATE'", "'DELETE'", "'SET'", "'WHERE'", 
                     "'AND'", "'OR'", "'NOT'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "CREATE", "READ", "UPDATE", "DELETE", 
                      "SET", "WHERE", "AND", "OR", "NOT", "BOOLEANO", "CADENA", 
                      "NUMERO", "ID", "WS" ]

    RULE_programa = 0
    RULE_sentencia = 1
    RULE_create = 2
    RULE_read = 3
    RULE_update = 4
    RULE_delete = 5
    RULE_whereOpcional = 6
    RULE_documento = 7
    RULE_listaCampos = 8
    RULE_campo = 9
    RULE_asignaciones = 10
    RULE_asignacion = 11
    RULE_condicion = 12
    RULE_operador = 13
    RULE_valor = 14
    RULE_identificador = 15

    ruleNames =  [ "programa", "sentencia", "create", "read", "update", 
                   "delete", "whereOpcional", "documento", "listaCampos", 
                   "campo", "asignaciones", "asignacion", "condicion", "operador", 
                   "valor", "identificador" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    CREATE=13
    READ=14
    UPDATE=15
    DELETE=16
    SET=17
    WHERE=18
    AND=19
    OR=20
    NOT=21
    BOOLEANO=22
    CADENA=23
    NUMERO=24
    ID=25
    WS=26

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(gramaticaParser.EOF, 0)

        def sentencia(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.SentenciaContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.SentenciaContext,i)


        def getRuleIndex(self):
            return gramaticaParser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)




    def programa(self):

        localctx = gramaticaParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 122880) != 0):
                self.state = 32
                self.sentencia()
                self.state = 37
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 38
            self.match(gramaticaParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SentenciaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def create(self):
            return self.getTypedRuleContext(gramaticaParser.CreateContext,0)


        def read(self):
            return self.getTypedRuleContext(gramaticaParser.ReadContext,0)


        def update(self):
            return self.getTypedRuleContext(gramaticaParser.UpdateContext,0)


        def delete(self):
            return self.getTypedRuleContext(gramaticaParser.DeleteContext,0)


        def getRuleIndex(self):
            return gramaticaParser.RULE_sentencia

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSentencia" ):
                listener.enterSentencia(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSentencia" ):
                listener.exitSentencia(self)




    def sentencia(self):

        localctx = gramaticaParser.SentenciaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_sentencia)
        try:
            self.state = 44
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13]:
                self.enterOuterAlt(localctx, 1)
                self.state = 40
                self.create()
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 2)
                self.state = 41
                self.read()
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 3)
                self.state = 42
                self.update()
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 4)
                self.state = 43
                self.delete()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CreateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CREATE(self):
            return self.getToken(gramaticaParser.CREATE, 0)

        def identificador(self):
            return self.getTypedRuleContext(gramaticaParser.IdentificadorContext,0)


        def documento(self):
            return self.getTypedRuleContext(gramaticaParser.DocumentoContext,0)


        def getRuleIndex(self):
            return gramaticaParser.RULE_create

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCreate" ):
                listener.enterCreate(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCreate" ):
                listener.exitCreate(self)




    def create(self):

        localctx = gramaticaParser.CreateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_create)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self.match(gramaticaParser.CREATE)
            self.state = 47
            self.identificador()
            self.state = 48
            self.documento()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReadContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def READ(self):
            return self.getToken(gramaticaParser.READ, 0)

        def identificador(self):
            return self.getTypedRuleContext(gramaticaParser.IdentificadorContext,0)


        def whereOpcional(self):
            return self.getTypedRuleContext(gramaticaParser.WhereOpcionalContext,0)


        def getRuleIndex(self):
            return gramaticaParser.RULE_read

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRead" ):
                listener.enterRead(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRead" ):
                listener.exitRead(self)




    def read(self):

        localctx = gramaticaParser.ReadContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_read)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self.match(gramaticaParser.READ)
            self.state = 51
            self.identificador()
            self.state = 52
            self.whereOpcional()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UpdateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def UPDATE(self):
            return self.getToken(gramaticaParser.UPDATE, 0)

        def identificador(self):
            return self.getTypedRuleContext(gramaticaParser.IdentificadorContext,0)


        def SET(self):
            return self.getToken(gramaticaParser.SET, 0)

        def asignaciones(self):
            return self.getTypedRuleContext(gramaticaParser.AsignacionesContext,0)


        def whereOpcional(self):
            return self.getTypedRuleContext(gramaticaParser.WhereOpcionalContext,0)


        def getRuleIndex(self):
            return gramaticaParser.RULE_update

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUpdate" ):
                listener.enterUpdate(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUpdate" ):
                listener.exitUpdate(self)




    def update(self):

        localctx = gramaticaParser.UpdateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_update)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self.match(gramaticaParser.UPDATE)
            self.state = 55
            self.identificador()
            self.state = 56
            self.match(gramaticaParser.SET)
            self.state = 57
            self.asignaciones()
            self.state = 58
            self.whereOpcional()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeleteContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DELETE(self):
            return self.getToken(gramaticaParser.DELETE, 0)

        def identificador(self):
            return self.getTypedRuleContext(gramaticaParser.IdentificadorContext,0)


        def whereOpcional(self):
            return self.getTypedRuleContext(gramaticaParser.WhereOpcionalContext,0)


        def getRuleIndex(self):
            return gramaticaParser.RULE_delete

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDelete" ):
                listener.enterDelete(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDelete" ):
                listener.exitDelete(self)




    def delete(self):

        localctx = gramaticaParser.DeleteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_delete)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self.match(gramaticaParser.DELETE)
            self.state = 61
            self.identificador()
            self.state = 62
            self.whereOpcional()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhereOpcionalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHERE(self):
            return self.getToken(gramaticaParser.WHERE, 0)

        def condicion(self):
            return self.getTypedRuleContext(gramaticaParser.CondicionContext,0)


        def getRuleIndex(self):
            return gramaticaParser.RULE_whereOpcional

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhereOpcional" ):
                listener.enterWhereOpcional(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhereOpcional" ):
                listener.exitWhereOpcional(self)




    def whereOpcional(self):

        localctx = gramaticaParser.WhereOpcionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_whereOpcional)
        try:
            self.state = 67
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [18]:
                self.enterOuterAlt(localctx, 1)
                self.state = 64
                self.match(gramaticaParser.WHERE)
                self.state = 65
                self.condicion(0)
                pass
            elif token in [-1, 13, 14, 15, 16]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DocumentoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def listaCampos(self):
            return self.getTypedRuleContext(gramaticaParser.ListaCamposContext,0)


        def getRuleIndex(self):
            return gramaticaParser.RULE_documento

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDocumento" ):
                listener.enterDocumento(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDocumento" ):
                listener.exitDocumento(self)




    def documento(self):

        localctx = gramaticaParser.DocumentoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_documento)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self.match(gramaticaParser.T__0)
            self.state = 70
            self.listaCampos()
            self.state = 71
            self.match(gramaticaParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListaCamposContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def campo(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.CampoContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.CampoContext,i)


        def getRuleIndex(self):
            return gramaticaParser.RULE_listaCampos

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListaCampos" ):
                listener.enterListaCampos(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListaCampos" ):
                listener.exitListaCampos(self)




    def listaCampos(self):

        localctx = gramaticaParser.ListaCamposContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_listaCampos)
        self._la = 0 # Token type
        try:
            self.state = 82
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [25]:
                self.enterOuterAlt(localctx, 1)
                self.state = 73
                self.campo()
                self.state = 78
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==3:
                    self.state = 74
                    self.match(gramaticaParser.T__2)
                    self.state = 75
                    self.campo()
                    self.state = 80
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CampoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identificador(self):
            return self.getTypedRuleContext(gramaticaParser.IdentificadorContext,0)


        def valor(self):
            return self.getTypedRuleContext(gramaticaParser.ValorContext,0)


        def getRuleIndex(self):
            return gramaticaParser.RULE_campo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCampo" ):
                listener.enterCampo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCampo" ):
                listener.exitCampo(self)




    def campo(self):

        localctx = gramaticaParser.CampoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_campo)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self.identificador()
            self.state = 85
            self.match(gramaticaParser.T__3)
            self.state = 86
            self.valor()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AsignacionesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def asignacion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.AsignacionContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.AsignacionContext,i)


        def getRuleIndex(self):
            return gramaticaParser.RULE_asignaciones

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAsignaciones" ):
                listener.enterAsignaciones(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAsignaciones" ):
                listener.exitAsignaciones(self)




    def asignaciones(self):

        localctx = gramaticaParser.AsignacionesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_asignaciones)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            self.asignacion()
            self.state = 93
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3:
                self.state = 89
                self.match(gramaticaParser.T__2)
                self.state = 90
                self.asignacion()
                self.state = 95
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AsignacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identificador(self):
            return self.getTypedRuleContext(gramaticaParser.IdentificadorContext,0)


        def valor(self):
            return self.getTypedRuleContext(gramaticaParser.ValorContext,0)


        def getRuleIndex(self):
            return gramaticaParser.RULE_asignacion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAsignacion" ):
                listener.enterAsignacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAsignacion" ):
                listener.exitAsignacion(self)




    def asignacion(self):

        localctx = gramaticaParser.AsignacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_asignacion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self.identificador()
            self.state = 97
            self.match(gramaticaParser.T__4)
            self.state = 98
            self.valor()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CondicionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return gramaticaParser.RULE_condicion

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class CondSimpleContext(CondicionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramaticaParser.CondicionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def identificador(self):
            return self.getTypedRuleContext(gramaticaParser.IdentificadorContext,0)

        def operador(self):
            return self.getTypedRuleContext(gramaticaParser.OperadorContext,0)

        def valor(self):
            return self.getTypedRuleContext(gramaticaParser.ValorContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondSimple" ):
                listener.enterCondSimple(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondSimple" ):
                listener.exitCondSimple(self)


    class CondAndContext(CondicionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramaticaParser.CondicionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def condicion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.CondicionContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.CondicionContext,i)

        def AND(self):
            return self.getToken(gramaticaParser.AND, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondAnd" ):
                listener.enterCondAnd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondAnd" ):
                listener.exitCondAnd(self)


    class CondOrContext(CondicionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramaticaParser.CondicionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def condicion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.CondicionContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.CondicionContext,i)

        def OR(self):
            return self.getToken(gramaticaParser.OR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondOr" ):
                listener.enterCondOr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondOr" ):
                listener.exitCondOr(self)


    class CondAgrupadaContext(CondicionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramaticaParser.CondicionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def condicion(self):
            return self.getTypedRuleContext(gramaticaParser.CondicionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondAgrupada" ):
                listener.enterCondAgrupada(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondAgrupada" ):
                listener.exitCondAgrupada(self)


    class CondNotContext(CondicionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramaticaParser.CondicionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(gramaticaParser.NOT, 0)
        def condicion(self):
            return self.getTypedRuleContext(gramaticaParser.CondicionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondNot" ):
                listener.enterCondNot(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondNot" ):
                listener.exitCondNot(self)



    def condicion(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = gramaticaParser.CondicionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 24
        self.enterRecursionRule(localctx, 24, self.RULE_condicion, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [21]:
                localctx = gramaticaParser.CondNotContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 101
                self.match(gramaticaParser.NOT)
                self.state = 102
                self.condicion(5)
                pass
            elif token in [25]:
                localctx = gramaticaParser.CondSimpleContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 103
                self.identificador()
                self.state = 104
                self.operador()
                self.state = 105
                self.valor()
                pass
            elif token in [6]:
                localctx = gramaticaParser.CondAgrupadaContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 107
                self.match(gramaticaParser.T__5)
                self.state = 108
                self.condicion(0)
                self.state = 109
                self.match(gramaticaParser.T__6)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 121
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 119
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                    if la_ == 1:
                        localctx = gramaticaParser.CondAndContext(self, gramaticaParser.CondicionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_condicion)
                        self.state = 113
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 114
                        self.match(gramaticaParser.AND)
                        self.state = 115
                        self.condicion(5)
                        pass

                    elif la_ == 2:
                        localctx = gramaticaParser.CondOrContext(self, gramaticaParser.CondicionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_condicion)
                        self.state = 116
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 117
                        self.match(gramaticaParser.OR)
                        self.state = 118
                        self.condicion(4)
                        pass

             
                self.state = 123
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class OperadorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return gramaticaParser.RULE_operador

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperador" ):
                listener.enterOperador(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperador" ):
                listener.exitOperador(self)




    def operador(self):

        localctx = gramaticaParser.OperadorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_operador)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 124
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 7968) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CADENA(self):
            return self.getToken(gramaticaParser.CADENA, 0)

        def NUMERO(self):
            return self.getToken(gramaticaParser.NUMERO, 0)

        def BOOLEANO(self):
            return self.getToken(gramaticaParser.BOOLEANO, 0)

        def getRuleIndex(self):
            return gramaticaParser.RULE_valor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValor" ):
                listener.enterValor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValor" ):
                listener.exitValor(self)




    def valor(self):

        localctx = gramaticaParser.ValorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_valor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 126
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 29360128) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdentificadorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(gramaticaParser.ID, 0)

        def getRuleIndex(self):
            return gramaticaParser.RULE_identificador

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentificador" ):
                listener.enterIdentificador(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentificador" ):
                listener.exitIdentificador(self)




    def identificador(self):

        localctx = gramaticaParser.IdentificadorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_identificador)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 128
            self.match(gramaticaParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[12] = self.condicion_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def condicion_sempred(self, localctx:CondicionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 3)
         




