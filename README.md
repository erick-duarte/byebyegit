## byebyegit
BR: ferramenta para identificar **git exposed** em multiplos dominios.

EN: tool to identify **git exposed** on multiple domains.


## Usage instructions :
```
Note : Use python 3.7+

$ git clone https://github.com/erick-duarte/byebyegit
$ cd byebyegit
$ pip3 install -r requirements.txt
$ python3 byebyegit.py --domain example.com
```

## Usage options :
```
--domain, -d -> Domain name of the taget [ex : google.com]
--retries, -r -> Specify number of retries for 4xx and 5xx errors
```

## Perfect use:
[subfinder](https://github.com/projectdiscovery/subfinder)

[httpx](https://github.com/projectdiscovery/httpx)

```
subfinder -d example.com.br | httpx | byebyegit.py
```

<img width="681" alt="Captura de Tela 2023-01-26 às 11 13 23" src="https://user-images.githubusercontent.com/59427098/214860671-beaca57f-50b1-45e2-8992-840010764af7.png">
