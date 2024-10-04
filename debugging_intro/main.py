class Class():
    def __init__(self):
        self.x = 0 
    def add(self, a, b):
        return a + b

    def multiply(self, a, c):
        prod = 0
        for i in range(c):
           prod = self.add(prod ,a) 
        
        return prod
    
if __name__ == "__main__":
    c = Class()
    print(c.multiply(5, 10))
