/* Independent simulation of actual weighted walks, with first-entrance
   compression of reversed loop erasure. No path-law formula is sampled.
   Compile: cc -O2 -std=c11 independent_sim.c -o independent_sim
   Run: nice -n 10 ./independent_sim 10000000 > independent_sim.out
   One process, bounded arrays, 240-second wall-time alarm. */
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <time.h>
#include <sys/resource.h>

#define VMAX 16
#define EMAX 20
#define TRACE_MAX 1000000
static int trace[TRACE_MAX];
static uint64_t state;
static uint64_t random64(void) {
    /* SplitMix64, different generator from the supplied code. */
    uint64_t z = (state += UINT64_C(0x9e3779b97f4a7c15));
    z = (z ^ (z >> 30)) * UINT64_C(0xbf58476d1ce4e5b9);
    z = (z ^ (z >> 27)) * UINT64_C(0x94d049bb133111eb);
    return z ^ (z >> 31);
}
static uint64_t below(uint64_t bound) {
    uint64_t threshold = -bound % bound, z;
    do { z = random64(); } while (z < threshold);
    return z % bound;
}
static int nv, ne, degree[VMAX], neighbor[VMAX][3], edgeid[VMAX][3];
static int eu[EMAX], ev[EMAX], leg[2][4];
static uint64_t weight[EMAX], steps;
static void add(int x, int y) {
    if (ne >= EMAX || degree[x] >= 3 || degree[y] >= 3) abort();
    neighbor[x][degree[x]] = y; edgeid[x][degree[x]++] = ne;
    neighbor[y][degree[y]] = x; edgeid[y][degree[y]++] = ne;
    eu[ne] = x; ev[ne] = y; weight[ne++] = 1;
}
static void build(int ell) {
    nv=4; ne=0; steps=0; memset(degree,0,sizeof(degree));
    add(0,1); add(0,2); add(1,2);
    for (int side=0;side<2;side++) {
        int prev=side+1;
        for (int j=0;j<ell;j++) {
            int next=j+1==ell?3:nv++;
            leg[side][j]=ne; add(prev,next); prev=next;
        }
    }
}
static int find_edge(int x,int y) {
    for (int k=0;k<degree[x];k++) if (neighbor[x][k]==y) return edgeid[x][k];
    abort();
}
static int ant(int validate, long *different) {
    int parent[VMAX], x=0, nt=1;
    for (int v=0;v<nv;v++) parent[v]=-1;
    parent[0]=0;
    if (validate) trace[0]=0;
    while (x!=3) {
        uint64_t total=0;
        for (int k=0;k<degree[x];k++) total+=weight[edgeid[x][k]];
        uint64_t ticket=below(total);
        int k=0;
        while (ticket>=weight[edgeid[x][k]]) ticket-=weight[edgeid[x][k++]];
        int y=neighbor[x][k];
        if (parent[y]<0) parent[y]=x;
        x=y; steps++;
        if (validate) {
            if (nt==TRACE_MAX) abort();
            trace[nt++]=x;
        }
    }
    int reverse[VMAX], nr=0;
    for (x=3;;x=parent[x]) {
        reverse[nr++]=x;
        if (x==0) break;
        if (nr>=nv) abort();
    }
    if (validate) {
        int stack[VMAX], ns=0;
        for (int j=nt-1;j>=0;j--) {
            int k=0;
            while (k<ns && stack[k]!=trace[j]) k++;
            if (k<ns) ns=k+1; else stack[ns++]=trace[j];
        }
        if (ns!=nr || memcmp(stack,reverse,nr*sizeof(int))) abort();
        ns=0;
        for (int j=0;j<nt;j++) {
            int k=0;
            while (k<ns && stack[k]!=trace[j]) k++;
            if (k<ns) ns=k+1; else stack[ns++]=trace[j];
        }
        int diff=ns!=nr;
        if (!diff) for (int j=0;j<ns;j++) if (stack[j]!=reverse[nr-j-1]) diff=1;
        *different+=diff;
    }
    int rung=0;
    for (int j=0;j+1<nr;j++) {
        int e=find_edge(reverse[j],reverse[j+1]);
        weight[e]++;
        if (e==2) rung=1;
    }
    return rung;
}
int main(int argc,char **argv) {
    alarm(240);
    int priority=getpriority(PRIO_PROCESS,0);
    if (priority<10 && setpriority(PRIO_PROCESS,0,10)) { perror("setpriority"); return 3; }
    printf("process_nice=%d; static_trace_bytes=%zu\n",getpriority(PRIO_PROCESS,0),sizeof(trace));
    long limit=argc>1?strtol(argv[1],NULL,10):10000000;
    if (limit<10000 || limit>100000000) return 2;
    time_t began=time(NULL);
    for (int ell=2;ell<=3;ell++) for (int run=0;run<2;run++) {
        uint64_t seed=(uint64_t)(2026111201+run);
        state=seed; build(ell);
        long checkpoint=1000, different=0, rungs=0;
        printf("ell=%d seed=%llu ants=%ld\n",ell,(unsigned long long)seed,limit);
        printf("n a c h prediction residual a_minus_c\n");
        for (long n=1;n<=limit;n++) {
            rungs+=ant(n<=10000,&different);
            if (n==checkpoint || n==limit) {
                if (weight[0]+weight[1]!=(uint64_t)n+2 ||
                    weight[leg[0][0]]+weight[leg[1][0]]!=(uint64_t)n+2 ||
                    weight[2]!=(uint64_t)rungs+1) abort();
                for (int s=0;s<2;s++) for (int j=1;j<ell;j++)
                    if (weight[leg[s][j]]!=weight[leg[s][0]]) abort();
                double den=n+2.0, a=weight[0]/den, c=weight[leg[0][0]]/den;
                double h=weight[2]/den, target=(1.0-1.0/ell)*a*(1-a);
                printf("%ld %.9f %.9f %.9f %.9f %+.9f %+.9f\n",n,a,c,h,target,h-target,a-c);
                fflush(stdout);
                checkpoint*=10;
            }
        }
        printf("literal_reverse_validation=10000 PASS; forward_differs_on_same_walk=%ld; walk_steps=%llu; all_invariants=PASS\n",
               different,(unsigned long long)steps);
    }
    printf("elapsed_wall_seconds=%ld\n",(long)(time(NULL)-began));
    return 0;
}
