liste = []

while True:
    menu = int(input("""
choisissez parmi les 5 options suivantes :
1: Ajouter un élément a la liste
2: Retirer un élément de la liste
3: Afficher la liste
4: Vider la liste 
5: Quitter
👉  Votre choix : """))
    
    if menu == 1:
        #creation de l'element
        element_de_liste = input("Entrez le nom d'un élément a ajouter a la liste de courses : ")
        print(f"L'élément {element_de_liste} a bien été ajouté a la liste")
        
        #ajout de l'element dans la liste
        liste.append(element_de_liste)
               
        print('-'*50)
        
    elif menu == 3:
        
        if not element_de_liste in liste :
             print(f"Votre liste ne contient aucun contenue")
        else:
            print("Voici le contenue de votre liste :")
        #creation de l'indice de l'element
        for i in liste:
            print(f"{liste.index(i) + 1}.  {i}")     
        print('-'*50)
    #retirer un element de la liste
    elif menu == 2:
        
        element_de_liste = input("Veillez entrer le nom de l'élément a enlever : ")
        #verification de l'element dans la liste
        if element_de_liste in liste:
            liste.remove(element_de_liste)
            print(f"L'élément {element_de_liste} a bien été retirer a la liste")
        
            
            #sinon retirer un element inexistant ou deja suprimer
        else:
            print(f"L'élément {element_de_liste} n'est pas dans la liste")
        
        print('-'*50)
    elif menu == 4:
        liste.clear()
        print(f"La liste a été vidé de son contenue")
        
        print('-'*50)
    elif menu == 5:
        print("A bientot ! ")
        break
    
#cas ou menu est different d'un int

    
        
    
   
   
       
    
        
        
                 
            
            
            
        
        
        
       
            
        
        
        
     
    
           
