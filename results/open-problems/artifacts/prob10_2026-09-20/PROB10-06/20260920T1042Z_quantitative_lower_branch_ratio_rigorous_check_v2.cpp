#include <boost/numeric/interval.hpp>
#include <boost/numeric/interval/rounded_arith.hpp>
#include <boost/numeric/interval/utility.hpp>
#include <iostream>
#include <iomanip>
#include <string>
#include <algorithm>
#include <cmath>
#include <vector>
#include <limits>
using I = boost::numeric::interval<double>;

struct Bounds { I rho; double product_hi; I Rlo; I theta; };
static I sq(const I& x){ return x*x; }

Bounds bounds(const I& L, const I& P){
    I R = I(6.0)-I(3.0)*L+L*P;
    I u=(I(3.0)-L)/I(3.0);
    I d2=R/(I(6.0)+L*P);
    I d3=R/(I(6.0)-L+L*P);
    I u2=I(2.0)*(I(3.0)-L)/(L+I(6.0));
    I u3=u;
    I r2=d2/u2, r3=d3/u3;
    I w2=(I(1.0)-P)*r2, w3=P*r3, w0=I(1.0)-w2-w3;
    auto K = [&](const I& base,int j){
        if(j==1){ return w0/base + base*w2/sq(base+u2) + base*w3/sq(base+u3); }
        return w0*w0/base
            + I(2.0)*base*w0*w2/sq(base+u2)
            + I(2.0)*base*w0*w3/sq(base+u3)
            + base*w2*w2/sq(base+I(2.0)*u2)
            + I(2.0)*base*w2*w3/sq(base+u2+u3)
            + base*w3*w3/sq(base+I(2.0)*u3);
    };
    I K1=K(L,1), K2=K(L,2);
    I rho=(I(1.0)-P)*I(2.0)*K1 + P*I(3.0)*K2;
    I A=(I(1.0)-P)*I(6.0)*(I(3.0)-L)/sq(L+I(6.0)) + P*(I(3.0)-L)/I(9.0);
    if(rho.upper()>=1.0) throw 1;
    I eta=A/(I(1.0)-rho);
    I mu=(I(1.0)-P)*d2+P*d3;
    I a=L-I(1.0);
    I D=I(1.0)/a + I(2.0)*eta*K(a,2)/mu - I(3.0)/(I(9.0)-L);
    I Rlo=I(0.75)*(I(1.0)+a*mu/(I(3.0)*u*(a+I(4.0)*u)));
    I theta=P*Rlo/(I(1.0)-P+P*Rlo);
    double two_thirds_safe=std::nextafter(2.0/3.0,std::numeric_limits<double>::infinity());
    if(theta.lower()<=two_thirds_safe) throw 2;
    I t(theta.lower());
    I g=t*(I(1.0)-t)/(I(2.0)+t);
    I prod=I(L.upper())*I(g.upper())*I(D.upper());
    return {rho,prod.upper(),Rlo,theta};
}

struct Node{double a,b,c,d; int depth;};
struct Result{long long visited=0, accepted=0; double worstprod=0,worstrho=0,mintheta=10,minratio=10;};

Result certify(double l0,double l1,double p0,double p1,double q,int maxdepth=28){
    double ninf=-std::numeric_limits<double>::infinity(), pinf=std::numeric_limits<double>::infinity();
    // Expand the requested decimal/rational rectangle outwards by one representable number,
    // so the machine rectangle contains the exact intended endpoints.
    l0=std::nextafter(l0,ninf); l1=std::nextafter(l1,pinf);
    p0=std::nextafter(p0,ninf); p1=std::nextafter(p1,pinf);
    // Compare against a number strictly below the stated exact thresholds.
    double qsafe=std::nextafter(q,ninf), rhosafe=std::nextafter(0.99,ninf);
    std::vector<Node> st; st.push_back({l0,l1,p0,p1,0}); Result out;
    while(!st.empty()){
        auto x=st.back(); st.pop_back(); out.visited++;
        bool good=false; Bounds z;
        try{
            z=bounds(I(x.a,x.b),I(x.c,x.d));
            good=(z.rho.upper()<rhosafe && z.product_hi<qsafe);
        }catch(...){ good=false; }
        if(good){
            out.accepted++;
            out.worstprod=std::max(out.worstprod,z.product_hi);
            out.worstrho=std::max(out.worstrho,z.rho.upper());
            out.mintheta=std::min(out.mintheta,z.theta.lower());
            out.minratio=std::min(out.minratio,z.Rlo.lower());
            continue;
        }
        if(x.depth>=maxdepth){
            std::cerr<<"FAIL depth box "<<std::setprecision(17)
                     <<x.a<<' '<<x.b<<' '<<x.c<<' '<<x.d<<"\n";
            return Result{-1,-1,0,0,0,0};
        }
        if((x.depth%2)==0){
            double m=(x.a+x.b)/2;
            st.push_back({x.a,m,x.c,x.d,x.depth+1});
            st.push_back({m,x.b,x.c,x.d,x.depth+1});
        }else{
            double m=(x.c+x.d)/2;
            st.push_back({x.a,x.b,x.c,m,x.depth+1});
            st.push_back({x.a,x.b,m,x.d,x.depth+1});
        }
    }
    return out;
}

void run(const std::string& name,double l0,double l1,double p0,double p1,double q){
    auto r=certify(l0,l1,p0,p1,q);
    if(r.visited<0) std::exit(2);
    double margin=4.0*(1.0-q)/((3.0+l1)*(3.0+l1));
    std::cout<<name<<"_PASS visited="<<r.visited<<" accepted="<<r.accepted<<"\n";
    std::cout<<std::setprecision(17);
    std::cout<<name<<"_product_upper<"<<q<<" worst_accepted="<<r.worstprod<<"\n";
    std::cout<<name<<"_rho_upper<0.99 worst_accepted="<<r.worstrho<<"\n";
    std::cout<<name<<"_min_theta_lower="<<r.mintheta
             <<" min_ratio_lower="<<r.minratio<<"\n";
    std::cout<<name<<"_derivative_margin_float="<<margin<<"\n";
}

int main(){
    run("A",1.85527,2.0005,47.0/64.0,1.0,0.999);
    run("B",1.85527,2.03,0.75,1.0,0.98);
    run("C",1.85527,2.15,0.8,1.0,0.97);
    std::cout<<"ALL_RIGOROUS_INTERVAL_CHECKS_PASS\n";
    return 0;
}
