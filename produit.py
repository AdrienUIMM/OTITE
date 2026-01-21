class Produit : 
    
    material_density_kg_m3 = {"Bois": 700 ,"Verre" : 2500, "Acier" : 7700 , "Aluminium" : 2700}
    
    
    def __init__(self,material,length, width, height) : 
    
        self.__material = material 
        self.__length_m = length /1000
        self.__width_m = width / 1000
        self.__height_m = height / 1000
        self.__volume_m3 = self.ComputeVolume()
        self.__mass_kg = self.ComputeMass()
        
    def __str__(self):
        
        texte = "Matériel :" + self.__material + "\n Length =  " + str(self.__length_m) +"\n Width = " + str(self.__width_m)  +"\n Height=" + str(self.__height_m) +"\n Volume = " + str(self.__volume_m3) + "\n Masse = " + str(self.__mass_kg)
        return texte
    
    def ComputeVolume(self) : 
        return self.__length_m * self.__width_m * self.__height_m
    
    def ComputeMass(self) : 
        densite = self.material_density_kg_m3[self.__material]
        return densite*self.__volume_m3
    
    @property
     def length(self):
        return self.__length_m
    
    @length.setter
        def length(self, l):
        self.__length_m = l / 1000.0
        self.__volume_m3 = self.ComputeVolume()
        self.__mass_kg = self.ComputeMass()
        
#Début du main
#___________________________________________________________________________
       
if __name__ == "__main__":
    
    prod1 = Produit("Bois",500,500,500)
    print(prod1)
    prod1.__length_m = 1000
    print(prod1)
    
    
    
    
    


        
        