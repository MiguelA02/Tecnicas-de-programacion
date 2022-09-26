from contextlib import nullcontext


def openNewWindow(operacion): 
    def sumar():
        resultado.set(float(primerNumero.get()) + float(segundoNumero.get()))
        limpiar()
    def restar():
        resultado.set(float(primerNumero.get()) - float(segundoNumero.get()))
        limpiar()
    def multiplicacion():
        resultado.set(float(primerNumero.get()) * float(segundoNumero.get()))
        limpiar()
    def division():
        resultado.set(float(primerNumero.get()) / float(segundoNumero.get()))
        limpiar()
    def esPrimo():
        for i in range (2, int(primerNumero.get())):
            if(int(primerNumero.get())%i == 0):
                resultado.set("No es primo")
                return   
        resultado.set("Es primo")
    def esPalindromo():
        numberString = str(primerNumero.get())
        reverseString = ''.join(reversed(numberString))
        if (numberString == reverseString):
            resultado.set("Es palindromo")
            return
        resultado.set("No es palindromo")
    def limpiar():
        primerNumero.set("")
        segundoNumero.set("")    

    newWindow = Toplevel(root) 
    newWindow.title("New Window") 
    newWindow.geometry("400x200") 

    primerNumero = StringVar();
    segundoNumero = StringVar();
    resultado = StringVar();


    def template(funcion, simbolo):
        if(simbolo == nullcontext):
            PrimerEntry = Entry(newWindow, justify="center", textvariable= primerNumero).pack()
            Espacio = Label(newWindow, justify="center", text= "").pack()
            TercerEntry = Entry(newWindow, justify="center", textvariable= resultado).pack()
            boton = Button(newWindow, text= "Consultar", command= funcion)
            boton.pack();
        else:
            PrimerEntry = Entry(newWindow, justify="center", textvariable= primerNumero).pack()
            operador = Label(newWindow, justify="center", text= simbolo).pack()
            SegundoEntry = Entry(newWindow, justify="center", textvariable= segundoNumero).pack()
            igual = Label(newWindow, justify="center", text= "=").pack()
            TercerEntry = Entry(newWindow, justify="center", textvariable= resultado).pack()
            boton = Button(newWindow, text= "Consultar", command= funcion).pack()

    codigoSumar = 1
    codigoRestar = 2
    codigoMultiplicacion = 3
    codigoDivision = 4
    codigoEsPrimo = 5
    codigoEsPalimdromo = 6

    if operacion == codigoSumar:
        template(sumar, "+")
    if operacion == codigoRestar:
        template(restar, "-")
    if operacion == codigoMultiplicacion:
        template(multiplicacion, "x")
    if operacion == codigoDivision:
        template(division, "/")
    if operacion == codigoEsPrimo:
        template(esPrimo, nullcontext)
    if operacion == codigoEsPalimdromo:
        template(esPalindromo, nullcontext)
    else:
        print('')

    
    
    
from tkinter import * 
root = Tk()
root.config(bd=90);


def ventanaSumar():
    openNewWindow(1)

def ventanaRestar():
    openNewWindow(2)

def ventanaMultiplicacion():
    openNewWindow(3)

def ventanaDivision():
    openNewWindow(4)

def ventanaEsPrimo():
    openNewWindow(5)
def ventanaEsPalimdromo():
    openNewWindow(6)


botonVentanaSumar = Button(root, text = "Sumar", command=ventanaSumar)
botonVentanaSumar.pack()

botonVentanaResta= Button(root, text = "Resta", command=ventanaRestar)
botonVentanaResta.pack()

botonVentanaMultiplicacion = Button(root, text = "Multiplicacion", command=ventanaMultiplicacion)
botonVentanaMultiplicacion.pack()

botonVentanaDivision = Button(root, text = "Division", command=ventanaDivision)
botonVentanaDivision.pack()

botonVentanaPrimo = Button(root, text ="Es primo?", command=ventanaEsPrimo)
botonVentanaPrimo.pack()

botonVentanaPalindromo = Button(root, text ="Es palindromo?", command=ventanaEsPalimdromo)
botonVentanaPalindromo.pack()



