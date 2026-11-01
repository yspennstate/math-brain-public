#include <bits/stdc++.h>
#include <boost/multiprecision/cpp_int.hpp>
#include <omp.h>
using namespace std;
using u64 = uint64_t;
using i64 = long long;
using i128 = __int128_t;

static constexpr int N=9, MAXE=36, MAXP=630;
static constexpr i64 MOD=1000000007LL;
static constexpr uint32_t TAU_MAX=4782969u; // tau(K9)=9^7

static vector<pair<int,int>> pairs_n(int n){ vector<pair<int,int>> p; for(int j=1;j<n;j++)for(int i=0;i<j;i++)p.push_back({i,j}); return p; }

struct Canon {
    int n=0; uint16_t nb[10]{}; int colors[10]{}; vector<vector<int>> classes; u64 best=0;
    void build(u64 code){ fill(begin(nb),end(nb),0); int bit=0; for(int j=1;j<n;j++)for(int i=0;i<j;i++,bit++) if((code>>bit)&1ULL){nb[i]|=uint16_t(1u<<j);nb[j]|=uint16_t(1u<<i);} }
    void refine(){
        for(int i=0;i<n;i++)colors[i]=__builtin_popcount((unsigned)nb[i]);
        while(true){
            int maxc=*max_element(colors,colors+n); array<array<unsigned char,11>,10> sig{};
            for(int i=0;i<n;i++){ sig[i][0]=(unsigned char)colors[i]; for(int j=0;j<n;j++) if((nb[i]>>j)&1u) sig[i][1+colors[j]]++; }
            vector<int> idx(n); iota(idx.begin(),idx.end(),0);
            sort(idx.begin(),idx.end(),[&](int a,int b){ for(int k=0;k<2+maxc;k++) if(sig[a][k]!=sig[b][k]) return sig[a][k]<sig[b][k]; return false; });
            int nc[10]; int cid=-1;
            for(int pos=0;pos<n;pos++){ int v=idx[pos]; bool diff=(pos==0); if(pos){int u=idx[pos-1]; for(int k=0;k<2+maxc;k++) if(sig[v][k]!=sig[u][k]){diff=true;break;}} if(diff)cid++; nc[v]=cid; }
            bool same=true; for(int i=0;i<n;i++)if(nc[i]!=colors[i]){same=false;break;} for(int i=0;i<n;i++)colors[i]=nc[i]; if(same)break;
        }
        int maxc=*max_element(colors,colors+n); classes.assign(maxc+1,{}); for(int i=0;i<n;i++)classes[colors[i]].push_back(i);
    }
    inline u64 ordered_code(const int* order) const { u64 out=0; int bit=0; for(int b=1;b<n;b++)for(int a=0;a<b;a++,bit++) if((nb[order[b]]>>order[a])&1u) out|=1ULL<<bit; return out; }
    void rec(int ci,int* order,int pos){ if(ci==(int)classes.size()){best=min(best,ordered_code(order));return;} auto v=classes[ci]; sort(v.begin(),v.end()); do{for(int x:v)order[pos++]=x;rec(ci+1,order,pos);pos-=(int)v.size();}while(next_permutation(v.begin(),v.end())); }
    u64 operator()(u64 code,int nn){n=nn;build(code);refine();best=ULLONG_MAX;int order[10];rec(0,order,0);return best;}
};

static uint64_t burnside_unlabeled_count(int n){
    auto pairs=pairs_n(n); int M=pairs.size(); int edge_idx[10][10]; memset(edge_idx,-1,sizeof(edge_idx));
    for(int k=0;k<M;k++){auto[a,b]=pairs[k];edge_idx[a][b]=edge_idx[b][a]=k;}
    vector<int> perm(n); iota(perm.begin(),perm.end(),0); unsigned long long total=0,fact=1; for(int i=2;i<=n;i++)fact*=i;
    do{ bool seen[45]{}; int orbits=0; for(int k=0;k<M;k++)if(!seen[k]){orbits++;int cur=k;while(!seen[cur]){seen[cur]=true;auto[a,b]=pairs[cur];cur=edge_idx[perm[a]][perm[b]];}} total += 1ULL<<orbits; }while(next_permutation(perm.begin(),perm.end()));
    if(total%fact) throw runtime_error("Burnside divisibility failed"); return total/fact;
}

static string graph6_of_code(u64 code,int n){
    string s; s.push_back(char(63+n)); int M=n*(n-1)/2; for(int k=0;k<M;k+=6){int x=0;for(int b=0;b<6;b++){x<<=1;int pos=k+b;if(pos<M && ((code>>pos)&1ULL))x|=1;}s.push_back(char(63+x));}return s;
}
static string i128str(i128 x){ if(x==0)return"0";bool neg=x<0;if(neg)x=-x;string s;while(x){s.push_back(char('0'+x%10));x/=10;}if(neg)s.push_back('-');reverse(s.begin(),s.end());return s; }

static thread_local uint32_t tau_[1<<N];
static thread_local uint32_t te_[MAXE][1<<N];
static thread_local uint32_t tp_[MAXP][1<<N];
static thread_local u64 forest_[1<<N];
static thread_local int eu[MAXE],ev[MAXE],pair_index[MAXE][MAXE];
static thread_local i64 invmat[8][8];
static i64 modnorm(i64 x){x%=MOD;if(x<0)x+=MOD;return x;}
static i64 invmod(i64 a){i64 b=MOD,u=1,v=0;while(b){i64 t=a/b,na=a-t*b;a=b;b=na;i64 nu=u-t*v;u=v;v=nu;}return modnorm(u);}

static uint32_t tree_data(unsigned mask,uint16_t adj[N],int m){
    int verts[N],idx[N],k=0; for(int i=0;i<N;i++)idx[i]=-1; for(int i=0;i<N;i++)if(mask>>i&1u)verts[k++]=i;
    if(k==0)return 0; if(k==1)return 1; int root=verts[k-1],d=k-1; i64 a[8][8]{},b[8][8]{}; for(int i=0;i<d;i++)idx[verts[i]]=i;
    for(int ii=0;ii<d;ii++){int u=verts[ii],deg=0;for(int jj=0;jj<k;jj++)if(jj!=ii){int v=verts[jj];if(adj[u]>>v&1u)deg++;}a[ii][ii]=deg;for(int jj=0;jj<d;jj++)if(ii!=jj){int v=verts[jj];if(adj[u]>>v&1u)a[ii][jj]=MOD-1;}b[ii][ii]=1;}
    i64 det=1;int sign=1;
    for(int col=0;col<d;col++){int pr=col;while(pr<d&&a[pr][col]==0)pr++;if(pr==d)return 0;if(pr!=col){for(int j=0;j<d;j++){swap(a[pr][j],a[col][j]);swap(b[pr][j],b[col][j]);}sign=-sign;}i64 piv=a[col][col];det=det*piv%MOD;i64 ip=invmod(piv);for(int j=0;j<d;j++){a[col][j]=a[col][j]*ip%MOD;b[col][j]=b[col][j]*ip%MOD;}for(int r=0;r<d;r++)if(r!=col){i64 f=a[r][col];if(!f)continue;for(int j=0;j<d;j++){a[r][j]=modnorm(a[r][j]-f*a[col][j]);b[r][j]=modnorm(b[r][j]-f*b[col][j]);}}}
    if(sign<0)det=modnorm(-det); if(det<=0||det>TAU_MAX)throw runtime_error("tau bound failure"); uint32_t tau=(uint32_t)det; for(int i=0;i<d;i++)for(int j=0;j<d;j++)invmat[i][j]=b[i][j];
    i64 raw[MAXE]{}; int inside[MAXE],ni=0;
    for(int e=0;e<m;e++)if((mask>>eu[e]&1u)&&(mask>>ev[e]&1u)){inside[ni++]=e;int u=eu[e],v=ev[e];i64 val=0;if(u!=root)val+=invmat[idx[u]][idx[u]];if(v!=root)val+=invmat[idx[v]][idx[v]];if(u!=root&&v!=root){val-=invmat[idx[u]][idx[v]];val-=invmat[idx[v]][idx[u]];}raw[e]=modnorm(val);i64 q=det*raw[e]%MOD;if(q<0||q>(i64)tau)throw runtime_error("te bound failure");te_[e][mask]=(uint32_t)q;}
    for(int aa=0;aa<ni;aa++)for(int bb=aa+1;bb<ni;bb++){int e=inside[aa],f=inside[bb],pi=pair_index[e][f];int us[2]={eu[e],ev[e]},vs[2]={eu[f],ev[f]};int cs[2]={1,-1},ds[2]={1,-1};i64 cross=0;for(int x=0;x<2;x++)if(us[x]!=root)for(int y=0;y<2;y++)if(vs[y]!=root)cross+=(i64)cs[x]*ds[y]*invmat[idx[us[x]]][idx[vs[y]]];cross=modnorm(cross);i64 val=modnorm(raw[e]*raw[f]%MOD-cross*cross%MOD);i64 q2=det*val%MOD;if(q2<0||q2>(i64)tau)throw runtime_error("tp bound failure");tp_[pi][mask]=(uint32_t)q2;}
    return tau;
}

struct CheckStats{u64 graphs=0,pairs=0,zero=0,maxF=0; i128 minpos=-1,maxgap=0; u64 mincode=0,maxcode=0,maxFcode=0;int mine=-1,minf=-1,maxe=-1,maxf=-1;};

static bool check_graph(u64 code,CheckStats &st){
    uint16_t adj[N]{}; int m=0,bit=0; for(int j=1;j<N;j++)for(int i=0;i<j;i++,bit++)if((code>>bit)&1ULL){adj[i]|=uint16_t(1u<<j);adj[j]|=uint16_t(1u<<i);eu[m]=i;ev[m]=j;m++;}
    int pc=0;for(int e=0;e<m;e++)for(int f=e+1;f<m;f++){pair_index[e][f]=pair_index[f][e]=pc++;}
    memset(tau_,0,sizeof(tau_)); memset(te_,0,(size_t)m*(1u<<N)*sizeof(uint32_t)); memset(tp_,0,(size_t)pc*(1u<<N)*sizeof(uint32_t));
    for(unsigned mask=1;mask<(1u<<N);mask++)tau_[mask]=tree_data(mask,adj,m);
    forest_[0]=1;for(unsigned mask=1;mask<(1u<<N);mask++){unsigned lb=mask&-mask,rest=mask^lb;u64 sum=0;for(unsigned x=rest;;x=(x-1)&rest){unsigned T=x|lb;sum+=(u64)tau_[T]*forest_[mask^T];if(x==0)break;}forest_[mask]=sum;}
    unsigned full=(1u<<N)-1;u64 Z=forest_[full]; if(Z>st.maxF){st.maxF=Z;st.maxFcode=code;}
    u64 ze[MAXE]{};for(int e=0;e<m;e++){unsigned em=(1u<<eu[e])|(1u<<ev[e]),other=full^em;u64 s=0;for(unsigned x=other;;x=(x-1)&other){unsigned T=em|x;s+=(u64)te_[e][T]*forest_[full^T];if(x==0)break;}ze[e]=s;}
    for(int e=0;e<m;e++)for(int f=e+1;f<m;f++){
        st.pairs++;int pi=pair_index[e][f];unsigned em=(1u<<eu[e])|(1u<<ev[e]),fm=(1u<<eu[f])|(1u<<ev[f]),um=em|fm;u64 zef=0;unsigned o=full^um;
        for(unsigned x=o;;x=(x-1)&o){unsigned T=um|x;zef+=(u64)tp_[pi][T]*forest_[full^T];if(x==0)break;}
        if((em&fm)==0){for(unsigned x=o;;x=(x-1)&o){unsigned A=em|x,left=o^x;for(unsigned y=left;;y=(y-1)&left){unsigned B=fm|y,rem=left^y;zef+=(u64)te_[e][A]*te_[f][B]*forest_[rem];if(y==0)break;}if(x==0)break;}}
        i128 delta=(i128)ze[e]*ze[f]-(i128)Z*zef;
        if(delta<0){cout<<"COUNTEREXAMPLE code="<<code<<" g6="<<graph6_of_code(code,N)<<" m="<<m<<" e="<<eu[e]<<","<<ev[e]<<" f="<<eu[f]<<","<<ev[f]<<" Z="<<Z<<" Ze="<<ze[e]<<" Zf="<<ze[f]<<" Zef="<<zef<<" delta="<<i128str(delta)<<"\n";return false;}
        if(delta==0)st.zero++;else{if(st.minpos<0||delta<st.minpos){st.minpos=delta;st.mincode=code;st.mine=e;st.minf=f;}if(delta>st.maxgap){st.maxgap=delta;st.maxcode=code;st.maxe=e;st.maxf=f;}}
    }
    st.graphs++;return true;
}

int main(int argc,char**argv){
    if(argc!=2){cerr<<"usage: checker atlas7_codes.txt\n";return 2;}auto t0=chrono::steady_clock::now();
    cout<<"HARD10-01 exact n=9 dense-sector uniform-forest certificate\n";
    cout<<"scope=all unlabeled simple 9-vertex graphs with 19..36 edges; unit weights; all distinct present edge pairs\n";
    cout<<"arithmetic=exact integer counts; modular Laplacian algebra only where true tree counts are < MOD\n";
    vector<u64> c7raw;{ifstream f(argv[1]);if(!f)throw runtime_error("cannot open atlas7 input");u64 x;while(f>>x)c7raw.push_back(x);}if(c7raw.size()!=1044)throw runtime_error("atlas7 rows !=1044");
    auto U7=burnside_unlabeled_count(7),U8=burnside_unlabeled_count(8),U9=burnside_unlabeled_count(9);if(U7!=1044||U8!=12346||U9!=274668)throw runtime_error("Burnside mismatch");cout<<"burnside U7="<<U7<<" U8="<<U8<<" U9="<<U9<<" PASS\n";
    Canon C;unordered_set<u64>s7;s7.reserve(1500);for(u64 x:c7raw)s7.insert(C(x,7));if(s7.size()!=U7)throw runtime_error("atlas7 canonical mismatch");vector<u64>c7(s7.begin(),s7.end());sort(c7.begin(),c7.end());
    unordered_set<u64>s8;s8.reserve(20000);u64 ext8=0;for(u64 base:c7)for(unsigned mask=0;mask<(1u<<7);mask++){ext8++;s8.insert(C(base|(u64(mask)<<21),8));}if(ext8!=1044ULL*128||s8.size()!=U8)throw runtime_error("n8 augmentation incomplete");vector<u64>c8(s8.begin(),s8.end());sort(c8.begin(),c8.end());cout<<"n8 raw_extensions="<<ext8<<" canonical="<<c8.size()<<" COMPLETE=PASS\n";
    unordered_set<u64>s9;s9.reserve(350000);u64 ext9=0;for(u64 base:c8)for(unsigned mask=0;mask<(1u<<8);mask++){ext9++;s9.insert(C(base|(u64(mask)<<28),9));}if(ext9!=12346ULL*256||s9.size()!=U9)throw runtime_error("n9 augmentation incomplete");vector<u64>c9(s9.begin(),s9.end());sort(c9.begin(),c9.end());cout<<"n9 raw_extensions="<<ext9<<" canonical="<<c9.size()<<" COMPLETE=PASS\n";
    array<u64,37> hist{};for(u64 x:c9)hist[__builtin_popcountll(x)]++;u64 hsum=0;for(int m=0;m<=36;m++){hsum+=hist[m];cout<<"edge_hist["<<m<<"]="<<hist[m]<<"\n";if(hist[m]!=hist[36-m])throw runtime_error("complement histogram symmetry failed");}if(hsum!=U9)throw runtime_error("hist sum mismatch");cout<<"edge_hist_complement_symmetry=PASS\n";
    u64 dense_expected=0;for(int m=19;m<=36;m++)dense_expected+=hist[m];cout<<"dense_expected_classes_19_36="<<dense_expected<<"\n";
    int nth=max(1, min(5, omp_get_max_threads())); omp_set_num_threads(nth);
    vector<CheckStats> sts(nth); atomic<bool> bad(false); atomic<u64> done_dense(0);
    #pragma omp parallel for schedule(dynamic,128)
    for(long long ii=0; ii<(long long)c9.size(); ii++){
        if(bad.load(memory_order_relaxed)) continue;
        u64 code=c9[ii]; int m=__builtin_popcountll(code); if(m<19) continue;
        int tid=omp_get_thread_num();
        if(!check_graph(code,sts[tid])){bad.store(true);continue;}
        u64 d=done_dense.fetch_add(1)+1; if(d%10000==0) cerr<<"progress dense="<<d<<"/"<<dense_expected<<"\n";
    }
    if(bad.load()) return 1;
    CheckStats st; for(auto &q:sts){st.graphs+=q.graphs;st.pairs+=q.pairs;st.zero+=q.zero;if(q.maxF>st.maxF){st.maxF=q.maxF;st.maxFcode=q.maxFcode;}if(q.minpos>=0&&(st.minpos<0||q.minpos<st.minpos)){st.minpos=q.minpos;st.mincode=q.mincode;st.mine=q.mine;st.minf=q.minf;}if(q.maxgap>st.maxgap){st.maxgap=q.maxgap;st.maxcode=q.maxcode;st.maxe=q.maxe;st.maxf=q.maxf;}}
    if(st.graphs!=dense_expected)throw runtime_error("dense checked count mismatch");
    cout<<"omp_threads="<<nth<<"\n";
    cout<<"STATUS PASS\n";cout<<"dense_graphs_checked="<<st.graphs<<"\n";cout<<"edge_pairs_tested="<<st.pairs<<"\n";cout<<"zero_gaps="<<st.zero<<"\n";cout<<"max_forest_count="<<st.maxF<<" g6="<<graph6_of_code(st.maxFcode,N)<<"\n";if(st.minpos>=0)cout<<"min_positive_gap="<<i128str(st.minpos)<<" g6="<<graph6_of_code(st.mincode,N)<<" edge_indices="<<st.mine<<","<<st.minf<<"\n";cout<<"max_gap="<<i128str(st.maxgap)<<" g6="<<graph6_of_code(st.maxcode,N)<<" edge_indices="<<st.maxe<<","<<st.maxf<<"\n";
    cout<<"elapsed_seconds="<<fixed<<setprecision(3)<<chrono::duration<double>(chrono::steady_clock::now()-t0).count()<<"\n";cout<<"ALL_EXACT_CHECKS_PASS\n";return 0;
}
