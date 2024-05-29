from mmpose.apis import MMPoseInferencer
import matplotlib.pyplot as plt
import cv2
from mpl_toolkits.mplot3d import Axes3D

# 使用模型别名创建推理器
inferencer = MMPoseInferencer(pose3d = "human3d")

folder_path = "fall.jpg"

# 读取图像
image = cv2.imread(folder_path)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# 进行关键点检测
result_generator = inferencer(image, show=False, use_oks_tracking=True)
results = [result for result in result_generator]

# 获取关键点坐标
points = results[0]['predictions'][0][0]['keypoints']

# 创建 3D 图形
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 绘制点并标记编号
for i, point in enumerate(points):
    ax.scatter(point[0], point[1], point[2])
    ax.text(point[0], point[1], point[2], str(i+1), fontsize=12, ha='right')

# 设置坐标轴标签
ax.set_xlabel('X轴')
ax.set_ylabel('Y轴')
ax.set_zlabel('Z轴')
plt.axis('equal')
# 显示图形
plt.title('带编号的三维点图')
plt.show()