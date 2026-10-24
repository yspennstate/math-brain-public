#include <boost/multiprecision/cpp_int.hpp>
#include <iostream>
#include <vector>
#include <tuple>
#include <algorithm>
#include <stdexcept>
using boost::multiprecision::cpp_rational;
using Q=cpp_rational;
struct I{Q lo,hi; I(Q a=0):lo(a),hi(a){} I(Q a,Q b):lo(a),hi(b){if(b<a) throw std::runtime_error("bad");}};
I add(I a,I b){return I(a.lo+b.lo,a.hi+b.hi);} I neg(I a){return I(-a.hi,-a.lo);} I sub(I a,I b){return add(a,neg(b));}
I mul(I a,I b){Q v1=a.lo*b.lo,v2=a.lo*b.hi,v3=a.hi*b.lo,v4=a.hi*b.hi; return I(std::min(std::min(v1,v2),std::min(v3,v4)),std::max(std::max(v1,v2),std::max(v3,v4)));}
I inv(I a){if(a.lo<=0 && a.hi>=0) throw std::runtime_error("zero"); return I(Q(1)/a.hi,Q(1)/a.lo);} I divi(I a,I b){return mul(a,inv(b));}
I sq(I a){ if(a.lo>=0) return I(a.lo*a.lo,a.hi*a.hi); if(a.hi<=0) return I(a.hi*a.hi,a.lo*a.lo); Q m=std::max(a.lo*a.lo,a.hi*a.hi); return I(0,m);} 
I powi(I a,int n){I r(1); for(int i=0;i<n;i++) r=mul(r,a); return r;}
I C(Q x){return I(x);} I add(I a,Q b){return add(a,C(b));} I add(Q a,I b){return add(C(a),b);} I sub(I a,Q b){return sub(a,C(b));} I sub(Q a,I b){return sub(C(a),b);} I mul(I a,Q b){return mul(a,C(b));} I mul(Q a,I b){return mul(C(a),b);} I divi(I a,Q b){return divi(a,C(b));} I divi(Q a,I b){return divi(C(a),b);} 
long double ld(const Q& q){return q.convert_to<long double>();}
Q frac(long long a,long long b=1){return Q(a)/Q(b);} 
int fact(int n){int r=1; for(int i=2;i<=n;i++) r*=i; return r;}
I Kfun(I base,int j,I w0,I w3,I w4,I u3,I u4){I tot(0); for(int n3=0;n3<=j;n3++) for(int n4=0;n4<=j-n3;n4++){int n0=j-n3-n4; Q coeff=frac(fact(j),fact(n0)*fact(n3)*fact(n4)); I w=mul(coeff,mul(powi(w0,n0),mul(powi(w3,n3),powi(w4,n4)))); I s=add(mul(n3,u3),mul(n4,u4)); I ker=divi(base,sq(add(base,s))); tot=add(tot,mul(w,ker));} return tot;}
struct Bnd{I rho; Q prod,thlo;};
Bnd bound34(I L,I P){
 I R=add(sub(C(12),mul(4,L)),mul(L,P)); I u=divi(sub(4,L),4); I d3=divi(R,add(12,mul(L,P))); I d4=divi(R,add(sub(12,L),mul(L,P))); I u3=divi(mul(3,sub(4,L)),add(12,L)); I u4=u; I r3=divi(d3,u3), r4=divi(d4,u4); I w3=mul(sub(1,P),r3), w4=mul(P,r4), w0=sub(sub(1,w3),w4);
 I K2=Kfun(L,2,w0,w3,w4,u3,u4), K3=Kfun(L,3,w0,w3,w4,u3,u4); I rho=add(mul(mul(sub(1,P),3),K2),mul(mul(P,4),K3)); I A=add(mul(sub(1,P),divi(mul(12,sub(4,L)),sq(add(12,L)))),mul(P,divi(sub(4,L),16))); I eta=divi(A,sub(1,rho)); I mu=add(mul(sub(1,P),d3),mul(P,d4)); I a=sub(L,1); I Kc=Kfun(a,3,w0,w3,w4,u3,u4); I D=sub(add(divi(1,a),divi(mul(mul(3,eta),Kc),mu)),divi(4,sub(16,L)));
 I br=add(divi(mul(sub(1,P),d3),add(3,u3)),divi(mul(P,d4),add(3,u4))); I Rstar=mul(frac(4,5),add(1,mul(divi(sub(L,1),sub(4,L)),br))); I thI=divi(mul(P,Rstar),add(sub(1,P),mul(P,Rstar))); Q th=thI.lo; if(th<frac(8,13)) throw std::runtime_error("theta low"); Q g=th*(1-th)/(3+th); Q prod=L.hi*g*D.hi; return {rho,prod,th};
}
struct Node{Q l0,l1,p0,p1;int dep;};
void certify(Q l0,Q l1,Q p0,Q p1,Q qt,Q rqt,int maxdep){std::vector<Node> st; st.push_back({l0,l1,p0,p1,0}); long long vis=0,acc=0; Q worst=-1000,wr=-1000; int md=0; while(!st.empty()){Node n=st.back(); st.pop_back(); vis++; md=std::max(md,n.dep); bool good=false; Bnd b; try{b=bound34(I(n.l0,n.l1),I(n.p0,n.p1)); good=(b.rho.hi<rqt && b.prod<qt);}catch(...){good=false;} if(good){acc++; if(b.prod>worst) worst=b.prod; if(b.rho.hi>wr) wr=b.rho.hi; continue;} if(n.dep>=maxdep){std::cerr<<"FAIL depth "<<n.dep<<" box "<<ld(n.l0)<<" "<<ld(n.l1)<<" "<<ld(n.p0)<<" "<<ld(n.p1)<<"\n"; exit(2);} if((n.p1-n.p0) > (n.l1-n.l0)){Q m=(n.p0+n.p1)/2; st.push_back({n.l0,n.l1,n.p0,m,n.dep+1}); st.push_back({n.l0,n.l1,m,n.p1,n.dep+1});} else {Q m=(n.l0+n.l1)/2; st.push_back({n.l0,m,n.p0,n.p1,n.dep+1}); st.push_back({m,n.l1,n.p0,n.p1,n.dep+1});}}
 std::cout<<"PASS visited="<<vis<<" accepted="<<acc<<" worst_prod="<<(double)ld(worst)<<" worst_rho="<<(double)ld(wr)<<" maxdepth="<<md<<"\n";
}
int main(int argc,char**argv){
 const Q q=frac(99,100), rq=frac(49,50);
 if(argc!=2){std::cerr<<"usage: checker low|high\n"; return 2;}
 std::string mode=argv[1];
 if(mode=="low"){
   std::cout<<"RECT_LOW lambda=[71/25,3] p=[2/3,1] product<99/100 rho<49/50\n";
   certify(frac(71,25),frac(3),frac(2,3),frac(1),q,rq,30);
 } else if(mode=="high"){
   std::cout<<"RECT_HIGH lambda=[3,603/200] p=[2/3,1] product<99/100 rho<49/50\n";
   certify(frac(3),frac(603,200),frac(2,3),frac(1),q,rq,30);
 } else return 2;
 Q margin=frac(8)*(frac(1)-q)/((frac(4)+frac(603,200))*(frac(4)+frac(603,200)));
 if(margin!=frac(3200,1968409)) return 3;
 if(!(frac(47,13)>frac(603,200))) return 4;
 std::cout<<"DERIVATIVE_MARGIN=3200/1968409\n";
 std::cout<<"THETA_BASE=8/13 M_BASE=47/13 > 603/200\n";
 std::cout<<"ALL_EXACT_CHECKS_PASS\n";
}
