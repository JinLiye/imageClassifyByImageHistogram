import os
import uuid  # 导入uuid模块生成唯一标识符

def rename_subfolders(folder_path, a):
    # 获取文件夹下的所有子文件夹
    subfolders = [f for f in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, f))]

    # 排序子文件夹（可选），确保重命名顺序一致
    subfolders.sort()

    # 批量重命名子文件夹
    for index, subfolder in enumerate(subfolders, start=1):
        unique_suffix = uuid.uuid4().hex[:6]
        new_name = f"id{a}_{index}_{unique_suffix}"  # 新文件夹名称，基于给定数字a和索引
        old_path = os.path.join(folder_path, subfolder)
        new_path = os.path.join(folder_path, new_name)

        # 重命名文件夹
        os.rename(old_path, new_path)
        print(f"已将 '{subfolder}' 重命名为 '{new_name}'")


def del_subfolders(folder_path):
    # 获取文件夹下的所有子文件夹
    subfolders = [f for f in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, f))]

    for subfolder in subfolders:
        old_path = os.path.join(folder_path, subfolder)

        # 找到最后一个下划线的位置并截断名称
        if "_" in subfolder:
            new_name = subfolder.rsplit("_", 1)[0]  # 删除最后一个下划线及其后的内容
            new_path = os.path.join(folder_path, new_name)

            # 检查目标路径是否存在
            if not os.path.exists(new_path):
                os.rename(old_path, new_path)
                print(f"已将 '{subfolder}' 重命名为 '{new_name}'")
            else:
                print(f"无法重命名 '{subfolder}' 为 '{new_name}'，目标路径已存在。")
        else:
            print(f"子文件夹 '{subfolder}' 不包含下划线，跳过重命名。")


# 示例用法
folder_path = 'your folder path'  # 替换为实际文件夹路径
a = 94  # 替换为你的数字

if __name__ == '__main__':
    rename_subfolders(folder_path, a)
    del_subfolders(folder_path)