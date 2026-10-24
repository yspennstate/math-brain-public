#include <assert.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define N 8
#define M 28
#define GP 720
#define ALL ((uint32_t)((1ULL<<28)-1ULL))

typedef struct { uint32_t *x; size_t n,cap; } V;
static int ei[N][N], eu[M], ev[M], perm[GP][N], np;
static uint32_t emap[GP][M];
static long long Cbin[29][29];

static void push(V *v,uint32_t x){ if(v->n==v->cap){v->cap=v->cap?2*v->cap:64;v->x=realloc(v->x,v->cap*sizeof(uint32_t));assert(v->x);} v->x[v->n++]=x; }
static int cmp32(const void*a,const void*b){uint32_t x=*(const uint32_t*)a,y=*(const uint32_t*)b;return x<y?-1:x>y;}
static void init_edges(void){memset(ei,-1,sizeof(ei));int q=0;for(int i=0;i<N;i++)for(int j=i+1;j<N;j++){ei[i][j]=ei[j][i]=q;eu[q]=i;ev[q]=j;q++;}assert(q==M);}
static void pg(int d,int used[6],int a[6]){if(d==6){perm[np][0]=0;perm[np][1]=1;for(int i=0;i<6;i++)perm[np][i+2]=a[i]+2;np++;return;}for(int y=0;y<6;y++)if(!used[y]){used[y]=1;a[d]=y;pg(d+1,used,a);used[y]=0;}}
static void init_group(void){int u[6]={0},a[6];pg(0,u,a);assert(np==GP);for(int g=0;g<GP;g++)for(int e=0;e<M;e++)emap[g][e]=1u<<ei[perm[g][eu[e]]][perm[g][ev[e]]];}
static uint32_t act(uint32_t s,int g){uint32_t r=0;while(s){int e=__builtin_ctz(s);s&=s-1;r|=emap[g][e];}return r;}
static uint32_t canon(uint32_t s){uint32_t b=s;for(int g=1;g<GP;g++){uint32_t t=act(s,g);if(t<b)b=t;}return b;}
static int orbit_sz(uint32_t s){int st=0;for(int g=0;g<GP;g++)st+=act(s,g)==s;assert(st&&GP%st==0);return GP/st;}
static V extend(V *p){V z={0};for(size_t i=0;i<p->n;i++)for(int e=0;e<M;e++)if(!(p->x[i]&(1u<<e)))push(&z,canon(p->x[i]|(1u<<e)));qsort(z.x,z.n,sizeof(uint32_t),cmp32);size_t w=0;for(size_t i=0;i<z.n;i++)if(!i||z.x[i]!=z.x[i-1])z.x[w++]=z.x[i];z.n=w;return z;}
static int connected(uint32_t E){uint8_t adj[N]={0};for(int e=0;e<M;e++)if(E&(1u<<e)){adj[eu[e]]|=1u<<ev[e];adj[ev[e]]|=1u<<eu[e];}uint8_t seen=1,fr=1;while(fr){uint8_t q=0;for(int v=0;v<N;v++)if(fr&(1u<<v))q|=adj[v];q&=~seen;seen|=q;fr=q;}return seen==255;}
static void init_bin(void){for(int n=0;n<=28;n++){Cbin[n][0]=Cbin[n][n]=1;for(int k=1;k<n;k++)Cbin[n][k]=Cbin[n-1][k-1]+Cbin[n-1][k];}}
static long long ch(int n,int k){return k<0||k>n?0:Cbin[n][k];}

static uint32_t Kmask(int n){uint32_t E=0;for(int i=0;i<n;i++)for(int j=i+1;j<n;j++)E|=1u<<ei[i][j];return E;}
static int dense_regime(int n,int m){int c=(n-1)*(n-2)/2;return c+2<=m && m<=n*(n-1)/2;}
static uint32_t balloon(int n,int m){
 if(dense_regime(n,m)){uint32_t E=Kmask(n-1);int c=(n-1)*(n-2)/2,r=m-c;for(int u=0;u<r;u++)E|=1u<<ei[n-1][u];return E;}
 if(n==4&&m==4)return (1u<<ei[0][1])|(1u<<ei[0][2])|(1u<<ei[1][2])|(1u<<ei[0][3]);
 uint32_t E=balloon(n-1,m-1);int deg[N]={0};for(int e=0;e<M;e++)if(E&(1u<<e)){if(eu[e]<n-1)deg[eu[e]]++;if(ev[e]<n-1)deg[ev[e]]++;}int u=0;for(int v=1;v<n-1;v++)if(deg[v]<deg[u])u=v;E|=1u<<ei[u][n-1];return E;
}
static void dist(uint32_t E,int s,int d[N]){for(int i=0;i<N;i++)d[i]=-1;int q[N],h=0,t=0;d[s]=0;q[t++]=s;while(h<t){int u=q[h++];for(int e=0;e<M;e++)if(E&(1u<<e)){int v=eu[e]==u?ev[e]:ev[e]==u?eu[e]:-1;if(v>=0&&d[v]<0){d[v]=d[u]+1;q[t++]=v;}}}}
static void diam(uint32_t E,int *s,int *t){int bd=-1,d[N];*s=0;*t=1;for(int a=0;a<N;a++){dist(E,a,d);for(int b=a+1;b<N;b++)if(d[b]>bd){bd=d[b];*s=a;*t=b;}}}
static uint32_t relabel(uint32_t E,int s,int t){int f[N],q=2;f[s]=0;f[t]=1;for(int v=0;v<N;v++)if(v!=s&&v!=t)f[v]=q++;uint32_t R=0;for(int e=0;e<M;e++)if(E&(1u<<e))R|=1u<<ei[f[eu[e]]][f[ev[e]]];return R;}

static void splitvec(uint32_t E,long long ans[29]){
 static long long cc[256][29]; uint32_t ind[256]; memset(cc,0,sizeof(cc));
 for(int S=0;S<256;S++){uint32_t x=0;for(int e=0;e<M;e++)if((E&(1u<<e))&&(S&(1u<<eu[e]))&&(S&(1u<<ev[e])))x|=1u<<e;ind[S]=x;}
 for(int sz=1;sz<=N;sz++)for(int S=1;S<256;S++)if(__builtin_popcount((unsigned)S)==sz){
   int es=__builtin_popcount(ind[S]);for(int j=0;j<=es;j++)cc[S][j]=ch(es,j);
   int root=1u<<__builtin_ctz((unsigned)S), rest=S^root;
   for(int sub=rest;;sub=(sub-1)&rest){int T=root|sub;if(T!=S){int U=S^T,euq=__builtin_popcount(ind[U]),dt=__builtin_popcount(ind[T]);for(int i=0;i<=dt;i++)if(cc[T][i])for(int j=0;j<=euq;j++)cc[S][i+j]-=cc[T][i]*ch(euq,j);}if(sub==0)break;}
   for(int j=0;j<29;j++)assert(cc[S][j]>=0);
 }
 memset(ans,0,29*sizeof(long long));
 for(int S=0;S<256;S++)if((S&1)&&!(S&2)){int U=255^S,d1=__builtin_popcount(ind[S]),d2=__builtin_popcount(ind[U]);for(int i=0;i<=d1;i++)if(cc[S][i])for(int j=0;j<=d2;j++)if(cc[U][j])ans[i+j]+=cc[S][i]*cc[U][j];}
}

static long long det6(uint32_t E,int s,int t){ long long A[6][6]; int map[6],q=0; for(int v=0;v<N;v++)if(v!=s&&v!=t)map[q++]=v; assert(q==6);
 for(int i=0;i<6;i++)for(int j=0;j<6;j++){int u=map[i],v=map[j]; if(i==j){int d=0;for(int w=0;w<N;w++)if(w!=u&&(E&(1u<<ei[u][w])))d++;A[i][j]=d;}else A[i][j]=(E&(1u<<ei[u][v]))?-1:0;}
 long long sign=1,prev=1; for(int k=0;k<5;k++){int p=k;while(p<6&&A[p][k]==0)p++;assert(p<6);if(p!=k){for(int j=k;j<6;j++){long long z=A[k][j];A[k][j]=A[p][j];A[p][j]=z;}sign=-sign;}long long piv=A[k][k];for(int i=k+1;i<6;i++)for(int j=k+1;j<6;j++){long long num=A[i][j]*piv-A[i][k]*A[k][j];assert(num%prev==0);A[i][j]=num/prev;}prev=piv;for(int i=k+1;i<6;i++)A[i][k]=0;} return sign*A[5][5]; }
static uint32_t deladd(uint32_t E,int a,int b,int c,int d){assert(E&(1u<<ei[a][b]));E&=~(1u<<ei[a][b]);assert(!(E&(1u<<ei[c][d])));E|=1u<<ei[c][d];return E;}
static uint32_t contract56_sub01(uint32_t E){
 assert(E&(1u<<ei[5][6])); uint32_t R=E; R&=~(1u<<ei[5][6]);
 for(int v=0;v<N;v++)if(v!=5&&v!=6){uint32_t b=1u<<ei[6][v];if(R&b){R&=~b;R|=1u<<ei[5][v];}}
 assert(R&(1u<<ei[0][1]));R&=~(1u<<ei[0][1]);R|=1u<<ei[0][6];R|=1u<<ei[1][6];return R;
}

int main(void){
 init_edges();init_group();init_bin();
 const long long exG[6]={840,1404,2160,3024,5292,8232}, exH[6]={900,1440,2592,3780,5880,8575};
 const int ss[6]={2,3,5,1,2,3}, tt[6]={7,7,7,7,7,7};
 for(int idx=0;idx<6;idx++){int m=14+idx;uint32_t G=balloon(8,m),H; if(m<=15)H=contract56_sub01(G); else if(m==16)H=deladd(G,2,4,2,6); else if(m==17)H=deladd(G,0,1,4,6); else if(m==18)H=deladd(G,0,1,4,6); else H=deladd(G,3,4,4,6); assert(__builtin_popcount(G)==m&&__builtin_popcount(H)==m&&connected(G)&&connected(H)); long long a=det6(G,ss[idx],tt[idx]),b=det6(H,ss[idx],tt[idx]); printf("m=%d N6 balloon=%lld competitor=%lld\n",m,a,b);assert(a==exG[idx]&&b==exH[idx]&&b>a);}
 V r[9]={0};r[0].x=malloc(sizeof(uint32_t));r[0].x[0]=0;r[0].n=r[0].cap=1;const int expn[9]={1,4,13,43,137,419,1189,3021,6860};
 for(int k=1;k<=8;k++){r[k]=extend(&r[k-1]);assert((int)r[k].n==expn[k]);long long tot=0;for(size_t i=0;i<r[k].n;i++)tot+=orbit_sz(r[k].x[i]);assert(tot==ch(28,k));}
 int viol=0; for(int m=20;m<=26;m++){int k=28-m,s,t,conn=0,ties=0;uint32_t B=balloon(8,m);diam(B,&s,&t);B=relabel(B,s,t);long long bv[29];splitvec(B,bv);for(size_t i=0;i<r[k].n;i++){uint32_t G=ALL^r[k].x[i];if(!connected(G))continue;conn++;long long gv[29];splitvec(G,gv);int eq=1,bad=0;for(int j=0;j<29;j++){if(gv[j]!=bv[j])eq=0;if(gv[j]>bv[j])bad=1;}ties+=eq;viol+=bad;}printf("m=%d connected_orbits=%d ties=%d\n",m,conn,ties);}
 assert(viol==0);printf("R01_ROMERO_SPLIT8_INDEPENDENT_EXACT_AUDIT_PASS\n");for(int k=0;k<=8;k++)free(r[k].x);return 0;
}
