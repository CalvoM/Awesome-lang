# Awesome-lang

## Using flex to produce lexer

```sh
    flex lexer.lex
    g++ lex.yy.c -ll
    ./a.out ./sample.txt
```

## Using the python script 

```sh
    python3 Lexer.py
```
**NB**
Change the file on *line 75* if you have another file as input.