// Exact integer finite differences; only final logarithms use binary64.
#include <stdint.h>
#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <time.h>
#define N 25
static uint64_t bin[N+1][N+1];
static int64_t d[N+1];
static double best[2][4];
static uint32_t arg[2][4];
int main(int argc,char **argv){
 int n=argc>1?atoi(argv[1]):12;
 if(n<1||n>24)return 2;
 for(int m=0;m<=n;m++){bin[m][0]=bin[m][m]=1;for(int t=1;t<m;t++)bin[m][t]=bin[m-1][t-1]+bin[m-1][t];}
 uint64_t count=1ULL<<n,balanced=0,nonconstant=0;
 for(int b=0;b<2;b++)for(int z=0;z<4;z++)best[b][z]=-1;
 double scale=ldexp(1.,-2*n);clock_t start=clock();
 for(uint32_t mask=0;mask<count;mask++){
   d[0]=1;for(int t=1;t<=n;t++)d[t]=(mask>>(t-1)&1)?-1:1;
   double val[4]={0},I=0;
   int bal=0;
   for(int k=0;k<=n;k++){
     int64_t F=0;uint64_t L=0,Q=0;
     for(int t=0;t<=n-k;t++){
       int64_t x=d[t];uint64_t c=bin[n-k][t];
       F+=(int64_t)c*x; L+=c*llabs(x);Q+=c*(uint64_t)(x*x);
     }
     if(!k)bal=(F==0);
     if(F){
       double w=(double)bin[n][k]*(double)(F*F)*scale;
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
   nonconstant++;if(bal)balanced++;
   for(int z=0;z<4;z++){
      double r=val[z]/I;
      if(r>best[0][z]+1e-14){best[0][z]=r;arg[0][z]=mask;}
      if(bal&&I>1){r=val[z]/(I-1);if(r>best[1][z]+1e-14){best[1][z]=r;arg[1][z]=mask;}}
   }
 }
 printf("{\"n\":%d,\"representatives\":%llu,\"nonconstant\":%llu,\"balanced\":%llu,\"cpu_seconds\":%.6f,\"maxima\":{",n,(unsigned long long)count,(unsigned long long)nonconstant,(unsigned long long)balanced,(double)(clock()-start)/CLOCKS_PER_SEC);
 const char*names[]={"A","B","Gamma","P"};
 for(int b=0;b<2;b++)for(int z=0;z<4;z++){
   if(b||z)printf(",");
   printf("\"%s/%s\":{\"value\":%.16g,\"mask\":%u}",names[z],b?"(I-1)":"I",best[b][z],arg[b][z]);
 }
 puts("}}");return 0;
}
