Q=[[6,7,8,10],[4,5,6,13],[10,6,5,11],[8,9,7,9],[1,2,1,2],[2,1,2,4],[3,3,2,2],[4,1,3,3]]
min =[0]*8
w=[0]*5
z=0
print('Матрица Q (исходная) ')
for i in range(8):
    for j in range(4):
        print(Q[i][j], end=' ')
    print()
print ('======================================================')
print('1. Критерий Вальда')
print('Минимальный элемент по строке в матрице Q')
for i in range(8):
     min[i] = Q[i][0]
     for j in range(4):
         if (Q[i][j]< min[i]) :
             min[i] = Q[i][j]
             j=j+1
     print('a{}'.format(i+1),' = ',min[i])
     i=i+1
max=min[0]
for i in range (8):
    if max< min[i]:
        max=min[i]
        k1=i+1
    i=i+1
print ('Максимальный элемент по столбцу = a{}'.format(k1),' = ',max)
print('Оптимальное решение по критерию Вальда - X{}'.format(k1))
w[z]=k1
z=z+1
print ('======================================================')
print('2. Критерий Сэвиджа')
print('Матрица R(рисков)') 
ax=[[0]*4]*8
b=[0]*4 
b=[10,9,8,13]
i=0
j=0
max1 =[0]*8
for i in range(8):
    max1[i]=0
    for j in range(4):
        ax[i][j]=b[j]-Q[i][j] 
        print(ax[i][j], end=' ')
        if (max1[i]<ax[i][j]):
            max1[i]=ax[i][j]
    print()
print('Максимальный элемент по строке')    
for ii in range (8):
    print('b{}'.format(ii+1),' = ',max1[ii])
min1=max1[0]
for i in range (8):
    if min1> max1[i]:
        min1=max1[i]
        k2=i+1
    i=i+1
print ('Минимальный элемент по столбцу = b{}'.format(k2),' = ',min1)
print('Оптимальное решение по критерию Сэвиджа - X{}'.format(k2))
w[z]=k2
z=z+1
print ('======================================================')
print('3. Критерий Гурвица')
y=0.6
max2 =[0]*8
min2 =[0]*8
g =([0]*8)
for i in range(8):
    max2[i]=Q[i][0]
    min2[i]=Q[i][0]
    for j in range(4):
        if (max2[i]<Q[i][j]):
            max2[i]=Q[i][j]
        if(min2[i]>Q[i][j]):
            min2[i]=Q[i][j]
    g[i]=y*min2[i]+(1-y)*max2[i]
print('Максимальный элемент по строке')    
for i in range (8):
    print('g{}'.format(i+1),' = ',round(g[i],1))
max3=g[0]
for i in range (8):
    if max3< g[i]:
        max3=g[i]
        k3=i+1
    i=i+1
print ('Максимальный эленмент = g{}'.format(k3),' = ',max3)
print('Оптимальное решение по критерию Гурвица - X{}'.format(k3))
w[z]=k3
z=z+1
print ('==========================================================')
print('4. Критерий Байеса')
p=[0.1,0.4,0.4,0.1]
d =([0]*8)
for i in range(8):
    for j in range(4):
        d[i]=d[i]+Q[i][j]*p[j]
    print(round(d[i],1))
max4=d[0]
for i in range (8):
    if max4< d[i]:
        max4=d[i]
        k4=i+1
    i=i+1
print ('Максимальный эленмент g{}'.format(k4),' = ',round(max4,1))
print('Оптимальное решение по критерию Байеса - X{}'.format(k4))
w[z]=k4
z=z+1
print ('=========================================================')
print('5. Критерий Лапласа')
n=4
f =([0]*8)
for i in range(8):
    for j in range(4):
        f[i]=f[i]+Q[i][j]*(1/n)
    print(round(f[i],2))
max5=f[0]
for i in range (8):
    if max5< f[i]:
        max5=f[i]
        k5=i+1
    i=i+1
print ('Максимальный эленмент f{}'.format(k5),' = ',round(max5,2))
print('Оптимальное решение по критерию Лапласа - X{}'.format(k5))
w[z]=k5
print ('=========================================================')
print('Матрица голосования')
print(' ')
t=[[0]*5]*8
x=[0]*8
print('Bальд','Сэвидж','Гульвиц','Байэес','Лаплас','sum',' ', 'X')
print(' ')
for i in range(8):
    for j in range (5):
        if (i==w[j]-1):
            print ('+', end='      ')
            x[i]=x[i]+1
        else:
            print ('-', end='      ')
    print(x[i],'   ', 'X{}'.format(i+1))
    print()
max6=x[0]
for i in range (8):
    if max6<x[i]:
        max6=x[i]
        kg=i+1
print ('Оптимальное решение - Х{}'.format(kg))