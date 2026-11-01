#include <gmp.h>
#include <gmpxx.h>
#include <algorithm>
#include <array>
#include <atomic>
#include <cassert>
#include <chrono>
#include <cmath>
#include <cstdint>
#include <functional>
#include <iomanip>
#include <iostream>
#include <map>
#include <mutex>
#include <numeric>
#include <sstream>
#include <string>
#include <vector>
#ifdef _OPENMP
#include <omp.h>
#endif

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
int mpfr_set(mpfr_ptr, mpfr_srcptr, mpfr_rnd_t);
int mpfr_log(mpfr_ptr, mpfr_srcptr, mpfr_rnd_t);
int mpfr_neg(mpfr_ptr, mpfr_srcptr, mpfr_rnd_t);
int mpfr_add(mpfr_ptr, mpfr_srcptr, mpfr_srcptr, mpfr_rnd_t);
int mpfr_sub(mpfr_ptr, mpfr_srcptr, mpfr_srcptr, mpfr_rnd_t);
int mpfr_mul(mpfr_ptr, mpfr_srcptr, mpfr_srcptr, mpfr_rnd_t);
int mpfr_div_ui(mpfr_ptr, mpfr_srcptr, unsigned long, mpfr_rnd_t);
int mpfr_cmp_si(mpfr_srcptr, long);
double mpfr_get_d(mpfr_srcptr, mpfr_rnd_t);
}

static constexpr int NV=6;
static constexpr int N=64;
static constexpr uint64_t FULL=~uint64_t(0);
static constexpr mpfr_prec_t PREC=192;
static constexpr int DEG=6;
static const int BINOM[7]={1,6,15,20,15,6,1};
static mpq_class Q(long n,long d=1){ mpq_class q(n,d); q.canonicalize(); return q; }

struct MP { mpfr_t v; MP(){mpfr_init2(v,PREC);mpfr_set_ui(v,0,MPFR_RNDN);} ~MP(){mpfr_clear(v);} MP(const MP&)=delete; MP& operator=(const MP&)=delete; };
static void setq(MP&x,const mpq_class&q,mpfr_rnd_t r){mpfr_set_q(x.v,q.get_mpq_t(),r);} 
static double getd(const MP&x){return mpfr_get_d(x.v,MPFR_RNDN);} 
static void neglog_bounds(const mpq_class&q,MP&lo,MP&hi){MP qlo,qhi,lgu,lgd;setq(qlo,q,MPFR_RNDD);setq(qhi,q,MPFR_RNDU);mpfr_log(lgu.v,qhi.v,MPFR_RNDU);mpfr_neg(lo.v,lgu.v,MPFR_RNDD);mpfr_log(lgd.v,qlo.v,MPFR_RNDD);mpfr_neg(hi.v,lgd.v,MPFR_RNDU);} 
static void entropy_bounds(const mpq_class&q,MP&lo,MP&hi){
    if(q==0||q==1){mpfr_set_ui(lo.v,0,MPFR_RNDN);mpfr_set_ui(hi.v,0,MPFR_RNDN);return;}
    assert(q>0&&q<1);mpq_class r=1-q;MP qlo,qhi,rlo,rhi,nlqlo,nlqhi,nlrlo,nlrhi,t1lo,t1hi,t2lo,t2hi;
    setq(qlo,q,MPFR_RNDD);setq(qhi,q,MPFR_RNDU);setq(rlo,r,MPFR_RNDD);setq(rhi,r,MPFR_RNDU);
    neglog_bounds(q,nlqlo,nlqhi);neglog_bounds(r,nlrlo,nlrhi);
    mpfr_mul(t1lo.v,qlo.v,nlqlo.v,MPFR_RNDD);mpfr_mul(t1hi.v,qhi.v,nlqhi.v,MPFR_RNDU);
    mpfr_mul(t2lo.v,rlo.v,nlrlo.v,MPFR_RNDD);mpfr_mul(t2hi.v,rhi.v,nlrhi.v,MPFR_RNDU);
    mpfr_add(lo.v,t1lo.v,t2lo.v,MPFR_RNDD);mpfr_add(hi.v,t1hi.v,t2hi.v,MPFR_RNDU);
}
static void ln_integer_bounds(unsigned long a,MP&lo,MP&hi){MP x;mpfr_set_ui(x.v,a,MPFR_RNDN);mpfr_log(lo.v,x.v,MPFR_RNDD);mpfr_log(hi.v,x.v,MPFR_RNDU);} 

using Poly=std::array<mpq_class,7>;
struct Group{Poly p;int mult;};
static Poly qpoly(uint64_t mask,int y){int c[7]={};for(int x=0;x<N;x++)if((mask>>x)&1ull)c[__builtin_popcountll((unsigned)(x^y))]++;Poly p;for(int d=0;d<=DEG;d++)p[d]=Q(c[d],BINOM[d]);return p;}
static std::string pkey(const Poly&p){std::ostringstream os;for(int i=0;i<=DEG;i++)os<<p[i].get_num()<<'/'<<p[i].get_den()<<';';return os.str();}
static std::pair<Poly,Poly> subdivide(const Poly&c,const mpq_class&t){mpq_class row[7][7];for(int i=0;i<=DEG;i++)row[0][i]=c[i];for(int r=1;r<=DEG;r++)for(int i=0;i<=DEG-r;i++)row[r][i]=(1-t)*row[r-1][i]+t*row[r-1][i+1];Poly L,R;for(int i=0;i<=DEG;i++){L[i]=row[i][0];R[i]=row[DEG-i][i];}return {L,R};}
static Poly restrict_poly(const Poly&c,const mpq_class&a,const mpq_class&b){Poly left=c;if(b!=1)left=subdivide(c,b).first;if(a==0)return left;return subdivide(left,a/b).second;}
static mpq_class eval_poly(const Poly&c,const mpq_class&a){std::array<mpq_class,7> cur=c;int len=7;while(len>1){for(int i=0;i<len-1;i++)cur[i]=(1-a)*cur[i]+a*cur[i+1];len--;}return cur[0];}
static void entropy_min_endpoint(const mpq_class&loq,const mpq_class&hiq,MP&hlo,MP&hhi){mpq_class dlo=abs(2*loq-1),dhi=abs(2*hiq-1);entropy_bounds(dlo>=dhi?loq:hiq,hlo,hhi);} 

static bool direct_compressed(uint64_t m){
    for(int i=0;i<NV;i++)for(int base=0;base<N;base++)if(((base>>i)&1)==0){int a=(m>>base)&1ull,b=(m>>(base|(1<<i)))&1ull;if(a<b)return false;}
    for(int i=0;i<NV;i++)for(int j=i+1;j<NV;j++)for(int base=0;base<N;base++)if(((base>>i)&1)==0&&((base>>j)&1)==0){int q[4]={base,base|(1<<j),base|(1<<i),base|(1<<i)|(1<<j)};int prev=1;for(int k=0;k<4;k++){int z=(m>>q[k])&1ull;if(z>prev)return false;prev=z;}}
    return true;
}
static std::vector<uint64_t> enumerate_compressed(){
    std::array<uint64_t,N> succ{},pred{};
    for(int i=0;i<NV;i++)for(int base=0;base<N;base++)if(((base>>i)&1)==0){int u=base,v=base|(1<<i);succ[u]|=1ull<<v;}
    for(int i=0;i<NV;i++)for(int j=i+1;j<NV;j++)for(int base=0;base<N;base++)if(((base>>i)&1)==0&&((base>>j)&1)==0){int u=base|(1<<j),v=base|(1<<i);succ[u]|=1ull<<v;}
    for(int k=0;k<N;k++){uint64_t bk=1ull<<k;for(int i=0;i<N;i++)if(succ[i]&bk)succ[i]|=succ[k];}
    for(int u=0;u<N;u++){uint64_t x=succ[u];while(x){int v=__builtin_ctzll(x);x&=x-1;pred[v]|=1ull<<u;}}
    std::array<uint64_t,N> pm{},sm{};for(int v=0;v<N;v++){pm[v]=pred[v]|(1ull<<v);sm[v]=succ[v]|(1ull<<v);} 
    std::vector<uint64_t> out;std::function<void(uint64_t,uint64_t)> rec=[&](uint64_t inc,uint64_t exc){uint64_t undec=FULL&~(inc|exc);if(!undec){out.push_back(inc);return;}int best=-1,score=-1;uint64_t x=undec;while(x){int v=__builtin_ctzll(x);x&=x-1;int sc=__builtin_popcountll(pm[v]&undec)+__builtin_popcountll(sm[v]&undec);if(sc>score){score=sc;best=v;}}if((pm[best]&exc)==0)rec(inc|pm[best],exc);if((sm[best]&inc)==0)rec(inc,exc|sm[best]);};
    rec(0,0);std::sort(out.begin(),out.end());out.erase(std::unique(out.begin(),out.end()),out.end());for(auto m:out)assert(direct_compressed(m));return out;
}
static bool is_constant(uint64_t m){return m==0u||m==FULL;}
static bool is_dictator(uint64_t m){for(int i=0;i<NV;i++){bool ok0=true,ok1=true;for(int x=0;x<N;x++){int v=(m>>x)&1ull,xi=(x>>i)&1;if(v!=xi)ok1=false;if(v!=(1-xi))ok0=false;}if(ok0||ok1)return true;}return false;}
static std::array<mpq_class,N> walsh_pm(uint64_t mask){std::array<mpq_class,N> c;for(int S=0;S<N;S++){long s=0;for(int x=0;x<N;x++){int v=((mask>>x)&1ull)?-1:1;int chi=(__builtin_popcountll((unsigned)(x&S))&1)?-1:1;s+=v*chi;}c[S]=Q(s,N);}return c;}
static mpq_class avg_sensitivity(uint64_t m){long s=0;for(int x=0;x<N;x++)for(int i=0;i<NV;i++)s+=(((m>>x)&1ull)!=((m>>(x^(1<<i)))&1ull));return Q(s,N);}
static std::vector<Group> groups_for(uint64_t m){
    using Count=std::array<unsigned char,7>;
    std::map<Count,int> tmp;
    for(int y=0;y<N;y++){
        Count c{};
        uint64_t z=m;
        while(z){ int x=__builtin_ctzll(z); z&=z-1; c[__builtin_popcountll((unsigned long long)(x^y))]++; }
        tmp[c]++;
    }
    std::vector<Group> v; v.reserve(tmp.size());
    for(auto &kv:tmp){ Poly p; for(int d=0;d<=DEG;d++) p[d]=Q(kv.first[d],BINOM[d]); v.push_back({p,kv.second}); }
    return v;
}

static void D_point(uint64_t mask,const mpq_class&a,const std::vector<Group>&groups,MP&dlo,MP&dhi,const MP&ln2lo,const MP&ln2hi){mpq_class p=Q(__builtin_popcountll(mask),N);MP halo,hahi,hplo,hphi,sumlo,sumhi;entropy_bounds(a,halo,hahi);entropy_bounds(p,hplo,hphi);mpfr_set(dlo.v,ln2lo.v,MPFR_RNDD);mpfr_set(dhi.v,ln2hi.v,MPFR_RNDU);mpfr_sub(dlo.v,dlo.v,hahi.v,MPFR_RNDD);mpfr_sub(dhi.v,dhi.v,halo.v,MPFR_RNDU);mpfr_sub(dlo.v,dlo.v,hphi.v,MPFR_RNDD);mpfr_sub(dhi.v,dhi.v,hplo.v,MPFR_RNDU);mpfr_set_ui(sumlo.v,0,MPFR_RNDN);mpfr_set_ui(sumhi.v,0,MPFR_RNDN);for(const auto&g:groups){mpq_class q=eval_poly(g.p,a);MP qlo,qhi;entropy_bounds(q,qlo,qhi);for(int k=0;k<g.mult;k++){mpfr_add(sumlo.v,sumlo.v,qlo.v,MPFR_RNDD);mpfr_add(sumhi.v,sumhi.v,qhi.v,MPFR_RNDU);}}mpfr_div_ui(sumlo.v,sumlo.v,N,MPFR_RNDD);mpfr_div_ui(sumhi.v,sumhi.v,N,MPFR_RNDU);mpfr_add(dlo.v,dlo.v,sumlo.v,MPFR_RNDD);mpfr_add(dhi.v,dhi.v,sumhi.v,MPFR_RNDU);} 

struct NodeGroup{Poly p;int mult;};
struct LocalStats{long long nodes=0,leaves=0;int maxdepth=0;double minlower=1e100;uint64_t minmask=0;mpq_class mina,minb;bool ok=true;};
static bool interval_lower(uint64_t mask,const mpq_class&b,const std::vector<NodeGroup>&gs,const MP&ln2lo,const MP&hpU,double &out){
    MP hbL,hbU,sumL,dlo; entropy_bounds(b,hbL,hbU);mpfr_set(dlo.v,ln2lo.v,MPFR_RNDD);mpfr_sub(dlo.v,dlo.v,hbU.v,MPFR_RNDD);mpfr_sub(dlo.v,dlo.v,hpU.v,MPFR_RNDD);mpfr_set_ui(sumL.v,0,MPFR_RNDN);
    for(const auto&g:gs){mpq_class lo=g.p[0],hi=g.p[0];for(int i=1;i<=DEG;i++){if(g.p[i]<lo)lo=g.p[i];if(g.p[i]>hi)hi=g.p[i];}MP hL,hU;entropy_min_endpoint(lo,hi,hL,hU);for(int k=0;k<g.mult;k++)mpfr_add(sumL.v,sumL.v,hL.v,MPFR_RNDD);}mpfr_div_ui(sumL.v,sumL.v,N,MPFR_RNDD);mpfr_add(dlo.v,dlo.v,sumL.v,MPFR_RNDD);out=getd(dlo);return mpfr_cmp_si(dlo.v,0)>0;
}
static void split_half(const std::vector<NodeGroup>&gs,std::vector<NodeGroup>&L,std::vector<NodeGroup>&R){L.clear();R.clear();L.reserve(gs.size());R.reserve(gs.size());mpq_class half=Q(1,2);for(const auto&g:gs){auto lr=subdivide(g.p,half);L.push_back({std::move(lr.first),g.mult});R.push_back({std::move(lr.second),g.mult});}}
static bool certify_rec(uint64_t mask,const mpq_class&a,const mpq_class&b,const std::vector<NodeGroup>&gs,int depth,const MP&ln2lo,const MP&hpU,LocalStats&st){
    st.nodes++;double val; if(interval_lower(mask,b,gs,ln2lo,hpU,val)){st.leaves++;st.maxdepth=std::max(st.maxdepth,depth);if(val<st.minlower){st.minlower=val;st.minmask=mask;st.mina=a;st.minb=b;}return true;}
    if(depth>=28)return false;mpq_class mid=(a+b)/2;std::vector<NodeGroup>L,R;split_half(gs,L,R);if(!certify_rec(mask,a,mid,L,depth+1,ln2lo,hpU,st))return false;return certify_rec(mask,mid,b,R,depth+1,ln2lo,hpU,st);
}
static LocalStats certify_candidate(uint64_t mask,const std::vector<Group>&orig,const mpq_class&A0,const mpq_class&A1,const MP&ln2lo){
    LocalStats st;std::vector<NodeGroup> root;root.reserve(orig.size());for(const auto&g:orig)root.push_back({restrict_poly(g.p,A0,A1),g.mult});mpq_class p=Q(__builtin_popcountll(mask),N);MP hpL,hpU;entropy_bounds(p,hpL,hpU);st.ok=certify_rec(mask,A0,A1,root,0,ln2lo,hpU,st);return st;
}

int main(int argc,char**argv){
    auto t0=std::chrono::steady_clock::now();auto cand=enumerate_compressed();assert(cand.size()==1173);std::vector<uint64_t> non;int constants=0,dicts=0,bal=0,bias=0;for(auto m:cand){if(is_constant(m)){constants++;continue;}if(is_dictator(m)){dicts++;continue;}non.push_back(m);if(__builtin_popcountll(m)==32)bal++;else bias++;}
    std::cout<<"PROB20-21 N<=6 FAST FULL-NOISE-INTERVAL CERTIFICATE\n";std::cout<<"source_defined_compressed_candidates="<<cand.size()<<" constants="<<constants<<" dictators="<<dicts<<" nontrivial="<<non.size()<<" balanced_nontrivial="<<bal<<" biased_nontrivial="<<bias<<"\n";
    MP ln2lo,ln2hi;ln_integer_bounds(2,ln2lo,ln2hi);
    mpq_class minAS;uint64_t minASMask=0;bool haveAS=false;mpq_class minDelta;uint64_t minDeltaMask=0;bool haveD=false;
    for(auto m:non){if(__builtin_popcountll(m)==32){auto s=avg_sensitivity(m);if(!haveAS||s<minAS){haveAS=true;minAS=s;minASMask=m;}}auto c=walsh_pm(m);mpq_class mu=c[0],V=1-mu*mu,W1=0;for(int i=0;i<NV;i++)W1+=c[1ull<<i]*c[1ull<<i];mpq_class d=V-W1;if(!haveD||d<minDelta){haveD=true;minDelta=d;minDeltaMask=m;}}
    assert(minAS==Q(5,4));assert(minDelta==Q(57,1024));std::cout<<"min_balanced_avg_sensitivity="<<minAS<<" mask="<<minASMask<<" min_Delta="<<minDelta<<" mask="<<minDeltaMask<<"\n";
    mpq_class A0=Q(1,524288),A1=Q(69,140),rho0=Q(1,70);
    MP hA0L,hA0U,hPL,hPU,biasGap;entropy_bounds(A0,hA0L,hA0U);entropy_bounds(Q(31,64),hPL,hPU);mpfr_set(biasGap.v,ln2lo.v,MPFR_RNDD);mpfr_sub(biasGap.v,biasGap.v,hA0U.v,MPFR_RNDD);mpfr_sub(biasGap.v,biasGap.v,hPU.v,MPFR_RNDD);assert(mpfr_cmp_si(biasGap.v,0)>0);std::cout<<std::setprecision(17)<<"biased_low_noise_lower_gap_nat="<<getd(biasGap)<<"\n";
    mpq_class c0=Q(1);for(int k=0;k<5;k++)c0*=Q(524287,524288);
    MP lnAL,lnAU,ln6L,ln6U,coefLo,term1,term2,balMargin;ln_integer_bounds(524288,lnAL,lnAU);ln_integer_bounds(6,ln6L,ln6U);mpq_class coef=Q(5,4)*c0-1;setq(coefLo,coef,MPFR_RNDD);mpfr_mul(term1.v,coefLo.v,lnAL.v,MPFR_RNDD);MP sbar;setq(sbar,Q(5,4),MPFR_RNDU);mpfr_mul(term2.v,sbar.v,ln6U.v,MPFR_RNDU);mpfr_sub(balMargin.v,term1.v,term2.v,MPFR_RNDD);MP one;mpfr_set_ui(one.v,1,MPFR_RNDN);mpfr_sub(balMargin.v,balMargin.v,one.v,MPFR_RNDD);assert(mpfr_cmp_si(balMargin.v,0)>0);std::cout<<"balanced_low_noise_margin_over_alpha="<<getd(balMargin)<<"\n";
    mpq_class minSq;uint64_t minSqMask=0;bool haveSq=false;mpq_class minL;uint64_t minLMask=0;bool haveL=false;
    for(auto m:non){auto c=walsh_pm(m);mpq_class mu=abs(c[0]),V=1-mu*mu,W1=0;for(int i=0;i<NV;i++)W1+=c[1ull<<i]*c[1ull<<i];mpq_class d=V-W1;mpq_class L=(1-rho0*rho0)*d-Q(63)*rho0*rho0*V;mpq_class sq=L*L-Q(4)*mu*mu*rho0*rho0*Q(63)*V;assert(L>0&&sq>0);if(!haveSq||sq<minSq){haveSq=true;minSq=sq;minSqMask=m;}if(!haveL||L<minL){haveL=true;minL=L;minLMask=m;}}
    std::cout<<"high_noise_rho0=1/70 min_L="<<minL<<" mask="<<minLMask<<" min_square_margin="<<minSq<<" mask="<<minSqMask<<"\n";
    std::vector<std::vector<Group>> allg(non.size());
    for(size_t i=0;i<non.size();i++) allg[i]=groups_for(non[i]);
    long long istart=0,iend=(long long)non.size(); if(argc>=2) istart=std::stoll(argv[1]); if(argc>=3) iend=std::stoll(argv[2]);
    if(istart<0)istart=0; if(iend>(long long)non.size())iend=non.size(); assert(istart<=iend);
    std::cout<<"batch_start="<<istart<<" batch_end="<<iend<<" batch_count="<<(iend-istart)<<"\n";
    std::vector<LocalStats> stats(iend-istart);std::atomic<int> failed{0};
    #pragma omp parallel for schedule(dynamic,1)
    for(long long i=istart;i<iend;i++){auto st=certify_candidate(non[i],allg[i],A0,A1,ln2lo);stats[i-istart]=std::move(st);if(!stats[i-istart].ok)failed.fetch_add(1);}
    long long nodes=0,leaves=0;int maxdepth=0;double minlower=1e100;uint64_t minmask=0;mpq_class mina,minb;for(auto &ss:stats){nodes+=ss.nodes;leaves+=ss.leaves;maxdepth=std::max(maxdepth,ss.maxdepth);if(ss.minlower<minlower){minlower=ss.minlower;minmask=ss.minmask;mina=ss.mina;minb=ss.minb;}}
    std::cout<<"middle=[1/524288,69/140] failed_candidates="<<failed.load()<<" nodes="<<nodes<<" leaves="<<leaves<<" maxdepth="<<maxdepth<<" min_interval_lower_nat="<<minlower<<" mask="<<minmask<<" a="<<mina<<" b="<<minb<<"\n";
    if(failed.load()!=0) return 2;
    auto t1=std::chrono::steady_clock::now();std::cout<<"wall_seconds="<<std::chrono::duration<double>(t1-t0).count()<<"\n";if(failed.load()){std::cout<<"RESULT=BATCH_FAIL\n";return 2;}std::cout<<"RESULT=BATCH_PASS\n";return 0;
}
