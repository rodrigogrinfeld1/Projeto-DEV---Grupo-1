import pandas as pd

df = pd.read_csv("dataset_unificado.csv")
df.head()
df = df.rename(columns={
    'Data': 'Data',
    '433 - Índice nacional de preços ao consumidor-amplo (IPCA) - Var. % mensal': 'IPCA (%)',
    '29037 - Endividamento das famílias com o Sistema Financeiro Nacional em relação à renda acumulada dos últimos doze meses (RNDBF) - %,': 'Endividamento (%)'
})
df['Data'] = pd.to_datetime(df['Data'], format="%m/%Y")
df['IPCA (%)'] = df['IPCA (%)'].str.replace(',', '.').astype(float)
df['Endividamento (%)'] = df['Endividamento (%)'].str.replace(',', '.').astype(float)
df[['Data', 'IPCA (%)', 'Endividamento (%)']].head()

import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid", palette="muted")
plt.rcParams["figure.figsize"] = (14, 6)

# 1. Gráfico de séries temporais
plt.figure()
plt.plot(df['Data'], df['IPCA (%)'], label='Inflação (IPCA)', color='red')
plt.plot(df['Data'], df['Endividamento (%)'], label='Endividamento das Famílias', color='blue')
plt.title("Inflação e Endividamento das Famílias ao Longo do Tempo")
plt.xlabel("Ano")
plt.ylabel("Percentual (%)")
plt.legend()
plt.tight_layout()
plt.show()

# 2. Gráfico de dispersão entre IPCA e Endividamento
plt.figure()
sns.scatterplot(data=df, x='IPCA (%)', y='Endividamento (%)')
plt.title("Relação entre Inflação (IPCA) e Endividamento das Famílias")
plt.xlabel("Inflação (IPCA) - % ao mês")
plt.ylabel("Endividamento das Famílias - %")
plt.tight_layout()
plt.show()

# 3. Correlação de Pearson
correlation = df['IPCA (%)'].corr(df['Endividamento (%)'])
correlation

"""
-Gráfico Temporal:

O gráfico mostra que tanto a inflação (IPCA) quanto o endividamento das famílias variam ao longo do tempo, mas não de forma obviamente sincronizada.

-Gráfico de Dispersão:

Os pontos mostram uma fraca tendência positiva, mas com muita dispersão — ou seja, não há uma relação clara e linear.

-Correlação de Pearson:

O coeficiente é ≈ 0,10, o que indica uma correlação positiva fraca entre inflação e endividamento.

Isso sugere que a inflação tem pouca influência direta sobre o nível de endividamento das famílias, ao menos de forma linear e direta.
"""
