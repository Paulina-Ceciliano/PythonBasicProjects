nombre = input('Nombre: ')
print('Género: ')
genero = input('Mujer / Hombre / Otro: ').lower()
if genero == 'mujer':

    print('Mucho gusto en conocerla, mylady', nombre,'!')
    print('Razas')
    print('Elfa Blanca: Seres apegados a la madre naturaleza, respetan las leyes naturales y cuidan de ella. Utilizan magia blanca, son muy excelentes creando pósimas, hechizos y usando el arco')
    print('Elfa oscura: Seres que destruyen todo a su paso, peores enemigos de toda raza que no sean ellos mismos, crean magia negra destructiva y horrible, huelen muy feo')
    print('Valkiria: Nórdicas hijas del dios Odín, excelentes guerreras con hacha y espada')
    print('Orca: Aliados de los elfos oscuros, seres despreciables pero buenos en batalla, arrazan ciudades')
    print('Humana: Un ser voluble, buenos con la espada y el arco, la habilidad la escoges tu')
    print('Elfa blanca/ Elfa oscura/ Valkiria/ Orca/ Humana')
    raza = input('Raza: ').lower()

    if raza == 'elfa blanca':
        print('Eres un ser especial')

        print('Es momento de empezar la aventura!')
        print('Estamos en el bosque blanco, en casa... Todo se siente en paz. Estas a punto de compartir la cena con tus seres amados')
        print('Tu madre te envía al bosque por una cesta de hongos que olvidó, sólo falta eso y la cena estará lista')
        print('Vas corriendo al bosque en busca de la cesta y la ves a lo lejos, y verla te alegra mucho')
        print('Pero... Por qué la tierra tiembla de esta forma?')
        print('La gran madre no dijo nada sobre algún temblor o erupción cercano...')
        print('Volteas a ver la aldea y notas que ha caido una bola gigante de fuego!!!')
        print('Esto no es de la naturaleza! Son el ejercito de Mout!! Un ejercito que destruye todo a su paso, no saben cuidar los recursos, son nómadas que invaden tierras cada que terminan con una ciudad, causan sequías y hambruna por doquier')
        print('Están atacando el bosque blanco! El lugar con las tierras más fructíferas. Los bosques blancos son custodiados por los elfos blancos, ellos cuidan y se comunican con la naturaleza')
        print('Este ejercitó atacó justo en la fiesta del pueblo')
        print('Corres a tu hogar, hay muchas Casas destruidas, gritos y familias destruidas... Tu casa...')
        print('Tu casa fue afortunada, pero tu padre ha salido a defender a la aldea')
        print('Tu madre y hermanos corren a refugiarse')
        print('Te preocupa tu padre, ya es una persona anciana, el corazón valiente lo llama a defender lo suyo')
        print('Tu hermano mayor va tras él pero tu tienes que cuidar a la familia!!')
        print('Fin por ahora... tengo que ir a domrir')

    elif raza == 'elfa oscura':
        print('Otro mal para el mundo...')
    elif raza == 'valkiria':
        print('Una guerrera respetable')
    elif raza == 'orca':
        print('Un esclava más de la maldad')
    elif raza == 'humana':
        print('Piensa dos veces antes de actuar, humana...')

        print('Qué habilidad quieres desarrollar? Espada o Arco?')
        habilidad = input('Espada / Arco: ').lower()
        
        if habilidad == 'espada':
            print('La habilidad que escogiste es: ',habilidad)
        elif habilidad == 'arco':
           print('La habilidad que escogiste es: ',habilidad)
        else:
            print('Piénsalo y regresa más tarde')
            quit()

    else:
        print('Esa no era una opción, has perdido antes de siquiera empezar! ')
        quit()

elif genero == 'man':
    print('Nice to meet you gentleman!')

elif genero == 'otro':
    print("Nice to meet you!")
else: 
    print('Esa no era una opción, pierdes...')
