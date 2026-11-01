#include <boost/multiprecision/cpp_int.hpp>
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <limits>
#include <map>
#include <numeric>
#include <set>
#include <string>
#include <unordered_map>
#include <utility>
#include <vector>

using boost::multiprecision::cpp_int;
using std::cout;
using std::endl;
using i64 = long long;
using u64 = unsigned long long;

static constexpr int NVAR=6;
static constexpr int NV=64;
static constexpr int HALF=32;
static constexpr int DMAX=32*34;
static constexpr int QLOG=(1<<20);
static constexpr i64 INF = std::numeric_limits<i64>::max()/4;
static const std::vector<int> PRIMES={2,3,5,7,11,13,17,19,23,29,31};

cpp_int ipow(int base, int exp){
    cpp_int b=base, r=1;
    while(exp){
        if(exp&1) r*=b;
        exp>>=1;
        if(exp) b*=b;
    }
    return r;
}

std::map<int,int> log_floor_num;

void init_log_bounds(){
    for(int p:PRIMES){
        if(p==2){ log_floor_num[p]=QLOG; continue; }
        cpp_int z=ipow(p,QLOG);
        int k=boost::multiprecision::msb(z); // floor(log2(p^QLOG))
        log_floor_num[p]=k;
    }
}

std::map<int,int> factor_int(int x){
    std::map<int,int> f;
    for(int p:PRIMES){ while(x%p==0){f[p]++;x/=p;} }
    assert(x==1);
    return f;
}

i64 log_lower_scaled(int a){
    if(a<=1) return 0;
    i64 s=0;
    for(auto [p,e]:factor_int(a)) s += (i64)e*log_floor_num[p];
    return s;
}

i64 log_upper_scaled_prime(int p){
    if(p==2) return QLOG;
    return (i64)log_floor_num[p]+1;
}

i64 tterm_lower_scaled(int a){
    if(a<=1) return 0;
    return (i64)a*a*log_lower_scaled(a);
}

int popc(unsigned x){return __builtin_popcount(x);} 
int g_boundary(int m){
    int s=0; for(int i=0;i<m;i++) s+=popc((unsigned)i);
    return 6*m-2*s;
}

int comb6(int d){ static int c[7]={1,6,15,20,15,6,1}; return c[d]; }

// Minimize a rigorous lower numerator for T_nonempty = sum a_S^2 log2 a_S
// subject only to exact Parseval/influence moments and Walsh-parity/square constraints.
i64 dp_min_tlower(int m, int B, bool &reachable){
    const int Qmass=m*(64-m), Dtarget=32*B;
    std::vector<int> avals;
    for(int a=(m&1); a<=m; a+=2) avals.push_back(a);
    std::unordered_map<int,i64> dp, nd;
    dp.reserve(50000); nd.reserve(50000);
    dp[0]=0; // key = qsum*(DMAX+1)+dsum
    for(int d=1;d<=6;d++){
        for(int rep=0;rep<comb6(d);rep++){
            nd.clear();
            nd.reserve(dp.size()*2+100);
            for(const auto &kv:dp){
                int key=kv.first; i64 val=kv.second;
                int qsum=key/(DMAX+1), dsum=key%(DMAX+1);
                for(int a:avals){
                    int q=a*a;
                    int nq=qsum+q, nds=dsum+d*q;
                    if(nq>Qmass || nds>DMAX) continue;
                    int nk=nq*(DMAX+1)+nds;
                    i64 nv=val+tterm_lower_scaled(a);
                    auto it=nd.find(nk);
                    if(it==nd.end() || nv<it->second) nd[nk]=nv;
                }
            }
            dp.swap(nd);
        }
    }
    int target=Qmass*(DMAX+1)+Dtarget;
    auto it=dp.find(target);
    if(it==dp.end()){reachable=false; return 0;}
    reachable=true; return it->second;
}

i64 L_lower_from_T(int m,int B,i64 Tnon_lower){
    int a0=32-m;
    i64 T0=tterm_lower_scaled(a0);
    i64 exact=(i64)QLOG*1024*5*(B-6);
    i64 neg=(i64)B*961*log_upper_scaled_prime(31);
    return exact + 6*(T0+Tnon_lower) - neg;
}

std::array<int,64> walsh_for_set(u64 mask){
    std::array<int,64> f{}, W{};
    for(int x=0;x<64;x++) f[x]=((mask>>x)&1ULL)?-1:1;
    for(int s=0;s<64;s++){
        int t=0;
        for(int x=0;x<64;x++) t += (((popc((unsigned)(s&x))&1)?-1:1)*f[x]);
        W[s]=t;
    }
    return W;
}

int boundary_of_set(u64 mask){
    int B=0;
    for(int x=0;x<64;x++) if((mask>>x)&1ULL){
        for(int i=0;i<6;i++) if(((mask>>(x^(1<<i)))&1ULL)==0) B++;
    }
    return B;
}

i64 exact_function_Llower(u64 mask){
    auto W=walsh_for_set(mask);
    int B=boundary_of_set(mask);
    i64 Tlow=0;
    for(int s=0;s<64;s++) Tlow += tterm_lower_scaled(std::abs(W[s])/2);
    i64 exact=(i64)QLOG*1024*5*(B-6);
    i64 neg=(i64)B*961*log_upper_scaled_prime(31);
    return exact+6*Tlow-neg;
}

// Exact self-check for no 8-set with 11 induced edges. Enumerate all connected
// 8-sets containing 0 by expansion and deduplicate masks; any 8-set with 11
// edges is connected because every disconnected 8-set has at most emax(7)+emax(1)=9.
std::map<int,long long> enumerate_connected8_edges(){
    std::array<u64,64> nb{};
    for(int x=0;x<64;x++){
        u64 z=0; for(int i=0;i<6;i++) z|=(1ULL<<(x^(1<<i))); nb[x]=z;
    }
    std::set<u64> layer{1ULL};
    for(int k=1;k<8;k++){
        std::set<u64> nxt;
        for(u64 mask:layer){
            u64 bd=0, mm=mask;
            while(mm){int v=__builtin_ctzll(mm); mm&=mm-1; bd|=nb[v];}
            u64 cand=bd&~mask;
            while(cand){u64 bit=cand&-cand; cand-=bit; nxt.insert(mask|bit);}    
        }
        layer.swap(nxt);
    }
    std::map<int,long long> cnt;
    for(u64 mask:layer){
        int e2=0; u64 mm=mask;
        while(mm){int v=__builtin_ctzll(mm); mm&=mm-1; e2+=__builtin_popcountll(nb[v]&mask);} 
        cnt[e2/2]++;
    }
    cout << "connected_8_sets_containing_0=" << layer.size() << "\n";
    return cnt;
}

int main(){
    init_log_bounds();
    cout << "QLOG=" << QLOG << "\n";
    cout << "log_bounds:";
    for(int p:PRIMES){
        cout << " p"<<p<<"=["<<log_floor_num[p]<<","<<(p==2?log_floor_num[p]:log_floor_num[p]+1)<<"]/Q";
    }
    cout << "\n";

    // For B>=36, I=B/32>=9/8. Shannon subadditivity gives
    // H/I <= 6 h_2(I/6)/I <= (16/3) h_2(3/16).
    // Certify that this is strictly below the one-point candidate C6*.
    // 96*(C6* - (16/3)h_2(3/16))
    //   = 3072 + 96 log2 3 + 416 log2 13 - 961 log2 31.
    i64 highB_gap_lower = (i64)3072*QLOG
        + (i64)96*log_floor_num[3]
        + (i64)416*log_floor_num[13]
        - (i64)961*log_upper_scaled_prime(31);
    cout << "highB_gap_96Q_lower_num=" << highB_gap_lower << "\n";
    if(highB_gap_lower<=0){ cout << "HIGH_B_CERTIFICATE=FAIL\n"; return 3; }
    cout << "HIGH_B_CERTIFICATE=PASS\n";

    cout << "g6_m_1_to_32:";
    for(int m=1;m<=32;m++) cout << " "<<m<<":"<<g_boundary(m);
    cout << "\n";

    std::set<std::pair<int,int>> unresolved;
    int proved=0, moment_impossible=0;
    std::vector<int> ms;
    for(int m=1;m<=16;m++) ms.push_back(m);
    ms.push_back(32);
    for(int m:ms){
        int g=g_boundary(m);
        for(int B=g;B<36;B+=2){
            bool reach=false;
            i64 Tmin=dp_min_tlower(m,B,reach);
            if(!reach){
                cout << "relax m="<<m<<" B="<<B<<" state=IMPOSSIBLE_BY_MOMENTS\n";
                moment_impossible++; continue;
            }
            i64 Llo=L_lower_from_T(m,B,Tmin);
            cout << "relax m="<<m<<" B="<<B<<" Llower_num="<<Llo;
            if(Llo>0){ cout << " CERTIFIED_POSITIVE\n"; proved++; }
            else { cout << " UNRESOLVED_RELAX\n"; unresolved.insert({m,B}); }
        }
    }
    cout << "relax_certified="<<proved<<" moment_impossible="<<moment_impossible<<" unresolved_count="<<unresolved.size()<<"\n";
    cout << "unresolved_pairs:";
    for(auto [m,B]:unresolved) cout << " ("<<m<<","<<B<<")";
    cout << "\n";

    // For exact boundary minimizers, Jovanovski Lemma 1 reduces to gamma_m={0,...,m-1} up to cube isomorphism.
    std::set<std::pair<int,int>> residual;
    for(auto [m,B]:unresolved){
        if(B==g_boundary(m)){
            u64 mask = (m==64)?~0ULL:((m==64)?~0ULL:((1ULL<<m)-1ULL));
            i64 Llo=exact_function_Llower(mask);
            cout << "gamma_minimizer m="<<m<<" B="<<B<<" actualB="<<boundary_of_set(mask)<<" Llower_num="<<Llo;
            if(m==1 && B==6){
                cout << " ONEPOINT_EQUALITY_HANDLED_EXACTLY\n";
            } else if(Llo>0){
                cout << " CERTIFIED_POSITIVE\n";
            } else {
                cout << " NEEDS_REVIEW\n"; residual.insert({m,B});
            }
        } else residual.insert({m,B});
    }

    auto ecnt=enumerate_connected8_edges();
    cout << "connected8_edge_hist:";
    for(auto [e,c]:ecnt) cout << " "<<e<<":"<<c;
    cout << "\n";
    cout << "connected8_e11_count="<<ecnt[11]<<"\n";
    if(residual.count({8,26}) && ecnt[11]==0){ residual.erase({8,26}); cout << "pair_(8,26)=IMPOSSIBLE\n"; }

    // m=1,B=6 is the intended equality and does not count as unresolved.
    residual.erase({1,6});
    cout << "final_residual_count="<<residual.size()<<"\n";
    for(auto [m,B]:residual) cout << "FINAL_RESIDUAL ("<<m<<","<<B<<")\n";
    if(!residual.empty()) return 2;
    cout << "C6_CERTIFICATE=PASS\n";
    cout << "candidate_C6_exact=160/3-(961/96)*log2(31)\n";
    return 0;
}
