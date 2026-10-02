def validar(num):
    lista = [",",".","x","+","/","-","÷","%","r","q"]
    
    for letra in num:
        if not letra.isdigit():
            if not letra in lista:
                return False           
            
    return True             
                

def calculadora(numeros):
    formula = ""
    if validar(numeros):
        for crt in numeros:
            if crt == "x":
                formula += "*"
            elif crt == "÷" or crt == "/":
                formula += "/"
            else:
                formula += crt
        calculo = eval(formula)

        return calculo
    else:
            return f'Valor invalio'            
            
        


if __name__ == "__main__":
    print(calculadora(str(input("Informe os numero que deseja calcular: "))))
