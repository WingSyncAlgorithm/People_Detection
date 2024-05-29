import pickle
import matplotlib.pyplot as plt

class Person():
    def __init__(self, idx, position):
        self.idx = [idx]
        self.same_person = []
        self.image = []
        self.path = []
        self.previous_position = position
        self.current_position = position
        self.keypoints = []
        self.angles = []
        self.angles_cost = []

    def add_image(self, image):
        self.image.append(image)

    def add_path(self, path):
        self.path.append(path)

    def update_position(self, position):
        self.previous_position = self.current_position
        self.current_position = position

    def connect_same_person(self, person_idx):
        self.same_person.append(person_idx)

# 從 pickle 文件中讀取 Person 物件
with open(R'person_0/1.pickle', 'rb') as f:
    person = pickle.load(f)

# 提取 angles_cost 數據
angles_cost = person.angles_cost

# 繪製圖表
plt.plot(angles_cost)
plt.xlabel('Frame')
plt.ylabel('Angles Cost')
plt.title('Angles Cost over Frames')
plt.show()
