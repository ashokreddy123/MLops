import csv,os
import shutil
root_folder = "/home/ubuntu/keras-retinanet/output_datagen/ust_data/data_apr_23_all"
copy_folder = "/home/ubuntu/keras-retinanet/output_datagen/ust_data/data_apr_23_all_balanced"

anno_path = "/home/ubuntu/keras-retinanet/output_datagen/ust_data/annotations_apr_23_all_balanced.csv"

anno_read = csv.reader(open(anno_path),delimiter=',')

for row in anno_read:
	file = row[0].split('/')[-1]
	print(file)
	file_path = os.path.join(root_folder,file)
	shutil.copy(file_path,copy_folder)
	"""
	for key in classes_dict.keys():
		if(row[5]==key):
			classes_dict[key] += 1
	"""