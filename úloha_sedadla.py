import tkinter # import plátna
canvas = tkinter.Canvas(width=600, height=300, bg='white') # vytvorenie plána (širka, výška, farba pozadia) 
canvas.pack() # nahranie plátna

pocetradov = 10 # premenná pocetradov s hodnotou 10
VEL = 40 # premenná VEL s hodnotou 40
busx, busy = 50, 50 # premenná busx a busy s hodnotou 50 a 50

def zafarbi (sedadlo, farba): # funkcia ktorá zafarbí sedadlá na červeno keď sa na ne klikne
    canvas.itemconfig('sedadlo_' + str(sedadlo), fill='red')
                    
def kresli(x, y, pocet): # funkcia ktorá urobí 40 sedadiel vedľa seba a do stĺpcov
    cislo = 0
    for i in range(pocet):
        for j in range(4):
            cislo += 1
            canvas.create_rectangle(x+i*VEL, y+j*VEL,
                                    x+(i+1)*VEL-10, y+(j+1)*VEL-10,
                                    tags='sedadlo_'+str(cislo), fill='limegreen')
            canvas.create_text(x+i*VEL+VEL/2-5, y+j*VEL+VEL/2-5, text=cislo)

def klik(event): 
    if (busx < event.x < busx + VEL * pocetradov and
        busy < event.y < busy + VEL * 4):
        ix = (event.x - busx) // VEL
        iy = (event.y - busy) // VEL
        sedadlo = ix * 4 + iy + 1
        zafarbi(sedadlo, 'red')
        print(sedadlo)

canvas.create_text(120,230,fill="black",font="Arial",text="Počet voľných miest: ") # vytvori to text "Počet voľných miest: "
canvas.create_text(135,250,fill="black",font="Arial",text="Počet obsadených miest: ") #  vytvori to text "Počet obsadených miest: "
canvas.create_text(152,270,fill="black",font="Arial",text="Počet voľných miest pri uličke: ") #  vytvori to text "Počet voľných miest pri uličke: "

kresli(busx, busy, pocetradov) # vykreslí to sedadlá
canvas.bind('<Button-1>', klik) # bind na ľavé tlačitko myši
