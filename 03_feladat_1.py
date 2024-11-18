"""Készíts egy programot, amely a felhasználó által megadott mondatról a mondatvégi jel alapján eldönti milyen fajtájú! (kijelentő, kérdő, felkiáltó / felszólító / óhatjtó)
"""

megadott_mondat = input("Kérlek adj meg egy mondatot: ")

if megadott_mondat[-1] == '.':
    print('Ez a mondat kijelentő')
elif megadott_mondat[-1] == '?':
    print('Ez a mondat kérdő')
elif megadott_mondat[-1] == '!':
    print('Ez a mondat felkiáltó/óhajtó/felszólító')
else:    
    print('Nem adtál meg mondatvégi írásjelet.')    