################## CLI CALCULATOR PROJECT BY MURILO SILVA (MS) ##################

import re


class Calculator:
    def __init__(self) -> None:
        self.result = 'Nada ocorreu :('
        print('\n {:*^100s}'.format('WELCOME TO CLI CALCULATOR'))
        print('''\
            Operações disponíveis: \n \
            1.\tSoma\n \
            2.\tSubtração\n \
            3.\tMultiplicação\n \
            4.\tDivisão\n \
            ''')
        try:
            operation = int(input('Digite o número da operação: '))
            if operation == 1:
                numbers = input(
                    'Digite a soma, separando os números pelo sinal + (ex: 2+2) \n')
                numbers = re.sub('[^0-9]', '', numbers)
                numbers = [float(i) for i in list(numbers)]
                self.soma(numbers)
            elif operation == 2:
                numbers = input(
                    'Digite a subtração, separando os números pelo sinal - (ex: 4-2) \n')
                numbers = numbers.split('-')
                numbers = [float(re.sub('[^0-9]', '', i)) for i in numbers]
                self.sub(numbers)
            elif operation == 3:
                numbers = input(
                    'Digite a multiplicação, separando os números pelo sinal * (ex: 2*2) \n')
                numbers = numbers.split('*')
                numbers = [float(re.sub('[^0-9]', '', i)) for i in numbers]
                self.mult(numbers)
            elif operation == 4:
                numbers = input(
                    'Digite a divisão, separando os números pelo sinal / (ex: 40/20) \n')
                numbers = numbers.split('/')
                numbers = [float(re.sub('[^0-9]', '', i)) for i in numbers]
                self.div(numbers)
            else:
                print('\033[93mOperação inválida\033[0m')
        except (RuntimeError, ValueError) as e:
            print(f'\033[91mOperação inválida!\033[0m')
            raise e

    def soma(self, numbers_list):
        self.result = sum(numbers_list)

    def sub(self, numbers_list):
        self.result = numbers_list[0]
        for index in range(1, len(numbers_list)):
            self.result = self.result - numbers_list[index]

    def mult(self, numbers_list):
        self.result = numbers_list[0]
        for index in range(1, len(numbers_list)):
            self.result = self.result * numbers_list[index]

    def div(self, numbers_list):
        self.result = numbers_list[0]
        for index in range(1, len(numbers_list)):
            if (numbers_list[index] != 0):
                self.result = self.result / numbers_list[index]
            else:
                self.result = '\033[93mValor do denominador inválido!\033[0m'

    def __str__(self) -> str:
        return str(self.result)


if __name__ == "__main__":
    c = Calculator()
    print(c)
