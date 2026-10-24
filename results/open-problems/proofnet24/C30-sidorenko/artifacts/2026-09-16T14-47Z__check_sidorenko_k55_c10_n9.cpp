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
static u128 pow128(u128 a,int e){ u128 r=1; while(e--){r*=a;} return r; }

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
            while(!seen[cur]){
                seen[cur]=true; auto [a,b]=pairs[cur]; cur=edge_idx[perm[a]][perm[b]];
            }
        }
        total += 1ULL<<orbits;
    } while(next_permutation(perm.begin(),perm.end()));
    if(total%fact) throw runtime_error("Burnside divisibility failed");
    return total/fact;
}

static inline int edge_count(u64 code){ return __builtin_popcountll(code); }

static inline uint64_t hom_H_n9(u64 code){
    // H=K_{5,5}\\C_10; exact five-common-neighbor contraction, regrouped in c.
    uint16_t nb[9]{}; int bit=0;
    for(int j=1;j<9;j++) for(int i=0;i<j;i++,bit++) if((code>>bit)&1ULL){ nb[i]|=uint16_t(1u<<j); nb[j]|=uint16_t(1u<<i); }
    uint8_t C[9][9][9];
    for(int a=0;a<9;a++) for(int b=0;b<9;b++){
        uint16_t ab=nb[a]&nb[b];
        for(int c=0;c<9;c++) C[a][b][c]=(uint8_t)__builtin_popcount((unsigned)(ab&nb[c]));
    }
    uint64_t h=0;
    for(int a=0;a<9;a++) for(int b=0;b<9;b++) for(int d=0;d<9;d++) for(int e=0;e<9;e++){
        unsigned r=0;
        for(int c=0;c<9;c++) r += unsigned(C[a][b][c])*unsigned(C[b][c][d])*unsigned(C[c][d][e]);
        h += uint64_t(r)*uint64_t(C[d][e][a])*uint64_t(C[e][a][b]);
    }
    if(h>3486784401ULL) throw runtime_error("hom upper bound failed");
    return h;
}

static uint64_t hom_contraction_slow(u64 code,int n){
    uint16_t nb[9]{}; int bit=0;
    for(int j=1;j<n;j++) for(int i=0;i<j;i++,bit++) if((code>>bit)&1ULL){nb[i]|=uint16_t(1u<<j);nb[j]|=uint16_t(1u<<i);}
    uint8_t C[9][9][9]{};
    for(int a=0;a<n;a++)for(int b=0;b<n;b++){uint16_t ab=nb[a]&nb[b];for(int c=0;c<n;c++)C[a][b][c]=(uint8_t)__builtin_popcount((unsigned)(ab&nb[c]));}
    uint64_t h=0;
    for(int a=0;a<n;a++)for(int b=0;b<n;b++)for(int c=0;c<n;c++)for(int d=0;d<n;d++)for(int e=0;e<n;e++)
        h += uint64_t(C[c][d][e])*C[d][e][a]*C[e][a][b]*C[a][b][c]*C[b][c][d];
    return h;
}

int main(int argc,char**argv){
    if(argc!=2){ cerr<<"usage: checker atlas7_codes.txt\n"; return 2; }
    auto t0=chrono::steady_clock::now();
    cout<<"C30 Sidorenko exact n=9 certificate\n";
    cout<<"H=K_{5,5}\\C_10; v(H)=10; e(H)=15\n";
    cout<<"arithmetic=integer_exact; floating_point_decisions=NONE\n" << flush;

    vector<u64> c7raw; { ifstream f(argv[1]); if(!f) throw runtime_error("cannot open atlas7 data"); u64 x; while(f>>x)c7raw.push_back(x); }
    if(c7raw.size()!=1044) throw runtime_error("atlas7 row count !=1044");
    auto U7=burnside_unlabeled_count(7), U8=burnside_unlabeled_count(8), U9=burnside_unlabeled_count(9);
    if(U7!=1044 || U8!=12346 || U9!=274668) throw runtime_error("Burnside count mismatch");
    cout<<"burnside_counts: U7="<<U7<<" U8="<<U8<<" U9="<<U9<<" PASS\n" << flush;

    Canon C;
    unordered_set<u64> s7; s7.reserve(1500);
    for(u64 x:c7raw) s7.insert(C(x,7));
    if(s7.size()!=U7) throw runtime_error("atlas7 canonical uniqueness/completeness failed");
    vector<u64> c7(s7.begin(),s7.end()); sort(c7.begin(),c7.end());
    cout<<"n7_base: rows=1044 canonical_unique=1044 burnside=1044 COMPLETE=PASS\n";

    unordered_set<u64> s8; s8.reserve(20000); uint64_t ext8=0;
    for(u64 base:c7) for(unsigned mask=0;mask<(1u<<7);mask++){ ext8++; s8.insert(C(base|(u64(mask)<<21),8)); }
    if(ext8!=1044ULL*128 || s8.size()!=U8) throw runtime_error("complete n8 augmentation failed");
    vector<u64> c8(s8.begin(),s8.end()); sort(c8.begin(),c8.end());
    cout<<"n8_generation: raw_extensions="<<ext8<<" canonical_classes="<<c8.size()<<" burnside="<<U8<<" COMPLETE=PASS\n" << flush;

    unordered_set<u64> s9; s9.reserve(350000); uint64_t ext9=0;
    for(u64 base:c8) for(unsigned mask=0;mask<(1u<<8);mask++){ ext9++; s9.insert(C(base|(u64(mask)<<28),9)); }
    if(ext9!=12346ULL*256 || s9.size()!=U9) throw runtime_error("complete n9 augmentation failed");
    vector<u64> c9(s9.begin(),s9.end()); sort(c9.begin(),c9.end());
    cout<<"n9_generation: raw_extensions="<<ext9<<" canonical_classes="<<c9.size()<<" burnside="<<U9<<" COMPLETE=PASS\n" << flush;

    // Exact implementation cross-check on 256 deterministically selected n=9 canonical classes.
    for(size_t k=0;k<256;k++){
        size_t idx=(k*(c9.size()-1))/255;
        if(hom_H_n9(c9[idx])!=hom_contraction_slow(c9[idx],9)) throw runtime_error("hom implementation cross-check failed");
    }
    cout<<"hom_fast_vs_direct_contraction_256_spread_classes=PASS\n";

    const u128 n20=pow128(9,20);
    // K9 is the all-edge code on 36 edges. Compute its exact ratio benchmark and test whether it is globally minimal.
    const u64 K9=(1ULL<<36)-1;
    const u64 hK9=hom_H_n9(K9);
    const u128 numK=u128(hK9)*n20;
    const u128 denK=pow128(72,15);
    // For each possible edge count m, precompute the least integer h that can meet K9's ratio:
    // h*n20/(2m)^15 >= numK/denK iff h >= ceil(numK*(2m)^15/(denK*n20)).
    uint64_t hthreshold[37]{};
    for(int m=1;m<=36;m++){
        cpp_int A=cpp_int(numK)*cpp_int(pow128(2*m,15));
        cpp_int B=cpp_int(denK)*cpp_int(n20);
        cpp_int q=(A+B-1)/B;
        hthreshold[m]=q.convert_to<uint64_t>();
    }

    atomic<long long> violations(0), ratio_below_K9(0);
    atomic<uint64_t> min_defect_low64(ULLONG_MAX); // display only for defects fitting low64 is not relied upon.
    u64 first_bad_code=0; int first_bad_m=0; uint64_t first_bad_h=0; i128 first_bad_D=0;
    #pragma omp parallel for schedule(dynamic,256)
    for(long long ii=0;ii<(long long)c9.size();ii++){
        u64 code=c9[ii]; int m=edge_count(code); uint64_t h=hom_H_n9(code);
        i128 D=i128(u128(h)*n20)-i128(pow128(2*m,15));
        if(D<0){
            long long old=violations.fetch_add(1);
            if(old==0){
                #pragma omp critical(firstbad)
                { first_bad_code=code; first_bad_m=m; first_bad_h=h; first_bad_D=D; }
            }
        }
        if(m>0 && h<hthreshold[m]) ratio_below_K9.fetch_add(1);
    }
    if(violations.load()!=0){ cerr<<"first_bad code="<<first_bad_code<<" m="<<first_bad_m<<" h="<<first_bad_h<<" D="<<i128str(first_bad_D)<<"\n"; throw runtime_error("Sidorenko violation found"); }
    if(ratio_below_K9.load()!=0) throw runtime_error("ratio below K9 found");
    cout<<"n9_violations=0\n";
    cout<<"n9_K9_hom="<<hK9<<"\n";
    cout<<"n9_K9_ratio_numerator="<<u128str(numK)<<"\n";
    cout<<"n9_K9_ratio_denominator="<<u128str(denK)<<"\n";
    cout<<"n9_global_min_ratio_certificate=K9 PASS\n";
    cout<<"largest_completely_checked_host_order=9\n";
    cout<<"omp_threads="<<omp_get_max_threads()<<"\n";
    cout<<"elapsed_seconds="<<fixed<<setprecision(3)<<chrono::duration<double>(chrono::steady_clock::now()-t0).count()<<"\n";
    cout<<"ALL_EXACT_CHECKS_PASS\n";
}
