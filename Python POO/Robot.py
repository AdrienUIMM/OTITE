class Robot :  
    
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



    


if __name__ == "__main__":

    print(Robot.marque) # utilisation attribut de class sans instanciation

    rob1 = Robot() # premiere instance de robot
    rob2 = Robot() # seconde instance de robot

    # Ordres sur robot 1
    rob1.GetStatus()
    rob1.MoveHome()
    rob1.RaiseDefault()
    rob1.GetStatus()
    rob1.ClearDefault()
    rob1.GetStatus()

    # Ordres sur robot 2
    rob2.GetStatus()
    rob2.RaiseDefault()
    rob2.GetStatus()
