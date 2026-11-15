/* Exact dyadic masses, binary64 logarithms. No NPN generation here. */
#include <stdint.h>
#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <time.h>
#include <sys/resource.h>
#define MAX 16384
static double tab[2049];
static double ell(int64_t x){if(x<=0)return 0;return x<=2048?tab[x]:x*log2((double)x);}
static double ph(int64_t a,int64_t b){return ell(a+b)-ell(a)-ell(b);}
static void wt(int64_t*a,int M){for(int h=1;h<M;h*=2)for(int x=0;x<M;x+=2*h)for(int j=0;j<h;j++){int64_t p=a[x+j],q=a[x+j+h];a[x+j]=p+q;a[x+j+h]=p-q;}}
void init(void){for(int x=1;x<=2048;x++)tab[x]=x*log2((double)x);}
/* out: I,H,Hminus,five witness costs. params: per-coordinate P,N packed as two integers per family. */
void evaluate(const int8_t*f,int n,int full,double*out,int*params){
 int L=1<<n,M=L/2,m=n-1;int64_t hat[MAX],a[MAX/2],b[MAX/2],wa[MAX/2],wb[MAX/2],ma[MAX/2],mb[MAX/2];
 for(int x=0;x<L;x++)hat[x]=f[x];wt(hat,L);double den=(double)L*L;
 for(int j=0;j<9;j++)out[j]=0;
 for(int s=0;s<L;s++){int64_t v=hat[s]*hat[s];out[0]+=__builtin_popcount((unsigned)s)*v;out[1]+=v*(2*n)-ell(v);}
 for(int i=0;i<n;i++){
  int bit=1<<i;int64_t A=0,B=0;double exact=0,sz=0;int64_t ca[15]={0},cb[15]={0};
  for(int t=0;t<M;t++){int s=(t&(bit-1))|((t&~(bit-1))<<1);a[t]=hat[s]*hat[s];b[t]=hat[s|bit]*hat[s|bit];A+=a[t];B+=b[t];exact+=ph(a[t],b[t]);int k=__builtin_popcount((unsigned)t);ca[k]+=a[t];cb[k]+=b[t];}
  for(int k=0;k<=m;k++)sz+=ph(ca[k],cb[k]);out[2]+=exact;out[6]+=sz;
  double best[5]={ph(A,B),ph(A,B),ph(A,B),sz,ph(A,B)};int bp[5]={0},bn[5]={0};
  if(full){
   for(int t=0;t<M;t++){wa[t]=a[t];wb[t]=b[t];}wt(wa,M);wt(wb,M);
   for(int p=0;p<M;p++){double z=ph((A+wa[p])/2,(B+wb[p])/2)+ph((A-wa[p])/2,(B-wb[p])/2);if(z<best[0]-1e-9){best[0]=z;bp[0]=p;}}
   if(full!=3)for(int N=0;N<M;N++){
    int64_t cna[15]={0},cnb[15]={0};
    for(int t=0;t<M;t++){int k=__builtin_popcount((unsigned)(t&N));cna[k]+=a[t];cnb[k]+=b[t];ma[t]=(t&N)?0:a[t];mb[t]=(t&N)?0:b[t];}
    int64_t za=cna[0],zb=cnb[0];double z=ph(za,zb)+ph(A-za,B-zb);if(z<best[1]-1e-9){best[1]=z;bn[1]=N;}
    double zc=0;for(int k=0;k<=m;k++)zc+=ph(cna[k],cnb[k]);if(zc<best[4]-1e-9){best[4]=zc;bn[4]=N;}
    wt(ma,M);wt(mb,M);
    if(full==1)for(int p=0;p<M;p++){
     int64_t x0=(za+ma[p])/2,y0=(zb+mb[p])/2,x1=(za-ma[p])/2,y1=(zb-mb[p])/2;
     double z2=ph(x0,y0)+ph(x1,y1)+ph((A+wa[p])/2-x0,(B+wb[p])/2-y0)+ph((A-wa[p])/2-x1,(B-wb[p])/2-y1);
     if(z2<best[2]-1e-9){best[2]=z2;bp[2]=p;bn[2]=N;}
    }
   }
  }
  double lowest=best[0];for(int k=1;k<5;k++)if(best[k]<lowest)lowest=best[k];out[8]+=lowest;
  for(int k=0;k<5;k++){if(k!=3)out[3+k]+=best[k];if(params){params[(i*5+k)*2]=bp[k];params[(i*5+k)*2+1]=bn[k];}}
 }
 for(int k=0;k<9;k++)out[k]/=den;
}
#ifndef LIBRARY
int main(int argc,char**argv){if(argc!=3)return 2;int n=atoi(argv[1]),L=1<<n;init();FILE*fp=fopen(argv[2],"rb");if(!fp)return 3;uint32_t t;uint64_t count=0;double best[8];uint32_t tt[8];for(int j=0;j<8;j++){best[j]=-1;tt[j]=0;}clock_t start=clock();
 while(fread(&t,4,1,fp)==1){int8_t f[32];for(int x=0;x<L;x++)f[x]=(t>>x&1)?-1:1;double o[9];evaluate(f,n,1,o,0);count++;if(o[0])for(int j=0;j<8;j++){double r=o[j+1]/o[0];if(r>best[j]+1e-12){best[j]=r;tt[j]=t;}}if(count%50000==0){fprintf(stderr,"%llu %.3f CPU seconds\n",(unsigned long long)count,(double)(clock()-start)/CLOCKS_PER_SEC);fflush(stderr);}}
 fclose(fp);struct rusage u;getrusage(RUSAGE_SELF,&u);printf("{\"n\":%d,\"count\":%llu,\"cpu_seconds\":%.6f,\"maxrss_bytes\":%ld,\"nice\":%d,\"threads\":1,\"maxima\":[",n,count,(double)(clock()-start)/CLOCKS_PER_SEC,u.ru_maxrss,getpriority(PRIO_PROCESS,0));for(int j=0;j<8;j++)printf("%s{\"ratio\":%.15g,\"tt\":\"0x%08x\"}",j?",":"",best[j],tt[j]);puts("]}");return 0;}
#endif
