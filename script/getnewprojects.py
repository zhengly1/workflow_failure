import requests, json, time


github_token = ''  # set your GitHub token

read_file_path = '../data/results.json'


write_file_path = "../data/new_projects.json"

base_url = 'https://api.github.com/repos/'

headers = {
    'Authorization': f'Bearer {github_token}',
    'Accept': 'application/vnd.github.v3.raw'
}

information = []

with open(read_file_path, 'r', encoding='latin-1') as file:
    data = json.load(file)


items = data['items']
for item in items:
    failed_jobs = []
    workflow_url = base_url + item['name'] + '/actions/runs'

    time.sleep(0.8)

    response = requests.get(workflow_url, headers=headers)

    if response.status_code == 200:
        failed_run_ids = []
        if response.json()['total_count'] > 0:
            information.append({
                'project_name': item['name'],
            })
    else:
            print(f'Failed to retrieve run id. Status code: {response.status_code}')



with open(write_file_path, "w") as json_file:

    json.dump(information, json_file)

print("Data has been saved to", write_file_path)
