from flask import Flask, render_template, request, redirect
# Agora o import vai funcionar porque a função existe neste arquivo!
from estrutura_de_dados import tarefas, adicionar_tarefa, completar_tarefa, salvar_dado, carregar_dados

app = Flask(__name__)

# Carregar os dados salvos assim que o programa abrir
carregar_dados()

@app.route("/")
def index():
    return render_template("index.html", tarefas=tarefas)

@app.route("/adicionar", methods=["POST"])
def adicionar():
    texto = request.form["texto_tarefa"]
    adicionar_tarefa(texto)
    salvar_dado() 
    return redirect("/")

@app.route("/completar/<int:id>")
def completar(id):
    completar_tarefa(id)
    salvar_dado()
    return redirect("/")

@app.route("/dashboard")
def dashboard():
    # 1. Recarrega os dados do arquivo para garantir que pegamos o que foi feito antes
    from estrutura_de_dados import carregar_dados, tarefas
    carregar_dados() 

    # 2. Faz os cálculos com a lista atualizada
    total = len(tarefas)
    # Conta apenas os dicionários onde 'feito' é True
    concluidas = sum(1 for t in tarefas if t.get('feito') == True)
    
    porcentagem = 0
    if total > 0:
        porcentagem = round((concluidas / total) * 100, 1)
    
    return render_template("dashboard.html", 
                           total=total, 
                           concluidas=concluidas, 
                           pendentes=total - concluidas, 
                           porcentagem=porcentagem)


if __name__ == "__main__":
    app.run(debug=True)