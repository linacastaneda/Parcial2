# Generated from gramatica.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .gramaticaParser import gramaticaParser
else:
    from gramaticaParser import gramaticaParser

# This class defines a complete listener for a parse tree produced by gramaticaParser.
class gramaticaListener(ParseTreeListener):

    # Enter a parse tree produced by gramaticaParser#programa.
    def enterPrograma(self, ctx:gramaticaParser.ProgramaContext):
        pass

    # Exit a parse tree produced by gramaticaParser#programa.
    def exitPrograma(self, ctx:gramaticaParser.ProgramaContext):
        pass


    # Enter a parse tree produced by gramaticaParser#sentencia.
    def enterSentencia(self, ctx:gramaticaParser.SentenciaContext):
        pass

    # Exit a parse tree produced by gramaticaParser#sentencia.
    def exitSentencia(self, ctx:gramaticaParser.SentenciaContext):
        pass


    # Enter a parse tree produced by gramaticaParser#create.
    def enterCreate(self, ctx:gramaticaParser.CreateContext):
        pass

    # Exit a parse tree produced by gramaticaParser#create.
    def exitCreate(self, ctx:gramaticaParser.CreateContext):
        pass


    # Enter a parse tree produced by gramaticaParser#read.
    def enterRead(self, ctx:gramaticaParser.ReadContext):
        pass

    # Exit a parse tree produced by gramaticaParser#read.
    def exitRead(self, ctx:gramaticaParser.ReadContext):
        pass


    # Enter a parse tree produced by gramaticaParser#update.
    def enterUpdate(self, ctx:gramaticaParser.UpdateContext):
        pass

    # Exit a parse tree produced by gramaticaParser#update.
    def exitUpdate(self, ctx:gramaticaParser.UpdateContext):
        pass


    # Enter a parse tree produced by gramaticaParser#delete.
    def enterDelete(self, ctx:gramaticaParser.DeleteContext):
        pass

    # Exit a parse tree produced by gramaticaParser#delete.
    def exitDelete(self, ctx:gramaticaParser.DeleteContext):
        pass


    # Enter a parse tree produced by gramaticaParser#whereOpcional.
    def enterWhereOpcional(self, ctx:gramaticaParser.WhereOpcionalContext):
        pass

    # Exit a parse tree produced by gramaticaParser#whereOpcional.
    def exitWhereOpcional(self, ctx:gramaticaParser.WhereOpcionalContext):
        pass


    # Enter a parse tree produced by gramaticaParser#documento.
    def enterDocumento(self, ctx:gramaticaParser.DocumentoContext):
        pass

    # Exit a parse tree produced by gramaticaParser#documento.
    def exitDocumento(self, ctx:gramaticaParser.DocumentoContext):
        pass


    # Enter a parse tree produced by gramaticaParser#listaCampos.
    def enterListaCampos(self, ctx:gramaticaParser.ListaCamposContext):
        pass

    # Exit a parse tree produced by gramaticaParser#listaCampos.
    def exitListaCampos(self, ctx:gramaticaParser.ListaCamposContext):
        pass


    # Enter a parse tree produced by gramaticaParser#campo.
    def enterCampo(self, ctx:gramaticaParser.CampoContext):
        pass

    # Exit a parse tree produced by gramaticaParser#campo.
    def exitCampo(self, ctx:gramaticaParser.CampoContext):
        pass


    # Enter a parse tree produced by gramaticaParser#asignaciones.
    def enterAsignaciones(self, ctx:gramaticaParser.AsignacionesContext):
        pass

    # Exit a parse tree produced by gramaticaParser#asignaciones.
    def exitAsignaciones(self, ctx:gramaticaParser.AsignacionesContext):
        pass


    # Enter a parse tree produced by gramaticaParser#asignacion.
    def enterAsignacion(self, ctx:gramaticaParser.AsignacionContext):
        pass

    # Exit a parse tree produced by gramaticaParser#asignacion.
    def exitAsignacion(self, ctx:gramaticaParser.AsignacionContext):
        pass


    # Enter a parse tree produced by gramaticaParser#condSimple.
    def enterCondSimple(self, ctx:gramaticaParser.CondSimpleContext):
        pass

    # Exit a parse tree produced by gramaticaParser#condSimple.
    def exitCondSimple(self, ctx:gramaticaParser.CondSimpleContext):
        pass


    # Enter a parse tree produced by gramaticaParser#condAnd.
    def enterCondAnd(self, ctx:gramaticaParser.CondAndContext):
        pass

    # Exit a parse tree produced by gramaticaParser#condAnd.
    def exitCondAnd(self, ctx:gramaticaParser.CondAndContext):
        pass


    # Enter a parse tree produced by gramaticaParser#condOr.
    def enterCondOr(self, ctx:gramaticaParser.CondOrContext):
        pass

    # Exit a parse tree produced by gramaticaParser#condOr.
    def exitCondOr(self, ctx:gramaticaParser.CondOrContext):
        pass


    # Enter a parse tree produced by gramaticaParser#condAgrupada.
    def enterCondAgrupada(self, ctx:gramaticaParser.CondAgrupadaContext):
        pass

    # Exit a parse tree produced by gramaticaParser#condAgrupada.
    def exitCondAgrupada(self, ctx:gramaticaParser.CondAgrupadaContext):
        pass


    # Enter a parse tree produced by gramaticaParser#condNot.
    def enterCondNot(self, ctx:gramaticaParser.CondNotContext):
        pass

    # Exit a parse tree produced by gramaticaParser#condNot.
    def exitCondNot(self, ctx:gramaticaParser.CondNotContext):
        pass


    # Enter a parse tree produced by gramaticaParser#operador.
    def enterOperador(self, ctx:gramaticaParser.OperadorContext):
        pass

    # Exit a parse tree produced by gramaticaParser#operador.
    def exitOperador(self, ctx:gramaticaParser.OperadorContext):
        pass


    # Enter a parse tree produced by gramaticaParser#valor.
    def enterValor(self, ctx:gramaticaParser.ValorContext):
        pass

    # Exit a parse tree produced by gramaticaParser#valor.
    def exitValor(self, ctx:gramaticaParser.ValorContext):
        pass


    # Enter a parse tree produced by gramaticaParser#identificador.
    def enterIdentificador(self, ctx:gramaticaParser.IdentificadorContext):
        pass

    # Exit a parse tree produced by gramaticaParser#identificador.
    def exitIdentificador(self, ctx:gramaticaParser.IdentificadorContext):
        pass



del gramaticaParser