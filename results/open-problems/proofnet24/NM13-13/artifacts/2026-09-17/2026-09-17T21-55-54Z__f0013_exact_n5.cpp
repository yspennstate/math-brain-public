#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <map>
#include <numeric>
#include <string>
#include <unordered_map>
#include <vector>

using std::array;
using std::cerr;
using std::cout;
using std::map;
using std::string;
using std::unordered_map;
using std::vector;
using i64 = long long;
using u64 = unsigned long long;
using i128 = __int128_t;

// Exact exhaustive certificate for F0013 at n=5.
//
// Diagonal sign conjugation D A D^{-1}=DAD preserves the characteristic
// polynomial. Modulo the trivial D=-I kernel, the action has size 2^(5-1)=16
// and is free because every off-diagonal entry is nonzero. Every orbit has a
// unique representative whose first-row off-diagonal entries are all +1.
// Thus it is enough to enumerate 2^21 representatives and multiply each count
// by 16.
//
// For A = [[a, 1^T],[c,B]], with B 4x4, the block determinant identity gives
//   det(xI-A)=(x-a)det(xI-B)-1^T adj(xI-B)c.
// We compute det(xI-B) and adj(xI-B) exactly from traces / Cayley-Hamilton.
// Every resulting n=5 polynomial is independently rechecked by a direct
// Faddeev-LeVerrier computation on the full 5x5 matrix.

struct ArrHash {
    size_t operator()(array<int,6> const& a) const noexcept {
        u64 h=1469598103934665603ULL;
        for(int x:a){ h ^= (u64)(uint32_t)(x+1000003); h*=1099511628211ULL; }
        return (size_t)h;
    }
};

static vector<i64> signed_divisors(i64 n){
    vector<i64> v;
    if(n==0) return v;
    n=std::llabs(n);
    for(i64 d=1; d*d<=n; ++d) if(n%d==0){
        v.push_back(d); v.push_back(-d);
        if(d*d!=n){ v.push_back(n/d); v.push_back(-(n/d)); }
    }
    std::sort(v.begin(),v.end());
    v.erase(std::unique(v.begin(),v.end()),v.end());
    return v;
}

static bool integer_root(const vector<i64>& c, i64* root){
    i64 C=c.back();
    if(C==0){ *root=0; return true; }
    for(i64 r: signed_divisors(C)){
        i128 y=0;
        for(i64 a:c) y=y*r+a;
        if(y==0){ *root=r; return true; }
    }
    return false;
}

static vector<i64> divide_linear(const vector<i64>& c, i64 r){
    const int n=(int)c.size()-1;
    vector<i64> q(n);
    q[0]=c[0];
    for(int i=1;i<n;i++) q[i]=c[i]+r*q[i-1];
    i64 rem=c[n]+r*q[n-1];
    assert(rem==0);
    return q;
}

static bool divide_quadratic(const vector<i64>& c, i64 a, i64 b, vector<i64>* qout){
    const int n=(int)c.size()-1;
    if(n<2) return false;
    vector<i64> q(n-1,0);
    q[0]=c[0];
    if((int)q.size()>=2) q[1]=c[1]-a*q[0];
    for(int k=2;k<(int)q.size();++k) q[k]=c[k]-a*q[k-1]-b*q[k-2];

    vector<i128> prod(c.size(),0);
    for(int i=0;i<(int)q.size();++i){
        prod[i]+=q[i];
        prod[i+1]+=(i128)a*q[i];
        prod[i+2]+=(i128)b*q[i];
    }
    for(int i=0;i<(int)c.size();++i) if(prod[i]!=(i128)c[i]) return false;
    if(qout) *qout=q;
    return true;
}

static bool find_quadratic_factor(const vector<i64>& c, i64* aa, i64* bb, vector<i64>* quotient){
    const int n=(int)c.size()-1;
    assert(n==4 || n==5);
    assert(c.back()!=0);

    // Gauss lemma makes every Q-factor monic integral. If x^2+a x+b is a
    // factor, then b divides the constant term. Cauchy's root bound R for c
    // gives |a|<=2R because the two roots of the quadratic are roots of c.
    i64 maxcoef=0;
    for(size_t i=1;i<c.size();++i) maxcoef=std::max(maxcoef,std::llabs(c[i]));
    const i64 R=1+maxcoef;
    const i64 abound=2*R;
    for(i64 b: signed_divisors(c.back())){
        for(i64 a=-abound; a<=abound; ++a){
            vector<i64> q;
            if(divide_quadratic(c,a,b,&q)){
                if(aa) *aa=a; if(bb) *bb=b; if(quotient) *quotient=q;
                return true;
            }
        }
    }
    return false;
}

static string factor_pattern(vector<i64> c){
    vector<int> degs;
    while(c.size()>1){
        i64 r=0;
        if(integer_root(c,&r)){
            degs.push_back(1);
            c=divide_linear(c,r);
            continue;
        }
        const int d=(int)c.size()-1;
        if(d<=3){
            degs.push_back(d);
            break;
        }
        i64 a=0,b=0;
        vector<i64> q;
        if(find_quadratic_factor(c,&a,&b,&q)){
            degs.push_back(2);
            c=q;
        } else {
            degs.push_back(d);
            break;
        }
    }
    std::sort(degs.begin(),degs.end());
    string s;
    for(size_t i=0;i<degs.size();++i){ if(i) s+=","; s+=std::to_string(degs[i]); }
    return s;
}

static vector<i64> charpoly_direct(const vector<vector<int>>& A){
    const int n=(int)A.size();
    vector<vector<i64>> P(n,vector<i64>(n)), N(n,vector<i64>(n));
    for(int i=0;i<n;i++) for(int j=0;j<n;j++) P[i][j]=A[i][j];
    vector<i64> tr(n+1,0), coeff(n+1,0); coeff[0]=1;
    for(int k=1;k<=n;k++){
        for(int i=0;i<n;i++) tr[k]+=P[i][i];
        i64 s=0;
        for(int i=1;i<=k;i++) s += coeff[k-i]*tr[i];
        assert(s%k==0);
        coeff[k]=-s/k;
        if(k<n){
            for(int i=0;i<n;i++) for(int j=0;j<n;j++){
                i64 z=0; for(int h=0;h<n;h++) z+=P[i][h]*A[h][j]; N[i][j]=z;
            }
            P.swap(N);
        }
    }
    return coeff;
}

static int modn(i64 x,int p){ int r=(int)(x%p); return r<0?r+p:r; }

static bool irreducible_mod_prime_deg5(const array<int,6>& pdesc, int p){
    // Rabin criterion for monic degree-5 f over F_p (5 is prime):
    // f irreducible iff x^(p^5)=x mod f and gcd(f,x^p-x)=1.
    array<int,6> f{};
    for(int i=0;i<=5;i++) f[5-i]=modn(pdesc[i],p);
    assert(f[5]==1);

    auto mulmod = [&](array<int,5> a, array<int,5> b){
        array<int,9> t{};
        for(int i=0;i<5;i++) for(int j=0;j<5;j++) t[i+j]=modn(t[i+j]+(i64)a[i]*b[j],p);
        for(int d=8;d>=5;--d){
            int z=t[d];
            if(!z) continue;
            for(int j=0;j<5;j++) t[d-5+j]=modn(t[d-5+j]-(i64)z*f[j],p);
        }
        array<int,5> r{}; for(int i=0;i<5;i++) r[i]=modn(t[i],p); return r;
    };
    auto powx = [&](u64 e){
        array<int,5> r{}; r[0]=1;
        array<int,5> b{}; b[1]=1;
        while(e){ if(e&1) r=mulmod(r,b); b=mulmod(b,b); e>>=1; }
        return r;
    };
    auto invmod = [&](int a){ int r=1; for(int i=0;i<p-2;i++) r=(int)((i64)r*a%p); return r; };
    auto gcd_degree = [&](array<int,5> g){
        vector<int> A(6),B(5);
        for(int i=0;i<6;i++) A[i]=f[i];
        for(int i=0;i<5;i++) B[i]=modn(g[i],p);
        auto trim=[&](vector<int>& v){ while(v.size()>1 && modn(v.back(),p)==0) v.pop_back(); };
        trim(A); trim(B);
        while(!(B.size()==1 && B[0]==0)){
            vector<int> R=A;
            int inv=invmod(modn(B.back(),p));
            while(R.size()>=B.size() && !(R.size()==1 && R[0]==0)){
                int shift=(int)R.size()-(int)B.size();
                int q=modn((i64)R.back()*inv,p);
                for(size_t j=0;j<B.size();++j) R[shift+j]=modn(R[shift+j]-(i64)q*B[j],p);
                trim(R);
            }
            A=B; B=R; trim(A); trim(B);
        }
        trim(A);
        return (int)A.size()-1;
    };

    auto xp=powx((u64)p);
    xp[1]=modn(xp[1]-1,p);
    if(gcd_degree(xp)!=0) return false;

    u64 p5=1; for(int i=0;i<5;i++) p5*=p;
    auto xp5=powx(p5);
    xp5[1]=modn(xp5[1]-1,p);
    for(int i=0;i<5;i++) if(modn(xp5[i],p)!=0) return false;
    return true;
}

int main(){
    unordered_map<array<int,6>,u64,ArrHash> poly_weight_reps;
    poly_weight_reps.reserve(5000);

    u64 representatives=0;
    u64 block_direct_mismatches=0;
    u64 parity_failures=0;

    for(uint32_t mask=0; mask<(1u<<16); ++mask){
        int B[4][4];
        for(int i=0;i<4;i++) for(int j=0;j<4;j++) B[i][j]=((mask>>(4*i+j))&1)?1:-1;

        i64 B2[4][4]={},B3[4][4]={},B4[4][4]={};
        for(int i=0;i<4;i++) for(int j=0;j<4;j++){
            for(int k=0;k<4;k++) B2[i][j]+=(i64)B[i][k]*B[k][j];
        }
        for(int i=0;i<4;i++) for(int j=0;j<4;j++){
            for(int k=0;k<4;k++) B3[i][j]+=B2[i][k]*B[k][j];
        }
        for(int i=0;i<4;i++) for(int j=0;j<4;j++){
            for(int k=0;k<4;k++) B4[i][j]+=B3[i][k]*B[k][j];
        }

        i64 tr1=0,tr2=0,tr3=0,tr4=0;
        for(int i=0;i<4;i++){ tr1+=B[i][i]; tr2+=B2[i][i]; tr3+=B3[i][i]; tr4+=B4[i][i]; }
        i64 q1=-tr1;
        i64 n2=tr2+q1*tr1; assert(n2%2==0); i64 q2=-n2/2;
        i64 n3=tr3+q1*tr2+q2*tr1; assert(n3%3==0); i64 q3=-n3/3;
        i64 n4=tr4+q1*tr3+q2*tr2+q3*tr1; assert(n4%4==0); i64 q4=-n4/4;

        i64 s[4][4];
        for(int j=0;j<4;j++){
            i64 b1=0,b2=0,b3=0;
            for(int i=0;i<4;i++){ b1+=B[i][j]; b2+=B2[i][j]; b3+=B3[i][j]; }
            s[j][0]=1;
            s[j][1]=b1+q1;
            s[j][2]=b2+q1*b1+q2;
            s[j][3]=b3+q1*b2+q2*b1+q3;
        }

        for(int cm=0;cm<16;cm++){
            int c[4]; for(int j=0;j<4;j++) c[j]=((cm>>j)&1)?1:-1;
            i64 t[4]={};
            for(int d=0;d<4;d++) for(int j=0;j<4;j++) t[d]+=(i64)c[j]*s[j][d];

            for(int a=-1;a<=1;a+=2){
                array<int,6> p={1,
                    (int)(q1-a),
                    (int)(q2-a*q1-t[0]),
                    (int)(q3-a*q2-t[1]),
                    (int)(q4-a*q3-t[2]),
                    (int)(-a*q4-t[3])};

                vector<vector<int>> A(5,vector<int>(5));
                A[0][0]=a; for(int j=1;j<5;j++) A[0][j]=1;
                for(int i=1;i<5;i++){ A[i][0]=c[i-1]; for(int j=1;j<5;j++) A[i][j]=B[i-1][j-1]; }
                vector<i64> direct=charpoly_direct(A);
                bool same=true; for(int k=0;k<6;k++) if(direct[k]!=p[k]) same=false;
                if(!same) ++block_direct_mismatches;

                // A is the all-ones matrix mod 2, so chi_A=x^5+x^4 mod 2.
                if((p[0]&1)!=1 || (p[1]&1)!=1 || (p[2]&1) || (p[3]&1) || (p[4]&1) || (p[5]&1)) ++parity_failures;

                ++poly_weight_reps[p];
                ++representatives;
            }
        }
    }

    assert(representatives==(1ULL<<21));
    assert(block_direct_mismatches==0);
    assert(parity_failures==0);

    const u64 orbit_size=16;
    const u64 total=representatives*orbit_size;
    assert(total==(1ULL<<25));

    map<string,u64> pattern_matrix_counts;
    map<string,u64> pattern_poly_counts;
    const vector<int> primes={3,5,7,11,13,17,19,23,29,31,37,41};
    map<int,u64> min_witness_matrix_counts;
    map<int,u64> single_prime_irred_matrix_counts;
    u64 q_irred=0, witness_union=0;
    u64 classification_disagreements=0;

    for(const auto& kv: poly_weight_reps){
        vector<i64> coeff(kv.first.begin(),kv.first.end());
        string pat=factor_pattern(coeff);
        const u64 matrix_weight=kv.second*orbit_size;
        pattern_matrix_counts[pat]+=matrix_weight;
        pattern_poly_counts[pat]++;
        const bool qirr=(pat=="5");
        if(qirr) q_irred+=matrix_weight;

        int firstw=0;
        for(int prime:primes){
            if(irreducible_mod_prime_deg5(kv.first,prime)){
                single_prime_irred_matrix_counts[prime]+=matrix_weight;
                if(firstw==0) firstw=prime;
            }
        }
        const bool cert_irred=(firstw!=0);
        if(cert_irred){ witness_union+=matrix_weight; min_witness_matrix_counts[firstw]+=matrix_weight; }
        if(qirr!=cert_irred) ++classification_disagreements;
    }

    // Regression: reproduce the exact n=4 atlas from the previous run.
    map<string,u64> n4;
    for(uint32_t mask=0;mask<(1u<<16);++mask){
        vector<vector<int>> A(4,vector<int>(4));
        for(int i=0;i<4;i++) for(int j=0;j<4;j++) A[i][j]=((mask>>(4*i+j))&1)?1:-1;
        vector<i64> p=charpoly_direct(A);
        n4[factor_pattern(p)]++;
    }
    assert(n4["1,1,1,1"]==10560);
    assert(n4["1,1,2"]==24544);
    assert(n4["1,3"]==19968);
    assert(n4["2,2"]==1440);
    assert(n4["4"]==9024);

    assert(classification_disagreements==0);
    assert(q_irred==witness_union);
    u64 sum=0; for(auto const& x:pattern_matrix_counts) sum+=x.second; assert(sum==total);

    cout << "F0013 exact n=5 exhaustive certificate\n";
    cout << "canonical_representatives=" << representatives << "\n";
    cout << "diagonal_sign_orbit_size=" << orbit_size << "\n";
    cout << "expanded_total_matrices=" << total << "\n";
    cout << "distinct_characteristic_polynomials=" << poly_weight_reps.size() << "\n";
    cout << "block_vs_direct_charpoly_mismatches=" << block_direct_mismatches << "\n";
    cout << "mod2_parity_failures=" << parity_failures << "\n";
    cout << "n4_regression=PASS\n";

    cout << "factor_pattern_matrix_counts:\n";
    for(auto const& x:pattern_matrix_counts) cout << "  " << x.first << " : " << x.second << "\n";
    cout << "factor_pattern_distinct_polynomial_counts:\n";
    for(auto const& x:pattern_poly_counts) cout << "  " << x.first << " : " << x.second << "\n";

    const u64 g=std::gcd(q_irred,total);
    cout << "Q_irreducible_matrices=" << q_irred << "\n";
    cout << "Q_reducible_matrices=" << total-q_irred << "\n";
    cout << "P_Q_irreducible=" << q_irred/g << "/" << total/g << "\n";
    cout << "P_Q_reducible=" << (total-q_irred)/g << "/" << total/g << "\n";

    u64 cumulative=0;
    cout << "modular_irreducibility_certificate_cumulative_union:\n";
    for(int prime:primes){
        auto it=min_witness_matrix_counts.find(prime);
        if(it!=min_witness_matrix_counts.end()) cumulative+=it->second;
        cout << "  primes<= " << prime << " : " << cumulative << "\n";
    }
    cout << "modular_witness_union=" << witness_union << "\n";
    cout << "Q_vs_modular_certificate_disagreements=" << classification_disagreements << "\n";
    cout << "minimum_witness_prime_distribution:\n";
    for(auto const& x:min_witness_matrix_counts) cout << "  " << x.first << " : " << x.second << "\n";
    cout << "single_prime_irreducible_counts:\n";
    for(int prime:primes) cout << "  " << prime << " : " << single_prime_irred_matrix_counts[prime] << "\n";

    cout << "ALL_EXACT_CHECKS_PASS\n";
    return 0;
}
