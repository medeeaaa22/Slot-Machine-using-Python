import random

# Create a constant value, something is not gonna change
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    'A': 2,
    'B': 4,
    'C': 6,
    'D': 8
}

symbol_value = {
    'A': 5,
    'B': 4,
    'C': 3,
    'D': 2
}


def check_winnings(columns, lines, bet, values):
    winnings = 0
    winnings_lines = []
    for line in range(lines):
        # the symbol that we want to check is the whatever symbol is in the first column of the current row
        symbol = columns[0][line]
        for column in columns:  # loop for every column to check the symbol
            symbol_to_check = column[line]  # column at the current row
            if symbol != symbol_to_check:
                break
        else:
            # the bet on each line, not the total bet
            winnings += values[symbol] * bet
            winnings_lines.append(line + 1)

    return winnings, winnings_lines


def get_solt_machine_spin(rows, cols, symbols):
    # Randomly pic the number of rows inside of each column

    all_symbols = []
    for symbol, symbol_count in symbols.items():  # give you both the key and the value for dict
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []  # interior list that represent the rows
    # Each of this nested lists represent the values in our call
    # For every column, we need to generate a certain number of symbols
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]  # copy of all symbols
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)  # add value to column

        columns.append(column)
# Once we pick a value, we need to remove it from this list so we cant choose that value again (if its only 2A, we wont be able to select 3A)
    return columns


def print_slot_machine(columns):  # transposing, matrix
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):  # gives the index
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")

        print()


def deposit():
    while True:  # Continually ask the user to give a deposit amount, a value amount
        amount = input("What would you like to deposit? $")
        # Make sure that the amount is a number
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")

    return amount


def get_numer_of_lines():
    while True:
        lines = input(
            "Enter the number of lines to bet on (1-" + str(MAX_LINES) + "). ")
        # Make sure that the amount is a number
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")

    return lines


def get_bet():
    while True:
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number.")

    return amount


def spin(balance):
    lines = get_numer_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(
                f"You dont have enough to bet that amount, your current ballance is: ${balance}.")
        else:
            break

    print(
        f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}.")

    slots = get_solt_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winnings_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f'You won ${winnings}.')
    # *-splat / unpacked operator, its gonna pass every single line of winnings_lines list to this print function.
    print(f'You won on lines:', *winnings_lines)
    return winnings - total_bet


def main():
    balance = deposit()
    while True:
        print(f'Current balance is ${balance}.')
        answer = input('Press enter to play (q to quit).')
        if answer == "q":
            break
        balance += spin(balance)

    print(f"You lef with ${balance}.")


main()
