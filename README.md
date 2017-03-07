# FumeCrawler
## Crawler para pegar os horários das aulas

#### Obs: Por enquanto o crawler só retorna as datas da Avaliação 1

### Funcionamento:

#### - Terminal/CMD

1. Rodar `install.py` no terminal/CMD
2. Rodar `fumeCrawler.py`
3. Seguir de acordo com sua vontade escolhendo as opções

#### - Importando em algum projeto

##### Pode ser feito de duas formas:
1. Importando: `from fumeCrawler import FumeCrawler`
2. Passando o RA e a senha através da função `.run(RA, password)`

 Ex:
 ```python
 from fumeCrawler import FumeCrawler

fumeCrawler = FumeCrawler()
fumeCrawler.run('1A221455701', '******')
 ```

