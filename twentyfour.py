class student :
    def __init__(self,name,sub1,sub2,sub3):

        self.name = name
        self.sub1 = sub1
        self.sub2 = sub2
        self.sub3 = sub3
    def avg(self):
            average = int(self.sub1+self.sub2+self.sub3)/3
            print(average)
        


s1 = student("shreya",67,78,90)
s1.avg()