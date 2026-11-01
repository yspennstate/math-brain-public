#include <gmp.h>
#include <gmpxx.h>
#include <algorithm>
#include <array>
#include <cassert>
#include <chrono>
#include <cmath>
#include <cstdint>
#include <iomanip>
#include <functional>
#include <iostream>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <tuple>
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
int mpfr_div(mpfr_ptr, mpfr_srcptr, mpfr_srcptr, mpfr_rnd_t);
int mpfr_div_ui(mpfr_ptr, mpfr_srcptr, unsigned long, mpfr_rnd_t);
int mpfr_cmp_si(mpfr_srcptr, long);
int mpfr_cmp(mpfr_srcptr, mpfr_srcptr);
double mpfr_get_d(mpfr_srcptr, mpfr_rnd_t);
}

static constexpr int NV=5;
static constexpr int N=32;
static constexpr uint32_t FULL=0xffffffffu;
static constexpr mpfr_prec_t PREC=256;
static constexpr int DEG=5;
static const int BINOM[6]={1,5,10,10,5,1};

static mpq_class Q(long n,long d=1){ mpq_class q(n,d); q.canonicalize(); return q; }

struct MP {
    mpfr_t v;
    MP(){ mpfr_init2(v,PREC); mpfr_set_ui(v,0,MPFR_RNDN); }
    ~MP(){ mpfr_clear(v); }
    MP(const MP&)=delete; MP& operator=(const MP&)=delete;
};
static void setq(MP& x,const mpq_class&q,mpfr_rnd_t r){ mpfr_set_q(x.v,q.get_mpq_t(),r); }
static double getd(const MP&x){ return mpfr_get_d(x.v,MPFR_RNDN); }

static void neglog_bounds(const mpq_class&q,MP&lo,MP&hi){
    MP qlo,qhi,lgu,lgd;
    setq(qlo,q,MPFR_RNDD); setq(qhi,q,MPFR_RNDU);
    mpfr_log(lgu.v,qhi.v,MPFR_RNDU); mpfr_neg(lo.v,lgu.v,MPFR_RNDD);
    mpfr_log(lgd.v,qlo.v,MPFR_RNDD); mpfr_neg(hi.v,lgd.v,MPFR_RNDU);
}
static void entropy_bounds(const mpq_class&q,MP&lo,MP&hi){
    if(q==0 || q==1){ mpfr_set_ui(lo.v,0,MPFR_RNDN); mpfr_set_ui(hi.v,0,MPFR_RNDN); return; }
    assert(q>0 && q<1);
    mpq_class r=1-q;
    MP qlo,qhi,rlo,rhi,nlqlo,nlqhi,nlrlo,nlrhi,t1lo,t1hi,t2lo,t2hi;
    setq(qlo,q,MPFR_RNDD); setq(qhi,q,MPFR_RNDU);
    setq(rlo,r,MPFR_RNDD); setq(rhi,r,MPFR_RNDU);
    neglog_bounds(q,nlqlo,nlqhi); neglog_bounds(r,nlrlo,nlrhi);
    mpfr_mul(t1lo.v,qlo.v,nlqlo.v,MPFR_RNDD); mpfr_mul(t1hi.v,qhi.v,nlqhi.v,MPFR_RNDU);
    mpfr_mul(t2lo.v,rlo.v,nlrlo.v,MPFR_RNDD); mpfr_mul(t2hi.v,rhi.v,nlrhi.v,MPFR_RNDU);
    mpfr_add(lo.v,t1lo.v,t2lo.v,MPFR_RNDD); mpfr_add(hi.v,t1hi.v,t2hi.v,MPFR_RNDU);
}
static void ln_integer_bounds(unsigned long a,MP&lo,MP&hi){
    MP x; mpfr_set_ui(x.v,a,MPFR_RNDN);
    mpfr_log(lo.v,x.v,MPFR_RNDD); mpfr_log(hi.v,x.v,MPFR_RNDU);
}

using Poly=std::array<mpq_class,6>;
struct Group{ Poly p; int mult; };

static Poly qpoly(uint32_t mask,int y){
    int c[6]={0,0,0,0,0,0};
    for(int x=0;x<N;x++) if((mask>>x)&1u) c[__builtin_popcount((unsigned)(x^y))]++;
    Poly p;
    for(int d=0;d<=DEG;d++) p[d]=Q(c[d],BINOM[d]);
    return p;
}
static std::string pkey(const Poly&p){
    std::ostringstream os;
    for(int i=0;i<=DEG;i++) os<<p[i].get_num()<<'/'<<p[i].get_den()<<';';
    return os.str();
}
static std::pair<Poly,Poly> subdivide(const Poly&c,const mpq_class&t){
    mpq_class row[6][6];
    for(int i=0;i<=DEG;i++) row[0][i]=c[i];
    for(int r=1;r<=DEG;r++) for(int i=0;i<=DEG-r;i++) row[r][i]=(1-t)*row[r-1][i]+t*row[r-1][i+1];
    Poly L,R;
    for(int i=0;i<=DEG;i++){ L[i]=row[i][0]; R[i]=row[DEG-i][i]; }
    return {L,R};
}
static Poly restrict_poly(const Poly&c,const mpq_class&a,const mpq_class&b){
    assert(0<=a && a<=b && b<=1);
    Poly left=c;
    if(b!=1) left=subdivide(c,b).first;
    if(a==0) return left;
    return subdivide(left,a/b).second;
}
static mpq_class eval_poly(const Poly&c,const mpq_class&a){
    std::vector<mpq_class> cur(c.begin(),c.end());
    while(cur.size()>1){
        std::vector<mpq_class> nxt;
        for(size_t i=0;i+1<cur.size();i++) nxt.push_back((1-a)*cur[i]+a*cur[i+1]);
        cur.swap(nxt);
    }
    return cur[0];
}
static void entropy_min_endpoint(const mpq_class&loq,const mpq_class&hiq,MP&hlo,MP&hhi){
    mpq_class dlo=abs(2*loq-1),dhi=abs(2*hiq-1);
    entropy_bounds(dlo>=dhi?loq:hiq,hlo,hhi);
}

static bool direct_compressed(uint32_t m){
    for(int i=0;i<NV;i++){
        for(int base=0;base<N;base++) if(((base>>i)&1)==0){
            int a=(m>>base)&1u;
            int b=(m>>(base|(1<<i)))&1u;
            if(a<b) return false;
        }
    }
    for(int i=0;i<NV;i++) for(int j=i+1;j<NV;j++){
        for(int base=0;base<N;base++) if(((base>>i)&1)==0 && ((base>>j)&1)==0){
            int q[4]={base,base|(1<<j),base|(1<<i),base|(1<<i)|(1<<j)};
            int prev=1;
            for(int k=0;k<4;k++){
                int z=(m>>q[k])&1u;
                if(z>prev) return false;
                prev=z;
            }
        }
    }
    return true;
}

static std::vector<uint32_t> enumerate_compressed(){
    std::array<uint32_t,N> succ{},pred{};
    for(int i=0;i<NV;i++) for(int base=0;base<N;base++) if(((base>>i)&1)==0){
        int u=base,v=base|(1<<i);
        succ[u]|=(1u<<v); pred[v]|=(1u<<u);
    }
    for(int i=0;i<NV;i++) for(int j=i+1;j<NV;j++){
        for(int base=0;base<N;base++) if(((base>>i)&1)==0 && ((base>>j)&1)==0){
            int u=base|(1<<j),v=base|(1<<i);
            succ[u]|=(1u<<v); pred[v]|=(1u<<u);
        }
    }
    for(int k=0;k<N;k++){
        uint32_t bk=(1u<<k);
        for(int i=0;i<N;i++) if(succ[i]&bk) succ[i]|=succ[k];
    }
    pred.fill(0);
    for(int u=0;u<N;u++){
        uint32_t x=succ[u];
        while(x){ uint32_t l=x&(~x+1u); int v=__builtin_ctz(x); x-=l; pred[v]|=(1u<<u); }
    }
    std::array<uint32_t,N> pm{},sm{};
    for(int v=0;v<N;v++){ pm[v]=pred[v]|(1u<<v); sm[v]=succ[v]|(1u<<v); }
    std::vector<uint32_t> out;
    std::function<void(uint32_t,uint32_t)> rec=[&](uint32_t inc,uint32_t exc){
        uint32_t undec=FULL & ~(inc|exc);
        if(undec==0){ out.push_back(inc); return; }
        int best=-1,score=-1;
        uint32_t x=undec;
        while(x){
            int v=__builtin_ctz(x); x&=x-1;
            int sc=__builtin_popcount(pm[v]&undec)+__builtin_popcount(sm[v]&undec);
            if(sc>score){score=sc;best=v;}
        }
        if((pm[best]&exc)==0) rec(inc|pm[best],exc);
        if((sm[best]&inc)==0) rec(inc,exc|sm[best]);
    };
    rec(0,0);
    std::sort(out.begin(),out.end());
    out.erase(std::unique(out.begin(),out.end()),out.end());
    for(uint32_t m:out) assert(direct_compressed(m));
    return out;
}

static bool is_constant(uint32_t m){ return m==0u || m==FULL; }
static bool is_dictator(uint32_t m){
    for(int i=0;i<NV;i++){
        bool ok0=true,ok1=true;
        for(int x=0;x<N;x++){
            int v=(m>>x)&1u,xi=(x>>i)&1;
            if(v!=xi) ok1=false;
            if(v!=(1-xi)) ok0=false;
        }
        if(ok0||ok1) return true;
    }
    return false;
}
static std::array<mpq_class,N> walsh_pm(uint32_t mask){
    std::array<mpq_class,N> c;
    for(int S=0;S<N;S++){
        long s=0;
        for(int x=0;x<N;x++){
            int v=((mask>>x)&1u)?-1:1;
            int chi=(__builtin_popcount((unsigned)(x&S))&1)?-1:1;
            s+=v*chi;
        }
        c[S]=Q(s,N);
    }
    return c;
}
static mpq_class avg_sensitivity(uint32_t m){
    long s=0;
    for(int x=0;x<N;x++) for(int i=0;i<NV;i++) s += (((m>>x)&1u)!=((m>>(x^(1<<i)))&1u));
    return Q(s,N);
}

static std::vector<Group> groups_for(uint32_t m){
    std::map<std::string,std::pair<Poly,int>> tmp;
    for(int y=0;y<N;y++){
        Poly p=qpoly(m,y); std::string k=pkey(p);
        auto it=tmp.find(k);
        if(it==tmp.end()) tmp[k]={p,1}; else it->second.second++;
    }
    std::vector<Group> v;
    for(auto &kv:tmp) v.push_back({kv.second.first,kv.second.second});
    return v;
}

static void D_point(uint32_t mask,const mpq_class&a,const std::vector<Group>&groups,MP&dlo,MP&dhi,const MP&ln2lo,const MP&ln2hi){
    mpq_class p=Q(__builtin_popcount(mask),N);
    MP halo,hahi,hplo,hphi,sumlo,sumhi;
    entropy_bounds(a,halo,hahi); entropy_bounds(p,hplo,hphi);
    mpfr_set(dlo.v,ln2lo.v,MPFR_RNDD); mpfr_set(dhi.v,ln2hi.v,MPFR_RNDU);
    mpfr_sub(dlo.v,dlo.v,hahi.v,MPFR_RNDD); mpfr_sub(dhi.v,dhi.v,halo.v,MPFR_RNDU);
    mpfr_sub(dlo.v,dlo.v,hphi.v,MPFR_RNDD); mpfr_sub(dhi.v,dhi.v,hplo.v,MPFR_RNDU);
    mpfr_set_ui(sumlo.v,0,MPFR_RNDN); mpfr_set_ui(sumhi.v,0,MPFR_RNDN);
    for(const auto&g:groups){
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

static void D_interval_lower(uint32_t mask,const mpq_class&a,const mpq_class&b,const std::vector<Group>&groups,MP&dlo,const MP&ln2lo){
    mpq_class p=Q(__builtin_popcount(mask),N);
    MP hbL,hbU,hpL,hpU,sumL;
    entropy_bounds(b,hbL,hbU); entropy_bounds(p,hpL,hpU);
    mpfr_set(dlo.v,ln2lo.v,MPFR_RNDD);
    mpfr_sub(dlo.v,dlo.v,hbU.v,MPFR_RNDD);
    mpfr_sub(dlo.v,dlo.v,hpU.v,MPFR_RNDD);
    mpfr_set_ui(sumL.v,0,MPFR_RNDN);
    for(const auto&g:groups){
        Poly r=restrict_poly(g.p,a,b);
        mpq_class lo=r[0],hi=r[0];
        for(int i=1;i<=DEG;i++){ if(r[i]<lo)lo=r[i]; if(r[i]>hi)hi=r[i]; }
        MP hL,hU; entropy_min_endpoint(lo,hi,hL,hU);
        for(int k=0;k<g.mult;k++) mpfr_add(sumL.v,sumL.v,hL.v,MPFR_RNDD);
    }
    mpfr_div_ui(sumL.v,sumL.v,N,MPFR_RNDD);
    mpfr_add(dlo.v,dlo.v,sumL.v,MPFR_RNDD);
}

struct CertStats{
    long long leaves=0;
    int maxdepth=0;
    double minlower=1e100;
    uint32_t minmask=0;
    mpq_class mina,minb;
};
static bool certify_interval(uint32_t m,const std::vector<Group>&g,const mpq_class&a,const mpq_class&b,int depth,const MP&ln2lo,CertStats&st){
    MP lo; D_interval_lower(m,a,b,g,lo,ln2lo);
    if(mpfr_cmp_si(lo.v,0)>0){
        st.leaves++; st.maxdepth=std::max(st.maxdepth,depth);
        double d=getd(lo);
        if(d<st.minlower){st.minlower=d;st.minmask=m;st.mina=a;st.minb=b;}
        return true;
    }
    if(depth>=30) return false;
    mpq_class mid=(a+b)/2;
    return certify_interval(m,g,a,mid,depth+1,ln2lo,st) && certify_interval(m,g,mid,b,depth+1,ln2lo,st);
}

int main(){
    auto t0=std::chrono::steady_clock::now();
    auto cand=enumerate_compressed();
    std::cout<<"PROB20-21 N<=5 FULL-NOISE-INTERVAL CERTIFICATE\n";
    std::cout<<"model_runtime_metadata=UNVERIFIED\n";
    std::cout<<"source_defined_compressed_candidates="<<cand.size()<<"\n";
    assert(cand.size()==119);

    int constants=0,dicts=0,balanced_non=0,biased_non=0;
    std::vector<uint32_t> nontriv;
    std::map<uint32_t,std::vector<Group>> groups;
    for(uint32_t m:cand){
        if(is_constant(m)){constants++;continue;}
        if(is_dictator(m)){dicts++;continue;}
        nontriv.push_back(m);
        if(__builtin_popcount(m)==N/2) balanced_non++; else biased_non++;
        groups[m]=groups_for(m);
    }
    std::cout<<"constant_candidates="<<constants<<"\n";
    std::cout<<"dictator_candidates="<<dicts<<"\n";
    std::cout<<"nontrivial_candidates="<<nontriv.size()<<"\n";
    std::cout<<"balanced_nondictator_candidates="<<balanced_non<<"\n";
    std::cout<<"biased_nontrivial_candidates="<<biased_non<<"\n";

    MP ln2lo,ln2hi; ln_integer_bounds(2,ln2lo,ln2hi);

    mpq_class minAS; uint32_t minASMask=0; bool have=false;
    mpq_class minDelta; uint32_t minDeltaMask=0; bool haveD=false;
    for(uint32_t m:nontriv){
        if(__builtin_popcount(m)==N/2){
            mpq_class s=avg_sensitivity(m);
            if(!have || s<minAS){have=true;minAS=s;minASMask=m;}
        }
        auto c=walsh_pm(m);
        mpq_class mu=c[0],var=1-mu*mu,W1=0;
        for(int i=0;i<NV;i++) W1+=c[1<<i]*c[1<<i];
        mpq_class d=var-W1;
        assert(d>0);
        if(!haveD || d<minDelta){haveD=true;minDelta=d;minDeltaMask=m;}
    }
    assert(minAS==Q(11,8));
    assert(minDelta==Q(13,128));
    std::cout<<"min_balanced_nondictator_avg_sensitivity="<<minAS<<" mask="<<minASMask<<"\n";
    std::cout<<"min_Delta_var_minus_W1="<<minDelta<<" mask="<<minDeltaMask<<"\n";

    mpq_class A0=Q(1,8192),A1=Q(63,128),rho0=Q(1,64);
    std::cout<<"full_alpha_interval=[0,1/2]\n";
    std::cout<<"low_noise=[0,1/8192]\n";
    std::cout<<"middle=[1/8192,63/128]\n";
    std::cout<<"high_noise=[63/128,1/2]\n";

    MP hA0L,hA0U,h15L,h15U,biasGap;
    entropy_bounds(A0,hA0L,hA0U); entropy_bounds(Q(15,32),h15L,h15U);
    mpfr_set(biasGap.v,ln2lo.v,MPFR_RNDD);
    mpfr_sub(biasGap.v,biasGap.v,hA0U.v,MPFR_RNDD);
    mpfr_sub(biasGap.v,biasGap.v,h15U.v,MPFR_RNDD);
    assert(mpfr_cmp_si(biasGap.v,0)>0);
    std::cout<<std::setprecision(17)<<"biased_low_noise_lower_gap_nat="<<getd(biasGap)<<"\n";

    mpq_class c0=Q(8191,8192); c0=c0*c0*c0*c0;
    MP ln8192L,ln8192U,ln5L,ln5U,coefLo,term1,term2,balMargin;
    ln_integer_bounds(8192,ln8192L,ln8192U); ln_integer_bounds(5,ln5L,ln5U);
    mpq_class coef=Q(11,8)*c0-1;
    setq(coefLo,coef,MPFR_RNDD);
    mpfr_mul(term1.v,coefLo.v,ln8192L.v,MPFR_RNDD);
    MP sbar; setq(sbar,Q(11,8),MPFR_RNDU);
    mpfr_mul(term2.v,sbar.v,ln5U.v,MPFR_RNDU);
    mpfr_sub(balMargin.v,term1.v,term2.v,MPFR_RNDD);
    MP one; mpfr_set_ui(one.v,1,MPFR_RNDN);
    mpfr_sub(balMargin.v,balMargin.v,one.v,MPFR_RNDD);
    assert(mpfr_cmp_si(balMargin.v,0)>0);
    std::cout<<"balanced_low_noise_uniform_margin_over_alpha="<<getd(balMargin)<<"\n";

    mpq_class highGap=(1-rho0*rho0)*Q(13,128)-rho0*Q(45,8)-31*rho0*rho0;
    assert(highGap==Q(3187,524288) && highGap>0);
    std::cout<<"high_noise_rational_margin="<<highGap<<"\n";

    long neg=0; double minGrid=1e100; uint32_t minGridMask=0; mpq_class minGridA;
    for(uint32_t m:nontriv){
        auto &gg=groups[m];
        for(int j=0;j<=128;j++){
            mpq_class a=Q(j,256);
            MP lo,hi; D_point(m,a,gg,lo,hi,ln2lo,ln2hi);
            if(mpfr_cmp_si(hi.v,0)<0) neg++;
            if(j>0 && j<128){
                double d=getd(lo);
                if(d<minGrid){minGrid=d;minGridMask=m;minGridA=a;}
            }
        }
    }
    assert(neg==0);
    std::cout<<"counterexample_grid_alpha=j/256,j=0..128\n";
    std::cout<<"counterexample_grid_certified_negative="<<neg<<"\n";
    std::cout<<"grid_smallest_interior_lower_D_nat="<<minGrid<<" mask="<<minGridMask<<" alpha="<<minGridA<<"\n";

    CertStats st;
    for(uint32_t m:nontriv){
        bool ok=certify_interval(m,groups[m],A0,A1,0,ln2lo,st);
        if(!ok){
            std::cerr<<"FAILED middle certification mask="<<m<<"\n";
            return 2;
        }
    }
    std::cout<<"middle_leaf_intervals="<<st.leaves<<"\n";
    std::cout<<"middle_max_bisection_depth="<<st.maxdepth<<"\n";
    std::cout<<"middle_min_outward_lower_D_nat="<<st.minlower<<" mask="<<st.minmask<<" a="<<st.mina<<" b="<<st.minb<<"\n";
    std::cout<<"log_engine=MPFR_shared_library_directed_rounding_256_bits_exact_rational_inputs\n";

    auto t1=std::chrono::steady_clock::now();
    double secs=std::chrono::duration<double>(t1-t0).count();
    std::cout<<"checker_runtime_seconds="<<secs<<"\n";
    std::cout<<"RESULT=PASS\n";
    return 0;
}
