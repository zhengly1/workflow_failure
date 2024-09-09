import requests, json, time, os, shutil


github_token = ''  # set your GitHub token

read_file_path = '../data/java_failed_job_information.json'

base_url = 'https://api.github.com/repos/'

headers = {
    'Authorization': f'Bearer {github_token}',
    'Accept': 'application/vnd.github.v3.raw'
}



with open(read_file_path, 'r') as file:
    data = json.load(file)

for item in data:
    failed_jobs = []

    folder_name = item['project_name'].replace("/", "__")
    if os.path.exists('java/' + folder_name):
        continue
    else:
        os.mkdir('java/' + folder_name)
        os.chdir('java/' + folder_name)
        for job_information in item['failed_jobs']:
            job_url = base_url + item['project_name'] + '/actions/jobs/' + str(job_information['job_id']) + '/logs'

            time.sleep(0.8)

            while True:
                try:
                    response = requests.get(job_url, headers=headers)
                    if response.status_code == 200:

                        log_file_name = str(job_information['run_id']) + '_' + str(
                            job_information['job_id']) + '_logs.txt'
                        with open(log_file_name, 'w', encoding='utf-8') as log_file:
                            log_file.write(response.text)
                        break
                    else:
                        print(f'Failed to retrieve job log. job url:{job_url}')
                        break
                except Exception as e:

                    print(f"发生了一个异常：{e}")
                    time.sleep(1.5)

        if len(os.listdir('java/' + folder_name)) == 0:
            shutil.rmtree('java/' + folder_name)
            print('delete java/' + folder_name)

