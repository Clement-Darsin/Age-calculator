def get_current_year ():
    import datetime
    date = datetime.datetime.now()
    return date.year

def your_age ():
    date_minimum = minimum()
    date_maximum = maximum()
    print("quel est ton annee de naissance?" + " (" + date_minimum+" " + date_maximum +")" )
    return input()

def your_birthday(ref, naiss):
    naissance = int(naiss)
    age = ref-naissance
    return age

def minimum ():
    date = str(get_current_year()-110)
    return date
def maximum():
    date_max = str(get_current_year())
    return date_max

annee_de_reference = get_current_year()
annee_de_naissance = your_age()
age = your_birthday(annee_de_reference, annee_de_naissance)

print("votre âge est "+ str(age) +" ans")



