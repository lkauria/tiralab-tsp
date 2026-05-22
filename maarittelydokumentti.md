# Määrittelydokumentti (luonnos)

Jatkan periodeissa 1 ja 2 (vuosi 2025) kesken jäänyttä työtä.

Opinto-ohjelmani on tietojenkäsittelytieteen kandiohjelma.

## Ohjelmointikieli

Kurssilla koodattava ohjelmointikieli on python. Pystyn vertaisarvioimaan myös javascriptilla/typescriptilla ja javalla koodattuja projeketja.

## Algoritmi

Tulen kurssin projektissa toteuttamaan kauppamatkustajan ongelman Christofidesin aproksimaatioalgoritmilla ja visualisoimaan algoritmin toteutuksen valmiilla visualisointikirjastolla, matplotlibilla.

## Syötteet

Ohjelma tulee saamaan syötteenä x,y -koordinaattipisteet, joiden välillä on kustannus (paino) eli käytännössä pisteiden välinen pituus kaksiulotteisella tasolla.

Ohjelma muodostaa raakakoordinaateista ensin kustannusmatriisin, jota pienin virittävä puu (MST) käyttää jälleen syötteenään listana. Tätä listaa Christofidesin algoritmi ... (jatkuu)

## Aika- ja tilavaativuus

Koska kauppamatkustajan ongelma on NP-kova-ongelma, toteutus isommalle sijaintiryppäälle tehdään approksimaatioalgoritmina tai heuristisena algoritmina. Tässä on valittu approksimaatioalgoritmi toteutukseen.

Christofidesin algoritmin aika- ja tilavaatimuus ... (kesken)

Ohjeistus vielä alla:
"Käytä aika ja tilavaatimuuksia apuvälineenä ymmärtääksenne, miten työhön kannattaa asennoitua.
Nämä kannattaa katsoa wikipediasta ja varmistaa, että ymmärrätte oman algoritmin kohdalla mistä ne tulevat. Miksi algoritmisi tarvitsee sen verran aikaa?"

## Lähteet

MST:tä ja Primiä varten luettu:
Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2022). Introduction to algorithms / Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, Clifford Stein. (Fourth edition.). The MIT Press.

Christofidesia varten ... (kesken)

## Harjoitustyön ydin

Harjoitustyön ydin on kirjoittaa ikiaikaiseen kauppamatkustajan pulmaan algoritmi, joka on nyt valittu Christofidesin 1,5-approksimaatioalgoritmi. Tämä tarkoittaa, että Christofidesin algoritmi takaa enintään 1,5-kertaisen tuloksen.

Kauppamatkustajan ongelmassa pyritään löytämään mahdollisimman kustannustehokkain reitti kaikkien annettujen pisteiden välille niin, että jokaisessa pisteessä käydään vain kerran ja että ensimmäiseen pisteeseen palataan. Tässä tapauksessa kustannuksena kahden pisteen välillä (paino) käytetään matkaa, vaikka se voisi olla myös esim. aika tai taloudellinen kustannus.

Pisteet ja graafit (MST ja lopullinen reitti) visualisoidaan matplotlibilla, jotta testaaminen onnistuu myös visuaalisesti.

Ensin on tuotettava kustannusmatriisi, jota pienin virittävä puu (MST) käyttää pohjanaan. MST muodostetaan hyödyntäen Primin algoritmia. Kun MST-lista on valmis ... (kesken)
