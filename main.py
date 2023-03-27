def maior (num1,num2) :
  
  if num1 > num2 :
    print ("O maior número é:",num1)
  else :
    print("O maior número é:",num2)
    
maior (8,9)
maior (5,7)
maior(4,6)
print("//-------MÚLTIPLO-------\\")
def mult (num1,num2) :
  if num1 % num2 == 0 :
    print("O número",num1,"é multiplo de",num2)
  else :
    print("O número",num1,"não é multiplo de",num2)

mult(8,4)
mult(10,5)
mult(9,3)
print("//-------ÁREA-------\\")

def area (num1) :
  print ("A área do quadrado é ",num1 ** 2)

area (5)