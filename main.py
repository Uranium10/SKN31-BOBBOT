import os
import requests
from bs4 import BeautifulSoup

# DISCORD WEBHooK
WEBHOOK_URL = os.environ.get("DISCORD_WEBHOOK_URL")

# 더좋은 밥상 카카오톡 채널
CHANNEL_URL = "https://pf.kakao.com/_xfWxfCxj"

def get_menu_image():
    try:
        # 홈페이지 요청
        response = requests.get(CHANNEL_URL)
        response.raise_for_status()

        # HTML 파싱
        soup = BeautifulSoup(response.text, 'html.parser')

        # 메타 태그에서 og:image 추출
        meta_image = soup.find("meta", property="og:image")

        if meta_image and meta_image.get("content"):
            return meta_image["content"]
        else:
            return None
    except Exception as e:
        print(f"이미지 파싱 중 오류 발생: {e}")
        return None

def send_to_discord(img):
    if not WEBHOOK_URL:
        print("디스코드 webhook url을 설정해주세요")
        return
    # 디스코드 메세지 페이로드
    data = {
        "content": "",
        "embeds": [
            {
                "image":{
                    "url": img
                }
            }
        ]
    }

    response = requests.post(WEBHOOK_URL, json=data)

    if response.status_code == 204:
        print("식단 전송 완료")
    else:
        print(f"식단 전송 실패 {response.status_code}")

if __name__ == "__main__":
    img = get_menu_image()
    if img:
        send_to_discord(img)