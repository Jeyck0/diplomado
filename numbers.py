import time
inicio = time.time()

input = 0


for i in range(100000):
    input = input+1
    print(input)

fin = time.time()
print("tiempo de ejecución")
print(fin-inicio) 