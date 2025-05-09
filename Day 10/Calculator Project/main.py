import art
print(art.logo)
def add(n1, n2):
    return n1 + n2
def sub(n1, n2):
    return n1 - n2
def multip(n1, n2):
    return n1 * n2
def divide(n1, n2):
    if n2 == 0:
        raise ZeroDivisionError("Não é possível dividir por zero.")
    return n1 / n2
symbols = {"+": add,"-": sub,"*": multip,"/": divide}
#print(symbols['*'](4, 8))
def calculator():
    continue_calc = True
    first_number = None

    while continue_calc:
        try:
            if first_number is None:
                first_number = int(input("Digite o primeiro número:\n"))

            symbol = input("Digite o operador matemático (+, -, *, /):\n")
            if symbol not in symbols:
                raise ValueError("Operador inválido.")

            second_number = int(input("Digite o próximo número:\n"))
            result = symbols[symbol](first_number, second_number)
            choice = input(f"Quer continuar calculando com {result}? (s/n):\n").strip().lower()
            if choice == 's':
                first_number = result
            else:
                reset = input("Deseja iniciar um novo cálculo? (s/n):\n").strip().lower()
                if reset == 's':
                    first_number = None
                else:
                    continue_calc = False
                    print("Encerrando a calculadora.")

        except ValueError as ve:
            print(f"Erro de valor: {ve}")
        except ZeroDivisionError as zde:
            print(f"Erro: {zde}")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")

calculator()