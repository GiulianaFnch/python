# quota do condominio

orcamento = float(input("Escreva o valor do orçamento anual (€): "))
permilagem = float(input("Escreva o valor da permilagem da fração (por mil): "))

def quota_mensal(orcamento_anual, permilagem_fracao):
    quota_condominio = (orcamento_anual*permilagem_fracao) / 1000
    return quota_condominio


quota = quota_mensal(orcamento, permilagem)

print(f"O valor da quota do condomínio é igual a {quota:.2f}€ anuais e {quota/12:.2f}€ mensais.")
