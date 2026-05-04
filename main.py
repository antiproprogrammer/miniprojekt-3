import turtle

# Funktion för att rita kvadrat
def rita_kvadrat(t, sida, färg):
    t.pencolor(färg)
    for _ in range(4):
        t.forward(sida)
        t.left(90)

# Funktion för att rita triangel
def rita_triangel(t, sida, färg):
    t.pencolor(färg)
    for _ in range(3):
        t.forward(sida)
        t.left(120)

# Funktion för att rita cirkel
def rita_cirkel(t, radie, färg):
    t.pencolor(färg)
    t.circle(radie)

# Funktion för att rita blomma 
def rita_blomma(t, antal_kronblad, storlek, färg):
    vinkel = 360 / antal_kronblad
    t.pencolor(färg)
    
    for _ in range(antal_kronblad):
        rita_kvadrat(t, storlek, färg)
        t.right(vinkel)

# Huvudmeny 
def main():
    t = turtle.Turtle()
    t.speed(5)          
    
    while True:
        print("\n--- TURTLE MÖNSTER ---")
        print("1. Rita kvadrat")
        print("2. Rita triangel")
        print("3. Rita cirkel")
        print("4. Rita blomma")
        print("5. Avsluta")
        val = input("Välj: ")
        
        if val == "1":
            sida = int(input("Ange sidlängd: "))
            färg = input("Ange färg (t.ex. red, blue, green): ")
            rita_kvadrat(t, sida, färg)
            
        elif val == "2":
            sida = int(input("Ange sidlängd: "))
            färg = input("Ange färg (t.ex. red, blue, green): ")
            rita_triangel(t, sida, färg)
            
        elif val == "3":
            radie = int(input("Ange radie: "))
            färg = input("Ange färg (t.ex. red, blue, green): ")
            rita_cirkel(t, radie, färg)
            
        elif val == "4":
            antal = int(input("Ange antal kronblad: "))
            storlek = int(input("Ange storlek på kronbladen: "))
            färg = input("Ange färg (t.ex. red, blue, green): ")
            rita_blomma(t, antal, storlek, färg)
            
        elif val == "5":
            print("Hej då!")
            break
        else:
            print("Ogiltigt val, försök igen.")
    
    turtle.done()   # Håller fönstret öppet

if __name__ == "__main__":
    main()