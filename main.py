def main():
    total_jogadores={'10000000101': {'nome':'Carlos Silva','genero':'M','senha':'123','posicao':'Goleiro','status_da_peneira':False},
    '10000000102': {'nome':'João Souza','genero':'M','senha':'123','posicao':'Goleiro','status_da_peneira':False},'20000000101': {'nome':'Ana Lima','genero':'F','senha':'123','posicao':'Goleiro','status_da_peneira':False},
    '20000000102': {'nome':'Mariana Rocha','genero':'F','senha':'123','posicao':'Goleiro','status_da_peneira':False},'10000000201': {'nome':'Pedro Costa','genero':'M','senha':'123','posicao':'Zagueiro','status_da_peneira':False},
    '10000000202': {'nome':'Lucas Santos','genero':'M','senha':'123','posicao':'Zagueiro','status_da_peneira':False},'20000000201': {'nome':'Beatriz Alves','genero':'F','senha':'123','posicao':'Zagueiro','status_da_peneira':False},
    '20000000202': {'nome':'Fernanda Dias','genero':'F','senha':'123','posicao':'Zagueiro','status_da_peneira':False},'10000000301': {'nome':'Rafael Melo','genero':'M','senha':'123','posicao':'Lateral','status_da_peneira':False},'10000000302': {'nome':'Bruno Nunes','genero':'M','senha':'123','posicao':'Lateral','status_da_peneira':False},
    '20000000301': {'nome':'Juliana Reis','genero':'F','senha':'123','posicao':'Lateral','status_da_peneira':False},'20000000302': {'nome':'Patricia Gomes','genero':'F','senha':'123','posicao':'Lateral','status_da_peneira':False},
    '10000000401': {'nome': 'Diego Martins', 'genero': 'M', 'senha': '123', 'posicao': 'Ala','status_da_peneira': False},'10000000402': {'nome': 'Felipe Castro', 'genero': 'M', 'senha': '123', 'posicao': 'Ala','status_da_peneira': False},
    '20000000401': {'nome': 'Larissa Freitas', 'genero': 'F', 'senha': '123', 'posicao': 'Ala','status_da_peneira': False},'20000000402': {'nome': 'Camila Ribeiro', 'genero': 'F', 'senha': '123', 'posicao': 'Ala','status_da_peneira': False},
    '10000000501': {'nome': 'Gustavo Oliveira', 'genero': 'M', 'senha': '123', 'posicao': 'Volante','status_da_peneira': False},'10000000502': {'nome': 'Thiago Araujo', 'genero': 'M', 'senha': '123', 'posicao': 'Volante','status_da_peneira': False},
    '20000000501': {'nome': 'Amanda Pinto', 'genero': 'F', 'senha': '123', 'posicao': 'Volante','status_da_peneira': False},'20000000502': {'nome': 'Bianca Teixeira', 'genero': 'F', 'senha': '123', 'posicao': 'Volante','status_da_peneira': False},
    '10000000601': {'nome': 'Leonardo Vieira', 'genero': 'M', 'senha': '123', 'posicao': 'Meio campo','status_da_peneira': False},'10000000602': {'nome': 'Matheus Barbosa', 'genero': 'M', 'senha': '123', 'posicao': 'Meio campo','status_da_peneira': False},
    '20000000601': {'nome': 'Gabriela Cardoso', 'genero': 'F', 'senha': '123', 'posicao': 'Meio campo','status_da_peneira': False},'20000000602': {'nome': 'Renata Moura', 'genero': 'F', 'senha': '123', 'posicao': 'Meio campo','status_da_peneira': False},
    '10000000701': {'nome': 'André Lopes', 'genero': 'M', 'senha': '123', 'posicao': 'Meia atacante','status_da_peneira': False},'10000000702': {'nome': 'Vinicius Correia', 'genero': 'M', 'senha': '123','posicao': 'Meia atacante', 'status_da_peneira': False},
    '20000000701': {'nome': 'Isabela Ferreira', 'genero': 'F', 'senha': '123','posicao': 'Meia atacante', 'status_da_peneira': False},'20000000702': {'nome': 'Natália Cunha', 'genero': 'F', 'senha': '123', 'posicao': 'Meia atacante','status_da_peneira': False},
    '10000000801': {'nome': 'Caio Mendes', 'genero': 'M', 'senha': '123', 'posicao': 'Ponta','status_da_peneira': False},'10000000802': {'nome': 'Igor Farias', 'genero': 'M', 'senha': '123', 'posicao': 'Ponta','status_da_peneira': False},
    '20000000801': {'nome': 'Carolina Duarte', 'genero': 'F', 'senha': '123', 'posicao': 'Ponta','status_da_peneira': False},'20000000802': {'nome': 'Aline Moreira', 'genero': 'F', 'senha': '123', 'posicao': 'Ponta','status_da_peneira': False}}
    arquivo_das_peneiras={}
    logins_dos_funcionarios={'Claudio':'12345', 'Ana':'Abacate',}

    while True:
        jogador_ou_funcionario=input('Você é um jogador ou um funcionário?\n'
                                      'Digite "1" para jogador ou "2" para funcionário ou 0 para sair')
        match jogador_ou_funcionario:
            case '1':
                jogador_inicio(total_jogadores,arquivo_das_peneiras)
            case '2':
                funcionario(logins_dos_funcionarios,arquivo_das_peneiras,total_jogadores)
            case '0':
                print('Volte sempre!')
                break
            case _:
                print('Por favor, digite "1", "2" ou "0"')

def jogador_inicio(lista_jogadores,arquivo_das_peneiras):
    while True:
        login_ou_criar_conta_jogador = input('Bem-vindo jogador!\n'
                                             'Para acessar as funcionalidades da plataforma\n'
                                             'É necessário fazer login ou criar uma conta\n'
                                             'Digite "1" para fazer login ou "2" para criar uma conta\n'
                                             'Ou 0 para voltar a escolha inicial')
        match login_ou_criar_conta_jogador:
            case '1':
                login_jogador(lista_jogadores,arquivo_das_peneiras)
            case '2':
                nova_conta,chave_cpf=criar_conta_jogador()
                if chave_cpf in lista_jogadores:
                    print('CPF já cadastrado, use ele para fazer o login')
                else:
                    lista_jogadores[chave_cpf]=nova_conta
                    print('Conta criada com sucesso!')
            case '0':
                break
            case _:
                print('Por favor, digite "1", "2" ou "0"')

def login_jogador(lista_jogadores,arquivo_das_peneiras):
    l_cpf=input('Digite o CPF: ')
    l_senha=input('Digite a senha: ')
    if verificar_login(lista_jogadores,l_cpf,l_senha):
        menu_jogador(lista_jogadores,l_cpf,arquivo_das_peneiras)
    else:
        print('CPF ou senha incorreta, tente novamente')
        return

def verificar_login(lista_jogadores,cpf,senha):
    return cpf in lista_jogadores and senha == lista_jogadores[cpf]['senha']

def criar_conta_jogador():
    nome = input('Digite o seu nome: ')
    cpf = input('Digite o seu CPF: ')
    genero = input('Digite o seu gênero biológico: ')
    senha= input('Crie uma senha para acessar a sua conta: ')
    conta={'nome':nome,'genero':genero,'senha':senha,'posicao':'sem posição definida','status_da_peneira': False}
    return conta,cpf

def menu_jogador(lista_jogadores,chave_cpf,arquivo_das_peneiras):
    print(f'Bem-vindo {lista_jogadores[chave_cpf]["nome"]}')
    while True:
        print('O que deseja fazer?\n'
              '1- Escolher posição\n'
              '2- Ver status e convite para peneira\n'
              '0- Sair')
        escolha_menu=input('Digite sua escolha[1, 2 ou 0]: ')
        match escolha_menu:
            case '1':
                if lista_jogadores[chave_cpf]['posicao'] == 'sem posição definida':
                    nova_posicao=escolher_posicao()
                    lista_jogadores[chave_cpf]['posicao']=nova_posicao
                    print(f"Posição de {lista_jogadores[chave_cpf]['posicao']} escolhida com sucesso")
                else:
                    confirmacao=input(f'Atualmente, posição marcada é: {lista_jogadores[chave_cpf]["posicao"]}. Para confirmar a mudança digite "s", se não digite qualquer coisa')
                    match confirmacao:
                        case 'S'|'s':
                            nova_posicao = escolher_posicao()
                            lista_jogadores[chave_cpf]['posicao'] = nova_posicao
                            print(f"Posição de {lista_jogadores[chave_cpf]['posicao']} escolhida com sucesso")
                        case _:
                            pass
            case '2':
                ver_status_jogador(lista_jogadores,chave_cpf,arquivo_das_peneiras)
            case '0':
                break
            case _:
                print('Por favor, digite "1", "2" ou "0"')

def ver_status_jogador(lista_jogadores,chave_cpf,arquivo_das_peneiras):
    print(f'Nome: {lista_jogadores[chave_cpf]["nome"]}\n'
          f'CPF: {chave_cpf}\n'
          f'Posição escolhida: {lista_jogadores[chave_cpf]["posicao"]}')
    if lista_jogadores[chave_cpf]['status_da_peneira']:
        peneira=lista_jogadores[chave_cpf]['status_da_peneira']
        print(f"Você foi escalado, parabéns!\n"
              f"A peneira vai acontecer em {arquivo_das_peneiras[lista_jogadores[chave_cpf]['status_da_peneira']]['local']}\n"
              f"No dia {arquivo_das_peneiras[peneira]['dia da peneira']} e o horário de termino e início são: {arquivo_das_peneiras[peneira]['horario inicio']} {arquivo_das_peneiras[peneira]['horario fim']}\n")
        for time in arquivo_das_peneiras[peneira]['times']:
            for posicao in arquivo_das_peneiras[peneira]['times'][time]:
                if arquivo_das_peneiras[peneira]['times'][time][posicao] == chave_cpf:
                    print(f'Seu time é: {time}')
    else:
        print('Você ainda não está escalado, fique atento a atualizações')

def escolher_posicao():
    while True:
        escolha_de_posicao=input('1-Goleiro\n'
                                 '2-Zagueiro\n'
                                 '3-Lateral\n'
                                 '4-Ala\n'
                                 '5-Volante\n'
                                 '6-Meio campo\n'
                                 '7-Meia atacante\n'
                                 '8-Ponta\n'
                                 '9-Centro avante\n'
                                 'Digite a sua escolha: ')
        match escolha_de_posicao:
            case '1':
                nova_posicao='Goleiro'
                return nova_posicao
            case '2':
                nova_posicao= 'Zagueiro'
                return nova_posicao
            case '3':
                nova_posicao = 'Lateral'
                return nova_posicao
            case '4':
                nova_posicao = 'Ala'
                return nova_posicao
            case '5':
                nova_posicao = 'Volante'
                return nova_posicao
            case '6':
                nova_posicao = 'Meio campo'
                return nova_posicao
            case '7':
                nova_posicao = 'Meia atacante'
                return nova_posicao
            case '8':
                nova_posicao = 'Ponta'
                return nova_posicao
            case '9':
                nova_posicao = 'Centro avante'
                return nova_posicao
            case _:
                print('Por favor, digite um número válido')

def funcionario(lista_de_funcionarios,arquivo_das_peneiras,total_jogadores):
    login_funcionario=input('Digite o seu login: ')
    senha_funcionario=input('Digite sua senha: ')
    if verificar_login_funcionario(login_funcionario,senha_funcionario,lista_de_funcionarios):
        menu_funcionario(login_funcionario,arquivo_das_peneiras,total_jogadores)
    else:
        tentar_novamente=input('Login ou senha incorreta, deseja tentar novamente?[S/N]')
        match tentar_novamente:
            case 'S'|'s':
                funcionario(lista_de_funcionarios,arquivo_das_peneiras,total_jogadores)
            case 'N'|'n':
                return

def menu_funcionario(login_funcionario,arquivo_das_peneiras,total_jogadores):
    print(f'Bem-vindo {login_funcionario}')
    while True:
        escolha_funcionario=input('O que deseja fazer?\n'
                                  '1- Agendar peneira\n'
                                  '2- Ver peneiras atuais\n'
                                  '0- Sair\n'
                                  'Digite sua escolha: ')
        match escolha_funcionario:
            case '1':
                chave_peneira,informacoes_peneira=agendar_peneira(arquivo_das_peneiras,total_jogadores)
                arquivo_das_peneiras[chave_peneira]=informacoes_peneira
                print('Peneira gerada com sucesso!')
            case '2':
                ver_peneira_funcionario(arquivo_das_peneiras,total_jogadores)
            case '0':
                break

def agendar_peneira(arquivo_das_peneiras,total_jogadores):
    print('Para criar a peneira são necessárias algumas informações')
    dia_da_peneira=input('Digite o dia da peneira (digite formato "dia/mês"): ')
    horario_inicio=input('Digite um horário para iniciar a peneira (digite no formato "xx:xx"): ')
    horario_fim=input('Digite um horário para finalizar a peneira (digite no formato "xx:xx"): ')
    jogos_masculinos=int(input('Digite o número de jogos masculinos: '))
    jogos_feminino=int(input('Digite o número de jogos femininos: '))
    local=input('Digite o local onde vai acontecer: ')
    numero_da_peneira=len(arquivo_das_peneiras)+1
    chave_peneira='peneira '+str(numero_da_peneira)
    arquivo_de_times=gerar_times(jogos_masculinos,jogos_feminino,total_jogadores,chave_peneira)
    return chave_peneira,{'dia da peneira':dia_da_peneira,
                          'horario inicio':horario_inicio,
                          'horario fim':horario_fim,
                          'local':local,
                          'times':arquivo_de_times}

def gerar_times(jogos_masculinos,jogos_feminino,total_jogadores,chave_peneira):
    arquivo_de_times={}
    posicoes=[
        'Goleiro',
        'Zagueiro',
        'Lateral',
        'Ala',
        'Volante',
        'Meio campo',
        'Meia atacante',
        'Ponta',
        'Centro avante'
    ]
    for numero_time in range(1,(jogos_masculinos*2)+1):
        nome_time='time '+str(numero_time)+' masculino'
        arquivo_de_times[nome_time]={}
        for posicao in posicoes:
            arquivo_de_times[nome_time][posicao]='EM FALTA DE JOGADOR'
            for cpf in total_jogadores:
                jogador=total_jogadores[cpf]
                if jogador['genero'] == 'M' and jogador['status_da_peneira'] == False and jogador['posicao'] == posicao:
                            arquivo_de_times[nome_time][posicao]=cpf
                            total_jogadores[cpf]['status_da_peneira']=chave_peneira
                            break
    for numero_time in range(1,(jogos_feminino*2)+1):
        nome_time='time '+str(numero_time)+' feminino'
        arquivo_de_times[nome_time]={}
        for posicao in posicoes:
            arquivo_de_times[nome_time][posicao]='EM FALTA DE JOGADOR'
            for cpf in total_jogadores:
                jogador=total_jogadores[cpf]
                if jogador['genero'] == 'F' and jogador['status_da_peneira'] == False and jogador['posicao'] == posicao:
                            arquivo_de_times[nome_time][posicao]=cpf
                            total_jogadores[cpf]['status_da_peneira']=chave_peneira
                            break
    return arquivo_de_times

def ver_peneira_funcionario(arquivo_das_peneiras,total_jogadores):
    if len(arquivo_das_peneiras) == 0:
        print('Nenhuma peneira cadastrada')
        return
    for peneira in arquivo_das_peneiras:
        print(" \n"
        f"PENEIRA: {peneira}\n"
        f"Local: {arquivo_das_peneiras[peneira]['local']}\n"
        f"Data: {arquivo_das_peneiras[peneira]['dia da peneira']}\n"
        f"Início: {arquivo_das_peneiras[peneira]['horario inicio']}\n"
        f"Fim: {arquivo_das_peneiras[peneira]['horario fim']}\n"
        ' ')
        for time in arquivo_das_peneiras[peneira]['times']:
            print(f'\n{time}')
            for posicao in arquivo_das_peneiras[peneira]['times'][time]:
                cpf = arquivo_das_peneiras[peneira]['times'][time][posicao]
                if cpf == 'EM FALTA DE JOGADOR':
                    print(f'{posicao}: EM FALTA DE JOGADOR')
                else:
                    print(f'{posicao}: {total_jogadores[cpf]["nome"]} ({cpf})')

def verificar_login_funcionario(login,senha,lista_de_funcionarios):
    return login in lista_de_funcionarios and senha == lista_de_funcionarios[login]

print("bem vindo ao motor lógico")
main()
