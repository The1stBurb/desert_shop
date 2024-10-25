class dsrtItm:
    def __init__(self,nm):#,nm):
        self.nm=nm
    def __str__(self):
        return f"Type: {self.__class__.__name__}\nName: {self.nm}\nQuantity: {self.quan}\nPrice Per: {self.pp_}"
    def cost(self):
        return self.quan*self.pp_
    def gt_nm(self):
        return self.nm
    def get_quan(self):
        return self.quan
    
class candy(dsrtItm):#("candy")
    def __init__(self,nm,weg,ppp):
        super().__init__(nm)
        self.quan=weg
        self.pp_=ppp

class cookie(dsrtItm):#("cookie")
    def __init__(self,nm,quan,ppd):
        super().__init__(nm)
        self.quan=quan
        self.pp_=ppd

class iceCream(dsrtItm):#("ice cream")
    def __init__(self,nm,scps,pps):
        super().__init__(nm)
        self.quan=scps
        self.pp_=pps

class sunday(iceCream):#("sunday")
    def __init__(self,nm,scps,pps,top,ppt):
        super().__init__(nm,scps,pps)
        self.tp=top
        self.quan=1
        self.pp_=ppt
items=[
    # candy("Candy Corn",0,0),
    # iceCream("Gummy Bears",0,0),
    # candy("Chocolate Chips",0,0),
    # sunday("Pistachio",0,0,"pistachios"),
    # iceCream("Vanilla",0,0),
    # cookie("Oatmeal Raisin",0,0),
    candy("Candy Corn", 1.5, .25),
    iceCream("Gummy Bears", .25, .35),
    candy("Chocolate Chips", 6, 3.99),
    sunday("Pistachio", 2, .79, "Hot Fudge", 1.29),
    iceCream("Vanilla", 3, .69),
    cookie("Oatmeal Raisin", 2, 3.45),
]
class order:
    def __init__(self):
        self.ord=[]
    def add(self,itm):
        quan=input(f"How many {itm.nm}s would you like? ")
        itm.quan=quan
        self.ord.append(itm)
    def __str__(self):
        return "\n".join([f"{i.quan}x {i.nm}" for i in self.ord])+f"\nOrder length: {len(self.ord)}"
    def __len___(self):
        return len(self.ord)
ord=order()
print(ord)
ord.add(items[0])
ord.add(items[3])
print(ord)
# print(candy("corn",0,0).quan=5)