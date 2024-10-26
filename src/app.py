from datetime import datetime

def calcular_idade(data_nascimento):
    hoje = datetime.today()
    nascimento_datetime = datetime.strptime(data_nascimento, "%d/%m/%Y")
    diferenca = hoje - nascimento_datetime
    idade = diferenca.days // 365
    return idade

if __name__ == "__main__":
    nascimento = input("Digite sua data de nascimento (dd/mm/yyyy): ")
    idade = calcular_idade(nascimento)
    print(f"Sua idade é {idade}")
