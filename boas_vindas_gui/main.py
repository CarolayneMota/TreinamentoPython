# Importa as bibliotecas
from PyQt6 import uic, QtWidgets
def boas_vindas():
    nome = formulario.txt_nome.text()
    formulario.lbl_resultado.setText(f"Bem-vind@ {nome}")

# Criando a aplicação princial
app = QtWidgets.QApplication([])

# Carrego a ui - Link
# Retorna: formulário com os componetes; window é a janela com forn
Form, Window  = uic.loadUiType("boas_vindas_gui/tela.ui")

# Criar a Window() - Janela
window = Window()
# Cria o foemulário para ter acesso aos componentes
formulario = Form()
# link janela  -> formulário
formulario.setupUi(window)

# CODIGO SEMPRE ABAIXO DO SETUOUI

formulario.lbl_resultado.setText("Setouuu")

formulario.tbm_enviar.clicked.connect(boas_vindas)

window.show()
app.exec()
