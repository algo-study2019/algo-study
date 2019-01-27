## 1. CS and DS

### 1.1. 자료구조와 추상데이터타입

- 추상데이터타입(Abstract Data Type): 데이터와 그 데이터에 대한 추상적인 연산들로 구성
  - 이 책의 한계: 따로 ADT를 선언하여 명세를 정의하지 않아도 DS를 구현하는데 무리가 없으므로 ADT 선언 생략
- 자료구조(Data Structure): 일련의 동일한 타입의 데이터를 정돈하여 저장한 구성체
  - ADT를 구체화한 것.
- 효율적인 DS, ADT, Algorithm은 맞물려 돌아간다.

### 1.2. 수행시간

- 수행시간 : 시간복잡도(Time Complexcity), 기본적인 연산 횟수(O)에 입력횟수(N)을 대입
  - 기본연산(Elementary Operation): 데이터간 크기 비교, 데이터 읽기 및 갱신, 숫자 계산 등
- 공간복잡도(Space Complexity): 메모리 사용 정도
- 3종류
  - \*Worst-case Analysis(Big-O): Upper bound
  - Average-case Analysis(Big-theta): N ~ Uniform distribution
  - Best-case Analysis(Big-sigma): Lower bound, when do you find optimal algorithm(whatever you input, show best time complexcity)

#### 1.3.1 수행시간의 점근표기법(Asymptotic Notation)

- usually, Big-O
- O(1): constant time
- O(logN): logarithmic time
- O(N): linear time
- O(NlogN): log-linear time
- O(N^2): Quadratic time
- O(N^k): polynomial time
- O(2^n): exponential time
- O(N!):

### 1.4. 파이썬 언어에 대한 기본적인 지식

- structure
  - class
  - method
  - instance variable: self.sth
  - constructor : init
- basic grammar
  - list: in C or java, it's a dynamic array
  - if
  - for, while
  - range
  - embedded functions
  - lambda args: expression

### 1.5. python memory

- heap memory
  - object, list, tuple, dictionary 등이 저장
  - gc에 의해 제거되지 않는한, 프로그램이 끝날 때까지 남아있다.
- stack memory
  - function, method 호출에 따른 parameter / local variance
- garbage collection
  - reference count가 0이되면 gc
  - 상호 참조로 삭제 되지 않는 경우 발생
  - 그래서 파이썬에서는 generation-based garbage collection 기법을 사용
- gb gc
  - 대부분의 객체가 수명이 짧다는 점에 기반해서 만듦
  - young / old gen을 나눠서 heap에 저장

## 2. 순환(Recursion): 함수의 실행 과정 중 스스로를 호출

- 2 parts
  - Base Case: no more call self
  - Recursion Case
- python recursion error
  - [sys.setrecursionlimit](showUp.ipynb)
  - Tail Recursion: it's efficient to convert to a loop
- VS loop
  - recursion is more readable, but bad space complexity : system memory
  - similar time complexity

## 3. Linked List

### 3-1 Singly Linked List

- 동적 메모리 할당을 받아 노드를 저장하고, 레퍼런스를 이용하여 노드들을 한 방향으로 연결하여 리스트를 구현
- [singly linked list - class](ch02/slist.py)
  - [SSL main func](ch02/main.py)
- **must Sequential Search**
- execution time
  - search(): O(N)
  - insert, delete: O(1)
  - insert/delete after: if does not give the front node, O(N)
- stack, queue, chaining of hashing, tree

### 3-2 Doubly Linked List

- 각 노드가 두 개의 레퍼런스를 가지고 각각 이전 노드와 다음 노드를 가리키는 연결리스트이다.
- [DLL implement](ch02/dll.py)
- [main func](ch02/main.py)
- execution time
  - insert, delete : O(1)
  - search: O(N)
- deque, binomial heap, fibonacci heap

### 3-3 Circular Linked List

- [CLL implement](ch02/cll.py)
- [main func](ch02/main.py)
- Good
  - search tail and head: O(1)
  - if not empty, every node do not have None -> don't have to inspect None
- Bad
  - can't search reverse
  - easily inf loop
- execution time
  - insert, delete: O(1)
  - search: O(N)
- board game, cpu time slice OS, binomial heap, fibonacci heap

## 4. Stack and Queue

### 4-1 Stack

- 한 쪽 끝에서만 item을 삭제하거나 추가: push & pop
- big-O
    - list: push & pop : O(1)
        - but, python list is dynamic, so it takes O(N) <- using index0
        - ***python list에는 -1 index를 입구로 사용하는 pop, append가 구현되어 있다***
    - singly linked list: push & pop : O(1)

### 4-2 Queue

- 한 쪽 끝에서 삽입되서 반대쪽에서 삭제되는 자료구조: FIFO
- 응용
  - CPU Task Scheduling
  - Network Printer
  - Interrupt processing in Real-time system
  - Event-driven computer simulation
  - call center
  - level-order traversal
  - breath-first search of Graph
- 수행시간
  - add, remove: O(1)
    - python list : O(N)
- [collections.deque](https://docs.python.org/3/library/collections.html#collections.deque)

### 4-3 Deque

- 양쪽 끝에서 삽입과 삭제가 모두 이루어지는 큐
    - Stack + Queue
- Application
    - Scroll
    - undo
    - 방문 기록
- 수행시간
    - stack, queue와 수행 시간 동일
- [collections.deque](https://docs.python.org/3/library/collections.html#collections.deque)

## 5. 문제풀이

- [쇠막대기](pipe.py)
- [프린터](printer.py)
- [다리를 지나가는 트럭](truck.py)
- [기능 개발](dev.py)
- [탑](top.py)
- [주식가격](stock.py)
