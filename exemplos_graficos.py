import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('clientes-v3-preparado.csv')
print(df.head())

df_corr = df[['salario', 'idade', 'anos_experiencia', 'numero_filhos', 'nivel_educacao_cod', 'area_atuacao_cod', 'estado_cod']].corr()

# Heatmap de correlação 
plt.figure(figsize=(10, 6))
sns.heatmap(df_corr, annot=True, fmt='.2f')
plt.title('Mapa de Calor da Correlação entre Variáveis')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Countplot
sns.countplot(x='estado_civil', data=df)
plt.title('Distribuição de Estado Civil')
plt.xlabel('Estado Civil')
plt.ylabel('Contagem')
plt.show()

