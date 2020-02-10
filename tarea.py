from sys import exit

def countIf(p, it):
    i = 0

    for x in it:
        if p(x):
            i += 1

    return i 

class Archivo:
    def __init__(self,nombre):
        try: 
            self.nombre = nombre
            self.f = open(self.nombre,'r')
        except:        
            print(f'Error abriendo archivo {self.nombre}')
            exit(0)

    def muestra(self,cad=''):
        if cad == '':
            i=1  
            for linea in self.f:
                print('{:3}:    {}'.format(i,linea),end="")
                i +=1
            self.f.seek(0)
        elif cad == 'hex':
            i=1
            for linea in self.f:
                print('{:3}:    {}'.format(hex(i),linea),end="")
                i +=1
            self.f.seek(0)      
    
    def cuentaVocales(self):
        contador = 0

        for linea in self.f:
            contador += countIf(lambda x: x.lower() in set("aàeèiìoòuù"), linea)
        self.f.seek(0)

        return contador

    def cuentaConsonantes(self):
        contador = 0

        for linea in self.f:
            contador += countIf(lambda x: x.lower() in set("qwrtyplkjhgfdszxcvbnm"), linea)
        self.f.seek(0)

        return contador

    def copiaArchivo(self, nuevo):
        new = open(nuevo ,"w")

        for linea in self.f:
            new.write(linea)
        self.f.seek(0);
            
    def cuentaSignos(self):
        contador = 0

        for linea in self.f:
            contador += countIf(lambda x: x.lower() in set(".:,'"';'), linea)
        self.f.seek(0)

        return contador
    
    def cuentaEspacios(self):
        contador = 0

        for linea in self.f:
            contador += countIf(lambda x: x.lower() in set(" "), linea)
        self.f.seek(0)

        return contador

    def cuentaPalabras(self):
        def isPalabra(s):
            contador = 0
            cadena = ''

            for i in range (len(s)):
                if s[i] in set(' '):
                    if cadena.isalpha(): 
                        contador +=1
                    cadena = '' 
                else:
                    cadena = cadena + s[i]

            if cadena != '' and cadena.isalpha(): 
                contador  += 1
            return contador 

        contador = 0
        for linea in self.f:
            contador += isPalabra(linea)
        self.f.seek(0)
        return contador

    def cuentaLineas(self):
        contador = 0

        for linea in self.f.readlines():
            contador += 1
        self.f.seek(0)

        return contador    

    def cuentaMayusculas (self):
        contador = 0

        for linea in self.f:
            contador += countIf(lambda x: x.lower() in set("QWERTYUIOPASDFGHJKLZXCVBNMÁÉÍÓÚ"), linea)
        self.f.seek(0)

        return contador
    
    def cuentaMinusculas (self):
        contador = 0

        for linea in self.f:
            contador += countIf(lambda x: x.lower() in set('qwertyuiopasdfghjklzxcvbnmáéíóú'), linea)
        self.f.seek(0)

        return contador

    def convertirMayusculas(self):
        for linea in self.f:
            print(linea.upper())  

        self.f.seek(0)

    def convertirMinusculas(self):
        for linea in self.f:
            print(linea.lower())

        self.f.seek(0)
    
    def convertirHexadecimal(self):
        for linea in self.f:
            for i in range(len(linea)):
                print(hex(int(linea[i])))

        self.f.seek(0);


if __name__ == "__main__":
    nombre = input("Introduzca el nombre del archivo: ")
    newArchivo = Archivo(nombre)
    
    while(True):
        print('\n')
        print('  1.- Mostrar archivo\n',
              ' 2.- Contar vocales\n',
              ' 3.- Contar consonantes\n',
              ' 4.- Contar signos de puntuación\n',
              ' 5.- Contar espacios\n',
              ' 6.- Contar palabras\n',
              ' 7.- Contar Lineas\n',
              ' 8.- Contar mayúsculas\n',
              ' 9.- Contar minusculas\n',
              '10.- Copiar archivo\n',
              '11.- Convertir todo a mayusculas\n',
              '12.- Convertir todo a minusculas\n',
              '13.- Mostrar hexadecimal\n',
              '0.- Salir\n')

        opcion  =  int(input('Seleccione una opción:'))

        if(opcion  == 0):
            exit(0)
        elif(opcion == 1):
            newArchivo.muestra()
        elif(opcion == 2):
            print(f'hay {newArchivo.cuentaVocales()} vocales')
        elif(opcion == 3):
            print(f'hay {newArchivo.cuentaConsonantes()} consonantes')
        elif(opcion == 4):
            print(f'hay {newArchivo.cuentaSignos()} signos de puntuación')
        elif(opcion == 5):
            print(f'hay {newArchivo.cuentaEspacios()} espacios')
        elif(opcion == 6):
            print(f'hay {newArchivo.cuentaPalabras()} palabras')
        elif(opcion == 7):
            print(f'hay {newArchivo.cuentaLineas()} lineas')
        elif(opcion == 8):
            print(f'hay {newArchivo.cuentaMayusculas()} mayúsculas')
        elif(opcion == 9):
            print(f'hay {newArchivo.cuentaMinusculas()} minúsculas')
        elif(opcion == 10):
            nuevo = input("ingrese un nuevo nombre de archivo: ")
            newArchivo.copiaArchivo(nuevo) 
        elif(opcion == 11):
            newArchivo.convertirMayusculas()
        elif(opcion == 12):
            newArchivo.convertirMinusculas() 
        elif(opcion == 13):
            newArchivo.convertirHexadecimal()
        else:
            print('Opción no válida, intente de nuevo')
        
