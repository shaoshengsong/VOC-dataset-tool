# VOC-dataset-tool
tool :training on your custom dataset with pascal voc
**1 video2img.py**
 从视频文件里抽帧保存成图片

**2 convert2jpg.py **
图片文件格式需要是jpg的，如果是其他格式则需要转换

**3 rename.py**
文件名称需要是VOC的格式的，数字6位，不足6位前面补0

**4 buildtxt.py **
使用标注工具，标注图片会生成的xml文件
此程序是根据自定义设置的比例  生成4个文件


trainval_append.txt 训练和验证集
test_append.txt 测试集
train_append.txt 训练集
val_append.txt 验证集


**5 mergefile.py **
将生成的文件 与 原始文件进行 对应合并

原始的是
test.txt：测试集
train.txt：训练集
val.txt：验证集
trainval.txt：训练和验证集

需要合并的文件是

trainval_append.txt 训练和验证集
test_append.txt 测试集
train_append.txt 训练集
val_append.txt 验证集

执行结果是train_append.txt的文件内容会合并到train.txt中
其他依此类推

**6 create_pascal_tf_record_custom.py**
将VOC格式转换成ft格式文件
解决ImageSets/Main使用哪个文件的问题
这里使用的是
test.txt：测试集
train.txt：训练集
val.txt：验证集
trainval.txt：训练和验证集

	    #examples_path = os.path.join(data_dir, year, 'ImageSets', 'Main',
	    #                            'aeroplane_' + FLAGS.set + '.txt')
	    examples_path = os.path.join(data_dir, year, 'ImageSets', 'Main',
	                                 FLAGS.set + '.txt')

**7  data/pascal_label_map.pbtxt**

这个需要手动更改，

	item {
	  id: 171
	  name: 'custom_class_name'
	}


以上工具可以各自独立运行，根据需要使用。
