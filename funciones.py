print("Ejemplo de funciones")
# declarando funciones
def hola():
    print("Alguien uso la funcion hola")
    
def chat(mensa):
    print(f"Chat {mensa}")
    
def ellacontesta(mensa):
    print(f"chat ella :{mensa}")
    
def escribenombre(ap,n):
    print(f"Tu nombre completo es :{n} {ap}")
    
def suma(a,b):
    s=a+b
    return s


# llamadas a funciones
hola()
chat("que bonita estas")
ellacontesta("gracias")
escribenombre("Nava","Eliseo")
print("Operacion suma")
c1=int(input("ingresa un numero"))
c2=int(input("ingresa un numero"))
damesuma=suma(c1,c2)
print(f"La suma de {c1} + {c2} = {damesuma}")