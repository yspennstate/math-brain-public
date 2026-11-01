#include <boost/multiprecision/cpp_int.hpp>
#include <cstdint>
#include <functional>
#include <iostream>
#include <vector>
using boost::multiprecision::cpp_int;
using std::cout; using std::cerr; using std::vector;
using u128 = __uint128_t;

static uint64_t mod_cpp(const cpp_int& x, uint64_t m){ return (uint64_t)(x % m); }
static uint64_t mulmod(uint64_t a, uint64_t b, uint64_t m){ return (uint64_t)((u128)a*b % m); }
static long long egcd(long long a,long long b,long long&x,long long&y){
    if(!b){x=1;y=0;return a;}
    long long x1,y1; long long g=egcd(b,a%b,x1,y1);
    x=y1; y=x1-y1*(a/b); return g;
}
static uint64_t invmod(uint64_t a,uint64_t m){
    long long x,y; long long g=egcd((long long)a,(long long)m,x,y);
    if(g!=1){ cerr << "inverse failure\n"; std::exit(3); }
    __int128 z=x; z%=(__int128)m; if(z<0) z+=m; return (uint64_t)z;
}

int main(){
    const uint64_t p=256717, q=800000, d=q-p;
    const uint64_t b=4220452010631561279ULL;
    const cpp_int a("1995237757733917147310102692686664915858011319606812684127301");
    const cpp_int M("5000000000000000000");
    cpp_int c[8];
    for(int k=0;k<=6;k++){
        cpp_int qq=1, pp=1;
        for(int j=0;j<6-k;j++) qq*=q;
        for(int j=0;j<k;j++) pp*=p;
        c[k]=qq*d*pp;
    }
    c[7]=1; for(int j=0;j<7;j++) c[7]*=p;
    const cpp_int D_R=c[0]+c[3]+c[6]+c[7];
    const uint64_t H=2200;
    const cpp_int T_max=D_R+cpp_int(H)*c[7];
    const cpp_int D_new=T_max+1;
    if(D_new*M>a){ cerr<<"non-tight-row branch would fail\n"; return 4; }

    // For a tight row i: V_i=b, (BV)_i=a.  If s_j=aV_j-b(BV)_j,
    // T_i=sum_j B_ij s_j is an integer satisfying T_i == a^2 (mod b).
    // The inherited four-band theorem implies, after grouping by label type,
    // T_i=sum_k c_k S_k with S0>=1, S7>=1,
    // S1+S2+S3>=1, S4+S5+S6>=1.
    // We exhaust every such relaxed tuple with T_i<=T_max.
    const uint64_t target=mod_cpp(a*a,b);
    uint64_t cm[8]; for(int k=0;k<8;k++) cm[k]=mod_cpp(c[k],b);
    const uint64_t inv7=invmod(cm[7],b);

    vector<uint64_t> s(8,0);
    uint64_t nodes=0, leaves=0;
    bool found=false; cpp_int best=0;

    std::function<void(int,const cpp_int&,uint64_t)> rec;
    rec=[&](int k,const cpp_int& total,uint64_t residue){
        if(found && total>=best) return;
        if(k==7){
            if(s[1]+s[2]+s[3]==0) return;
            if(s[4]+s[5]+s[6]==0) return;
            cpp_int rem=T_max-total;
            if(rem<c[7]) return;
            uint64_t max7=(uint64_t)(rem/c[7]);
            uint64_t needmod=(target + b - residue)%b;
            uint64_t need=mulmod(needmod,inv7,b);
            if(need==0) need=b; // S7 must be positive.
            ++leaves;
            if(need>=1 && need<=max7){
                cpp_int T=total+cpp_int(need)*c[7];
                if(!found || T<best){ found=true; best=T; }
            }
            return;
        }
        cpp_int rem=T_max-total;
        uint64_t maxs=(uint64_t)(rem/c[k]);
        uint64_t r=residue;
        for(uint64_t z=0;z<=maxs;z++){
            s[k]=z; ++nodes;
            rec(k+1,total+cpp_int(z)*c[k],r);
            r+=cm[k]; if(r>=b) r-=b;
        }
    };

    // S0 is positive by the inherited four-band theorem.  Enumerate all
    // possible S0 under the budget, then S1,...,S6; solve S7 exactly modulo b.
    uint64_t max0=(uint64_t)(T_max/c[0]);
    for(uint64_t s0=1;s0<=max0;s0++){
        s[0]=s0;
        rec(1,cpp_int(s0)*c[0],mulmod(cm[0],s0,b));
    }

    cout << "P02 T02 successor-slack semigroup checker\n";
    cout << "target_a2_mod_b=" << target << "\n";
    cout << "D_R=" << D_R << "\n";
    cout << "c7=" << c[7] << "\n";
    cout << "H=" << H << "\n";
    cout << "T_max=D_R+H*c7=" << T_max << "\n";
    cout << "D_new=T_max+1=" << D_new << "\n";
    cout << "max_S0_under_budget=" << max0 << "\n";
    cout << "enumeration_nodes=" << nodes << "\n";
    cout << "modular_leaf_tests=" << leaves << "\n";
    cout << "congruent_relaxed_tuple_found=" << (found?1:0) << "\n";
    if(found) cout << "best_congruent_T=" << best << "\n";
    if(found){ cerr << "unexpected relaxed tuple at or below threshold\n"; return 5; }
    cout << "NO_CONGRUENT_RELAXED_T_AT_OR_BELOW_THRESHOLD=PASS\n";
    cout << "D_NEW_TIMES_M_LE_A=PASS\n";
    cout << "TIGHT_ROW_SLACK_GAP_D_NEW=PASS\n";
    cout << "ALL_EXACT_CHECKS_PASS\n";
    return 0;
}
