
import sys

print('Digite um numero: ')
entrada = int(sys.stdin.readline())
n=[]
n.append(entrada)
for i in range(1,10):
    n.append(n[i-1]*2)
for a in range(10):
    print(f'N[{a}] = {n[a]}')


'''
x = int(input())
for i in range (1,x+1):
  x = []
  if i <= 49:
    square = i*i
    print("%i^2 = %i" %(i, square))
'''