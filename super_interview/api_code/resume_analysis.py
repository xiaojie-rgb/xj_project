import requests
import json
import re

def resume(job_name,file_id):

    # 请求头配置
    headers = {
        'Authorization': 'Bearer pat_bDIK2ROhVuTMWnYWpjVNIRFhaMGeZbm860mAOw09SkrFWGQnKbmLHR0RoczCYs1N',
        'Content-Type': 'application/json',
    }
    resume_value = json.dumps({"file_id": file_id})
    # 请求体配置
    payload = {
        'workflow_id': '7486660865895235636',
        'parameters': {
            'job_name': job_name,
            'resume': resume_value,
        },
        'app_id': '7486375465822289971'
    }

    # print(json.dumps(payload, indent=2))


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
        data_json = res['data']
        suggestion = json.loads(data_json)
        suggestions = suggestion['output']
        # print(suggestions)
        return suggestions
