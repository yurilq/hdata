from google.cloud import storage, bigquery
import pandas as pd

def baixar_dados_gcs_hdata(bucket_name, blob_name):
    """Baixa um arquivo do Google Cloud Storage e retorna o caminho local."""
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(blob_name)
    caminho_local = f'temp/{blob_name.split("/")[-1]}'
    blob.download_to_filename(caminho_local)
    return caminho_local

def enviar_para_bigquery_hdata(caminho_csv, dataset_id, tabela_id):
    """Envia um arquivo CSV para uma tabela no BigQuery."""
    client = bigquery.Client()
    tabela_ref = f'{client.project}.{dataset_id}.{tabela_id}'
    
    df = pd.read_csv(caminho_csv)
    job = client.load_table_from_dataframe(df, tabela_ref)
    job.result()  # Aguarda a conclusão do carregamento
    print(f'Dados carregados com sucesso na tabela {tabela_ref}')
