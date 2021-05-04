class Parser
%token IF
%token DEF
%token CLASS
%token NEWLINE
%token NUMBER
%token STRING
%token TRUE FALSE NIL
%token IDENTIFIER
%token CONSTANT
%token INDENT DEDENT

%left ','
%right '='
%left '||'
%left '&&'
%left '==' '!='
%left '>' '>=' '<' '<='
%left '+' '-'
%right '*' '/'
%right '!'
%left  '.'
