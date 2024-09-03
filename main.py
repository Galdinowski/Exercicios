import json

#EX2
print("\n")
print(f"Comecando o exercicio 2: \n")

def fibonacci(n):
    if n < 0:
        return False
    
    a, b = 0, 1
    while b <= n:
        if b == n:
            return True
        a, b = b, a + b
    
    return False


numero = int(input("Digite um numero: "))
if fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")
    
    
    

      #EX 3
print("\n")
print(f"Comecando o exercicio 3: \n")

with open('/home/galdino/Documents/Arquivos_VSCODE/python/Exercicios/diasDoFaturamento.json') as fat:
     faturamentoMensal = json.load(fat)
     
def calcFatMensal(faturamentoMensal):
   
    faturamentos = [dia['valor'] for dia in faturamentoMensal if dia['valor'] > 0]
    
    maior_faturamento = max(faturamentos)
    menor_faturamento = min(faturamentos)
    
    
    mediaFatmensal = sum(faturamentos) / len(faturamentos)
    dias_acima_da_media = sum(1 for valor in faturamentos if valor > mediaFatmensal)
    
    return menor_faturamento, maior_faturamento, dias_acima_da_media

menor, maior, dias_acima_media = calcFatMensal(faturamentoMensal)

print(f"Menor faturamento: R$ {menor:,.2f}")
print(f"Maior faturamento: R$ {maior:,.2f}")
print(f"Dias com faturamento acima da média: {dias_acima_media}")

    
    
    
    
#EX4
print("\n")
print(f"Comecando o exercicio 4: \n")

with open ('/home/galdino/Documents/Arquivos_VSCODE/python/Exercicios/faturamento.json') as f:
        data = json.load(f)

def calcular_percentuais(data):
    total = sum(data.values())
    fatpercentual = {estado: (valor / total) * 100 for estado, valor in data.items()}
    return fatpercentual

# Exemplo de uso

fatpercentual = calcular_percentuais(data)
for estado, percentual in fatpercentual.items():
    print(f"{estado}: {percentual:.2f}%")

    


    #EX5
print("\n")
print(f"Comecando o exercicio 5: \n")

palavra = input("Digite uma palavra: ")
palavra_invertida = ""
for letra in palavra[::-1]:
    palavra_invertida += letra
print(palavra_invertida)  

