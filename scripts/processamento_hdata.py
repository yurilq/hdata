import pandas as pd
from scripts.util_hdata import carregar_configuracoes_hdata, exportar_dados_hdata

def executar_fluxo_enriquecimento_hdata(caminho_dados_recebidos, caminho_config, caminho_saida):
    """
    Executa todo o fluxo de enriquecimento de dados.
    """
    # Carregar os dados
    dados_recebidos = pd.read_excel(caminho_dados_recebidos)

    # Carregar configurações de regras
    config = carregar_configuracoes_hdata(caminho_config)

    # Aplicar regras de negócio e exportar
    dados_enriquecidos = aplicar_regras_de_negocio_hdata(dados_recebidos, config)
    exportar_dados_hdata(dados_enriquecidos, caminho_saida)

def aplicar_regras_de_negocio_hdata(dados, config):
    # Exemplo de como aplicar as regras
    if 'ajustar_valores' in config:
        regra = config['ajustar_valores']
        coluna = regra['coluna']
        valor = regra['valor']
        dados[coluna] *= valor

    # Outras regras podem ser aplicadas aqui
    return dados
