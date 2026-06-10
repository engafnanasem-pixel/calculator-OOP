class calc:
   def __init__(self , name="my calc"):
      self.name =name
      self.history = []
      self.count = 0
      
      
   def add (self, a ,b):
      result = a+b
      self._save(f"{a} + {b} = {result}")
      return result
      
      
   def sub (self, a ,b):
      result = a-b
      self._save(f"{a} - {b} = {result}")
      return result
      
   def mult (self, a ,b):
      result = a*b
      self._save(f"{a} * {b} = {result}")
      return result
      
      
   def div (self, a ,b):
      if b == 0 :
         print ("Cannot divide on zero")
         return None
      result = a/b
      self._save(f"{a} / {b} = {result}")
      return result
      
      
   def _save (self , text):
      self.history.append(text)
      self.count +=1
      
      
   def show_history (self):
      if not self.history :
         print ("NO HISTORY❌️")
         return
      for i , item in enumerate(self.history, 1 ):
         print (f"{i}.{item}")
         
         
   def clear_history(self,clos):
      
         if clos == "y":
            self.history.clear()
            print("History DELETED 💯️")
         else :
            print("It's OKAY🙃️")
      
      
   def stats(self):
      print (f"The CALCUlater :{self.name}")
      print(f"No.OPERATIONS:{self.count}")
      
      
      
      
      
      
calculater = calc ("Fonna")
print(calculater.add(10,5))
print(calculater.sub(20,8))
print(calculater.mult(3,4))
print(calculater.div(15,3))
print(calculater.div(5,0))
calculater.show_history()
calculater.stats()








def main():
   cal = calc("Fona")
   
   while True:
      print("\n Choose the number of operation you want :") 
      print("1. +")
      print("2. -")
      print("3. *")
      print("4. /")
      print("5. History")
      print("6. status")
      print("7. clear history")
      print("8. Exit")
      choice = input ("Your Choice:")
      if choice == "8":
         clos = input ("Are you sure ? y or n")
         if clos == "y":
            print ("BYE BYE")
            break
         
         
         
      elif choice in ["1","2","3","4"]:
         a= float (input ("THe 1st number :"))
         b= float (input ("The 2nd number :"))
         if choice == "1": print (cal.add(a,b))
         elif choice == "2": print (cal.sub(a,b))
         elif choice == "3": print (cal.mult(a,b))
         elif choice == "4": print (cal.div(a,b))
      elif choice == "5": cal.show_history()
      elif choice == "6": cal.stats()
      elif choice == "7": 
         clos = input ("Are you sure ? y or n")
         cal.clear_history(clos)
   
   
   
main()   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
