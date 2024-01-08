import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 从CSV文件读取数据
data = pd.read_excel('1.xls')

# 计算相关系数矩阵
corr_matrix = data.corr()

# 设置图像尺寸
fig, ax = plt.subplots(figsize=(10, 10))
# 绘制热力图
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f',ax=ax)

# 设置图形属性
# plt.title('Correlation Coefficient Heatmap')
# 设置横纵坐标字体大小
ax.tick_params(axis='x', labelsize=12)  # 设置x轴标签字体大小
ax.tick_params(axis='y', labelsize=12)  # 设置y轴标签字体大小

# 设置纵坐标字体横向排布
ax.set_yticklabels(ax.get_yticklabels(), rotation=0)
# 设置横坐标旋转角度
ax.set_xticklabels(ax.get_xticklabels(), rotation=65)  # 设置x轴标签旋转角度为45度
# 显示图形
plt.savefig('1.png')
plt.show()
