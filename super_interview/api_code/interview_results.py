import requests
import json


def interview_re(que1, que2, que3, que4, que5, ans1, ans2, ans3, ans4, ans5):
    # 请求头配置
    headers = {
        'Authorization': 'Bearer pat_bDIK2ROhVuTMWnYWpjVNIRFhaMGeZbm860mAOw09SkrFWGQnKbmLHR0RoczCYs1N',
        'Content-Type': 'application/json',
    }
    # 请求体配置
    payload = {
        'workflow_id': '7488718105133187098',
        'parameters': {
            'que1': que1,
            'que2': que2,
            'que3': que3,
            'que4': que4,
            'que5': que5,
            'ans1': ans1,
            'ans2': ans2,
            'ans3': ans3,
            'ans4': ans4,
            'ans5': ans5,
        },
        'app_id': '7486375465822289971'
    }

    # 发送请求

    response = requests.post(
        "https://api.coze.cn/v1/workflow/run",
        headers=headers,
        json=payload)

    if response.ok:
        # print('请求数据成功')
        res = json.loads(response.text)
        data_json = res['data']
        results_data = json.loads(data_json)
        results = results_data['output']
        # print(results)
        return results


