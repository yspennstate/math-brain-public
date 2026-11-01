#include <assert.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define NV 8
#define NE 28
#define NG 720
#define FULL_MASK ((uint32_t)((1ULL<<NE)-1ULL))

typedef struct { uint32_t *a; size_t n, cap; } Vec;

static int eidx[NV][NV];
static int eu[NE], ev[NE];
static uint32_t pmap[NG][NE];
static int perms[NG][NV];
static int ng = 0;
static int64_t binomc[29][29];

static int cmp_u32(const void *A, const void *B){
    uint32_t a=*(const uint32_t*)A, b=*(const uint32_t*)B;
    return (a>b)-(a<b);
}

static void vec_push(Vec *v, uint32_t x){
    if(v->n==v->cap){ v->cap = v->cap? 2*v->cap : 128; v->a = (uint32_t*)realloc(v->a, v->cap*sizeof(uint32_t)); assert(v->a); }
    v->a[v->n++]=x;
}

static void init_edges(void){
    memset(eidx,-1,sizeof(eidx));
    int k=0;
    for(int i=0;i<NV;i++) for(int j=i+1;j<NV;j++){
        eu[k]=i; ev[k]=j; eidx[i][j]=eidx[j][i]=k; k++;
    }
    assert(k==NE);
}

static void gen_perm_rec(int pos, int used[6], int arr[6]){
    if(pos==6){
        int *p=perms[ng];
        p[0]=0; p[1]=1;
        for(int i=0;i<6;i++) p[i+2]=arr[i]+2;
        ng++; return;
    }
    for(int x=0;x<6;x++) if(!used[x]){ used[x]=1; arr[pos]=x; gen_perm_rec(pos+1,used,arr); used[x]=0; }
}

static void init_perms(void){
    int used[6]={0}, arr[6];
    gen_perm_rec(0,used,arr);
    assert(ng==NG);
    for(int g=0;g<NG;g++) for(int e=0;e<NE;e++){
        int a=perms[g][eu[e]], b=perms[g][ev[e]];
        int j=eidx[a][b]; assert(j>=0);
        pmap[g][e]=(uint32_t)1u<<j;
    }
}

static uint32_t permute_mask(uint32_t x, int g){
    uint32_t y=0, z=x;
    while(z){ int e=__builtin_ctz(z); z &= z-1; y |= pmap[g][e]; }
    return y;
}

static uint32_t canonical(uint32_t x){
    uint32_t best=x;
    for(int g=1;g<NG;g++){ uint32_t y=permute_mask(x,g); if(y<best) best=y; }
    return best;
}

static int64_t choosei(int n,int k){ if(k<0||k>n) return 0; return binomc[n][k]; }

static void init_binom(void){
    memset(binomc,0,sizeof(binomc));
    for(int n=0;n<=28;n++){ binomc[n][0]=binomc[n][n]=1; for(int k=1;k<n;k++) binomc[n][k]=binomc[n-1][k-1]+binomc[n-1][k]; }
}

static Vec next_orbits(const Vec *prev){
    Vec cand={0};
    for(size_t i=0;i<prev->n;i++){
        uint32_t x=prev->a[i];
        for(int e=0;e<NE;e++) if(!(x & ((uint32_t)1u<<e))) vec_push(&cand, canonical(x|((uint32_t)1u<<e)));
    }
    qsort(cand.a,cand.n,sizeof(uint32_t),cmp_u32);
    size_t w=0;
    for(size_t i=0;i<cand.n;i++) if(i==0||cand.a[i]!=cand.a[i-1]) cand.a[w++]=cand.a[i];
    cand.n=w;
    return cand;
}

static int orbit_size(uint32_t rep){
    int stab=0;
    for(int g=0;g<NG;g++) if(permute_mask(rep,g)==rep) stab++;
    assert(stab>0 && NG%stab==0);
    return NG/stab;
}

static int connected(uint32_t mask){
    uint8_t adj[NV]={0};
    for(int e=0;e<NE;e++) if(mask&((uint32_t)1u<<e)){ adj[eu[e]]|=(uint8_t)(1u<<ev[e]); adj[ev[e]]|=(uint8_t)(1u<<eu[e]); }
    uint8_t seen=1, frontier=1;
    while(frontier){
        uint8_t nxt=0;
        for(int v=0;v<NV;v++) if(frontier&(1u<<v)) nxt |= adj[v];
        nxt &= (uint8_t)~seen; seen |= nxt; frontier=nxt;
    }
    return seen==0xff;
}

static uint32_t complete_mask_n(int n){
    uint32_t m=0; for(int i=0;i<n;i++) for(int j=i+1;j<n;j++) m|=(uint32_t)1u<<eidx[i][j]; return m;
}

static int in_I0(int n,int m){ int c=(n-1)*(n-2)/2; return c+2<=m && m<=n*(n-1)/2; }

static uint32_t balloon(int n,int m){
    if(in_I0(n,m)){
        uint32_t E=complete_mask_n(n-1); int c=(n-1)*(n-2)/2; int r=m-c;
        for(int u=0;u<r;u++) E|=(uint32_t)1u<<eidx[n-1][u];
        return E;
    }
    if(n==4 && m==4) return ((uint32_t)1u<<eidx[0][1])|((uint32_t)1u<<eidx[0][2])|((uint32_t)1u<<eidx[1][2])|((uint32_t)1u<<eidx[0][3]);
    uint32_t E=balloon(n-1,m-1); int deg[NV]={0};
    for(int e=0;e<NE;e++) if(E&((uint32_t)1u<<e)){ if(eu[e]<n-1)deg[eu[e]]++; if(ev[e]<n-1)deg[ev[e]]++; }
    int u=0; for(int v=1;v<n-1;v++) if(deg[v]<deg[u]) u=v;
    E|=(uint32_t)1u<<eidx[u][n-1]; return E;
}

static void all_dist(uint32_t E,int s,int d[NV]){
    for(int i=0;i<NV;i++) d[i]=-1;
    d[s]=0;
    int q[NV],h=0,t=0;q[t++]=s;
    while(h<t){int u=q[h++]; for(int e=0;e<NE;e++) if(E&((uint32_t)1u<<e)){
        int v=-1; if(eu[e]==u)v=ev[e]; else if(ev[e]==u)v=eu[e];
        if(v>=0&&d[v]<0){d[v]=d[u]+1;q[t++]=v;}
    }}
}

static void diameter_pair(uint32_t E,int *S,int *T){
    int best=-1,bs=0,bt=1,d[NV];
    for(int s=0;s<NV;s++){ all_dist(E,s,d); for(int t=s+1;t<NV;t++) if(d[t]>best){best=d[t];bs=s;bt=t;} }
    *S=bs;*T=bt;
}

static uint32_t relabel_terminals(uint32_t E,int s,int t){
    int mapv[NV],nxt=2; mapv[s]=0;mapv[t]=1;
    for(int v=0;v<NV;v++) if(v!=s&&v!=t) mapv[v]=nxt++;
    uint32_t R=0;
    for(int e=0;e<NE;e++) if(E&((uint32_t)1u<<e)) R|=(uint32_t)1u<<eidx[mapv[eu[e]]][mapv[ev[e]]];
    return R;
}

static void poly_mul_binom_add(int64_t out[29], const int64_t *a, int adeg, int e, int sign){
    for(int i=0;i<=adeg;i++) if(a[i]) for(int j=0;j<=e;j++) out[i+j]+=sign*a[i]*choosei(e,j);
}

static void split_vector(uint32_t E,int64_t ans[29]){
    static int64_t C[256][29];
    memset(C,0,sizeof(C));
    uint32_t induced[256];
    for(int S=0;S<256;S++){
        uint32_t im=0; for(int e=0;e<NE;e++) if((E&((uint32_t)1u<<e)) && (S&(1u<<eu[e])) && (S&(1u<<ev[e]))) im|=(uint32_t)1u<<e;
        induced[S]=im;
    }
    for(int sz=1;sz<=NV;sz++) for(int S=1;S<256;S++) if(__builtin_popcount((unsigned)S)==sz){
        int eS=__builtin_popcount(induced[S]);
        for(int j=0;j<=eS;j++) C[S][j]=choosei(eS,j);
        int r=__builtin_ctz((unsigned)S); int root=1<<r; int rest=S^root;
        for(int sub=rest;;sub=(sub-1)&rest){
            int T=root|sub;
            if(T!=S){ int U=S^T; int eU=__builtin_popcount(induced[U]); int degT=__builtin_popcount(induced[T]); poly_mul_binom_add(C[S],C[T],degT,eU,-1); }
            if(sub==0) break;
        }
        for(int j=0;j<29;j++) assert(C[S][j]>=0 && C[S][j]<(1LL<<31));
    }
    memset(ans,0,29*sizeof(int64_t));
    for(int S=0;S<256;S++) if((S&1)&&!(S&2)){
        int U=255^S;
        int d1=__builtin_popcount(induced[S]), d2=__builtin_popcount(induced[U]);
        for(int i=0;i<=d1;i++) if(C[S][i]) for(int j=0;j<=d2;j++) if(C[U][j]) ans[i+j]+=C[S][i]*C[U][j];
    }
    for(int j=0;j<29;j++) assert(ans[j]>=0 && ans[j]<(1LL<<40));
}

int main(void){
    init_edges(); init_perms(); init_binom();
    Vec reps[9]={0}; reps[0].a=malloc(sizeof(uint32_t)); reps[0].a[0]=0; reps[0].n=reps[0].cap=1;
    const int expect[9]={1,4,13,43,137,419,1189,3021,6860};
    printf("ROMERO-2025-SPLIT8 exact full-layer certificate\n");
    printf("orbit certificate verified by constructive generation + orbit-stabilizer:\n");
    for(int k=1;k<=8;k++){
        reps[k]=next_orbits(&reps[k-1]);
        assert((int)reps[k].n==expect[k]);
        int64_t sum=0; for(size_t i=0;i<reps[k].n;i++){ assert(canonical(reps[k].a[i])==reps[k].a[i]); assert(__builtin_popcount(reps[k].a[i])==k); sum+=orbit_size(reps[k].a[i]); }
        assert(sum==choosei(NE,k));
        if(k>=2) printf("k=%d orbits=%zu total_labeled=%lld\n",k,reps[k].n,(long long)sum);
    }
    printf("m  missing  connected_orbits  split_vector_ties  violations\n");
    int total_viol=0;
    for(int m=20;m<=26;m++){
        int k=NE-m; uint32_t B=balloon(8,m); int s,t; diameter_pair(B,&s,&t); B=relabel_terminals(B,s,t);
        assert(__builtin_popcount(B)==m && connected(B));
        int64_t bv[29]; split_vector(B,bv);
        int conn=0,ties=0,viol=0;
        for(size_t i=0;i<reps[k].n;i++){
            uint32_t G=FULL_MASK ^ reps[k].a[i]; if(!connected(G)) continue; conn++;
            int64_t gv[29]; split_vector(G,gv); int bad=0,eq=1;
            for(int j=0;j<29;j++){ if(gv[j]>bv[j]) bad=1; if(gv[j]!=bv[j]) eq=0; }
            if(bad) viol++;
            if(eq) ties++;
        }
        printf("%2d %8d %17d %18d %11d\n",m,k,conn,ties,viol); total_viol+=viol;
    }
    assert(total_viol==0);
    printf("PASS: coefficientwise domination for every connected two-terminal orbit, m=20,...,26.\n");
    printf("Therefore diameter-terminal balloons are uniformly most split reliable in T_{8,m}, m=20,...,26.\n");
    printf("With the prior exact m=14,...,19 nonexistence certificates, all 13 n=8 classes are decided.\n");
    for(int k=0;k<=8;k++) free(reps[k].a);
    return 0;
}
