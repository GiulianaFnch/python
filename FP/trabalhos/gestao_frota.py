import datetime
from collections import defaultdict # ajuda na contagem e agregação

# estrutura de dados
# dicionario principal para armazenar a frota de veículos elétricos
# chave : matrícula (string)
# valor :  dicionario com os detalhes do carro e historico
FROTA = {}

# dicionario para historico de alugueres (simplicidade)
# chave : ID do aluguer (poderia ser uma tupla (matricula, hora_inicio))
# valor : dicionario com os detalhes do aluguer
ALUGUERES = {}

# para simular uma matricula inicial para testes
FROTA['AA-00-BB'] = {
    'modelo': 'Tesla Model 3',
    'capacidade_bateria': 75,
    'autonomia_maxima': 500,
    'estado': 'disponivel',
    'bateria': 95,
    'localizacao': 'Porto',
    'historico_alugueres': [],
    'aluguer_atual': None    
}

# funções de gestão da frota

def adicionar_carro(mat, mod, cap, aut):
    """ Adiciona um novo carro à frota"""
    if mat in FROTA:
        print(f"Erro: Carro com matricula {mat} já existe")
        return

    try:
        FROTA[mat] = {
            'modelo': mod,
            'capacidade_bateria': float(cap),
            'autonomia_maxima': float(aut),
            'estado': 'disponivel',
            'bateria': 100,
            'localizacao': 'Sede',
            'historico_alugueres': [],
            'aluguer_atual': None # chave para o id do aluguer em curso
        }
        print(f"Carro {mat} adicionado com sucesso")
    except ValueError:
        print(f"Erro: Capacidade e autonomia devem ser números")

def remover_carro(mat):
    """ Remove um carro da frota se não estiver alugado"""
    if mat not in FROTA:
        print(f"Erro: Carro com matricula {mat} não existe")
        return
    if FROTA[mat]['estado'] == 'alugado':
        print(f"Erro: Carro com matricula {mat} está alugado e não pode ser removido")
        return
    del FROTA[mat]
    print(f"Carro {mat} removido com sucesso")

def listar_carros():
    """ Lista todos os carros da frota com seu estado atual"""
    if not FROTA:
        print("A frota está vazia")
        return
    
    print("----Frota EcoRide -----")
    for mat, carro in FROTA.items():
        alugado_info = f" (Aluguer: {dados['aluguer_atual']})" if dados['aluguer_atual'] else ""
        print(f"***{mat}***: ({dados['modelo']}): Estado: **{dados['estado']}** Bateria: {dados['bateria']}%) | Localização: {dados['localizacao']}{alugado_info}")
        
    print("-------------------------")

def abrir_tarefa_aluguer(mat, hora_inicio):
    """ Regista o início de um aluguer"""
    if mat not in FROTA:
        print(f"Erro: Carro com matricula {mat} não existe")
        return
    
    carro = FROTA[mat]

    if carro['estado'] != 'disponivel':
        print(f"Erro: Carro com matricula {mat} não está disponível")
        return
    
    try: 
        # cria um id de aluguer único (usamoa a matricula e a hora de inicio)
        id_aluguer = f"{mat}_{hora_inicio.strftime('%Y%m%d%H%M%S')}

        ALUGUERES[id_aluguer] = {
            'matricula': mat,
            'hora_inicio': hora_inicio,
            'hora_fim': None,
            'local_inicio' : carro['localizacao'],
            'local_fim': None,
            'concluido': False
        }
        
        # atualiza o estado do carro
        carro['estado'] = 'alugado'
        carro['aluguer_atual'] = id_aluguer
        carro['historico_alugueres'].append(id_aluguer)

        print (f"Aluguer {id_aluguer} iniciado para o carro {mat} às {hora_inicio.strftime('%H:%M')}")

    except Exception as e:
        print(f"Erro ao abrir aluguer: {str(e)}")


def fechar_tarefa_aluguer(mat, hora_fim, local_fim):
    """ Regista o fim de um aluguer"""
    if mat not in FROTA:
        print(f"Erro: Carro com matricula {mat} não existe")
        return
    
    carro = FROTA[mat]
    id_aluguer = carro['aluguer_atual']

    if not id_aluger or id_aluguer not in ALUGUERES:
        print(f"Erro: Carro com matricula {mat} não tem um aluguer em curso registado")
        return
    
    aluguer = ALUGUERES[id_aluguer]
    
    # verifica se a hora de fim é posterior à hora de inicio
    if hora_fim <= aluguer['hora_inicio']:
        print(f"Erro: Hora de fim {hora_fim.strftime('%H:%M')} deve ser posterior à hora de inicio {aluguer['hora_inicio'].strftime('%H:%M')}")
        return

    # atualiza o aluguer
    aluguer['hora_fim'] = hora_fim
    aluguer['local_fim'] = local_fim
    aluguer['concluido'] = True

    # atualiza o estado do carro
    carro['estado'] = 'disponivel'
    carro['aluguer_atual'] = None
    carro['localizacao'] = local_fim

    print(f"Aluguer {id_aluguer} concluído para o carro {mat} às {hora_fim.strftime('%H:%M')} em {local_fim}.")

def monitorar_e_atualizar(mat, novo_estado, nova_bateria, nova_localizacao):
    """ Monitora e atualiza o estado do carro específico"""
    if mat not in FROTA:
        print(f"Erro: Carro com matricula {mat} não encontrado")
        return
    
    carro = FROTA[mat]
    
    # validação do estado
    estados_validos = ['disponivel', 'alugado', 'manutenção']
    if novo_estado not in estados_validos:
        print(f"Erro: Estado {novo_estado} inválido. Use um de: {', '.join(estados_validos)}")
        return

    # validação da bateria
    try:
        bateria_pct = int(nova_bateria)
        if bateria_pct < 0 or bateria_pct > 100:
            raise ValueError
    except ValueError:
        print(f"Erro: Bateria deve ser um número entre 0 e 100")
        return
    
    # atualiza os dados
    carro['estado'] = novo_estado
    carro['bateria'] = bateria_pct
    carro['localizacao'] = nova_localizacao
    
    print(f"Carro {mat} atualizado para estado {novo_estado}, bateria {bateria_pct}% e localização {nova_localizacao}")


    # se o estado for alterado para disponivel e o carro estava alugada, sugere que o aluguer terminou

    if novo_estado == 'disponivel' and carro['aluguer_atual']:
        print(f"\nAtenção: Carro definido como disponível, mas tinha um aluguer {carro['aluguer_atual']} em curso. Verifique a situação do carro {mat}!")


# 4 funções de análise e mapas

def gerar_mapa_horas_aluguer():
    """ Gera um mapa com as horas de aluguer"""
    horas_por_carro = defaultdict(float)

    for id_aluguer, dados in ALUGUERES.items():
        if dados['concluido']:
            duracao = (dados['hora_fim'] - dados['hora_inicio'])
            duracao_horas = duracao.total_seconds() / 3600
            horas_por_carro[dados['matricula']] += duracao_horas

    print("\nMapa de horas de aluguer por carro:")
    for mat, horas in sorted(horas_por_carro.items(), key=lambda x: x[1], reverse=True):
        print(f"{mat}: {horas:.2f} horas")
    
    print("-------------------------")

def gerar_mapas_areas_frequentes():
    """ Contagem de quantas vezes cada area é registrada como localização final"""
    if not ALUGUERES:
        print("Nenhum aluguer registrado")
        return
    
    contagem_areas = defaultdict(int)
    for dados in ALUGUERES.values():
        if dados['local_fim']:
            contagem_areas[dados['local_fim']] += 1
    
    print("\nMapa de areas mais frequentes de viagens (local de devolução):")
    for area, count in sorted(contagem_areas.items(), key=lambda x: x[1], reverse=True):
        print(f"***{area}***: {count} devoluções")
    
    #adicionalmente podemos ver as localizações atuais dos carros
    print("\nMapa de localizações atuais dos carros:")
    

    print("-------------------------")

        
    

            