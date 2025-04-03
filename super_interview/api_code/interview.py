import requests
import json


def handle_interview(interview_type, job, difficulty, file_id):
    # 请求头配置
    headers = {
        'Authorization': 'Bearer pat_bDIK2ROhVuTMWnYWpjVNIRFhaMGeZbm860mAOw09SkrFWGQnKbmLHR0RoczCYs1N',
        'Content-Type': 'application/json',
    }
    resume_value = json.dumps({"file_id": file_id})
    # 请求体配置
    payload = {
        'workflow_id': '7488669847939104809',
        'parameters': {
            'type': interview_type,
            'difficulty': difficulty,
            'job': job,
            'file_id': resume_value
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
        question_data = json.loads(data_json)
        question = question_data['output']
        question_list = []

        # 分割不同题目（按三级标题分割）
        questions = question.split('### ')[1:]  # 跳过第一个空元素

        for q in questions:
            try:
                # 提取标题和内容
                lines = q.strip().split('\n', 1)  # 分割标题和内容
                if len(lines) < 1:
                    continue

                # 构造问题字典
                question_dict = {
                    "title": lines[0].strip(),
                    "content": lines[1].strip() if len(lines) > 1 else ""
                }

                question_list.append(question_dict)
            except Exception as e:
                print(f"解析问题时出错：{str(e)}")
                continue
        # print(question_list)
        return question_list

