#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include "interval_log.h"
int main(void){unsigned long long x;while(scanf("%llu",&x)==1){Interval v=ilog2(x);printf("%llu %llu %llu\n",x,(unsigned long long)v.lo,(unsigned long long)v.hi);}return 0;}
