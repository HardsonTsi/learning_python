import os

chemin = './'
dossier = os.path.join(chemin, 'dossier');
if not os.path.exists(dossier):
    os.makedirs(dossier)
    print('Dossier créé')
else:
    print('Dossier existant');
    response = int(input('Voulez-vous remplacer le dossier existant ?'))
    if response == 1:
            os.makedirs(dossier, exist_ok=True)
            print('Dossier remplacé')
