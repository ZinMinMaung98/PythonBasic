class circle:
    def getr(self,r):
        self.r = r

    def geta(self):
        self.a = 3.14* self.r*self.r
        return  self.a

c1 = circle()
c1.getr(343)
print("Area result is : ",end="")
print(str(c1.geta()))
