from user import register_user
from authority import Authority, CertificateRepository
from communication import Communication

def main_menu():
    print("Bonjour ô maître Rémi ! Que souhaitez-vous faire aujourd'hui ?")
    print("->1<- Chiffrer / déchiffrer des messages.")
    print("->2<- Créer un couple de clés publique / privée.")
    print("->3<- Signer / générer un certificat.")
    print("->4<- Vérifier un certificat.")
    print("->5<- Enregistrer un document dans le coffre-fort.")
    print("->6<- Envoyer un message (asynchrone).")
    print("->7<- Demander une preuve de connaissance.")
    print("->0<- I WANT IT ALL !! I WANT IT NOW !! SecCom from scratch?")

    choice = input("Veuillez choisir une option: ")
    if choice == '1':
        
        # Chiffrer / déchiffrer des messages
        pass
    elif choice == '2':
        # Créer un couple de clés publique / privée
        email = input("Entrez votre email: ")
        user_data = register_user(email)
        print("Clés générées:", user_data)
    elif choice == '3':

        # Signer / générer un certificat
        email = input("Entrez votre email: ")
        user_data = register_user(email)
        authority = Authority()
        certificate, signature = authority.sign_certificate(user_data)
        print("Certificat signé:", certificate, signature)
    elif choice == '4':

        # Vérifier un certificat
        email = input("Entrez l'email: ")
        certificate = input("Entrez le certificat: ")
        signature = input("Entrez la signature: ")
        authority = Authority()
        is_valid = authority.verify_certificate(email, certificate, signature)
        print("Certificat valide:", is_valid)
    elif choice == '5':

        # Enregistrer un document dans le coffre-fort
        pass
    elif choice == '6':

        # Envoyer un message (asynchrone)
        communication = Communication()
        message = input("Entrez le message: ")
        encrypted_message = communication.send_message(message)
        print("Message chiffré:", encrypted_message)
    elif choice == '7':

        # Demander une preuve de connaissance
        pass
    elif choice == '0':

        # I WANT IT ALL !! I WANT IT NOW !! SecCom from scratch?
        pass

if __name__ == "__main__":
    main_menu()