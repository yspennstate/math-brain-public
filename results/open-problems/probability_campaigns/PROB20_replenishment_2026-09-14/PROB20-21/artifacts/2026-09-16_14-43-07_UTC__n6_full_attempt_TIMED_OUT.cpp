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

static constexpr int NV=6;
static constexpr int N=64;
static constexpr uint64_t FULL=~uint64_t(0);
static constexpr mpfr_prec_t PREC=256;
static constexpr int DEG=6;
static const int BINOM[7]={1,6,15,20,15,6,1};

static mpq_class Q(long n,long d=1){ mpq_class q(n,d); q.canonicalize(); return q; }

struct MP { mpfr_t v; MP(){ mpfr_init2(v,PREC); mpfr_set_ui(v,0,MPFR_RNDN); } ~MP(){ mpfr_clear(v); } MP(const MP&)=delete; MP& operator=(const MP&)=delete; };
static void setq(MP& x,const mpq_class&q,mpfr_rnd_t r){ mpfr_set_q(x.v,q.get_mpq_t(),r); }
static double getd(const MP&x){ return mpfr_get_d(x.v,MPFR_RNDN); }
static void neglog_bounds(const mpq_class&q,MP&lo,MP&hi){ MP qlo,qhi,lgu,lgd; setq(qlo,q,MPFR_RNDD); setq(qhi,q,MPFR_RNDU); mpfr_log(lgu.v,qhi.v,MPFR_RNDU); mpfr_neg(lo.v,lgu.v,MPFR_RNDD); mpfr_log(lgd.v,qlo.v,MPFR_RNDD); mpfr_neg(hi.v,lgd.v,MPFR_RNDU); }
static void entropy_bounds(const mpq_class&q,MP&lo,MP&hi){ if(q==0 || q==1){ mpfr_set_ui(lo.v,0,MPFR_RNDN); mpfr_set_ui(hi.v,0,MPFR_RNDN); return; } assert(q>0 && q<1); mpq_class r=1-q; MP qlo,qhi,rlo,rhi,nlqlo,nlqhi,nlrlo,nlrhi,t1lo,t1hi,t2lo,t2hi; setq(qlo,q,MPFR_RNDD); setq(qhi,q,MPFR_RNDU); setq(rlo,r,MPFR_RNDD); setq(rhi,r,MPFR_RNDU); neglog_bounds(q,nlqlo,nlqhi); neglog_bounds(r,nlrlo,nlrhi); mpfr_mul(t1lo.v,qlo.v,nlqlo.v,MPFR_RNDD); mpfr_mul(t1hi.v,qhi.v,nlqhi.v,MPFR_RNDU); mpfr_mul(t2lo.v,rlo.v,nlrlo.v,MPFR_RNDD); mpfr_mul(t2hi.v,rhi.v,nlrhi.v,MPFR_RNDU); mpfr_add(lo.v,t1lo.v,t2lo.v,MPFR_RNDD); mpfr_add(hi.v,t1hi.v,t2hi.v,MPFR_RNDU); }
static void ln_integer_bounds(unsigned long a,MP&lo,MP&hi){ MP x; mpfr_set_ui(x.v,a,MPFR_RNDN); mpfr_log(lo.v,x.v,MPFR_RNDD); mpfr_log(hi.v,x.v,MPFR_RNDU); }

using Poly=std::array<mpq_class,7>; struct Group{ Poly p; int mult; };
static Poly qpoly(uint64_t mask,int y){ int c[7]={0,0,0,0,0,0,0}; for(int x=0;x<N;x++) if((mask>>x)&1ull) c[__builtin_popcountll((unsigned)(x^y))]++; Poly p; for(int d=0;d<=DEG;d++) p[d]=Q(c[d],BINOM[d]); return p; }
static std::string pkey(const Poly&p){ std::ostringstream os; for(int i=0;i<=DEG;i++) os<<p[i].get_num()<<'/'<<p[i].get_den()<<';'; return os.str(); }
static std::pair<Poly,Poly> subdivide(const Poly&c,const mpq_class&t){ mpq_class row[7][7]; for(int i=0;i<=DEG;i++) row[0][i]=c[i]; for(int r=1;r<=DEG;r++) for(int i=0;i<=DEG-r;i++) row[r][i]=(1-t)*row[r-1][i]+t*row[r-1][i+1]; Poly L,R; for(int i=0;i<=DEG;i++){ L[i]=row[i][0]; R[i]=row[DEG-i][i]; } return {L,R}; }
static Poly restrict_poly(const Poly&c,const mpq_class&a,const mpq_class&b){ assert(0<=a && a<=b && b<=1); Poly left=c; if(b!=1) left=subdivide(c,b).first; if(a==0) return left; return subdivide(left,a/b).second; }
static mpq_class eval_poly(const Poly&c,const mpq_class&a){ std::vector<mpq_class> cur(c.begin(),c.end()); while(cur.size()>1){ std::vector<mpq_class> nxt; for(size_t i=0;i+1<cur.size();i++) nxt.push_back((1-a)*cur[i]+a*cur[i+1]); cur.swap(nxt); } return cur[0]; }
static void entropy_min_endpoint(const mpq_class&loq,const mpq_class&hiq,MP&hlo,MP&hhi){ mpq_class dlo=abs(2*loq-1),dhi=abs(2*hiq-1); entropy_bounds(dlo>=dhi?loq:hiq,hlo,hhi); }

static bool direct_compressed(uint64_t m){ for(int i=0;i<NV;i++){ for(int base=0;base<N;base++) if(((base>>i)&1)==0){ int a=(m>>base)&1ull; int b=(m>>(base|(1<<i)))&1ull; if(a<b) return false; } } for(int i=0;i<NV;i++) for(int j=i+1;j<NV;j++){ for(int base=0;base<N;base++) if(((base>>i)&1)==0 && ((base>>j)&1)==0){ int q[4]={base,base|(1<<j),base|(1<<i),base|(1<<i)|(1<<j)}; int prev=1; for(int k=0;k<4;k++){ int z=(m>>q[k])&1ull; if(z>prev) return false; prev=z; } } } return true; }
static std::vector<uint64_t> enumerate_compressed(){ std::array<uint64_t,N> succ{},pred{}; for(int i=0;i<NV;i++) for(int base=0;base<N;base++) if(((base>>i)&1)==0){ int u=base,v=base|(1<<i); succ[u]|=(1ull<<v); pred[v]|=(1ull<<u); } for(int i=0;i<NV;i++) for(int j=i+1;j<NV;j++){ for(int base=0;base<N;base++) if(((base>>i)&1)==0 && ((base>>j)&1)==0){ int u=base|(1<<j),v=base|(1<<i); succ[u]|=(1ull<<v); pred[v]|=(1ull<<u); } } for(int k=0;k<N;k++){ uint64_t bk=(1ull<<k); for(int i=0;i<N;i++) if(succ[i]&bk) succ[i]|=succ[k]; } pred.fill(0); for(int u=0;u<N;u++){ uint64_t x=succ[u]; while(x){ uint64_t l=x&(~x+1u); int v=__builtin_ctzll(x); x-=l; pred[v]|=(1ull<<u); } } std::array<uint64_t,N> pm{},sm{}; for(int v=0;v<N;v++){ pm[v]=pred[v]|(1ull<<v); sm[v]=succ[v]|(1ull<<v); } std::vector<uint64_t> out; std::function<void(uint64_t,uint64_t)> rec=[&](uint64_t inc,uint64_t exc){ uint64_t undec=FULL & ~(inc|exc); if(undec==0){ out.push_back(inc); return; } int best=-1,score=-1; uint64_t x=undec; while(x){ int v=__builtin_ctzll(x); x&=x-1; int sc=__builtin_popcountll(pm[v]&undec)+__builtin_popcountll(sm[v]&undec); if(sc>score){score=sc;best=v;} } if((pm[best]&exc)==0) rec(inc|pm[best],exc); if((sm[best]&inc)==0) rec(inc,exc|sm[best]); }; rec(0,0); std::sort(out.begin(),out.end()); out.erase(std::unique(out.begin(),out.end()),out.end()); for(uint64_t m:out) assert(direct_compressed(m)); return out; }
static bool is_constant(uint64_t m){ return m==0u || m==FULL; }
static bool is_dictator(uint64_t m){ for(int i=0;i<NV;i++){ bool ok0=true,ok1=true; for(int x=0;x<N;x++){ int v=(m>>x)&1ull,xi=(x>>i)&1; if(v!=xi) ok1=false; if(v!=(1-xi)) ok0=false; } if(ok0||ok1) return true; } return false; }
static std::array<mpq_class,N> walsh_pm(uint64_t mask){ std::array<mpq_class,N> c; for(int S=0;S<N;S++){ long s=0; for(int x=0;x<N;x++){ int v=((mask>>x)&1ull)?-1:1; int chi=(__builtin_popcountll((unsigned)(x&S))&1)?-1:1; s+=v*chi; } c[S]=Q(s,N); } return c; }
static mpq_class avg_sensitivity(uint64_t m){ long s=0; for(int x=0;x<N;x++) for(int i=0;i<NV;i++) s += (((m>>x)&1ull)!=((m>>(x^(1<<i)))&1ull)); return Q(s,N); }
static std::vector<Group> groups_for(uint64_t m){ std::map<std::string,std::pair<Poly,int>> tmp; for(int y=0;y<N;y++){ Poly p=qpoly(m,y); std::string k=pkey(p); auto it=tmp.find(k); if(it==tmp.end()) tmp[k]={p,1}; else it->second.second++; } std::vector<Group> v; for(auto &kv:tmp) v.push_back({kv.second.first,kv.second.second}); return v; }
static void D_point(uint64_t mask,const mpq_class&a,const std::vector<Group>&groups,MP&dlo,MP&dhi,const MP&ln2lo,const MP&ln2hi){ mpq_class p=Q(__builtin_popcountll(mask),N); MP halo,hahi,hplo,hphi,sumlo,sumhi; entropy_bounds(a,halo,hahi); entropy_bounds(p,hplo,hphi); mpfr_set(dlo.v,ln2lo.v,MPFR_RNDD); mpfr_set(dhi.v,ln2hi.v,MPFR_RNDU); mpfr_sub(dlo.v,dlo.v,hahi.v,MPFR_RNDD); mpfr_sub(dhi.v,dhi.v,halo.v,MPFR_RNDU); mpfr_sub(dlo.v,dlo.v,hphi.v,MPFR_RNDD); mpfr_sub(dhi.v,dhi.v,hplo.v,MPFR_RNDU); mpfr_set_ui(sumlo.v,0,MPFR_RNDN); mpfr_set_ui(sumhi.v,0,MPFR_RNDN); for(const auto&g:groups){ mpq_class q=eval_poly(g.p,a); MP qlo,qhi; entropy_bounds(q,qlo,qhi); for(int k=0;k<g.mult;k++){ mpfr_add(sumlo.v,sumlo.v,qlo.v,MPFR_RNDD); mpfr_add(sumhi.v,sumhi.v,qhi.v,MPFR_RNDU); } } mpfr_div_ui(sumlo.v,sumlo.v,N,MPFR_RNDD); mpfr_div_ui(sumhi.v,sumhi.v,N,MPFR_RNDU); mpfr_add(dlo.v,dlo.v,sumlo.v,MPFR_RNDD); mpfr_add(dhi.v,dhi.v,sumhi.v,MPFR_RNDU); }
static void D_interval_lower(uint64_t mask,const mpq_class&a,const mpq_class&b,const std::vector<Group>&groups,MP&dlo,const MP&ln2lo){ mpq_class p=Q(__builtin_popcountll(mask),N); MP hbL,hbU,hpL,hpU,sumL; entropy_bounds(b,hbL,hbU); entropy_bounds(p,hpL,hpU); mpfr_set(dlo.v,ln2lo.v,MPFR_RNDD); mpfr_sub(dlo.v,dlo.v,hbU.v,MPFR_RNDD); mpfr_sub(dlo.v,dlo.v,hpU.v,MPFR_RNDD); mpfr_set_ui(sumL.v,0,MPFR_RNDN); for(const auto&g:groups){ Poly r=restrict_poly(g.p,a,b); mpq_class lo=r[0],hi=r[0]; for(int i=1;i<=DEG;i++){ if(r[i]<lo)lo=r[i]; if(r[i]>hi)hi=r[i]; } MP hL,hU; entropy_min_endpoint(lo,hi,hL,hU); for(int k=0;k<g.mult;k++) mpfr_add(sumL.v,sumL.v,hL.v,MPFR_RNDD); } mpfr_div_ui(sumL.v,sumL.v,N,MPFR_RNDD); mpfr_add(dlo.v,dlo.v,sumL.v,MPFR_RNDD); }
struct CertStats{ long long leaves=0; int maxdepth=0; double minlower=1e100; uint64_t minmask=0; mpq_class mina,minb; };
static bool certify_interval(uint64_t m,const std::vector<Group>&g,const mpq_class&a,const mpq_class&b,int depth,const MP&ln2lo,CertStats&st){ MP lo; D_interval_lower(m,a,b,g,lo,ln2lo); if(mpfr_cmp_si(lo.v,0)>0){ st.leaves++; st.maxdepth=std::max(st.maxdepth,depth); double d=getd(lo); if(d<st.minlower){st.minlower=d;st.minmask=m;st.mina=a;st.minb=b;} return true; } if(depth>=30) return false; mpq_class mid=(a+b)/2; return certify_interval(m,g,a,mid,depth+1,ln2lo,st) && certify_interval(m,g,mid,b,depth+1,ln2lo,st); }

int main(){
    auto t0=std::chrono::steady_clock::now(); auto cand=enumerate_compressed(); std::cout<<"PROB20-21 N<=6 FULL-NOISE-INTERVAL CERTIFICATE\n"; std::cout<<"model_runtime_metadata=UNVERIFIED\n"; std::cout<<"source_defined_compressed_candidates="<<cand.size()<<"\n"; assert(cand.size()==1173);
    int constants=0,dicts=0,balanced_non=0,biased_non=0; std::vector<uint64_t> nontriv; std::map<uint64_t,std::vector<Group>> groups; for(uint64_t m:cand){ if(is_constant(m)){constants++;continue;} if(is_dictator(m)){dicts++;continue;} nontriv.push_back(m); if(__builtin_popcountll(m)==N/2) balanced_non++; else biased_non++; groups[m]=groups_for(m); }
    std::cout<<"constant_candidates="<<constants<<"\n"<<"dictator_candidates="<<dicts<<"\n"<<"nontrivial_candidates="<<nontriv.size()<<"\n"<<"balanced_nondictator_candidates="<<balanced_non<<"\n"<<"biased_nontrivial_candidates="<<biased_non<<"\n";
    MP ln2lo,ln2hi; ln_integer_bounds(2,ln2lo,ln2hi);
    mpq_class minAS; uint64_t minASMask=0; bool have=false; mpq_class minDelta; uint64_t minDeltaMask=0; bool haveD=false; for(uint64_t m:nontriv){ if(__builtin_popcountll(m)==N/2){ mpq_class s=avg_sensitivity(m); if(!have || s<minAS){have=true;minAS=s;minASMask=m;} } auto c=walsh_pm(m); mpq_class mu=c[0],var=1-mu*mu,W1=0; for(int i=0;i<NV;i++) W1+=c[1<<i]*c[1<<i]; mpq_class d=var-W1; assert(d>0); if(!haveD || d<minDelta){haveD=true;minDelta=d;minDeltaMask=m;} }
    assert(minAS==Q(5,4)); assert(minDelta==Q(57,1024)); std::cout<<"min_balanced_nondictator_avg_sensitivity="<<minAS<<" mask="<<minASMask<<"\n"<<"min_Delta_var_minus_W1="<<minDelta<<" mask="<<minDeltaMask<<"\n";
    mpq_class A0=Q(1,524288),A1=Q(69,140),rho0=Q(1,70); std::cout<<"full_alpha_interval=[0,1/2]\nlow_noise=[0,1/524288]\nmiddle=[1/524288,69/140]\nhigh_noise=[69/140,1/2]\n";
    MP hA0L,hA0U,h31L,h31U,biasGap; entropy_bounds(A0,hA0L,hA0U); entropy_bounds(Q(15,32),h31L,h31U); mpfr_set(biasGap.v,ln2lo.v,MPFR_RNDD); mpfr_sub(biasGap.v,biasGap.v,hA0U.v,MPFR_RNDD); mpfr_sub(biasGap.v,biasGap.v,h31U.v,MPFR_RNDD); assert(mpfr_cmp_si(biasGap.v,0)>0); std::cout<<std::setprecision(17)<<"biased_low_noise_lower_gap_nat="<<getd(biasGap)<<"\n";
    mpq_class c0=Q(524287,524288); c0=c0*c0*c0*c0*c0; MP lnAL,lnAU,ln6L,ln6U,coefLo,term1,term2,balMargin; ln_integer_bounds(524288,lnAL,lnAU); ln_integer_bounds(6,ln6L,ln6U); mpq_class coef=Q(5,4)*c0-1; setq(coefLo,coef,MPFR_RNDD); mpfr_mul(term1.v,coefLo.v,lnAL.v,MPFR_RNDD); MP sbar; setq(sbar,Q(5,4),MPFR_RNDU); mpfr_mul(term2.v,sbar.v,ln6U.v,MPFR_RNDU); mpfr_sub(balMargin.v,term1.v,term2.v,MPFR_RNDD); MP one; mpfr_set_ui(one.v,1,MPFR_RNDN); mpfr_sub(balMargin.v,balMargin.v,one.v,MPFR_RNDD); assert(mpfr_cmp_si(balMargin.v,0)>0); std::cout<<"balanced_low_noise_uniform_margin_over_alpha="<<getd(balMargin)<<"\n";
    mpq_class minHighSq; uint64_t minHighMask=0; bool haveHigh=false; mpq_class minHighL; uint64_t minHighLMask=0; bool haveHighL=false; for(uint64_t m:nontriv){ auto c=walsh_pm(m); mpq_class mu=abs(c[0]),var=1-mu*mu,W1=0; for(int i=0;i<NV;i++) W1+=c[1ull<<i]*c[1ull<<i]; mpq_class d=var-W1; mpq_class L=(1-rho0*rho0)*d-63*rho0*rho0*var; mpq_class sq=L*L-4*mu*mu*rho0*rho0*63*var; assert(L>0 && sq>0); if(!haveHigh || sq<minHighSq){haveHigh=true;minHighSq=sq;minHighMask=m;} if(!haveHighL || L<minHighL){haveHighL=true;minHighL=L;minHighLMask=m;} } std::cout<<"high_noise_exact_min_square_margin="<<minHighSq<<" mask="<<minHighMask<<"\n"<<"high_noise_exact_min_L="<<minHighL<<" mask="<<minHighLMask<<"\n";
    long neg=0; double minGrid=1e100; uint64_t minGridMask=0; mpq_class minGridA; for(uint64_t m:nontriv){ auto &gg=groups[m]; for(int j=0;j<=64;j++){ mpq_class a=Q(j,128); MP lo,hi; D_point(m,a,gg,lo,hi,ln2lo,ln2hi); if(mpfr_cmp_si(hi.v,0)<0) neg++; if(j>0 && j<64){ double d=getd(lo); if(d<minGrid){minGrid=d;minGridMask=m;minGridA=a;} } } } assert(neg==0); std::cout<<"counterexample_grid_alpha=j/128,j=0..64\n"<<"counterexample_grid_certified_negative="<<neg<<"\n"<<"grid_smallest_interior_lower_D_nat="<<minGrid<<" mask="<<minGridMask<<" alpha="<<minGridA<<"\n";
    CertStats st; for(uint64_t m:nontriv){ bool ok=certify_interval(m,groups[m],A0,A1,0,ln2lo,st); if(!ok){ std::cerr<<"FAILED middle certification mask="<<m<<"\n"; return 2; } }
    std::cout<<"middle_leaf_intervals="<<st.leaves<<"\n"<<"middle_max_bisection_depth="<<st.maxdepth<<"\n"<<"middle_min_outward_lower_D_nat="<<st.minlower<<" mask="<<st.minmask<<" a="<<st.mina<<" b="<<st.minb<<"\n"<<"log_engine=MPFR_shared_library_directed_rounding_256_bits_exact_rational_inputs\n";
    auto t1=std::chrono::steady_clock::now(); double secs=std::chrono::duration<double>(t1-t0).count(); std::cout<<"checker_runtime_seconds="<<secs<<"\nRESULT=PASS\n"; return 0;
}
