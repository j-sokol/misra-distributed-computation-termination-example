# Ukončení distribuovaného výpočtu pomocí markerů (Misra)

Jan Sokol

Semestrální práce na předmět NI-DSV, 2020

## Algoritmus v pseudokódu

Pseudokód je převzaný z přednášky v [1]:

```
color           := black
token_present   := false
round           := 0
state           := not computing (false)

when received message:
    state = computing (true)
    color = black

when waiting_for_computing:
    state = not computing (false)

when received_token(token):
    round = token
    token present = True
    if round == size_of_cluster and color == white:
        Log out that distributed computation is terminated

when token_present and state == passive (false):
    if color == black:
        round = 0
    else:
        round = round + 1
    send token(round) to successor_in_topology
    color = white
    token_present = false
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

Přiřadíme token libovolnému uzlu

```
bash ./assign_token.sh
``` 

Spustíme výpočet pomocí příkazu

```
bash ./commands/simulate_computing.sh
```
V terminálu se spuštěným `docker-compose` uvidíme komunikaci Misrova algoritmu. Po dokončení se zobrazí `COMPUTATION_TERMINATED`. 

Výstup vypadá následovně:
```
node3_1  | [2020-12-12 13:07:01,653] [root] [INFO] [10.10.0.3] Handling waiting_message: token_present=True, is_computing=True, colour=black, round=16
node3_1  | [2020-12-12 13:07:01,653] [root] [INFO] [10.10.0.3] Handling send_token: token_present=True, is_computing=False, colour=black, round=16
node3_1  | [2020-12-12 13:07:01,653] [root] [INFO] [10.10.0.3] Next node is 10.10.0.4
node3_1  | [2020-12-12 13:07:01,654] [root] [INFO] [10.10.0.3] forwarding token 0 to 10.10.0.4
node1_1  | [2020-12-12 13:07:01,660] [root] [INFO] [10.10.0.4] Received token 0 from 10.10.0.3
node1_1  | [2020-12-12 13:07:01,661] [root] [INFO] [10.10.0.4] Handling received_token 0
node1_1  | [2020-12-12 13:07:01,661] [root] [INFO] [10.10.0.4] vars: token_present=False, is_computing=False, colour=black, round=0
node1_1  | INFO:     10.10.0.3:39632 - "GET /receive_token?token=0 HTTP/1.1" 200 OK
node1_1  | [2020-12-12 13:07:02,632] [root] [INFO] [10.10.0.4] Handling send_token: token_present=True, is_computing=False, colour=black, round=0
node3_1  | [2020-12-12 13:07:02,633] [root] [INFO] [10.10.0.3] Token 0 to 10.10.0.4 forwarded, resp={"status":"token received"}
node3_1  | INFO:     10.10.0.4:45050 - "GET /compute?compute_time=29 HTTP/1.1" 200 OK
node1_1  | [2020-12-12 13:07:02,632] [root] [INFO] [10.10.0.4] Next node is 10.10.0.2
node1_1  | [2020-12-12 13:07:02,632] [root] [INFO] [10.10.0.4] forwarding token 0 to 10.10.0.2
node2_1  | [2020-12-12 13:07:02,639] [root] [INFO] [10.10.0.2] Received token 0 from 10.10.0.4
node2_1  | [2020-12-12 13:07:02,639] [root] [INFO] [10.10.0.2] Handling received_token 0
node2_1  | [2020-12-12 13:07:02,639] [root] [INFO] [10.10.0.2] vars: token_present=False, is_computing=False, colour=white, round=0
node2_1  | INFO:     10.10.0.4:58690 - "GET /receive_token?token=0 HTTP/1.1" 200 OK
node2_1  | [2020-12-12 13:07:03,645] [root] [INFO] [10.10.0.2] Handling send_token: token_present=True, is_computing=False, colour=white, round=0
node1_1  | [2020-12-12 13:07:03,646] [root] [INFO] [10.10.0.4] Token 0 to 10.10.0.2 forwarded, resp={"status":"token received"}
node2_1  | [2020-12-12 13:07:03,646] [root] [INFO] [10.10.0.2] Next node is 10.10.0.3
node2_1  | [2020-12-12 13:07:03,646] [root] [INFO] [10.10.0.2] forwarding token 1 to 10.10.0.3
node3_1  | [2020-12-12 13:07:03,652] [root] [INFO] [10.10.0.3] Received token 1 from 10.10.0.2
node3_1  | [2020-12-12 13:07:03,652] [root] [INFO] [10.10.0.3] Handling received_token 1
node3_1  | [2020-12-12 13:07:03,652] [root] [INFO] [10.10.0.3] vars: token_present=False, is_computing=False, colour=white, round=1
node2_1  | [2020-12-12 13:07:04,660] [root] [INFO] [10.10.0.2] Token 1 to 10.10.0.3 forwarded, resp={"status":"token received"}
node3_1  | INFO:     10.10.0.2:49522 - "GET /receive_token?token=1 HTTP/1.1" 200 OK
node3_1  | [2020-12-12 13:07:04,658] [root] [INFO] [10.10.0.3] Handling send_token: token_present=True, is_computing=False, colour=white, round=1
node3_1  | [2020-12-12 13:07:04,659] [root] [INFO] [10.10.0.3] Next node is 10.10.0.4
node3_1  | [2020-12-12 13:07:04,659] [root] [INFO] [10.10.0.3] forwarding token 2 to 10.10.0.4
node1_1  | [2020-12-12 13:07:04,664] [root] [INFO] [10.10.0.4] Received token 2 from 10.10.0.3
node1_1  | [2020-12-12 13:07:04,665] [root] [INFO] [10.10.0.4] Handling received_token 2
node1_1  | [2020-12-12 13:07:04,665] [root] [INFO] [10.10.0.4] vars: token_present=False, is_computing=False, colour=white, round=2
node1_1  | INFO:     10.10.0.3:39638 - "GET /receive_token?token=2 HTTP/1.1" 200 OK
node3_1  | [2020-12-12 13:07:05,672] [root] [INFO] [10.10.0.3] Token 2 to 10.10.0.4 forwarded, resp={"status":"token received"}
node1_1  | [2020-12-12 13:07:05,671] [root] [INFO] [10.10.0.4] Handling send_token: token_present=True, is_computing=False, colour=white, round=2
node1_1  | [2020-12-12 13:07:05,672] [root] [INFO] [10.10.0.4] Next node is 10.10.0.2
node1_1  | [2020-12-12 13:07:05,672] [root] [INFO] [10.10.0.4] forwarding token 3 to 10.10.0.2
node2_1  | [2020-12-12 13:07:05,678] [root] [INFO] [10.10.0.2] Received token 3 from 10.10.0.4
node2_1  | [2020-12-12 13:07:05,678] [root] [INFO] [10.10.0.2] Handling received_token 3
node2_1  | [2020-12-12 13:07:05,679] [root] [INFO] [10.10.0.2] vars: token_present=False, is_computing=False, colour=white, round=3
node2_1  | [2020-12-12 13:07:05,679] [root] [ERROR] [10.10.0.2] >>>> COMPUTATION TERMINATION DETECTED
```
Případně lze výpočet inicializovat pomocí
```
bash ./run_all.sh
``` 



Poté lze znovu spustit výpočet pomocí 


```
bash ./commands/simulate_computing.sh
```


Ukázku ukončíme zasláním signálu `SIGNINT` procesu s `docker-compose` (`^C`).

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