from mmpose.apis import MMPoseInferencer
import matplotlib.pyplot as plt
import cv2

# 使用模型别名创建推理器
inferencer = MMPoseInferencer("human")

folder_path = "p.jpg"

# 读取图像
image = cv2.imread(folder_path)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# 进行关键点检测
result_generator = inferencer(image, show=False, use_oks_tracking=True)
results = [result for result in result_generator]

# 获取关键点坐标
points = results[0]['predictions'][0][0]['keypoints']

# 显示图像
plt.imshow(image)
plt.axis('off')  # 关闭坐标轴显示

# 绘制关键点并标记编号
for i, point in enumerate(points):
    plt.scatter(point[0], point[1], color='red')  # 绘制关键点
    plt.text(point[0], point[1], str(i+1), fontsize=8, color='red', ha='right')  # 标记编号

plt.title('带编号的关键点图')
plt.show()
