import pandas as pd
import numpy as np

data = {
 'Funcionario': [f'Funcionario_{i}' for i in range(1, 11)],
 'Departamento': ['RH', 'TI', 'Vendas', 'TI', 'RH', 'Vendas', 'Financeiro', 'TI', 'Financeiro',
'Vendas'],
 'Salario': np.random.randint(2000, 7000, size=10),
 'Experiencia_anos': np.random.randint(1, 11, size=10)
}
df_func = pd.DataFrame(data)
print(df_func)

# 1. Agrupe os dados por departamento e calcule o salário médio.

departamento_salario = df_func.groupby("Departamento")["Salario"].agg("mean")
print(f"\nSalário médio por departamento:\n", departamento_salario)

# 2. Adicione uma coluna chamada salário ajustado, que adiciona 10% ao salário para funcionários com mais de 5 anos de experiência

condicao = df_func["Experiencia_anos"]>5
func_antigos = df_func[condicao]

# where: se Experiencia_anos > 5 aplica 10%, senão mantém o salário
df_func["Salario_ajustado"] = np.where(condicao, df_func["Salario"] * 1.10, df_func["Salario"])
print(f"\nTabela ajustada com nova coluna:\n", df_func)

# 3. Crie uma tabela com o total e a média salarial por departamento.

total_media = df_func.groupby("Departamento")["Salario"].agg(["sum", "mean"]).round(2)
print(f"\nTotal e média por departamento:\n", total_media)

# 4. Use transform para adicionar uma coluna com o salário médio do departamento de cada funcionário.

df_func["Salario_medio_departamento"] = df_func.groupby("Departamento")["Salario"].transform("mean")

print(f"\nDataFrame com salário médio do departamento por funcionário:\n", df_func)