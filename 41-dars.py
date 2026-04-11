# class Talaba:
#     def __init__(self,ism,familiya,yosh,otasining_ismi,manzil):
#         self.ism = ism
#         self.familiya = familiya
#         self.yosh = yosh
#         self.otasining_ismi = otasining_ismi
#         self.manzil = manzil
#     def FIO(self):
#         return f"{self.ism} {self.familiya}{self.otasining_ismi}"    


# talaba1=Talaba("matluba","ollayorova","16","Bektemir_qizi","xorazm")
# print(talaba1.FIO())
# print(talaba1.manzil)
# print(talaba1.yosh)
# print(talaba1.otasining_ismi)



class kitoblar:
    def __init__(self,sahifa,narxi,yili,nomi,muallifi,):
        self.sahifa=sahifa
        self.narxi=narxi
        self.yili=yili
        self.nomi=nomi
        self.muallifi=muallifi
    def noma(self):
        return f"{self.sahifa} {self.narxi} {self.yili} {self.nomi} {self.muallifi}"
    
kitob1= kitoblar("127","50","2024","choliqushi","Rashod Nuri Gultekin")
kitob2= kitoblar("234","56","2009","nur borki soya bor","o'tkir xoshimov")

print(kitob1.nomi)
print(kitob2.yili)
print(kitob1.sahifa)
print(kitob2.muallifi)
    