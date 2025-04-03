import json

import requests
from werkzeug.utils import secure_filename


def upload(uploaded_file):
    headers = {
        'Authorization': 'Bearer pat_bDIK2ROhVuTMWnYWpjVNIRFhaMGeZbm860mAOw09SkrFWGQnKbmLHR0RoczCYs1N',
    }

    # 安全处理文件名
    filename = uploaded_file.filename

    # 构造符合要求的 files 参数
    # uploaded_file.stream 是文件流对象，不是直接内容，但可通过流操作按需读取。
    # 在调用外部 API 时，直接传递流更高效（尤其是大文件）。
    files = {
        'file': (filename, uploaded_file.stream)
    }

    response = requests.post(
        'https://api.coze.cn/v1/files/upload',
        headers=headers,
        files=files
    )
    res = json.loads(response.text)
    # print(res)
    data = res['data']
    id = data['id']
    return id