# tiralab-tsp

Christofidesin approksimaatioalgoritmin toteutus kauppamatkustajan ongelmaan (TSP).

## Vaatimukset

- Python 3.8+
- matplotlib
- pyproj

## Asennus ja käynnistys

```bash
# Kloonaa repositorio
git clone https://github.com/lkauria/tiralab-tsp.git
cd tiralab-tsp

# Luo virtuaaliympäristö ja aktivoi se
python3 -m venv .venv
source .venv/bin/activate

# Asenna riippuvuudet
pip install matplotlib pyproj pylint

# Aja ohjelma
python src/main.py
```

## Testien ajo

```bash
python -m pytest tests/ -v
```

## Koodin laadun tarkistus

```bash
pylint src/
```