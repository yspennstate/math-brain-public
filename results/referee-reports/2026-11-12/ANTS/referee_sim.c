/* Independent trace process: weights stay frozen throughout each ant;
   an edge bitset receives ONE increment after absorption, irrespective of repeats. */
#include <stdint.h>
#include <stdio.h>
#include <time.h>
#include <unistd.h>
#include <signal.h>
#include <sys/resource.h>
static uint64_t state=20261112;
static uint64_t rng(void){uint64_t x=state;x^=x>>12;x^=x<<25;x^=x>>27;state=x;return x*UINT64_C(2685821657736338717);}
static uint64_t draw(uint64_t n){uint64_t x,threshold=-n%n;do{x=rng();}while(x<threshold);return x%n;}
static double now(void){struct timespec t;clock_gettime(CLOCK_MONOTONIC,&t);return t.tv_sec+t.tv_nsec*1e-9;}
static void run(char *name,int nv,int m,int E[][2],int N,int F){
    int deg[8]={0},adj[8][12],nb[8][12];uint64_t w[16],steps=0,multi=0;
    for(int j=0;j<m;j++){w[j]=1;int u=E[j][0],v=E[j][1];adj[u][deg[u]]=j;nb[u][deg[u]++]=v;adj[v][deg[v]]=j;nb[v][deg[v]++]=u;}
    printf("%s edges",name);for(int j=0;j<m;j++)printf(" (%d,%d)",E[j][0],E[j][1]);puts("");
    double start=now();uint64_t n=0,next=1000;
    while(n<UINT64_C(100000000)){
        int x=N;uint32_t trace=0;unsigned visits[16]={0};
        while(x!=F){uint64_t sum=0;for(int k=0;k<deg[x];k++)sum+=w[adj[x][k]];
            uint64_t r=draw(sum);int k=0;while(r>=w[adj[x][k]]){r-=w[adj[x][k]];k++;}
            int j=adj[x][k];trace|=1u<<j;visits[j]++;x=nb[x][k];steps++;
        }
        for(int j=0;j<m;j++){if(trace&(1u<<j))w[j]++;if(visits[j]>1)multi++;}n++;
        int stop=(n%4096==0&&now()-start>35.0)||n==UINT64_C(100000000);
        if(n==next||stop){printf("n=%llu ratios",(unsigned long long)n);for(int j=0;j<m;j++)printf(" %.10f",(double)w[j]/n);printf(" steps=%llu repeats=%llu seconds=%.3f\n",(unsigned long long)steps,(unsigned long long)multi,now()-start);fflush(stdout);if(n==next)next*=10;}
        if(stop)break;
    }
}
int main(void){alarm(235);setpriority(PRIO_PROCESS,0,10);
    int paw[][2]={{0,1},{1,2},{1,3},{2,3}};
    int detour[][2]={{0,1},{0,2},{1,4},{2,4},{1,3},{3,4}};
    int shadow[][2]={{0,1},{0,2},{1,4},{2,4},{1,3},{2,3},{3,4}};
    int k33[][2]={{1,0},{1,4},{1,5},{2,0},{2,4},{2,5},{3,0},{3,4},{3,5},{5,4}};
    run("paw N0 x1 y2 F3",4,4,paw,0,3);
    run("detour N0 a1 b2 y3 F4",5,6,detour,0,4);
    run("shadow N0 a1 b2 c3 F4",5,7,shadow,0,4);
    run("K33 N0 F4 x5",6,10,k33,0,4);
    return 0;
}
