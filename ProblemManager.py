import os

def get_str_from_file(filename):
	retstr = ""
	with open(filename) as file:
		retstr = file.read()
	return retstr

def get_tests():
	files_dict = {}
	for folder, sub_folder, file  in os.walk('problem'):
		files_dict[folder] = file
	# return dict
	retdict = {}
	# for problem in problems:
	for problem in list(os.walk('problem'))[0][1]:
		inputs = []
		outputs = []
		for file in files_dict["problem/" + problem + '/input']:
			string = get_str_from_file("problem/" + problem + '/input/' + file)
			inputs.append(string)
		for file in files_dict["problem/" + problem + '/output']:
			string = get_str_from_file("problem/" + problem + '/output/' + file)
			outputs.append(string)
		retdict[problem] = [inputs, outputs]
	return retdict