# STEP 1.프로젝트 설명

본 프로젝트는 nomic-ai 사의 gpt4all 깃 리포지토리를 참고하여, Pyqt5 GUI를 이용해 간단하게 LLM AI모델을 사용할 수 있게 만들었습니다.


# STEP 2.모델 다운로드

Option (1/2). ggml-gpt4all-j 모델
- 상업적 이용 가능
- 성능은 떨어짐
- https://gpt4all.io/models/ggml-gpt4all-j-v1.3-groovy.bin

Option (2/2). ggml-gpt4all-l13b 모델
- 상업적 이용 불가능
- 성능은 좋음
- https://gpt4all.io/models/ggml-gpt4all-l13b-snoozy.bin


# STEP 3.사용 방법

1. requirments.txt 파일 내용을 인스톨합니다. (pip install -r requirements.txt)
2. main.py 파일이 있는 디렉토리로 이동합니다.
3. 다음 명령어를 실행하여 exe 파일을 생성합니다. (pyinstaller -F -w main.py)
4. dist 폴더에 생성된 main.exe 파일을 실행합니다.
5. 질문할 내용 입력하고 Generate 버튼을 누른 후 STEP 2 에서 다운받은 모델 파일을 선택합니다. 
6. End.