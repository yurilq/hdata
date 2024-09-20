# HData GCP Data Enrichment Project

## Visão Geral
Este projeto realiza o enriquecimento de dados financeiros e integra com o Google Cloud Platform (GCP), utilizando Google Cloud Storage para armazenamento e BigQuery para armazenamento final dos dados processados.

## Configuração

### Pré-requisitos

1. **Google Cloud SDK** instalado e autenticado.
2. **Bucket no Google Cloud Storage** configurado para armazenamento de dados.
3. **BigQuery Dataset e Tabela** configurados.

### Passos

1. **Configurar o ambiente**
   Configure as credenciais do GCP usando:
   ```bash
   gcloud auth application-default login
