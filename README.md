# Ukončení distribuovaného výpočtu pomocí markerů (Misra)

Jan Sokol

Semestrální práce na předmět NI-DSV, 2020

## Algoritmus v pseudokódu

Pseudokód je převzaný z přednášky v [1]:

```
TODO
```

## Implementace

Aplikace je implementovaná pomocí FastApi frameworku v Pythonu. Distribuovaná applikace je nasazena pomocí Dockeru do virtuální sítě.



Při posílání tokenu mezi nodami je přidáno čekání

## Jak spustit semestrálku

Z rootového adresáře tohoto repozitáře je třeba spustit

```
docker-compose up
```
který nasadí 3 instance této aplikace do virtuální docker sítě. 

Pro ukázku výpočtu a Misrova algoritmu v jiném terminálu se připojíme na jednu z instancí

```

```

v adresáři `commands` spustíme příkaz na přidání uzlů do kastru

```
bash ./commands/add_nodes.sh
```

Spustíme výpočet pomocí příkazu

```
bash ./commands/simulate_computing.sh
```
V terminálu se spuštěným `docker-compose` uvidíme komunikaci Misrova algoritmu. Po dokončení se zobrazí `COMPUTATION_TERMINATED`. 

Výstup vypadá následovně:
```

```


Ukázku ukončíme zasláním signálu `SIGNINT` procesu s `docker-compose`.

### Lokálně

```
python3 -m venv __venv__
. ./__venv__/bin/activate
python3 -m pip install -r requirements.txt
```

``` 
bash docker-entrypoint.sh
``` 

## Reference

[1] https://moodle-vyuka.cvut.cz/pluginfile.php/307514/mod_page/content/4/MI-DSV_08.pdf
[2] https://www.cs.utexas.edu/users/misra/scannedPdf.dir/DetectTerm.pdf 