a = 0 
b = 0
c = "+-*/"

print("Digite o primeiro numero: ")
a = int(input())    
print("Digite o segundo numero: ")
b = int(input())    
print("Digite a operacao: ")
c = str(input())
if c == "+":
    print("O resultado e: " + str(a + b))
elif c == "-":
    print("O resultado e: " + str(a - b))
elif c == "*":
    print("O resultado e: " + str(a * b))
elif c == "/":
    print("O resultado e: " + str(a / b))
else:
    print("Operacao invalida")  