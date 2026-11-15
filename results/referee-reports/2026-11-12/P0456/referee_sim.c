/* Exact rank-permutation sampler for iid continuous scores, independently written.
   Generate uniformly random unseen edges until all vertices have K incidences.
   Each vertex's first K incidences are then its K preferred edges. */
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <time.h>
#include <sys/resource.h>

static uint64_t state;
static uint64_t random64(void) {
    uint64_t z=(state+=UINT64_C(0x9e3779b97f4a7c15));
    z=(z^(z>>30))*UINT64_C(0xbf58476d1ce4e5b9);
    z=(z^(z>>27))*UINT64_C(0x94d049bb133111eb);
    return z^(z>>31);
}
static uint64_t mix(uint64_t z) {
    z=(z^(z>>30))*UINT64_C(0xbf58476d1ce4e5b9);
    z=(z^(z>>27))*UINT64_C(0x94d049bb133111eb);
    return z^(z>>31);
}
static unsigned bounded(unsigned n) {
    uint64_t r,threshold=(-((uint64_t)n))%n;
    do {r=random64();} while(r<threshold);
    return (unsigned)(r%n);
}
typedef struct {int u,v,rank;} Edge;
static int find(int *p,int x) {
    while(p[x]!=x) {p[x]=p[p[x]];x=p[x];} return x;
}
static double se(double sum,double sumsq,int t) {
    return t>1?sqrt(fmax(0.,(sumsq-sum*sum/t)/(t-1)/t)):0.;
}
int main(int argc,char **argv) {
    if(argc!=5&&argc!=6) {fprintf(stderr,"usage: referee_sim n trials seed raw.csv [minimum_k]\n");return 2;}
    int n=atoi(argv[1]),trials=atoi(argv[2]);state=strtoull(argv[3],0,10);
    int lo=(int)floor(log(n))-1,hi=lo+3;
    if(argc==6) {lo=atoi(argv[5]);hi=lo+3;}
    if(n<20) {lo=1;hi=n-1;}
    int nk=hi-lo+1;
    if(n<3||n>50000||nk>20) return 2;
    size_t cap=1;
    while(cap<(size_t)n*hi*8 && cap<((size_t)n*(n-1)*4))cap*=2;
    uint64_t *hash=calloc(cap,sizeof(*hash));
    int *deg=calloc(n,sizeof(int)),*p=malloc(n*sizeof(int)),*sz=malloc(n*sizeof(int)),*kept=malloc(n*sizeof(int));
    Edge *edges=malloc((size_t)n*hi*sizeof(Edge));
    int *hist=calloc((size_t)nk*(n+1),sizeof(int));
    double sums[20]={0},sqs[20]={0},facts[20]={0},factqs[20]={0};
    int conn[20]={0},zero[20]={0},bad[20]={0};
    FILE *raw=fopen(argv[4],"w"); if(!raw||!hash||!edges||!hist)return 3;
    fprintf(raw,"trial,n,k,Z,components\n");
    time_t start=time(0);int done=0;size_t maxdraws=0;
    for(int t=0;t<trials;t++) {
        memset(hash,0,cap*sizeof(*hash));memset(deg,0,n*sizeof(int));
        int left=n,ne=0;size_t draws=0;
        while(left) {
            unsigned u=bounded(n),v=bounded(n);if(u==v)continue;
            if(u>v) {unsigned q=u;u=v;v=q;}
            uint64_t key=(uint64_t)u*n+v+1;size_t pos=mix(key)&(cap-1);
            while(hash[pos]&&hash[pos]!=key)pos=(pos+1)&(cap-1);
            if(hash[pos])continue;
            hash[pos]=key;draws++;
            if(draws>cap/2) {fprintf(stderr,"hash occupancy safety stop\n");return 4;}
            if(deg[u]<hi&&deg[v]<hi) {
                edges[ne++]=(Edge){(int)u,(int)v,1+(deg[u]>deg[v]?deg[u]:deg[v])};
            }
            if(deg[u]<hi&&++deg[u]==hi)left--;
            if(deg[v]<hi&&++deg[v]==hi)left--;
        }
        if(draws>maxdraws)maxdraws=draws;
        for(int k=lo;k<=hi;k++) {
            for(int i=0;i<n;i++) {p[i]=i;sz[i]=1;kept[i]=0;}
            int nc=n;
            for(int j=0;j<ne;j++)if(edges[j].rank<=k) {
                int u=edges[j].u,v=edges[j].v;kept[u]++;kept[v]++;
                int x=find(p,u),y=find(p,v);
                if(x!=y) {if(sz[x]<sz[y]){int q=x;x=y;y=q;}p[y]=x;sz[x]+=sz[y];nc--;}
            }
            int z=0;for(int i=0;i<n;i++)z+=(kept[i]==0);
            int q=k-lo;double f=(double)z*(z-1);
            sums[q]+=z;sqs[q]+=(double)z*z;facts[q]+=f;factqs[q]+=f*f;
            conn[q]+=(nc==1);zero[q]+=(z==0);bad[q]+=(z==0&&nc!=1);
            hist[(size_t)q*(n+1)+z]++;
            fprintf(raw,"%d,%d,%d,%d,%d\n",t,n,k,z,nc);
        }
        done++;
        if(time(0)-start>=235)break;
    }
    fclose(raw);
    for(int k=lo;k<=hi;k++) {
        int q=k-lo;double lambda=n*exp(-k),pc=(double)conn[q]/done;
        double scale=lambda*lambda*(n-1.)/n;
        double tv=0.,pm=exp(-lambda);
        for(int z=0;z<=n;z++) {tv+=fabs((double)hist[(size_t)q*(n+1)+z]/done-pm);pm*=lambda/(z+1.);}
        printf("n=%d k=%d T=%d lambda=%.6f mean=%.6f meanSE=%.6f var=%.6f p1ratio=%.6f p1ratioSE=%.6f p2ratio=%.6f p2ratioSE=%.6f conn=%.6f connSE=%.6f limit=%.6f p0=%.6f noiso_disconnected=%d empiricalTV=%.6f\n",
            n,k,done,lambda,sums[q]/done,se(sums[q],sqs[q],done),
            (sqs[q]-sums[q]*sums[q]/done)/(done-1),sums[q]/done/lambda,se(sums[q],sqs[q],done)/lambda,
            facts[q]/done/scale,se(facts[q],factqs[q],done)/scale,pc,sqrt(pc*(1-pc)/done),exp(-lambda),(double)zero[q]/done,bad[q],tv/2);
    }
    struct rusage usage;getrusage(RUSAGE_SELF,&usage);
    printf("elapsed_seconds=%ld max_unseen_edges=%zu hash_bytes=%zu maxrss_bytes=%ld seed=%s\n",(long)(time(0)-start),maxdraws,cap*sizeof(*hash),usage.ru_maxrss,argv[3]);
    free(hash);free(deg);free(p);free(sz);free(kept);free(edges);free(hist);return 0;
}
