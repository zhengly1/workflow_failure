import requests, json, time


github_token = ''  # set your GitHub token

read_file_path = '../data/java_failed_run_ids.json'


write_file_path = "../data/java_failed_job_information.json"

base_url = 'https://api.github.com/repos/'

headers = {
    'Authorization': f'Bearer {github_token}',
    'Accept': 'application/vnd.github.v3.raw'
}

information = []

with open(read_file_path, 'r') as file:
    data = json.load(file)

for item in data:
    failed_jobs = []
    for run_id in item['run_id']:
        run_url = base_url + item['project_name'] + '/actions/runs/' + str(run_id) + '/jobs'

        time.sleep(0.8)

        response = requests.get(run_url, headers=headers)

        if response.status_code == 200:
            if response.json()['total_count'] > 0:
                jobs = response.json().get('jobs', [])
                for job in jobs:
                    if job['conclusion'] == 'failure':
                        for step in job['steps']:
                            if step['conclusion'] == 'failure':
                                failed_jobs.append({
                                    "run_id": job['run_id'],
                                    "job_id": job['id'],
                                    "job_name": job['name'],
                                    "workflow_name": job['workflow_name'],
                                    "url": 'https://github.com/' + item['project_name'] + '/actions/runs/' + str(
                                        run_id) + '/job/' + str(job['id']),
                                    "step": step['name'],
                                    "time": job['created_at'],
                                    "labels": job['labels']
                                }
                                )
        else:
            print(f'Failed to retrieve job id. run url:{run_url}')
    if len(failed_jobs) != 0:
        information.append({
            'project_name': item['project_name'],
            'failed_jobs': failed_jobs,
        })
    # print(information)


with open(write_file_path, "w") as json_file:
    json.dump(information, json_file)

print("Data has been saved to", write_file_path)
