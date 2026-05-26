# Määrittelydokumentti (luonnos)

Jatkan periodeissa 1 ja 2 (vuosi 2025) kesken jäänyttä työtä.

Opinto-ohjelmani on tietojenkäsittelytieteen kandiohjelma.

## Ohjelmointikieli

Ohjelmointikieli on python. Vertaisarvioinnissa myös javascript/typescript, react ja java onnistuvat.

## Algoritmi

Projektissa toteutetaan kauppamatkustajan ongelman ratkaiseva Christofidesin aproksimaatioalgoritmi ja visualisoidaan algoritmin toteutus valmiilla visualisointikirjastolla, matplotlibilla.

## Syötteet

Ohjelma tulee saamaan syötteenä x,y -koordinaattipisteet, joiden välillä on kustannus (paino) eli käytännössä pisteiden välinen pituus kaksiulotteisella tasolla.

Ohjelma laskee ensin koordinaateista kustannusmatriisin. Matriisia käytetään syötteenä pienimmän virittävän puun (MST) muodostamisessa ja niin edelleen. Algoritmin tarkempi avaus on toteutusdokumentaatiossa.

## Aika- ja tilavaativuus

Koska kauppamatkustajan ongelma on NP-kova-ongelma, toteutus isommalle sijaintiryppäälle tehdään approksimaatioalgoritmina tai heuristisena algoritmina. Tässä on valittu approksimaatioalgoritmi toteutukseen.

Christofidesin algoritmin aika- ja tilavaatimuus: Algoritmin pullonkaula on täydellisen parituksen steppi, joka on O(n^3). Approksimaatioalgoritmilla pystytään käsittelemään kymmeniä tuhansia sijaintipisteitä, kun eksakti TSP tämän hetken laskentatehoilla (vuosi 2026) pääsee muutaman kymmenen sijantipisteen ratkaisuun.

## Lähteet

Yleiskuvaa Christofidesin algoritmista muun muassa Wikipediassa: https://en.wikipedia.org/wiki/Christofides_algorithm .

MST:tä ja Primiä varten luettu lukua 23:
Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2022). Introduction to algorithms / Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, Clifford Stein. (Fourth edition.). The MIT Press.

## Harjoitustyön ydin

Harjoitustyön ydin on kirjoittaa kauppamatkustajan pulmaan algoritmi, joka on nyt valittu Christofidesin 1,5-approksimaatioalgoritmi. Tämä tarkoittaa, että Christofidesin algoritmi takaa enintään 1,5-kertaisen tuloksen globaaliin optimiin verrattuna.

Kauppamatkustajan ongelmassa pyritään löytämään mahdollisimman kustannustehokkain reitti kaikkien annettujen pisteiden välille niin, että jokaisessa pisteessä käydään vain kerran ja että ensimmäiseen pisteeseen palataan viimeisestä. Tässä tapauksessa kustannuksena kahden pisteen välillä (paino) käytetään matkaa, vaikka se voisi olla myös esim. aika tai taloudellinen kustannus.

Pisteet ja graafit visualisoidaan matplotlibilla, jotta testaaminen onnistuu myös visuaalisesti.
