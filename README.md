# samdul11food

- API에 음식 이름을 query string으로 요청을 보내면 `시간,음식이름`의 형식으로 csv파일에 저장합니다. 
- 시간은 대한민국 표준시(KST)로 저장됩니다.

### Usage
```bash
$ sudo docker pull mingk42/food:v0.2.13
$ sudo docker run -d -p 8011:8080 --name food11  mingk42/food:v0.2.13
```

### Version

- `0.2.13` : 위 기능 구현 완료

### Dependency

![FastAPI](https://img.shields.io/badge/fastapi-009688.svg?style=for-the-badge&logo=fastapi&logoColor=FFFFFF)