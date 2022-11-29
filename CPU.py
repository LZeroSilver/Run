import turtle
import psutil


"""
psutil은 cpu사용량 %를 알려주는 모듈
psutil.cpu_percent(2)는 % 출력. float을 출력값으로 반환한다.
(2초 동안의 cpu 사용량을 %로 나타낸...)
(cpu는 특정 시간동안의 사용량으로 계산하는 듯. 특정 시간동안의 사용량에 대해 조사 요망)
"""


a = psutil.cpu_percent(2)
print(a)


"""
해당 코드를 돌려본 결과 2 전후로 %가 나오는 경향성 발견,
사용량% 2을 기준으로 속도를 두 부분으로 나눔. (영상 재생 여부)
터틀의 속도는 int형, 0이 가장 빠르고(이미 그림이 완성될 정도로), 1이 가장 느린.
print(a)를 통해 실제 사용량이 나온다. 또한 무한 루프를 통해 터틀은 계속해서 회전.
실제 사용량과 속도를 알 수 있을 것이다.
"""

if a<2:
    b=1
else:
    b=0

turtle.speed(b)
while True:
    turtle.circle(100)


"""
pip install psutil   : psutil 설치

당시에 크롬을 통해 열려 있던 창
https://www.geeksforgeeks.org/how-to-get-current-cpu-and-ram-usage-in-python/
https://jvvp.tistory.com/1044
cpu,ram 관련 코드 작성에 도움된, psutil 관련 영문, 한글 설명 웹페이지
"""
