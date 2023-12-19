import matplotlib.pyplot as plt
import numpy as np

# 创建一个随机数列
data = np.random.randn(1000)

# 直方图
plt.hist(data, bins=30)
plt.title('Histogram')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()

# 线图
plt.plot(data)
plt.title('Line Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()

# 散点图
x = np.random.randn(1000)
y = np.random.randn(1000)
plt.scatter(x, y)
plt.title('Scatter Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()