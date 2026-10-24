#include <boost/multiprecision/cpp_int.hpp>
#include <algorithm>
#include <chrono>
#include <functional>
#include <iomanip>
#include <iostream>
#include <string>
#include <vector>
using boost::multiprecision::cpp_int;
using std::cerr; using std::cout; using std::string; using std::vector;

using Poly = vector<cpp_int>; // low-to-high coefficients

static void trim(Poly& p){ while(p.size()>1 && p.back()==0) p.pop_back(); }
static Poly add(const Poly&a,const Poly&b){ Poly c(std::max(a.size(),b.size())); for(size_t i=0;i<a.size();++i)c[i]+=a[i]; for(size_t i=0;i<b.size();++i)c[i]+=b[i]; trim(c); return c; }
static Poly sub(const Poly&a,const Poly&b){ Poly c(std::max(a.size(),b.size())); for(size_t i=0;i<a.size();++i)c[i]+=a[i]; for(size_t i=0;i<b.size();++i)c[i]-=b[i]; trim(c); return c; }
static Poly scale(Poly a,const cpp_int&s){ for(auto&x:a)x*=s; trim(a); return a; }
static Poly mul(const Poly&a,const Poly&b){ Poly c(a.size()+b.size()-1); for(size_t i=0;i<a.size();++i)for(size_t j=0;j<b.size();++j)c[i+j]+=a[i]*b[j]; trim(c); return c; }
static cpp_int eval(const Poly&p,long long x){ cpp_int r=0; for(size_t ii=p.size();ii-- >0;){r*=x;r+=p[ii];} return r; }
static cpp_int ipow(cpp_int a,int e){ cpp_int r=1; while(e){if(e&1)r*=a;a*=a;e>>=1;} return r; }
static cpp_int binom(int n,int k){ if(k<0||k>n)return 0; if(k>n-k)k=n-k; cpp_int r=1; for(int i=1;i<=k;++i){r*=n-k+i;r/=i;}return r; }
static Poly shift_arg(const Poly&p,long long c){ // p(x+c)
    Poly q(p.size());
    for(int i=0;i<(int)p.size();++i){
        for(int r=0;r<=i;++r){ q[r]+=p[i]*binom(i,r)*ipow(cpp_int(c),i-r); }
    }
    trim(q); return q;
}
static Poly mul_n2(Poly p){ p.insert(p.begin(),2,cpp_int(0)); return p; }
static Poly mul_linear(const Poly&p,long long c0,long long c1){ // (c0+c1*n)p
    Poly q(p.size()+1); for(size_t i=0;i<p.size();++i){q[i]+=cpp_int(c0)*p[i];q[i+1]+=cpp_int(c1)*p[i];} trim(q); return q;
}

static cpp_int factorial_int(int n){ cpp_int x=1; for(int i=2;i<=n;++i)x*=i; return x; }
static void partitions_rec(int rem,int max_part,vector<int>&cur,const std::function<void(const vector<int>&)>&visit){
    if(rem==0){visit(cur);return;} int hi=std::min(rem,max_part);
    for(int first=hi;first>=1;--first){cur.push_back(first);partitions_rec(rem-first,first,cur,visit);cur.pop_back();}
}
static cpp_int hook_dimension(const vector<int>&lam,int n,const cpp_int&fact){
    cpp_int hooks=1; int rows=(int)lam.size(), width=lam.empty()?0:lam[0]; vector<int> colh(width,0);
    for(int j=0;j<width;++j) while(colh[j]<rows && lam[colh[j]]>j) ++colh[j];
    for(int i=0;i<rows;++i) for(int j=0;j<lam[i];++j){ int h=(lam[i]-j)+(colh[j]-i-1); hooks*=h; }
    cpp_int q=fact/hooks; if(q*hooks!=fact){cerr<<"NONINTEGRAL_HOOK n="<<n<<"\n";std::exit(2);} return q;
}
static long long partition_number_euler(int n){ vector<long long> p(n+1);p[0]=1; for(int m=1;m<=n;++m){long long s=0;for(int k=1;;++k){int g1=k*(3*k-1)/2,g2=k*(3*k+1)/2;if(g1>m)break;long long sign=(k%2?1:-1);s+=sign*p[m-g1];if(g2<=m)s+=sign*p[m-g2];}p[m]=s;}return p[n]; }
static vector<cpp_int> exact_row(int n,long long&pcount){ cpp_int fact=factorial_int(n); vector<cpp_int> ell(n+2);vector<int>cur;pcount=0; partitions_rec(n,n,cur,[&](const vector<int>&lam){++pcount;cpp_int f=hook_dimension(lam,n,fact);ell[lam[0]]+=f*f;}); if(pcount!=partition_number_euler(n)){cerr<<"PARTITION_COUNT_FAIL n="<<n<<" got="<<pcount<<" expected="<<partition_number_euler(n)<<"\n";std::exit(3);} cpp_int sum=0;for(int k=1;k<=n;++k)sum+=ell[k];if(sum!=fact){cerr<<"FACTORIAL_SUM_FAIL n="<<n<<"\n";std::exit(4);}return ell; }
static long double to_ld(const cpp_int&x){return x.convert_to<long double>();}

int main(){
    auto t0=std::chrono::steady_clock::now();
    cout<<"P0282 fixed-defect polynomial-cone + exact row77 certificate\n";
    const int J=20;
    vector<Poly>P(J+2);
    P[0]=Poly{1}; P[1]=Poly{1,-2,1}; // (n-1)^2
    for(int j=1;j<=J;++j){
        Poly sj=shift_arg(P[j],-1), sjm1=shift_arg(P[j-1],-1);
        Poly inside=add(sj,scale(sjm1,cpp_int(j)));
        Poly term1=mul_n2(inside);
        Poly term2=mul_linear(P[j],-(j+1),2); // (2n-j-1)P_j
        P[j+1]=sub(term1,term2);
        if((int)P[j+1].size()-1!=2*(j+1)){cerr<<"DEGREE_FAIL j="<<j+1<<"\n";return 5;}
    }
    cout<<"generated_integer_polynomials_P0_through_P"<<(J+1)<<" exact=True\n";

    for(int j=1;j<=J;++j){
        Poly D=sub(scale(mul(P[j],P[j]),cpp_int(j+1)),scale(mul(P[j-1],P[j+1]),cpp_int(j)));
        Poly Q=shift_arg(D,2*j+1); // D_j(m+2j+1)
        int nonpos=0; for(const auto&c:Q) if(c<=0) ++nonpos;
        if(nonpos){cerr<<"SHIFTED_COEFFICIENT_FAIL j="<<j<<" nonpositive="<<nonpos<<"\n";return 6;}
        cout<<"defect="<<j<<" D_degree="<<(D.size()-1)<<" shifted_at="<<(2*j+1)<<" all_coefficients_strictly_positive=True coefficient_count="<<Q.size()<<"\n";
    }

    // Exact finite bridge: for defect j, polynomial identification via KW2 is only used at n>=2j+1.
    // Check every smaller source-valid n, j+2 <= n <= 2j, by independent RSK/hook enumeration.
    vector<vector<cpp_int>> small(2*J+1);
    long long bridge_checks=0, poly_matches=0;
    for(int nn=1;nn<=2*J;++nn){ long long pc=0; small[nn]=exact_row(nn,pc); }
    for(int j=1;j<=J;++j){
        for(int nn=j+2;nn<=2*j;++nn){
            int k=nn-j;
            cpp_int M=small[nn][k]*small[nn][k]-small[nn][k-1]*small[nn][k+1];
            if(M<=0){cerr<<"FINITE_BRIDGE_MARGIN_FAIL j="<<j<<" n="<<nn<<" k="<<k<<"\n";return 7;}
            ++bridge_checks;
        }
        // Sanity-check polynomial/source identification wherever both fit within n<=40.
        for(int nn=2*j-1;nn<=2*J;++nn){
            if(nn<j+1) continue;
            int k=nn-j; if(k<1||k>nn)continue;
            cpp_int pj=eval(P[j],nn), factj=factorial_int(j);
            if(pj != factj*small[nn][k]){cerr<<"POLY_SOURCE_MATCH_FAIL j="<<j<<" n="<<nn<<"\n";return 8;}
            ++poly_matches;
        }
    }
    cout<<"finite_prepolynomial_bridge_checks="<<bridge_checks<<" all_strict=True range_defects=1..20\n";
    cout<<"polynomial_source_crosschecks_n_le_40="<<poly_matches<<" all_exact=True\n";

    // Full source row n=77, independent exact RSK/hook arithmetic.
    long long pc77=0; vector<cpp_int> e77=exact_row(77,pc77); cpp_int minnum=0,minden=1,minmargin=0; int mink=-1; bool set=false;
    for(int k=2;k<77;++k){cpp_int num=e77[k]*e77[k],den=e77[k-1]*e77[k+1],mar=num-den;if(mar<0){cerr<<"NEGATIVE_SOURCE_MARGIN n=77 k="<<k<<"\n";return 9;}if(!set||num*minden<minnum*den){set=true;minnum=num;minden=den;minmargin=mar;mink=k;}}
    cout<<std::setprecision(17);
    cout<<"row77_partitions="<<pc77<<" expected="<<partition_number_euler(77)<<" factorial_sum_check=True all_source_margins_nonnegative=True\n";
    cout<<"row77_min_k="<<mink<<" min_ratio~"<<(to_ld(minnum)/to_ld(minden))<<"\n";
    cout<<"row77_min_ratio_exact="<<minnum<<"/"<<minden<<"\n";
    cout<<"row77_min_margin_exact="<<minmargin<<"\n";
    cout<<"frozen_metric_movement=N_exact 76->77 when chained to archived n<=76 certificate\n";
    auto t1=std::chrono::steady_clock::now(); std::chrono::duration<double> sec=t1-t0;
    cout<<"elapsed_seconds="<<std::setprecision(6)<<sec.count()<<"\n";
    cout<<"ALL_EXACT_CHECKS_PASS\n";
    return 0;
}
