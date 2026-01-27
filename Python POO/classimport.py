import Cellule
from Robot import Robot as ro
import multirobot as mr

if __name__ == "__main__":
    
    cell = Cellule.Cellule()
    rob1 = ro()
    rob2 = mr.MultiRobot(3)

print("Mode Courant = ",cell.GetMode())
rob1.GetStatus()

print(rob1.GetStatus())
print(rob1)

rob2.MoveHome()
rob2.RaiseDefault()
print(rob2)
    
    
    
