1.Origin_data文件夹里面存放的是原始的未经过处理的LAP-14和三个Rest数据集

2. Processed_data文件夹里面存放的是经过处理的数据
其中，
（1）几个test_data是使用Data_Process.py进行程序处理（不执行拆分的程序）之后，再手动将“空格回车空格”替换为"回车符号"，
（2）real_train和real_valid数据集是使用Data_Process.py进行程序处理，再手动将“空格回车空格”替换为"回车符号"，
