
import os

def rename_files():
	file_list = os.listdir("prank")
	saved_path = os.getcwd()
	os.chdir("prank")

	for file_name in file_list:
		print("Old Name: " + file_name)
		print("New Name: " + file_name.translate(None, "0123456789"))
		#os.rename(file_name, file_name.translate(None, "0123456789"))

	os.chdir(saved_path)

rename_files()
print(os.getcwd())