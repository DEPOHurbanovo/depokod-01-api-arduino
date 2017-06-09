a = raw_input("Zadaj prve cislo: ")
b = raw_input("Zadaj druhe cislo: ")

operation = raw_input("Zadaj operaciu [+/-]")

if operation == "+":
	c = int(a) + int(b)
elif operation == "-":
	c = int(a) - int(b)

print("Vysledok: " + str(bin(c)) if raw_input("Chces vysledok binarne? [y/n] ") == "y" else str(c))

def starts_with_two(number):
	return str(i).startswith("2")

print("Vypisujem cisla 2* od 0 do 3000")

for i in range(0, 3000):
	if starts_with_two(i):
		print(i)
