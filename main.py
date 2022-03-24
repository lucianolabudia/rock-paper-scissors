import random


def main():
    rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

    paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

    scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

    game_images = [rock, paper, scissors]

    user_choice = int(input('¿Qué eliges? Selecciona 0 para Piedra, 1 para Papel o 2 para Tijeras.\n'))
    
    if user_choice >= 3 or user_choice < 0:
        print('Has escrito un número inválido, Perdiste')
    else:
        print(game_images[user_choice])

        computer_choice = random.randint(0, 2)
        print('Seleccion de la computadora:')
        print(game_images[computer_choice])

        if user_choice >= 3 or user_choice < 0:
            print('Has escrito un número inválido, Perdiste')
        elif user_choice == 0 and computer_choice == 2:
            print('Ganaste!')
        elif computer_choice == 0 and user_choice == 2:
            print('Perdiste')
        elif computer_choice > user_choice:
            print('Perdiste')
        elif computer_choice < user_choice:
            print('Ganaste!')
        elif computer_choice == user_choice:
            print('Es un Empate')



if __name__ == '__main__':
    main()