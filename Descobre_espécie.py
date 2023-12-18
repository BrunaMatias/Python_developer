print("informe as características da espécie buscada")
print("Vertebrado ou Invertebrado:")
a = input() 

if a == 'vertebrado': 
    
    print("ave ou mamifero:")
    b = input() 
    
    if b == 'ave':
        print("carnivoro ou onivoro:")
        c = input() 
        
        if c == 'carnivoro':
            print("Espécie identificada: aguia")
        elif c == 'onivoro':
            print("Espécie identificada: pomba")
        else: print("Nenhuma espécie identificada")
        
    elif b == 'mamifero':
        print("onivoro ou herbivoro:")
        c = input() 
        
        if c == 'onivoro':
            print("Espécie identificada: homem")
        elif c == 'herbivoro':
            print("Espécie identificada: vaca")
        else: print("Nenhuma espécie identificada")
        
    else: print("Nenhuma espécie identificada")

elif a == 'invertebrado':
    print("inseto ou anelideo:")
    b = input() 
    
    if b == 'inseto':
        print("hematofogo ou herbivoro:")
        c = input() 
        
        if c == 'hematofago':
            print("Espécie identificada: pulga")
        elif c == 'herbivoro':
            print("Espécie identificada: lagarta")
        else: print("Nenhuma espécie identificada")
    
    elif b == 'anelideo':
        print("hematofogo ou onivoro:")
        c = input() 
        
        if c == 'hematofago':
            print("Espécie identificada: sanguessuga")
        elif c == 'onivoro':
            print("Espécie identificada: minhoca")
        else: print("Nenhuma espécie identificada")
        
    else: print("Nenhuma espécie identificada")
        
else: print("Nenhuma espécie identificada")
    
    
    
    
