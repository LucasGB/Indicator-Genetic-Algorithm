[RSI, SMA, MACD, X]
[Stoch, EMA, Bollinger Bands, MACD]

Aplicamos um crossover:
[RSI, SMA, Bollinger Bands, MACD], fitness = 0.6
[Stoch, EMA, MACD, X] fitness = 0.57



Utilizei o algoritmo genético PIKAIA, por Charbonneau. 
1 - Calcula o fitness de cada individuo da população.
2 - Seleciona pares de soluções da população atual, com a probabilidade de seleção sendo proporcional ao fitness da solução.
3 - Reproduzir as duas soluções selecionadas e gerar dois filhos.
4 - Repetir passos 2 e 3 até que o numero de individuos seja igual ao da população.
5 - Substituir a população atual com a nova gerada.
6 - Repetir os passos 1 a 5 até que um critério de termino seja satisfeito.