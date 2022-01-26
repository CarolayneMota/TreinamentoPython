# Importa as bibliotecas
from PyQt6 import uic, QtWidgets
import equacao2 as eq

# Criando a aplicação princial
app = QtWidgets.QApplication([])

# Carrego a ui - Link
# Retorna: Formulário com os componentes; Window é a janela com form
Form, Window = uic.loadUiType("equacao_2_grau/raizes.ui")

# Criar a Window() - Janela
janela = Window()
# Cria o formulário para ter acesso aos componentes
formulario = Form()
# link janela -> formulário
formulario.setupUi(janela)

formulario.btn_resolver.clicked.connect(lambda: eq.bhaskara(formulario))

janela.show()
app.exec()
