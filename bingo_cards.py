import random
from itertools import combinations

def generate_bingo_cards(min, max, num_cards):
    # Generate all possible combinations of four unique numbers from 1 to 50
    all_combinations = list(combinations(range(min, max), 4))
    random.shuffle(all_combinations)

    cards = []

    for _ in range(num_cards):
        card = [all_combinations.pop()]

        # Loop to ensure each set in the group is unique across all groups
        while len(card) < 3:
            next_combination = None

            for combination in all_combinations:
                if all(number not in row for row in card for number in combination):
                    next_combination = combination
                    break

            if next_combination:
                card.append(next_combination)
                all_combinations.remove(next_combination)
            else:
                # Handle the case when there are not enough unique combinations left
                break

        # Add the group to the list of groups
        cards.append(card)

    return cards

def write_bingo_cards_to_file(cards, filename="bingo_cards.tex"):
    with open(filename, 'w') as file:
        file.write("\\documentclass[letterpaper, 36pt]{article}\n")
        file.write("\\usepackage[margin=0.25in]{geometry}\n")
        file.write("\\usepackage{array}\n")
        file.write("\\usepackage{tikz}\n")
        file.write("\\pagestyle{empty}\n")
        file.write("\\begin{document}\n")

        for i, card in enumerate(cards, start=1):
            if (i - 1) % 6 == 0:
                if i != 1:
                    file.write("\\clearpage\n")  # Start a new page for every group of two cards
                file.write("\\begin{center}\n")

            if (i - 1) % 2 == 0:
                # file.write("\\vspace{0.5in}\n")
                file.write("\\textbf{{\\LARGE Lô Tô}}\\\\\n")
                file.write("\\vspace{0.20in}\n")
            
            file.write("\\begin{tikzpicture}[scale=0.75, font=\\Huge]\n")  # Adjust the scale and font size
            for j, row in enumerate(card):
                for k, number in enumerate(row):
                    file.write("\\draw ({},{}) rectangle ++(3,-3) node[pos=.5] {{\\textbf{{{}}}}};\n".format(k*3, -j*3, number))
                if j < len(card) - 1:  # Check if it's not the last row in the card
                    file.write("\\vspace{1in}\n")  # Add vertical space between rows in the card
                elif i == len(cards) and j == len(card) - 1:
                    # Check if it's the last row of the last card
                    file.write("\\vspace{0.5in}\n")  # Add vertical space after the last row
            file.write("\\end{tikzpicture}\n")
            file.write("\\hspace{0.5in}\n")
            file.write("\\vspace{0.20in}\n")  # Add more vertical space between the previous row and the heading of the next row


        file.write("\\end{center}\n")
        file.write("\\end{document}\n")

    print("Bingo cards written to 'bingo_cards.tex'.")



















if __name__ == "__main__":
    min = int(input("Enter min number: "))
    max = int(input("Enter max number: "))
    num_cards = int(input("Enter number of cards: "))
    bingo_cards = generate_bingo_cards(min, max, num_cards)
    write_bingo_cards_to_file(bingo_cards)
