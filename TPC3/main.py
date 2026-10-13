import re

def tokenize(string):
    reconhecidos = []
    linha = 1
    mo = re.finditer(r'(?P<COMENTARIO>\#(.)+)|(?P<VARIAVEL>\?[A-Za-z0-9]+)|(?P<LINGUA>\@[A-Za-z0-9]{2})|(?P<STRING>"[^"]*")|(?P<DELIMITADOR>[{}.])|(?P<LIMIT>LIMIT\b)|(?P<SELECT>select\b)|(?P<NUM>\d+\b)|(?P<CONCEITO>[A-Za-z0-9:]+)', string)

    for m in mo:
        dic = m.groupdict()
        if dic['COMENTARIO']:
            t = ("COMENTARIO", dic['COMENTARIO'], linha, m.span())
    
        elif dic['VARIAVEL']:
            t = ("VARIAVEL", dic['VARIAVEL'], linha, m.span())
    
        elif dic['STRING']:
            t = ("STRING", dic['STRING'], linha, m.span())
    
        elif dic['DELIMITADOR']:
            t = ("DELIMITADOR", dic['DELIMITADOR'], linha, m.span())

        elif dic['LIMIT']:
            t = ("LIMIT", dic['LIMIT'], linha, m.span())

        elif dic['SELECT']:
            t = ("SELECT", dic['SELECT'], linha, m.span())

        elif dic['NUM']:
            t = ("NUM", dic['NUM'], linha, m.span())
            
        elif dic['CONCEITO']:
            t = ("CONCEITO", dic['CONCEITO'], linha, m.span())

        else:
            t = ("UNKNOWN", m.group(), linha, m.span())
        if t[0] != 'UNKNOWN': reconhecidos.append(t)
    return reconhecidos

def main():
    with open("query.txt", encoding="utf-8") as f:
        for linha in f:
            for tok in tokenize(linha):
                print(tok) 

if __name__ == "__main__":
    main()