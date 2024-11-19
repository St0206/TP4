def est_bissextile(annee):
    return (annee % 4== 0 and annee % 100!=0) or (annee % 400 == 0)

def verification_date(date):
    if len(date)!=8 or not date.isdigit():
        print("Erreur la date doit etre une chaine de 8 choiffres au format jjmmaaaa")
        return False
    jour=int(date[:2])
    mois=int(date[2:4])
    annee=int(date[4:])

    if mois <1 or mois > 12:
        print(f"Erreur le mois {mois} est invalide")
        return False

    nbr_jour=[31,29 if  est_bissextile(annee) else 28,31,30,31,30,31,31,30,31,30,31]

    if jour <1 or jour > nbr_jour[mois-1]:
        print(f"Erreur le jour {jour} est invalide")
        return False


    print (f"La date {date} est valide ")
    return True

test_date=["3102199", "31041000", "32052020", "30032021", "29022022"]
for date in test_date:
    print (f"Verifaction de la date: {date}")
    verification_date(date)
    print("-"*40)











