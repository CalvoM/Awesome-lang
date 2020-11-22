import re
class Lexer():
    def __init__(self):
        self.keywords=["def","class","if","true","false","nil"]
        self.current_indent=0
        self.indent_stack=[]
        
    def tokenize(self,code:str):
        code = code.rstrip()
        self.tokens = []
        i=0
        while i<len(code):
            chunk = code[i:]
            if m := re.match("\A([a-z]\w*)",chunk):#word
                if m[1] in self.keywords:
                    self.tokens.append([self.to_sym(m[1]),m[1]])
                else:
                    self.tokens.append([self.to_sym("identifier"),m[1]])
                i+=len(m[1])
            elif constant:=re.match("\A([A-Z]\w*)",chunk):#constant
                self.tokens.append([self.to_sym("constant"),constant[1]])
                i+=len(constant[1])
            elif number:=re.match("\A([0-9]+)",chunk):#number
                self.tokens.append([self.to_sym("number"),number[1]])
                i+=len(number[1])
            elif string:=re.match("\A\"([^\"]*)\"",chunk):#string
                self.tokens.append([self.to_sym("string"),string[0]])
                i+=len(string.group())
            elif indent:=re.match("\A\:\n( +)",chunk,re.MULTILINE):#indent
                if len(indent[1])<=self.current_indent:
                    raise f"Bad indent, got {len(indent[1])} indents, expected>{self.current_indent}"
                self.current_indent = len(indent[1])
                self.indent_stack.append(self.current_indent)
                self.tokens.append([self.to_sym("indent"),len(indent[1])])
                i+=len(indent[1])+2
            elif indent:=re.match("\A\n( *)",chunk,re.MULTILINE):
                if len(indent[1])==self.current_indent:
                    self.tokens.append([self.to_sym("newline"),"\n"])
                elif len(indent[1])<self.current_indent:
                    while len(indent[1])<self.current_indent:
                        self.indent_stack.pop()
                        if len(self.indent_stack)>0:
                            self.current_indent = self.indent_stack[-1]
                        else:
                            self.current_indent=0
                        self.tokens.append([self.to_sym("dedent"),len(indent[1])])
                    self.tokens.append([self.to_sym("newline"),"\n"])
                else:
                    raise "Missing :"
                i+=len(indent[1])+1
            elif operator:=re.match("\A(\|\||&&|==|!=|<=|>=)",chunk):
                print(operator)
                self.tokens.append([self.to_sym(operator[1]),operator[1]])
                i+=len(operator[1])
            elif space:=re.match("\A ",chunk):
                i+=1
            else:
                value=chunk[0:1]
                self.tokens.append([self.to_sym(value),value])
                i+=1
        if len(self.indent_stack):
            while indent:=self.indent_stack.pop():
                self.tokens.append([self.to_sym("dedent"),indent])
                if len(self.indent_stack)==0:
                    break
    
    def to_sym(self,word:str)->str:
        word = word.upper()
        return repr(word)


if __name__ == "__main__":
    lex = Lexer()
    content=""
    with open("./sample.txt","r") as f:
        content = f.read()
    lex.tokenize(content)
    for t in lex.tokens:
        print(t)
    