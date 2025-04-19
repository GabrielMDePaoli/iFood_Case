from pyspark.sql import SparkSession
import pyspark
import pyspark.sql.functions as F

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def get_numeric_col_summary(df,
                            col_name:str) -> None:
    # Mostrando valores unicos de cada coluna
    summary = df.select(
        F.min(col_name).alias("min"),
        F.max(col_name).alias("max"),
        F.mean(col_name).alias("mean"),
        F.count(col_name).alias("non_null_count"),
        F.count("*").alias("total_count")
    )

    # Contagem de nulos
    null_count = df.select(
        (F.count("*") - F.count(col_name)).alias("null_count")
    )

    # Quartis e mediana
    quantiles = df.approxQuantile(col_name, [0.25, 0.5, 0.75], 0.01)
    q1, median, q3 = quantiles if quantiles else (None, None, None)

    # Mostrar tudo juntinho (print manual)
    summary_data = summary.collect()[0]
    null_data = null_count.collect()[0]

    print("Statistical summary of column 'credit_card_limit':")
    print(f"Min: {summary_data['min']:,}")
    print(f"Max: {summary_data['max']:,}")
    print(f"Mean: {round(summary_data['mean']):,}")
    print(f"Q1 (25%): {q1:,}")
    print(f"Median (Q2 - 50%): {median:,}")
    print(f"Q3 (75%): {q3:,}")
    print(f"Not null values count: {summary_data['non_null_count']:,}")
    print(f"Null values count: {null_data['null_count']:,}")

def get_values_count(df,
                     col_name:str):
    value_count_df = (df
        .groupBy(col_name)
        .agg(
            F.count("*").alias("count"))
        .withColumn(
            "percentage",
            F.round(F.col("count") * 100 / df.count(), 1))
        .orderBy(F.col("percentage").desc())
    )
    print(value_count_df.show())
    return value_count_df

def show_histogram_plot(df,
                        col_name:str,
                        num_bins:int=10) -> None:
    # Removing null values for the plot
    df_ = df.filter(F.col(col_name).isNotNull())

    # Get minimun and maximun values
    min_val, max_val = df_.selectExpr(f"min({col_name})", f"max({col_name})").first()

    # Calculate number of bins
    bin_width = (max_val - min_val) / num_bins

    # Create columns for each bin
    df__hist = df_.withColumn(
        "bin", F.floor((F.col(col_name) - min_val) / bin_width)
    )

    # Count values in each bin
    bin_counts = df__hist.groupBy("bin").count().orderBy("bin")

    # Trazer os dados para o pandas para plotar
    hist_data = bin_counts.toPandas()

    # Criar labels dos bins (faixa de valores)
    hist_data["bin_label"] = hist_data["bin"].apply(lambda b: f"{min_val + b*bin_width:.0f} - {min_val + (b+1)*bin_width:.0f}")

    # Plotar histograma
    plt.figure(figsize=(10,6))
    plt.bar(hist_data["bin_label"], hist_data["count"], width=0.8)
    plt.xticks(rotation=45)
    plt.xlabel("Faixa de crédito")
    plt.ylabel("Quantidade")
    plt.title("Histograma de credit_card_limit")
    plt.tight_layout()
    plt.show()
