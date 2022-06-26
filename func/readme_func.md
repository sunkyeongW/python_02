#함수 중요성
1. 코드의 복잡도를 쉽게 품.
2. 코드의 재사용성
- 분리되고 모듈된 코드를 재사용
3. 코드의 안정성과 수정이 쉬움.

#함수 정의 방법
def function_name(parameter):

#return
함수에서 결과값을 반환시킴.

# *args, **kwargs 매개변수
*args 튜플형태
**kwargs 딕셔너리형태

#중첩 함수
함수안에 함수로 호출했을때 중첩 되어있는 함수는 정의되지 않음.

#람다(Lambda)
메모리 절약, 가독성 향상, 코드 간결
즉시 실행 함수(heap 초기화) -> 메모리 초기화

#def mul_func(x, y):
#    return x * y

#lambda x, y: x * y   #위의 선언가 같은 결과를 보여줌