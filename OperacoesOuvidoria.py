from operacoesbd import *

conexao = abrirBancoDados('localhost','root', '12345', 'ouvidoria')
sqlListarMafinestacoes = 'select * from manifestacoes;'

def listar_manifestacoes():
    manifestacoes = listarBancoDados(conexao, sqlListarMafinestacoes)
    if len(manifestacoes) > 0:
        print('Manifestações cadastradas:')
        for protocolo, descricao in manifestacoes:
            manifestacao_formatada = f"{protocolo} - {descricao}"
            print(manifestacao_formatada)
    else:
        print('Não há manifestações a serem exibidas.')

def criar_manifestacao(listaManifestacoes):
    manifestacoes = listarBancoDados(conexao, sqlListarMafinestacoes)
    tiposManifestacao = ['Reclamação', 'Sugestão', 'Elogio']

    print('Qual tipo de manifestação você deseja registrar?')

    for i in range(len(tiposManifestacao)):
        print(f'[{i+1}] {tiposManifestacao[i]}')

    tipo = int(input('Digite o tipo de manifestação que deseja: \n'))

    if tipo > 3:
       return print('Opção Inválida - Tente Novamente')