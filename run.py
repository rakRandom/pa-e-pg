from modules import *

__author__ = "Fellipe Leonardo"


def run():
    pa_obj = pa.PA()
    pg_obj = pg.PG()

    user_input: str
    initial_val: float
    second_val: float
    increase_val: float
    result: float
    num_quantity: int

    user_input = input("Deseja executar uma P.A. ou P.G.?\n[PA] / [PG]: ").lower()

    if user_input == "pa":
        user_input = input("\nDeseja saber a razão, valor na posição N ou a soma da P.A.?\n[R] / [N] / [S]: ").lower()
        initial_val = float(input("\nDigite o valor inicial da sequência: "))

        if user_input == 'r':
            second_val = float(input("Digite o segundo valor da sequência: "))

            result = pa_obj.progression(initial_val, second_val)

            print(f"A razão da sua P.A. é: {result:.2f}")

        elif user_input == 'n':
            num_quantity = int(input("Digite a posição para ser encontrada: "))
            increase_val = float(input("Digite a razão da sua P.A.: "))

            result = pa_obj.nth_value(initial_val, num_quantity, increase_val)

            print(f"O número da sua P.A. na posição {num_quantity} é {result:.2f}")

        elif user_input == 's':
            num_quantity = int(input("Digite a posição para ser encontrada: "))
            increase_val = float(input("Digite a razão da sua P.A.: "))

            result = pa_obj.value_sum(initial_val, num_quantity, increase_val)

            print(f"O resultado da soma da sua P.A. de 1 até {num_quantity} (inclusivo) é {result:.2f}")

    elif user_input == "pg":
        user_input = input("\nDeseja saber a razão, valor na posição N ou a soma da P.G.?\n[R] / [N] / [S]: ").lower()
        initial_val = float(input("\nDigite o valor inicial da sequência: "))

        if user_input == 'r':
            second_val = float(input("Digite o segundo valor da sequência: "))

            result = pg_obj.progression(initial_val, second_val)

            print(f"A razão da sua P.G. é: {result:.2f}")

        elif user_input == 'n':
            num_quantity = int(input("Digite a posição para ser encontrada: "))
            increase_val = float(input("Digite a razão da sua P.A.: "))

            result = pg_obj.nth_value(initial_val, num_quantity, increase_val)

            print(f"O número da sua P.G. na posição {num_quantity} é {result:.2f}")

        elif user_input == 's':
            user_input = input("Sua soma é finita?\n[S] / [N]: ").lower()

            if user_input == 's':
                num_quantity = int(input("Digite a posição para ser encontrada: "))
                increase_val = float(input("Digite a razão da sua P.G.: "))

                result = pg_obj.finite_value_sum(initial_val, num_quantity, increase_val)

                print(f"O resultado da soma da sua P.G. de 1 até {num_quantity} (inclusivo) é {result:.2f}")

            elif user_input == 'n':
                increase_val = float(input("Digite a razão da sua P.G.: "))

                result = pg_obj.infinite_value_sum(initial_val, increase_val)

                print(f"O resultado da soma infinita da sua P.G. é {result:.2f}")


if __name__ == "__main__":
    run()
