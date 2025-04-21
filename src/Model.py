import pandas as pd
import numpy as np

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, log_loss, confusion_matrix

# Modelos de classificação
from catboost import CatBoostClassifier

class Model:
    def __init__(self, modeling_dict:dict):
        # Modelo
        self.model:CatBoostClassifier = modeling_dict["model"]

        # Dados
        self.metrics = modeling_dict["metrics"]
        self.metrics_full_table = modeling_dict["metrics_full_table"]
        self.params = modeling_dict["params"]

        # Bases
        self.X_train = modeling_dict["X_train"]
        self.y_train = modeling_dict["y_train"]
        self.X_train_bal = modeling_dict["X_train_bal"]
        self.y_train_bal = modeling_dict["y_train_bal"]
        self.X_val = modeling_dict["X_val"]
        self.y_val = modeling_dict["y_val"]
        self.X_val_bal = modeling_dict["X_val_bal"]
        self.y_val_bal = modeling_dict["y_val_bal"]

    def predict(self, X:pd.DataFrame):
        """Realize uma predição"""
        return self.model.predict(X)

    def calculate_pred_metric(self, X:pd.DataFrame, y):
        """"Calcula métricas predefinidas, retornando-as em forma de dicionario"""
        # Gerando predição
        pred = self.predict(X)
        # Retornando métricas
        return {
            "precision": precision_score(y, pred),
            "accuracy": accuracy_score(y, pred),
            "recall": recall_score(y, pred),
            "f1": f1_score(y, pred),
            "log_loss": log_loss(y, pred), # Penaliza erros quando a confiança é grande
        }

    def show_confusion_matrix(self, X:pd.DataFrame, y):
        """Apresenta uma matriz de confusão"""
        # Gerando predição
        pred = self.predict(X)
        cm = confusion_matrix(y, pred, normalize=True)
        # Mostrando matriz de confusão
        print(cm)
        return cm
