from datetime import datetime

def multi_porcentagem(percen): # calcula a porcentagem multiplicando
    percen = float(percen)
    resultado = percen / 100
    return str(resultado)

def soma_porcentagem(percen): # calcula a porcentagem positiva
    percen = float(percen)
    resultado = percen / 100
    resultado = 1.0 + resultado
    
    return str(resultado)

def validar(num):
    lista = [",",".","*","x","+","/","-","÷","%","r","q"]
    for letra in num:
        if not letra.isdigit():
            if not letra in lista:
                return False           
    return True             

def calculadora(numeros):
    #gerando um arquivo log temporario toda vez que o o codigo for execultado ele ira escluir os dados e iniciar novamente
    with open("log_Temporario.txt", "w", encoding="utf-8") as arquivo_log:
        print(f"="*33+" CALCULADORA INICIADO COM SUCESSO "+"="*33+f"\nDATA e HORA: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n",file=arquivo_log)
    
    # gera o historico completo dos logues de todos os calculos
    with open("calculadora.log", "a", encoding="utf-8") as arquivo_log:
            print(f"="*33+" CALCULADORA INICIADO COM SUCESSO "+"="*33+f"\nDATA e HORA: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n",file=arquivo_log)    
    
    if not validar(numeros): # Retorna falso sé o criterio de caracteres não for aceito
        return 'Valor invalido'
        
    # organiza os caracteres antes de continuamos
    formula = numeros.replace("x", "*").replace("÷", "/").replace(",", ".")
    
    while "%" in formula:
        crt = formula.find("%") # Encontra a posição do primeiro "%"
        
        
        fatia = formula[:crt] # fatia o testo aparti da posiçao do '%'
        fatia_invertida = fatia[::-1] # inverte a fatia
        
        porce_invertida = ""
        sinal_origem = ""
        posicao_sinal = -1
        
        # Captura o número da porcentagem andando para trás
        for n in range(len(fatia_invertida)):
            caractere = fatia_invertida[n]
            if caractere.isdigit() or caractere == ".":
                porce_invertida += caractere
            elif caractere in ["+", "-", "*", "/"]:
                sinal_origem = caractere
                posicao_sinal = len(fatia) - 1 - n # Descobre o índice real do sinal na string original
                break
                
        porce = porce_invertida[::-1] # Desinverte o número da porcentagem para a posição original
        
        if sinal_origem == "+": # se o sinal da porecentage for '+'      
            fator_soma = soma_porcentagem(porce) # usando a função 'soma_porcentagem'
            
            # log temporario
            with open("log_Temporario.txt", "a", encoding="utf-8") as arquivo_log: # criando o log dos valores retornado 
                print(f"{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}: Resultado da função 'soma_porcentagem'\nResultado: {fator_soma}\n"+"-"*100,file=arquivo_log)

            # historico de log
            with open("calculadora.log", "a", encoding="utf-8") as arquivo_log: # criando o log dos valores retornado 
                print(f"{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}: Resultado da função 'soma_porcentagem'\nResultado: {fator_soma}\n"+"-"*100,file=arquivo_log)
                            
            # Pegamos tudo que estava antes do sinal de "+"
            parte_anterior = formula[:posicao_sinal]
            # log temporario
            with open("log_Temporario.txt", "a", encoding="utf-8") as arquivo_log: # criando o log dos valores retornado 
                print(f"{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}: Pegando a parte anterio ao sinal\nResultado: {parte_anterior}\n"+"-"*100,file=arquivo_log)
            # historico de log
            with open("calculadora.log", "a", encoding="utf-8") as arquivo_log: # criando o log dos valores retornado 
                print(f"{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}: Pegando a parte anterio ao sinal\nResultado: {parte_anterior}\n"+"-"*100,file=arquivo_log)
            
            # Resolvemos o valor acumulado até aqui antes de aplicar a multiplicação
            valor_acumulado = str(eval(parte_anterior))
            # log temporario
            with open("log_Temporario.txt", "a", encoding="utf-8") as arquivo_log: # criando o log dos valores retornado 
                print(f"{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}: soma da porcentagem já resolvida antes do proximo calculo\nResultado: {valor_acumulado}\n"+"-"*100,file=arquivo_log)
            # historico de log
            with open("calculadora.log", "a", encoding="utf-8") as arquivo_log: # criando o log dos valores retornado 
                print(f"{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}: soma da porcentagem já resolvida antes do proximo calculo\nResultado: {valor_acumulado}\n"+"-"*100,file=arquivo_log)
                            
            nova_fatia_calculada = f"*{fator_soma}" # adicionado os valores da soma porcentagem caso tenha mais de uma porcentagem
            
            # Remonta a fórmula com o pedaço atualizado e o que sobrou depois do "%"
            formula = valor_acumulado + nova_fatia_calculada + formula[crt + 1:]
        
        # calcular a multiplicação de porcentagem
        elif sinal_origem == "*":
            fator_multiplicacao = multi_porcentagem(porce) # função para multiplicar os valores
            
            # log temporario
            with open("log_Temporario.txt", "a", encoding="utf-8") as arquivo_log: # criando o log dos valores retornado 
                print(f"{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}: Multiplicação da porcentagem já resolvida antes do proximo calculo\nResultado: {fator_multiplicacao}\n"+"-"*100,file=arquivo_log)
            # historico de log
            with open("calculadora.log", "a", encoding="utf-8") as arquivo_log: # criando o log dos valores retornado 
                print(f"{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}: Multiplicação já resolvida antes do proximo calculo\nResultado: {fator_multiplicacao}\n"+"-"*100,file=arquivo_log)
            
            # Pegamos tudo que estava antes do sinal de "*"
            parte_anterior = formula[:posicao_sinal]
            # log temporario
            with open("log_Temporario.txt", "a", encoding="utf-8") as arquivo_log: # criando o log dos valores retornado 
                print(f"{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}: Pegando a parte anterio ao sinal\nResultado: {parte_anterior}\n"+"-"*100,file=arquivo_log)
            # historico de log
            with open("calculadora.log", "a", encoding="utf-8") as arquivo_log: # criando o log dos valores retornado 
                print(f"{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}: Pegando a parte anterio ao sinal\nResultado: {parte_anterior}\n"+"-"*100,file=arquivo_log)
            
            # Resolvemos o valor acumulado até aqui antes de aplicar a multiplicação
            valor_acumulado = str(eval(parte_anterior))
            # log temporario
            with open("log_Temporario.txt", "a", encoding="utf-8") as arquivo_log: # criando o log dos valores retornado 
                print(f"{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}: soma da porcentagem já resolvida antes do proximo calculo\nResultado: {valor_acumulado}\n"+"-"*100,file=arquivo_log)
            # historico de log
            with open("calculadora.log", "a", encoding="utf-8") as arquivo_log: # criando o log dos valores retornado 
                print(f"{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}: soma da porcentagem já resolvida antes do proximo calculo\nResultado: {valor_acumulado}\n"+"-"*100,file=arquivo_log)
                            
            nova_fatia_calculada = f"*{fator_multiplicacao}" # adicionado os valores da soma porcentagem caso tenha mais de uma porcentagem
            
            # Remonta a fórmula com o pedaço atualizado e o que sobrou depois do "%"
            formula = valor_acumulado + nova_fatia_calculada + formula[crt + 1:]

        else:
            formula = formula[:posicao_sinal + 1] + f"({porce}/100)" + formula[crt + 1:] # para evitar erro caso colocado outros numeros
    # log temporario    
    with open("log_Temporario.txt", "a", encoding="utf-8") as arquivo_log:
        print(f"{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}: Formula finalizada!\n\n"+"="*100,"\n",file=arquivo_log)
    # historico de log
    with open("calculadora.log", "a", encoding="utf-8") as arquivo_log:
        print(f"{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}: Formula finalizada!\n\n"+"="*100,"\n",file=arquivo_log)
        
    calculo = eval(formula)
    return calculo

if __name__ == "__main__":
    expressao_teste = "100x10%+10%" # Valor texte só mente para validar a formula
    print(f"Calculando para: {expressao_teste}")
    print(f"Resultado final: {calculadora(expressao_teste)}")

