#include <bits/stdc++.h>
#include <boost/multiprecision/cpp_int.hpp>
#include <omp.h>
using namespace std;
using u64 = uint64_t;
using u128 = __uint128_t;
using i128 = __int128_t;
using boost::multiprecision::cpp_int;

static string u128str(u128 x){ if(x==0) return "0"; string s; while(x){ s.push_back(char('0'+x%10)); x/=10; } reverse(s.begin(),s.end()); return s; }
static string i128str(i128 x){ if(x<0) return string("-")+u128str(u128(-x)); return u128str(u128(x)); }
static u128 pow128(u128 a,int e){ u128 r=1; while(e--) r*=a; return r; }
static inline int edge_count(u64 code){ return __builtin_popcountll(code); }
static vector<pair<int,int>> pairs_n(int n){ vector<pair<int,int>> p; for(int j=1;j<n;j++) for(int i=0;i<j;i++) p.push_back({i,j}); return p; }

struct Canon {
    int n=0;
    uint16_t nb[10]{};
    int colors[10]{};
    vector<vector<int>> classes;
    u64 best=0;

    void build(u64 code){
        fill(begin(nb),end(nb),0); int bit=0;
        for(int j=1;j<n;j++) for(int i=0;i<j;i++,bit++) if((code>>bit)&1ULL){ nb[i]|=uint16_t(1u<<j); nb[j]|=uint16_t(1u<<i); }
    }
    void refine(){
        for(int i=0;i<n;i++) colors[i]=__builtin_popcount((unsigned)nb[i]);
        while(true){
            int maxc=*max_element(colors,colors+n);
            array<array<unsigned char,11>,10> sig{};
            for(int i=0;i<n;i++){
                sig[i][0]=(unsigned char)colors[i];
                for(int j=0;j<n;j++) if((nb[i]>>j)&1u) sig[i][1+colors[j]]++;
            }
            vector<int> idx(n); iota(idx.begin(),idx.end(),0);
            sort(idx.begin(),idx.end(),[&](int a,int b){
                for(int k=0;k<2+maxc;k++) if(sig[a][k]!=sig[b][k]) return sig[a][k]<sig[b][k];
                return false;
            });
            int nc[10]; int cid=-1;
            for(int pos=0;pos<n;pos++){
                int v=idx[pos]; bool diff=(pos==0);
                if(pos){ int u=idx[pos-1]; for(int k=0;k<2+maxc;k++) if(sig[v][k]!=sig[u][k]){diff=true;break;} }
                if(diff) cid++; nc[v]=cid;
            }
            bool same=true; for(int i=0;i<n;i++) if(nc[i]!=colors[i]){same=false;break;}
            for(int i=0;i<n;i++) colors[i]=nc[i];
            if(same) break;
        }
        int maxc=*max_element(colors,colors+n);
        classes.assign(maxc+1,{});
        for(int i=0;i<n;i++) classes[colors[i]].push_back(i);
    }
    inline u64 ordered_code(const int* order) const {
        u64 out=0; int bit=0;
        for(int b=1;b<n;b++) for(int a=0;a<b;a++,bit++) if((nb[order[b]]>>order[a])&1u) out|=1ULL<<bit;
        return out;
    }
    void rec(int ci,int* order,int pos){
        if(ci==(int)classes.size()){ best=min(best,ordered_code(order)); return; }
        auto v=classes[ci]; sort(v.begin(),v.end());
        do { for(int x:v) order[pos++]=x; rec(ci+1,order,pos); pos-=(int)v.size(); } while(next_permutation(v.begin(),v.end()));
    }
    u64 operator()(u64 code,int nn){ n=nn; build(code); refine(); best=ULLONG_MAX; int order[10]; rec(0,order,0); return best; }
};

static uint64_t burnside_unlabeled_count(int n){
    auto pairs=pairs_n(n); const int M=pairs.size();
    int edge_idx[10][10]; memset(edge_idx,-1,sizeof(edge_idx));
    for(int k=0;k<M;k++){auto [a,b]=pairs[k]; edge_idx[a][b]=edge_idx[b][a]=k;}
    vector<int> perm(n); iota(perm.begin(),perm.end(),0);
    unsigned long long total=0, fact=1; for(int i=2;i<=n;i++) fact*=i;
    do {
        bool seen[45]{}; int orbits=0;
        for(int k=0;k<M;k++) if(!seen[k]){
            orbits++; int cur=k;
            while(!seen[cur]){ seen[cur]=true; auto [a,b]=pairs[cur]; cur=edge_idx[perm[a]][perm[b]]; }
        }
        total += 1ULL<<orbits;
    } while(next_permutation(perm.begin(),perm.end()));
    if(total%fact) throw runtime_error("Burnside divisibility failed");
    return total/fact;
}

static inline uint64_t hom_H_n10(u64 code){
    uint16_t nb[10]{}; int bit=0;
    for(int j=1;j<10;j++) for(int i=0;i<j;i++,bit++) if((code>>bit)&1ULL){ nb[i]|=uint16_t(1u<<j); nb[j]|=uint16_t(1u<<i); }
    uint8_t C[10][10][10];
    for(int a=0;a<10;a++) for(int b=0;b<10;b++){
        uint16_t ab=nb[a]&nb[b];
        for(int c=0;c<10;c++) C[a][b][c]=(uint8_t)__builtin_popcount((unsigned)(ab&nb[c]));
    }
    uint64_t h=0;
    for(int a=0;a<10;a++) for(int b=0;b<10;b++) for(int d=0;d<10;d++) for(int e=0;e<10;e++){
        unsigned r=0;
        for(int c=0;c<10;c++) r += unsigned(C[a][b][c])*unsigned(C[b][c][d])*unsigned(C[c][d][e]);
        h += uint64_t(r)*uint64_t(C[d][e][a])*uint64_t(C[e][a][b]);
    }
    if(h>10000000000ULL) throw runtime_error("hom upper bound failed");
    return h;
}

static uint64_t hom_contraction_slow(u64 code,int n){
    uint16_t nb[10]{}; int bit=0;
    for(int j=1;j<n;j++) for(int i=0;i<j;i++,bit++) if((code>>bit)&1ULL){nb[i]|=uint16_t(1u<<j);nb[j]|=uint16_t(1u<<i);}
    uint8_t C[10][10][10]{};
    for(int a=0;a<n;a++)for(int b=0;b<n;b++){uint16_t ab=nb[a]&nb[b];for(int c=0;c<n;c++)C[a][b][c]=(uint8_t)__builtin_popcount((unsigned)(ab&nb[c]));}
    uint64_t h=0;
    for(int a=0;a<n;a++)for(int b=0;b<n;b++)for(int c=0;c<n;c++)for(int d=0;d<n;d++)for(int e=0;e<n;e++)
        h += uint64_t(C[c][d][e])*C[d][e][a]*C[e][a][b]*C[a][b][c]*C[b][c][d];
    return h;
}

static inline u64 mix64(u64 x){
    x += 0x9e3779b97f4a7c15ULL;
    x = (x ^ (x >> 30)) * 0xbf58476d1ce4e5b9ULL;
    x = (x ^ (x >> 27)) * 0x94d049bb133111ebULL;
    return x ^ (x >> 31);
}

struct AtomicSet {
    static constexpr u64 EMPTY = UINT64_MAX;
    size_t cap, mask;
    unique_ptr<atomic<u64>[]> tab;
    atomic<uint64_t> inserted{0};
    AtomicSet(size_t c):cap(c),mask(c-1),tab(new atomic<u64>[c]){
        if((c&(c-1))!=0) throw runtime_error("hash capacity must be power of two");
        #pragma omp parallel for schedule(static)
        for(long long i=0;i<(long long)cap;i++) tab[i].store(EMPTY,memory_order_relaxed);
    }
    bool insert(u64 x){
        size_t p=(size_t)mix64(x)&mask;
        for(size_t probes=0; probes<cap; probes++){
            u64 cur=tab[p].load(memory_order_relaxed);
            if(cur==x) return false;
            if(cur==EMPTY){
                if(tab[p].compare_exchange_weak(cur,x,memory_order_relaxed,memory_order_relaxed)){
                    inserted.fetch_add(1,memory_order_relaxed); return true;
                }
                if(cur==x) return false;
            }
            p=(p+1)&mask;
        }
        throw runtime_error("hash table full");
    }
};

int main(){
    auto t0=chrono::steady_clock::now();
    cout<<"C30 Sidorenko exact n=10 certificate\n";
    cout<<"H=K_{5,5}\\C_10; v(H)=10; e(H)=15\n";
    cout<<"arithmetic=integer_exact; floating_point_decisions=NONE\n" << flush;

    auto U7=burnside_unlabeled_count(7);
    auto U8=burnside_unlabeled_count(8);
    auto U9=burnside_unlabeled_count(9);
    auto U10=burnside_unlabeled_count(10);
    if(U7!=1044 || U8!=12346 || U9!=274668 || U10!=12005168ULL) throw runtime_error("Burnside count mismatch");
    cout<<"burnside_counts: U7="<<U7<<" U8="<<U8<<" U9="<<U9<<" U10="<<U10<<" PASS\n" << flush;

    // Self-contained exhaustive labeled generation at n=7.
    unordered_set<u64> s7; s7.reserve(1500); Canon C7;
    const u64 labeled7 = 1ULL<<21;
    for(u64 code=0; code<labeled7; code++) s7.insert(C7(code,7));
    if(s7.size()!=U7) throw runtime_error("complete labeled n7 canonicalization failed");
    vector<u64> c7(s7.begin(),s7.end()); sort(c7.begin(),c7.end());
    cout<<"n7_generation: labeled_graphs="<<labeled7<<" canonical_classes="<<c7.size()<<" burnside="<<U7<<" COMPLETE=PASS\n" << flush;

    unordered_set<u64> s8; s8.reserve(20000); uint64_t ext8=0; Canon C8;
    for(u64 base:c7) for(unsigned mask=0;mask<(1u<<7);mask++){ ext8++; s8.insert(C8(base|(u64(mask)<<21),8)); }
    if(ext8!=1044ULL*128 || s8.size()!=U8) throw runtime_error("complete n8 augmentation failed");
    vector<u64> c8(s8.begin(),s8.end()); sort(c8.begin(),c8.end());
    cout<<"n8_generation: raw_extensions="<<ext8<<" canonical_classes="<<c8.size()<<" burnside="<<U8<<" COMPLETE=PASS\n" << flush;

    unordered_set<u64> s9; s9.reserve(350000); uint64_t ext9=0; Canon C9;
    for(u64 base:c8) for(unsigned mask=0;mask<(1u<<8);mask++){ ext9++; s9.insert(C9(base|(u64(mask)<<28),9)); }
    if(ext9!=12346ULL*256 || s9.size()!=U9) throw runtime_error("complete n9 augmentation failed");
    vector<u64> c9(s9.begin(),s9.end()); sort(c9.begin(),c9.end());
    cout<<"n9_generation: raw_extensions="<<ext9<<" canonical_classes="<<c9.size()<<" burnside="<<U9<<" COMPLETE=PASS\n" << flush;

    const size_t HCAP=1ULL<<25; // load factor < 0.36 at U10.
    AtomicSet s10(HCAP);
    atomic<uint64_t> ext10{0};
    #pragma omp parallel
    {
        Canon C10;
        #pragma omp for schedule(dynamic,16)
        for(long long bi=0; bi<(long long)c9.size(); bi++){
            u64 base=c9[(size_t)bi];
            for(unsigned mask=0; mask<(1u<<9); mask++){
                ext10.fetch_add(1,memory_order_relaxed);
                u64 raw=base|(u64(mask)<<36);
                s10.insert(C10(raw,10));
            }
        }
    }
    const uint64_t expected_ext10=U9*512ULL;
    if(ext10.load()!=expected_ext10) throw runtime_error("n10 extension count mismatch");
    uint64_t scan_count=0;
    for(size_t i=0;i<HCAP;i++) if(s10.tab[i].load(memory_order_relaxed)!=AtomicSet::EMPTY) scan_count++;
    if(scan_count!=s10.inserted.load() || scan_count!=U10) throw runtime_error("complete n10 augmentation/canonical count failed");
    cout<<"n10_generation: raw_extensions="<<ext10.load()<<" canonical_classes="<<scan_count<<" burnside="<<U10<<" COMPLETE=PASS\n" << flush;

    // Deterministic implementation cross-check on first 256 occupied hash slots.
    int checked=0;
    for(size_t i=0;i<HCAP && checked<256;i++){
        u64 code=s10.tab[i].load(memory_order_relaxed);
        if(code==AtomicSet::EMPTY) continue;
        if(hom_H_n10(code)!=hom_contraction_slow(code,10)) throw runtime_error("hom implementation cross-check failed");
        checked++;
    }
    if(checked!=256) throw runtime_error("not enough n10 classes for cross-check");
    cout<<"hom_fast_vs_direct_contraction_256_classes=PASS\n" << flush;

    const u128 n20=pow128(10,20);
    const u64 K10=(1ULL<<45)-1;
    const u64 hK10=hom_H_n10(K10);
    const u128 numK=u128(hK10)*n20;
    const u128 denK=pow128(90,15);
    uint64_t hthreshold[46]{};
    for(int m=1;m<=45;m++){
        cpp_int A=cpp_int(numK)*cpp_int(pow128(2*m,15));
        cpp_int B=cpp_int(denK)*cpp_int(n20);
        cpp_int q=(A+B-1)/B;
        hthreshold[m]=q.convert_to<uint64_t>();
    }

    atomic<long long> violations{0}, ratio_below_K10{0};
    atomic<u64> first_bad_code{0}; atomic<int> first_bad_m{0}; atomic<uint64_t> first_bad_h{0};
    #pragma omp parallel for schedule(dynamic,1024)
    for(long long ii=0; ii<(long long)HCAP; ii++){
        u64 code=s10.tab[(size_t)ii].load(memory_order_relaxed);
        if(code==AtomicSet::EMPTY) continue;
        int m=edge_count(code); uint64_t h=hom_H_n10(code);
        i128 D=i128(u128(h)*n20)-i128(pow128(2*m,15));
        if(D<0){
            long long old=violations.fetch_add(1,memory_order_relaxed);
            if(old==0){ first_bad_code.store(code); first_bad_m.store(m); first_bad_h.store(h); }
        }
        if(m>0 && h<hthreshold[m]) ratio_below_K10.fetch_add(1,memory_order_relaxed);
    }
    if(violations.load()!=0){ cerr<<"first_bad code="<<first_bad_code.load()<<" m="<<first_bad_m.load()<<" h="<<first_bad_h.load()<<"\n"; throw runtime_error("Sidorenko violation found"); }
    if(ratio_below_K10.load()!=0) throw runtime_error("ratio below K10 found");

    cout<<"n10_violations=0\n";
    cout<<"n10_K10_hom="<<hK10<<"\n";
    cout<<"n10_K10_ratio_numerator="<<u128str(numK)<<"\n";
    cout<<"n10_K10_ratio_denominator="<<u128str(denK)<<"\n";
    cout<<"n10_global_min_ratio_certificate=K10 PASS\n";
    cout<<"largest_completely_checked_host_order=10\n";
    cout<<"omp_threads="<<omp_get_max_threads()<<"\n";
    cout<<"elapsed_seconds="<<fixed<<setprecision(3)<<chrono::duration<double>(chrono::steady_clock::now()-t0).count()<<"\n";
    cout<<"ALL_EXACT_CHECKS_PASS\n";
    return 0;
}
