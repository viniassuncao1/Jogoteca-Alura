from flask import Flask #Importando a biblioteca flask
 
app = Flask(__name__) # Criando a variavel onde colocaremos a aplicacao, o name faz referencia ao proprio arquivo.

@app.route('/Inicio') #Cria uma rota e nomeia ela
def ola():#funcao que define oque existe na rota
    return '<h1> Olá Mundo! </h1>' #retorna o que sera exibido na rota e usa linguagem HTML


app.run() # Rodar a aplicação