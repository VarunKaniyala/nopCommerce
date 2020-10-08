# from pythonBasics.OopsDemo import Calculator
from RahulShetty.Excercises.OopsDemo import Calculator
class ChildImp(Calculator):
    num2 = 200

    def __init__(self):
        Calculator.__init__(self, 2, 10)

    # def getCompleteData(self):
    #     return self.num2 + self.num + self.Summation()


obj = ChildImp()
# print(obj.getCompleteData())
