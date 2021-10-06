x=[[1,2,3,4,5],
  [1,2,3,4,5],
  [1,2,3,4,5],
  [1,2,3,4,5],
  [1,2,3,4,5]]
for i in range(len(x)):
    print('Suma elem liniei',i,'=',sum(x[i]))
for i in range(len(x)):
    sumaC=0
    for j in range(len(x[0])):
         sumaC+=x[j][i]
    print('Suma elem coloanei',i,'=',sumaC)

diagonala_p=[]
diagonala_s=[]

for i in range(len(x)):
    for j in range(len(x[0])):
        if i==j:
            diagonala_p.append(x[i][j])
        if(i+j)==(len(x)-1):
            diagonala_s.append(x[i][j])
print('diagonala principala=',diagonala_p)
print('diagonala secundara=',diagonala_s)