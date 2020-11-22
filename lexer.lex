/* Lexer for Awesome-lang */
%{
    #include <iostream>
    #include <stdio.h>
    #include <vector>
    #include <list>
    #include <tuple>
    #include <algorithm>
    std::vector<std::tuple<std::string,std::string>> tokens;
    std::list<std::string> keywords={"def","class","if","true","false","nil"};
%}

identifier ([a-z]+)
constant ([A-Z]+)
number ([0-9]+)
str \"([^\"]*)\"
operator (=|\|\||&&|==|!=|<=|>=)
indent :\n(\s*)

%%
{str}           {
                    tokens.push_back(std::make_tuple("STRING",std::string(yytext)));
                }
{number}        {
                    tokens.push_back(std::make_tuple("NUMBER",std::string(yytext)));
                }
{identifier}    {
                    if(std::find(keywords.begin(), keywords.end(), std::string(yytext)) != keywords.end()){
                        auto val = std::string(yytext);
                        std::transform(val.begin(), val.end(),val.begin(), [](unsigned char c) -> unsigned char { return std::toupper(c); });
                        tokens.push_back(std::make_tuple(val,std::string(yytext)));
                    }else{
                        tokens.push_back(std::make_tuple("IDENTIFIER",std::string(yytext)));

                    }
                }
{operator}      {
                    tokens.push_back(std::make_tuple(std::string(yytext),std::string(yytext)));
                }
{indent}        { 
                    std::cout<<"INDENT "<<yyleng<<std::endl;
                }
{constant}      {
                    tokens.push_back(std::make_tuple("CONSTANT",std::string(yytext)));
                }

%%
int main(int argc, char* argv[]){
    if(argc>1){
        FILE *in_ = fopen(argv[1],"r");
        if(in_){
            yyin=in_;
        }
    }
    yylex();
    for(auto i:tokens){
        std::cout<<std::get<0>(i)<<" "<<std::get<1>(i)<<std::endl;
    }
}