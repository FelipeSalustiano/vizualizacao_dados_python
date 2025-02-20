import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd 

df = pd.read_csv('clientes-v3-preparado.csv')
print(df.head().to_string())

# Histograma 
plt.hist(df['salario'])
plt.show()

# Histograma - Parâmetros
plt.figure(figsize=(10,6))
plt.hist(df['salario'], bins=100, color='green', alpha=0.8)
plt.title('Histograma - Distribuição de Salários')
plt.xlabel('Salário')
plt.xticks(ticks=range(0, int(df['salario'].max())+2000, 2000))
plt.ylabel('Frequência')
plt.grid(True)
plt.show()

# Mútlplos gráficos 
plt.figure(figsize=(10, 6))
plt.subplot(2, 2, 1) 
# Gráfico de disperção
plt.scatter(df['salario'], df['salario'])
plt.title('Dispersão - Salário e Salário')
plt.xlabel('Salário')
plt.ylabel('Salário')

plt.subplot(1, 2, 2)
plt.scatter(df['salario'], df['anos_experiencia'], color='skyblue', alpha=0.6, s=30)
plt.title('Dispersão - Salário e Anos de Experiência')
plt.xlabel('Salário')
plt.ylabel('Anos de Experiência')

# Mapa de calor 
corr = df[['salario', 'anos_experiencia']].corr()
plt.subplot(2, 2, 3)
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correlação - Salário e Anos de Experiência')
plt.tight_layout()
plt.show()
