#include <boost/numeric/interval.hpp>
#include <boost/numeric/interval/rounded_transc.hpp>
#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <iomanip>
#include <limits>
#include <stdexcept>

using namespace boost::numeric;
using Rounding = interval_lib::save_state<interval_lib::rounded_transc_std<double>>;
using Checking = interval_lib::checking_base<double>;
using Policies = interval_lib::policies<Rounding,Checking>;
using I = interval<double,Policies>;

static I Z(long long n){ return I(static_cast<double>(n)); }
static I rat(long long n,long long d){
    double x=static_cast<double>(n)/static_cast<double>(d);
    return I(std::nextafter(x,-std::numeric_limits<double>::infinity()),
             std::nextafter(x,+std::numeric_limits<double>::infinity()));
}
static I ipow(I x,int n){ I y(1.0); while(n--) y*=x; return y; }
static int binom(int n,int r){ int q=1; for(int j=1;j<=r;j++) q=q*(n-r+j)/j; return q; }
static I weight(int k,int r,I p){ return Z(binom(k,r))*ipow(p,r)*ipow(Z(1)-p,k-r); }

static I harmonic_pattern(int k,int r,I m3,I m4){
    I den(0.0);
    if(k-r) den += Z(k-r)/m3;
    if(r) den += Z(r)/m4;
    return Z(1)/den;
}
static I Tcomp(int k,I lam,I p,I m3,I m4){
    I s(0.0);
    for(int r=0;r<=k;r++) s += weight(k,r,p)*harmonic_pattern(k,r,m3,m4);
    return Z(1)+lam*s;
}

// M^(0) is the scalar Cauchy envelope. Applying the increasing harmonic
// Jensen map T twelve times preserves an upper bound on the exact vector
// z_k=E[1/B | nu=k]: if z<=M then z<=T(z)<=T(M).
static void escape_lower_bounds(I lam,I p,I &d3,I &d4){
    I d = Z(1)-lam*(Z(4)-p)/Z(12);
    if(d.lower()<=0) throw std::runtime_error("nonpositive scalar escape bound");
    I z = Z(1)/d;
    I m3=Z(1)+lam*z/Z(3), m4=Z(1)+lam*z/Z(4);
    for(int it=0;it<12;it++){
        I n3=Tcomp(3,lam,p,m3,m4), n4=Tcomp(4,lam,p,m3,m4);
        m3=n3; m4=n4;
    }
    d3=Z(1)/m3; d4=Z(1)/m4;
}

static I KJ(I base,int j,I p,I d3,I d4){
    I s(0.0);
    for(int r=0;r<=j;r++){
        I t=Z(j-r)*d3+Z(r)*d4;
        I den=base+t;
        s += weight(j,r,p)*base/(den*den);
    }
    return s;
}

struct Bound { I rho, D, R, theta, prod; };
static Bound bound_box(I lam,I p){
    I d3,d4; escape_lower_bounds(lam,p,d3,d4);
    I u=(Z(4)-lam)/Z(4);
    I u3=Z(3)*(Z(4)-lam)/(Z(12)+lam), u4=u;
    I K2=KJ(lam,2,p,d3,d4), K3=KJ(lam,3,p,d3,d4);
    I rho=(Z(1)-p)*Z(3)*K2+p*Z(4)*K3;
    if(rho.upper()>=1.0) throw std::runtime_error("rho crosses one");

    // Valid on lambda>=2: each possible sibling sum lies in the increasing
    // region of s/(lambda+s)^2, so evaluating at S_max bounds the source.
    I A=(Z(1)-p)*Z(12)*(Z(4)-lam)/((Z(12)+lam)*(Z(12)+lam))
       +p*(Z(4)-lam)/Z(16);
    I eta=A/(Z(1)-rho);
    I mu=(Z(1)-p)*d3+p*d4;
    I a=lam-Z(1);
    I Kc=KJ(a,3,p,d3,d4);
    I D=Z(1)/a+Z(3)*eta*Kc/mu-Z(4)/(Z(16)-lam);

    I branch=(Z(1)-p)*d3/(Z(3)+u3)+p*d4/(Z(3)+u4);
    I Rstar=rat(4,5)*(Z(1)+(lam-Z(1))/(Z(4)-lam)*branch);
    I theta=p*Rstar/((Z(1)-p)+p*Rstar);
    if(theta.lower()<=0.5) throw std::runtime_error("theta not on decreasing branch");

    // g(theta)=theta(1-theta)/(3+theta) is decreasing for theta>=1/2.
    // Evaluate it rigorously at the certified lower endpoint of theta.
    I t(theta.lower());
    I gg=t*(Z(1)-t)/(Z(3)+t);
    double gup=gg.upper();
    I prod=lam*I(gup)*D;
    return {rho,D,Rstar,theta,prod};
}

struct Node { double l0,l1,p0,p1; int depth; };
struct Stats { long long visited=0, accepted=0; double worst_prod=-1, worst_rho=-1, min_theta=1; int maxdepth=0; };

static bool certify(long long Lnum,long long Lden,long long pnum,long long pden,
                    long long qnum,long long qden,long long rnum,long long rden,
                    Stats &st){
    I Lex=rat(Lnum,Lden), pex=rat(pnum,pden), qex=rat(qnum,qden), rex=rat(rnum,rden);
    double Lhi=Lex.upper(), p0=pex.lower(), qlo=qex.lower(), rlo=rex.lower();
    std::vector<Node> stack{{2.0,Lhi,p0,1.0,0}};
    while(!stack.empty()){
        Node n=stack.back(); stack.pop_back(); st.visited++; st.maxdepth=std::max(st.maxdepth,n.depth);
        Bound b; bool good=false;
        try {
            b=bound_box(I(n.l0,n.l1),I(n.p0,n.p1));
            good=(b.prod.upper()<qlo && b.rho.upper()<rlo);
        } catch(...) { good=false; }
        if(good){
            st.accepted++;
            st.worst_prod=std::max(st.worst_prod,b.prod.upper());
            st.worst_rho=std::max(st.worst_rho,b.rho.upper());
            st.min_theta=std::min(st.min_theta,b.theta.lower());
            continue;
        }
        if(n.depth>=36){
            std::cerr<<std::setprecision(17)<<"FAIL box lambda=["<<n.l0<<","<<n.l1
                     <<"] p=["<<n.p0<<","<<n.p1<<"]";
            try{ std::cerr<<" prod_hi="<<b.prod.upper()<<" rho_hi="<<b.rho.upper(); }catch(...){}
            std::cerr<<"\n";
            return false;
        }
        if((n.p1-n.p0)>(n.l1-n.l0)){
            double m=(n.p0+n.p1)/2.0;
            stack.push_back({n.l0,n.l1,n.p0,m,n.depth+1});
            stack.push_back({n.l0,n.l1,m,n.p1,n.depth+1});
        } else {
            double m=(n.l0+n.l1)/2.0;
            stack.push_back({n.l0,m,n.p0,n.p1,n.depth+1});
            stack.push_back({m,n.l1,n.p0,n.p1,n.depth+1});
        }
    }
    return true;
}

static void run_mode(const char* name,long long pn,long long pd,long long Ln,long long Ld,
                     long long qn,long long qd){
    Stats st;
    bool ok=certify(Ln,Ld,pn,pd,qn,qd,97,100,st);
    std::cout<<std::setprecision(12)<<"MODE="<<name<<" nit=12 p0="<<(double)pn/pd
             <<" L="<<(double)Ln/Ld<<" q="<<(double)qn/qd<<"\n";
    if(!ok){ std::cout<<"FAILED\n"; std::exit(2); }
    std::cout<<"PASS visited="<<st.visited<<" accepted="<<st.accepted
             <<" worst_prod="<<st.worst_prod<<" worst_rho="<<st.worst_rho
             <<" min_theta="<<st.min_theta<<" maxdepth="<<st.maxdepth<<"\n";
    I p=rat(pn,pd), L=rat(Ln,Ld);
    I theta0=Z(4)*p/(Z(5)-p), M0=Z(3)+theta0;
    if(M0.lower()<=L.upper()){ std::cerr<<"coarse M>L check failed\n"; std::exit(3); }
    std::cout<<"coarse_M_lower="<<M0.lower()<<" endpoint_upper="<<L.upper()<<"\n";
}

int main(){
    std::cout<<"IEEE_INTERVAL_DIRECTED_ROUNDING_CHECK\n";
    run_mode("cross_three_fifths",3,5,3001,1000,999,1000);
    run_mode("two_thirds",2,3,31,10,99,100);
    run_mode("three_quarters",3,4,651,200,99,100);
    std::cout<<"ALL_RIGOROUS_INTERVAL_CHECKS_PASS\n";
}
