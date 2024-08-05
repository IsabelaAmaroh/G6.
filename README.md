# Group G6 

# Bem-vindo, este é o nosso projeto "Segmentação Semântica de Tumor Cerebral" desenvolvido para a disciplina de Engenharia de Software - UNIFESP - 2024

# Descrição do projeto:
Este projeto visa desenvolver um sistema de segmentação de imagens médicas, focado na detecção e classificação precisa de tumores (meningioma, glioma e pituitário) a nível de pixel. Utilizando técnicas avançadas de processamento de imagens e aprendizado profundo. O sistema identificará com precisão as regiões de interesse, fornecendo informações cruciais para diagnósticos e tratamentos mais eficazes.
Além disso, para fins de produtizar a solução garantindo performance e eficiência tecnológica, foi definida uma arquitetura em nuvem que propicie as etapas de extração das imagens e armazenamento em camadas de um datalake, sendo que nesta etapa também foi criado um webapp serveless em c# e implantado em cloud Microsoft Azure, cuja interface permite o upload das imagens diretamente integrado com o datalake. Para a etapa de processamento/transformação das imagens foi utilizada a plataforma Databricks, todo o código python foi transcrito para Pyspark nesta ferramenta, com isso obtendo o ganho em escalonamento de computação (cluster de processamento), processamento paralelo (spark) e performance significativa. Ao fim da etapa de transformação e tratamento das imagens, uma camada final de entrega destas foi defnida (camada trusted do datalake). O carregamento para esta camada disponibiliza as imagens e dados para fins de integração com ERP's ou datavis por exemplo.

# Imagens dos resultados obtidos:

- Grupo de recursos com componentes utilizados
![image](https://github.com/user-attachments/assets/e9ecd7b4-6148-4513-a291-4d98e18d7cf0)

- Webapp serveless para carregamento de imagens, integrado com a nuvem:
![image](https://github.com/user-attachments/assets/7a9e1c52-e747-4609-9260-20aa3a66d6fc)

- Armazenamento em datalake
![image](https://github.com/user-attachments/assets/6b22cda2-8f97-40d3-82a8-5b2dcab11c57)

- Arquitetura geral do projeto
![image](https://github.com/user-attachments/assets/cc4d6bd5-9195-48f6-94bf-6fed291c6e51)

- Processamento/transformacao de imagens com databricks
![image](https://github.com/user-attachments/assets/f56c65eb-6239-41a6-bd88-13cacc559027)

<!-- Este é um comentário em Markdown
![image](https://user-images.githubusercontent.com/77756047/211304452-220fedf0-f91b-490f-8a65-a60ce860bc5c.png) -->

## Nós usamos:

* Aprendizado Profundo;

* Processamento de Imagens Médicas;

* Engenharia de Software.

## Feito por:

### Gabriel Bianchi;
[![LinkedIn](https://img.icons8.com/color/48/000000/linkedin.png)](https://www.linkedin.com/in/gabriel-bianchis/)

### Isabela Amaro;
[![LinkedIn](https://img.icons8.com/color/48/000000/linkedin.png)](https://www.linkedin.com/in/isabela-amarocd/)

### Wilian Rosa.
[![LinkedIn](https://img.icons8.com/color/48/000000/linkedin.png)](https://www.linkedin.com/in/wiliam-rosa/)

<!-- ![GG6](https://github.com/IsabelaAmaroh/G6./assets/86272548/3086ed98-a12a-4109-8e55-4b812d3150dc) -->

