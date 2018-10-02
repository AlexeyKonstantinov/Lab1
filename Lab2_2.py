#Лабораторная 2, задание 2, восстановление данных
import numpy as np
import random as rand

#Создаем массив 10х10 заполненный случайными величинами от 1 до 30 включительно
X = np.random.randint(1, 31, (10,10))

#10 случайных ячеек заполняем нулями
stroki = np.arange(10);
stolbci = np.arange(10);
np.random.shuffle(stroki)
np.random.shuffle(stolbci)
for i in range(10):
    X[stroki[i]][stolbci[i]] = 0

miss = []
for i in range(10):
    miss.append( [stroki[i], stolbci[i]] )

X_Vin = np.copy(X)
for i in range(X.shape[0]):
    for j in range (X.shape[1]):
        if [i,j] in miss:
            if [i,j-1] not in miss and (j-1) >= 0:
                X_Vin [i,j] = X[i, j-1]
            elif [i,j+1] not in miss and (j+1) <= 9:
                X_Vin [i,j] = X[i, j+1]
            else:
                X_Vin [i,j] = -999
        else:
            X_Vin[i,j] = X[i,j]

X_lin = np.copy(X)
for i in range(X.shape[0]):
    for j in range (X.shape[1]):
        if [i,j] in miss:
            if j == 0:
                X_lin[i,j] = X[i, j+1]
            elif j == 9:
                X_lin[i,j] = X[i, j-1]
            else:
                X_lin[i,j] = (X[i, j-1] + X[i, j+1])/2
        else:
            X_lin[i,j] = X[i,j]

X_cor = np.copy(X)
for i in range(X.shape[0]):
    for j in range(X.shape[1]):
        if [i, j] in miss:
            if i < 9:
                if j > 0:
                    if (X[i+1,j-1] != 0):
                        X_cor[i,j] = (X[i+1,j]/X[i+1,j-1])*X[i,j-1]
                    else:
                        X_cor[i,j] = (X[i+1,j]/15)*X[i,j-1]                        
                elif j == 0:
                    if (X[i+1,j]):
                        X_cor[i,j] = (X[i+1,j+1]/X[i+1,j])*X[i,j+1]
                    else:
                        X_cor[i,j] = (X[i+1,j+1]/15)*X[i,j+1]
            elif i == 9:
                if j > 0:
                    if (X[i-1,j-1] != 0):
                        X_cor[i,j] = (X[i-1,j]/X[i-1,j-1])*X[i,j-1]
                    else:
                        X_cor[i,j] = (X[i-1,j]/15)*X[i,j-1]                        
                elif j == 0:
                    if (X[i-1,j] != 0):
                        X_cor[i,j] = (X[i-1,j+1]/X[i-1,j])*X[i,j+1]
                    else:
                        X_cor[i,j] = (X[i-1,j+1]/15)*X[i,j+1]                        
        else:
            X_cor[i,j] = X[i,j]
            

