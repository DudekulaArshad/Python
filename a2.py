
class NumberWave:
    def __init__(self):
        self.levels=0
    def inputDetails(self):
        self.levels=int(input().strip())
    def printPattern(self):
        pass
class ReverseNumberWave(NumberWave):
    def printPattern(self):
        for i in range(1,self.levels+1):
            for j in range(i,0,-1):
                if j==1:
                    print(j,end="")
                else:
                    print(j,end=" ")

wave=ReverseNumberWave()
wave.inputDetails()
wave.printPattern()

