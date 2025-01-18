from tkinter import ttk
from tkinter import *

from PIL import ImageTk, Image


#funciones
def click(valor):
    global texto
    texto=texto+str(valor)
    datos.set(texto)
def resultado():
    global texto
    operacion=str(eval(texto))
    datos.set(operacion)
def borrado():
    global texto
    texto=('')
    datos.set('0')
def guardado():
    tomaDato=int(posicion.get())
    tomaDato1=int(posicion1.get())
    tomaDato2=int(posicion2.get())
    almacen.extend([tomaDato,tomaDato1,tomaDato2])
    mayor=max(almacen)
    menor=min(almacen)
    d1.set(almacen)
    d2.set(mayor)
    d3.set(menor)
    numerosPares=[]
    for y in almacen:
        if y % 2 ==0:
            numerosPares.append(y)
    p4.set(numerosPares)

    
#información del pagina
libreria=Tk()
libreria.title('calculadora')
pestaña=Frame(libreria, width=600, height=400)
pestaña.pack()
#estilo del aplicativo
#imagen de fondo
imagen=ImageTk.PhotoImage(Image.open(r'C:\Users\Juamp\OneDrive\Desktop\programación\calculadora\fondo.jpg').resize((600, 400)))
fondo=Label(pestaña,image=imagen)
fondo.place(x=0,y=0)

#imagen icono
libreria.iconbitmap('C:\\Users\\Juamp\\OneDrive\\Desktop\\programación\\calculadora\\icono.ico')
s=ttk.Style()
s.configure('Estilo.TButton', foreground='red')
s.map('Estilo.TButton', background=[('active','blue')])

#variables que almacenaran la informacion
datos=StringVar()
texto=('')
d1=StringVar()
d1.set('')
d2=StringVar()
d2.set('')
d3=StringVar()
d3.set('')
p4=StringVar()
p4.set('')
almacen=[]
#entrada de información
pantalla=Entry(pestaña, font=('Tiny 20'), width=17, textvariable=datos).place(x=190,y=10)
#Entrada de datos a lista
posicion=Entry(pestaña, font=('Tiny 20'), width=3)
posicion.place(x=190, y=270)
posicion1=Entry(pestaña, font=('Tiny 20'), width=3)
posicion1.place(x=290, y=270)
posicion2=Entry(pestaña, font=('Tiny 20'), width=3)
posicion2.place(x=390, y=270)
#botones acciones
borrado=ttk.Button(pestaña, text='AC', width=5,command=borrado, style='Estilo.TButton').place(x=190, y=60)
punto=Button(pestaña, text='.', width=5, command=lambda:click('.')).place(x=330, y=220)
igual=Button(pestaña, text='=', width=5, command=resultado).place(x=400, y=220)
paren1=Button(pestaña, text='(', width=5, command=lambda:click('(')).place(x=260, y=60)
paren2=Button(pestaña, text=')', width=5, command=lambda:click(')')).place(x=330, y=60)
dividir=Button(pestaña, text='÷', width=5, command=lambda:click('/')).place(x=400, y=60)
multi=Button(pestaña, text='x', width=5, command=lambda:click('*')).place(x=400, y=100)
suma=Button(pestaña, text='+', width=5, command=lambda:click('+')).place(x=400, y=140)
resta=Button(pestaña, text='-', width=5, command=lambda:click('-')).place(x=400, y=180)
orga=ttk.Button(pestaña, text='Evaluar', width=6, command=guardado).place(x=290, y=320)

#botones numeros
bot7=Button(pestaña, text='7', width=5, command=lambda:click('7')).place(x=190, y=100)
bot4=Button(pestaña, text='4', width=5, command=lambda:click('4')).place(x=190, y=140)
bot1=Button(pestaña, text='1', width=5, command=lambda:click('1')).place(x=190, y=180)
bot0=Button(pestaña, text='0', width=15, command=lambda:click('0')).place(x=190, y=220)
bot8=Button(pestaña, text='8', width=5, command=lambda:click('8')).place(x=260, y=100)
bot5=Button(pestaña, text='5', width=5, command=lambda:click('5')).place(x=260, y=140)
bot2=Button(pestaña, text='2', width=5, command=lambda:click('2')).place(x=260, y=180)
bot9=Button(pestaña, text='9', width=5, command=lambda:click('9')).place(x=330, y=100)
bot6=Button(pestaña, text='6', width=5, command=lambda:click('6')).place(x=330, y=140)
bot3=Button(pestaña, text='3', width=5, command=lambda:click('3')).place(x=330, y=180)
#Escrito en pantalla
E=Label(pestaña, text='Datos:').place(x=10, y=270)
ListaDatos=Label(pestaña, textvariable=d1, width=10)
ListaDatos.place(x=60, y=270)

R_mayor=Label(pestaña, text='Mayor:').place(x=10, y=300)

D_mayor=Label(pestaña, textvariable=d2, width=5)
D_mayor.place(x=60,y=300)

R_menor=Label(pestaña, text='Menor:').place(x=10, y=330)

D_menor=Label(pestaña, textvariable=d3, width=5)
D_menor.place(x=60, y=330)
pares=Label(pestaña, text='Pares:').place(x=10,y=360)

R_pares=Label(pestaña, textvariable=p4, width=10)
R_pares.place(x=60, y=360)

libreria.mainloop()
