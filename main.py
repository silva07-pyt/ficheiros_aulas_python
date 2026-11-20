
import PySimpleGUI as sg

# Criar o layout da janela
layout = [
    [sg.Text("Olá! Bem-vindo ao Python!")],
    [sg.Text("Escreve o teu nome:")],
    [sg.Input(key="-NOME-")],
    [sg.Button("Enviar"), sg.Button("Sair")]
]

# Criar a janela
janela = sg.Window("A minha primeira aplicação", layout)

# Ciclo de eventos
while True:
    evento, valores = janela.read()

    if evento == sg.WINDOW_CLOSED or evento == "Sair":
        break

    if evento == "Enviar":
        nome = valores["-NOME-"]
        sg.popup(f"Olá, {nome}!")

janela.close()
