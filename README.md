# m-pipeline-project
머신러닝 파이프라인 프로젝트
![d drawio](https://user-images.githubusercontent.com/60678531/150493637-9f224f81-c285-45d9-8601-1924fd1a3f17.png)
1. 학습 모델 변경 및 전처리 방법 또는 hyperparameter가 변화시 commit 
2. Jenkins는 학습 코드 변경 인식 train.py 재학습 만약 train.py가 변화하지 않으면 기존에 가지고있던 모델를 fastAPI서버로 배포 
3. 도커 이미지는 도커허브에 push(이것도 코드변화시 도커허브에 저장)
