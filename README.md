Face_Recognition
===================================================
- First Version (Simple Face Detection & Recognition)

개발환경 구축
---------------------------------------------------
- python3 version(Anaconda3 추천) 설치 필수
- 필요 패키지 설치
  - (https://ukayzm.github.io/python-face-recognition/) 참고
  - dlib 라이브러리 설치 전에 Linux와 MacOS의 경우 CMake 설치 필요
  <pre><code>pip install CMake</code></pre>
  - dlib 라이브러리 설치 전에 Window의 경우 CMake 설치시 (https://ndb796.tistory.com/365) 참고

  
Version1. 내용
---------------------------------------------------
- knowns 폴더에 가족 구성원의 사진 파일을 저장함
- who 폴더에 누구인지 확인할 사진 파일을 저장 (iuiu.jpeg, Song.png)
- face_recognition1.py 실행시 knowns에서 가족 구성원의 이미지를 가져와 인코딩 값을 저장
- who 폴더에서 아이유, 송중기 사진을 각각 인코딩 한 후 가족구성원의 사진들과 각각 face_distance를 계산
- face_distance를 계산하여 거리가 가장 가까운 가족구성원을 매칭시키고 그 distance가 0.4 미만일 때만 가족구성원의 이름 출력, 0.4 이상이면 Unknown 출력
- 아이유는 Daughter 출력, 송중기는 Unknown 출력된 걸 확인 가능
