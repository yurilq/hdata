from scripts.processamento_hdata import executar_fluxo_enriquecimento_hdata
from scripts.gcp_utils_hdata import baixar_dados_gcs_hdata, enviar_para_bigquery_hdata

# Definir os parâmetros do GCP
bucket_name = 'hdata-bucket'
arquivo_entrada = 'input/dados_recebidos_hdata.xlsx'
arquivo_saida = 'output/dados_enriquecidos_hdata.csv'
dataset_id = 'hdata_financeiro'
tabela_id = 'dados_enriquecidos'

# Baixar o arquivo do GCS
caminho_local = baixar_dados_gcs_hdata(bucket_name, arquivo_entrada)

# Caminhos locais para arquivos temporários
caminho_saida_local = 'data/output/dados_enriquecidos_hdata.csv'
caminho_config = 'config/regras_hdata.json'

# Executar o fluxo de enriquecimento
executar_fluxo_enriquecimento_hdata(caminho_local, caminho_config, caminho_saida_local)

# Enviar o arquivo enriquecido para o BigQuery
enviar_para_bigquery_hdata(caminho_saida_local, dataset_id, tabela_id)
