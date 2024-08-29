from PIL import Image
from multiprocessing import Process
import histogram as htg
import os
import shutil

def calculate_image_similarity(img1_path, img2_path):
    # 打开图片
    img1 = Image.open(img1_path)
    img2 = Image.open(img2_path)

    # 直方图归一化
    img1_htg = htg.regularizeImage(img1)
    img2_htg = htg.regularizeImage(img2)

    # 计算相似度
    similarity = htg.calMultipleHistogramSimilarity(img1_htg, img2_htg)

    return similarity

def view_similar_images(src_folder):
    # 定义图片所在的子文件夹路径
    rgb_folder = os.path.join(src_folder, 'rgb')
    # 获取所有图片文件
    all_images = [os.path.join(rgb_folder, f) for f in os.listdir(rgb_folder) if f.endswith('.bmp')]
    sim = []
    base_image_path = all_images.pop(0)

    for img_path in all_images:
        similarity = calculate_image_similarity(base_image_path, img_path)
        sim.append(similarity)
        if len(sim)>1000:
            break
    print(sim)
    sorted_data = sorted(sim)
    n = len(sorted_data)

    # 计算1/4分位数的位置
    pos = len(sorted_data) - len(sorted_data)*0.12
    print(f"\nRecommended thresholds：{sorted_data[int(pos)]}")

def move_or_delete_images(src_folder,num_of_del,yuzhi):
    # 定义图片所在的子文件夹路径
    rgb_folder = os.path.join(src_folder, 'rgb')

    # 获取所有图片文件
    all_images = [os.path.join(rgb_folder, f) for f in os.listdir(rgb_folder) if f.endswith('.bmp')]

    # 文件夹索引
    folder_index = 1
    # 标记已处理的图片
    processed_images = set()

    while all_images:
        # 取第一张图片
        base_image_path = all_images.pop(0)
        processed_images.add(base_image_path)

        # 创建新文件夹
        new_folder_name = f"{os.path.basename(src_folder)}_{folder_index}"
        new_folder_path = os.path.join(src_folder, new_folder_name)
        new_rgb_folder_path = os.path.join(new_folder_path, 'rgb')
        os.makedirs(new_rgb_folder_path, exist_ok=True)

        # 移动第一张图片到新文件夹
        new_base_image_path = os.path.join(new_rgb_folder_path, os.path.basename(base_image_path))
        shutil.move(base_image_path, new_base_image_path)

        to_move = []
        for img_path in all_images:
            similarity = calculate_image_similarity(new_base_image_path, img_path)
            # print(similarity)
            # print(type(similarity))
            # 0.5有颜色场景
            if similarity > yuzhi:
                # print("============")
                to_move.append(img_path)
                # 强调变化性
                new_base_image_path = img_path
        print(len(to_move))
        if len(to_move) < num_of_del:
            # 如果相似图片小于7，删除这些文件
            for img_path in to_move:
                os.remove(img_path)
                processed_images.add(img_path)
                all_images.remove(img_path)

            # 删除基础图片
            os.remove(os.path.join(new_rgb_folder_path, os.path.basename(base_image_path)))
            processed_images.remove(base_image_path)

            # 删除创建的空文件夹
            # os.rmdir(new_folder_path)
            shutil.rmtree(new_folder_path)
            folder_index -= 1
        else:
            # 移动所有相似图片到新文件夹
            for img_path in to_move:
                shutil.move(img_path, new_rgb_folder_path)
                processed_images.add(img_path)
                all_images.remove(img_path)

        # 更新文件夹索引
        folder_index += 1

    print("classify and delete has finished")
# 目录
src_folder_path = 'the folder path of your project'
num_of_del = 10
yuzhi = 0.89

if __name__ == '__main__':
    # 输入选择
    choose = input("input one to show the Similarity, otherwise to classify and delete:")

    try:
        choose = int(choose)
    except ValueError:
        choose = -1  # 如果输入不是数字，则设为默认值 -1

    if choose == 1:
        view_similar_images(src_folder_path)
    else:
        move_or_delete_images(src_folder_path,num_of_del,yuzhi)

