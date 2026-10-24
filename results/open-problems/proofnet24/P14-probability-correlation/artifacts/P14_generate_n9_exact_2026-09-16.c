#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <inttypes.h>

#define MAXN 9

typedef uint64_t u64;
typedef struct {
    unsigned char deg, tri;
    unsigned char nbrdeg[9];
    unsigned char ecn[9];
    unsigned char necn[9];
} VKey;

typedef struct {
    u64 *slot; size_t cap, used;
} USet;

static unsigned long long canon_calls=0, canon_leaves=0, canon_max_leaves=0;

static int edge_index(int i,int j){
    if(i>j){int t=i;i=j;j=t;}
    return j*(j-1)/2+i;
}
static void decode_code(u64 code,int n,uint16_t adj[MAXN]){
    for(int i=0;i<MAXN;i++) adj[i]=0;
    for(int j=1;j<n;j++) for(int i=0;i<j;i++) if((code>>edge_index(i,j))&1ULL){
        adj[i]|=(uint16_t)(1u<<j); adj[j]|=(uint16_t)(1u<<i);
    }
}
static u64 encode_perm(const uint16_t adj[MAXN],int n,const int perm[MAXN]){
    u64 code=0;
    for(int j=1;j<n;j++) for(int i=0;i<j;i++) if((adj[perm[i]]>>perm[j])&1u)
        code |= 1ULL<<edge_index(i,j);
    return code;
}
static int popc16(uint16_t x){ return __builtin_popcount((unsigned)x); }
static int vkeycmp(const VKey *a,const VKey *b){
    if(a->deg!=b->deg) return (int)a->deg-(int)b->deg;
    if(a->tri!=b->tri) return (int)a->tri-(int)b->tri;
    int c=memcmp(a->nbrdeg,b->nbrdeg,9); if(c) return c;
    c=memcmp(a->ecn,b->ecn,9); if(c) return c;
    return memcmp(a->necn,b->necn,9);
}
static void initial_colors(const uint16_t adj[MAXN],int n,int color[MAXN],int *ncolors){
    VKey k[MAXN]; memset(k,0,sizeof(k));
    int deg[MAXN]; for(int v=0;v<n;v++) deg[v]=popc16(adj[v]&((1u<<n)-1));
    for(int v=0;v<n;v++){
        k[v].deg=(unsigned char)deg[v];
        uint16_t nb=adj[v]&((1u<<n)-1);
        int tri2=0;
        for(int u=0;u<n;u++) if(u!=v){
            int cn=popc16(adj[v]&adj[u]&((1u<<n)-1));
            if((nb>>u)&1u){ k[v].nbrdeg[deg[u]]++; k[v].ecn[cn]++; tri2+=cn; }
            else k[v].necn[cn]++;
        }
        k[v].tri=(unsigned char)(tri2/2);
    }
    int ord[MAXN]; for(int i=0;i<n;i++) ord[i]=i;
    for(int i=1;i<n;i++){ int x=ord[i],j=i; while(j>0 && vkeycmp(&k[x],&k[ord[j-1]])<0){ord[j]=ord[j-1];j--;} ord[j]=x; }
    int c=-1;
    for(int ii=0;ii<n;ii++){
        if(ii==0 || vkeycmp(&k[ord[ii]],&k[ord[ii-1]])!=0) c++;
        color[ord[ii]]=c;
    }
    *ncolors=c+1;
}
static void refine_colors(const uint16_t adj[MAXN],int n,int color[MAXN],int *ncolors){
    for(;;){
        int nc=*ncolors;
        struct RKey { unsigned char old; unsigned char cnt[MAXN]; } rk[MAXN];
        memset(rk,0,sizeof(rk));
        for(int v=0;v<n;v++){
            rk[v].old=(unsigned char)color[v];
            for(int u=0;u<n;u++) if((adj[v]>>u)&1u) rk[v].cnt[color[u]]++;
        }
        int ord[MAXN]; for(int i=0;i<n;i++) ord[i]=i;
        #define RCMP(a,b) (rk[(a)].old!=rk[(b)].old ? (int)rk[(a)].old-(int)rk[(b)].old : memcmp(rk[(a)].cnt,rk[(b)].cnt,(size_t)nc))
        for(int i=1;i<n;i++){ int x=ord[i],j=i; while(j>0 && RCMP(x,ord[j-1])<0){ord[j]=ord[j-1];j--;} ord[j]=x; }
        int newc[MAXN], c=-1;
        for(int ii=0;ii<n;ii++){
            if(ii==0 || RCMP(ord[ii],ord[ii-1])!=0) c++;
            newc[ord[ii]]=c;
        }
        #undef RCMP
        int newnc=c+1, same=1;
        for(int v=0;v<n;v++) if(newc[v]!=color[v]){same=0;break;}
        for(int v=0;v<n;v++) color[v]=newc[v];
        *ncolors=newnc;
        if(same || newnc==nc) return;
    }
}

typedef struct {
    const uint16_t *adj; int n;
    int cells[MAXN][MAXN], csz[MAXN], ncells;
    int perm[MAXN]; int pos0[MAXN];
    u64 best; int have;
    unsigned long long leaves;
} Ctx;

static void permute_cell(Ctx *c,int ci,int depth){
    if(ci==c->ncells){
        u64 x=encode_perm(c->adj,c->n,c->perm); c->leaves++;
        if(!c->have || x<c->best){c->best=x;c->have=1;}
        return;
    }
    int sz=c->csz[ci], start=c->pos0[ci];
    int a[MAXN]; for(int i=0;i<sz;i++) a[i]=c->cells[ci][i];
    struct Frame { int k; };
    for(int i=1;i<sz;i++){int x=a[i],j=i;while(j>0&&a[j-1]>x){a[j]=a[j-1];j--;}a[j]=x;}
    for(;;){
        for(int i=0;i<sz;i++) c->perm[start+i]=a[i];
        permute_cell(c,ci+1,0);
        int i=sz-2; while(i>=0 && a[i]>=a[i+1]) i--;
        if(i<0) break;
        int j=sz-1; while(a[j]<=a[i]) j--;
        int t=a[i];a[i]=a[j];a[j]=t;
        for(int l=i+1,r=sz-1;l<r;l++,r--){t=a[l];a[l]=a[r];a[r]=t;}
    }
    (void)depth;
}

static u64 canonical_code(u64 code,int n){
    uint16_t adj[MAXN]; decode_code(code,n,adj);
    int color[MAXN], nc=0; initial_colors(adj,n,color,&nc); refine_colors(adj,n,color,&nc);
    Ctx c; memset(&c,0,sizeof(c)); c.adj=adj;c.n=n;c.ncells=nc;
    int pos=0;
    for(int col=0;col<nc;col++){
        c.pos0[col]=pos;
        for(int v=0;v<n;v++) if(color[v]==col) c.cells[col][c.csz[col]++]=v;
        pos+=c.csz[col];
    }
    permute_cell(&c,0,0);
    canon_calls++; canon_leaves+=c.leaves; if(c.leaves>canon_max_leaves)canon_max_leaves=c.leaves;
    return c.best;
}
static u64 mix64(u64 x){ x^=x>>30;x*=0xbf58476d1ce4e5b9ULL;x^=x>>27;x*=0x94d049bb133111ebULL;x^=x>>31;return x; }
static void set_init(USet *s,size_t cap){s->cap=cap;s->used=0;s->slot=(u64*)calloc(cap,sizeof(u64));if(!s->slot){perror("calloc");exit(2);}}
static int set_add(USet *s,u64 code){
    u64 key=code+1; size_t m=s->cap-1, i=(size_t)mix64(code)&m;
    while(s->slot[i]){if(s->slot[i]==key)return 0;i=(i+1)&m;}
    s->slot[i]=key;s->used++;return 1;
}
static int cmp_u64(const void*a,const void*b){u64 x=*(const u64*)a,y=*(const u64*)b;return x<y?-1:x>y;}
static u64* set_values(USet*s){u64*a=malloc(s->used*sizeof(u64));if(!a){perror("malloc");exit(2);}size_t k=0;for(size_t i=0;i<s->cap;i++)if(s->slot[i])a[k++]=s->slot[i]-1;qsort(a,k,sizeof(u64),cmp_u64);return a;}

static int g6_read(FILE*f,int expected_n,u64 *out){
    char line[128]; if(!fgets(line,sizeof(line),f))return 0; size_t len=strcspn(line,"\r\n");line[len]=0;
    if(!len || (unsigned char)line[0]!=(unsigned char)(63+expected_n)){fprintf(stderr,"bad g6 n\n");exit(3);} int ne=expected_n*(expected_n-1)/2, bp=0;u64 code=0;
    for(size_t ci=1;ci<len&&bp<ne;ci++){int x=(unsigned char)line[ci]-63;if(x<0||x>63){fprintf(stderr,"bad g6 char\n");exit(3);}for(int b=5;b>=0&&bp<ne;b--,bp++)if((x>>b)&1)code|=1ULL<<bp;}
    if(bp<ne){fprintf(stderr,"short g6\n");exit(3);}*out=code;return 1;
}
static void g6_write(FILE*f,u64 code,int n){
    fputc(63+n,f);int ne=n*(n-1)/2;
    for(int p=0;p<ne;p+=6){int x=0;for(int b=0;b<6;b++){x<<=1;if(p+b<ne && ((code>>(p+b))&1ULL))x|=1;}fputc(63+x,f);}fputc('\n',f);
}
static u64 extend_code(u64 parent,int nparent,unsigned mask){
    u64 code=parent; int newv=nparent; for(int i=0;i<nparent;i++)if((mask>>i)&1u)code|=1ULL<<edge_index(i,newv);return code;
}

int main(int argc,char**argv){
    if(argc!=4){fprintf(stderr,"usage: %s n7.g6 n8out.g6 n9out.g6\n",argv[0]);return 2;}
    FILE*f=fopen(argv[1],"r");if(!f){perror("n7");return 2;}
    clock_t t0=clock();
    USet s7;set_init(&s7,1u<<12);u64 c7;size_t n7lines=0;
    while(g6_read(f,7,&c7)){n7lines++;set_add(&s7,canonical_code(c7,7));}
    fclose(f);
    if(n7lines!=1044 || s7.used!=1044){fprintf(stderr,"n7 seed count/isomorphism mismatch lines=%zu unique=%zu\n",n7lines,s7.used);return 4;}
    u64 *v7=set_values(&s7);
    USet s8;set_init(&s8,1u<<16);
    for(size_t ii=0;ii<s7.used;ii++) for(unsigned mask=0;mask<(1u<<7);mask++) set_add(&s8,canonical_code(extend_code(v7[ii],7,mask),8));
    u64 *v8=set_values(&s8);
    FILE*o8=fopen(argv[2],"w");if(!o8){perror("n8out");return 2;}for(size_t i=0;i<s8.used;i++)g6_write(o8,v8[i],8);fclose(o8);
    printf("n7_lines=%zu unique7=%zu candidates8=%zu unique8=%zu expected8=12346\n",n7lines,s7.used,s7.used*(1u<<7),s8.used);fflush(stdout);
    if(s8.used!=12346){fprintf(stderr,"n8 count mismatch\n");return 4;}
    USet s9;set_init(&s9,1u<<20);
    unsigned long long cand9=0;
    for(size_t i=0;i<s8.used;i++){
        for(unsigned mask=0;mask<(1u<<8);mask++){set_add(&s9,canonical_code(extend_code(v8[i],8,mask),9));cand9++;}
        if((i+1)%1000==0){fprintf(stderr,"progress parents8=%zu candidates9=%llu unique9=%zu cpu=%.2f\n",i+1,cand9,s9.used,(double)(clock()-t0)/CLOCKS_PER_SEC);fflush(stderr);}
    }
    u64 *v9=set_values(&s9);
    FILE*o9=fopen(argv[3],"w");if(!o9){perror("n9out");return 2;}for(size_t i=0;i<s9.used;i++)g6_write(o9,v9[i],9);fclose(o9);
    printf("candidates9=%llu unique9=%zu expected9=274668\n",cand9,s9.used);
    printf("canonical_calls=%llu canonical_leaf_permutations=%llu canonical_max_leaves=%llu\n",canon_calls,canon_leaves,canon_max_leaves);
    printf("cpu_seconds=%.6f\n",(double)(clock()-t0)/CLOCKS_PER_SEC);
    free(v7);free(v8);free(v9);free(s7.slot);free(s8.slot);free(s9.slot);
    if(s9.used!=274668){fprintf(stderr,"n9 count mismatch\n");return 5;}
    puts("STATUS PASS");return 0;
}
