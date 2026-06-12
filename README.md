# tiralab-tsp

Christofidesin approksimaatioalgoritmin toteutus kauppamatkustajan ongelmaan (TSP).

## Vaatimukset

- Python 3.8+
- matplotlib

## Asennus ja käynnistys

```bash
# Kloonaa repositorio
git clone https://github.com/lkauria/tiralab-tsp.git
cd tiralab-tsp

# Luo virtuaaliympäristö ja aktivoi se
python3 -m venv .venv
source .venv/bin/activate

# Asenna riippuvuudet
pip install matplotlib pylint

# Aja ohjelma
python src/main.py
```

## Datasetti

Vaihda datasetti tiedostossa `src/data/nodes.py` muuttamalla yläosan `DATASET`-muuttujaa:

```python
DATASET = "finland"  # 20 largest cities in Finland
DATASET = "usa"      # 100 largest cities in the US
DATASET = "own"      # your own dataset
```

### Oman datasettin lisääminen

Koordinaatit täytyy olla valmiiksi muunnettu — ohjelma ei tee koordinaattimuunnoksia. Lisää pisteet `nodes_own`-listaan `src/data/nodes.py`:ssä `(x, y)` -tuplina:

```python
nodes_own = [
    (123456, 654321),
    (234567, 765432),
    ...
]
```

Jos data on EPSG-koordinaatistossa, vaihda `CRS`-arvo tiedoston lopussa oikeaan:

```python
if DATASET == "own":
    nodes = nodes_own
    CRS = "EPSG:xxxx"  # replace with the correct coordinate system
```

Jos koordinaatisto ei ole tiedossa, aseta `CRS = None`.

## Testien ajo

```bash
python -m pytest tests/ -v
```

## Koodin laadun tarkistus

```bash
pylint src/
```
