# VARIAVEIS E TIPOS DE DADOS

#Tres tipos basicos de variáveis: INT - FLOAT - STRING

#Outro tipo comum de variável: BOOLEAN >> True - False 


# PROGRAMA QUE CALCULA A IDADE
def main(ano_nascimento):

    # Mostra o objetivo do Programa
    print("VAMOS CALCULAR A IDADE DESEJADA:")

    #variáveis
    ano_atual = 2023

    #calculando a idade
    idade = ano_atual - ano_nascimento

    #mostrando o resultado do calculo 
    print(f"A idade calculada é de {idade} anos.")


if __name__ == "__main__":
   
    ano_nascimento = 1975
    main(ano_nascimento)