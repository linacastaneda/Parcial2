// Generated from /home/lina/parcial2/Punto2/gramatica.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class gramaticaParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, CREATE=13, READ=14, UPDATE=15, DELETE=16, 
		SET=17, WHERE=18, AND=19, OR=20, NOT=21, BOOLEANO=22, CADENA=23, NUMERO=24, 
		ID=25, WS=26;
	public static final int
		RULE_programa = 0, RULE_sentencia = 1, RULE_create = 2, RULE_read = 3, 
		RULE_update = 4, RULE_delete = 5, RULE_whereOpcional = 6, RULE_documento = 7, 
		RULE_listaCampos = 8, RULE_campo = 9, RULE_asignaciones = 10, RULE_asignacion = 11, 
		RULE_condicion = 12, RULE_operador = 13, RULE_valor = 14, RULE_identificador = 15;
	private static String[] makeRuleNames() {
		return new String[] {
			"programa", "sentencia", "create", "read", "update", "delete", "whereOpcional", 
			"documento", "listaCampos", "campo", "asignaciones", "asignacion", "condicion", 
			"operador", "valor", "identificador"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'{'", "'}'", "','", "':'", "'='", "'('", "')'", "'>'", "'<'", 
			"'>='", "'<='", "'!='", "'CREATE'", "'READ'", "'UPDATE'", "'DELETE'", 
			"'SET'", "'WHERE'", "'AND'", "'OR'", "'NOT'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, "CREATE", "READ", "UPDATE", "DELETE", "SET", "WHERE", "AND", "OR", 
			"NOT", "BOOLEANO", "CADENA", "NUMERO", "ID", "WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "gramatica.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public gramaticaParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProgramaContext extends ParserRuleContext {
		public TerminalNode EOF() { return getToken(gramaticaParser.EOF, 0); }
		public List<SentenciaContext> sentencia() {
			return getRuleContexts(SentenciaContext.class);
		}
		public SentenciaContext sentencia(int i) {
			return getRuleContext(SentenciaContext.class,i);
		}
		public ProgramaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_programa; }
	}

	public final ProgramaContext programa() throws RecognitionException {
		ProgramaContext _localctx = new ProgramaContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_programa);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(35);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 122880L) != 0)) {
				{
				{
				setState(32);
				sentencia();
				}
				}
				setState(37);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(38);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class SentenciaContext extends ParserRuleContext {
		public CreateContext create() {
			return getRuleContext(CreateContext.class,0);
		}
		public ReadContext read() {
			return getRuleContext(ReadContext.class,0);
		}
		public UpdateContext update() {
			return getRuleContext(UpdateContext.class,0);
		}
		public DeleteContext delete() {
			return getRuleContext(DeleteContext.class,0);
		}
		public SentenciaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_sentencia; }
	}

	public final SentenciaContext sentencia() throws RecognitionException {
		SentenciaContext _localctx = new SentenciaContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_sentencia);
		try {
			setState(44);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case CREATE:
				enterOuterAlt(_localctx, 1);
				{
				setState(40);
				create();
				}
				break;
			case READ:
				enterOuterAlt(_localctx, 2);
				{
				setState(41);
				read();
				}
				break;
			case UPDATE:
				enterOuterAlt(_localctx, 3);
				{
				setState(42);
				update();
				}
				break;
			case DELETE:
				enterOuterAlt(_localctx, 4);
				{
				setState(43);
				delete();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CreateContext extends ParserRuleContext {
		public TerminalNode CREATE() { return getToken(gramaticaParser.CREATE, 0); }
		public IdentificadorContext identificador() {
			return getRuleContext(IdentificadorContext.class,0);
		}
		public DocumentoContext documento() {
			return getRuleContext(DocumentoContext.class,0);
		}
		public CreateContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_create; }
	}

	public final CreateContext create() throws RecognitionException {
		CreateContext _localctx = new CreateContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_create);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(46);
			match(CREATE);
			setState(47);
			identificador();
			setState(48);
			documento();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ReadContext extends ParserRuleContext {
		public TerminalNode READ() { return getToken(gramaticaParser.READ, 0); }
		public IdentificadorContext identificador() {
			return getRuleContext(IdentificadorContext.class,0);
		}
		public WhereOpcionalContext whereOpcional() {
			return getRuleContext(WhereOpcionalContext.class,0);
		}
		public ReadContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_read; }
	}

	public final ReadContext read() throws RecognitionException {
		ReadContext _localctx = new ReadContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_read);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(50);
			match(READ);
			setState(51);
			identificador();
			setState(52);
			whereOpcional();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class UpdateContext extends ParserRuleContext {
		public TerminalNode UPDATE() { return getToken(gramaticaParser.UPDATE, 0); }
		public IdentificadorContext identificador() {
			return getRuleContext(IdentificadorContext.class,0);
		}
		public TerminalNode SET() { return getToken(gramaticaParser.SET, 0); }
		public AsignacionesContext asignaciones() {
			return getRuleContext(AsignacionesContext.class,0);
		}
		public WhereOpcionalContext whereOpcional() {
			return getRuleContext(WhereOpcionalContext.class,0);
		}
		public UpdateContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_update; }
	}

	public final UpdateContext update() throws RecognitionException {
		UpdateContext _localctx = new UpdateContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_update);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(54);
			match(UPDATE);
			setState(55);
			identificador();
			setState(56);
			match(SET);
			setState(57);
			asignaciones();
			setState(58);
			whereOpcional();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DeleteContext extends ParserRuleContext {
		public TerminalNode DELETE() { return getToken(gramaticaParser.DELETE, 0); }
		public IdentificadorContext identificador() {
			return getRuleContext(IdentificadorContext.class,0);
		}
		public WhereOpcionalContext whereOpcional() {
			return getRuleContext(WhereOpcionalContext.class,0);
		}
		public DeleteContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_delete; }
	}

	public final DeleteContext delete() throws RecognitionException {
		DeleteContext _localctx = new DeleteContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_delete);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(60);
			match(DELETE);
			setState(61);
			identificador();
			setState(62);
			whereOpcional();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class WhereOpcionalContext extends ParserRuleContext {
		public TerminalNode WHERE() { return getToken(gramaticaParser.WHERE, 0); }
		public CondicionContext condicion() {
			return getRuleContext(CondicionContext.class,0);
		}
		public WhereOpcionalContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_whereOpcional; }
	}

	public final WhereOpcionalContext whereOpcional() throws RecognitionException {
		WhereOpcionalContext _localctx = new WhereOpcionalContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_whereOpcional);
		try {
			setState(67);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case WHERE:
				enterOuterAlt(_localctx, 1);
				{
				setState(64);
				match(WHERE);
				setState(65);
				condicion(0);
				}
				break;
			case EOF:
			case CREATE:
			case READ:
			case UPDATE:
			case DELETE:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DocumentoContext extends ParserRuleContext {
		public ListaCamposContext listaCampos() {
			return getRuleContext(ListaCamposContext.class,0);
		}
		public DocumentoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_documento; }
	}

	public final DocumentoContext documento() throws RecognitionException {
		DocumentoContext _localctx = new DocumentoContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_documento);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(69);
			match(T__0);
			setState(70);
			listaCampos();
			setState(71);
			match(T__1);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ListaCamposContext extends ParserRuleContext {
		public List<CampoContext> campo() {
			return getRuleContexts(CampoContext.class);
		}
		public CampoContext campo(int i) {
			return getRuleContext(CampoContext.class,i);
		}
		public ListaCamposContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_listaCampos; }
	}

	public final ListaCamposContext listaCampos() throws RecognitionException {
		ListaCamposContext _localctx = new ListaCamposContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_listaCampos);
		int _la;
		try {
			setState(82);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ID:
				enterOuterAlt(_localctx, 1);
				{
				setState(73);
				campo();
				setState(78);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==T__2) {
					{
					{
					setState(74);
					match(T__2);
					setState(75);
					campo();
					}
					}
					setState(80);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
				break;
			case T__1:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CampoContext extends ParserRuleContext {
		public IdentificadorContext identificador() {
			return getRuleContext(IdentificadorContext.class,0);
		}
		public ValorContext valor() {
			return getRuleContext(ValorContext.class,0);
		}
		public CampoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_campo; }
	}

	public final CampoContext campo() throws RecognitionException {
		CampoContext _localctx = new CampoContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_campo);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(84);
			identificador();
			setState(85);
			match(T__3);
			setState(86);
			valor();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AsignacionesContext extends ParserRuleContext {
		public List<AsignacionContext> asignacion() {
			return getRuleContexts(AsignacionContext.class);
		}
		public AsignacionContext asignacion(int i) {
			return getRuleContext(AsignacionContext.class,i);
		}
		public AsignacionesContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_asignaciones; }
	}

	public final AsignacionesContext asignaciones() throws RecognitionException {
		AsignacionesContext _localctx = new AsignacionesContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_asignaciones);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(88);
			asignacion();
			setState(93);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__2) {
				{
				{
				setState(89);
				match(T__2);
				setState(90);
				asignacion();
				}
				}
				setState(95);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AsignacionContext extends ParserRuleContext {
		public IdentificadorContext identificador() {
			return getRuleContext(IdentificadorContext.class,0);
		}
		public ValorContext valor() {
			return getRuleContext(ValorContext.class,0);
		}
		public AsignacionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_asignacion; }
	}

	public final AsignacionContext asignacion() throws RecognitionException {
		AsignacionContext _localctx = new AsignacionContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_asignacion);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(96);
			identificador();
			setState(97);
			match(T__4);
			setState(98);
			valor();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CondicionContext extends ParserRuleContext {
		public CondicionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_condicion; }
	 
		public CondicionContext() { }
		public void copyFrom(CondicionContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class CondSimpleContext extends CondicionContext {
		public IdentificadorContext identificador() {
			return getRuleContext(IdentificadorContext.class,0);
		}
		public OperadorContext operador() {
			return getRuleContext(OperadorContext.class,0);
		}
		public ValorContext valor() {
			return getRuleContext(ValorContext.class,0);
		}
		public CondSimpleContext(CondicionContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class CondAndContext extends CondicionContext {
		public List<CondicionContext> condicion() {
			return getRuleContexts(CondicionContext.class);
		}
		public CondicionContext condicion(int i) {
			return getRuleContext(CondicionContext.class,i);
		}
		public TerminalNode AND() { return getToken(gramaticaParser.AND, 0); }
		public CondAndContext(CondicionContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class CondOrContext extends CondicionContext {
		public List<CondicionContext> condicion() {
			return getRuleContexts(CondicionContext.class);
		}
		public CondicionContext condicion(int i) {
			return getRuleContext(CondicionContext.class,i);
		}
		public TerminalNode OR() { return getToken(gramaticaParser.OR, 0); }
		public CondOrContext(CondicionContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class CondAgrupadaContext extends CondicionContext {
		public CondicionContext condicion() {
			return getRuleContext(CondicionContext.class,0);
		}
		public CondAgrupadaContext(CondicionContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class CondNotContext extends CondicionContext {
		public TerminalNode NOT() { return getToken(gramaticaParser.NOT, 0); }
		public CondicionContext condicion() {
			return getRuleContext(CondicionContext.class,0);
		}
		public CondNotContext(CondicionContext ctx) { copyFrom(ctx); }
	}

	public final CondicionContext condicion() throws RecognitionException {
		return condicion(0);
	}

	private CondicionContext condicion(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		CondicionContext _localctx = new CondicionContext(_ctx, _parentState);
		CondicionContext _prevctx = _localctx;
		int _startState = 24;
		enterRecursionRule(_localctx, 24, RULE_condicion, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(111);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NOT:
				{
				_localctx = new CondNotContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;

				setState(101);
				match(NOT);
				setState(102);
				condicion(5);
				}
				break;
			case ID:
				{
				_localctx = new CondSimpleContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(103);
				identificador();
				setState(104);
				operador();
				setState(105);
				valor();
				}
				break;
			case T__5:
				{
				_localctx = new CondAgrupadaContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(107);
				match(T__5);
				setState(108);
				condicion(0);
				setState(109);
				match(T__6);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			_ctx.stop = _input.LT(-1);
			setState(121);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,8,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(119);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,7,_ctx) ) {
					case 1:
						{
						_localctx = new CondAndContext(new CondicionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_condicion);
						setState(113);
						if (!(precpred(_ctx, 4))) throw new FailedPredicateException(this, "precpred(_ctx, 4)");
						setState(114);
						match(AND);
						setState(115);
						condicion(5);
						}
						break;
					case 2:
						{
						_localctx = new CondOrContext(new CondicionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_condicion);
						setState(116);
						if (!(precpred(_ctx, 3))) throw new FailedPredicateException(this, "precpred(_ctx, 3)");
						setState(117);
						match(OR);
						setState(118);
						condicion(4);
						}
						break;
					}
					} 
				}
				setState(123);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,8,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class OperadorContext extends ParserRuleContext {
		public OperadorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_operador; }
	}

	public final OperadorContext operador() throws RecognitionException {
		OperadorContext _localctx = new OperadorContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_operador);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(124);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 7968L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ValorContext extends ParserRuleContext {
		public TerminalNode CADENA() { return getToken(gramaticaParser.CADENA, 0); }
		public TerminalNode NUMERO() { return getToken(gramaticaParser.NUMERO, 0); }
		public TerminalNode BOOLEANO() { return getToken(gramaticaParser.BOOLEANO, 0); }
		public ValorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_valor; }
	}

	public final ValorContext valor() throws RecognitionException {
		ValorContext _localctx = new ValorContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_valor);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(126);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 29360128L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class IdentificadorContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(gramaticaParser.ID, 0); }
		public IdentificadorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_identificador; }
	}

	public final IdentificadorContext identificador() throws RecognitionException {
		IdentificadorContext _localctx = new IdentificadorContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_identificador);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(128);
			match(ID);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 12:
			return condicion_sempred((CondicionContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean condicion_sempred(CondicionContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 4);
		case 1:
			return precpred(_ctx, 3);
		}
		return true;
	}

	public static final String _serializedATN =
		"\u0004\u0001\u001a\u0083\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001"+
		"\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004"+
		"\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007"+
		"\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b"+
		"\u0002\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002\u000f\u0007"+
		"\u000f\u0001\u0000\u0005\u0000\"\b\u0000\n\u0000\f\u0000%\t\u0000\u0001"+
		"\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0003"+
		"\u0001-\b\u0001\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001"+
		"\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0004\u0001\u0004\u0001"+
		"\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0005\u0001\u0005\u0001"+
		"\u0005\u0001\u0005\u0001\u0006\u0001\u0006\u0001\u0006\u0003\u0006D\b"+
		"\u0006\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\b\u0001\b"+
		"\u0001\b\u0005\bM\b\b\n\b\f\bP\t\b\u0001\b\u0003\bS\b\b\u0001\t\u0001"+
		"\t\u0001\t\u0001\t\u0001\n\u0001\n\u0001\n\u0005\n\\\b\n\n\n\f\n_\t\n"+
		"\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\f\u0001\f\u0001"+
		"\f\u0001\f\u0001\f\u0001\f\u0001\f\u0001\f\u0001\f\u0001\f\u0001\f\u0003"+
		"\fp\b\f\u0001\f\u0001\f\u0001\f\u0001\f\u0001\f\u0001\f\u0005\fx\b\f\n"+
		"\f\f\f{\t\f\u0001\r\u0001\r\u0001\u000e\u0001\u000e\u0001\u000f\u0001"+
		"\u000f\u0001\u000f\u0000\u0001\u0018\u0010\u0000\u0002\u0004\u0006\b\n"+
		"\f\u000e\u0010\u0012\u0014\u0016\u0018\u001a\u001c\u001e\u0000\u0002\u0002"+
		"\u0000\u0005\u0005\b\f\u0001\u0000\u0016\u0018~\u0000#\u0001\u0000\u0000"+
		"\u0000\u0002,\u0001\u0000\u0000\u0000\u0004.\u0001\u0000\u0000\u0000\u0006"+
		"2\u0001\u0000\u0000\u0000\b6\u0001\u0000\u0000\u0000\n<\u0001\u0000\u0000"+
		"\u0000\fC\u0001\u0000\u0000\u0000\u000eE\u0001\u0000\u0000\u0000\u0010"+
		"R\u0001\u0000\u0000\u0000\u0012T\u0001\u0000\u0000\u0000\u0014X\u0001"+
		"\u0000\u0000\u0000\u0016`\u0001\u0000\u0000\u0000\u0018o\u0001\u0000\u0000"+
		"\u0000\u001a|\u0001\u0000\u0000\u0000\u001c~\u0001\u0000\u0000\u0000\u001e"+
		"\u0080\u0001\u0000\u0000\u0000 \"\u0003\u0002\u0001\u0000! \u0001\u0000"+
		"\u0000\u0000\"%\u0001\u0000\u0000\u0000#!\u0001\u0000\u0000\u0000#$\u0001"+
		"\u0000\u0000\u0000$&\u0001\u0000\u0000\u0000%#\u0001\u0000\u0000\u0000"+
		"&\'\u0005\u0000\u0000\u0001\'\u0001\u0001\u0000\u0000\u0000(-\u0003\u0004"+
		"\u0002\u0000)-\u0003\u0006\u0003\u0000*-\u0003\b\u0004\u0000+-\u0003\n"+
		"\u0005\u0000,(\u0001\u0000\u0000\u0000,)\u0001\u0000\u0000\u0000,*\u0001"+
		"\u0000\u0000\u0000,+\u0001\u0000\u0000\u0000-\u0003\u0001\u0000\u0000"+
		"\u0000./\u0005\r\u0000\u0000/0\u0003\u001e\u000f\u000001\u0003\u000e\u0007"+
		"\u00001\u0005\u0001\u0000\u0000\u000023\u0005\u000e\u0000\u000034\u0003"+
		"\u001e\u000f\u000045\u0003\f\u0006\u00005\u0007\u0001\u0000\u0000\u0000"+
		"67\u0005\u000f\u0000\u000078\u0003\u001e\u000f\u000089\u0005\u0011\u0000"+
		"\u00009:\u0003\u0014\n\u0000:;\u0003\f\u0006\u0000;\t\u0001\u0000\u0000"+
		"\u0000<=\u0005\u0010\u0000\u0000=>\u0003\u001e\u000f\u0000>?\u0003\f\u0006"+
		"\u0000?\u000b\u0001\u0000\u0000\u0000@A\u0005\u0012\u0000\u0000AD\u0003"+
		"\u0018\f\u0000BD\u0001\u0000\u0000\u0000C@\u0001\u0000\u0000\u0000CB\u0001"+
		"\u0000\u0000\u0000D\r\u0001\u0000\u0000\u0000EF\u0005\u0001\u0000\u0000"+
		"FG\u0003\u0010\b\u0000GH\u0005\u0002\u0000\u0000H\u000f\u0001\u0000\u0000"+
		"\u0000IN\u0003\u0012\t\u0000JK\u0005\u0003\u0000\u0000KM\u0003\u0012\t"+
		"\u0000LJ\u0001\u0000\u0000\u0000MP\u0001\u0000\u0000\u0000NL\u0001\u0000"+
		"\u0000\u0000NO\u0001\u0000\u0000\u0000OS\u0001\u0000\u0000\u0000PN\u0001"+
		"\u0000\u0000\u0000QS\u0001\u0000\u0000\u0000RI\u0001\u0000\u0000\u0000"+
		"RQ\u0001\u0000\u0000\u0000S\u0011\u0001\u0000\u0000\u0000TU\u0003\u001e"+
		"\u000f\u0000UV\u0005\u0004\u0000\u0000VW\u0003\u001c\u000e\u0000W\u0013"+
		"\u0001\u0000\u0000\u0000X]\u0003\u0016\u000b\u0000YZ\u0005\u0003\u0000"+
		"\u0000Z\\\u0003\u0016\u000b\u0000[Y\u0001\u0000\u0000\u0000\\_\u0001\u0000"+
		"\u0000\u0000][\u0001\u0000\u0000\u0000]^\u0001\u0000\u0000\u0000^\u0015"+
		"\u0001\u0000\u0000\u0000_]\u0001\u0000\u0000\u0000`a\u0003\u001e\u000f"+
		"\u0000ab\u0005\u0005\u0000\u0000bc\u0003\u001c\u000e\u0000c\u0017\u0001"+
		"\u0000\u0000\u0000de\u0006\f\uffff\uffff\u0000ef\u0005\u0015\u0000\u0000"+
		"fp\u0003\u0018\f\u0005gh\u0003\u001e\u000f\u0000hi\u0003\u001a\r\u0000"+
		"ij\u0003\u001c\u000e\u0000jp\u0001\u0000\u0000\u0000kl\u0005\u0006\u0000"+
		"\u0000lm\u0003\u0018\f\u0000mn\u0005\u0007\u0000\u0000np\u0001\u0000\u0000"+
		"\u0000od\u0001\u0000\u0000\u0000og\u0001\u0000\u0000\u0000ok\u0001\u0000"+
		"\u0000\u0000py\u0001\u0000\u0000\u0000qr\n\u0004\u0000\u0000rs\u0005\u0013"+
		"\u0000\u0000sx\u0003\u0018\f\u0005tu\n\u0003\u0000\u0000uv\u0005\u0014"+
		"\u0000\u0000vx\u0003\u0018\f\u0004wq\u0001\u0000\u0000\u0000wt\u0001\u0000"+
		"\u0000\u0000x{\u0001\u0000\u0000\u0000yw\u0001\u0000\u0000\u0000yz\u0001"+
		"\u0000\u0000\u0000z\u0019\u0001\u0000\u0000\u0000{y\u0001\u0000\u0000"+
		"\u0000|}\u0007\u0000\u0000\u0000}\u001b\u0001\u0000\u0000\u0000~\u007f"+
		"\u0007\u0001\u0000\u0000\u007f\u001d\u0001\u0000\u0000\u0000\u0080\u0081"+
		"\u0005\u0019\u0000\u0000\u0081\u001f\u0001\u0000\u0000\u0000\t#,CNR]o"+
		"wy";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}