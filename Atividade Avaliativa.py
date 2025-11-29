def chatbot():
    print("BEM-VINDO AO CHATBOT DE AGENDAMENTO")
    print("**************************************\n")

    nome = input("Qual o seu nome? ")

    print("\nEscolha o tipo de consulta:")
    print("1 - Clínica Geral")
    print("2 - Odontologia")
    print("3 - Cardiologia")
    print("4 - Ortopedia")

    opcao = input("Digite apenas o número da opção desejada: ")

    tipos = {
        "1": "Clínica Geral",
        "2": "Odontologia",
        "3": "Cardiologia",
        "4": "Ortopedia"
    }

    tipo_consulta = tipos.get(opcao, "error")

    data = input("\nInforme a data da consulta (dd/mm/aaaa): ")
    horario = input("Informe o horário da consulta (hh:mm): ")

    print("\n*   *    *    *     *")
    print("RESUMO DO AGENDAMENTO\n")
    print("*  *  *  *  *  *  *  *  *  *")
    print(f"Paciente: {nome}")
    print(f"Consulta: {tipo_consulta}")
    print(f"Data: {data}")
    print(f"Horário: {horario}")
    print("==============================================\n")

    # Confirmação
    confirmacao = input("Deseja confirmar o agendamento? (s/n): ")

    if confirmacao.lower() == "s":
        print("\nAgendamento confirmado com sucesso!")
    else:
        print("\nAgendamento cancelado.")

    print("\nObrigado por usar o chatbot!\n")


chatbot()

