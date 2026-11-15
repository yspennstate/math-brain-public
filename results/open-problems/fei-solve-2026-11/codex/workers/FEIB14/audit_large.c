/* Independent optimizer: direct cell sums for every pair (P,N), no masked transforms. */
#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>
#include <sys/resource.h>
static double*e;
static double ph(int64_t a,int64_t b){return e[a+b]-e[a]-e[b];}
int main(int argc,char**argv){if(argc!=3)return 2;int n=atoi(argv[1]),L=1<<n,M=L/2;char*h=argv[2];if(h[0]=='0'&&h[1]=='x')h+=2;int len=0;while(h[len])len++;
 int8_t*f=calloc(L,1);int64_t*mu=calloc(L,sizeof(int64_t));int*pc=calloc(M,sizeof(int));uint8_t*par=calloc(M*M,1);e=calloc(L*L+1,sizeof(double));clock_t start=clock();
 for(int x=1;x<=L*L;x++)e[x]=x*log2((double)x);
 for(int x=0;x<L;x++){int j=len-1-x/4;int z=0;if(j>=0){char c=h[j];z=c>='a'?c-'a'+10:c-'0';}f[x]=(z>>(x%4)&1)?-1:1;}
 double I=0,H=0;for(int s=0;s<L;s++){int a=0;for(int x=0;x<L;x++)a+=f[x]*(__builtin_parity((unsigned)(s&x))?-1:1);mu[s]=(int64_t)a*a;I+=__builtin_popcount((unsigned)s)*mu[s];H+=2*n*mu[s]-e[mu[s]];}
 for(int t=0;t<M;t++)pc[t]=__builtin_popcount((unsigned)t);for(int p=0;p<M;p++)for(int t=0;t<M;t++)par[p*M+t]=__builtin_parity((unsigned)(p&t));
 double total[7]={0};
 for(int i=0;i<n;i++){
  int64_t a[512],b[512],A=0,B=0,sa[15]={0},sb[15]={0};int bit=1<<i;
  for(int t=0;t<M;t++){int s=(t&(bit-1))|((t&~(bit-1))<<1);a[t]=mu[s];b[t]=mu[s|bit];A+=a[t];B+=b[t];sa[pc[t]]+=a[t];sb[pc[t]]+=b[t];total[0]+=ph(a[t],b[t]);}
  double best[5]={ph(A,B),ph(A,B),ph(A,B),0,ph(A,B)};
  for(int k=0;k<n;k++)best[3]+=ph(sa[k],sb[k]);
  for(int p=0;p<M;p++){int64_t ca[2]={0},cb[2]={0};for(int t=0;t<M;t++){int k=par[p*M+t];ca[k]+=a[t];cb[k]+=b[t];}double v=ph(ca[0],cb[0])+ph(ca[1],cb[1]);if(v<best[0])best[0]=v;}
  for(int N=0;N<M;N++){
   int64_t ca[15]={0},cb[15]={0};for(int t=0;t<M;t++){int k=pc[t&N];ca[k]+=a[t];cb[k]+=b[t];}
   double v=ph(ca[0],cb[0])+ph(A-ca[0],B-cb[0]);if(v<best[1])best[1]=v;
   v=0;for(int k=0;k<n;k++)v+=ph(ca[k],cb[k]);if(v<best[4])best[4]=v;
   for(int p=0;p<M;p++){
    int64_t da[4]={0},db[4]={0};for(int t=0;t<M;t++){int k=par[p*M+t]+2*((t&N)!=0);da[k]+=a[t];db[k]+=b[t];}
    double z=0;for(int k=0;k<4;k++)z+=ph(da[k],db[k]);if(z<best[2])best[2]=z;
   }
  }
  double lowest=best[0];for(int k=0;k<5;k++){total[k+1]+=best[k];if(best[k]<lowest)lowest=best[k];}total[6]+=lowest;
 }
 struct rusage r;getrusage(RUSAGE_SELF,&r);printf("{\"n\":%d,\"ratios\":[%.15g",n,H/I);for(int k=0;k<7;k++)printf(",%.15g",total[k]/I);printf("],\"cpu_seconds\":%.6f,\"maxrss_bytes\":%ld,\"nice\":%d,\"threads\":1}\n",(double)(clock()-start)/CLOCKS_PER_SEC,r.ru_maxrss,getpriority(PRIO_PROCESS,0));return 0;}
