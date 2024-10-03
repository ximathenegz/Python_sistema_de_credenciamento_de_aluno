import json

# Função de salvar arquivo em json
def salvar_arquivo(lista_qualquer, nome_arquivo):
    with open(nome_arquivo, "w") as arquivo_aberto:
        json.dump(lista_qualquer, arquivo_aberto)

# Função de carregar arquivo em json
def ler_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo_aberto:
            lista_qualquer = json.load(arquivo_aberto)
        return lista_qualquer
    except:
        return []

# Função de processar o menu de operações

def processar_menu_operacoes(escolha2, nome_arquivo):
    if escolha2 == 1:
        incluir_cadastro(nome_arquivo)
    elif escolha2 == 2:
        listar_cadastros(nome_arquivo)
    elif escolha2 == 3:
        editar_cadastro(nome_arquivo)
    elif escolha2 == 4:
        excluir_cadastro(nome_arquivo)
    elif escolha2 == 0:
        print("Você pediu para retornar")
        return False
    else:
        print("Opção secundária inválida, repita:")
    return True

# Função de mostrar o menu principal
def mostrar_menu_principal():
    print("Seja bem-vindo(a) ao Sistema PUC.")
    print("\n MENU PRINCIPAL\n")
    print("(1) para ESTUDANTES")
    print("(2) para DISCIPLINAS")
    print("(3) para PROFESSORES")
    print("(4) para TURMAS")
    print("(5) para MATRÍCULAS")
    print("Digite (0) para sair")
    return int(input())

# Função de mostrar o menu de operações
def mostrar_menu_operacoes():
    print("\n Bem vindo ao menu secundário: (", escolha_cadastral, ")")
    print("\n MENU DE OPERAÇÕES \n")
    print('(1) para incluir')
    print("(2) para listar")
    print("(3) para atualizar")
    print("(4) para excluir")
    print("Digite (0) para retornar ao menu principal:")
    return int(input())

# Função de incluir cadastro, seja ele estudante, professor, turma, matricula ou disciplina.
def incluir_cadastro(nome_arquivo):
    # Criei a variável tipo_cadastro para poder reutilizar as funções para professor, turma, matricula e disciplina.
    tipo_cadastro = input("Digite o tipo de cadastro (estudante/professor/disciplina/turma/matricula): ")

    if tipo_cadastro == "estudante":
        codigo = int(input("Digite o código do estudante: "))
        nome = str(input("Digite o nome do(a) estudante: "))
        cpf = str(input("Digite o CPF do(a) estudante: "))
        print("Dados do estudante incluídos com sucesso.")

        dados_estudante = {"codigo": codigo, "nome": nome, "cpf": cpf}
        lista_qualquer = ler_arquivo(nome_arquivo)
        lista_qualquer.append(dados_estudante)
        salvar_arquivo(lista_qualquer, nome_arquivo)

    elif tipo_cadastro == "professor":
        codigo = int(input("Digite o código do professor: "))
        nome = str(input("Digite o nome do(a) professor: "))
        cpf = str(input("Digite o CPF do(a) professor: "))
        print("Dados do professor incluídos com sucesso.")

        dados_professor = {"codigo": codigo, "nome": nome, "cpf": cpf}
        lista_qualquer = ler_arquivo(nome_arquivo)
        lista_qualquer.append(dados_professor)
        salvar_arquivo(lista_qualquer, nome_arquivo)

    elif tipo_cadastro == "disciplina":
        codigo = int(input("Digite o código da disciplina: "))
        nome = str(input("Digite o nome da disciplina: "))
        print("Dados da disciplina incluídos com sucesso.")

        dados_disciplina = {"codigo": codigo, "nome": nome}
        lista_qualquer = ler_arquivo(nome_arquivo)
        lista_qualquer.append(dados_disciplina)
        salvar_arquivo(lista_qualquer, nome_arquivo)

    elif tipo_cadastro == "turma":
        codigo_turma = int(input("Digite o código da turma: "))
        codigo_professor = int(input("Digite o código do professor: "))
        codigo_disciplina = int(input("Digite o código da disciplina: "))
        print("Dados da turma incluídos com sucesso.")

        dados_turma = {"codigo_turma": codigo_turma, "codigo_professor": codigo_professor,
                       "codigo_disciplina": codigo_disciplina}
        lista_qualquer = ler_arquivo(nome_arquivo)
        lista_qualquer.append(dados_turma)
        salvar_arquivo(lista_qualquer, nome_arquivo)

    elif tipo_cadastro == "matricula":
        codigo_turma = int(input("Digite o código da turma: "))
        codigo_estudante = int(input("Digite o código do estudante: "))
        print("Dados da matrícula incluídos com sucesso.")

        dados_matricula = {"codigo_turma": codigo_turma, "codigo_estudante": codigo_estudante}
        lista_qualquer = ler_arquivo(nome_arquivo)
        lista_qualquer.append(dados_matricula)
        salvar_arquivo(lista_qualquer, nome_arquivo)

    else:
        print("Tipo de cadastro inválido.")

# Função de mostrar os cadastros na tela.
def listar_cadastros(nome_arquivo):
    escolha_cadastral2 = "Listar"
    lista_qualquer = ler_arquivo(nome_arquivo)
    print("Lista de dados incluídos:", lista_qualquer)

# Função de editar cadastros.
def editar_cadastro(nome_arquivo):
    tipo_cadastro = input("Digite o tipo de cadastro (estudante/professor/disciplina/turma/matricula): ")
    lista_qualquer = ler_arquivo(nome_arquivo)
    escolha_cadastral2 = "Atualizar"

    try:
        if tipo_cadastro == "estudante":
            codigo_para_editar = int(input("Qual o código de estudante que deseja editar: "))
            for cadastro in lista_qualquer:
                if cadastro.get("codigo") == codigo_para_editar:
                    cadastro["codigo"] = int(input("Digite o novo código do estudante: "))
                    cadastro["nome"] = input("Digite o novo nome do estudante: ")
                    cadastro["cpf"] = input("Digite o novo CPF do estudante: ")
                    print("Estudante atualizado com sucesso.")
                    break
            else:
                print(f"Não encontrei o estudante de código {codigo_para_editar} na lista.")

        elif tipo_cadastro == "professor":
            codigo_para_editar = int(input("Qual o código de professor que deseja editar: "))
            for cadastro in lista_qualquer:
                if cadastro.get("codigo") == codigo_para_editar:
                    cadastro["codigo"] = int(input("Digite o novo código do professor: "))
                    cadastro["nome"] = input("Digite o novo nome do professor: ")
                    cadastro["cpf"] = input("Digite o novo CPF do professor: ")
                    print("Professor atualizado com sucesso.")
                    break
            else:
                print(f"Não encontrei o professor de código {codigo_para_editar} na lista.")

        elif tipo_cadastro == "disciplina":
            codigo_para_editar = int(input("Qual o código da disciplina que deseja editar: "))
            for cadastro in lista_qualquer:
                if cadastro.get("codigo") == codigo_para_editar:
                    cadastro["codigo"] = int(input("Digite o novo código da disciplina: "))
                    cadastro["nome"] = input("Digite o novo nome da disciplina: ")
                    print("Disciplina atualizada com sucesso.")
                    break
            else:
                print(f"Não encontrei a disciplina de código {codigo_para_editar} na lista.")

        elif tipo_cadastro == "turma":
            codigo_para_editar = int(input("Qual o código da turma que deseja editar: "))
            for cadastro in lista_qualquer:
                if cadastro.get("codigo_turma") == codigo_para_editar:
                    cadastro["codigo_turma"] = int(input("Digite o novo código da turma: "))
                    cadastro["codigo_professor"] = int(input("Digite o novo código do professor: "))
                    cadastro["codigo_disciplina"] = int(input("Digite o novo código da disciplina: "))
                    print("Turma atualizada com sucesso.")
                    break
            else:
                print(f"Não encontrei a turma de código {codigo_para_editar} na lista.")

        elif tipo_cadastro == "matricula":
            codigo_para_editar = int(input("Qual o código da matrícula que deseja editar: "))
            for cadastro in lista_qualquer:
                if cadastro.get("codigo_matricula") == codigo_para_editar:
                    cadastro["codigo_turma"] = int(input("Digite o novo código da turma: "))
                    cadastro["codigo_estudante"] = int(input("Digite o novo código do estudante: "))
                    print("Matrícula atualizada com sucesso.")
                    break
            else:
                print(f"Não encontrei a matrícula de código {codigo_para_editar} na lista.")

    except KeyError:
        print("Erro: Chave ausente ao tentar editar o registro.")

    salvar_arquivo(lista_qualquer, nome_arquivo)


# Função de excluir cadastro
def excluir_cadastro(nome_arquivo):
    tipo_cadastro = input("Digite o tipo de cadastro (estudante/professor/disciplina/turma/matricula): ")
    lista_qualquer = ler_arquivo(nome_arquivo)
    escolha_cadastral2 = "Excluir"
    codigo_para_excluir = int(input("Qual é o código do(a) item que deseja excluir? "))

    try:
        if tipo_cadastro == "estudante":
            for cadastro in lista_qualquer:
                if cadastro["codigo"] == codigo_para_excluir:
                    lista_qualquer.remove(cadastro)
                    print(f"Código de estudante [{codigo_para_excluir}] excluído com sucesso.")
                    break
            else:
                print(f"Não encontrei o estudante de código {codigo_para_excluir} na lista.")

        elif tipo_cadastro == "professor":
            for cadastro in lista_qualquer:
                if cadastro["codigo"] == codigo_para_excluir:
                    lista_qualquer.remove(cadastro)
                    print(f"Código de professor [{codigo_para_excluir}] excluído com sucesso.")
                    break
            else:
                print(f"Não encontrei o professor de código {codigo_para_excluir} na lista.")

        elif tipo_cadastro == "disciplina":
            for cadastro in lista_qualquer:
                if cadastro["codigo"] == codigo_para_excluir:
                    lista_qualquer.remove(cadastro)
                    print(f"Código de disciplina [{codigo_para_excluir}] excluído com sucesso.")
                    break
            else:
                print(f"Não encontrei a disciplina de código {codigo_para_excluir} na lista.")

        elif tipo_cadastro == "turma":
            for cadastro in lista_qualquer:
                if cadastro["codigo_turma"] == codigo_para_excluir:
                    lista_qualquer.remove(cadastro)
                    print(f"Código de turma [{codigo_para_excluir}] excluído com sucesso.")
                    break
            else:
                print(f"Não encontrei a turma de código {codigo_para_excluir} na lista.")

        elif tipo_cadastro == "matricula":
            for cadastro in lista_qualquer:
                if cadastro["codigo_matricula"] == codigo_para_excluir:
                    lista_qualquer.remove(cadastro)
                    print(f"Código de matrícula [{codigo_para_excluir}] excluído com sucesso.")
                    break
            else:
                print(f"Não encontrei a matrícula de código {codigo_para_excluir} na lista.")
    except KeyError:
        print("Erro: Chave ausente ao tentar excluir o registro.")

    salvar_arquivo(lista_qualquer, nome_arquivo)


# Arquivos criados para a persistência dos dados.
arquivo_estudante = "estudantes.json"
arquivo_disciplina = "disciplinas.json"
arquivo_professor = "professores.json"
arquivo_turma = "turmas.json"
arquivo_matricula = "matriculas.json"

# Listas
lista_estudantes = []
lista_professores = []
lista_disciplinas = []
lista_turmas = []
lista_matriculas = []

# Loop principal
while True:
    escolha = mostrar_menu_principal()
    escolha_cadastral = ""

    if escolha == 1:
        escolha_cadastral = "Estudantes"
        while True:
            escolha2 = mostrar_menu_operacoes()
            escolha_cadastral2 = ""
            if not processar_menu_operacoes(escolha2, arquivo_estudante):
                break
    elif escolha == 2:
        escolha_cadastral = "Disciplinas"
        while True:
            escolha2 = mostrar_menu_operacoes()
            escolha_cadastral2 = ""
            if not processar_menu_operacoes(escolha2, arquivo_disciplina):
                break
    elif escolha == 3:
        escolha_cadastral = "Professores"
        while True:
            escolha2 = mostrar_menu_operacoes()
            escolha_cadastral2 = ""
            if not processar_menu_operacoes(escolha2, arquivo_professor):
                break
    elif escolha == 4:
        escolha_cadastral = "Turmas"
        while True:
            escolha2 = mostrar_menu_operacoes()
            escolha_cadastral2 = ""
            if not processar_menu_operacoes(escolha2, arquivo_turma):
                break
    elif escolha == 5:
        escolha_cadastral = "Matrículas"
        while True:
            escolha2 = mostrar_menu_operacoes()
            escolha_cadastral2 = ""
            if not processar_menu_operacoes(escolha2, arquivo_matricula):
                break
    elif escolha == 0:
        break
    else:
        print("Comando inválido, repita:")
        continue