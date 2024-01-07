class Math:
    
    # static methods are used inside class to organize functions and to move it around easily    

    @staticmethod
    def add5(x):
        return x + 5
    
    @staticmethod
    def add10(x):
        return x + 10
    
    @staticmethod
    def pr():
        print("run")
        
Math.pr()
print(Math.add10(5))