#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "interval_log.h"
#define N 25
#define CAP 8192
static uint64_t bin[N+1][N+1];static int64_t d[N+1];
typedef struct {uint64_t lo,hi;uint32_t mask;} Candidate;
static Candidate cand[2][4][CAP];static int count[2][4];static uint64_t maxlo[2][4],maxhi[2][4];static int have[2][4];
static void add(int b,int z,uint64_t lo,uint64_t hi,uint32_t mask){
 have[b][z]=1;if(hi>maxhi[b][z])maxhi[b][z]=hi;
 if(lo>maxlo[b][z]){maxlo[b][z]=lo;int keep=0;for(int i=0;i<count[b][z];i++)if(cand[b][z][i].hi>=lo)cand[b][z][keep++]=cand[b][z][i];count[b][z]=keep;}
 if(hi>=maxlo[b][z]){if(count[b][z]==CAP)exit(7);cand[b][z][count[b][z]++]=(Candidate){lo,hi,mask};}
}
static uint64_t lower_coefficient(int64_t x){return x>0?(uint64_t)x:0;}
int main(int argc,char**argv){
 int n=argc>1?atoi(argv[1]):12;if(n<1||n>24)return 2;
 for(int a=0;a<=n;a++){bin[a][0]=bin[a][a]=1;for(int j=1;j<a;j++)bin[a][j]=bin[a-1][j-1]+bin[a-1][j];}
 clock_t start=clock();
 for(uint32_t mask=0;mask<(1U<<n);mask++){
  d[0]=1;for(int j=1;j<=n;j++)d[j]=(mask>>(j-1)&1)?-1:1;
  unsigned __int128 lo[4]={0},hi[4]={0};uint64_t I=0;int balanced=0;
  for(int k=0;k<=n;k++){
   int64_t F=0;uint64_t L=0,Q=0,NN=0;
   for(int t=0;t<=n-k;t++){uint64_t c=bin[n-k][t],v=llabs(d[t]);F+=(int64_t)c*d[t];L+=c*v;Q+=c*v*v;if(v)NN+=c;}
   if(!k)balanced=F==0;
   if(F){
    uint64_t FF=(uint64_t)(F*F),mass=bin[n][k]*FF;I+=k*mass;
    Interval a=ilog2(Q),b=ilog2(llabs(F)),c=ilog2(L),p=ilog2(NN);
    int64_t low[4]={0},high[4]={0};
    if(k&&Q!=(1ULL<<(n+k))){low[0]=(n+k)*(int64_t)LOG_Q-(int64_t)a.hi;high[0]=(n+k)*(int64_t)LOG_Q-(int64_t)a.lo;}
    if((Q<<(n-k))!=FF){low[1]=(n-k)*(int64_t)LOG_Q+(int64_t)a.lo-2*(int64_t)b.hi;high[1]=(n-k)*(int64_t)LOG_Q+(int64_t)a.hi-2*(int64_t)b.lo;}
    if(L!=(uint64_t)llabs(F)){low[2]=(int64_t)c.lo-(int64_t)b.hi;high[2]=(int64_t)c.hi-(int64_t)b.lo;}
    if(k&&NN!=(1ULL<<(n-k))){low[3]=(n-k)*(int64_t)LOG_Q-(int64_t)p.hi;high[3]=(n-k)*(int64_t)LOG_Q-(int64_t)p.lo;}
    for(int z=0;z<4;z++){if(high[z]<0)exit(8);lo[z]+=(unsigned __int128)mass*lower_coefficient(low[z]);hi[z]+=(unsigned __int128)mass*(uint64_t)high[z];}
   }
   for(int t=0;t<n-k;t++)d[t]-=d[t+1];
  }
  if(!I)continue;
  for(int b=0;b<2;b++){
   if(b&&(!balanced||I<=(1ULL<<(2*n))))continue;
   uint64_t den=b?I-(1ULL<<(2*n)):I;
   for(int z=0;z<4;z++){
    unsigned __int128 l=lo[z]/den,h=(hi[z]+den-1)/den;
    if((l>>64)||(h>>64))exit(9);
    add(b,z,(uint64_t)l,(uint64_t)h,mask);
   }
  }
 }
 printf("{\"n\":%d,\"representatives\":%u,\"cpu_seconds\":%.6f,\"scale\":%llu,\"maxima\":{",n,1U<<n,(double)(clock()-start)/CLOCKS_PER_SEC,(unsigned long long)LOG_Q);
 const char*names[]={"A","B","Gamma","P"};
 for(int b=0;b<2;b++)for(int z=0;z<4;z++){
  if(b||z)printf(",");printf("\"%s/%s\":",names[z],b?"(I-1)":"I");
  if(!have[b][z]){printf("null");continue;}
  printf("{\"lower_numerator\":%llu,\"upper_numerator\":%llu,\"candidates\":[",(unsigned long long)maxlo[b][z],(unsigned long long)maxhi[b][z]);
  for(int j=0;j<count[b][z];j++){if(j)printf(",");printf("%u",cand[b][z][j].mask);}printf("]}");
 }
 puts("}}");return 0;
}
