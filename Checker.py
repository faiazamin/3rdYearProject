import requests, json, time

all_tests = {}
API = "https://api.judge0.com/submissions/"
SAFETY_COUNTER = 50

def judge(problemid, language, code):
	global all_tests
	inputs = all_tests.get(problemid)[0]
	outputs = all_tests.get(problemid)[1]
	tokens = []
	for i in range(len(inputs)):
		data = make_data(problemid, language, code, inputs[i], outputs[i])
		result = requests.post(url = API, json = data)
		token = json.loads(result.text)["token"]
		tokens.append(token)
	time_limit = int(get_problem_data(problemid).get("time_limit"))
	time.sleep(time_limit + 1)
	result = ""
	safety_counter = SAFETY_COUNTER 
	for token in tokens:
		while True:
			safety_counter -= 1
			if(safety_counter == 0):
				result = "JUDGE ABORTED"
				break
			verdict = requests.get(url = API + token).json()
			if verdict["status"]["description"] == "Processing":
				time.sleep(0.5)
			else :
				result = verdict["status"]["description"]
				break
		if result != "Accepted":
			break
	# result is stored in result
	print(result)

def make_data(problemid, language, code, input_test, output_test):
	language_id = 54
	if language == "C":
		language_id = 50
	elif language == "PYTHON":
		language_id = 21
	memory_limit = int(get_problem_data(problemid).get("memory_limit")) * 1024
	time_limit = 	get_problem_data(problemid).get("time_limit")
	data = {"source_code": code, "language_id": language_id, "number_of_runs": "1","stdin": input_test,"expected_output": output_test,"cpu_time_limit": time_limit,"cpu_extra_time": "0.1","wall_time_limit": "5","memory_limit": memory_limit,"stack_limit": "64000","max_processes_and_or_threads": "30","enable_per_process_and_thread_time_limit": "false","enable_per_process_and_thread_memory_limit": "true","max_file_size": "1024"}
	return data

def get_problem_data(problemid):
	return {"memory_limit" : 32, "time_limit" : 1}

if __name__ == "__main__":
	code = ""
	with open("problem/1/test.cpp") as file:
		code = file.read()
	inputs = []
	outputs = []
	for i in range(1, 6):
		with open("problem/1/input/" + str(i)) as file:
			inputs.append(file.read())

	for i in range(1, 6):
		with open("problem/1/output/" + str(i)) as file:
			outputs.append(file.read())

	global all_tests
	all_tests["1"] = [inputs, outputs]
	judge("1", "C++", code)