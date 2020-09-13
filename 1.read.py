import os
import aip

APP_ID = '19699484'
API_KEY = 'qhcEWPTqlNG8mptj7DXOztuU'
SECRET_KEY = 'eXLBGpZ85eUohDaU1tgMDR9PViiqhSQL'
client = aip.AipSpeech(APP_ID, API_KEY, SECRET_KEY)

def main():
    global client
    result = client.synthesis('比如 nvidia broadcast', 'zh', 1, {
        'vol': 5,
        'per': 0,
    })

    # 识别正确返回语音二进制 错误则返回dict 参照下面错误码
    if not isinstance(result, dict):
        with open('audio.mp3', 'wb') as f:
            f.write(result)

if __name__ == '__main__':
    main()