import json
import pandas as pd

def carregar_configuracoes_hdata(caminho_config):
    """
    Carrega as configurações do arquivo JSON de regras de negócio.
    
    Args:
        caminho_config (str): Caminho do arquivo de configuração (regras).
    
    Returns:
        dict: Configurações carregadas do arquivo.
    """
    with open(caminho_config, 'r') as file:
        config = json.load(file)
    return config

def exportar_dados_hdata(df, caminho_saida):
    """
    Exporta os dados processados para um arquivo CSV.
    
    Args:
        df (pd.DataFrame): DataFrame com os dados enriquecidos.
        caminho_saida (str): Caminho do arquivo de saída.
    """
    df.to_csv(caminho_saida, index=False)
    print(f'Dados exportados com sucesso para {caminho_saida}')

def carregar_dados_excel_hdata(caminho_entrada):
    """
    Carrega os dados de um arquivo Excel.
    
    Args:
        caminho_entrada (str): Caminho do arquivo Excel de entrada.
    
    Returns:
        pd.DataFrame: DataFrame contendo os dados do arquivo Excel.
    """
    return pd.read_excel(caminho_entrada)

def validar_colunas_obrigatorias_hdata(df, colunas_obrigatorias):
    """
    Valida se as colunas obrigatórias estão presentes no DataFrame.
    
    Args:
        df (pd.DataFrame): DataFrame com os dados a serem validados.
        colunas_obrigatorias (list): Lista de colunas que devem estar presentes.
    
    Raises:
        ValueError: Se alguma das colunas obrigatórias estiver ausente.
    """
    colunas_faltantes = [col for col in colunas_obrigatorias if col not in df.columns]
    
    if colunas_faltantes:
        raise ValueError(f"Colunas faltantes: {', '.join(colunas_faltantes)}")

def verificar_registros_vazios_hdata(df):
    """
    Verifica se existem registros vazios no DataFrame.
    
    Args:
        df (pd.DataFrame): DataFrame contendo os dados a serem verificados.
    
    Returns:
        int: Quantidade de registros vazios.
    """
    registros_vazios = df.isnull().sum().sum()
    return registros_vazios
