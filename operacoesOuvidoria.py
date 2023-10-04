
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


    print(tiposManifestacao[tipo-1])

    for i in range(len(tiposManifestacao)):
        if i+1 == tipo:
            textoInput = 'Descreva sua ' + tiposManifestacao[i] + ': '
            manifestacao = input(textoInput)
            manifestacao = f'[{tiposManifestacao[i]}] {manifestacao}'

            print(manifestacao)

            insertManifestacao = f'insert into manifestacoes(descricao) values(%s)'
            dado = [manifestacao]

            insertNoBancoDados(conexao, insertManifestacao, dado)
            protocolo = len(manifestacoes) + 1
            print('Manifestação cadastrada com sucesso!')


def exibir_quantidade_manifestacoes():
    manifestacoes = listarBancoDados(conexao, sqlListarMafinestacoes)
    print(f'Até o momento, você abriu exatas {len(manifestacoes)} manifestações')

def pesquisar_manifestacao():
    listar_manifestacoes()
    protocolo = int(input('Informe o protocolo da manifestação:\n '))

    sqlPesquisarManifestacao = f'SELECT * FROM manifestacoes WHERE protocolo = {protocolo}'

    manifestacao = listarBancoDados(conexao, sqlPesquisarManifestacao)

    if len(manifestacao) > 0:
        print('Manifestação encontrada:')
        for protocolo, descricao in manifestacao:
            manifestacao_formatada = f"{protocolo} - {descricao}"
            print(manifestacao_formatada)

    else:
        print('Manifestação não encontrada.')

def remover_manifestacao():
    manifestacoes = listarBancoDados(conexao, sqlListarMafinestacoes)

    if len(manifestacoes) != 0:
        listar_manifestacoes()
        protocolo = int(input('Informe o número do protocolo da manifestação a ser removida:\n '))
        deleteManifestacao = f"DELETE FROM manifestacoes where protocolo = %s"
        dado = [protocolo]
        excluirBancoDados(conexao, deleteManifestacao, dado)
        print('Manifestação removida')
    else:
        print("Não há manifestações para serem removidas")

def alterar_manifestacao():
    manifestacoes = listarBancoDados(conexao, sqlListarMafinestacoes)
    if len(manifestacoes) != 0:
        listar_manifestacoes()
        protocolo = int(input('Informe o número do protocolo da manifestação a ser alterada:\n '))
        if 1 <= protocolo:
            novaDescricao = input("Digite a nova descrição da manifestação: ")
            updateManifestacao = "UPDATE manifestacoes SET descricao = %s WHERE protocolo = %s"
            dados = [novaDescricao, protocolo]
            atualizarBancoDados(conexao, updateManifestacao, dados)
            print("Manifestação alterada com sucesso!")
        else:
            print('Protocolo inválido!')
    else:
        print("Não há manifestações a serem alteradas.")





