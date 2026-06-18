# Testausdokumentti

## Yksikkötestauksen kattavuusraportti

Testit kattavat 6 algoritmimoduulia yhteensä 20 testillä.

| Tiedosto            | Testejä | Testattu                                      |
| ------------------- | ------- | --------------------------------------------- |
| `test_graph.py`     | 3       | `euclidean_distance`, `build_distance_matrix` |
| `test_mst.py`       | 2       | `prim_mst`                                    |
| `test_matching.py`  | 6       | `odd_degree_vertices`, `greedy_matching`      |
| `test_multigraph.py`| 2       | `build_multigraph`                            |
| `test_euler.py`     | 4       | `eulerian_circuit`                            |
| `test_hamilton.py`  | 3       | `hamiltonian_circuit`                         |

`visualize.py` ja `main.py` eivät ole yksikkötestattu.

## Mitä on testattu ja miten?

Testit on kirjoitettu Pythonin `unittest`-kirjastolla.

Testatut asiat:

- `euclidean_distance`: etäisyys samaan pisteeseen on 0, ja pisteiden (0,0) ja (3,4) välinen etäisyys on 5.0
- `build_distance_matrix`: etäisyysmatriisin diagonaali on 0 kaikille solmuille
- `prim_mst`: n solmun MST:ssä on n-1 kaarta, ja algoritmi valitsee halvimman kaaren
- `odd_degree_vertices`: palauttaa oikeat solmut, tulosjoukon koko on aina parillinen
- `greedy_matching`: jokainen solmu esiintyy tuloksessa tasan kerran, lähimmät solmut paritetaan
- `build_multigraph`: multigraafissa on enemmän kaaria kuin MST:ssä, ja jokaisen solmun aste on parillinen
- `eulerian_circuit`: kierros alkaa ja loppuu samaan solmuun, kaikki solmut käydään

## Minkälaisilla syötteillä testaus tehtiin?

Yksikkötesteissä käytetään pieniä koodatuja syötteitä, esimerkiksi 3-4 solmun verkkoja, joissa kaarten painot ovat tiedossa etukäteen. Näin tulos on helppo laskea käsin ja verrata. Mukana on myös rajatapaukset tyhjälle verkolle ja yhden solmun verkolle.

Manuaalisesti on testattu kahdella dataseteillä:

- 20 Suomen suurinta kaupunkia (EPSG:3067)
- 100 Yhdysvaltain suurinta kaupunkia (EPSG:3857)

## Miten testit voidaan toistaa?

```bash
python -m pytest tests/ -v
```

## Empiirinen testaus

Algoritmia ei ole testattu empiirisesti suoritusajan tai ratkaisun laadun suhteen. Tämä voisi olla jatkokehityskohde, esimerkiksi vertailemalla Christofidesin reitin pituutta optimaaliseen ratkaisuun eri kokoisilla syötteillä.
