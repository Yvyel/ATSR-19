# defines class with set peramiters 

# import sys
import sys

class DragonFly:

    def print(self):
    	print("Here is our DragonFly!")
    	print(f"Number of wings = {self.num_wings}")
    	print(f"Length of DragonFly = {self.length}")
    	print(f"Weight of DragonFly = {self.weight_mg}")

    def __init__(self,nwings=4,length=1,weightmg=1.):
    	self.num_wings   = nwings
    	self.length      = length
    	self.weight_mg   = weightmg

def main():

    nwings = 3
    length = 30
    weightmg = 600


    if(len(sys.argv)>=2):
    	nwings = int(sys.argv[2])

    if(len(sys.argv)>=3):
    	length = float(sys.argv[2])

    if(len(sys.argv)>=4):
        weightmg = str(sys.argv[2])

    our_DragonFly = DragonFly(nwings=nwings,length=length,weightmg=weightmg)

    our_DragonFly.print()

if __name__=="__main__":
    main()
	

