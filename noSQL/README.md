# NoSQL 이해
-   Not only SQL
-   RDBMS의 한계를 극복하기 위해 만들어진 새로운 형태의 데이터저장소
-   RDBMS처럼 고정된 스키마 및 JOIN 이 존재하지 않음
-   스키마 변경? ALERT 등 필요 없음
![nosql] (https://user-images.githubusercontent.com/73468962/148645995-1bbbc8fb-a042-4d75-af05-a4ee8fdebfa8.png)



# Why NoSQL?

-   RDBMS를 기본으로 사용하지만,
-   초당 데이터가 수십만개씩 쌓이는 서비스가 많아지면서(쇼셜, 온라인 서비스등), NoSQL을 사용하는 경우가 많아지고 있음
    
-   경험적 수치
    
    -   95% read, 5% write 경우는 RDBMS 가 성능이 나쁘지 않음
    -   50% write > 인 경우 RDBMS는 성능 저하 또는 불안정
    -   NoSQL + Redis (In memory cache) 등을 고려하게 됨

-   NoSQL 데이터베이스는 각 데이터베이스마다 기반으로 하는 데이터 모델이 다르므로, 데이터 모델별로 대표적인 데이터베이스를 알아둘 필요가 있음
    -   각기 데이터베이스 다루는 인터페이스가 다름
        -   Key/Value Store
        -   Wide Column Store
        -   Document Store

##  mongoDB 란?

-   mongoDB는 document db
    -   JSON 기반의 Document 기반 데이터 관리

- MongoDB Document 예)

		{
		    "_id": ObjectId("5099803df3f42312312391"),
		    "username": "davelee",
		    "name": { first: "Dave", last: "Lee" }
		}

## MongoDB 데이터 구조

- Database - Collection(table대신) - Document(low 대신에. column이라는 개념이 없다.)

-   RDBMS의 table이 아니라, collection 에 JSON 형태의 Document를 넣습니다.
-   Document 하나가 하나의 로우(레코드)임

![nosql] (https://user-images.githubusercontent.com/73468962/148645993-eb214ba5-3afb-4973-bb2c-f4889e79a8e5.png)

#### MongoDB Database[](https://www.fun-coding.org/mongodb_basic1.html#MongoDB-Database)

-   Database는 Collection의 집합

#### MongoDB Collection[](https://www.fun-coding.org/mongodb_basic1.html#MongoDB-Collection)

-   Collection은 MongoDB Document의 집합
-   RDBMS Table과 유사한 개념, 단 정규화된 데이터 구조, 즉 Schema가 정의되어 있지 않음

## mongoDB 설치 및 환경 구축

## **1. 설치 하기**

설치 링크 :  [www.mongodb.com/try/download/enterprise](https://www.mongodb.com/try/download/enterprise)

계속 next 누르다가 MongoDB Compass Install는 선택.

## **2. 환경 구축**
환경 변수 -> path로 가서
설치된 MongoDB의 bin폴더 경로를 입력
이후 cmd창에 mongodb --version을 입력하여 정상 설치 확인

이후 MongoDB Compass를 실행하여 정상적으로 MongoDB에 접속이 되는지 확인
NewConnection에서 접속 할 mongodb://localhost:27017/mydbname 를 입력하여 CONNECT를 진행
여기 까지 정상적으로 완료되면 끝!
