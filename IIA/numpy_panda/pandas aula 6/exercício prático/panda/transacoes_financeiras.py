import numpy as np
import pandas as pd

data = {
'Data': pd.date_range(start='2024-01-01', periods=20, freq='D'),
'Tipo': np.random.choice(['Crédito', 'Débito'], size=20),
'Valor': np.random.randint(100, 1000, size=20)
}
df_fin = pd.DataFrame(data)
print(df_fin)


# 1. Calcule o total de créditos e débitos por semana (utilize resample).
tipo_semana = df_fin.set_index('Data').groupby('Tipo').resample('W')['Valor'].sum().unstack()
print(f"\n ---------- Tabela total de cada tipo de créditos por semanas: ---------- \n",tipo_semana)

# 2. Adicione uma coluna com o saldo acumulado ao longo do tempo.

df_fin_movimentacao = df_fin

# vou criar uma nova coluna "movimentação" em que débito será negativo
df_fin_movimentacao['Movimentação'] = df_fin_movimentacao['Valor']
df_fin_movimentacao.loc[df_fin_movimentacao['Tipo'] == 'Débito', 'Movimentação'] *= -1

df_fin_movimentacao['Saldo Acumulado'] = df_fin_movimentacao['Movimentação'].cumsum()
print(f"\n ---------- Tabela com movimentações e saldo acumulado: ---------- \n",df_fin_movimentacao)


# 3. Use groupby para obter a média, o mínimo e o máximo do valor por tipo de
# transação.

estatistica = df_fin.groupby('Tipo')['Valor'].agg(['mean', 'min', 'max'])

print(f"\n ---------- Estatística: ---------- \n",estatistica)


# 4. Filtre e apresente as transações com valor superior à média geral.

media = df_fin['Valor'].mean()

valor_superior = df_fin.loc[df_fin['Valor']>media, 'Valor']
print(df_fin)