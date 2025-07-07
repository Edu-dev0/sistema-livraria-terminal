print("bem vindo a livraria de Miqueias Eduardo")
lista_livro=[]
id_global= 0

def cadastra_livro(id):
    """
    função para cadastra livros e coloca-los dentro da lista
    """
    print ('-'*8 + "cadastra livro" + 8*'-')
    nome=(input("nome do livro: "))
    autor=(input("nome do autor(a): "))
    editora=(input("nome da editora: "))
    livro={
         "id":id,
        "nome":nome,
        "autor":autor,
        "detalhes":{
            "editora":editora
         }
     }

    lista_livro.append(livro)
    print("livro cadastrado!")

def consultar_livro():
   """
   função para consultar todos os livros ou livros especificos através do id e do autor.
   """
   while True:
      print('-'*8 + "Consultar Livros" + 8 *'-')
      print("1. Consultar Todos")
      print("2. Consultar por ID")
      print("3. Consultar por Autor")
      print("4. Voltar")

      opção=input("opção: ")

      if(opção=='1'):
       print("todos os livros: ")

       for livro in lista_livro:
        print(f"\nID: {livro['id']}|Nome: {livro['nome']}|Autor(a): {livro['autor']}|editora: {livro['detalhes']['editora']}")
       
      
      elif(opção == '2'):
         try:
          id_busca = int(input("ID do livro: "))
         except ValueError:
             print("\nPor favor, digite um número válido.\n")
             continue
         
         livro_encontrado=False #iniciando a variavel

         for livro in lista_livro:
            if livro["id"] == id_busca:
                    print(f"\nLivro encontrado:")
                    print(f"ID: {livro['id']}")
                    print(f"Nome: {livro['nome']}")
                    print(f"Autor(a): {livro['autor']}")
                    print(f"Editora: {livro['detalhes']['editora']}\n")
                    livro_encontrado=True #true se o livro for encontrado
                    break
            
         if(not livro_encontrado):
                print("\nLivro não encontrado!\n")
                

      elif opção == '3':
            autor_busca = input("Nome do autor(a): ")
            livro_encontrado=False

            print(f"\nLivros de {autor_busca}:")

            for livro in lista_livro:
                if livro['autor'].lower() == autor_busca.lower():
                    print(f"\nID: {livro['id']} |livro: {livro['nome']} - editora: {livro['detalhes']['editora']}\n")
                    livro_encontrado=True
            if(not livro_encontrado):
                    print("\nAutor não encontrado!\n")
        
      elif(opção=='4'):
          break
      
      else: 
          print("\nopção inválida!\n")
          continue

def remover_livro():
    try:
     id_remover=int(input("digite o id do livro a ser removido: "))
    except ValueError:
        print("\nEntrada inválida. Digite apenas números.\n")
        return

    for i, livro in enumerate(lista_livro):
        if livro["id"] == id_remover:
            del lista_livro[i]
            print("\nLivro removido com sucesso!\n")
            return
    print("ID não encontrado!")

#programa principal

while True:
     print('-'*30)
     print('-'*8 + "MENU PRINCIPAL" + 8*'-' )
     print('-'*30)

     print("1. Cadastrar Livro")
     print("2. Consultar Livros")
     print("3. Remover Livro")
     print("4. Sair")
     
     opcao = input("Escolha uma opção: ")
        
     if opcao == '1':
        id_global += 1
        cadastra_livro(id_global)
        
     elif opcao == '2':
         consultar_livro()
        
     elif opcao == '3':
            remover_livro()
        
     elif opcao == '4':
            print("Saindo do sistema...")
            break
        
     else:
            print("Opção inválida!")
