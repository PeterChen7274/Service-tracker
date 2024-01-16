# taskapp/utils.py
import requests
import json

#钉钉提醒，可以修改message参数改变通知信息
def send_dingtalk_message(task, message):
    url = task.ding

    headers = {'Content-Type': 'application/json;charset=utf-8'}

    data = {
        "msgtype": "text",
        "text": {
            "content": message
        }
    }

    response = requests.post(url, data=json.dumps(data), headers=headers)
    
    if response.status_code == 200:
        print("Message sent successfully.")
    else:
        print(f"Failed to send message. Status code: {response.status_code}, Response: {response.text}")
