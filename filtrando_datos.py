"""
        -------- ≪ Drilling Final Modulo 3 ≫ -------
-Dada la siguiente lista de nombres:
        ●Harry Houdini ●Newton ●David Blaine ●Hawking ●Messi ●Teller ●Eistein ●Pele ●Juanes
-Crear función mostrar_nombres(), que muestre todos los nombres dados;
-Crear función hacer_grandioso(), que agregue al nombre de los magos "El gran";
-Mostrar en pantalla:
*Todos los nombres dados; *Lista de Magos modificados; *Lista de Cientificos; y *Lista de los no definidos
"""

#Se crea función para obtener lista de nombres
def imprimir_nombres():
    for n in nombres:
        print("\t●", n)
#Se crea función para obtener solo los nombres de Magos agregando "El gran"       
def hacer_grandioso():
    for i, mg in enumerate(magos_gran):
        magos_gran[i]= f"El gran {mg}"
        print("\t●", magos_gran[i])
#Se crea función para obtener solo los nombres de Cientificos       
def imprimir_cientificos():
    for c in cientificos:
        print("\t●", c)
#Se crea función para obtener solo los nombres de Indefinidos        
def imprimir_indefinidos():
    for i in nombres:
        if i not in magos and i not in cientificos:
            indefinidos.append(i)
            print("\t●", i)
#Variable con lista de nombres
nombres= ["Harry Houdini", "Newton", "David Blaine", "Hawking", "Messi", "Teller", "Eistein", "Pele", "Juanes"]
#Variables con lista de Magos
magos= ["Harry Houdini", "David Blaine", "Teller"]
#Se clona la lista de magos nombrandola en la variable "magos_gran", para modificar lista
magos_gran= ["Harry Houdini", "David Blaine", "Teller"]
#Variable con lista de Cientificos
cientificos= ["Newton", "Hawking", "Eistein"]
#Variable vacía que se agregará a los indefinidos
indefinidos=[]
#Se usa función print para mostrar en pantalla listado de Nombres y se llama a la función correspondiente
print("")
print("════════ ≪ •NOMBRES• ≫ ════════")
imprimir_nombres()
print("")
#Se usa función print para mostrar en pantalla listado de Magos modificado y se llama a la función correspondiente
print("╭─────────────• MAGOS •────────────╮")
hacer_grandioso()
print("╰──────────────• .^. •─────────────╯")
print("")
#Se usa función print para mostrar en pantalla listado de Cientificos y se llama a la función correspondiente
print("╭══════ .CIENTIFICOS. ══════╮")
imprimir_cientificos()
print("╰═══════════ .^. ═══════════╯")
print("")
#Se usa función print para mostrar en pantalla listado de Indefinidos y se llama a la función correspondiente
print("╭────── INDEFINIDOS ──────╮") 
imprimir_indefinidos()
print("╰────────── .^. ──────────╯")
print("")
