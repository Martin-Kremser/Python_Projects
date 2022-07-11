while True:
    try:
        size_string: str = input("Give me your size: ")
        size: float = float(size_string)
        break
    except ValueError:
        print("This dosen´t looks like a Number. Try again!")
if size <= 10:
    print("Oh, this is small.")
elif size <= 80:
    print("This size is medium.")
else:
    print("Huh, this is large.")
