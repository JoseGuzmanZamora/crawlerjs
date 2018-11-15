from pygments import highlight
from pygments import lex
from pygments.lexers.javascript import JavascriptLexer
from pygments.formatters.html import HtmlFormatter

lexer = JavascriptLexer()

archivo = open('output.html', 'r+')
code = open('index.js', 'r+').read()
formatter = HtmlFormatter(lineous=True, nowrap=False, cssclass="source")

tokens = lex(code, lexer)
results = []
for x in tokens:
    results.append(x)

contador = 0
for y in results:
    if y[1] == "require":
        print(results[contador + 2][1])
    contador += 1

