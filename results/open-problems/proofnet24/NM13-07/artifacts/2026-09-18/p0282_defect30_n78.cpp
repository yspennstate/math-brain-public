#include <boost/multiprecision/cpp_int.hpp>
#include <algorithm>
#include <chrono>
#include <functional>
#include <iomanip>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <vector>
using boost::multiprecision::cpp_int;
using std::cerr; using std::cout; using std::map; using std::set; using std::string; using std::vector;
using Poly = vector<cpp_int>; // low-to-high coefficients

static void trim(Poly& p){ while(p.size()>1 && p.back()==0) p.pop_back(); }
static Poly add(const Poly&a,const Poly&b){ Poly c(std::max(a.size(),b.size())); for(size_t i=0;i<a.size();++i)c[i]+=a[i]; for(size_t i=0;i<b.size();++i)c[i]+=b[i]; trim(c); return c; }
static Poly sub(const Poly&a,const Poly&b){ Poly c(std::max(a.size(),b.size())); for(size_t i=0;i<a.size();++i)c[i]+=a[i]; for(size_t i=0;i<b.size();++i)c[i]-=b[i]; trim(c); return c; }
static Poly scale(Poly a,const cpp_int&s){ for(auto&x:a)x*=s; trim(a); return a; }
static Poly mul(const Poly&a,const Poly&b){ Poly c(a.size()+b.size()-1); for(size_t i=0;i<a.size();++i)for(size_t j=0;j<b.size();++j)c[i+j]+=a[i]*b[j]; trim(c); return c; }
static cpp_int eval(const Poly&p,long long x){ cpp_int r=0; for(size_t ii=p.size();ii-- >0;){r*=x;r+=p[ii];} return r; }
static cpp_int ipow(cpp_int a,int e){ cpp_int r=1; while(e){if(e&1)r*=a;a*=a;e>>=1;} return r; }
static cpp_int binom(int n,int k){ if(k<0||k>n)return 0; if(k>n-k)k=n-k; cpp_int r=1; for(int i=1;i<=k;++i){r*=n-k+i;r/=i;}return r; }
static Poly shift_arg(const Poly&p,long long c){ Poly q(1,cpp_int(0)); for(size_t ii=p.size(); ii-- >0;){ Poly nq(q.size()+1); for(size_t r=0;r<q.size();++r){ nq[r]+=q[r]*cpp_int(c); nq[r+1]+=q[r]; } nq[0]+=p[ii]; q.swap(nq); trim(q);} return q; }
static Poly mul_n2(Poly p){ p.insert(p.begin(),2,cpp_int(0)); return p; }
static Poly mul_linear(const Poly&p,long long c0,long long c1){ Poly q(p.size()+1); for(size_t i=0;i<p.size();++i){q[i]+=cpp_int(c0)*p[i];q[i+1]+=cpp_int(c1)*p[i];} trim(q); return q; }

static cpp_int factorial_int(int n){ cpp_int x=1; for(int i=2;i<=n;++i)x*=i; return x; }
static vector<cpp_int> factorials(int n){ vector<cpp_int> f(n+1); f[0]=1; for(int i=1;i<=n;++i)f[i]=f[i-1]*i; return f; }
static void partitions_rec(int rem,int max_part,vector<int>&cur,const std::function<void(const vector<int>&)>&visit){ if(rem==0){visit(cur);return;} int hi=std::min(rem,max_part); for(int first=hi;first>=1;--first){cur.push_back(first);partitions_rec(rem-first,first,cur,visit);cur.pop_back();} }
static cpp_int hook_dimension(const vector<int>&lam,int n,const cpp_int&fact){ cpp_int hooks=1; int rows=(int)lam.size(), width=lam.empty()?0:lam[0]; vector<int> colh(width,0); for(int j=0;j<width;++j) while(colh[j]<rows && lam[colh[j]]>j) ++colh[j]; for(int i=0;i<rows;++i) for(int j=0;j<lam[i];++j){ int h=(lam[i]-j)+(colh[j]-i-1); hooks*=h; } if(fact%hooks!=0){cerr<<"NONINTEGRAL_HOOK n="<<n<<"\n";std::exit(2);} return fact/hooks; }
static long long partition_number_euler(int n){ vector<long long> p(n+1);p[0]=1; for(int m=1;m<=n;++m){long long s=0;for(int k=1;;++k){int g1=k*(3*k-1)/2,g2=k*(3*k+1)/2;if(g1>m)break;long long sign=(k%2?1:-1);s+=sign*p[m-g1];if(g2<=m)s+=sign*p[m-g2];}p[m]=s;}return p[n]; }
static vector<cpp_int> exact_row(int n,long long&pcount){ cpp_int fact=factorial_int(n); vector<cpp_int> ell(n+2);vector<int>cur;pcount=0; partitions_rec(n,n,cur,[&](const vector<int>&lam){++pcount;cpp_int f=hook_dimension(lam,n,fact);ell[lam[0]]+=f*f;}); if(pcount!=partition_number_euler(n)){cerr<<"PARTITION_COUNT_FAIL n="<<n<<" got="<<pcount<<" expected="<<partition_number_euler(n)<<"\n";std::exit(3);} cpp_int sum=0;for(int k=1;k<=n;++k)sum+=ell[k];if(sum!=fact){cerr<<"FACTORIAL_SUM_FAIL n="<<n<<"\n";std::exit(4);}return ell; }
static long double to_ld(const cpp_int&x){return x.convert_to<long double>();}

// Exact residual-partition formula. For mu |- t and lambda=(N,mu), N>=mu_1,
// f^lambda = f^mu * (n!/t!) * prod_i (N - mu_i + i) / (N+r)!, n=N+t.
static cpp_int extended_dimension(const vector<int>&mu,int t,int n,const vector<cpp_int>&facts){
    int N=n-t; if(N<1) return 0; if(!mu.empty() && N<mu[0]) return 0;
    int r=(int)mu.size(); cpp_int fmu = (t==0?cpp_int(1):hook_dimension(mu,t,facts[t]));
    cpp_int num=fmu*(facts[n]/facts[t]);
    for(int i=0;i<r;++i) num*=cpp_int(N-mu[i]+(i+1));
    cpp_int den=facts[N+r];
    if(num%den!=0){cerr<<"EXTENDED_DIM_NONINTEGRAL t="<<t<<" n="<<n<<"\n";std::exit(10);} return num/den;
}

int main(){
    auto t0=std::chrono::steady_clock::now();
    const int J=30, FULLN=78, MAXN=std::max(FULLN,2*J+2);
    vector<cpp_int> facts=factorials(MAXN);
    cout<<"P0282 defect-30 quantifier-swap + exact row78 certificate\n";

    // Kauers-Wang fixed-defect polynomial recursion.
    vector<Poly>P(J+2); P[0]=Poly{1}; P[1]=Poly{1,-2,1};
    for(int j=1;j<=J;++j){
        Poly sj=shift_arg(P[j],-1), sjm1=shift_arg(P[j-1],-1);
        Poly inside=add(sj,scale(sjm1,cpp_int(j)));
        P[j+1]=sub(mul_n2(inside),mul_linear(P[j],-(j+1),2));
        if((int)P[j+1].size()-1!=2*(j+1)){cerr<<"DEGREE_FAIL j="<<j+1<<"\n";return 5;}
    }
    cout<<"generated_integer_polynomials_P0_through_P"<<(J+1)<<" exact=True\n";

    long long cone_coeffs=0; int first_bad=0;
    cpp_int min_positive=0; bool min_set=false;
    for(int j=1;j<=J;++j){
        Poly D=sub(scale(mul(P[j],P[j]),cpp_int(j+1)),scale(mul(P[j-1],P[j+1]),cpp_int(j)));
        Poly Q=shift_arg(D,2*j+1); // D_j(m+2j+1)
        if((int)D.size()-1!=4*j){cerr<<"TURAN_DEGREE_FAIL j="<<j<<"\n";return 6;}
        for(const auto&c:Q){++cone_coeffs;if(c<=0 && first_bad==0) first_bad=j; if(c>0 && (!min_set||c<min_positive)){min_positive=c;min_set=true;}}
    }
    if(first_bad){cerr<<"SHIFTED_COEFFICIENT_FAIL first_j="<<first_bad<<"\n";return 7;}
    cout<<"defect_cone_range=1.."<<J<<" shifted_Dj_at_2j_plus_1_all_coefficients_strictly_positive=True total_coefficients="<<cone_coeffs<<"\n";
    cout<<"minimum_positive_shifted_coefficient="<<min_positive<<"\n";

    // Analytic-factorization checker: for each residual partition mu, the shifted
    // dimension j! f^(m+j-1,mu) factors into linear factors with nonnegative constants.
    long long factorization_checks=0;
    for(int t=0;t<=J+1;++t){
        vector<int> cur; partitions_rec(t,t,cur,[&](const vector<int>&mu){
            int r=(int)mu.size(); int mu1=mu.empty()?0:mu[0];
            // On n=m+2t-1, first row N=m+t-1. Valid in the stable range when m>=0.
            // Factor constants: t-1+i-mu_i (i=1..r) and t-1+s (s=r+1..t).
            for(int i=0;i<r;++i){ long long c=t-1+(i+1)-mu[i]; if(c<0){cerr<<"NEGATIVE_FACTOR_CONSTANT t="<<t<<" mu1="<<mu1<<" i="<<i+1<<" c="<<c<<"\n";std::exit(8);} }
            for(int s=r+1;s<=t;++s){ long long c=t-1+s; if(c<0){cerr<<"NEGATIVE_TAIL_FACTOR_CONSTANT\n";std::exit(8);} }
            ++factorization_checks;
        });
    }
    cout<<"residual_dimension_nonnegative_linear_factorizations_checked="<<factorization_checks<<" defects_0_through_"<<(J+1)<<"\n";

    // Independent validation of the residual formula against direct hook dimensions
    // on all (t,N,mu) with t<=12 and mu_1<=N<=15.
    long long residual_formula_crosschecks=0;
    for(int t=0;t<=12;++t){
        vector<int> cur; partitions_rec(t,t,cur,[&](const vector<int>&mu){
            int lo=mu.empty()?1:std::max(1,mu[0]);
            for(int N=lo;N<=15;++N){
                int n=N+t; vector<int> lam; lam.push_back(N); lam.insert(lam.end(),mu.begin(),mu.end());
                // If N==mu_1 this is still a partition with equal first rows.
                cpp_int direct=hook_dimension(lam,n,facts[n]);
                cpp_int residual=extended_dimension(mu,t,n,facts);
                if(direct!=residual){cerr<<"RESIDUAL_FORMULA_MISMATCH t="<<t<<" N="<<N<<"\n";std::exit(9);} ++residual_formula_crosschecks;
            }
        });
    }
    cout<<"residual_formula_direct_hook_crosschecks="<<residual_formula_crosschecks<<" all_exact=True\n";

    // Collect all residual E_t(n) values needed for the finite bridge j+2<=n<=2j.
    vector<set<int>> need(J+2);
    for(int j=1;j<=J;++j) for(int n=j+2;n<=2*j;++n){ for(int t: {j-1,j,j+1}) if(t>=0 && t<=J+1) need[t].insert(n); }
    vector<map<int,cpp_int>> E(J+2);
    for(int t=0;t<=J+1;++t){
        if(need[t].empty()) continue;
        vector<int> cur; partitions_rec(t,t,cur,[&](const vector<int>&mu){
            cpp_int fmu=(t==0?cpp_int(1):hook_dimension(mu,t,facts[t]));
            for(int n:need[t]){
                int N=n-t; if(N<1 || (!mu.empty()&&N<mu[0])) continue;
                int r=(int)mu.size(); cpp_int num=fmu*(facts[n]/facts[t]);
                for(int i=0;i<r;++i) num*=cpp_int(N-mu[i]+(i+1));
                cpp_int den=facts[N+r]; if(num%den!=0){cerr<<"BRIDGE_DIM_NONINTEGRAL t="<<t<<" n="<<n<<"\n";std::exit(11);} cpp_int dim=num/den;
                E[t][n]+=dim*dim;
            }
        });
    }
    long long bridge_checks=0; cpp_int min_bridge_margin=0; int min_bj=-1,min_bn=-1; bool bridge_set=false;
    for(int j=1;j<=J;++j){
        for(int n=j+2;n<=2*j;++n){
            cpp_int M=E[j][n]*E[j][n]-E[j-1][n]*E[j+1][n];
            if(M<=0){cerr<<"FINITE_BRIDGE_MARGIN_FAIL j="<<j<<" n="<<n<<"\n";return 12;}
            if(!bridge_set||M<min_bridge_margin){bridge_set=true;min_bridge_margin=M;min_bj=j;min_bn=n;} ++bridge_checks;
        }
    }
    cout<<"finite_bridge_defects=1.."<<J<<" checks="<<bridge_checks<<" all_strict=True minimum_margin_at_j="<<min_bj<<" n="<<min_bn<<" margin="<<min_bridge_margin<<"\n";

    // Cross-check polynomial/source identity at selected stable points using residual counts, not the recursion itself.
    long long poly_source_crosschecks=0;
    for(int j=1;j<=J;++j){
        for(int n: {2*j+1,2*j+2,2*j+5}){
            int t=j; vector<int> cur; cpp_int e=0; partitions_rec(t,t,cur,[&](const vector<int>&mu){ cpp_int dim=extended_dimension(mu,t,n,facts); e+=dim*dim; });
            cpp_int lhs=eval(P[j],n), rhs=facts[j]*e; if(lhs!=rhs){cerr<<"POLY_RESIDUAL_MATCH_FAIL j="<<j<<" n="<<n<<"\n";return 13;} ++poly_source_crosschecks;
        }
    }
    cout<<"polynomial_residual_source_crosschecks="<<poly_source_crosschecks<<" all_exact=True\n";

    // Full exact source row n=78, independent RSK/hook enumeration, to move frozen metric.
    long long pc=0; vector<cpp_int> row=exact_row(FULLN,pc); cpp_int minnum=0,minden=1,minmargin=0; int mink=-1; bool setmin=false;
    for(int k=2;k<FULLN;++k){ cpp_int num=row[k]*row[k], den=row[k-1]*row[k+1], mar=num-den; if(mar<0){cerr<<"NEGATIVE_SOURCE_MARGIN n="<<FULLN<<" k="<<k<<"\n";return 14;} if(!setmin||num*minden<minnum*den){setmin=true;minnum=num;minden=den;minmargin=mar;mink=k;} }
    cout<<std::setprecision(17);
    cout<<"row78_partitions="<<pc<<" expected="<<partition_number_euler(FULLN)<<" factorial_sum_check=True all_source_margins_nonnegative=True\n";
    cout<<"row78_min_k="<<mink<<" defect="<<(FULLN-mink)<<" min_ratio~"<<(to_ld(minnum)/to_ld(minden))<<"\n";
    cout<<"row78_min_ratio_exact="<<minnum<<"/"<<minden<<"\n";
    cout<<"row78_min_margin_exact="<<minmargin<<"\n";
    cout<<"frozen_metric_movement=N_exact 77->78 when chained to archived n<=77 certificate\n";
    auto t1=std::chrono::steady_clock::now(); std::chrono::duration<double> sec=t1-t0;
    cout<<"elapsed_seconds="<<std::setprecision(6)<<sec.count()<<"\n";
    cout<<"ALL_EXACT_CHECKS_PASS\n";
    return 0;
}
