import tkinter as tk
from tkinter import ttk
import json
import re

regularfont = ('arial', 12, 'normal')
boldfont = ('arial', 12, 'bold')


#══════════════════════════VENTANA ROOT════════════════════

class windows(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.wm_title("Test")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.config(bg = "lightblue", height = 500, width = 500)


        self.frames = {}
        for F in (LoginPage, MainPage, BasesClientes, BasesProductos, Facturacion):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(LoginPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

#══════════════════════════VENTANA LOGIN════════════════════

class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent)
        global frameLogin
        frameLogin = tk.Frame(self)
        frameLogin.config(bg = "lightblue", height = 500, width = 500)
        frameLogin.pack(side="bottom", fill="both", expand = True)

        UsuarioLabel = tk.Label(frameLogin, text='Usuario', font = regularfont).pack(side="top")
        global userEntry
        userEntry = ttk.Entry(frameLogin)
        userEntry.pack()

        PasswordLabel = tk.Label(frameLogin, text='Password', font = regularfont).pack()
        global passwordEntry
        passwordEntry = ttk.Entry(frameLogin, show = "*")
        passwordEntry.pack()

        BotonLogin = ttk.Button(frameLogin, text='Login', command = self.botonLogin).pack()
        

    def botonLogin(self):
        usuario = userEntry.get()
        contra = passwordEntry.get()
        with open('UserPassword.txt') as f: 
            data = f.read() 
        userPass = json.loads(data) 

        if (usuario in userPass) and (contra == userPass[usuario]):
            print("Inicio de sesión exitoso!")
            loginAccept = tk.Toplevel(frameLogin)
            loginAccept.title("Contraseña Correcta")
            Acceptlabel = tk.Label(loginAccept, text= "Contraseña Correcta!", font = boldfont).pack()
            Okbutton = ttk.Button(loginAccept, text= "Ok", command = lambda:[self.controller.show_frame(MainPage),loginAccept.withdraw()]).pack()
            
        else:
            print("Contraseña incorrecta.")
            loginDeny = tk.Toplevel(frameLogin)
            loginDeny.title("Contraseña Incorrecta")
            Denylabel = tk.Label(loginDeny, text= "Contraseña Incorrecta!", font = boldfont).pack()
            Okbutton = ttk.Button(loginDeny, text= "Ok", command = loginDeny.destroy).pack()

#══════════════════════════VENTANA MENU PRINCIPAL════════════════════

class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        frameMain = tk.Frame(self)
        frameMain.config(bg = "lightblue", height = 500, width = 500)
        frameMain.pack(side="top", fill="both", expand = True)
        label = tk.Label(frameMain, text = "▓▓▓▓ MENU PRINCIPAL ▓▓▓▓")
        label.pack(padx=10, pady=10)


        boton_bases_clientes = tk.Button(
            frameMain,
            text = "Bases de datos de Clientes",
            command = lambda: controller.show_frame(BasesClientes)
        )
        boton_bases_clientes.pack(side = "top", fill = tk.X)

        boton_bases_productos = tk.Button(
            frameMain,
            text = "Bases de datos de Productos",
            command = lambda: controller.show_frame(BasesProductos)
        )
        boton_bases_productos.pack(side = "top", fill = tk.X)
        

        boton_facturacion = tk.Button(
            frameMain,
            text = "Facturación",
            command = lambda: controller.show_frame(Facturacion)
        )
        boton_facturacion.pack(side = "top", fill = tk.X)

        boton_salir = tk.Button(
            frameMain,
            text = "Salir",
            command = quit
        )
        boton_salir.pack(side = "top", fill = tk.X)
        

#══════════════════════════BASES DE DATOS DE CLIENTES════════════════════

class BasesClientes(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        BasesClientes = tk.Frame(self)
        BasesClientes.config(bg = "lightblue", height = 500, width = 500)
        BasesClientes.pack(side="top", fill="both", expand = True)

        label = tk.Label(BasesClientes, text ="▓▓▓▓ BASE DE DATOS DE CLIENTES ▓▓▓▓")
        label.pack(padx=10, pady=10)

        global murodetexto
        murodetexto = tk.Text(BasesClientes, width= 50, height = 25)
        murodetexto.pack()

        scroll = tk.Scrollbar(self, command = murodetexto.yview)
        scroll.pack(side="right", fill = "y")

        boton_Agregar = ttk.Button(
            self,
            text = "Agregar nuevo Cliente",
            command = self.AgregarCliente
        )
        boton_Agregar.pack(side="top", fill=tk.X)

        boton_Ver = ttk.Button(
            self,
            text = "Ver Clientes",
            command = self.VerCliente
        )
        boton_Ver.pack(side="top", fill=tk.X)


        boton_Volver = ttk.Button(
            self,
            text = "Volver al menu anterior",
            command = lambda: controller.show_frame(MainPage)
        )
        boton_Volver.pack(side="top", fill=tk.X)

    def AgregarCliente(self):
        global Agregar
        Agregar = tk.Toplevel(BasesClientes)
        Agregar.title("Agregar Cliente")
        Agregarlabel = tk.Label(Agregar, text= "Por favor intrudzca los datos", font = boldfont).pack()
        Okbutton = ttk.Button(Agregar, text= "Ok", command = self.NuevoCliente)
        Okbutton.pack(side="bottom")

        newNameLabel = tk.Label(Agregar, text='Nombre', font = regularfont).pack(side="top")
        global newNameEntry
        newNameEntry = ttk.Entry(Agregar)
        newNameEntry.pack()

        newIDLabel = tk.Label(Agregar, text='Cedula', font = regularfont).pack(side="top")
        global newIDEntry
        newIDEntry = ttk.Entry(Agregar)
        newIDEntry.pack()

        newDireccionLabel = tk.Label(Agregar, text='Direccion', font = regularfont).pack(side="top")
        global newDireccionEntry
        newDireccionEntry = ttk.Entry(Agregar)
        newDireccionEntry.pack()

        newTelLabel = tk.Label(Agregar, text='Telefono', font = regularfont).pack(side="top")
        global newTelEntry
        newTelEntry = ttk.Entry(Agregar)
        newTelEntry.pack()

    def NuevoCliente(self):
        newNombre = newNameEntry.get()
        newCedula = newIDEntry.get()
        newDireccion = newDireccionEntry.get()
        newTelefono = newTelEntry.get()
        with open("Clientes.txt", "a") as f:
            f.write("\n"+str(line_count+1)+", "+
                    str(newNombre)+", "+
                    str(newCedula)+", "+
                    str(newDireccion)+", "+
                    str(newTelefono))
        Agregar.withdraw()
        murodetexto.insert(tk.INSERT,"Cliente agregado satisfactoriamente."+
                           "\nPor favor, cierre el programa y vuelvalo a abrir ver al cliente en la base de datos")
        
    def VerCliente(self):
        for i in range (0,line_count):
            murodetexto.insert(tk.INSERT,"\nCodigo: " + Customer[i].Codigo
                               +"\nNombre: "+ Customer[i].Nombre
                               +"\nCedula: "+ Customer[i].Cedula
                               +"\nDireccion: "+ Customer[i].Direccion
                               +"\nTelefono: "+ Customer[i].Telefono
                               +"\n")


#════CLASE CLIENTE════
Customer = []

class Cliente:
    def __init__(self,Codigo,Nombre,Cedula,Direccion,Telefono):
        self.Codigo = Codigo
        self.Nombre = Nombre
        self.Cedula = Cedula
        self.Direccion = Direccion
        self.Telefono = Telefono

file = open ("Clientes.txt", "r")
specificline = file.readlines()
line_count = len(specificline)

for i in range(0,line_count):
    content = specificline[i] 
    pattern = r", "
    parts = re.split(pattern, content)

    Customer.append([i])

    Customer[i] = Cliente(parts[0],
                       parts[1],
                       parts[2],
                       parts[3],
                       parts[4])

#══════════════════════════BASES DE DATOS DE PRODUCTOS════════════════════

class BasesProductos(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        BasesProductos = tk.Frame(self)
        BasesProductos.config(bg = "lightblue", height = 500, width = 500)
        BasesProductos.pack(side="top", fill="both", expand = True)

        label = tk.Label(BasesProductos, text ="▓▓▓▓ BASE DE DATOS DE PRODUCTOS ▓▓▓▓")
        label.pack(padx=10, pady=10)

        global murodetexto2
        murodetexto2 = tk.Text(BasesProductos, width= 50, height = 25)
        murodetexto2.pack()

        scroll = tk.Scrollbar(self, command = murodetexto2.yview)
        scroll.pack(side="right", fill = "y")

        boton_Ver = ttk.Button(
            self,
            text = "Ver Productos",
            command = self.VerProducto
        )
        boton_Ver.pack(side="top", fill=tk.X)

        boton_Volver = ttk.Button(
            self,
            text = "Volver al menu anterior",
            command = lambda: controller.show_frame(MainPage)
        )
        boton_Volver.pack(side="top", fill=tk.X)
      
    def VerProducto(self):
        for i in range (0,line_count):
            murodetexto2.insert(tk.INSERT,"\nCodigo: " + Products[i].Codigo
                               +"\nNombre: "+ Products[i].Nombre
                               +"\nPrecio: "+ Products[i].Precio
                               +"\n")

#════CLASE PRODUCTOS════
Products = []

class Producto:
    def __init__(self,Codigo,Nombre,Precio):
        self.Codigo = Codigo
        self.Nombre = Nombre
        self.Precio = Precio

file = open ("Productos.txt", "r")
specificline = file.readlines()
line_count = len(specificline)

for i in range(0,line_count):
    content = specificline[i] 
    pattern = r", "
    parts = re.split(pattern, content)

    Products.append([i])

    Products[i] = Producto(parts[0],
                       parts[1],
                       parts[2])

#══════════════════════════MODULO DE FACTURACIÓN════════════════════

class Facturacion(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        Facturacion = tk.Frame(self)
        label = tk.Label(self, text ="▓▓▓▓ MÓDULO DE FACTURACIÓN ▓▓▓▓")
        label.pack(padx=10, pady=10)

        global murodetexto3
        murodetexto3 = tk.Text(self, width= 50, height = 25)
        murodetexto3.pack()

        boton_NuevaFactura = ttk.Button(
            self,
            text = "Nueva Factura",
            command = self.NuevaFactura
        )
        boton_NuevaFactura.pack(side="top", fill=tk.X)

        boton_Volver = ttk.Button(
            self,
            text = "Volver al menu anterior",
            command = lambda: controller.show_frame(MainPage)
        )
        boton_Volver.pack(side="top", fill=tk.X)
        
    def NuevaFactura(self):
        global NuevaFactura
        NuevaFactura = tk.Toplevel(frameLogin)
        NuevaFactura.title("Nueva Factura")
        NuevaFacturaLabel = tk.Label(NuevaFactura, text= "Por favor intrudzca los datos", font = boldfont).pack()
        Okbutton = ttk.Button(NuevaFactura, text= "Ok", command = self.CrearFactura)
        Okbutton.pack(side="bottom")

        newNameLabel = tk.Label(NuevaFactura, text='Nombre', font = regularfont).pack(side="top")
        global NameEntry
        NameEntry = ttk.Entry(NuevaFactura)
        NameEntry.pack()

        newIDLabel = tk.Label(NuevaFactura, text='Cedula', font = regularfont).pack(side="top")
        global IDEntry
        IDEntry = ttk.Entry(NuevaFactura)
        IDEntry.pack()

        newDireccionLabel = tk.Label(NuevaFactura, text='Direccion', font = regularfont).pack(side="top")
        global DireccionEntry
        DireccionEntry = ttk.Entry(NuevaFactura)
        DireccionEntry.pack()

        TelLabel = tk.Label(NuevaFactura, text='Telefono', font = regularfont).pack(side="top")
        global TelEntry
        TelEntry = ttk.Entry(NuevaFactura)
        TelEntry.pack()

        ProdLabel = tk.Label(NuevaFactura, text='Código del producto comprado', font = regularfont).pack(side="top")
        global ProdEntry
        ProdEntry = ttk.Entry(NuevaFactura)
        ProdEntry.pack()

        QuantLabel = tk.Label(NuevaFactura, text='Cantidad Comprada', font = regularfont).pack(side="top")
        global QuantEntry
        QuantEntry = ttk.Entry(NuevaFactura)
        QuantEntry.pack()

        AmountLabel = tk.Label(NuevaFactura, text='Monto que está pagando', font = regularfont).pack(side="top")
        global AmountEntry
        AmountEntry = ttk.Entry(NuevaFactura)
        AmountEntry.pack()

        

    def CrearFactura(self):
        FNombre = NameEntry.get()
        FCedula = IDEntry.get()
        FDireccion = DireccionEntry.get()
        FTelefono = TelEntry.get()
        FProducto = int(ProdEntry.get())
        FMonto = int(AmountEntry.get())
        FQuant = int(QuantEntry.get())
        NuevaFactura.withdraw()

        murodetexto3.insert(tk.INSERT,"\nAquí está la factura"+
                            "\nNombre: " +str(FNombre)+
                            "\nCedula: " +str(FCedula)+
                            "\nDireccion: " +str(FDireccion)+
                            "\nTelefono: " +str(FTelefono)+ "\n"+
                            "\nCodigo: " + Products[FProducto].Codigo+
                            "\nNombre: "+ Products[FProducto].Nombre+
                            "\nPrecio: "+ Products[FProducto].Precio+
                            "\nCantidad: "+str(FQuant)+
                            "\nMonto a pagar: "+str((FQuant*int(Products[FProducto].Precio)))+
                            "\nMonto Pagado: "+str(FMonto)+
                            "\nVuelto: "+str(FMonto-(FQuant*int(Products[FProducto].Precio))))

        file1 = open("Factura.txt", "w")
        file1.writelines("\nNombre: " +str(FNombre)+
                            "\nCedula: " +str(FCedula)+
                            "\nDireccion: " +str(FDireccion)+
                            "\nTelefono: " +str(FTelefono)+ "\n"+
                            "\nCodigo: " + Products[FProducto].Codigo+
                            "\nNombre: "+ Products[FProducto].Nombre+
                            "\nPrecio: "+ Products[FProducto].Precio+
                            "\nCantidad: "+str(FQuant)+
                            "\nMonto a pagar: "+str((FQuant*int(Products[FProducto].Precio)))+
                            "\nMonto Pagado: "+str(FMonto)+
                            "\nVuelto: "+str(FMonto-(FQuant*int(Products[FProducto].Precio))))
        file1.close()
        


if __name__ == "__main__":
    testObj = windows()
    testObj.mainloop()

