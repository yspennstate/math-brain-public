#include <boost/multiprecision/cpp_int.hpp>
#include <iostream>
#include <vector>
#include <algorithm>
#include <stdexcept>
using boost::multiprecision::cpp_rational; using Q=cpp_rational;
struct I{Q lo,hi; I(Q a=0):lo(a),hi(a){} I(Q a,Q b):lo(a),hi(b){if(b<a)throw std::runtime_error("bad");}};
I add(I a,I b){return I(a.lo+b.lo,a.hi+b.hi);} I neg(I a){return I(-a.hi,-a.lo);} I sub(I a,I b){return add(a,neg(b));}
I mul(I a,I b){Q v1=a.lo*b.lo,v2=a.lo*b.hi,v3=a.hi*b.lo,v4=a.hi*b.hi; return I(std::min(std::min(v1,v2),std::min(v3,v4)),std::max(std::max(v1,v2),std::max(v3,v4)));}
I inv(I a){if(a.lo<=0 && a.hi>=0) throw std::runtime_error("zero"); return I(Q(1)/a.hi,Q(1)/a.lo);} I divi(I a,I b){return mul(a,inv(b));}
I sq(I a){if(a.lo>=0)return I(a.lo*a.lo,a.hi*a.hi); if(a.hi<=0)return I(a.hi*a.hi,a.lo*a.lo); Q m=std::max(a.lo*a.lo,a.hi*a.hi);return I(0,m);} I powi(I a,int n){I r(1);while(n--)r=mul(r,a);return r;}
I C(Q x){return I(x);} I add(Q a,I b){return add(C(a),b);} I add(I a,Q b){return add(a,C(b));} I sub(I a,Q b){return sub(a,C(b));} I sub(Q a,I b){return sub(C(a),b);} I mul(I a,Q b){return mul(a,C(b));} I mul(Q a,I b){return mul(C(a),b);} I divi(I a,Q b){return divi(a,C(b));} I divi(Q a,I b){return divi(C(a),b);} 
Q frac(long long a,long long b=1){return Q(a)/Q(b);} long double ld(const Q&q){return q.convert_to<long double>();} int binom(int n,int k){int r=1;for(int i=1;i<=k;i++)r=r*(n-k+i)/i;return r;}
I mixwt(int k,int r,I P){return mul(Q(binom(k,r)),mul(powi(P,r),powi(sub(1,P),k-r)));}
I Hpattern(int k,int r,I z3,I z4){I den(0); if(k-r)den=add(den,mul(k-r,inv(z3))); if(r)den=add(den,mul(r,inv(z4))); return inv(den);} 
I Tcomp(int k,I L,I P,I z3,I z4){I s(0);for(int r=0;r<=k;r++)s=add(s,mul(mixwt(k,r,P),Hpattern(k,r,z3,z4)));return add(1,mul(L,s));}
void dvec(I L,I P,int n,I&d3,I&d4){
  // scalar Cauchy supersolution z <= 1/d, then conditional z_k <= 1+lambda/(k d)
  I d=sub(1,divi(mul(L,sub(4,P)),12));
  I z=inv(d);
  I z3=add(1,divi(mul(L,z),3)), z4=add(1,divi(mul(L,z),4));
  for(int it=0;it<n;it++){I n3=Tcomp(3,L,P,z3,z4), n4=Tcomp(4,L,P,z3,z4); z3=n3; z4=n4;}
  d3=inv(z3); d4=inv(z4);
}
I KJ(I base,int j,I P,I d3,I d4){I tot(0);for(int r=0;r<=j;r++){I w=mixwt(j,r,P);I s=add(mul(j-r,d3),mul(r,d4));I ker=divi(base,sq(add(base,s)));tot=add(tot,mul(w,ker));}return tot;}
struct Bnd{I rho,D,Rstar,theta;Q prod;};
Bnd bound34(I L,I P,int nit){
 I d3,d4; dvec(L,P,nit,d3,d4);
 I u=divi(sub(4,L),4),u3=divi(mul(3,sub(4,L)),add(12,L)),u4=u;
 I K2=KJ(L,2,P,d3,d4),K3=KJ(L,3,P,d3,d4);
 I rho=add(mul(mul(sub(1,P),3),K2),mul(mul(P,4),K3));
 I A=add(mul(sub(1,P),divi(mul(12,sub(4,L)),sq(add(12,L)))),mul(P,divi(sub(4,L),16)));
 I eta=divi(A,sub(1,rho)); I mu=add(mul(sub(1,P),d3),mul(P,d4)); I a=sub(L,1); I Kc=KJ(a,3,P,d3,d4);
 I D=sub(add(divi(1,a),divi(mul(mul(3,eta),Kc),mu)),divi(4,sub(16,L)));
 I br=add(divi(mul(sub(1,P),d3),add(3,u3)),divi(mul(P,d4),add(3,u4)));
 I Rstar=mul(frac(4,5),add(1,mul(divi(sub(L,1),sub(4,L)),br)));
 I thI=divi(mul(P,Rstar),add(sub(1,P),mul(P,Rstar))); Q th=thI.lo; if(th<frac(1,2))throw std::runtime_error("theta low");
 Q g=th*(1-th)/(3+th); Q prod=L.hi*g*D.hi; return {rho,D,Rstar,thI,prod};
}
struct Node{Q l0,l1,p0,p1;int dep;};
void certify(Q l0,Q l1,Q p0,Q p1,Q qt,Q rqt,int maxdep,int nit){std::vector<Node>st{{l0,l1,p0,p1,0}};long long vis=0,acc=0;Q worst=-1000,wr=-1000,wth=1000;int md=0;while(!st.empty()){auto n=st.back();st.pop_back();vis++;md=std::max(md,n.dep);bool good=false;Bnd b;try{b=bound34(I(n.l0,n.l1),I(n.p0,n.p1),nit);good=(b.rho.hi<rqt&&b.prod<qt);}catch(...){good=false;}if(good){acc++;worst=std::max(worst,b.prod);wr=std::max(wr,b.rho.hi);wth=std::min(wth,b.theta.lo);continue;}if(n.dep>=maxdep){std::cerr<<"FAIL depth box "<<(double)ld(n.l0)<<" "<<(double)ld(n.l1)<<" "<<(double)ld(n.p0)<<" "<<(double)ld(n.p1)<<"\n";exit(2);}if((n.p1-n.p0)>(n.l1-n.l0)){Q m=(n.p0+n.p1)/2;st.push_back({n.l0,n.l1,n.p0,m,n.dep+1});st.push_back({n.l0,n.l1,m,n.p1,n.dep+1});}else{Q m=(n.l0+n.l1)/2;st.push_back({n.l0,m,n.p0,n.p1,n.dep+1});st.push_back({m,n.l1,n.p0,n.p1,n.dep+1});}}
std::cout<<"PASS visited="<<vis<<" accepted="<<acc<<" worst_prod="<<(double)ld(worst)<<" worst_rho="<<(double)ld(wr)<<" min_theta="<<(double)ld(wth)<<" maxdepth="<<md<<"\n";}
int main(int argc,char**argv){if(argc!=2)return 2;std::string mode=argv[1];int nit=1;Q L,p0,q,rq=frac(24,25);if(mode=="cross63"){L=frac(3001,1000);p0=frac(63,100);q=frac(999,1000);}else if(mode=="twothirds"){L=frac(611,200);p0=frac(2,3);q=frac(99,100);}else if(mode=="threequarters"){L=frac(321,100);p0=frac(3,4);q=frac(99,100);}else return 2;std::cout<<mode<<" p=["<<(double)ld(p0)<<",1] lambda=[3/2,"<<(double)ld(L)<<"] nit="<<nit<<"\n";certify(frac(3,2),L,p0,1,q,rq,40,nit);
Q thetab=frac(4)*p0/(frac(5)-p0);Q Mb=frac(3)+thetab;if(!(Mb>L)){std::cerr<<"M base fail\n";return 3;}Q margin=frac(8)*(frac(1)-q)/((frac(4)+L)*(frac(4)+L));std::cout<<"theta_base="<<(double)ld(thetab)<<" M_base="<<(double)ld(Mb)<<" margin="<<(double)ld(margin)<<" exact_margin="<<margin<<"\nALL_EXACT_CHECKS_PASS\n";}
