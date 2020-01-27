import pandas as pd 
import matplotlib.pyplot as plt

pd.read_csv ("manchas.csv")

manchas = pd.read_csv ("manchas.csv")
manchas
x = manchas["Ano"]
y = manchas["manchas"]
plt.plot(x,y)
plt.show()

######################################## 

dados = pd.read_csv('manchas.csv')

dados1 = manchas[0:10]
plt.plot(dados1.Ano, dados1.manchas)
plt.show()
########################################

dados2 = manchas[166:]
plt.plot(dados2.Ano, dados2.manchas)
plt.show()
########################################

plt.boxplot(manchas.manchas)
plt.show()

########################################

manchas = pd.read_csv ("manchas.csv")
manchas = manchas[0:29]

plt.plot(manchas.Ano, manchas.manchas)
plt.xlabel('Ano (s)')
plt.ylabel('Manchas')
plt.title('Número de manchas solares de Wolfer')
plt.grid(True)
plt.xticks(manchas.Ano, manchas.Ano, rotation = 'vertical')
plt.show()
