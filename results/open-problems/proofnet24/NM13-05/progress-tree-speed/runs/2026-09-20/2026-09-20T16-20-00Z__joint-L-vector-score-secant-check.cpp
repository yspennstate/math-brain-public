#include <bits/stdc++.h>
using namespace std;
struct I{double lo,hi;};
static inline double dn(double x){return nextafter(x,-INFINITY);} 
static inline double up(double x){return nextafter(x, INFINITY);} 
static inline I point(double x){return {x,x};}
static inline I add(I a,I b){return {dn(a.lo+b.lo),up(a.hi+b.hi)};}
static inline I sub(I a,I b){return {dn(a.lo-b.hi),up(a.hi-b.lo)};}
static inline I mul(I a,I b){double v[4]={a.lo*b.lo,a.lo*b.hi,a.hi*b.lo,a.hi*b.hi}; double l=*min_element(v,v+4),h=*max_element(v,v+4); return {dn(l),up(h)};}
static inline I divi(I a,I b){if(b.lo<=0 && b.hi>=0)return {-INFINITY,INFINITY}; I inv{dn(1.0/b.hi),up(1.0/b.lo)}; return mul(a,inv);}
static inline I sq(I a){return mul(a,a);} 
static inline I cube(I a){return mul(mul(a,a),a);} 
static inline I ipow(I a,int n){I r=point(1);for(int i=0;i<n;i++)r=mul(r,a);return r;}
static inline I scale(I a,double c){return mul(a,point(c));}
static inline I one_minus(I a){return sub(point(1),a);} 
static double Cbin(int n,int r){if(r<0||r>n)return 0; double z=1;for(int i=1;i<=r;i++)z=z*(n-r+i)/i;return z;}

pair<I,I> harmonic(I lam,I p,int nit=12){
 I q=one_minus(p), d=sub(point(1),divi(mul(lam,sub(point(4),p)),point(12)));
 I M3=add(point(1),divi(lam,scale(d,3))), M4=add(point(1),divi(lam,scale(d,4)));
 for(int it=0;it<nit;it++){
  I o3=M3,o4=M4;
  auto Tk=[&](int k){I s=point(0);for(int r=0;r<=k;r++){I prob=scale(mul(ipow(p,r),ipow(q,k-r)),Cbin(k,r));I den=add(scale(divi(point(1),o3),k-r),scale(divi(point(1),o4),r));s=add(s,divi(prob,den));}return add(point(1),mul(lam,s));};
  M3=Tk(3);M4=Tk(4);
 }
 return {M3,M4};
}
I KJ(int j,I a,I p,I d3,I d4){I q=one_minus(p),s=point(0);for(int r=0;r<=j;r++){I prob=scale(mul(ipow(p,r),ipow(q,j-r)),Cbin(j,r));I den=add(a,add(scale(d3,j-r),scale(d4,r)));s=add(s,mul(prob,divi(a,sq(den))));}return s;}
I csec(I t,I u){return divi(add(scale(t,2),u),mul(sq(t),sq(add(t,u))));}

pair<I,I> jointL(I lam,I p,I d3,I d4,I u3,I u4,int nit=12){
 I q=one_minus(p);
 I L03=divi(mul(one_minus(u3),sq(d3)),lam);
 I L04=divi(mul(one_minus(u4),sq(d4)),lam);
 I L3=L03,L4=L04;
 auto coef=[&](int n,int k){I uk=(k==3?u3:u4);I den=add(lam,add(uk,scale(u4,n-1)));return divi(lam,cube(den));};
 for(int it=0;it<nit;it++){
  I o3=L3,o4=L4;
  I s3=add(mul(q,mul(coef(3,3),o3)),mul(p,mul(coef(3,4),o4)));
  I s4=add(mul(q,mul(coef(4,3),o3)),mul(p,mul(coef(4,4),o4)));
  L3=add(L03,scale(s3,3));
  L4=add(L04,scale(s4,4));
 }
 return {L3,L4};
}

struct Eval{double prod_hi,rho_hi,theta_lo,eta_hi,delta_lo,L3lo,L4lo,Dhi;bool valid;};
Eval eval_box(double l0,double l1,double p0,double p1){
 I lam{l0,l1},p{p0,p1},q=one_minus(p);
 auto [M3,M4]=harmonic(lam,p,12); I d3=divi(point(1),M3),d4=divi(point(1),M4);
 I mu=add(mul(q,d3),mul(p,d4));
 I four_minus=sub(point(4),lam),u4=scale(four_minus,.25),u3=divi(scale(four_minus,3),add(point(12),lam));
 auto [L3,L4]=jointL(lam,p,d3,d4,u3,u4,12);
 I rho=add(mul(scale(q,3),KJ(2,lam,p,d3,d4)),mul(scale(p,4),KJ(3,lam,p,d3,d4)));
 I A=add(divi(scale(mul(q,four_minus),12),sq(add(point(12),lam))),scale(mul(p,four_minus),1.0/16.0));
 // Improved own-B subtraction in derivative-moment contraction.
 I delta=point(0);
 for(int n=3;n<=4;n++){
  I rootprob=(n==3?q:p);
  I tn=add(lam,scale(u4,n-1));
  I ch=add(mul(q,mul(csec(tn,u3),L3)),mul(p,mul(csec(tn,u4),L4)));
  delta=add(delta,mul(rootprob,scale(mul(lam,ch),n)));
 }
 I numeta=sub(A,delta),deneta=sub(point(1),rho),eta=divi(numeta,deneta);
 I a=sub(lam,point(1));
 // New score-level own-B subtraction for h_3/c_3.
 I ts=add(a,scale(u4,3)); // = 2 + lambda/4
 I qscore=add(mul(q,mul(csec(ts,u3),L3)),mul(p,mul(csec(ts,u4),L4)));
 I bracket=sub(mul(eta,KJ(3,a,p,d3,d4)),mul(a,qscore));
 I D=add(divi(point(1),a),scale(divi(bracket,mu),3));
 D=sub(D,divi(point(4),sub(point(16),lam)));
 // Inherited quantitative branch-addition localization.
 I ratio_inner=add(divi(mul(q,d3),add(point(3),u3)),divi(mul(p,d4),add(point(3),u4)));
 I R=scale(add(point(1),mul(divi(a,four_minus),ratio_inner)),.8);
 I theta=divi(mul(p,R),add(q,mul(p,R)));
 if(!(theta.lo>.5)||!(rho.hi<1)||!(numeta.lo>0)||!(mu.lo>0)||!(D.lo>0)||!(L3.lo>0)||!(L4.lo>0)) return {INFINITY,rho.hi,theta.lo,eta.hi,delta.lo,L3.lo,L4.lo,D.hi,false};
 I x=point(theta.lo),gx=divi(mul(x,one_minus(x)),add(point(3),x));
 I prod=mul(mul(lam,point(gx.hi)),D);
 return {prod.hi,rho.hi,theta.lo,eta.hi,delta.lo,L3.lo,L4.lo,D.hi,true};
}

struct Mode{string name;double p0,L,q;string ptxt,Ltxt,qtxt;};
struct Stats{long long visited=0,accepted=0;int maxdepth=0;double worstprod=0,worstrho=0,mintheta=1,mindelta=1e9,minL3=1e9,minL4=1e9;bool ok=true;string fail;};
void rec(double l0,double l1,double p0,double p1,int dep,const Mode&m,Stats&st){
 st.visited++;st.maxdepth=max(st.maxdepth,dep); Eval e=eval_box(l0,l1,p0,p1);
 if(e.valid&&e.prod_hi<m.q&&e.rho_hi<.99){st.accepted++;st.worstprod=max(st.worstprod,e.prod_hi);st.worstrho=max(st.worstrho,e.rho_hi);st.mintheta=min(st.mintheta,e.theta_lo);st.mindelta=min(st.mindelta,e.delta_lo);st.minL3=min(st.minL3,e.L3lo);st.minL4=min(st.minL4,e.L4lo);return;}
 if(dep>=40){st.ok=false;ostringstream os;os<<setprecision(17)<<"FAIL box l=["<<l0<<","<<l1<<"] p=["<<p0<<","<<p1<<"] prod="<<e.prod_hi<<" rho="<<e.rho_hi<<" theta="<<e.theta_lo<<" Dhi="<<e.Dhi<<" valid="<<e.valid;st.fail=os.str();return;}
 double lw=l1-l0,pw=p1-p0; if(lw/(m.L-2)>=pw/(1-m.p0)){double mid=(l0+l1)/2;rec(l0,mid,p0,p1,dep+1,m,st);if(!st.ok)return;rec(mid,l1,p0,p1,dep+1,m,st);}else{double mid=(p0+p1)/2;rec(l0,l1,p0,mid,dep+1,m,st);if(!st.ok)return;rec(l0,l1,mid,p1,dep+1,m,st);}
}
int main(){
 vector<Mode> modes={
  {"cross_293_500",dn(293.0/500.0),up(3001.0/1000.0),dn(9999.0/10000.0),"293/500","3001/1000","9999/10000"},
  {"three_fifths_151_50",dn(3.0/5.0),up(151.0/50.0),dn(999.0/1000.0),"3/5","151/50","999/1000"},
  {"two_thirds_78_25",dn(2.0/3.0),up(78.0/25.0),dn(199.0/200.0),"2/3","78/25","199/200"},
  {"three_quarters_409_125",dn(3.0/4.0),up(409.0/125.0),dn(999.0/1000.0),"3/4","409/125","999/1000"}
 };
 cout<<"JOINT_L_VECTOR_SECANT_DIRECTED_INTERVAL_CHECK\n";
 for(auto m:modes){Stats st;rec(2.0,m.L,m.p0,1.0,0,m,st);cout<<setprecision(17)<<"MODE="<<m.name<<" intended_p0="<<m.ptxt<<" intended_L="<<m.Ltxt<<" intended_q="<<m.qtxt<<" outer_p0="<<m.p0<<" outer_L="<<m.L<<" safe_q="<<m.q<<"\n";if(!st.ok){cout<<st.fail<<"\n";return 2;}cout<<"PASS visited="<<st.visited<<" accepted="<<st.accepted<<" worst_prod="<<st.worstprod<<" worst_rho="<<st.worstrho<<" min_theta="<<st.mintheta<<" min_delta="<<st.mindelta<<" min_L3="<<st.minL3<<" min_L4="<<st.minL4<<" maxdepth="<<st.maxdepth<<"\n";}
 cout<<"ALL_RIGOROUS_INTERVAL_CHECKS_PASS\n";
}
