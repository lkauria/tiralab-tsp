# Käyttöohje

## Ohjelman suorittaminen

```bash
python src/main.py
```

Ohjelma ajaa Christofidesin algoritmin valitulle dataseteille ja näyttää jokaisen vaiheen visualisoituna.

## Datasetti

Vaihda datasetti tiedostossa `src/data/nodes.py` muuttamalla `DATASET`-muuttujaa:

```python
DATASET = "finland"  # 20 Suomen suurinta kaupunkia
DATASET = "usa"      # 100 Yhdysvaltain suurinta kaupunkia
DATASET = "own"      # oma datasetti
```

## Oman datasettin käyttö

Ohjelma hyväksyy syötteenä listan pisteitä `(x, y)` -koordinaatteina. Koordinaatit täytyy olla valmiiksi projisoitu, ohjelma ei tee koordinaattimuunnoksia.

Lisää pisteet `nodes_own`-listaan `src/data/nodes.py`:ssä:

```python
nodes_own = [
    (123456, 654321),
    (234567, 765432),
]
```

Aseta myös koordinaatisto tiedoston lopussa:

```python
if DATASET == "own":
    nodes = nodes_own
    CRS = "EPSG:xxxx"  # vaihda oikeaan EPSG-koodiin
```

Jos koordinaatisto ei ole tiedossa, aseta `CRS = None`.

## Visualisointi

Ohjelma näyttää algoritmin vaiheet automaattisesti, yksi kuva kerrallaan (2 sekuntia per kuva). Jos haluat tarkastella jokaista kuvaa itse rauhassa, aseta `src/visualize.py`:ssä:

```python
MANUAL = True
```

Tällöin jokainen kuva jää auki, kunnes suljet ikkunan itse.
