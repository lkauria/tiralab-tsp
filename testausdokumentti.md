# Testausdokumentti

## Yksikkötestauksen kattavuusraportti

Testit kattavat algoritmin ydinmoduulit: `graph.py` ja `mst.py`. Kukin tiedosto sisältää 2-3 yksikkötestiä.

## Mitä on testattu ja miten?

Testit on kirjoitettu Pythonin `unittest`-kirjastolla tiedostoihin `tests/test_graph.py` ja `tests/test_mst.py`.

Testatut asiat:

- `euclidean_distance`: etäisyys samaan pisteeseen on 0, ja tunnettu etäisyys antaa oikean tuloksen 5.0
- `build_distance_matrix`: etäisyysmatriisin diagonaali on 0 kaikille solmuille
- `prim_mst`: n solmun MST:ssä on n-1 kaarta, ja algoritmi valitsee halvimman kaaren

## Minkälaisilla syötteillä testaus tehtiin?

Yksikkötesteissä käytetään pieniä koodatuja syötteitä, esimerkiksi 3 solmun verkko, jossa kaarten painot ovat tiedossa etukäteen. Näin tulos on helppo laskea käsin ja verrata.

Manuaalisesti on testattu kahdella dataseteillä:

- 20 Suomen suurinta kaupunkia (EPSG:3067)
- 100 Yhdysvaltain suurinta kaupunkia (EPSG:3857)

## Miten testit voidaan toistaa?

```bash
python -m pytest tests/ -v
```

## Empiirinen testaus

kesken

Algoritmia ei ole testattu empiirisesti suoritusajan tai ratkaisun laadun suhteen. Tämä voisi olla jatkokehityskohde, esimerkiksi vertailemalla Christofidesin reitin pituutta optimaaliseen ratkaisuun eri kokoisilla syötteillä.
