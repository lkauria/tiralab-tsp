## Toteutusdokumentti

### Ohjelman yleisrakenne

Ohjelma toteuttaa Christofidesin approksimaatioalgoritmin kauppamatkustajan ongelmaan (TSP). Koodi on jaettu tiedostoihin tehtävän mukaan:

- `graph.py` — laskee etäisyydet solmujen välille etäisyysmatriisiksi
- `mst.py` — rakentaa minimivirityspuun listamuotoon (MST)
- `matching.py` — parittaa parittomien solmujen joukon (tätä vielä hiottava)
- `multigraph.py` — yhdistää MST:n ja parituksen yhteen multigraafiin
- `euler.py` — luo Euler-kierroksen (kesken)
- (Tähän tulee vielä Hamilton)
- `visualize.py` — piirtää havainnoillistavat kuvat
- `main.py` — kutsuu yllä olevia tiedostoja järjestyksessä

---

### Algoritmin vaiheet

**0. Etäisyysmatriisi**

Lasketaan kaikkien solmujen väliset etäisyydet euklidisella kaavalla. Tulos on n×n-matriisi.

**1. Minimivirityspuu (MST)**

Käytetään Primin algoritmia. Se rakentaa puun käymällä solmuja läpi yksi kerrallaan ja valitsemalla aina pienimmän painon kaaren puun ulkopuolelle. Palautetaan vierekkäisyyslista.

**2. Parittomat solmut**

Katsotaan mitkä solmut ovat yhteydessä parittomaan määrään muita solmuja (yritä selittää yksinkertaisemmin). Näitä solmuja täytyy olla aina parillinen määrä (matemaattinen fakta).

**3. Täydellinen paritus (matching)**

Paritetaan parittomien solmujen joukko. Käytetään ahnetta algoritmia: valitaan toistuvasti lähimpien parittomien solmujen pari. Ei ole optimaalinen, mutta riittävä approksimaatioon.

**4. Multigraafi**

Yhdistetään MST:n kaaret ja parituskaaret. Sama kaari voi esiintyä kahdesti. Tämä takaa, että jokaisen solmun aste on parillinen — Euler-kierroksen edellytys.

**5. Euler-kierros**

kesken

**6. Hamiltonin kierros** _(tulossa)_

---

### Aika- ja tilavaativuudet

| Vaihe                      | Aikavaativuus |
| -------------------------- | ------------- |
| Etäisyysmatriisi           | O(n²)         |
| Primin MST                 | O(n²)         |
| Parittomien etsintä        | O(n)          |
| Ahne paritus               | O(n²)         |
| Multigraafin rakentaminen  | O(n)          |
| Euler-kierros (Hierholzer) | O(n)          |

Koko algoritmin aikavaativuus on O(n²), koska etäisyysmatriisi ja Primin algoritmi dominoivat.

Tilavaativuus on O(n²) etäisyysmatriisin takia.

---

### Puutteet ja parannusehdotukset

- Ahne paritus ei ole optimaalinen. Täydellinen paritus (esim. Edmond's blossom -algoritmi) antaisi paremman tuloksen, mutta on huomattavasti monimutkaisempi.
- Primin algoritmin voisi nopeuttaa kekoon perustuvaksi O(n log n) -ratkaisuksi.
- Eurer ja Hamilton toteuttamatta

---

### Tekoälyn käyttö

Työssä on käytetty Claude-kielimallia (Anthropic) koodin synnyttämisessä, parantamisessa ja debuggaamisessa. Vaikka koodi on kirjoitettu itse, suuri osa Christofidesin toteutuksesta pohjaa hyvin pitkälle tekoälyn antamiin ratkaisuehdotuksiin, kun omia ratkaisuja on lähdetty hiomaan. Malli on myös erityisesti auttanut visualisoinnissa ja algoritmien rakenteen selittämisessä. Kaikki koodi on kuitenkin kirjoitettu ja ymmärretty itse, vaikka tekoäly sitä on ehdottanutkin.

---

### Lähteet

- Christofidesin algoritmi: https://en.wikipedia.org/wiki/Christofides_algorithm
- Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2022). Introduction to algorithms (4. painos). The MIT Press.
- Christofides, N. (1976). Worst-case analysis of a new heuristic for the travelling salesman problem.
- Hierholzerin algoritmi: https://en.wikipedia.org/wiki/Eulerian_path
