import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

# 创建一个随机DataFrame
df = pd.DataFrame({
    'x': np.random.randn(1000),
    'y': np.random.randn(1000),
    'z': np.random.randn(1000)
})

# 直方图
sns.histplot(data=df, x="x", kde=True)
plt.show()

# 散点图
sns.scatterplot(data=df, x="x", y="y")
plt.show()

# 热力图
corr = df.corr()
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.show()