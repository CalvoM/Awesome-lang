from ply import yacc,lex
import mynodes

tokens = ["IF", "DEF", "CLASS", "NEWLINE", "NUMBER", "STRING", "TRUE", "FALSE",
          "NIL", "IDENTIFIER", "CONSTANT", "INDENT", "DEDENT", "LPAREN", "RPAREN",
          "NEWLINE", "SEMI_COLON", "DOT", "OR", "AND", "EQ", "NEQ", "GT", "GTEQ",
          "LT", "LTEQ", "PLUS", "MINUS", "TIMES", "DIVIDE", "COMMA","EQUATE"]

t_LPAREN = r"\("
t_RPAREN = r"\)"
t_SEMI_COLON = r";"
t_DOT = r"\."
t_OR = r"||"
t_AND = r"&&"
t_EQ = r"="
t_NEQ = r"!="
t_GT = r">"
t_GTEQ = r">="
t_LT = r"<"
t_LTEQ = r"<="
t_PLUS = r"\+"
t_MINUS = r"-"
t_TIMES = r"\*"
t_DIVIDE = r"/"
t_COMMA = r","
t_EQUATE = r"\="


def t_NEWLINE(t: lex.LexToken):
    r"\n+"
    t.lexer.no += int(t.value)


precedence = (
    ('left', 'COMMA'),
    ('right', 'EQUATE'),
    ('left', 'OR'),
    ('left', 'AND'),
    ('left', 'EQ', 'NEQ'),
    ('left', 'GT', 'GTEQ', 'LT', 'LTEQ'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
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
    p[0] = mynodes.CallNode(None, p[1], p[2])


def p_call_expr_args(p: yacc.YaccProduction):
    """Call : expr DOT IDENTIFIER ARGS"""
    p[0] = mynodes.CallNode(p[1], p[3], p[4])


def p_call_expr(p: yacc.YaccProduction):
    """Call : expr DOR IDENTIFIER"""
    p[0] = mynodes.CallNode(p[1], p[3], [])


def p_args(p: yacc.YaccProduction):
    """ARGS : LPAREN RPAREN"""
    p[0] = []


def p_args_list(p: yacc.YaccProduction):
    """ARGS : LPAREN ARGLIST RPAREN"""
    p[0] = p[2]


def p_arglist(p: yacc.YaccProduction):
    """ARGLIST : expr"""
    p[0] = p[1:]


def p_arglist_comma(p: yacc.YaccProduction):
    """ARGLIST : ARGLIST COMMA expr"""
    p[1] = p[1] + p[3]
    p[0] = p[1]


def p_operator(p: yacc.YaccProduction):
    """Operator : expr OR expr
                | expr AND expr
                | expr EQ expr
                | expr NEQ expr
                | expr GT expr
                | expr GTEQ expr
                | expr LT expr
                | expr LTEQ expr
                | expr PLUS expr
                | expr MINUS expr
                | expr TIMES expr
                | expr DIVIDEC expr"""
    p[0] = mynodes.CallNode(p[1], p[2], p[3])


def p_get_constant(p: yacc.YaccProduction):
    """GetConstant : CONSTANT"""
    p[0] = mynodes.GetConstantNode(p[1])


def p_set_constant(p: yacc.YaccProduction):
    """SetConstant : CONSTANT EQUATE expr"""
    p[0] = mynodes.SetConstantNode(p[1], p[2])


def p_get_local(p: yacc.YaccProduction):
    """GetLocal : IDENTIFIER"""
    p[0] = mynodes.GetLocalNode(p[1])


def p_set_local(p: yacc.YaccProduction):
    """SetLocal : IDENTIFIER EQUATE expr"""
    p[0] = mynodes.SetLocalNode(p[1], p[3])


def p_block(p: yacc.YaccProduction):
    """Block : INDENT expr DEDENT"""
    p[0] = p[2]


def p_def(p: yacc.YaccProduction):
    """Def : DEF IDENTIFIER Block"""
    p[0] = mynodes.DefNode(p[2], [], p[3])


def p_def_param_list(p: yacc.YaccProduction):
    """Def : DEF IDENTIFIER LPAREN ParamList RPAREN Block"""
    p[0] = mynodes.DefNode(p[2], p[4], p[6])


def p_param_list_empty(p: yacc.YaccProduction):
    """ParamList : """
    p[0] = []


def p_param_list_identifier(p: yacc.YaccProduction):
    """ParamList : IDENTIFIER"""
    p[0] = p[1:]


def p_param_list_param(p: yacc.YaccProduction):
    """ParamList : ParamList COMMA IDENTIFIER"""
    p[1] = p[1] + p[3]
    p[0] = p[1]


def p_class(p: yacc.YaccProduction):
    """Class :  CLASS CONSTANT Block"""
    p[0] = mynodes.ClassNode(p[2], p[3])


def p_if(p: yacc.YaccProduction):
    """If : IF expr Block"""
    p[0] = mynodes.IfNode(p[2], p[3])

def p_empty(p: yacc.YaccProduction):
    """empty:"""
    print("empty")
