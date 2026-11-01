#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <iomanip>
#include <limits>
#include <map>
#include <numeric>
#include <set>
#include <string>
#include <unordered_map>
#include <utility>
#include <vector>
#include <boost/multiprecision/cpp_int.hpp>
using boost::multiprecision::cpp_int;

static const int PNUM=11;
static const int PRIMES[PNUM]={2,3,5,7,11,13,17,19,23,29,31};
static const uint64_t QLOG=(1u<<20);
using EVec=std::array<int64_t,PNUM>;

static cpp_int ipow(cpp_int base,uint64_t exp){
    cpp_int r=1;
    while(exp){ if(exp&1) r*=base; exp>>=1; if(exp) base*=base; }
    return r;
}
struct LogBounds { std::array<uint64_t,PNUM> k{}; };
static LogBounds make_bounds(){
    LogBounds b;
    for(int j=0;j<PNUM;j++){
        cpp_int x=ipow(cpp_int(PRIMES[j]),QLOG);
        b.k[j]=boost::multiprecision::msb(x);
    }
    return b;
}
static int val(int a,int p){ int v=0; while(a>0 && a%p==0){a/=p;v++;} return v; }
static EVec term_vec(int a){
    EVec e{};
    if(a<=1) return e;
    int rem=a;
    for(int j=0;j<PNUM;j++){
        int v=0; while(rem%PRIMES[j]==0){rem/=PRIMES[j];v++;}
        if(v) e[j]=(int64_t)a*a*v;
    }
    if(rem!=1){ std::cerr<<"unfactored amplitude "<<a<<" rem="<<rem<<"\n"; std::exit(2); }
    return e;
}
static EVec addv(const EVec&a,const EVec&b){ EVec c{}; for(int j=0;j<PNUM;j++)c[j]=a[j]+b[j]; return c; }
static EVec subv(const EVec&a,const EVec&b){ EVec c{}; for(int j=0;j<PNUM;j++)c[j]=a[j]-b[j]; return c; }
static bool eqv(const EVec&a,const EVec&b){return a==b;}

// Exact sign of sum_j (a_j-b_j) log2(PRIMES[j]). Returns -1,0,+1.
// Fast rigorous dyadic enclosure; rare unresolved case falls back to exact integer products.
static int cmp_logs(const EVec&a,const EVec&b,const LogBounds&lb){
    EVec d=subv(a,b);
    bool all0=true; for(auto x:d) if(x){all0=false;break;} if(all0)return 0;
    __int128 lo=0,hi=0;
    for(int j=0;j<PNUM;j++){
        int64_t e=d[j]; if(!e)continue;
        if(j==0){ lo+=(__int128)e*QLOG; hi+=(__int128)e*QLOG; }
        else if(e>0){lo+=(__int128)e*lb.k[j]; hi+=(__int128)e*(lb.k[j]+1);}
        else {lo+=(__int128)e*(lb.k[j]+1); hi+=(__int128)e*lb.k[j];}
    }
    if(lo>0)return 1; if(hi<0)return -1;
    // Exact fallback: compare products of prime powers.
    cpp_int pos=1,neg=1;
    for(int j=0;j<PNUM;j++){
        if(d[j]>0) pos*=ipow(cpp_int(PRIMES[j]),(uint64_t)d[j]);
        else if(d[j]<0) neg*=ipow(cpp_int(PRIMES[j]),(uint64_t)(-d[j]));
    }
    if(pos<neg)return -1; if(pos>neg)return 1; return 0;
}

struct Best { bool ok=false; EVec t{}; };
static void relax_best(Best &dst,const EVec&cand,const LogBounds&lb){
    if(!dst.ok || cmp_logs(cand,dst.t,lb)<0){dst.ok=true;dst.t=cand;}
}

static int popc(unsigned x){return __builtin_popcount(x);}
static int edge_iso_E(int k){ int s=0; for(int j=0;j<k;j++)s+=popc((unsigned)j); return s; }
static int UEDGE[7][65];
static void init_edge_upper(){
    for(int d=0;d<=6;d++) for(int k=0;k<=64;k++) UEDGE[d][k]=-1000000;
    UEDGE[0][0]=UEDGE[0][1]=0;
    for(int d=1;d<=6;d++){
        int cap=1<<d, half=1<<(d-1);
        for(int k=0;k<=cap;k++){
            int best=-1000000;
            for(int a=0;a<=half;a++){ int b=k-a; if(b<0||b>half)continue;
                best=std::max(best,UEDGE[d-1][a]+UEDGE[d-1][b]+std::min(a,b));
            }
            UEDGE[d][k]=best;
        }
    }
}
static int bmin_cube6(int k){return 6*k-2*UEDGE[6][k];}
static const int MULT[7]={0,6,15,20,15,6,1};

// For a fixed number c of coefficients, compute min T log-vector for each attainable total square mass.
static std::vector<Best> local_profile(int c,int k,int Mlim,const LogBounds&lb){
    std::vector<int> amps;
    for(int a=(k&1);a<=k;a+=2) amps.push_back(a);
    std::vector<Best> dp(Mlim+1),ndp(Mlim+1); dp[0].ok=true;
    for(int pos=0;pos<c;pos++){
        for(auto &x:ndp)x=Best{};
        for(int m=0;m<=Mlim;m++) if(dp[m].ok){
            for(int a:amps){ int nm=m+a*a; if(nm>Mlim)continue;
                EVec cand=addv(dp[m].t,term_vec(a)); relax_best(ndp[nm],cand,lb);
            }
        }
        dp.swap(ndp);
    }
    return dp;
}

struct Key {int m,q; bool operator<(const Key&o)const{return m<o.m||(m==o.m&&q<o.q);} };
struct RelaxResult { std::map<Key,EVec> final; };
static RelaxResult spectral_relax(int k,const LogBounds&lb){
    int M=k*(64-k);
    std::array<std::vector<Best>,7> prof;
    for(int d=1;d<=6;d++) prof[d]=local_profile(MULT[d],k,M,lb);
    std::map<Key,EVec> cur,nxt; cur[{0,0}]=EVec{};
    for(int d=1;d<=6;d++){
        nxt.clear();
        std::vector<std::pair<int,EVec>> opts;
        for(int lm=0;lm<=M;lm++) if(prof[d][lm].ok) opts.push_back({lm,prof[d][lm].t});
        for(const auto &kv:cur){
            for(const auto&o:opts){
                int nm=kv.first.m+o.first; if(nm>M) continue;
                int nq=kv.first.q+d*o.first;
                EVec cand=addv(kv.second,o.second);
                Key key{nm,nq}; auto it=nxt.find(key);
                if(it==nxt.end()) nxt.emplace(key,cand);
                else if(cmp_logs(cand,it->second,lb)<0) it->second=cand;
            }
        }
        cur.swap(nxt);
    }
    RelaxResult rr;
    for(const auto&kv:cur) if(kv.first.m==M) rr.final.emplace(kv.first,kv.second);
    return rr;
}

static EVec total_T_with_empty(int k,const EVec&nonempty){ return addv(term_vec(32-k),nonempty); }
static EVec L_vec(int B,const EVec&T){
    EVec e{};
    e[0]+=5120LL*(B-6); // integer c = c log2 2
    for(int j=0;j<PNUM;j++) e[j]+=6*T[j];
    e[10]-=961LL*B; // -961 B log2 31
    return e;
}
static int sign_L(int B,const EVec&T,const LogBounds&lb){ EVec z{}; return cmp_logs(L_vec(B,T),z,lb); }

// Walsh/edge exact evaluation for a subset mask represented as vector vertices.
static EVec subset_T(const std::vector<int>&S){
    int k=(int)S.size(); EVec t=term_vec(32-k);
    for(int s=1;s<64;s++){
        int sum=0; for(int x:S) sum += (__builtin_parity((unsigned)(s&x)) ? -1 : 1);
        int a=std::abs(sum); t=addv(t,term_vec(a));
    }
    return t;
}
static int induced_edges(const std::vector<int>&S){
    uint64_t mask=0; for(int x:S)mask|=(1ULL<<x);
    int e=0; for(int x:S) for(int i=0;i<6;i++){int y=x^(1<<i); if(x<y && ((mask>>y)&1ULL))e++;}
    return e;
}
static void spectrum_checks(const std::vector<int>&S,int B,const EVec&T){
    int k=S.size(); long long mass=0,q=0;
    int a0=32-k; mass+=(long long)a0*a0;
    for(int s=1;s<64;s++){
        int z=0;for(int x:S)z+=(__builtin_parity((unsigned)(s&x))?-1:1);
        int a=std::abs(z); mass+=(long long)a*a; q+=(long long)popc(s)*a*a;
    }
    if(mass!=1024){std::cerr<<"Parseval fail k="<<k<<" mass="<<mass<<"\n";std::exit(7);}
    if(q!=32LL*B){std::cerr<<"influence Fourier fail k="<<k<<" q="<<q<<" B="<<B<<"\n";std::exit(7);}
    (void)T;
}

struct DenseStats { uint64_t leaves=0, strict=0, ties=0, bad=0; int64_t min_dummy=0; };
static DenseStats dense_stats;
static int target_k,target_e,target_B;
static const LogBounds* GLB=nullptr;
static std::vector<int> chosen;

static int deg_to_chosen(int v){int d=0; for(int x:chosen) if(popc((unsigned)(v^x))==1)d++; return d;}

static void dfs_dense(int start,int ecur){
    int s=chosen.size(); int r=target_k-s;
    if(r==0){
        if(ecur!=target_e)return;
        dense_stats.leaves++;
        EVec T=subset_T(chosen); spectrum_checks(chosen,target_B,T);
        int sg=sign_L(target_B,T,*GLB);
        if(sg>0)dense_stats.strict++; else if(sg==0)dense_stats.ties++; else {dense_stats.bad++; std::cerr<<"COUNTEREXAMPLE leaf k="<<target_k<<" B="<<target_B<<"\n";}
        return;
    }
    if(ecur>target_e)return;
    if(64-start<r)return;
    // rigorous upper bound on additional edges: best cross-to-current plus global max internal edges among r new vertices.
    std::vector<int> ds; ds.reserve(64-start);
    for(int v=start;v<64;v++) ds.push_back(deg_to_chosen(v));
    std::sort(ds.begin(),ds.end(),std::greater<int>());
    int maxadd=UEDGE[6][r]; for(int i=0;i<r && i<(int)ds.size();i++) maxadd+=ds[i];
    if(ecur+maxadd<target_e)return;
    // include/exclude via increasing combination enumeration
    int vmax=64-r;
    for(int v=start;v<=vmax;v++){
        int d=deg_to_chosen(v);
        if(ecur+d>target_e) continue;
        chosen.push_back(v);
        dfs_dense(v+1,ecur+d);
        chosen.pop_back();
    }
}

int main(){
    std::cout<<"P03 exact C6 verifier: spectral integer relaxation + dense-boundary exact enumeration\n";
    init_edge_upper();
    for(int k=0;k<=64;k++){ if(UEDGE[6][k]!=edge_iso_E(k)){std::cerr<<"edge-upper recurrence mismatch k="<<k<<" U="<<UEDGE[6][k]<<" E="<<edge_iso_E(k)<<"\n";return 9;} }
    std::cout<<"edge_upper_recurrence_verified_for_Q6: U6(k)=sum_{j<k}popcount(j) for k=0..64\n";
    LogBounds lb=make_bounds();
    std::cout<<"QLOG="<<QLOG<<"; exact product fallback enabled\n";
    for(int j=0;j<PNUM;j++) std::cout<<"prime="<<PRIMES[j]<<" floor(QLOG*log2 p)="<<lb.k[j]<<"\n";
    std::cout<<"candidate C6 = 160/3 - (961/96) log2(31)\n";
    std::cout<<std::setprecision(17);
    long double c6=160.0L/3.0L-(961.0L/96.0L)*log2l(31.0L);
    std::cout<<"candidate_decimal="<<(double)c6<<" (display only; never used for decisions)\n";

    std::set<std::pair<int,int>> exceptions;
    uint64_t relax_valid_states=0, relax_positive=0, relax_zero=0, relax_negative=0;
    std::cout<<"RELAXATION SUMMARY\n";
    for(int k=1;k<=32;k++){
        RelaxResult rr=spectral_relax(k,lb);
        int bmin=bmin_cube6(k);
        int valid=0,pos=0,zero=0,neg=0;
        for(const auto&kv:rr.final){
            int q=kv.first.q;
            if(q%64!=0)continue; // because B even in Q6
            int B=q/32;
            if(B<bmin || B>6*k)continue;
            valid++; relax_valid_states++;
            EVec T=total_T_with_empty(k,kv.second);
            int sg=sign_L(B,T,lb);
            if(sg>0){pos++;relax_positive++;}
            else if(sg==0){zero++;relax_zero++; exceptions.insert({k,B});}
            else {neg++;relax_negative++;exceptions.insert({k,B});}
        }
        std::cout<<"k="<<k<<" bmin="<<bmin<<" valid_relax_states="<<valid<<" strict="<<pos<<" zero="<<zero<<" noncertifying_negative="<<neg;
        if(zero||neg){std::cout<<" exception_B="; for(auto pr:exceptions)if(pr.first==k)std::cout<<pr.second<<",";}
        std::cout<<"\n";
    }
    std::cout<<"relax_totals valid="<<relax_valid_states<<" strict="<<relax_positive<<" zero="<<relax_zero<<" negative="<<relax_negative<<"\n";
    std::cout<<"noncertifying_pairs:"; for(auto p:exceptions)std::cout<<" (k="<<p.first<<",B="<<p.second<<")"; std::cout<<"\n";

    // Expected exact exception set: equality at k=1,B=6 plus a short list requiring direct enumeration.
    std::set<std::pair<int,int>> expected={{1,6},{4,16},{5,20},{6,22},{7,24},{8,24},{8,26},{9,28},{10,30},{12,32},{14,34},{16,32}};
    if(exceptions!=expected){
        std::cerr<<"FAIL: relaxation exception set differs from expected.\n";
        return 10;
    }

    // k=1 is the candidate equality family. Directly verify the rooted singleton.
    chosen={0}; EVec T1=subset_T(chosen); spectrum_checks(chosen,6,T1);
    if(sign_L(6,T1,lb)!=0){std::cerr<<"FAIL singleton not exact tie\n";return 11;}
    std::cout<<"singleton_rooted_tie=1; by translations there are 64 singleton functions and by output complement 128 literal extremizers\n";

    std::cout<<"DENSE EXCEPTION ENUMERATION (translation-normalized by 0 in minority set)\n";
    uint64_t allleaves=0,allstrict=0,allties=0;
    for(auto pr:exceptions){
        int k=pr.first,B=pr.second; if(k==1)continue;
        int num=6*k-B;
        if(num%2){std::cerr<<"bad parity target\n";return 12;}
        target_k=k;target_B=B;target_e=num/2;GLB=&lb;dense_stats=DenseStats{};chosen.clear();chosen.push_back(0);
        dfs_dense(1,0);
        std::cout<<"k="<<k<<" B="<<B<<" target_internal_edges="<<target_e<<" rooted_exact_sets="<<dense_stats.leaves<<" strict="<<dense_stats.strict<<" ties="<<dense_stats.ties<<" bad="<<dense_stats.bad<<"\n";
        if(dense_stats.bad||dense_stats.ties||dense_stats.strict!=dense_stats.leaves){std::cerr<<"FAIL dense comparison k="<<k<<" B="<<B<<"\n";return 13;}
        allleaves+=dense_stats.leaves;allstrict+=dense_stats.strict;allties+=dense_stats.ties;
    }
    std::cout<<"dense_totals rooted_exact_sets="<<allleaves<<" strict="<<allstrict<<" ties="<<allties<<"\n";
    std::cout<<"PASS: C6 is exactly 160/3-(961/96)log2(31); equality only for truth-table Hamming weight 1 or 63.\n";
    std::cout<<"Coverage certificate: output complement reduces to 1<=k<=32; spectral relaxation certifies every feasible (k,B) outside the listed pairs; for every remaining pair, translation puts 0 in the minority set and the branch-and-bound enumerates every exact-edge k-subset containing 0.\n";
    return 0;
}
