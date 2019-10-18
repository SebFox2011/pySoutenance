from Tkinter import * 

fenetre = Tk()
fenetre.title ("Interface graphique")

mainframe = Frame(fenetre, height=200,width=500)
mainframe.pack_propagate(0)
mainframe.pack(padx=5,pady=5)

label = Label(fenetre, text="Hello World")
label.pack()

fenetre.mainloop()
