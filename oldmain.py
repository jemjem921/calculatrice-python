def menu():
    print("=== Calculatrice ===")
    print("1. Addition")
    print("2. Soustraction")
    print("3. Multiplication")
    print("4. Division")
    choix = input("Choix : ")
    a = float(input("Nombre 1 : "))
    b = float(input("Nombre 2 : "))

    if choix == "1":
        print("Résultat :", a + b)
    elif choix == "2":
        print("Résultat :", a - b)
    elif choix == "3":
        print("Résultat :", a * b)
    elif choix == "4":
        if b == 0:
            print("Erreur : division par zéro")
        else:
            print("Résultat :", a / b)
            
            def division(a, b):
    if b == 0:
        raise ValueError("Division par zéro interdite")
    return a / b


if __name__ == "__main__":
    menu()

def addition(a, b):
    return a + b

def soustraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Erreur : division par zéro"
    return a / b
