/* One planar SRW, stopped on its first step outside the closed radius-n disc. */
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <inttypes.h>

static uint64_t state;
static uint64_t random64(void) {
    uint64_t z = (state += UINT64_C(0x9e3779b97f4a7c15));
    z = (z ^ (z >> 30)) * UINT64_C(0xbf58476d1ce4e5b9);
    z = (z ^ (z >> 27)) * UINT64_C(0x94d049bb133111eb);
    return z ^ (z >> 31);
}
int main(int argc, char **argv) {
    if (argc != 4) return 2;
    int n = atoi(argv[1]), side = 2*n+1, x=0, y=0;
    if (n < 1 || n > 4096) return 3;
    state = strtoull(argv[2], NULL, 10);
    size_t cells=(size_t)side*side;
    uint32_t *local = calloc(cells, sizeof(*local));
    if (!local) return 4;
    uint64_t steps=0;
    local[(size_t)n*side+n]=1;
    for (;;) {
        unsigned d = (unsigned)(random64() >> 62);
        if(d==0) ++x; else if(d==1) --x; else if(d==2) ++y; else --y;
        ++steps;
        if ((int64_t)x*x+(int64_t)y*y > (int64_t)n*n) break;
        size_t i=(size_t)(y+n)*side+x+n;
        if (local[i] == UINT32_MAX) return 5;
        ++local[i];
    }
    FILE *f=fopen(argv[3],"wb");
    if (!f) return 6;
    if(fwrite(local,sizeof(*local),cells,f)!=cells) return 7;
    fclose(f);
    printf("{\"n\":%d,\"seed\":%" PRIu64 ",\"exit_time\":%" PRIu64 ",\"exit_x\":%d,\"exit_y\":%d}\n",
           n,state-(steps*UINT64_C(0x9e3779b97f4a7c15)),steps,x,y);
    free(local);
    return 0;
}
