# Importa as bibliotecas
from PyQt6 import uic, QtWidgets
import funcoes

# Criando a aplicação princial
app = QtWidgets.QApplication([])

# Carrego a ui - Link
# Retorna: Formulário com os componentes; Window é a janela com form
Form, Window  = uic.loadUiType("calculadora/calc.ui")

# Criar a Window() - Janela
janela = Window()
# Cria o formulário para ter acesso aos componentes
formulario = Form()
# link janela -> formulário
formulario.setupUi(janela)

formulario.btn_mais.clicked.connect(lambda: funcoes.somar(formulario))
formulario.btn_menos.clicked.connect(lambda: funcoes.sub(formulario))
formulario.btn_dividir.clicked.connect(lambda: funcoes.div(formulario))
formulario.btn_mult.clicked.connect(lambda: funcoes.mult(formulario))
# formulario.btn_somar.clicked.connect(click_btn_somar)

janela.show()
app.exec()