class Robot :  
    
    marque = ("ABB", "FANUC", "Staubli")  
    state_ok = False 
    nb_alarme = 0
    pos_tool = [0,0,0]

    def GetStatus(self): 
        
        return self.state_ok 

    def MoveHome(self):  
        
        self.pos_tool = [10,10,500]
       
    def MovePick(self):  
        
        self.pos_tool = [100,30,120]  

    def MovePlace(self):  
        
        self.pos_tool = [100,150,230]

    def RaiseDefault(self):  
        
        self.state_ok = False

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
