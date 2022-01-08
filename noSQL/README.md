# md파일 편집 사이트
https://stackedit.io/app#

# NoSQL 이해
-   Not only SQL
-   RDBMS의 한계를 극복하기 위해 만들어진 새로운 형태의 데이터저장소
-   RDBMS처럼 고정된 스키마 및 JOIN 이 존재하지 않음
-   스키마 변경? ALERT 등 필요 없음
###
![nosql](https://user-images.githubusercontent.com/73468962/148645995-1bbbc8fb-a042-4d75-af05-a4ee8fdebfa8.png)



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

###
![nosql](https://user-images.githubusercontent.com/73468962/148645993-eb214ba5-3afb-4973-bb2c-f4889e79a8e5.png)

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

## mongoDB 데이터베이스 생성 및 삭제
**1. 몽고DB 생성**  

> use "몽고DB이름"

  

**2. Collection 생성 (table이랑 같은 개념인듯)**

> db.createCollection("컬렉션이름")

  

**3. createCollection 사용 없이 Document 생성 방법**

> db.생성할컬렉션이름.insert({"키값": "벨류"})

  

**4. 몽고DB 삭제**

> use "삭제할DB이름"

> db.dropDatabase();

  

**5. Collection 삭제**

> db.삭제할컬렉션이름.drop()


![ffff](https://velopert.com/wp-content/uploads/2016/02/ffff.png)

## Database 생성: _use_

_use DATABASE_NAME_ 명령어를 통하여 Database를 생성 할 수 있습니다.  
생성 후, 생성된 데이터베이스를사용하게 되구요, 데이터베이스가 이미 존재하는 경우엔 현존하는 데이터베이스를 사용합니다.

**예제:** mongodb_tutorial 이라는 데이터베이스를 생성합니다.

> use mongodb_tutorial
switched to db mongodb_tutorial

현재 사용중인 데이터베이스를 확인하려면 _db_  명령어를 입력하세요.

> db
mongodb_tutorial

내가 만든  **데이터베이스 리스트들을 확인**하려면 _show dbs_ 명령어를 입력하세요.

> show dbs
local  0.000GB

리스트에서 방금 만든 데이터베이스를 보려면 최소 한개의 Document를 추가해야합니다.

> db.book.insert({"name": "MongoDB Tutorial", "author": "velopert"});

WriteResult({ "nInserted" : 1 })
> show dbs
local             0.000GB
mongodb_tutorial  0.000GB

* 여기서 book 은 Collection 입니다. 따로 Collection 을 미리 생성하지 않아도  
위처럼 명령어를 작성하는데 차질이 없습니다.

## Database 제거: _db.dropDatabase()_

Database를 제거할땐  _db.dropDatabase()_  명령어를 사용합니다.

이 명령어를 사용하기 전, _use DATABASE_NAME_ 으로 삭제하고자 하는 데이터베이스를 선택해줘야합니다.

**예제:** mongodb_tutorial 데이터베이스를 제거합니다.

> use mongodb_tutorial
switched to db mongodb_tutorial
> db.dropDatabase();
{ "dropped" : "mongodb_tutorial", "ok" : 1 }

## Collection 생성:  _db.createCollection()_

Collection을 생성할때는  _db.createCollection(name, [options])_  명령어를 사용합니다.

_name_ 은 생성하려는 컬렉션의 이름이며 _option_  은 document 타입으로 구성된 해당 컬렉션의 설정값입니다.  
options 매개변수는 선택적인(Optional) 매개변수로서 생략하셔도 되고, 필요에따라 사용하면 됩니다.

**Option:**  
  
|Field|Type|설명|
 |---|---|---|
 |capped|Boolean|이 값을 true 로 설정하면 capped collection 을 활성화 시킵니다. Capped collection 이란, 고정된 크기(fixed size) 를 가진 컬렉션으로서, size 가 초과되면 가장 오래된 데이터를 덮어씁니다. **이 값을 true로 설정하면 size 값을 꼭 설정해야합니다.**|
 |autoIndex|Boolean|이 값을 true로 설정하면, _id 필드에 index를 자동으로 생성합니다. 기본값은 false 입니다.|
 |size|number|Capped collection 을 위해 해당 컬렉션의 최대 사이즈(maximum size)를 ~ bytes로 지정합니다.|
 |max|number|해당 컬렉션에 추가 할 수 있는 최대 갯수를 설정합니다.|



**예제1 :** test 데이터베이스에 books 컬렉션을 옵션없이 생성합니다.

> use test
switched to db test
> db.createCollection("books")
{ "ok" : 1 }

**예제2:** test 데이터베이스에 articles 컬렉션을 옵션과 함께 생성합니다.

> db.createCollection("articles", {
... capped: true,
... autoIndex: true,
... size: 6142800,
... max: 10000
... })
{ "ok" : 1 }

**예제3:** 따로 createCollection() 메소드를 사용하지 않아도 document를 추가하면 자동으로 컬렉션이 생성됩니다.

> db.people.insert({"name": "velopert"})
WriteResult({ "nInserted" : 1 })

내가 만든  **collection 리스트를 확인**하려면 _show collections_ 명령어를 입력하세요.

> show collections
articles
books
people

## Collection 제거:  _db.COLLECTION_NAME.drop()_

Collection을 제거 할 땐 _drop()_ 메소드를 사용합니다.

당연히, 이 명령어를 제거하기 전, 사용 할 데이터베이스를 우선 설정해야겠죠?

**예제:** test 데이터베이스의 people 컬렉션을 제거합니다.

> use test
switched to db test
> show collections
articles
books
people
> db.people.drop()
true
> show collections
articles
books

## Document 추가: _db.COLLECTION_NAME.insert(document)_

_insert()_  메소드를 사용하여 Document를 추가 할 수 있습니다.

이 명령어를 사용하기 전 데이터를 추가 할 데이터베이스를 선택해주어야합니다.

배열형식의 인자를 전달해주면 여러 다큐먼트를 동시에 추가 할 수 있습니다.

**예제1:** 한개의 다큐먼트를 books 컬렉션에 추가합니다.

> db.books.insert({"name": "NodeJS Guide", "author": "Velopert"})
WriteResult({ "nInserted" : 1 })

**예제2:** 두개의 다큐먼트를 books 컬렉션에 추가합니다. (가독성을 위해 여러줄로 작성되었습니다.)

> db.books.insert([
... {"name": "Book1", "author": "Velopert"},
... {"name": "Book2", "author": "Velopert"}
... ]);
BulkWriteResult({
        "writeErrors" : [ ],
        "writeConcernErrors" : [ ],
        "nInserted" : 2,
        "nUpserted" : 0,
        "nMatched" : 0,
        "nModified" : 0,
        "nRemoved" : 0,
        "upserted" : [ ]
})

**컬렉션의 다큐먼트 리스트를 확인**할때는 _db.COLLECTION_NAME.find()_  명령어를 사용하세요.

> db.books.find()
{ "_id" : ObjectId("56c08f3a4d6b67aafdeb88a3"), "name" : "MongoDB Guide", "author" : "Velopert" }
{ "_id" : ObjectId("56c08f474d6b67aafdeb88a4"), "name" : "NodeJS Guide", "author" : "Velopert" }
{ "_id" : ObjectId("56c0903d4d6b67aafdeb88a5"), "name" : "Book1", "author" : "Velopert" }
{ "_id" : ObjectId("56c0903d4d6b67aafdeb88a6"), "name" : "Book2", "author" : "Velopert" }

## Document 제거: _db.COLLECTION_NAME.remove(criteria, justOne)_

_remove(criteria, justOne)_  메소드를 사용하여 Document를 제거 할 수 있습니다.  
이 메소드에는 두가지의 매개변수가 있는데요,
|parameter|Type|설명|
 |---|---|---|
 |*criteria|document|삭제 할 데이터의 기준 값 (criteria) 입니다. 이 값이 { } 이면 컬렉션의 모든 데이터를 제거합니다.|
 |justOne|boolean|선택적(Optional) 매개변수이며 이 값이 true 면 1개 의 다큐먼트만 제거합니다. 이 매개변수가 생략되면 기본값은 false 로 서, criteria에 해당되는 모든 다큐먼트를 제거합니다.|


이 강좌에선 criteria 에 부분에선 특정 field 의 값이 매칭하는 경우만 배워보도록 하겠습니다. criteria 에 대한 자세한 내용은 다음 강좌에서 다뤄보겠습니다.

다큐먼트 추가 부분에서 _find()_  메소드를 잠깐 사용했었는데, 이 메소드 역시 criteria를 인수로 전달 할 수 있습니다. 다큐먼트를 제거하다가 실수를 하지 않도록 초보일땐, 제거전에는  _find()_ 를 먼저 해서 확인하는걸 습관화하세요.

**예제:** books 컬렉션에서 “name”이 “Book1” 인 다큐먼트를 제거

> db.books.find({"name": "Book1"})
{ "_id" : ObjectId("56c097f94d6b67aafdeb88ac"), "name" : "Book1", "author" : "Velopert" }
> db.books.remove({"name": "Book1"})
WriteResult({ "nRemoved" : 1 })
> db.books.find()
{ "_id" : ObjectId("56c08f3a4d6b67aafdeb88a3"), "name" : "MongoDB Guide", "author" : "Velopert" }
{ "_id" : ObjectId("56c08f474d6b67aafdeb88a4"), "name" : "NodeJS Guide", "author" : "Velopert" }
{ "_id" : ObjectId("56c097f94d6b67aafdeb88ad"), "name" : "Book2", "author" : "Velopert" }
