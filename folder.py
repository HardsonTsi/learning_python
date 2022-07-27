import os

chemin = './'
dossier = os.path.join(chemin, 'dossier');
if not os.path.exists(dossier):
    print('Dossier introuvable')
else:
    print('Dossier existant');
    response = int(input('Voulez-vous supprimer le dossier ?: '))
    if response == 1:
            os.removedirs(dossier);
            print('Dossier supprimé')
