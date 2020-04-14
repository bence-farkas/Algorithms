"""
This script purpose is to introduce the usage of python loops. Loops are
good because when we want to repeat python commands we do not need to
type again those line by line, instead we just create a loop for that.
Made by: Bence Farkas
Vers: Version 0.1
Date: 08/04/2020
"""

############################################################### WHILE CIKLUSOK HASZNALATA ###############################################################
# Feltetelezem tudod mar az alap python parancsokat, szoval most akkor hasznaljuk is oket!
"""
1. A "Hello World!" string kiiratasa haromszor az sdtout-ra:
Ahelyett, hogy haromszor leirnank a kovetkezo parancsot,
print("Hello World!")
print("Hello World!")
print("Hello World!")
tudunk am jobbat is! Megpedig hasznalhatjuk erre a while ciklust. A while ciklus a kovetkezokbol epul fel:

while CIKLUSFELTETEL:
	VALAMI_PARANCS(OK)

Vetitsuk ra ezt a mi peldankra. Tehat szeretnenk haromszor ismetelni a print("Hello World!") parancsot. A 
CIKLUSFELTETEL egy IGAZ/HAMIS ertekkel biro parancs, amit a while ciklus figyel es addig ismetli az alatta
levo blokkban a kodot, amig teljesul a feltetel amit kitalaltunk. Na, de lassuk a gyakorlatban!
"""

szamlalo = 0 # hozzunk letre egy szamlalot, ami szamolja, hogy hany alkalommal irtuk ki a Hello World!-ot.
while szamlalo < 3:
	# Hoppa! Egy ciklus feltetel! Vizsgaljuk a szamlalo erteket. Mindaddig ismeteljuk a parancsokat a
	# while ciklus alatti blokkban, amig a feltetel teljesul. Jelen esetben, ha eleri a 3-at, kilepunk a ciklusbol,
	# folytatodik tovabb a program, ha van meg parancs a tovabbiakban.
	print("Hello World!") # "Hello World!"" String kiiratasa konzolra
	szamlalo += 1 # A szamlalot noveltuk eggyel, hiszem az elobb kiirattuk a "Hello World!"-ot.
# Lathato, hogy mindaddig a ciklushoz tartozik valami, amig beljebb helyezkedik el a sorban alatta (indentalva van).


# De ezt visszafele is vizsgalhatjuk, a lenyeg, hogy amig teljesul a ciklusfeltetel, addig ismeteljuk az alatta levo blokkban a parancsokat:
szamlalo = 3 # Most 3-rol indulunk es csokkenteni fugjuk a valtozot.
while szamlalo > 0: # Ez is egy ciklusfeltetel, jelen esetben nezzuk, hogy a szamlalo nagyobb-e mint 0.
	print("Hello World!")
	szamlalo -= 1 # A szamlalot csokkentettuk eggyel, hiszem az elobb kiirattuk a "Hello World!"-ot.


# Legyen a kovetkezo pelda egy kivonas sorozat. Az adott szambol addig vonjunk ki 2-ot, amig el nem erjuk a 20-at. Ekkor a ciklusfeltetelunk a kovetkezo modon alakul:
# kivonando_szam > 20. A ciklusban pedig a kivonast ismetelgetjuk mindaddig, amig teljesul a feltetel.
kivonando_szam = 40 # kezdoertek amibol tortenik majd a ciklusban a kivonas sorozat.
while kivonando_szam > 20: # ciklusfeltetelunkben most azt adtuk meg, hogy a kivonando_szam nagyobb-e mint 20? Azaz, ez egy igaz/hamis kifejezes, amelyet a ciklus vizsgal
# a futasa soran.
	kivonando_szam = kivonando_szam - 2 # a kivonando szam uj erteke: a kivonando szam regi ertekebol kivonunk kettot.


# Most nezzunk meg egy masik peldat. Generaljunk random szamokat 1-5-ig. Itt legyen az a ciklusfeltetel, hogyha a random szamunk 5, akkor lepjen ki a ciklusbol.
import random # importaljuk ehhez eloszor a random python modult/fuggvenykonyvtarat
while True: # Azta... ilyet meg nem lattunk. A "True" kerult most a ciklusfeltetelbe, azaz mindig igaz lesz a ciklusfeltetel, vegtelensegig fogja porgetni a ciklust. Na,
# de akkor megis hogy a fenebe fogunk kilepni belole?! Ekkor azt tudjuk csinalni, hogy a cikluson belul vizsgaljuk a felteteleket az "if-elif-else" vezerlesi szerkezettel,
# es ha nem teljesul valamelyik feltetel, akkor a "break" paranccsal ki tudunk lepni a ciklusbol.
	generalt_szam = random.randint(1,6) # Generalunk egy random egesz szamot 1-tol 5-ig
	if generalt_szam == 5: # Vizsgaljuk a dupla egyenlovel, hogyha 5 a generalt szamunk, akkor..
		break # lepjunk ki a ciklusbol!
	# es ha nem 5, akkor generaljunk megint egy szamot, ugorjunk vissza a generalt_szam = random.randint(1,6) sorra.


# A kovetkezo peldaban egy lista elemeit szeretnenk kiiratni. Ekkor nezhetjuk peldaul ciklusfeltetelnek azt, hogy egy szamlalo elerte-e a lista veget:
lista = ["Trabant", "Opel", "Bugatti", "Ferrari", "Peugeot", "Mercedes", "Lancia"]
elem_index = 0 # Pythonban 0-tol kezdodik az indexeles, vannak egyes prognyelvek ahol mas, de azt inkabb felejtsuk el :-)))
lista_merete = len(lista) # lekerjuk a lista elemszamat

while elem_index < lista_merete: # A ciklusfeltetelunk most az, hogy az elem_index erteket vizsgaljuk minden egyes ismetlesben (ciklus iteracioban).
	print(lista[elem_index]) # Maga az lista elem kiiratasa a konzolra (stdout-ra)
	elem_index += 1 # index ertekenek novelese 1-gyel.


# Nezzunk meg most egy olyan peldat, amiben random szamokat pakolunk be a listankba minden egyes iteracioban csak egyszer. Legyen az iteraciok szama 10.
# Ket fele modon irhatjuk meg a ciklusfeltetelunket. Az egyik pl lehetne az, hogy keszitunk egy valtozot, amit minden egyes iteracioban novelunk egyel, es vizsgaljuk,
# eri el a 10-et. A masik, hogy maga a lista meretet vizsgaljuk, es ha eleri a 10-et, kilepunk. Vizsgaljuk most ezzel a modszerrel.

# Mivel a kettovel elozo helyen importaltuk a random modult, ezert itt mar nem kell.
lista = [] # hozzunk letre egy ures listat amibe pakoljuk a random szamainkat.
while len(lista) <= 10: # ciklusfeltetelunk most azt vizsgalja, hogy a lista elerte-e a 10-es meretet.
	lista.append(random.randint(0,100)) # Pakoljunk a listankba 0-100 kozotti egesz szamokat.






############################################################### FOR CIKLUSOK HASZNALATA ###############################################################
"""
A masik modszer a parancsaink ismetlesere a for ciklus. for ciklus eseten a deklaracio a kovetkezo: 

for CIKLUSVALTOZO in VEGIGJARANDO_OBJEKTUM:
	VALAMI_PARANCS(OK)

Lathatjuk, hogy itt a ciklusfeltetelunk rejtve marad, mig while ciklus eseteben nem kell ciklusvaltozot definialnunk. 
A ciklusfeltetelt belul ellenorzi a program, megpedig azt, hogy a vegigjarando objektumunk vegere ertunk-e. 
Termeszetesen elobb is kilephetunk a ciklusbol, ilyenkor ugyanugy a if-elif-else es "break" parancsot kell hasznalnunk.
A VEGIGJARANDO_OBJEKTUM-ok kepesek a for loop-ban visszaadni mindegy egyes iteracioban az adott elemuket. Tobb fele ilyen objektum is van, ebbol az egyik amit ismerunk mar
az a lista.
"""

# Elso peldakent nezzunk meg egy lista elemeinek a kiiratasat. Itt ami parancsot ismeteljuk az a lista elemenek kiiratasa. A lekerdezest belul megcsinalja a program, valamint
# ellenorzi a ciklusfeltetelt.

lista = ["fofekhenger", "lengescsillapito", "ekszij", "fenyszoro", "indexkapcsolo"] # hozzuk letre listankat, most string-ekkel toltottuk fel.
# szeretnenk kiiratni az elemeit, tehat addig ismetlunk egy kiiratast amig a lista tart.
for lista_elem in lista: # Itt a CIKLUSVALTOZO-nk a lista_elem amibe minden egyes iteracioban belekerul a kovetkezo elem a listabol. Ez automatikusan tortenik, es kozben
# ellenorzi, hogy van-e meg eleme a listanak. Ha nincs, kilepunk a ciklusbol.
	print(lista_elem) # Adott elem kiiratasa.

# Tehat osszefoglalva, annyiszor ismetlodott egy parancs a for ciklus blokkjaban, ahany elem volt a listankban.


# Ahhoz, hogy megkapjuk az elemnek a poziciojat (index) a listaban, az "enumerate" parancsot kell alkalmazzuk. Az enumerate(VEGIGJARANDO_OBJEKTUM) parancs visszaadja
# a lista elemet a poziciojaval egyutt. Ez a mi peldankban a kovetkezo:
for index_ertek, lista_elem in enumerate(lista): # Az enumerate(VEGIGJARANDO_OBJEKTUM) vissza adja az adott elemnek a pozicio erteket, es a lista adott elemet. Fontos, hogy
# az elso helyen mindig az index szerepel, a masodik helyen a lista eleme.
	print("Index: ", index_ertek, "Elem: ", lista_elem) # Egybevont kiiratas. Addig ismeteljuk ezt a parancsot, amig van a listaban elem.


# Lista elemszamot masra is hasznalhatunk, nem feltetlenul kell vele kozvetlenul dolgoznunk.
# Felhasznalhatjuk arra is, hogy annyiszor ismeteljunk pl egesz szam generalast ahany elem van a listankban. Nezzunk most egy ilyen peldat:

# listankat fent mar definialtuk, valamint importoltuk mar a random modult, tehat ezeket most nem kell ujra.

# Menjunk vegig a lista-n, de most nem kell torodnunk a CIKLUSVALTOZO-val. Belepakolodnak az elemek most is ugyanugy, viszont mi most nem hasznaljuk fel.
for lista_elem in lista:
	print(random.randint(0,500)) # 0-500 tartomanyban egesz szamot generalunk es kiiratjuk a konzolra.

###################################################################################################################################################
# Egy kis erdekesseg:
# Sokszor feleslegesen is dolgoztatjuk a szamitogepet, tobb energiat fogyaszt, gyorsabban is tud amortizalodni, meg ha ez nem is annyira szembetuno. Manapsag mar egyre
# fontosabb a programozasban a kornyezettudatossag.
# Pl, az elozo peldaban is feleslegesen olvasattuk ki a lista-bol a lista elemet es taroltuk a lista_elem-ben. Ahhoz, hogy ezt elkeruljuk, segitsegunkre van az ugynevezett
# underscore valtozo. Ha ezt hasznaljuk, akkor megadjuk a programnak, hogy ezzel a valtozoval nem torodunk, ne taroljon benne elemet, ezzel is tehermentesitve a memoriat.
# Nezzuk meg ezt az elozo peldan:
for _ in lista: # _ (underscore) valtozo hasznalata. A listan ugyanugy vegigmegyunk, de nem taroljuk elemeit.
	print(random.randint(0,500)) # 0-500 tartomanyban egesz szamot generalunk es kiiratjuk a konzolra.
###################################################################################################################################################







