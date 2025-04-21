import pandas as pd
import numpy as np
import os
from joblib import load
from random import choices

y_col = ["TARGET_USED_OFFER"]
cluster_col = "cluster"

# Colunas com valores categoricos
categorical_features = [
    "age","credit_card_limit","total_transactions","avg_amount",
    "most_used_offer_type","transactions_offer_rate","avg_time_to_use_offer","avg_time_to_view_offer",
    "all_coupon_usage_rate","pct_used_channel_mobile","pct_used_channel_email","pct_used_channel_social",
    "pct_used_channel_web","pct_used_type_bogo","pct_used_type_discount","pct_used_type_informational",
    "all_coupon_viewed_rate","pct_viewed_channel_mobile","pct_viewed_channel_email","pct_viewed_channel_social",
    "pct_viewed_channel_web","pct_viewed_type_bogo","pct_viewed_type_discount","pct_viewed_type_informational",
    "total_offers_received","total_mobile_offer","total_email_offer","total_social_offer",
    "total_web_offer","total_offers_bogo","total_offers_discount","total_offers_informational",
]

# Colunas endógenas (temos controle)
endogenous_cols = [
    "offer_received_date", "channel_mobile", "channel_email", "channel_social",
    "channel_web", "discount_value", "offer_duration", "offer_min_value"
]
endogenous_cat_cols = ["offer_type"]

# Colunas exógenas (externas, não temos controle)
exogenous_cols = [
    "recently_viewed_info_offer","age","credit_card_limit","total_transactions","avg_amount",
    "most_used_offer_type","transactions_offer_rate","avg_time_to_use_offer","avg_time_to_view_offer",
    "all_coupon_usage_rate","pct_used_channel_mobile","pct_used_channel_email","pct_used_channel_social",
    "pct_used_channel_web","pct_used_type_bogo","pct_used_type_discount","pct_used_type_informational",
    "all_coupon_viewed_rate","pct_viewed_channel_mobile","pct_viewed_channel_email","pct_viewed_channel_social",
    "pct_viewed_channel_web","pct_viewed_type_bogo","pct_viewed_type_discount","pct_viewed_type_informational",
    "total_offers_received","total_mobile_offer","total_email_offer","total_social_offer",
    "total_web_offer","total_offers_bogo","total_offers_discount","total_offers_informational"
]

def get_all_joblib(folder_path:str="") -> list:
    """Carrega todos os arquivos joblib de uma pasta"""
    files = os.listdir(folder_path)

    models = {}

    for file in files:
        # Número do cluster
        cl = int(file.replace(".joblib","").split("cl")[-1])
        # Carregando o modelo
        models[cl] = load(f"{folder_path}/{file}")

    return models

def modify_features(X, mod:dict):
    """Modifica os dados da tabela de acordo com o que estiver definido no dicionário de modificações"""
    mod_X = X.copy()

    for k, v in mod.items():
        if v == 1: mod_X[k] = 1
        elif v == 0: mod_X[k] = 0
        elif v == "low":
            # Obtendo limites da coluna atual
            minv, maxv = int(mod_X[k].min()*100), int(mod_X[k].max()*100)
            # Gerando valores aleatórios
            possible_values = [n / 100 for n in list(range(minv, maxv, 100))]
            mod_values = choices(possible_values, weights=[100/2**i for i in range(len(possible_values))], k=len(mod_X))
            # Definindo valores
            mod_X[k] = mod_values
        elif v == "high":
            # Obtendo limites da coluna atual
            minv, maxv = int(mod_X[k].min()*100), int(mod_X[k].max()*100)
            # Gerando valores aleatórios
            possible_values = [n / 100 for n in list(range(maxv, minv, -100))]
            mod_values = choices(possible_values, weights=[100/2**i for i in range(len(possible_values))], k=len(mod_X))
            # Definindo valores
            mod_X[k] = mod_values
        elif v == "keep": continue


    return mod_X
