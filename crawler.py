from pygments.lexers import JavascriptLexer
from pygments import lex
from pygments.token import Token
from pygments.token import String, string_to_tokentype

lexer = JavascriptLexer()

#File
filepath = 't.js'

#File open
fp = open(filepath).read()

#Code insertion
tokens = lex(fp, lexer)
code = []
for x in tokens:
    code.append(x)


def menu():
        print('\n--------- Crawler JS ---------\n')
        print('Press (1,2,3,4,5,6,7,8) to choose\n')
        print('1. Functions\n2. Variables \n3. Reserved Keywords\n4. Builtin \n5. Operators \n6. Constants \n7. Literals \n8. Full Lexer File ')
        x = input("> ")

        if x == '8':
                getVars()
        elif x == '9':
                functions()
        else: 
                print("Error, please enter a valid number. \n")
                menu()



#Imprimir el atibuto según el Token

def getVars():
        cont = 0
        cont2=0
        print('\n ------------------- variables definidas por var --------------------\n')
        for i in code:
                if i[1] == 'var':
                        print(code[cont+2][1])
                cont += 1
        print("\n")
        print('\n ------------------- variables definidas por Let --------------------\n')
        for j in code: 
                if j[1] == 'let':
                        print(code[cont2+2][1])
                cont2 += 1
        print("\n")


            
def functions():
        print('\n ------------------- Funciones --------------------\n')
        contador = 0
        for y in code:
                if y[1] == 'function':
                        if len(code[contador + 2][1]) > 1:
                                print("Name", code[contador + 2][1])
                                valor = code[contador + 4][1]
                                contador_aux = 4
                                while valor != ")":
                                        print("Parametro", valor)
                                        contador_aux += 1
                                        valor = code[contador + contador_aux][1]
                        else:
                                print("No tiene nombre.")
                                valor = code[contador + 3][1]
                                contador_aux = 3
                                while valor != ")":
                                        print("Parametro", valor)
                                        contador_aux += 1
                                        valor = code[contador + contador_aux][1]
                contador += 1



menu()