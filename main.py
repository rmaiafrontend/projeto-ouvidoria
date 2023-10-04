from operacoesOuvidoria import *
from operacoesbd import *

conexao = abrirBancoDados('localhost','root', '12345', 'ouvidoria')
sqlListarMafinestacoes = 'select * from manifestacoes;'

listaManifestacoes = listarBancoDados(conexao, sqlListarMafinestacoes)
opcao = 20

print('Olá, Para fazer uma solicitação, sugestão, elogio, crítica, reclamação ou denúncia, Clique em uma das opções abaixo.\n')


while opcao != 7:
    print('[ 1 ] Listagem de manifestações')
    print('[ 2 ] Criar uma nova manifestação')
    print('[ 3 ] Exibir quantidade de manifestações')
    print('[ 4 ] Pesquisar manifestação por protocolo')
    print('[ 5 ] Remover manifestação')
    print('[ 6 ] Alterar manifestação')
    print('[ 7 ] Sair do sistema')

    opcao = int(input('Digite sua opção:\n'))

    if opcao == 1:
        listar_manifestacoes()
    elif opcao == 2:
        criar_manifestacao(listaManifestacoes)
    elif opcao == 3:
        exibir_quantidade_manifestacoes()
    elif opcao == 4:
        pesquisar_manifestacao()
    elif opcao == 5:
        remover_manifestacao()
    elif opcao == 6:
        alterar_manifestacao()
    elif opcao != 7:
        print('Opção Inválida')
    else:
        print('Obrigado pela sua colaboração')


encerrarBancoDados(conexao)