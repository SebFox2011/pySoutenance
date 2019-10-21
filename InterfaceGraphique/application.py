from tkinter import * 
from led import Led
from GPIO import GPIO_initialize


fenetre = Tk()
fenetre.title ("Interface graphique")

mainframe = Frame(fenetre, height=400,width=500)
mainframe.pack_propagate(0)
mainframe.grid()

label = Label(mainframe, text="Etat led")
label.grid(row=0, column=0)

GPIO_initialize()
led= Led(15)

led_buttonOn = Button(mainframe, text="Led On", command=led.on)
led_buttonOn.grid(row=0, column=3)

led_buttonOff = Button(mainframe, text="Led Off", command=led.off)
led_buttonOff.grid(row=0, column=4)

exit_button  = Button(mainframe, text="Quit", command=fenetre.destroy)
exit_button.grid(row=2, column=2)

logo = PhotoImage(file='Icon.gif') # ne pas supprimer cette référence
Label(image=logo).grid(row=3,column=0)

fenetre.mainloop()