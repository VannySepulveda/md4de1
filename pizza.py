import datos as d
class Pizza():
    def __init__(self):
        self.precio= 10000
        self.porte='familiar'
        self.ingVeg1=""
        self.ingVeg2=""
        self.ingCar =""
        self.salsa=""
        self.masa=""
    
    def asigna_masa(self,masa):
        self.masa=masa
        if self.masa == 't' or self.masa == 'T':
            self.masa = "Tradicional"
        elif self.masa == 'd' or self.masa == 'D':
            self.masa = "Delgada"
        print(f"Su masa es {self.masa}")
    
    def asigna_salsa(self,sal):   
        if self.salsa == "": 
            if sal==1:self.salsa=d.salsas[0]
            elif sal==2:self.salsa=d.salsas[1]
        print("Su salsa es ", self.salsa)
    def asigna_veg(self,veg):
        if self.ingVeg1=="":
            if veg==1:self.ingVeg1=d.ing_veg[0]
            elif veg==2:self.ingVeg1=d.ing_veg[1]
            elif veg==3:self.ingVeg1=d.ing_veg[2]
            print(self.ingVeg1, "agregado ok")    
        elif self.ingVeg2=="":
            if veg==1:self.ingVeg2=d.ing_veg[0]
            elif veg==2:self.ingVeg2=d.ing_veg[1]
            elif veg==3:self.ingVeg2=d.ing_veg[2]                  
            print(self.ingVeg1," y ", self.ingVeg2, "agregados ok") 

    def asigna_car(self,car):   
        if self.ingCar == "": 
            if car==1:self.ingCar=d.ing_car[0]
            elif car==2:self.ingCar=d.ing_car[1]
            elif car==3:self.ingCar=d.ing_car[2]
        print("agregamos ", self.ingCar,"!!!") 
    
    
       
orden = Pizza()
        
# ELECCION DE MASA
ms=input("¿Quiere una masa tradicional o delgada? (T/D): ")
if ms.upper()  in ['T', 'D']:orden.asigna_masa(ms)
else:
    ms=input("Debe elegir una masa tradicional o delgada? (T/D): ")
    if ms.upper() in ['T', 'D']:orden.asigna_masa(ms)
    else:exit()

# ELECCION DE SALSAS
sal=input(d.MSalsa)
if sal in ['1','2']:orden.asigna_salsa(int(sal))
else:exit()
 
# ELECCION DE VG
i=1
while i <= 2:
    veg=input(d.Ming_veg)
    if veg in ['1','2','3']:orden.asigna_veg(int(veg))
    else:exit()
    i += 1
 
# ELECCION DE CARNE
car=input(d.Ming_car)
if car in ['1','2','3']:orden.asigna_car(int(car))
else:exit()      

print("Su pedido esta Ok:\n Masa ",orden.masa,"con ",orden.salsa,"\n Ingredientes:", orden.ingVeg1,orden.ingVeg2,orden.ingCar, "\n El precio es: $", orden.precio,"\n Tamaño", orden.porte, "\n Gracias por su compra")