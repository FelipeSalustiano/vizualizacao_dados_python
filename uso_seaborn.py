import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt 

df = pd.read_csv('clientes-v3-preparado.csv')
print(df.dtypes)

# Gráfico de dispersão 
sns.jointplot(x='idade', y='salario', data=df, kind='scatter')
plt.show()

# Gráfico de densidade 
plt.figure(figsize=(10, 6))
sns.kdeplot(df['salario'], fill=True, color='pink')
plt.title('Densidade de Salários')
plt.xlabel('Salário')
plt.ylabel('Densidade')
plt.show()

# Gráfico de Pairplot - Dispersão e Histograma
sns.pairplot(df[['idade', 'salario', 'anos_experiencia', 'nivel_educacao']])
plt.show()

# Gráfico de regressão
sns.regplot(y='idade', x='salario', data=df, color='red', scatter_kws={'alpha': 0.5, 'color':'yellow'})
plt.title('Regresão de Salário por Idade')
plt.xlabel('Idade')
plt.ylabel('Salario')
plt.show()

# Gráfico countplot com hue
sns.countplot(x='estado_civil', hue='nivel_educacao', data=df, palette='pastel')
plt.xlabel('Estado Civil')
plt.ylabel('Quantidade de Clientes')
plt.legend(title='Nível de Educação')
plt.show()
