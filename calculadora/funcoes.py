def somar(formulario):
    num1 = float(formulario.txt_num1.text())
    num2 = float(formulario.txt_num2.text())
    soma = num1 + num2
    formulario.lbl_resultado.setText(f"{soma}")


def sub(formulario):
    num1 = float(formulario.txt_num1.text())
    num2 = float(formulario.txt_num2.text())
    subtra = num1 - num2
    formulario.lbl_resultado.setText(f"{subtra}")


def div(formulario):
    num1 = float(formulario.txt_num1.text())
    num2 = float(formulario.txt_num2.text())
    divis = num1 / num2
    formulario.lbl_resultado.setText(f"{divis}")


def mult(formulario):
    num1 = float(formulario.txt_num1.text())
    num2 = float(formulario.txt_num2.text())
    multi = num1 * num2
    formulario.lbl_resultado.setText(f"{multi}")
