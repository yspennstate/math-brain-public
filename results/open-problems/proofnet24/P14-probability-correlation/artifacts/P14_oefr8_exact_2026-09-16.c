#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <limits.h>

#define N 8
#define MAXE 28
#define MAXP 378
#define MOD 1000000007LL

typedef long long i64;
typedef unsigned long long u64;
typedef __int128 i128;

typedef struct { u64 Z; u64 ze[MAXE]; u64 zef[MAXP]; } Stats;

static uint32_t tau_[1<<N];
static uint32_t te_[MAXE][1<<N];
static uint32_t tp_[MAXP][1<<N];
static u64 forest_[1<<N];
static int eu[MAXE], ev[MAXE], ew[MAXE], pair_index[MAXE][MAXE], pu[MAXP], pv[MAXP];
static i64 invmat[7][7];
static int m_global;

static i64 modnorm(i64 x){ x%=MOD; if(x<0)x+=MOD; return x; }
static i64 invmod(i64 a){
    i64 b=MOD,u=1,v=0;
    while(b){ i64 t=a/b; i64 na=a-t*b; a=b;b=na; i64 nu=u-t*v; u=v;v=nu; }
    return modnorm(u);
}

static uint32_t tree_data(unsigned mask){
    int verts[N], idx[N]; int k=0;
    for(int i=0;i<N;i++) idx[i]=-1;
    for(int i=0;i<N;i++) if(mask>>i&1u) verts[k++]=i;
    if(k==0) return 0;
    if(k==1) return 1;
    int root=verts[k-1], d=k-1;
    i64 a[7][7], b[7][7]; memset(a,0,sizeof(a)); memset(b,0,sizeof(b));
    for(int i=0;i<d;i++) idx[verts[i]]=i;
    for(int e=0;e<m_global;e++) if(ew[e]>0 && ((mask>>eu[e])&1u) && ((mask>>ev[e])&1u)){
        int u=eu[e],v=ev[e]; i64 w=ew[e];
        if(u!=root){ int iu=idx[u]; a[iu][iu]=modnorm(a[iu][iu]+w); }
        if(v!=root){ int iv=idx[v]; a[iv][iv]=modnorm(a[iv][iv]+w); }
        if(u!=root && v!=root){ int iu=idx[u],iv=idx[v]; a[iu][iv]=modnorm(a[iu][iv]-w); a[iv][iu]=modnorm(a[iv][iu]-w); }
    }
    for(int i=0;i<d;i++) b[i][i]=1;
    i64 det=1; int sign=1;
    for(int col=0;col<d;col++){
        int pr=col; while(pr<d && a[pr][col]==0) pr++;
        if(pr==d) return 0;
        if(pr!=col){
            for(int j=0;j<d;j++){ i64 t=a[pr][j];a[pr][j]=a[col][j];a[col][j]=t; t=b[pr][j];b[pr][j]=b[col][j];b[col][j]=t; }
            sign=-sign;
        }
        i64 piv=a[col][col]; det=det*piv%MOD; i64 ip=invmod(piv);
        for(int j=0;j<d;j++){ a[col][j]=a[col][j]*ip%MOD; b[col][j]=b[col][j]*ip%MOD; }
        for(int r=0;r<d;r++) if(r!=col){
            i64 f=a[r][col]; if(!f) continue;
            for(int j=0;j<d;j++){
                a[r][j]=modnorm(a[r][j]-f*a[col][j]);
                b[r][j]=modnorm(b[r][j]-f*b[col][j]);
            }
        }
    }
    if(sign<0) det=modnorm(-det);
    if(det<=0 || det>10000000){ fprintf(stderr,"bad weighted tau det=%lld mask=%u\n",det,mask); exit(3); }
    uint32_t tau=(uint32_t)det;
    for(int i=0;i<d;i++)for(int j=0;j<d;j++)invmat[i][j]=b[i][j];
    i64 raw[MAXE]; int inside[MAXE]; int ni=0;
    memset(raw,0,sizeof(raw));
    for(int e=0;e<m_global;e++) if(ew[e]>0){
        if(((mask>>eu[e])&1u)&&((mask>>ev[e])&1u)){
            inside[ni++]=e;
            int u=eu[e],v=ev[e]; i64 val=0;
            if(u!=root){ int iu=idx[u]; val += invmat[iu][iu]; }
            if(v!=root){ int iv=idx[v]; val += invmat[iv][iv]; }
            if(u!=root && v!=root){ int iu=idx[u],iv=idx[v]; val -= invmat[iu][iv]; val -= invmat[iv][iu]; }
            raw[e]=modnorm(val);
            i64 q=det*raw[e]%MOD*ew[e]%MOD;
            if(q<0 || q>(i64)tau){ fprintf(stderr,"bad te q=%lld tau=%u e=%d w=%d\n",q,tau,e,ew[e]); exit(4); }
            te_[e][mask]=(uint32_t)q;
        }
    }
    for(int aa=0;aa<ni;aa++) for(int bb=aa+1;bb<ni;bb++){
        int e=inside[aa], f=inside[bb], pi=pair_index[e][f];
        int us[2]={eu[e],ev[e]}, vs[2]={eu[f],ev[f]};
        int cs[2]={1,-1}, ds[2]={1,-1};
        i64 cross=0;
        for(int x=0;x<2;x++) if(us[x]!=root) for(int y=0;y<2;y++) if(vs[y]!=root){
            cross += (i64)cs[x]*ds[y]*invmat[idx[us[x]]][idx[vs[y]]];
        }
        cross=modnorm(cross);
        i64 val=modnorm(raw[e]*raw[f]%MOD - cross*cross%MOD);
        i64 q2=det*val%MOD*ew[e]%MOD*ew[f]%MOD;
        if(q2<0 || q2>(i64)tau){ fprintf(stderr,"bad tp q2=%lld tau=%u e=%d f=%d\n",q2,tau,e,f); exit(5); }
        tp_[pi][mask]=(uint32_t)q2;
    }
    return tau;
}

static void compute_stats(int special_g, int special_w, Stats *st){
    for(int e=0;e<m_global;e++) ew[e]=1;
    if(special_g>=0) ew[special_g]=special_w;
    memset(tau_,0,sizeof(tau_)); memset(te_,0,sizeof(te_)); memset(tp_,0,sizeof(tp_));
    for(unsigned mask=1;mask<(1u<<N);mask++) tau_[mask]=tree_data(mask);
    forest_[0]=1;
    for(unsigned mask=1;mask<(1u<<N);mask++){
        unsigned lb=mask & -mask, rest=mask^lb; u64 sum=0;
        for(unsigned x=rest;;x=(x-1)&rest){ unsigned T=x|lb; sum += (u64)tau_[T]*forest_[mask^T]; if(x==0)break; }
        forest_[mask]=sum;
    }
    unsigned full=(1u<<N)-1; st->Z=forest_[full];
    for(int e=0;e<m_global;e++) st->ze[e]=0;
    for(int p=0;p<m_global*(m_global-1)/2;p++) st->zef[p]=0;
    for(int e=0;e<m_global;e++){
        if(ew[e]==0){st->ze[e]=0;continue;}
        unsigned em=(1u<<eu[e])|(1u<<ev[e]); u64 s=0; unsigned other=full^em;
        for(unsigned x=other;;x=(x-1)&other){ unsigned T=em|x; s+=(u64)te_[e][T]*forest_[full^T]; if(x==0)break; }
        st->ze[e]=s;
    }
    for(int e=0;e<m_global;e++) for(int f=e+1;f<m_global;f++){
        int pi=pair_index[e][f];
        if(ew[e]==0 || ew[f]==0){st->zef[pi]=0;continue;}
        unsigned em=(1u<<eu[e])|(1u<<ev[e]), fm=(1u<<eu[f])|(1u<<ev[f]); unsigned um=em|fm;
        u64 zef=0; unsigned o=full^um;
        for(unsigned x=o;;x=(x-1)&o){ unsigned T=um|x; zef+=(u64)tp_[pi][T]*forest_[full^T]; if(x==0)break; }
        if((em&fm)==0){
            for(unsigned x=o;;x=(x-1)&o){
                unsigned A=em|x, left=o^x;
                for(unsigned y=left;;y=(y-1)&left){ unsigned B=fm|y, rem=left^y; zef+=(u64)te_[e][A]*te_[f][B]*forest_[rem]; if(y==0)break; }
                if(x==0)break;
            }
        }
        st->zef[pi]=zef;
    }
}

static i128 delta_pair(const Stats *st,int e,int f){ int pi=pair_index[e][f]; return (i128)st->ze[e]*st->ze[f]-(i128)st->Z*st->zef[pi]; }
static void print_i128(i128 x){ if(x<0){putchar('-');x=-x;} char s[80];int n=0;do{s[n++]='0'+x%10;x/=10;}while(x);while(n--)putchar(s[n]); }
static void sprint_i128(char *buf,size_t cap,i128 x){ char tmp[80];int n=0,neg=0;if(x<0){neg=1;x=-x;}do{tmp[n++]='0'+x%10;x/=10;}while(x);size_t k=0;if(neg&&k+1<cap)buf[k++]='-';while(n&&k+1<cap)buf[k++]=tmp[--n];buf[k]='\0'; }

int main(int argc,char**argv){
    if(argc<2){fprintf(stderr,"usage: %s graph8.g6 [start_index_1based] [count]\n",argv[0]);return 2;}
    long start=1, want=LONG_MAX; if(argc>=3)start=atol(argv[2]); if(argc>=4)want=atol(argv[3]);
    FILE*fp=fopen(argv[1],"r"); if(!fp){perror("fopen");return 2;}
    char line[256]; long idxg=0, processed=0; unsigned long long triples=0, q1neg=0, critical=0, zero_slack=0;
    i128 min_slack=-1; char minline[32]=""; int ming=-1,mine=-1,minf=-1; i128 minq0=0,minq1=0,minq2=0;
    i128 most_neg_q1=0; char negline[32]=""; int negg=-1,nege=-1,negf=-1; i128 negq0=0,negq2=0;
    clock_t t0=clock();
    while(fgets(line,sizeof(line),fp)){
        size_t len=strcspn(line,"\r\n"); line[len]='\0'; if(!len)continue; idxg++; if(idxg<start)continue; if(processed>=want)break; processed++;
        if((unsigned char)line[0] != 63+N){fprintf(stderr,"bad graph6 n at %ld\n",idxg);return 6;}
        int bits[30],nb=0,bitpos=0; for(size_t ci=1;ci<len;ci++){int x=(unsigned char)line[ci]-63;for(int b=5;b>=0;b--)bits[nb++]=(x>>b)&1;}
        int m=0; for(int j=1;j<N;j++)for(int i=0;i<j;i++){if(bits[bitpos]){eu[m]=i;ev[m]=j;m++;}bitpos++;}
        m_global=m; int pc=0; for(int e=0;e<m;e++)for(int f=e+1;f<m;f++){pair_index[e][f]=pair_index[f][e]=pc;pu[pc]=e;pv[pc]=f;pc++;}
        Stats base,s0,s2; compute_stats(-1,1,&base);
        for(int g=0;g<m;g++){
            compute_stats(g,0,&s0); compute_stats(g,2,&s2);
            for(int e=0;e<m;e++) if(e!=g) for(int f=e+1;f<m;f++) if(f!=g){
                triples++;
                i128 y0=delta_pair(&s0,e,f), y1=delta_pair(&base,e,f), y2=delta_pair(&s2,e,f);
                i128 n2=y2-2*y1+y0, n1=-3*y0+4*y1-y2;
                if((n2&1)!=0 || (n1&1)!=0){fprintf(stderr,"parity fail graph=%ld\n",idxg);return 7;}
                i128 q0=y0,q1=n1/2,q2=n2/2;
                if(q1<0){q1neg++; if(q1<most_neg_q1){most_neg_q1=q1;strcpy(negline,line);negg=g;nege=e;negf=f;negq0=q0;negq2=q2;}}
                int fail=0;
                if(q2<0) fail=1;
                else if(q2==0){ if(q0<0 || q1<0) fail=1; }
                else if(q1>=0){ if(q0<0) fail=1; }
                else {
                    critical++;
                    i128 slack=4*q0*q2-q1*q1;
                    if(slack<0) fail=1;
                    else { if(slack==0)zero_slack++; if(min_slack<0||slack<min_slack){min_slack=slack;strcpy(minline,line);ming=g;mine=e;minf=f;minq0=q0;minq1=q1;minq2=q2;} }
                }
                if(fail){
                    printf("OEFR_COUNTEREXAMPLE graph_index=%ld g6=%s g=(%d,%d) e=(%d,%d) f=(%d,%d) q0=",idxg,line,eu[g],ev[g],eu[e],ev[e],eu[f],ev[f]);print_i128(q0);printf(" q1=");print_i128(q1);printf(" q2=");print_i128(q2);printf(" discr_defect=q1^2-4q0q2=");print_i128(q1*q1-4*q0*q2);putchar('\n');
                    return 1;
                }
            }
        }
        if(processed%500==0) fprintf(stderr,"progress global_index=%ld processed=%ld triples=%llu sec=%.2f\n",idxg,processed,triples,(double)(clock()-t0)/CLOCKS_PER_SEC);
    }
    fclose(fp);
    printf("STATUS PASS\nstart_index=%ld\nprocessed_graphs=%ld\ncovered_end_index=%ld\noefr_triples_tested=%llu\nq1_negative=%llu\ncritical_q2pos_q1neg=%llu\nzero_discriminant_slack=%llu\n",start,processed,(processed?start+processed-1:start-1),triples,q1neg,critical,zero_slack);
    if(min_slack>=0){printf("min_nonnegative_discriminant_slack=");print_i128(min_slack);printf(" g6=%s g=%d e=%d f=%d q0=",minline,ming,mine,minf);print_i128(minq0);printf(" q1=");print_i128(minq1);printf(" q2=");print_i128(minq2);putchar('\n');}
    if(most_neg_q1<0){printf("most_negative_q1=");print_i128(most_neg_q1);printf(" g6=%s g=%d e=%d f=%d q0=",negline,negg,nege,negf);print_i128(negq0);printf(" q2=");print_i128(negq2);putchar('\n');}
    printf("elapsed_cpu_seconds=%.6f\n",(double)(clock()-t0)/CLOCKS_PER_SEC);
    return 0;
}
