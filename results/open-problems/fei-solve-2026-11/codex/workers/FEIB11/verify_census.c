/* Entire NPN5 census: independent integer FWHT/zeta and pow-based q moments. */
#include <stdint.h>
#include <stdio.h>
#include <math.h>
#include <sys/resource.h>
int main(void){
 FILE *f=fopen("npn5.txt","r");if(!f)return 2;
 double qs[7]={1,.5,.25,.1,.05,.01,0},best[7],bal[7];uint32_t arg[7],argb[7];
 for(int k=0;k<7;k++)best[k]=bal[k]=-1;
 unsigned t;int count=0,balanced=0;
 while(fscanf(f,"%x",&t)==1){
  count++;int c[32],m[32],u[32],ii=0;
  for(int x=0;x<32;x++)c[x]=1-2*((t>>x)&1);
  for(int h=1;h<32;h*=2)for(int x=0;x<32;x++)if(!(x&h)){int a=c[x],b=c[x|h];c[x]=a+b;c[x|h]=a-b;}
  for(int s=0;s<32;s++){u[s]=m[s]=c[s]*c[s];ii+=__builtin_popcount(s)*m[s];}
  for(int h=1;h<32;h*=2)for(int s=0;s<32;s++)if(!(s&h))u[s]+=u[s|h];
  if(!ii)continue;double I=ii/1024.;int isbal=c[0]==0&&ii>1024;balanced+=isbal;
  for(int k=0;k<7;k++){
   double M=0,L=0;
   if(k==0){uint64_t num=0;for(int s=0;s<32;s++)num+=(uint64_t)m[s]*u[s];L=-log2(num/1048576.);}
   else if(k==6){for(int s=0;s<32;s++)if(m[s])L+=m[s]/1024.*log2(1024./u[s]);}
   else{for(int s=0;s<32;s++)if(m[s])M+=m[s]/1024.*pow(u[s]/1024.,qs[k]);L=-log2(M)/qs[k];}
   if(L/I>best[k]+1e-12){best[k]=L/I;arg[k]=t;}
   if(isbal&&L/(I-1)>bal[k]+1e-12){bal[k]=L/(I-1);argb[k]=t;}
  }
 }
 fclose(f);struct rusage r;getrusage(RUSAGE_SELF,&r);
 printf("{\"count\":%d,\"balanced_non_dictator_count\":%d,\"nice\":%d,\"max_rss_bytes\":%ld,\"maxima\":[",count,balanced,getpriority(PRIO_PROCESS,0),r.ru_maxrss);
 for(int k=0;k<7;k++)printf("%s{\"q\":%.9g,\"ratio\":%.17g,\"tt_hex\":\"%08x\",\"balanced_ratio\":%.17g,\"balanced_tt_hex\":\"%08x\"}",k?",":"",qs[k],best[k],arg[k],bal[k],argb[k]);
 puts("]}");return count==616126?0:3;
}
