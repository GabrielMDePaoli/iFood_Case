### Formas de tentar analisar melhor nossa tabela de dados

- Cluster de clientes (provavelmente serão poucos clusters devido a pouca informação)
    - K-means (aproveitar para analisar os clusters e criar nomes para os perfis)
- Analisar correlação entre transações e idade e limite de crédito
- Transformar o dia após inicio do teste em uma data (não sei qual poderia ser, apenas para verificar se tem alguma sazonalidade, isso pode indicar melhor o momento de enviar o cupom)

### Inclusão de novos dados

- Frequencia de compra por semana, quantidade de transações por cliente
- Tipos de ofertas mais utilizadas por cliente
    - Preço mínimo
    - Duração
- Percentual de ofertas utilizadas por cliente
    - Geral
    - Tipo de oferta
    - Veículo
- Tempo médio que demora para usar uma oferta
- Tempo médio que demora para realizar outro pedido
- Taxa de pedidos com cupom

### Possiveis modelagens para se aplicar

- Calcular a probabilidade de a pessoa usar uma oferta
- Por similaridade: Alternating Least Squares (ALS) do PySpark

### Analise de resultado

- Estimar aumento na taxa de conversão
- Calcular retorno médio por cliente
- Comparando com o cenário atual

### Slides

1. Explica a lógica da segmentação/modelo em linguagem simples
2. Mostre antes vs. depois da personalização
3. Gráfico de aumento potencial de uso das ofertas
4. Destaque: menos ofertas desperdiçadas, mais conversão
5. Simulação de retorno estimado
