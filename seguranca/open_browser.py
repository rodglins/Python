# Biblioteca webbrowser: p/ exibição de documentos web.
import webbrowser
# biblioteca tkinter - fornece interface padrão python p/ ferramentas graficas tk
from tkinter import *

# variavel para representar tkinter:
root = Tk( )

# título:
root.title('Abrir o browser')
# tamanho:
root.geometry('300x200')

# funcao chamada google que irá abrir o site google:
def google():
    webbrowser.open('www.google.com')

# variavel recebe um botão do tkinter
mygoogle = Button(root, text='Abrir o Google', command=google).pack(pady=20)
# chamando o programa:
root.mainloop()

