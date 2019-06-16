#include <stdio.h>

int main(int argc, char const *argv[]) {
  long long N, K, s;
  int count = 0;
  long long a[100000], acum[100001];
  scanf("%lld %lld", &N, &K);
  acum[0] = 0;
  for (int i = 0; i < N; i++) {
    scanf("%lld", &a[i]);
    acum[i + 1] = acum[i] + a[i];
  }

  for (int i = 0; i < N; i++) {
    for (int j = N; j > i; j--) {
      s = acum[j] - acum[i];
      // printf("%lld", s);
      if (s >= K) {
        count++;
      } else {
        break;
      }
    }
  }

  printf("%d", count);
}
