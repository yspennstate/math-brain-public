/* Independent NPN orbit census. Bit x=1 means f(x)=-1. */
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>
#include <sys/resource.h>
static int n,N,pc[32];
static uint8_t *seen;
static FILE *reps;
static uint32_t masks[5]={0x55555555,0x33333333,0x0f0f0f0f,0x00ff00ff,0x0000ffff};
static uint32_t full;
static double us[6]={0,.25,.5,.75,.875,1};
static double best[9]; static uint32_t witness[9];
static unsigned long long count;
static uint32_t flip(uint32_t t,int i){int h=1<<i;return (((t&masks[i])<<h)|((t>>h)&masks[i]))&full;}
static uint32_t swm[5][5]; static int swd[5][5];
static uint32_t sw(uint32_t t,int i,int j){if(i==j)return t;uint32_t q=((t>>swd[i][j])^t)&swm[i][j];return t^q^(q<<swd[i][j]);}
static void orbit(uint32_t t,int depth){
 if(depth==n){
  uint32_t z=t;
  for(int a=0;a<N;a++){
   if(a)z=flip(z,__builtin_ctz((unsigned)a));
   uint32_t c=z;if(c&(1u<<(N-1)))c^=full;
   seen[c>>3]|=(uint8_t)(1u<<(c&7));
  }return;
 }
 for(int j=depth;j<n;j++)orbit(sw(t,depth,j),depth+1);
}
static void evaluate(uint32_t t){
 double a[32],mu[32],F[6][32],phi[6]={0};
 for(int x=0;x<N;x++)a[x]=(t>>x&1)?-1:1;
 for(int h=1;h<N;h<<=1)for(int x=0;x<N;x+=2*h)for(int j=0;j<h;j++){double p=a[x+j],q=a[x+j+h];a[x+j]=p+q;a[x+j+h]=p-q;}
 double I=0,var=0;
 for(int s=0;s<N;s++){mu[s]=a[s]*a[s]/((double)N*N);I+=pc[s]*mu[s];if(s)var+=mu[s];for(int k=0;k<6;k++)F[k][s]=mu[s];}
 for(int k=0;k<6;k++)for(int h=1;h<N;h<<=1)for(int x=0;x<N;x++)if(!(x&h))F[k][x]+=us[k]*F[k][x|h];
 for(int s=0;s<N;s++)if(mu[s]>0)for(int k=0;k<6;k++)phi[k]-=mu[s]*log2(F[k][s]);
 if(I>0){for(int k=0;k<6;k++){double z=phi[k]/I;if(z>best[k]+1e-13){best[k]=z;witness[k]=t;}}
 double cost=phi[2]-phi[5];double z=cost/I;if(z>best[6]+1e-13){best[6]=z;witness[6]=t;}
 if(I-var>1e-14){z=cost/(I-var);if(z>best[7]+1e-13){best[7]=z;witness[7]=t;}}
 /* conditional entropy of the superset coupling, using H(S|U)=B+D(mu Z||mu). */
 double kl=0;for(int u=0;u<N;u++)if(mu[u]){double Z=0;for(int s=u;;s=(s-1)&u){if(mu[s])Z+=mu[s]/F[5][s];if(!s)break;}if(Z)kl+=mu[u]*Z*log2(Z);}
 z=(phi[0]-phi[5]+kl)/I;if(z>best[8]+1e-13){best[8]=z;witness[8]=t;}
 }
}
int main(int argc,char **argv){
 n=argc>1?atoi(argv[1]):4;if(n<1||n>5)return 2;N=1<<n;full=N==32?UINT32_MAX:((1u<<N)-1);
 uint64_t limit=1ull<<(N-1),bytes=(limit+7)/8;
 fprintf(stderr,"n=%d seen_bytes=%llu threads=1 nice_inherited; start\n",n,(unsigned long long)bytes);
 seen=calloc(bytes,1);if(!seen)return 3;for(int s=0;s<N;s++)pc[s]=__builtin_popcount(s);
 for(int i=0;i<n;i++)for(int j=i+1;j<n;j++){swd[i][j]=(1<<j)-(1<<i);for(int x=0;x<N;x++)if((x&(1<<i))&&!(x&(1<<j)))swm[i][j]|=1u<<x;}
 char path[80];snprintf(path,sizeof path,"npn%d.bin",n);reps=fopen(path,"wb");if(!reps)return 4;
 for(int k=0;k<9;k++)best[k]=-1;
 clock_t start=clock();
 for(uint64_t tt=0;tt<limit;tt++)if(!(seen[tt>>3]>>(tt&7)&1)){
  uint32_t t=tt;evaluate(t);fwrite(&t,4,1,reps);count++;orbit(t,0);
  if(count%50000==0){fflush(reps);fprintf(stderr,"classes=%llu scanned=0x%08x cpu_seconds=%.2f\n",count,t,(double)(clock()-start)/CLOCKS_PER_SEC);}
 }
 fclose(reps);struct rusage ru;getrusage(RUSAGE_SELF,&ru);
 printf("{\"n\":%d,\"classes\":%llu,\"boolean_functions\":%llu,\"seen_bytes\":%llu,\"cpu_seconds\":%.6f,\"maxrss_bytes\":%ld,\"nice\":%d,\"threads\":1,\"suprema\":[",n,count,(unsigned long long)(2*limit),(unsigned long long)bytes,(double)(clock()-start)/CLOCKS_PER_SEC,ru.ru_maxrss,getpriority(PRIO_PROCESS,0));
 for(int k=0;k<9;k++){if(best[k]<0)printf("%s{\"value\":null,\"tt\":null}",k?",":"");else printf("%s{\"value\":%.15g,\"tt\":\"0x%0*x\"}",k?",":"",best[k],(N+3)/4,witness[k]);}puts("]}");free(seen);return 0;
}
