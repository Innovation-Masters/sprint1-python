import random
import time

# Dados do quiz
quiz_questions = [
    {
        "question": "Qual é a origem da Fórmula E?",
        "options": ["A. Japão", "B. Estados Unidos", "C. França", "D. China"],
        "answer": "C"
    },
    {
        "question": "Em que ano ocorreu a primeira temporada da Fórmula E?",
        "options": ["A. 2000", "B. 2014", "C. 2018", "D. 2020"],
        "answer": "B"
    },
    {
        "question": "Quantas equipes competem na Fórmula E?",
        "options": ["A. 10", "B. 12", "C. 15", "D. 20"],
        "answer": "B"
    },
    {
        "question": "Quem foi o campeão da primeira temporada da Fórmula E?",
        "options": ["A. Nelson Piquet Jr.", "B. Jean-Éric Vergne", "C. Lucas di Grassi", "D. Sébastien Buemi"],
        "answer": "A"
    },
    {
        "question": "Qual é o principal objetivo da Fórmula E?",
        "options": ["A. Entretenimento", "B. Inovação em veículos elétricos", "C. Ganhar dinheiro", "D. Turismo"],
        "answer": "B"
    }
]

# Estatísticas de pilotos e equipes (exemplo simplificado)
driver_stats = {
    "Nelson Piquet Jr.": "Vitórias: 3, Pódios: 5, Pontos: 150",
    "Jean-Éric Vergne": "Vitórias: 10, Pódios: 20, Pontos: 500",
    "Lucas di Grassi": "Vitórias: 12, Pódios: 25, Pontos: 600",
    "Sébastien Buemi": "Vitórias: 13, Pódios: 23, Pontos: 580"
}

# FUNÇÕES

def mensagem_inicial():
    print("="*12)
    print("FORMULA E")
    print("="*12)
    time.sleep(1)
    print("Bem-vindo ao Informativo Interativo sobre a Fórmula E!")

def menu_inicial():
    print("="*45)
    print("1. Iniciar Quiz")
    print("2. Ver Pontuação do Quiz")
    print("3. Estatísticas de Pilotos e Equipes")
    print("4. Simulador de Corridas")
    print("5. Sair")
    print("="*45)
    opcao = int(input("Escolha uma opção: "))
    return opcao

def iniciar_quiz(quiz_questions):
    print("Iniciando o quiz sobre Fórmula E...")
    pontuacao = 0
    for idx, question in enumerate(quiz_questions):
        print(f"\nPergunta {idx + 1}: {question['question']}")
        for option in question['options']:
            print(option)
        resposta = input("Sua resposta (A/B/C/D): ").upper()
        if resposta == question["answer"]:
            print("Correto!")
            pontuacao += 1
        else:
            print(f"Errado! A resposta correta é {question['answer']}")
        time.sleep(1)
    return pontuacao

def ver_pontuacao(pontuacao):
    print(f"\nSua pontuação atual é: {pontuacao} de {len(quiz_questions)}")
    time.sleep(2)

def estatisticas_pilotos(driver_stats):
    print("="*45)
    print("Estatísticas de Pilotos e Equipes")
    print("="*45)
    for driver, stats in driver_stats.items():
        print(f"{driver}: {stats}")
    time.sleep(2)

def simulador_corridas():
    print("="*45)
    print("Simulador de Corridas")
    print("="*45)
    print("Simulando resultados da próxima corrida...")
    time.sleep(2)
    resultados = ["Nelson Piquet Jr. venceu a corrida!", "Jean-Éric Vergne teve problemas no carro e ficou em 5º lugar.", "Lucas di Grassi fez a volta mais rápida!"]
    print(random.choice(resultados))
    time.sleep(2)

# Inicializando a pontuação
pontuacao = 0

# Mensagem inicial
mensagem_inicial()

# Loop do menu
while True:
    opcao = menu_inicial()

    if opcao == 1:
        pontuacao = iniciar_quiz(quiz_questions)
        ver_pontuacao(pontuacao)

    elif opcao == 2:
        ver_pontuacao(pontuacao)

    elif opcao == 3:
        estatisticas_pilotos(driver_stats)

    elif opcao == 4:
        simulador_corridas()

    elif opcao == 5:
        print("Obrigado por participar do informativo da Fórmula E!")
        time.sleep(1)
        break

    else:
        print("Opção inválida")
