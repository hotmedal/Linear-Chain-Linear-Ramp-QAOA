import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("gates_parallel.csv")  # your file

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(1, 1, 1)
sns.lineplot(
    data=df,
    x="n", y="depth",
    hue="p",
    estimator="mean",        # average over k & seed
    errorbar="sd",           # shaded ±1 std over k & seed
    marker="o", palette="tab10", linewidth=3
)

plt.rcParams.update({'font.size': 22})
plt.xlabel("n", fontsize=22)
plt.ylabel("Gate Depth", fontsize=22)

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles[::-1], labels[::-1], title="p", fontsize=20, loc='right', bbox_to_anchor=(1.05, 0.58), framealpha=1)
#plt.legend(title="p", fontsize=18, loc='right', bbox_to_anchor=(1.01, 0.6))
#plt.legend(title="p", bbox_to_anchor=(0.5, 1.08), fontsize=18, loc='upper center', ncol=20) 
plt.grid(True)
plt.xticks(sorted(df["n"].unique()), fontsize=20)
plt.yticks(fontsize=20)
plt.tight_layout()
plt.show()

