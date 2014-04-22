SimuCache
=========

O simulador possui os seguintes parâmetros de entrada:

• Número de arquivos. Número total de arquivos na simulação.

• Número de arquivos no cache. Número máximo de arquivos que o cache suporta.

• Algoritmo do cache. Algoritmo que o cache simulado utiliza. Pode ser LRU, LFU, FIFO ou RR.


• Modelo de frequência. Essa variável preenche a frequência inicial de acesso dos arquivos durante a simulação. É possível escolher entre aleatório, uniforme, zipf ou particular; em que nessa última é possível inserir manualmente as frequências para cada arquivo. Caso seja escolhida a distribuição zipf, o usuário deve indicar o expoente que será utilizado na distribuição. Esse expoente varia a homogeneidade da distribuição.

• Timeslot. Quantidade de timeslots que a simulação vai ter.

• Número de requisições. Número de requisições ao cache a cada timeslot.

Esse simulador pode ser utilizado para simular uma rede ICN, determinando
a quantidade de caches que teriam no simulador e o algoritmo desejado para guardar
conteúdo.

