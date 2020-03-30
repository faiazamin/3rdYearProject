import json,requests

judge_language = {"C++" : "54", "PYTHON" : "71", "PYTHON2" : "70", "C" : "50", "JAVA" : "62"}



data = {"source_code": code, "language_id": language_id, "number_of_runs": "1","stdin": input_text,"expected_output": output_text,"cpu_time_limit": time_limit,"cpu_extra_time": "0.5","wall_time_limit": "5","memory_limit": memory_limit,"stack_limit": "64000","max_processes_and_or_threads": "30","enable_per_process_and_thread_time_limit": "false","enable_per_process_and_thread_memory_limit": "true","max_file_size": "1024"}