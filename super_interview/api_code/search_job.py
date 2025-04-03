import requests
import json


def handle_job_data(job_name, city, education, salaryMin, workExperience):
    # 参数转换与默认值
    try:
        education = int(education) if education else 6
        salaryMin = int(salaryMin) if salaryMin else 0
        workExperience = int(workExperience) if workExperience else 1
    except ValueError:
        print("参数类型转换失败")
        return

    # 请求头配置
    headers = {
        'Authorization': 'Bearer pat_bDIK2ROhVuTMWnYWpjVNIRFhaMGeZbm860mAOw09SkrFWGQnKbmLHR0RoczCYs1N',
        'Content-Type': 'application/json',
    }

    # 请求体配置
    payload = {
        'workflow_id': '7486396723792674827',
        'parameters': {
            'job_name': job_name,
            'city': city,
            'education': education,
            'salaryMin': salaryMin,
            'workExperience': workExperience,
        },
        'app_id': '7486375465822289971'
    }


    # 发送请求

    response = requests.post(
        "https://api.coze.cn/v1/workflow/run",
        headers=headers,
        # 当使用 data = json.dumps(payload) 时，你需要手动进行 JSON 序列化
        # 并且在发送请求时，你需要将 data 作为参数传递，
        # 同时要设置合适的 Content - Type 头信息来表明数据是 JSON 格式

        # data = json.dumps(payload)
        # json=payload requests 库会自动将 payload 对象转换为 JSON 格式
        json=payload)


    if response.ok:
        # print('请求数据成功')

        res = json.loads(response.text)

        # 提取嵌套的json字符串
        data_json = res['data']

        # 将提取到的json字符串反序列化为字典
        jobs_dic = json.loads(data_json)

        jobs = jobs_dic['output']
        files = ['companyName', 'name', 'salary', 'workCity', 'cityDistrict', 'streetName', 'url']

        if jobs:
            job_lis = []
            # 遍历每个职位的数据
            for job in jobs:
                # 初始化一个空字典
                job_info = {}
                # 遍历要提取的字段
                for file in files:
                    # 得到每个职位里要提取的数据,添加到空字典中
                    job_info[file] = job[file]
                print(job_info)
                job_lis.append(job_info)
            # print(job_lis)
            return job_lis
        else:
            return []
