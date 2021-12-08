class Phone:
   # "A simple class for test"
    phone_version = "iphone13"
    brand_name = "apple"
    user_name = ""



    def __init__(self,user_name):
       self.user_name = user_name


    def bootLogo(self):
        print("Apple",self)

hrishi = Phone("Hrishikesh's Phone")
hrishi.bootLogo()