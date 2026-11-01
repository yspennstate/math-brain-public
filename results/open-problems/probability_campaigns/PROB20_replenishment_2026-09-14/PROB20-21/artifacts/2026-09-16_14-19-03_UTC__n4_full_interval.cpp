#include <gmp.h>
#include <gmpxx.h>
#include <algorithm>
#include <array>
#include <cassert>
#include <cmath>
#include <chrono>
#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <tuple>
#include <unordered_set>
#include <utility>
#include <vector>

extern "C" {
typedef long mpfr_prec_t;
typedef int mpfr_sign_t;
typedef long mpfr_exp_t;
typedef enum { MPFR_RNDN=0, MPFR_RNDZ=1, MPFR_RNDU=2, MPFR_RNDD=3, MPFR_RNDA=4, MPFR_RNDF=5 } mpfr_rnd_t;
typedef struct { mpfr_prec_t _mpfr_prec; mpfr_sign_t _mpfr_sign; mpfr_exp_t _mpfr_exp; mp_limb_t *_mpfr_d; } __mpfr_struct;
typedef __mpfr_struct mpfr_t[1];
typedef __mpfr_struct* mpfr_ptr;
typedef const __mpfr_struct* mpfr_srcptr;
void mpfr_init2(mpfr_ptr, mpfr_prec_t);
void mpfr_clear(mpfr_ptr);
int mpfr_set_q(mpfr_ptr, mpq_srcptr, mpfr_rnd_t);
int mpfr_set_ui(mpfr_ptr, unsigned long, mpfr_rnd_t);
int mpfr_set_si(mpfr_ptr, long, mpfr_rnd_t);
int mpfr_set(mpfr_ptr, mpfr_srcptr, mpfr_rnd_t);
int mpfr_log(mpfr_ptr, mpfr_srcptr, mpfr_rnd_t);
int mpfr_neg(mpfr_ptr, mpfr_srcptr, mpfr_rnd_t);
int mpfr_add(mpfr_ptr, mpfr_srcptr, mpfr_srcptr, mpfr_rnd_t);
int mpfr_sub(mpfr_ptr, mpfr_srcptr, mpfr_srcptr, mpfr_rnd_t);
int mpfr_mul(mpfr_ptr, mpfr_srcptr, mpfr_srcptr, mpfr_rnd_t);
int mpfr_div_ui(mpfr_ptr, mpfr_srcptr, unsigned long, mpfr_rnd_t);
int mpfr_cmp_si(mpfr_srcptr, long);
int mpfr_cmp(mpfr_srcptr, mpfr_srcptr);
double mpfr_get_d(mpfr_srcptr, mpfr_rnd_t);
}

static constexpr int NV=4;
static constexpr int N=16;
static constexpr uint32_t FULL=(1u<<16)-1;
static constexpr mpfr_prec_t PREC=256;

static mpq_class Q(long n,long d=1){ mpq_class q(n,d); q.canonicalize(); return q; }

struct MP {
    mpfr_t v;
    MP(){ mpfr_init2(v,PREC); mpfr_set_ui(v,0,MPFR_RNDN); }
    ~MP(){ mpfr_clear(v); }
    MP(const MP&)=delete; MP& operator=(const MP&)=delete;
};

static void setq(MP& x, const mpq_class& q, mpfr_rnd_t r){ mpfr_set_q(x.v,q.get_mpq_t(),r); }
static double getd(const MP& x){ return mpfr_get_d(x.v,MPFR_RNDN); }

static void neglog_bounds(const mpq_class& q, MP& lo, MP& hi){
    MP qlo,qhi,lgu,lgd;
    setq(qlo,q,MPFR_RNDD); setq(qhi,q,MPFR_RNDU);
    mpfr_log(lgu.v,qhi.v,MPFR_RNDU);
    mpfr_neg(lo.v,lgu.v,MPFR_RNDD);
    mpfr_log(lgd.v,qlo.v,MPFR_RNDD);
    mpfr_neg(hi.v,lgd.v,MPFR_RNDU);
}

static void entropy_bounds(const mpq_class& q, MP& lo, MP& hi){
    if(q==0 || q==1){ mpfr_set_ui(lo.v,0,MPFR_RNDN); mpfr_set_ui(hi.v,0,MPFR_RNDN); return; }
    mpq_class r=1-q;
    MP qlo,qhi,rlo,rhi,nlqlo,nlqhi,nlrlo,nlrhi,t1lo,t1hi,t2lo,t2hi;
    setq(qlo,q,MPFR_RNDD); setq(qhi,q,MPFR_RNDU);
    setq(rlo,r,MPFR_RNDD); setq(rhi,r,MPFR_RNDU);
    neglog_bounds(q,nlqlo,nlqhi); neglog_bounds(r,nlrlo,nlrhi);
    mpfr_mul(t1lo.v,qlo.v,nlqlo.v,MPFR_RNDD);
    mpfr_mul(t1hi.v,qhi.v,nlqhi.v,MPFR_RNDU);
    mpfr_mul(t2lo.v,rlo.v,nlrlo.v,MPFR_RNDD);
    mpfr_mul(t2hi.v,rhi.v,nlrhi.v,MPFR_RNDU);
    mpfr_add(lo.v,t1lo.v,t2lo.v,MPFR_RNDD);
    mpfr_add(hi.v,t1hi.v,t2hi.v,MPFR_RNDU);
}

static void ln_integer_bounds(unsigned long a, MP& lo, MP& hi){
    MP x; mpfr_set_ui(x.v,a,MPFR_RNDN);
    mpfr_log(lo.v,x.v,MPFR_RNDD); mpfr_log(hi.v,x.v,MPFR_RNDU);
}

static std::array<int,N> perm_map(const std::array<int,NV>& perm, int shift){
    std::array<int,N> out{};
    for(int x=0;x<N;x++){
        int y=0;
        for(int i=0;i<NV;i++) if((x>>i)&1) y|=1<<perm[i];
        out[x]=y^shift;
    }
    return out;
}

static uint32_t transform_mask(uint32_t mask, const std::array<int,N>& mp){
    uint32_t out=0;
    for(int x=0;x<N;x++) if((mask>>x)&1u) out |= 1u<<mp[x];
    return out;
}

static bool is_constant(uint32_t m){ return m==0 || m==FULL; }
static bool is_dictator(uint32_t m){
    for(int i=0;i<NV;i++){
        bool ok1=true,ok0=true;
        for(int x=0;x<N;x++){
            int v=(m>>x)&1u, xi=(x>>i)&1;
            if(v!=xi) ok1=false;
            if(v!=(1-xi)) ok0=false;
        }
        if(ok1||ok0) return true;
    }
    return false;
}

using Poly=std::array<mpq_class,5>;
static const int BINOM[5]={1,4,6,4,1};

static Poly qpoly(uint32_t mask,int y){
    int c[5]={0,0,0,0,0};
    for(int x=0;x<N;x++) if((mask>>x)&1u) c[__builtin_popcount((unsigned)(x^y))]++;
    Poly p;
    for(int d=0;d<5;d++) p[d]=Q(c[d],BINOM[d]);
    return p;
}

static std::pair<Poly,Poly> subdivide(const Poly& c, const mpq_class& t){
    mpq_class row[5][5];
    for(int i=0;i<5;i++) row[0][i]=c[i];
    for(int r=1;r<5;r++) for(int i=0;i<5-r;i++) row[r][i]=(1-t)*row[r-1][i]+t*row[r-1][i+1];
    Poly L,R;
    for(int i=0;i<5;i++){ L[i]=row[i][0]; R[i]=row[4-i][i]; }
    return {L,R};
}

static Poly restrict_poly(const Poly& c, const mpq_class& a, const mpq_class& b){
    Poly left=c;
    if(b!=1) left=subdivide(c,b).first;
    if(a==0) return left;
    return subdivide(left,a/b).second;
}

static mpq_class eval_poly(const Poly& c, const mpq_class& a){
    std::vector<mpq_class> cur(c.begin(),c.end());
    while(cur.size()>1){
        std::vector<mpq_class> nxt;
        for(size_t i=0;i+1<cur.size();i++) nxt.push_back((1-a)*cur[i]+a*cur[i+1]);
        cur.swap(nxt);
    }
    return cur[0];
}

static std::string pkey(const Poly& p){
    std::ostringstream os;
    for(int i=0;i<5;i++) os<<p[i].get_num()<<'/'<<p[i].get_den()<<';';
    return os.str();
}

struct Group { Poly p; int mult; };

static std::array<mpq_class,N> walsh_pm(uint32_t mask){
    std::array<mpq_class,N> c;
    for(int S=0;S<N;S++){
        int s=0;
        for(int x=0;x<N;x++){
            int v=((mask>>x)&1u)?-1:1;
            int chi=(__builtin_popcount((unsigned)(x&S))&1)?-1:1;
            s += v*chi;
        }
        c[S]=Q(s,N);
    }
    return c;
}

static void entropy_min_endpoint(const mpq_class& loq, const mpq_class& hiq, MP& hlo, MP& hhi){
    mpq_class dlo=abs(2*loq-1), dhi=abs(2*hiq-1);
    entropy_bounds(dlo>=dhi?loq:hiq,hlo,hhi);
}

static void D_point(uint32_t mask,const mpq_class& a,const std::vector<Group>& groups, MP& dlo, MP& dhi, const MP& ln2lo,const MP& ln2hi){
    mpq_class p=Q(__builtin_popcount(mask),N);
    MP halo,hahi,hplo,hphi,sumlo,sumhi;
    entropy_bounds(a,halo,hahi); entropy_bounds(p,hplo,hphi);
    mpfr_set(dlo.v,ln2lo.v,MPFR_RNDD); mpfr_set(dhi.v,ln2hi.v,MPFR_RNDU);
    mpfr_sub(dlo.v,dlo.v,hahi.v,MPFR_RNDD); mpfr_sub(dhi.v,dhi.v,halo.v,MPFR_RNDU);
    mpfr_sub(dlo.v,dlo.v,hphi.v,MPFR_RNDD); mpfr_sub(dhi.v,dhi.v,hplo.v,MPFR_RNDU);
    mpfr_set_ui(sumlo.v,0,MPFR_RNDN); mpfr_set_ui(sumhi.v,0,MPFR_RNDN);
    for(const auto& g:groups){
        mpq_class q=eval_poly(g.p,a); MP qlo,qhi;
        entropy_bounds(q,qlo,qhi);
        for(int k=0;k<g.mult;k++){
            mpfr_add(sumlo.v,sumlo.v,qlo.v,MPFR_RNDD);
            mpfr_add(sumhi.v,sumhi.v,qhi.v,MPFR_RNDU);
        }
    }
    mpfr_div_ui(sumlo.v,sumlo.v,N,MPFR_RNDD); mpfr_div_ui(sumhi.v,sumhi.v,N,MPFR_RNDU);
    mpfr_add(dlo.v,dlo.v,sumlo.v,MPFR_RNDD); mpfr_add(dhi.v,dhi.v,sumhi.v,MPFR_RNDU);
}

static void D_interval_lower(uint32_t mask,const mpq_class& a,const mpq_class& b,const std::vector<Group>& groups, MP& dlo,const MP& ln2lo){
    mpq_class p=Q(__builtin_popcount(mask),N);
    MP hbL,hbU,hpL,hpU,sumL;
    entropy_bounds(b,hbL,hbU); entropy_bounds(p,hpL,hpU);
    mpfr_set(dlo.v,ln2lo.v,MPFR_RNDD);
    mpfr_sub(dlo.v,dlo.v,hbU.v,MPFR_RNDD);
    mpfr_sub(dlo.v,dlo.v,hpU.v,MPFR_RNDD);
    mpfr_set_ui(sumL.v,0,MPFR_RNDN);
    for(const auto& g:groups){
        Poly r=restrict_poly(g.p,a,b);
        mpq_class lo=r[0],hi=r[0];
        for(int i=1;i<5;i++){ if(r[i]<lo) lo=r[i]; if(r[i]>hi) hi=r[i]; }
        MP hL,hU; entropy_min_endpoint(lo,hi,hL,hU);
        for(int k=0;k<g.mult;k++) mpfr_add(sumL.v,sumL.v,hL.v,MPFR_RNDD);
    }
    mpfr_div_ui(sumL.v,sumL.v,N,MPFR_RNDD);
    mpfr_add(dlo.v,dlo.v,sumL.v,MPFR_RNDD);
}

int main(int argc,char**argv){
    auto t0=std::chrono::steady_clock::now();
    std::vector<std::array<int,N>> maps;
    std::array<int,NV> p={0,1,2,3};
    do{ for(int s=0;s<N;s++) maps.push_back(perm_map(p,s)); }while(std::next_permutation(p.begin(),p.end()));
    assert(maps.size()==384);

    std::vector<char> seen(1u<<16,0); std::vector<uint32_t> reps; std::vector<int> osizes;
    for(uint32_t m=0;m<(1u<<16);m++) if(!seen[m]){
        std::set<uint32_t> orb;
        for(const auto& mp:maps){ uint32_t z=transform_mask(m,mp); orb.insert(z); orb.insert(FULL^z); }
        for(uint32_t z:orb) seen[z]=1;
        reps.push_back(*orb.begin()); osizes.push_back((int)orb.size());
    }
    assert(reps.size()==222); int osum=std::accumulate(osizes.begin(),osizes.end(),0); assert(osum==65536);

    std::map<uint32_t,std::vector<Group>> G;
    for(uint32_t m:reps){
        std::map<std::string,std::pair<Poly,int>> tmp;
        for(int y=0;y<N;y++){ Poly q=qpoly(m,y); auto k=pkey(q); auto it=tmp.find(k); if(it==tmp.end()) tmp[k]={q,1}; else it->second.second++; }
        std::vector<Group> vv; for(auto &kv:tmp) vv.push_back({kv.second.first,kv.second.second}); G[m]=vv;
    }

    std::vector<uint32_t> nontriv,balnon,bias;
    for(uint32_t m:reps) if(!is_constant(m)&&!is_dictator(m)){ nontriv.push_back(m); if(__builtin_popcount(m)==8) balnon.push_back(m); else bias.push_back(m); }

    MP ln2lo,ln2hi; ln_integer_bounds(2,ln2lo,ln2hi);

    mpq_class minDelta; uint32_t minDeltaMask=0; bool have=false;
    for(uint32_t m:nontriv){ auto c=walsh_pm(m); mpq_class mu=c[0],var=1-mu*mu,W1=0; for(int i=0;i<NV;i++) W1+=c[1<<i]*c[1<<i]; mpq_class d=var-W1; assert(d>0); if(!have||d<minDelta){have=true;minDelta=d;minDeltaMask=m;} }
    assert(minDelta==Q(11,64));

    mpq_class minAS; uint32_t minASMask=0; have=false;
    for(uint32_t m:balnon){ long ss=0; for(int x=0;x<N;x++) for(int i=0;i<NV;i++) ss += (((m>>x)&1u)!=((m>>(x^(1<<i)))&1u)); mpq_class av=Q(ss,N); if(!have||av<minAS){have=true;minAS=av;minASMask=m;} }
    assert(minAS==Q(3,2));

    mpq_class A0=Q(1,1024), A1=Q(63,128), rho0=Q(1,64);
    MP haL,haU,h7L,h7U,biasedGap;
    entropy_bounds(A0,haL,haU); entropy_bounds(Q(7,16),h7L,h7U);
    mpfr_set(biasedGap.v,ln2lo.v,MPFR_RNDD); mpfr_sub(biasedGap.v,biasedGap.v,haU.v,MPFR_RNDD); mpfr_sub(biasedGap.v,biasedGap.v,h7U.v,MPFR_RNDD);
    assert(mpfr_cmp_si(biasedGap.v,0)>0);

    mpq_class c0=Q(1023,1024); c0=c0*c0*c0; mpq_class coeff=Q(3,2)*c0-1;
    MP ln1024L,ln1024U,ln4L,ln4U,cfL,term1,term2,balMargin;
    ln_integer_bounds(1024,ln1024L,ln1024U); ln_integer_bounds(4,ln4L,ln4U); setq(cfL,coeff,MPFR_RNDD);
    mpfr_mul(term1.v,cfL.v,ln1024L.v,MPFR_RNDD);
    MP threehalfU; setq(threehalfU,Q(3,2),MPFR_RNDU); mpfr_mul(term2.v,threehalfU.v,ln4U.v,MPFR_RNDU);
    mpfr_sub(balMargin.v,term1.v,term2.v,MPFR_RNDD); MP one; mpfr_set_ui(one.v,1,MPFR_RNDN); mpfr_sub(balMargin.v,balMargin.v,one.v,MPFR_RNDD);
    assert(mpfr_cmp_si(balMargin.v,0)>0);
    assert(1-(Q(1023,1024)*Q(1023,1024)*Q(1023,1024)*Q(1023,1024)) < Q(1,2));

    mpq_class highL=Q(11,64)*(1-rho0*rho0);
    mpq_class highR=8*Q(7,8)*rho0+16*rho0*rho0;
    assert(highL>highR);

    double gridMin=1e100; uint32_t gridMask=0; mpq_class gridA;
    for(uint32_t m:nontriv){
        for(int j=0;j<=64;j++){
            mpq_class a=Q(j,128);
            MP dl,du; D_point(m,a,G[m],dl,du,ln2lo,ln2hi);
            if(mpfr_cmp_si(du.v,0)<0){ std::cerr<<"CERTIFIED COUNTEREXAMPLE GRID mask="<<m<<" a="<<a<<"\n"; return 3; }
            if(j>0&&j<64){ double mid=(getd(dl)+getd(du))/2; if(mid<gridMin){gridMin=mid;gridMask=m;gridA=a;} }
        }
    }

    struct Node{mpq_class a,b;int d;};
    long long leaves=0; int maxDepth=0; double minLower=1e100; uint32_t minMask=0; mpq_class minA,minB; int minD=0;
    for(uint32_t m:nontriv){
        std::vector<Node> st; st.push_back({A0,A1,0});
        while(!st.empty()){
            Node z=st.back();st.pop_back(); MP dl; D_interval_lower(m,z.a,z.b,G[m],dl,ln2lo);
            if(mpfr_cmp_si(dl.v,0)>0){
                leaves++; maxDepth=std::max(maxDepth,z.d); double v=mpfr_get_d(dl.v,MPFR_RNDD); if(v<minLower){minLower=v;minMask=m;minA=z.a;minB=z.b;minD=z.d;} continue;
            }
            if(z.d>=24){ std::cerr<<"UNCERTIFIED MIDDLE mask="<<m<<" a="<<z.a<<" b="<<z.b<<" depth="<<z.d<<" lower="<<getd(dl)<<"\n"; return 4; }
            mpq_class mid=(z.a+z.b)/2; st.push_back({mid,z.b,z.d+1}); st.push_back({z.a,mid,z.d+1});
        }
    }

    auto t1=std::chrono::steady_clock::now(); double sec=std::chrono::duration<double>(t1-t0).count();

    std::ostringstream out;
    out<<std::setprecision(17);
    out<<"PROB20-21 N<=4 FULL-NOISE-INTERVAL CERTIFICATE: PASS\n";
    out<<"model_runtime_metadata=UNVERIFIED\n";
    out<<"metric_before=UNMEASURED\nmetric_after=4\n";
    out<<"n4_truth_tables=65536\n";
    out<<"symmetry_group_size=768\ninput_symmetry_size=384\n";
    out<<"n4_orbits=222\nnontrivial_orbits="<<nontriv.size()<<"\n";
    out<<"balanced_nondictator_orbits="<<balnon.size()<<"\nbiased_nontrivial_orbits="<<bias.size()<<"\n";
    out<<"full_alpha_interval=[0,1/2]\nlow_noise=[0,1/1024]\nmiddle=[1/1024,63/128]\nhigh_noise=[63/128,1/2]\n";
    out<<"min_Delta_var_minus_W1="<<minDelta<<" mask="<<minDeltaMask<<"\n";
    out<<"min_balanced_nondictator_avg_sensitivity="<<minAS<<" mask="<<minASMask<<"\n";
    out<<"biased_low_noise_lower_gap_nat="<<mpfr_get_d(biasedGap.v,MPFR_RNDD)<<"\n";
    out<<"balanced_low_noise_uniform_margin_over_alpha="<<mpfr_get_d(balMargin.v,MPFR_RNDD)<<"\n";
    out<<"high_noise_exact_lhs="<<highL<<"\nhigh_noise_exact_rhs="<<highR<<"\n";
    out<<"counterexample_grid_points_per_orbit=65\ncounterexample_grid_certified_negative=0\n";
    out<<"grid_smallest_interior_D_approx="<<gridMin<<" mask="<<gridMask<<" alpha="<<gridA<<"\n";
    out<<"middle_leaf_intervals="<<leaves<<"\nmiddle_max_bisection_depth="<<maxDepth<<"\n";
    out<<"middle_min_outward_lower_D_nat="<<minLower<<" mask="<<minMask<<" a="<<minA<<" b="<<minB<<" depth="<<minD<<"\n";
    out<<"log_engine=MPFR_4.x_shared_library_directed_rounding_256_bits_exact_rational_inputs\n";
    out<<"checker_runtime_seconds="<<sec<<"\n";
    std::cout<<out.str();
    if(argc>1){ std::ofstream f(argv[1]); f<<out.str(); }
    return 0;
}
