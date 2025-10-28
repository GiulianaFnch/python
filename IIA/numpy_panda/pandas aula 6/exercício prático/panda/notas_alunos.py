import numpy as np
import pandas as pd

data = {
 'Aluno': [f'Aluno_{i}' for i in range(1, 7)] * 2,
 'Disciplina': ['Matemática']*6 + ['História']*6,
 'Nota': np.random.randint(50, 100, size=12)
}
df_notas = pd.DataFrame(data)

print(df_notas)

# 1. Calcule a nota média por disciplina.

media_disciplina = df_notas.groupby("Disciplina")["Nota"].agg("mean")
print(f"\nNota média por disciplina:\n", media_disciplina)

# 2. Crie uma tabela pivot com os alunos como linhas, disciplinas como colunas e
# as notas como valores.

tabela_pivot = df_notas.pivot_table(values="Nota", index="Aluno", columns="Disciplina")

print(f"\nTabela pivot:\n", tabela_pivot)

# 3. Crie uma coluna que represente a diferença da nota de cada aluno em relação
# à média da disciplina.

df_notas["Desvio"] = df_notas["Nota"] - df_notas["Disciplina"].map(media_disciplina)

print(f"\nTabela atualizada com o desvio de cada nota:\n", df_notas)

# 4. Classifique os alunos com base na média das suas notas nas diferentes
# disciplinas.

media_por_aluno = df_notas.groupby('Aluno')['Nota'].mean().sort_values(ascending=False)
print(f"\nMédia aluno:\n", media_por_aluno)

classificacao = media_por_aluno.reset_index().rename(columns={'Nota': 'Media_aluno'})
classificacao['Rank'] = classificacao['Media_aluno'].rank(method='dense', ascending=False).astype(int)

print(f"\nClassificação por média:\n", classificacao)

