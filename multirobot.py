class MultiRobot :  
    
    marque = "Fanuc" 
    state_ok = False 
    nb_alarme = 0
    pos_tool = [0,0,0]

    def GetStatus(self): 
        
        if self.state_ok == True:
            status = "OK"
        else:
            status = "NOK"

        print( self.marque +" Status " +status +" (" + str(self.nb_alarme) + ") " + "Position X=" + str(self.pos_tool[0]) +" Y=" + str(self.pos_tool[1]) +" Z=" + str(self.pos_tool[2]))
    

    def MoveHome(self):  
        
        self.pos_tool = [10,10,500]
       
    def MovePick(self):  
        
        self.pos_tool = [100,30,120]  

    def MovePlace(self):  
        
        self.pos_tool = [100,150,230]

    def RaiseDefault(self):  
        
        self.state_ok = False
        self.nb_alarme = self.nb_alarme + 1 ;

    def ClearDefault(self):  
        
        self.state_ok = True
    
    def __init__(self, id=1):
        
            self.id = id
            self.state_ok
            self.nb_alarme = 0
            self.pos_tool = [0,0,0]
    
    def __str__(self) : 
        if self.state_ok == True:
            status = "OK"
        else:
            status = "NOK"

        texte =  self.marque +" Status " +status +" (" + str(self.nb_alarme) + ") " + "Position X=" + str(self.pos_tool[0]) +" Y=" + str(self.pos_tool[1]) +" Z=" + str(self.pos_tool[2])
        return texte
        
    
        
            

if __name__ == "__main__":


    rob1 = MultiRobot() 
    rob2 = MultiRobot(2)
    
    
    print(rob1)
    

    rob1.MoveHome()
    rob1.RaiseDefault()
    print(rob1)
    rob1.ClearDefault()
    rob1.MovePick()
    print(rob1)
    print(rob2) 
    rob2.RaiseDefault()
    print(rob2)

    
