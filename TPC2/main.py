import re

#transformar arquivo em objeto de linhas
def transformarArquivoObjeto(nomeArquivo):
    with open(nomeArquivo, encoding='utf-8') as arquivo:
        linhas = arquivo.read().splitlines()
    return linhas

#voltar objeto de linhas para arquivo
def transformarObjetoArquivo(obj, nomeArquivo):
    with open(nomeArquivo, 'w', encoding='utf-8') as arquivo:
        arquivo.write("\n".join(obj))

def main():
    linhasMD = transformarArquivoObjeto('Receita.md')

    patternH1 = r'^# +(.+)$'
    patternH2 = r'^## +(.+)$'
    patternH3 = r'^### +(.+)$'
    patternBold = r'\*{2}(.+?)\*{2}'
    patternItalic = r'\*{1}(.+?)\*{1}'
    patternList = r'^\d+\. (.+)$'
    patternLink = r'\[(.+?)\]\((.+?)\)'
    patternImagem = r'^!\[(.+?)\]\((.+?)\)$'

    linhasHTML = []
    lista = False

    for linha in linhasMD:
        linha = re.sub(patternH1, r'<h1>\1</h1>', linha)
        linha = re.sub(patternH2, r'<h2>\1</h2>', linha)
        linha = re.sub(patternH3, r'<h3>\1</h3>', linha)
        linha = re.sub(patternBold, r'<b>\1</b>', linha)
        linha = re.sub(patternItalic, r'<i>\1</i>', linha)
        linha = re.sub(patternImagem, r'<img src="\2" alt="\1" />', linha)
        linha = re.sub(patternLink, r'<a href="\2">\1</a>', linha)
        if re.match(patternList, linha):
            if not lista:
                linhasHTML.append("<ol>")
                lista = True
        elif lista:
            linhasHTML.append("</ol>")
            lista = False
        linha = re.sub(patternList, r'<li>\1</li>', linha)
        linhasHTML.append(linha)
    
    transformarObjetoArquivo(linhasHTML, "Receita.html")

if __name__ == "__main__":
    main()