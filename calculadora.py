def calculadora(numeros):
    formula = ""
    for i in range(len(numeros)):
        if numeros[i] == "x":
            formula += "*"
        elif numeros[i] == "÷" or i == "/":
            formula += "/"
        else:
            formula += numeros[i]
    
    calculo = eval(formula)

    return calculo

if __name__ == "__main__":
    print(calculadora(str(input("Informe os numero que deseja calcular: "))))
