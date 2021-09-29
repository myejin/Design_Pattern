## :books: Design Pattern

<img width="200" src="https://user-images.githubusercontent.com/42771578/134512989-9a30807c-d5cc-4762-b28a-ea950736c659.png">

### 목차

[1. 싱글톤](#:bulb:-싱글톤)
[2. 팩토리](#:bulb:-팩토리)
[3. 퍼사드](#:bulb:-퍼사드)

&nbsp;

### :bulb: 싱글톤

> 목적

- 생성 디자인 패턴
- 클래스에 대한 <b>단일 객체</b>를 생성한다.
- 전역 객체를 제공한다.
- 공유된 리소스에 대해 동시 접근할 수 있다.

> 구현

- <a href="https://github.com/myejin/Design_Pattern/blob/main/%EC%8B%B1%EA%B8%80%ED%86%A4/singleton(lazy%20init).py">`게으른 초기화`</a>

- <a href="https://github.com/myejin/Design_Pattern/blob/main/%EC%8B%B1%EA%B8%80%ED%86%A4/meta_singleton.py">`메타클래스로 구현`</a>

- <a href="https://github.com/myejin/Design_Pattern/blob/main/%EC%8B%B1%EA%B8%80%ED%86%A4/borg.py">`모노스테이트(보그)`</a>

- <a href="https://github.com/myejin/Design_Pattern/blob/main/%EC%8B%B1%EA%B8%80%ED%86%A4/ex1_db_app.py">`[예제1]데이터베이스 연결`</a>

- <a href="https://github.com/myejin/Design_Pattern/blob/main/%EC%8B%B1%EA%B8%80%ED%86%A4/ex1_db_app.py">`[예제2]인프라 헬스체크`</a>

&nbsp;

### :bulb: 팩토리

> 목적

- 생성 디자인 패턴
- 객체 생성과 클래스 구현을 나눠 상호의존도를 줄인다.
- 기존 코드를 수정하지 않고, 팩토리에 새로운 클래스를 추가할 수 있다.

> 구현

- <a href="https://github.com/myejin/Design_Pattern/blob/main/%ED%8C%A9%ED%86%A0%EB%A6%AC/simple_factory.py">`심플팩토리(기본 개념이라, 패턴으로 인정하지 않기도 한다.)`</a>

- <a href="https://github.com/myejin/Design_Pattern/blob/main/%ED%8C%A9%ED%86%A0%EB%A6%AC/factory_method.py">`팩토리 메소드 - 프로필 생성`</a>

- <a href="https://github.com/myejin/Design_Pattern/blob/main/%ED%8C%A9%ED%86%A0%EB%A6%AC/abstract_factory.py">`추상 팩토리 - 피자공장`</a>

&nbsp;

### :bulb: 퍼사드

> 목적

- 구조 디자인 패턴
- 최소 지식 원칙, 상호작용하는 객체를 밀접한 몇 개의 객체로 최소화한다.
- 1개의 서브시스템에 여러 퍼사드가 존재할 수 있다.

> 구현

- <a href="https://github.com/myejin/Design_Pattern/blob/main/%ED%8D%BC%EC%82%AC%EB%93%9C/event_planning.py">`이벤트 플래닝`</a>

&nbsp;











