import tkinter as gui
from tkinter import messagebox

window = gui.Tk()
window.geometry('500x450')
window.title('Todo Liste')
window.config(bg='#111111')


def aufgabe_dazu():
    aufgabe = aufgabe_eingabe.get()

    if aufgabe != '':
        if aufgabe == 'Aufgabe eingeben':
            messagebox.showwarning('Error', 'Bitte eine Aufgabe eingeben')
        else:
            aufgaben_liste.insert(gui.END, aufgabe)
            aufgabe_eingabe.delete(0, 'end')
    else:
        messagebox.showwarning('Error', 'Bitte eine Aufgabe eingeben')


def aufgabe_weg():
    aufgaben_liste.delete(gui.ANCHOR)


def eingabe_entfernen(event, eingabe):
    eingabe.delete(0, gui.END)


frame = gui.Frame(window)
frame.pack(pady=10)

aufgaben_liste = gui.Listbox(frame, width=25, height=8, font=('Times', 18),
                             fg='#464646', selectbackground='#333333', activestyle='none')
aufgaben_liste.pack(side=gui.LEFT, fill=gui.BOTH)

scroll_bar = gui.Scrollbar(frame)
scroll_bar.pack(side=gui.RIGHT, fill=gui.BOTH)

aufgaben_liste.config(yscrollcommand=scroll_bar.set)
scroll_bar.config(command=aufgaben_liste.yview)

aufgabe_eingabe = gui.Entry(window, font=('Times', 24))
aufgabe_eingabe.insert(0, 'Aufgabe eingeben')
aufgabe_eingabe.bind('<Button-1>', lambda event: eingabe_entfernen(event, aufgabe_eingabe))
aufgabe_eingabe.pack(pady=20)

button_frame = gui.Frame(window)
button_frame.pack(pady=20)

aufgabe_dazu_btn = gui.Button(button_frame, text='Aufgabe hinzufügen', font=('Times', 14),
                              bg='green', fg='white', padx=20, pady=10, command=aufgabe_dazu)
aufgabe_dazu_btn.pack(fill=gui.BOTH, expand=True, side=gui.LEFT)

aufgabe_weg_btn = gui.Button(button_frame, text='Aufgabe löschen', font=('Times', 14),
                             bg='red', fg='white', padx=20, pady=10, command=aufgabe_weg)
aufgabe_weg_btn.pack(fill=gui.BOTH, expand=True, side=gui.LEFT)

window.mainloop()