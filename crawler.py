from pymongo import MongoClient
from pygments.lexers import JavascriptLexer
from pygments import lex
from pygments.token import Token
from pygments.token import String, string_to_tokentype
import pprint

'''#MONGO
client = MongoClient()
db = client['prueba']'''

lexer = JavascriptLexer()

#File
filepath = './test/requiere2.js'

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

def indexing(code):
        cont = 0
        # a iterar sobre el codigo para ver que es una variable. 
        for i in code:
            #DECLARACIONES DE VARIABLES Y FUNCIONES CON function
            if i[0] == string_to_tokentype('Token.Keyword.Declaration'):
                if i[1] == 'var':
                    print(code[cont + 2])
                elif i[1] == 'let':
                    print(code[cont + 2])
                elif i[1] == 'const':
                    print(code[cont + 2])
                elif i[1] == 'function':
                    #REVISA SI TIENE NOMBRE PARA GUARDARLO. 
                    if code[cont + 1][1] != '(':
                        print("Name", code[cont + 2][1])
                        valor = code[cont + 2][1]
                        contador_aux = 2
                        #VERIFICAR PARAMETROS
                        while valor != ")":
                            print("Parametro", valor)
                            contador_aux += 1
                            valor = code[cont + contador_aux][1]
                    #PARA FUNCIONES SIN NOMBRE O DECLARADAS HOLA: FUNCTION()
                    else:
                        if code[cont - 2][1] == ":":
                            print("Name", code[cont - 3][1])
                        else:
                            print("No tiene nombre.")
                        valor = code[cont + 1][1]
                        contador_aux = 1
                        #VERIFICAR PARAMETROS
                        while valor != ")":
                            print("Parametro", valor)
                            contador_aux += 1
                            valor = code[cont + contador_aux][1]
                
            #CLASES 
            elif i[0] == string_to_tokentype('Token.Keyword.Reserved'):
                if i[1] == 'class':
                    print(code[cont + 2])
                    #VERIFICAR SI TIENE CONSTRUCTOR PARA LOS PARAMETROS
                    if code[cont + 6][1] == 'constructor':
                        add = 8
                        valortemp = code[cont + add][1]
                        while valortemp != ')':
                            valortemp = code[cont + add][1]
                            print(valortemp)
                            add += 1
                    elif code[cont + 10][1] == 'constructor':
                        add = 12
                        valortemp = code[cont + add][1]
                        while valortemp != ')':
                            valortemp = code[cont + add][1]
                            print(valortemp)
                            add += 1

                    #VERIFICAR HERENCIA
                    if code[cont + 4][1] == 'extends':
                        print(code[cont + 6])
            #FUNCIONES

            cont += 1


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
                elif y[1] == '=>':
                    print("ES6 definition")
                    valor = code[contador][1]
                    contador_aux = 1
                    while valor != "=":
                        contador_aux += 1
                        valor = code[contador - contador_aux][1]
                    print("Name", code[contador - contador_aux - 2][1])
                    valor = code[contador][1]
                    contador_aux2 = 3
                    while valor != "(":
                        print("Parametro",code[contador - contador_aux2][1])
                        contador_aux2 += 1
                        valor = code[contador - contador_aux2][1]
                contador += 1

global recorrido
recorrido = []

def recorrer(codigo):
    nombres = []
    contador = 0
    for i in codigo:
                if i[1] == 'require':
                        print(codigo[contador + 2][1])
                        path_modificado = codigo[contador + 2][1][1:-1]
                        nombres.append('./test/' + path_modificado + '.js')
                contador += 1
                for x in nombres:
                    filepath2 = x
                    fp2 = open(filepath2).read()
                    tokens2 = lex(fp2, lexer)
                    code2 = []
                    for y in tokens2:
                        code2.append(y)
                    
                    if x not in recorrido:
                        recorrer(code2)
                    recorrido.append(x)         

#recorrer(code)
indexing(code)
#print(code)