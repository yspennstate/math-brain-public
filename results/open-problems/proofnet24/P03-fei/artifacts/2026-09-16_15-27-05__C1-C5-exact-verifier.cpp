#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iomanip>
#include <iostream>
#include <limits>
#include <numeric>
#include <set>
#include <string>
#include <vector>
#include <boost/multiprecision/cpp_int.hpp>
using boost::multiprecision::cpp_int;

static const int PRIMES[6] = {2,3,5,7,11,13};
static const uint64_t Q = (1u<<20);

static inline int parity32(uint32_t x){ return __builtin_parity(x); }
static inline int popc32(uint32_t x){ return __builtin_popcount(x); }

struct Data4 {
    std::array<int16_t,16> W{};
    uint8_t boundary=0;
};

static Data4 calc4(uint16_t tt){
    Data4 d;
    for(int s=0;s<16;s++){
        int w=0;
        for(int x=0;x<16;x++){
            int fx = ((tt>>x)&1) ? -1 : +1;
            int chi = parity32((uint32_t)(s&x)) ? -1 : +1;
            w += fx*chi;
        }
        d.W[s]=(int16_t)w;
    }
    int b=0;
    for(int i=0;i<4;i++) for(int x=0;x<16;x++) if(((x>>i)&1)==0){
        int y=x^(1<<i);
        b += (((tt>>x)&1) != ((tt>>y)&1));
    }
    d.boundary=(uint8_t)b;
    return d;
}

static std::vector<std::array<int,4>> perms4(){
    std::vector<std::array<int,4>> ps;
    std::array<int,4> p={0,1,2,3};
    do{ ps.push_back(p); }while(std::next_permutation(p.begin(),p.end()));
    return ps;
}

// y_i = x_{p[i]} xor neg_i; transformed output g(x)=f(y) xor outflip.
static uint16_t transform4(uint16_t f,const std::array<int,4>& p,int neg,int outflip){
    uint16_t g=0;
    for(int x=0;x<16;x++){
        int y=0;
        for(int i=0;i<4;i++){
            int bit=((x>>p[i])&1)^((neg>>i)&1);
            y |= bit<<i;
        }
        int val=((f>>y)&1)^outflip;
        g |= (uint16_t)val<<x;
    }
    return g;
}

static std::vector<uint16_t> npn_reps4(){
    auto ps=perms4();
    std::vector<uint8_t> seen(1u<<16,0);
    std::vector<uint16_t> reps;
    for(uint32_t f=0;f<(1u<<16);f++) if(!seen[f]){
        uint16_t rep=(uint16_t)f;
        reps.push_back(rep);
        for(const auto& p:ps) for(int neg=0;neg<16;neg++) for(int out=0;out<2;out++){
            seen[transform4(rep,p,neg,out)]=1;
        }
    }
    return reps;
}

struct LogBounds {
    std::array<uint64_t,6> k{}; // k/Q <= log2 p < (k+1)/Q
};

static cpp_int ipow(cpp_int base,uint64_t exp){
    cpp_int r=1;
    while(exp){
        if(exp&1) r*=base;
        exp>>=1;
        if(exp) base*=base;
    }
    return r;
}

static LogBounds exact_log_bounds(){
    LogBounds b;
    for(int j=0;j<6;j++){
        cpp_int x=ipow(cpp_int(PRIMES[j]),Q);
        unsigned msb_index=boost::multiprecision::msb(x);
        b.k[j]=msb_index; // floor(log2(p^Q)) = floor(Q log2 p)
        // exact defining inequalities are automatic from bit length; assert 2^k <= x < 2^(k+1)
    }
    return b;
}

static int valuation(int a,int p){
    int v=0;
    while(a>0 && a%p==0){a/=p;v++;}
    return v;
}

struct CertResult {
    bool tie=false;
    bool positive=false;
    bool inconclusive=false;
    int64_t lower_num=0; // Q*L lower bound numerator
    std::array<int64_t,6> e{};
};

static CertResult certify_candidate(int n,int B,const std::vector<int>& aval,const LogBounds& lb){
    CertResult cr;
    if(n==1){
        // Only two nonconstant functions, ratio exactly 0; caller handles as ties.
        cr.tie=true;
        return cr;
    }
    const int A=1<<(n-1);
    std::array<int64_t,6> e{};
    e[0] += (int64_t)A*A*(n-1)*(B-n); // log2(2)=1 encoded as coefficient of log2 2
    for(int a:aval) if(a>1){
        int rem=a;
        for(int j=0;j<6;j++){
            int v=valuation(rem,PRIMES[j]);
            if(v){ e[j] += (int64_t)n*a*a*v; for(int t=0;t<v;t++) rem/=PRIMES[j]; }
        }
        if(rem!=1){
            std::cerr<<"unfactored a="<<a<<" n="<<n<<" rem="<<rem<<"\n";
            std::exit(2);
        }
    }
    int ap=A-1;
    if(ap>1){
        int rem=ap;
        for(int j=0;j<6;j++){
            int v=valuation(rem,PRIMES[j]);
            if(v){ e[j] -= (int64_t)B*(A-1)*(A-1)*v; for(int t=0;t<v;t++) rem/=PRIMES[j]; }
        }
        if(rem!=1){ std::cerr<<"unfactored A-1\n"; std::exit(2); }
    }
    cr.e=e;
    bool allzero=true;
    for(auto z:e) if(z!=0) allzero=false;
    if(allzero){ cr.tie=true; return cr; }
    // Since log2 2 = 1 exactly, use exact Q for p=2 rather than interval.
    __int128 lower=0, upper=0;
    for(int j=0;j<6;j++){
        int64_t ej=e[j];
        if(j==0){
            lower += (__int128)ej*Q;
            upper += (__int128)ej*Q;
        }else if(ej>0){
            lower += (__int128)ej*lb.k[j];
            upper += (__int128)ej*(lb.k[j]+1);
        }else if(ej<0){
            lower += (__int128)ej*(lb.k[j]+1);
            upper += (__int128)ej*lb.k[j];
        }
    }
    if(lower>std::numeric_limits<int64_t>::max() || lower<std::numeric_limits<int64_t>::min()){
        std::cerr<<"lower overflow int64 reporting\n"; std::exit(2);
    }
    cr.lower_num=(int64_t)lower;
    if(lower>0) cr.positive=true;
    else if(upper<0){ // would be a rigorous counterexample to candidate
        std::cerr<<"RIGOROUS COUNTEREXAMPLE: n="<<n<<" B="<<B<<" lower="<<(long long)lower<<" upper="<<(long long)upper<<"\n";
        std::exit(3);
    }else cr.inconclusive=true;
    return cr;
}

static std::vector<int> walsh_abs_halves_raw(uint32_t tt,int n){
    int N=1<<n;
    std::vector<int> a(N);
    for(int s=0;s<N;s++){
        int w=0;
        for(int x=0;x<N;x++){
            int fx=((tt>>x)&1)?-1:+1;
            int chi=parity32((uint32_t)(s&x))?-1:+1;
            w += fx*chi;
        }
        a[s]=std::abs(w)/2;
    }
    return a;
}

static int boundary_raw(uint32_t tt,int n){
    int N=1<<n,b=0;
    for(int i=0;i<n;i++) for(int x=0;x<N;x++) if(((x>>i)&1)==0){
        int y=x^(1<<i);
        b += (((tt>>x)&1)!=((tt>>y)&1));
    }
    return b;
}

struct ScanStats {
    uint64_t nonconstant=0,ties=0,strict=0,inconclusive=0;
    uint64_t tie_onepoint=0;
    int64_t min_positive_lower=std::numeric_limits<int64_t>::max();
};

static ScanStats scan_raw(int n,const LogBounds& lb){
    ScanStats st;
    uint64_t total=1ull<<(1<<n);
    uint32_t allmask=(n==5)?0xffffffffu:((1u<<(1<<n))-1u);
    for(uint64_t fu=0;fu<total;fu++){
        uint32_t f=(uint32_t)fu;
        if(f==0 || f==allmask) continue;
        st.nonconstant++;
        int B=boundary_raw(f,n);
        auto a=walsh_abs_halves_raw(f,n);
        CertResult cr=certify_candidate(n,B,a,lb);
        if(cr.tie){
            st.ties++;
            int wt=popc32(f);
            if(std::min(wt,(1<<n)-wt)==1) st.tie_onepoint++;
        }else if(cr.positive){
            st.strict++;
            st.min_positive_lower=std::min(st.min_positive_lower,cr.lower_num);
        }else st.inconclusive++;
    }
    return st;
}

static ScanStats scan_n5_reduced(const std::vector<uint16_t>& reps,const std::vector<Data4>& d4,const LogBounds& lb){
    ScanStats st;
    std::vector<int> aval(32);
    for(uint16_t g:reps){
        const auto& G=d4[g];
        for(uint32_t hu=0;hu<65536;hu++){
            uint16_t h=(uint16_t)hu;
            if(g==0 && h==0) continue;
            if(g==0xffffu && h==0xffffu) continue;
            st.nonconstant++;
            const auto& H=d4[h];
            int B=(int)G.boundary+(int)H.boundary+popc32((uint32_t)(g^h));
            for(int s=0;s<16;s++){
                aval[s]=std::abs((int)G.W[s]+(int)H.W[s])/2;
                aval[s+16]=std::abs((int)G.W[s]-(int)H.W[s])/2;
            }
            CertResult cr=certify_candidate(5,B,aval,lb);
            if(cr.tie){
                st.ties++;
                int wt=popc32(g)+popc32(h);
                if(std::min(wt,32-wt)==1) st.tie_onepoint++;
            }else if(cr.positive){
                st.strict++;
                st.min_positive_lower=std::min(st.min_positive_lower,cr.lower_num);
            }else st.inconclusive++;
        }
    }
    return st;
}

static void print_stats(int n,const ScanStats& s,const std::string& mode){
    std::cout<<"n="<<n<<" mode="<<mode
             <<" nonconstant="<<s.nonconstant
             <<" ties="<<s.ties
             <<" ties_onepoint_or_complement="<<s.tie_onepoint
             <<" strict="<<s.strict
             <<" inconclusive="<<s.inconclusive;
    if(s.strict) std::cout<<" min_strict_QtimesL_lower="<<s.min_positive_lower;
    std::cout<<"\n";
}

int main(){
    std::cout<<"P03 exact C_n verifier, integer-only comparison core\n";
    std::cout<<"Q="<<Q<<" for dyadic log2-prime certificates\n";
    LogBounds lb=exact_log_bounds();
    for(int j=0;j<6;j++){
        std::cout<<"prime="<<PRIMES[j]<<" k="<<lb.k[j]
                 <<" certificate: k/Q <= log2(p) < (k+1)/Q\n";
    }

    std::vector<Data4> d4(65536);
    for(uint32_t f=0;f<65536;f++) d4[f]=calc4((uint16_t)f);
    auto reps=npn_reps4();
    std::cout<<"NPN4_representatives="<<reps.size()<<" expected=222\n";
    if(reps.size()!=222){ std::cerr<<"FAIL NPN class count\n"; return 4; }

    for(int n=1;n<=4;n++){
        ScanStats s=scan_raw(n,lb);
        print_stats(n,s,"full");
        if(s.inconclusive || s.ties!=s.tie_onepoint){ std::cerr<<"FAIL raw scan n="<<n<<"\n"; return 5; }
    }
    ScanStats s5=scan_n5_reduced(reps,d4,lb);
    print_stats(5,s5,"222x65536 NPN-reduced");
    uint64_t expected=(uint64_t)222*65536ull-1ull; // only all-plus constant occurs since 0 is the chosen constant representative; output complement is in its orbit
    std::cout<<"n=5 reduced_expected_nonconstant="<<expected<<"\n";
    if(s5.nonconstant!=expected || s5.inconclusive || s5.ties!=s5.tie_onepoint){
        std::cerr<<"FAIL n=5 scan\n"; return 6;
    }

    std::cout<<"Candidate exact formulas (bits):\n";
    std::cout<<"C1 = 0\n";
    std::cout<<"C2 = 2\n";
    std::cout<<"C3 = 16/3 - (3/2) log2(3)\n";
    std::cout<<"C4 = 12 - (49/16) log2(7)\n";
    std::cout<<"C5 = 128/5 - (45/8) log2(15)\n";
    std::cout<<std::setprecision(17);
    std::cout<<"PASS: exact comparison certificates prove candidate >= every covered function; equality only for one-point flips/output complements.\n";
    std::cout<<"Coverage proof obligation used by checker: every 5-variable truth table f=(g,h) is NPN-equivalent, using only the first four inputs plus output complement, to one with g among the 222 representatives; h is then arbitrary and is exhaustively scanned.\n";
    return 0;
}
