#include <stdio.h>
#include <stdint.h>
#include <math.h>
#include <time.h>
#include <sys/resource.h>
static int64_t C[25][25];
static double ell(double x){return x>0?x*log2(x):0;}
static double ph(double a,double b){return ell(a+b)-ell(a)-ell(b);}
int main(void){C[0][0]=1;for(int n=1;n<=24;n++){C[n][0]=C[n][n]=1;for(int k=1;k<n;k++)C[n][k]=C[n-1][k-1]+C[n-1][k];}
 clock_t start=clock();puts("[");for(int n=1;n<=20;n++){
 int64_t K[25][25]={0},F[25]={0};int f[25];for(int t=0;t<=n;t++)f[t]=1;
 for(int k=0;k<=n;k++)for(int t=0;t<=n;t++)for(int r=0;r<=k;r++)if(t-r>=0&&t-r<=n-k)K[k][t]+=(r&1?-1:1)*C[k][r]*C[n-k][t-r];F[0]=1<<n;
 double best=-1,bQ=-1,bpar=-1;unsigned bm=0,bqm=0,bpm=0;uint64_t count=1ull<<n;double den=(double)(1ull<<(2*n));
 for(unsigned j=0;j<count;j++){
  if(j){int t=__builtin_ctz(j)+1;for(int k=0;k<=n;k++)F[k]-=2*f[t]*K[k][t];f[t]=-f[t];}
  double I=0,E=0,Q=0,A[2]={0},B[2]={0};
  for(int k=0;k<=n;k++)I+=k*C[n][k]*(double)F[k]*F[k];
  if(!I)continue;
  for(int k=0;k<n;k++){double a=(double)F[k]*F[k],b=(double)F[k+1]*F[k+1];E+=n*C[n-1][k]*ph(a,b);Q+=n*C[n-1][k]*fabs((double)F[k]*F[k+1]);A[k&1]+=C[n-1][k]*a;B[k&1]+=C[n-1][k]*b;}
  double p=n*(ph(A[0],B[0])+ph(A[1],B[1]))/I;unsigned mask=j^(j>>1);
  if(E/I>best+1e-12){best=E/I;bm=mask;}if(Q/I>bQ+1e-12){bQ=Q/I;bqm=mask;}if(p>bpar+1e-12){bpar=p;bpm=mask;}
 }
 printf("%s{\"n\":%d,\"representatives\":%llu,\"Hm_over_I\":%.15g,\"value_mask\":\"0x%x\",\"half_norm_over_I\":%.15g,\"half_norm_mask\":\"0x%x\",\"parity_over_I\":%.15g,\"parity_mask\":\"0x%x\",\"cpu_seconds_cumulative\":%.6f}",n>1?",\n":"",n,(unsigned long long)count,best,bm,bQ,bqm,bpar,bpm,(double)(clock()-start)/CLOCKS_PER_SEC);fflush(stdout);
 }puts("\n]");return 0;}
