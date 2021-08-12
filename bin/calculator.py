from tkinter import Tk, Text, Button, END
import re

class Interfaz:
    def __init__(self, ventana):

        #Inicializa la ventana con un titulo
        self.ventana=ventana
        self.ventana.title("Calculator")

        #Agregar una caja de texto para que sea la pantalla de la calculadora
        self.pantalla=Text(ventana,state="disabled",width=13,height=1,background="azure3",foreground="black",font=("Helvetica",36))
        self.pantalla.tag_configure("right", justify="right")

        #Ubicar la pantalla en la ventana
        self.pantalla.grid(row=0,column=0,columnspan=4,padx=5,pady=5)
        
        #Inicializar la operacion mostrada en pantalla como string vacio
        self.operacion=""

        #Crear los botones de la calculadora
        boton1=self.crearBoton(7)
        boton2=self.crearBoton(8)
        boton3=self.crearBoton(9)
        boton4=self.crearBoton(u"\u232B",escribir=False)
        boton5=self.crearBoton(4)
        boton6=self.crearBoton(5)
        boton7=self.crearBoton(6)
        boton8=self.crearBoton(u"\u00F7")
        boton9=self.crearBoton(1)
        boton10=self.crearBoton(2)
        boton11=self.crearBoton(3)
        boton12=self.crearBoton("*")
        boton13=self.crearBoton(".")
        boton14=self.crearBoton(0)
        boton15=self.crearBoton("+")
        boton16=self.crearBoton("-")
        boton17=self.crearBoton("=",escribir=False,ancho=27,alto=2)

        #Ubicar los botones con el gestor grid
        botones=[boton1, boton2, boton3, boton4, boton5, boton6, boton7, boton8, boton9, boton10, boton11, boton12, boton13, boton14, boton15, boton16, boton17]
        contador=0
        for fila in range(1,5):
            for columna in range(4):
                botones[contador].grid(row=fila,column=columna)
                contador+=1
        #Ubicar el ultimo boton al final
        botones[16].grid(row=5,column=0,columnspan=4)    
        return
    
    #Metodo para crear un boton con el valor que debe mostrar
    def crearBoton(self, valor, escribir=True, ancho=3, alto=1):
        return Button(self.ventana, text=valor, width=ancho, height=alto, font=("Helvetica",15), command=lambda:self.click(valor,escribir))

    def click(self, texto, escribir):
        if not escribir:
            if texto=="=" and self.operacion!="":
                self.operacion=re.sub(u"\u00F7", "/", self.operacion)
                resultado=str(eval(self.operacion))
                self.operacion=""
                self.limpiarPantalla()
                self.mostrarEnPantalla(resultado)
            elif texto==u"\u232B":
                self.operacion=""
                self.limpiarPantalla()
        else:
            self.operacion+=str(texto)
            self.mostrarEnPantalla(texto)
        return

    #Borra el contenido de la pantalla de la calculadora
    def limpiarPantalla(self):
        self.pantalla.configure(state="normal")
        self.pantalla.delete("1.0", END)
        self.pantalla.configure(state="disabled")
        return
    

    #Muestra en la pantalla de la calculadora el contenido de las operaciones y los resultados
    def mostrarEnPantalla(self, valor):
        self.pantalla.configure(state="normal")
        self.pantalla.insert(END, valor, "right")
        self.pantalla.configure(state="disabled")
        return

ventana_principal=Tk()
ventana_principal.resizable(width=False, height=False)
calculator=Interfaz(ventana_principal)
ventana_principal.mainloop()