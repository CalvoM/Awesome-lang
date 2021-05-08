from ply import yacc,lex
import mynodes

tokens = ["IF", "DEF", "CLASS", "NEWLINE", "NUMBER", "STRING", "TRUE", "FALSE",
          "NIL", "IDENTIFIER", "CONSTANT", "INDENT", "DEDENT", "LPAREN", "RPAREN",
          "NEWLINE", "SEMI_COLON"]

t_LPAREN = r"\("
t_RPAREN = r"\)"
t_SEMI_COLON = r";"


def t_NEWLINE(t: lex.LexToken):
    r"\n+"
    t.lexer.no += int(t.value)


precedence = (
    ('left', ','),
    ('right', '='),
    ('left', '||'),
    ('left', '&&'),
    ('left', '==', '!='),
    ('left', '>', '>=', '<', '<='),
    ('left', '+', '-'),
    ('left', '*', '/'),
    ('right', '!'),
    ('left', '.')
)


def p_program_empty(p: yacc.YaccProduction):
    """program : empty"""
    p[0] = mynodes.Nodes([])


def p_program_expr(p: yacc.YaccProduction):
    """program : expr"""
    p[0] = p[1]


def p_expr_expr(p: yacc.YaccProduction):
    """expr : expr"""
    p[0] = mynodes.Nodes(p[1:])


def p_expr_term_expr(p: yacc.YaccProduction):
    """expr : expr term expr"""
    p[1] = p[1] + p[3]
    p[0] = p[1]


def p_expr_term(p: yacc.YaccProduction):
    """expr : expr term"""
    p[0] = p[1]


def p_expr_expr_major_def(p: yacc.YaccProduction):
    """expr : Literal
            | Call
            | Operator
            | GetConstant
            | SetConstant
            | GetLocal
            | SetLocal
            | Def
            | Class
            | If"""


def p_expr_parens(p: yacc.YaccProduction):
    """expr : LPAREN expr RPAREN"""
    p[0] = p[2]


def p_expr_just_term(p: yacc.YaccProduction):
    """expr : term"""
    p[0] = mynodes.Nodes([])


def p_term(p: yacc.YaccProduction):
    """term : NEWLINE
            | SEMI_COLON"""


def p_literal_num(p: yacc.YaccProduction):
    """Literal : NUMBER"""
    p[0] = mynodes.NumberNode(p[1])


def p_literal_str(p: yacc.YaccProduction):
    """Literal : STRING"""
    p[0] = mynodes.StringNode(p[1])


def p_literal_true(p: yacc.YaccProduction):
    """Literal : TRUE"""
    p[0] = mynodes.TrueNode()


def p_literl_false(p: yacc.YaccProduction):
    """Literal : FALSE"""
    p[0] = mynodes.FalseNode()


def p_literal_nil(p: yacc.YaccProduction):
    """Literal : NIL"""
    p[0] = mynodes.NilNode()


def p_call_id(p: yacc.YaccProduction):
    """Call : IDENTIFIER ARGS"""
    


def p_empty(p: yacc.YaccProduction):
    """empty:"""
    print("empty")
