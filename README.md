# Case iFood

<hr>

## 1. Sumário

1. Sumário
2. Estrutura dos arquivos
3. Como executar
4. Contexto
5. Estratégia
6. Resultado

## 2. Estrutura de arquivos

```text
📁 data - pasta de dados processados e não processados
    📁 processed - pasta com dados processados
        📄 AnaliseClusters.xlsx - planilha com dados dos clusters para que possam ser analisados no analisador de clusters
        📄 cluster_description.txt - desatques gerados pelo analisador de clusters
        📄 offers_for_modeling.csv - dados de ofertas gerados para treinar o modelo de uso de oferta
        📄 profile_clustered_dados.xlsx - planilha com dados que devem ser colocados na aba DADOS do AnaliseClusters.xlsx
        📄 profile_clustered_id.csv - de para que mostra qual é o cluster de cada cliente
        📄 profile_for_clustering - dados de perfil para a clusterização
    📁 raw - pasta com dados não processados
        📄 offers.json - dados de ofertas
        📄 profile.json - dados de clientes
        📄 transactions.json - dados de transações
📁 notebooks - pasta contento os notebooks do case
    📄 01_Data_Processing.ipynb - Processamento de dados não processados
    📄 02_Clustering.ipynb - Criar os clusters de clientes
    📄 03_Cluster_Analiser.ipynb - Analisa os clusters
    📄 04_Data_4_Modeling.ipynb - Gera os dados para a modelagem
    📄 05_Modeling.ipynb - Cria os modelos de uso de ofertas
    📄 06_Offer_Optimization.ipynb - Otimiza as ofertas para aumentar o uso
📁 presentaion - pasta de apresentações
    📄 01_iFood_Case.pdf - apresentação do case iFood
📁 src - pasta de códigos e arquivos auxiliares para os notebooks
    📁 models - pasta com os modelos treinados
        📄 catboost_clN - arquivo do modelo salvo após o treino
    📄 data_processing_functions.py- arquivo com código python a ser utilizado no notebook 01
    📄 Model.py- arquivo com código python com código preparado para receber alguns dados do modelo e ser salvo
    📄 offer_opt_functions.py- arquivo com código python a ser utilizado no notebook 06
📄 Case_Técnico_Data_Science_-_iFood_.pdf - detalhes sobre o case
📄 requirements.txt- todas as dependencias python para rodar os códigos
```

## 3. Como executar

Todos os códigos estão escritos em Python 3.11, portanto instale a versão necessária.

O notebook de processamento de dados utiliza PySpark local, defina as configurações corretas de conexão se necessário.

Após a instalação do PySpark localmente, pode-se executar os comando:

```text
> cd diretorio\do\spark
> spark-shell
```

E assim, você conseguirá executar criar a instancia do Spark que pode hospedar sessões do PySpark

O notebook de modelagem pode dar algum problema caso o treino do modelo CatBoost tente gerar arquivos em uma pasta que você não tenha acesso, portanto tente alterar o diretório para uma pasta que você tenha acesso.

Os demais códigos serão executados sem problemas.

## 4. Objetivo

O principal objetivo deste case é otimizar o oferecimento de ofertas à todos os clientes.

## 5. Estratégia

A solução é dividida em 5 partes:

1. Clusterização de clientes - Ao criar cluster de clientes, podemos segmenta-los de acordo com seu comportamento, criando mais exclusividade em nossa análise
2. Análise dos clusters - Detectando as principais características que tornam cada cluster exclusivo, e nomeando cada um de acordo com suas características, com ajuda de GenAI
3. Geração de modelos de classificação - Treinamento de modelos de classificação para calcular a probabilidade de uso dos cupons oferecidos
4. Análise dos modelos - Voltadas para detectar quais variáveis mais influenciam o calculo da probabilidade, assim podemos
5. Sugestão dos modelos - Utilizando a análise de influencias, detectamos as variáveis endógenas para que possamos aprimorar o envio de ofertas

## 6. Resultado

Através da analise do modelo utilizando a biblioteca Shap, vimos algumas variáveis endógenas que influenciam positivamente para o uso de ofertas, então modificamos seus valores para melhorar os resultados.
