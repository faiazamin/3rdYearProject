import requests, json, time
# from DatabaseFunctions import *
from ProblemManager import *
import base64

ALL_TESTS = get_tests()
API = "https://api.judge0.com/submissions/"
SAFETY_COUNTER = 50

def judge(problemid, language, code):
	global ALL_TESTS
	problemid = str(problemid)
	inputs = ALL_TESTS.get(problemid)[0]
	outputs = ALL_TESTS.get(problemid)[1]
	tokens = []
	for i in range(len(inputs)):
		data = make_data(problemid, language, code, inputs[i], outputs[i])
		result = requests.post(url = "https://api.judge0.com/submissions/?base64_encoded=true", json = data)
		token = json.loads(result.text)["token"]
		tokens.append(token)
	time_limit = int(get_problem_data(problemid).get("timelimit"))
	time.sleep(time_limit + 1)
	result = ""
	print(tokens)
	safety_counter = SAFETY_COUNTER 
	for token in tokens:
		while True:
			safety_counter -= 1
			if(safety_counter == 0):
				result = "JUDGE ABORTED"
				break
			try:
				verdict = requests.get(url = API + token).json()
				if verdict["status"]["description"] == "Processing":
					time.sleep(0.5)
				else :
					result = verdict["status"]["description"]
					break
			except:
				pass
		if result != "Accepted":
			break
	return result

def make_data(problemid, language, code, input_test, output_test):
	language_id = 54
	if language == "C":
		language_id = 50
	elif language == "PYTHON":
		language_id = 21
	memory_limit = int(get_problem_data(problemid).get("memorylimit")) * 1024
	time_limit = int(get_problem_data(problemid).get("timelimit"))
	data = {"source_code": base64.b64encode(code), "language_id": language_id, "number_of_runs": "1","stdin": base64.b64encode(input_test),"expected_output": base64.b64encode(output_test),"cpu_time_limit": time_limit,"cpu_extra_time": "0.1","wall_time_limit": "5","memory_limit": memory_limit,"stack_limit": "64000","max_processes_and_or_threads": "30","enable_per_process_and_thread_time_limit": "false","enable_per_process_and_thread_memory_limit": "true","max_file_size": "1024"}
	return data


def get_problem_data(problemid):
	return {"timelimit" : 2, "memorylimit" : 32}