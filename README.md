# Identify similar images

# How to use
## the input of the code
1. the the folder path of your project
2. num_of_del(If the same type of image is less than this value, all of them will be deleted)
3. threshold(If tow picture's Similarity more than the threshold,they will be considered as the same picture)

## the struct of the input folder
```
id01
├── rgb
│   ├── 1.bmp
│   ├── 2.bmp
│   └── 3.bmp
id02
├── rgb
│   ├── 1.bmp
│   ├── 2.bmp
│   └── 3.bmp
id03
├── rgb
│   ├── 1.bmp
│   ├── 2.bmp
│   └── 3.bmp
id04
├── rgb
│   ├── 1.bmp
│   ├── 2.bmp
│   └── 3.bmp
id05
├── rgb
│   ├── 1.bmp
│   ├── 2.bmp
│   └── 3.bmp
```
> if you want to classify the picture under ./id01/rgb ,the input folder should be ./id01, the name of the picture is random, but it should be xxx.bmp，if your picture is xxx.jpg or others, you can edit the code in app.py，change
```
all_images = [os.path.join(rgb_folder, f) for f in os.listdir(rgb_folder) if f.endswith('.bmp')]
```
> to 
```
all_images = [os.path.join(rgb_folder, f) for f in os.listdir(rgb_folder) if f.endswith('.jpg')]
```
> or the format of your picture
## the output of the code

the output of the code is a folder, the structure is like this:
```
id01_1
├── rgb
│   ├── 1.bmp
│   ├── 2.bmp
│   └── 3.bmp
id01_2
├── rgb
│   ├── 4.bmp
│   ├── 5.bmp
│   └── 6.bmp
id01_3
├── rgb
│   ├── 7.bmp
│   ├── 8.bmp
│   └── 9.bmp
id01_4
├── rgb
│   ├── 10.bmp
│   ├── 11.bmp
```
> the folder id01_1 is under the folder id01, and the folder id01_2 is under the folder id01, and so on. The picture under ./id01_1/rgb is the same picture, and the picture under ./id01_2/rgb is the same picture, and so on.

## app.py
1. Before you run the code, you should firstly install related libraries
2. Modify the folder path as attached on line 108
3. Run the code and input '1', and the code will compute the similarity between the first picture and others, and it will return a recommended threshold.
4. Modify the threshold as attached on line 110, you can use the recommended threshold or modify it by yourself.
5. Modify the num_of_del as needed
6. Run the code and input 'enter', and then the code will return the result under the '/folder path'

## rename.py
> this code is used to rename the folders. When you use app.py to classify the pictures, maybe you will find the picture under id01_1/rgb and id01_2/rgb are the same, so you should move them into one folder and delete the other folder. This action will lead the folder name unordered, so you should use this code to rename the folders.
1. Modify the folder path as attached on line 46
2. change the number 'a' as attached on line 47
3. Run the code
> the name of the folder will be changed as id'a'_1, id'a'_2, id'a'_3, and so on.


## Use the related libraries:
>
> PIL
>
> matplotlib
