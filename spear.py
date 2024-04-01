import pandas as pd

df = pd.read_csv("cardio_base.csv")

spearman_corr_matrix = df.corr(method='spearman')

abs_spearman_corr = spearman_corr_matrix.abs().unstack().sort_values(ascending=False)

abs_spearman_corr = abs_spearman_corr[abs_spearman_corr.index.get_level_values(0) != abs_spearman_corr.index.get_level_values(1)]

highest_corr_features = abs_spearman_corr.idxmax()

print("Two features with highest Spearman rank correlation coefficient:")
print(highest_corr_features)
