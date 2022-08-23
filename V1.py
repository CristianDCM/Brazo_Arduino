from tkinter import ttk
from tkinter import *
import time
import serial
import tkinter
import tkinter as tk

#+++++++++++++Global Variables+++++++++++++++++++++
#ser = serial.Serial(Puerto, 9600)
#++++++++++++++++Functions+++++++++++++++++++++++

def Mover(aCommand):
    #Esta funcion envia el comando de angulos articulares al arduino para mover los servos a las posiciones deseadas
    aCommand = 0  #Soporte sin usar para permitir que la función funcione en vivo con la barra de escala
    #ser.flushInput()
    #ser.flushOutput()
    command = str(Inferior.get()) +','+ str(Izquierda.get()) +','+ str(Derecha.get()) +','+ str(Superior.get()) +'d'
    print(command)
    #ser.write((command).encode())
    #espera hasta una respuesta si se encuentra desde el arduino
    OK = 'd'
    while (OK != 'd'):
        OK = ser.read(1)

#++++++++++++++++++++GUI++++++++++++++++++++++
root = Tk()
root.title('Interfaz Grafica')
#++++++++++++++++++++motores de accionamiento++++++++++++++++++
motorControl = Frame(root)
motorControl.pack()

forwardFrame = Frame(motorControl)
forwardFrame.pack()

backFrame = Frame(motorControl)
backFrame.pack (side = BOTTOM)

speedControl = Frame(root)
speedControl.pack()
#+++++++++++++++++ARM+++++++++++++++++++++++++
# The scroll bars
armControl = Frame(root)
armControl.pack( )

armLabel = Label(armControl, text = "Componentes", bg = "red", padx = 100)
armLabel.pack()

#Imagen
imglabel = Label(armControl)
img = tkinter.PhotoImage(file="Servo.png")
img = img.subsample(4, 4)
imglabel.config(image=img)
imglabel.pack()
#++++++++++++++++++++++Pinza++++++++++++++++++++++++++++
SuperiorLabel = Label(armControl, text = "Pinza", bg = "red", padx = 100)
SuperiorLabel.pack()
Superior = Scale(armControl, from_= 0, to = 40, length = 300, orient = HORIZONTAL,tickinterval=20, command = Mover)
Superior.set(10)
Superior.pack()
#++++++++++++++++++++++++Inferior+++++++++++++++++++++++++++
InferiorLabel = Label(armControl, text = "Inferior", bg = "red", padx = 100)
InferiorLabel.pack()
Inferior = Scale(armControl, from_= 0, to = 180, length = 300, orient = HORIZONTAL,tickinterval=30, command = Mover)
Inferior.pack()
#++++++++++++++++++++++Izquierda+++++++++++++++++++++++++
IzquierdaLabel = Label(armControl, text = "Izquierda", bg = "red", padx = 100)
IzquierdaLabel.pack()
Izquierda = Scale(armControl, from_= 0, to = 180, length = 300, orient = HORIZONTAL,tickinterval=30, command = Mover)
Izquierda.set(100)
Izquierda.pack()
#++++++++++++++++++++++Derecha++++++++++++++++++++++++++++
DerechaLabel = Label(armControl, text = "Derecha", bg = "red", padx = 100)
DerechaLabel.pack()
Derecha = Scale(armControl, from_= 0, to = 180, length = 300, orient = HORIZONTAL,tickinterval=30, command = Mover)
Derecha.set(140)
Derecha.pack()

#++++++++++++++++++++++Velocidad++++++++++++++++++++++++++++
VelocidadLabel = Label(armControl, text = "Velocidad", bg = "red", padx = 100)  #TERMINAR SLIDER VELOCIDAD FALTA DEFINIR FUNCION, SCRIPT ARDUINO
VelocidadLabel.pack()
Velocidad = Scale(armControl, from_= 0, to = 180, length = 300, orient = HORIZONTAL,tickinterval=30, command = Mover)
Velocidad.set(0)
Velocidad.pack()

root.mainloop()