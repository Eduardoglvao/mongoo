# Primeiro a importação do pymongo ou mongoDB
from pymongo import MongoClient
 #Iniciando a conexão com o Banco de dados ("MongoDB")
connection_string = 'mongodb://localhost:27017'#Faça a váriavel e conecte com Banco de dados
client = MongoClient(connection_string)
mydb = client["MeuBanco"]
mycol = mydb.get_collection('minhaCollection')

#Base do código while para iniciar o crude#
while True:
    print("\n1. Criar Documento\n2. Ler Documentos\n3. Atualizar Documento\n4. Deletar Documento\n5. Sair")
    escolha = int(input("Escolha uma opção: "))
    #Função Criar 
    if escolha == 1:
        #Criar()
        nome = input("Digite o nome: ")
        idade = int(input("Digite a idade: "))
        documento = {"nome": nome, "idade": idade}
        mycol.insert_one(documento)
        print("Documento criado com sucesso!")
        
        #Função Ler 
    elif escolha == 2:
        #Ler()
     for doc in mycol.find():
         print(doc)
         
         #Função Atualizar
    elif escolha == 3:
        #Atualizar()
        filtro = {"nome": input("Digite o nome do documento que quer atualizar: ")}
        Novonome = input("Digite um novo nome para o documento: ")
        Novaidade = int(input("Digite a nova idade: "))
        NovoValor = {"$set": {"nome": Novonome, "idade": Novaidade}}
        mycol.update_one(filtro, NovoValor)
        print("Documento foi Atualizado!")
        
    #Função Deletar 
    elif escolha == 4:
        #Deletar()
        filtro = {"nome": input("Digite o nome do documento que quer deletar: ")}
        mycol.delete_one(filtro)
        print("Documento deletado!")
        
    #Função Sair (para sair do código)
    elif escolha == 5:
        #Sair()
        print("Saindo...")
        break
    else:
        print("Opção inválida!")
        #sair do programa, autoexplicativo.