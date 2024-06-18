# import torch
# from torchvision import transforms
# from PIL import Image
#
# # 创建一个示例张量
# tensor = torch.randint(0, 256, (3, 124, 124), dtype=torch.uint8)
#
# # 确保张量的值在 [0, 255] 范围内，并且类型为 uint8
# # 如果你的张量已经满足这些条件，可以跳过这一步
# # tensor = tensor.clamp(0, 255).to(torch.uint8)
#
# # 使用 transforms.ToPILImage 转换张量为 PIL.Image
# to_pil = transforms.ToPILImage()
# image = to_pil(tensor)
#
# # 显示图像
# image.show()
#
# # 保存图像（可选）
# # image.save("output_image.png")

import matplotlib.pyplot as plt
from torchvision import datasets, transforms

# 定义数据转换
transform = transforms.ToTensor()

# 加载 CIFAR-100 数据集
dataset = datasets.CIFAR100('data/cifar-100', train=False, download=True, transform=transform)

# 创建一个子图网格来显示前 100 张图像
fig, axes = plt.subplots(nrows=10, ncols=10, figsize=(15, 15))

# 遍历前 100 张图像并显示
for i in range(100):
    image, label = dataset[i]

    # 转换张量为 PIL 图像并显示
    image = transforms.ToPILImage()(image)

    ax = axes[i // 10, i % 10]
    ax.imshow(image)
    ax.axis('off')

plt.tight_layout()
plt.show()

