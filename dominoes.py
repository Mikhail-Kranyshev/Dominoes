from random import shuffle


def maximum_element(one, two):
    max_element = max(one[0], two[0])
    for i in range(1, len(one)):
        tmp = max(one[i], two[i])
        if max_element < tmp:
            max_element = tmp
    if max_element in one:
        return one.pop(one.index(max_element)), "computer"
    return two.pop(two.index(max_element)), "player"


def prepare_game():
    shuffle(full_set := [[i, j] for i in range(7) for j in range(i, 7)])
    global stock, player, computer, domino_snake, status
    stock = full_set[:14]
    player = full_set[14:21]
    computer = full_set[21:]
    domino_snake = []
    maximum, status = maximum_element(player, computer)
    domino_snake.append(maximum)


def game():
    print('=' * 70)
    print(f"Stock size: {len(stock)}")
    print(f"Computer pieces: {len(computer)}")
    print(f"\n{domino_snake[0]}\n")
    print("Your pieces:")
    for i in range(len(player)):
        print(f"{i + 1}:{player[i]}")
    if status == "computer":
        print("\nStatus: Computer is about to make a move. Press Enter to continue...")
    else:
        print("\nStatus: It's your turn to make a move. Enter your command.")


stock = []
player = []
computer = []
domino_snake = []
status = ""


def main():
    prepare_game()
    game()


if __name__ == "__main__":
    main()
