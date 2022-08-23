from tkinter import ttk
from tkinter import *
import time
import serial
import tkinter
import tkinter as tk
#Variable serial
ser = serial.Serial("/dev/ttyACM0", 9600)
#Funcion de envio
def Mover(aCommand):
    #Esta funcion envia el comando de angulos articulares al arduino para mover los servos a las posiciones deseadas
    aCommand = 0  #Soporte sin usar para permitir que la función funcione en vivo con la barra de escala
    #ser.flushInput()
    #ser.flushOutput()
    command = str(Inferior.get()) +','+ str(Izquierda.get()) +','+ str(Derecha.get()) +','+ str(Superior.get()) +'d'
    print(command)
    ser.write((command).encode())
    #espera hasta una respuesta si se encuentra desde el arduino
    OK = 'd'
    while (OK != 'd'):
        OK = ser.read(1)
#GUI
root = Tk()
#root.iconbitmap("Icono.ico")
root.title('Interfaz Grafica')
#Las barras de desplazamiento
armControl = Frame(root)
armControl.pack()
armLabel = Label(armControl,padx = 400, text = "Brazo Robotico Arduino", fg ="white", bg = "red")
armLabel.pack()
LabelFrame = LabelFrame(armControl)
LabelFrame.pack()
#Pinza
SuperiorLabel = Label(armControl, text = "Pinza", padx = 100, borderwidth = 2, relief="ridge")
SuperiorLabel.pack()
Superior = Scale(armControl, from_= 0, to = 40, length = 300, orient = HORIZONTAL,tickinterval=20, command = Mover)
Superior.set(10)
Superior.pack()
#Imagen
Imglabel = Label(armControl)
Img = tkinter.PhotoImage(file="Servo.png")
Img = Img.subsample(4, 4)
Imglabel.config(image=Img)
Imglabel.pack()
#Inferior
InferiorLabel = Label(armControl, text = "Inferior", padx = 100, borderwidth = 2, relief="ridge")
InferiorLabel.pack()
Inferior = Scale(armControl, from_= 0, to = 180, length = 300, orient = HORIZONTAL,tickinterval=30, command = Mover)
Inferior.pack()
#Izquierda
IzquierdaControl = Frame(armControl)
IzquierdaControl.place(x=20, y=150)
IzquierdaLabel = Label(IzquierdaControl, text = "Izquierda", padx = 100, borderwidth = 2, relief="ridge")
IzquierdaLabel.pack()
Izquierda = Scale(IzquierdaControl, from_= 0, to = 180, length = 300, orient = HORIZONTAL,tickinterval=30, command = Mover)
Izquierda.set(100)
Izquierda.pack()
#Derecha
DerechaControl = Frame(armControl)
DerechaControl.place(x=605, y=150)
DerechaLabel = Label(DerechaControl, text = "Derecha", padx = 100, borderwidth = 2, relief="ridge")
DerechaLabel.pack()
Derecha = Scale(DerechaControl, from_= 0, to = 180, length = 300, orient = HORIZONTAL,tickinterval=30, command = Mover)
Derecha.set(140)
Derecha.pack()
#Velocidad
VelocidadLabel = Label(armControl, text = "Velocidad(En proceso..)",padx = 100, borderwidth = 2, relief="ridge")  #TERMINAR SLIDER VELOCIDAD FALTA DEFINIR FUNCION, SCRIPT ARDUINO
VelocidadLabel.pack()
Velocidad = Scale(armControl, from_= 0, to = 180, length = 300, orient = HORIZONTAL,tickinterval=30, command = Mover)
Velocidad.set(0)
Velocidad.pack()

root.mainloop()