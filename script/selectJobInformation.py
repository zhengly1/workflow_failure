import os, json

read_file_path = '../data/java_failed_job_information.json'

write_file_path = "../data/selected_java_failed_job_information.json"

with open(read_file_path, 'r') as file:
    data = json.load(file)

current_directory = 'java'
information = []

subdirectories = [d for d in os.listdir(current_directory) if os.path.isdir(os.path.join(current_directory, d))]

for subdirectory in subdirectories:
    name = subdirectory.replace("__", "/")
    project_information = next((item for item in data if item["project_name"] == name), None)
    # print(project_information)
    if project_information:
        subdirectory_path = os.path.join(current_directory, subdirectory)
        files = [f for f in os.listdir(subdirectory_path) if os.path.isfile(os.path.join(subdirectory_path, f))]
        job_ids = [word.split("_")[1] for word in files]
        # print(job_ids)
        for job_id in job_ids:
            job_information = next(
                (item for item in project_information["failed_jobs"] if str(item["job_id"]) == str(job_id)), None)
            if job_information:
                information.append({
                    'project_name': project_information["project_name"],
                    "run_id": job_information['run_id'],
                    "job_id": job_information['job_id'],
                    "job_name": job_information['job_name'],
                    "workflow_name": job_information['workflow_name'],
                    "url": job_information['url'],
                    "step": job_information['step'],
                    "time": job_information['time'],
                    "labels": job_information['labels']
                })

with open(write_file_path, "w") as json_file:
    json.dump(information, json_file)

print("Data has been saved to", write_file_path)
