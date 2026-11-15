// Exact integer finite differences; only final logarithms use binary64.
#include <stdint.h>
#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <time.h>
#define N 25
#include "quantlog.h"
static uint64_t bin[N+1][N+1];
static int64_t d[N+1];
static double best[2][4];
static uint32_t arg[2][4], candidates[2][4][4096];
static int nc[2][4];
static double runner[2][4];
static void record(int b,int z,double r,uint32_t mask){
 double tol=1e-10;
 if(r>best[b][z]+tol){runner[b][z]=best[b][z];best[b][z]=r;arg[b][z]=mask;nc[b][z]=0;}
 if(r>=best[b][z]-tol){
  if(nc[b][z]>=4096){fprintf(stderr,"candidate overflow\n");exit(4);}
  candidates[b][z][nc[b][z]++]=mask;
  if(r>best[b][z]){best[b][z]=r;arg[b][z]=mask;}
 }else if(r>runner[b][z])runner[b][z]=r;
}
int main(int argc,char **argv){
 int n=argc>1?atoi(argv[1]):12;
 if(n<1||n>24)return 2;
 for(int m=0;m<=n;m++){bin[m][0]=bin[m][m]=1;for(int t=1;t<m;t++)bin[m][t]=bin[m-1][t-1]+bin[m-1][t];}
 uint64_t count=1ULL<<n,balanced=0,nonconstant=0;
 long double coarsemax=0;uint32_t coarsearg=0;
 for(int b=0;b<2;b++)for(int z=0;z<4;z++)best[b][z]=-1;
 double scale=ldexp(1.,-2*n);clock_t start=clock();
 for(uint32_t mask=0;mask<count;mask++){
   d[0]=1;for(int t=1;t<=n;t++)d[t]=(mask>>(t-1)&1)?-1:1;
   double val[4]={0},I=0;
   int bal=0;
   uint64_t varnum=0,Iinteger=0;unsigned __int128 T=0;int F0nonzero=0;
   for(int k=0;k<=n;k++){
     int64_t F=0;uint64_t L=0,Q=0;
     for(int t=0;t<=n-k;t++){
       int64_t x=d[t];uint64_t c=bin[n-k][t];
       F+=(int64_t)c*x; L+=c*llabs(x);Q+=c*(uint64_t)(x*x);
     }
     if(!k){bal=(F==0);F0nonzero=F!=0;varnum=(1ULL<<(2*n))-(uint64_t)(F*F);}
     if(F){
       uint64_t mass=bin[n][k]*(uint64_t)(F*F);
       Iinteger+=k*mass;
       if(k)T+=(unsigned __int128)mass*(qlog(Q,1)+(n-k)*1024-2*qlog(llabs(F),0));
       double w=(double)bin[n][k]*(double)(F*F)*scale;
       if(k==0){
         double p=ldexp((double)((1LL<<n)-llabs(F)),-n-1);
         double b0=-2*w*log1p(-2*p)/log(2.);val[1]+=b0;val[2]+=b0/2;
         for(int t=0;t<n-k;t++)d[t]-=d[t+1];
         continue;
       }
       double logf=log2((double)llabs(F)),logq=log2((double)Q);
       val[0]+=w*((n+k)-logq);
       val[1]+=w*(logq+(n-k)-2*logf);
       val[2]+=w*(log2((double)L)-logf);
       // P is recorded too, though the brief asks ratios only for A,B,Gamma.
       uint64_t supp=0;for(int t=0;t<=n-k;t++)if(d[t])supp+=bin[n-k][t];
       val[3]+=w*((n-k)-log2((double)supp));
       I+=k*w;
     }
     for(int t=0;t<n-k;t++)d[t]-=d[t+1];
   }
   if(I==0)continue;
   unsigned __int128 certificate=1000*T+(F0nonzero?(unsigned __int128)1443*1024*varnum:0);
   if(certificate>(unsigned __int128)2180*1024*Iinteger){fprintf(stderr,"exact B certificate failed n=%d mask=%u\n",n,mask);return 5;}
   long double bound=(long double)certificate/(1000.L*1024*Iinteger);if(bound>coarsemax){coarsemax=bound;coarsearg=mask;}
   nonconstant++;if(bal)balanced++;
   for(int z=0;z<4;z++){
      double r=val[z]/I;
      record(0,z,r,mask);
      if(bal&&I>1){r=val[z]/(I-1);record(1,z,r,mask);}
   }
 }
 printf("{\"n\":%d,\"representatives\":%llu,\"nonconstant\":%llu,\"balanced\":%llu,\"cpu_seconds\":%.6f,\"maxima\":{",n,(unsigned long long)count,(unsigned long long)nonconstant,(unsigned long long)balanced,(double)(clock()-start)/CLOCKS_PER_SEC);
 const char*names[]={"A","B","Gamma","P"};
 for(int b=0;b<2;b++)for(int z=0;z<4;z++){
   if(b||z)printf(",");
   printf("\"%s/%s\":{\"value\":%.16g,\"mask\":%u,\"runner_up_below_tolerance\":%.16g,\"candidates\":[",names[z],b?"(I-1)":"I",best[b][z],arg[b][z],runner[b][z]);
   for(int c=0;c<nc[b][z];c++){if(c)printf(",");printf("%u",candidates[b][z][c]);}printf("]}");
 }
 printf("},\"B_le_3.463I_integer_certificate\":true,\"B_le_3.276I_integer_certificate\":true,\"B_le_2.18I_integer_certificate\":true,\"coarse_upper_max\":%.18Lg,\"coarse_upper_mask\":%u}\n",coarsemax,coarsearg);return 0;
}
