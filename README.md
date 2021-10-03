## :books: Design Pattern

<img width="200" src="https://user-images.githubusercontent.com/42771578/134512989-9a30807c-d5cc-4762-b28a-ea950736c659.png">

### 목차

[1. 싱글톤](#:bulb:-싱글톤)<br>
[2. 팩토리](#:bulb:-팩토리)<br>
[3. 퍼사드](#:bulb:-퍼사드)<br>
[4. 프록시](#:bulb:-프록시)

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
- 클라이언트에게 간소화된 인터페이스를 제공한다.
- 최소 지식 원칙, 상호작용하는 객체를 밀접한 몇 개의 객체로 최소화한다.
- 1개의 서브시스템에 여러 퍼사드가 존재할 수 있다.

> 구현

- <a href="https://github.com/myejin/Design_Pattern/blob/main/%ED%8D%BC%EC%82%AC%EB%93%9C/event_planning.py">`이벤트 플래닝`</a>

&nbsp;

### :bulb: 프록시

> 목적

- 구조 디자인 패턴
- 주 목적 : 실제 객체에 접근할 수 있는 대리객체를 제공해 접근을 제어한다.
- 제대로 설계되지 않는다면 실 객체의 응답시간에 영향을 줄 수 있다.
- 적용되는 방식에 따라
    가상 프록시 : 무거운 객체의 플레이스 홀더 역할을 할 수 있다. (이미지 있음을 표시하는 아이콘 표시)
    원격 프록시 : 다른 주소공간에 존재하는 객체에 대한 로컬 인스턴스를 생성한다. (모니터링 시스템)
    보호 프록시 : 실 객체의 중요한 부분에 대한 접근을 제어한다. (사용자 인증, 허가 담당 서비스)
    스마트 프록시 : 추가적인 행동을 취한다. (기능이 동시에 호출되면 객체의 잠금상태 확인)

> 구현

- <a href="https://github.com/myejin/Design_Pattern/blob/main/%ED%94%84%EB%A1%9D%EC%8B%9C/payment_system.py">`결제 시스템`</a>

&nbsp;










