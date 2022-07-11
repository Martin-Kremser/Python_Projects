import random as rnd

colors = "YORPGB"

n = rnd.randint(0, 5)
random_letter = colors[n]

secret = ""
for i in range(4):
    n = rnd.randrange(6)
    secret = secret + colors[n]

print(secret)
history = []

r = 1
while r <= 12:
    print(f"Round {r}")

    guess_invalid = True
    while guess_invalid:
        guess: str = input("Your guess: ").upper()
        if len(guess) == 4:
            guess_invalid = False
            for i in guess:
                if i not in colors:
                    guess_invalid = True
        elif guess == "BOARD":
            guess_is_invalid = False
            print()
            for row in history:
                for color in row[0]:
                    print(f"{color}", end="")
                print(f" | {row[1]} {row[2]}")
        else:
            var = guess_invalid == True
            print("Please write 4-letter words using the characters Y, O, R, P, G, B!")

    hits = 0
    for i in range(4):
        if guess[i] == secret[i]:
            hits = hits + 1

    close = 0
    for i in colors:
        close = close + min(secret.count(i), guess.count(i))
    close = close - hits

    print(f"HITS: {hits} CLOSE: {close}")

    if hits == 4:
        break
    history.append((guess, hits, close))
    r = r + 1

if hits == 4:
    print(f"Congratulations, you broke the code! The secret was {secret}.")
else:
    print(f"You have run out of attempts, you lost the game. The secret was {secret}.")
