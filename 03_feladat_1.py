"""Készíts egy programot, amely a felhasználó által megadott mondatról a mondatvégi jel alapján eldönti milyen fajtájú! (kijelentő, kérdő, felkiáltó / felszólító / óhatjtó)
"""

megadott_mondat = input("Kérlek adj meg egy mondatot: ")

if megadott_mondat.endswith('...'):
    print('Ez a mondat ...')
elif megadott_mondat.endswith('?'):
    print('Ez a mondat kérdő')
elif megadott_mondat.endswith('!'):
    print('Ez a mondat felkiáltó/óhajtó/felszólító')
elif megadott_mondat.endswith('.'):
    print('Ez a mondat kijelentő')
else:    
    print('Nem adtál meg mondatvégi írásjelet.')    