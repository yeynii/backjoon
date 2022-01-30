# 다음 소스는 N번째 피보나치 수를 구하는 C++ 함수이다.

# int fibonacci(int n) {
#     if (n == 0) {
#         printf("0");
#         return 0;
#     } else if (n == 1) {
#         printf("1");
#         return 1;
#     } else {
#         return fibonacci(n‐1) + fibonacci(n‐2);
#     }
# }

# 1은 2번 출력되고, 0은 1번 출력된다. N이 주어졌을 때, fibonacci(N)을 호출했을 때, 0과 1이 각각 몇 번 출력되는지 구하는 프로그램을 작성하시오.


fibo = [[1, 0], [0, 1]]

T = int(input())

for i in range(T):
  N = int(input())
  if len(fibo) <= N:
    for i in range(len(fibo), N + 1):
      fibo.append([i + j for i, j in zip(fibo[i-1], fibo[i-2])])
  print(*fibo[N])