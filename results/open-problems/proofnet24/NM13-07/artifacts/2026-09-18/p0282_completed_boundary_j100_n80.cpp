#include <boost/multiprecision/cpp_int.hpp>
#include <algorithm>
#include <chrono>
#include <functional>
#include <iomanip>
#include <iostream>
#include <vector>
using boost::multiprecision::cpp_int;
using std::cerr; using std::cout; using std::vector;
using Poly = vector<cpp_int>;

static void trim(Poly& p){ while(p.size()>1 && p.back()==0) p.pop_back(); }
static Poly add(const Poly&a,const Poly&b){ Poly c(std::max(a.size(),b.size())); for(size_t i=0;i<a.size();++i)c[i]+=a[i]; for(size_t i=0;i<b.size();++i)c[i]+=b[i]; trim(c); return c; }
static Poly sub(const Poly&a,const Poly&b){ Poly c(std::max(a.size(),b.size())); for(size_t i=0;i<a.size();++i)c[i]+=a[i]; for(size_t i=0;i<b.size();++i)c[i]-=b[i]; trim(c); return c; }
static Poly scale(Poly a,const cpp_int&s){ for(auto&x:a)x*=s; trim(a); return a; }
static Poly mul(const Poly&a,const Poly&b){ Poly c(a.size()+b.size()-1); for(size_t i=0;i<a.size();++i) if(a[i]!=0) for(size_t j=0;j<b.size();++j) if(b[j]!=0)c[i+j]+=a[i]*b[j]; trim(c); return c; }
static cpp_int eval(const Poly&p,long long x){ cpp_int r=0; for(size_t ii=p.size();ii-- >0;){r*=x;r+=p[ii];} return r; }
static Poly shift_arg(const Poly&p,long long c){ Poly q(1,cpp_int(0)); for(size_t ii=p.size();ii-- >0;){ Poly nq(q.size()+1); for(size_t r=0;r<q.size();++r){ nq[r]+=q[r]*cpp_int(c); nq[r+1]+=q[r]; } nq[0]+=p[ii]; q.swap(nq); trim(q);} return q; }
static Poly mul_n2(Poly p){ p.insert(p.begin(),2,cpp_int(0)); return p; }
static Poly mul_linear(const Poly&p,long long c0,long long c1){ Poly q(p.size()+1); for(size_t i=0;i<p.size();++i){q[i]+=cpp_int(c0)*p[i];q[i+1]+=cpp_int(c1)*p[i];} trim(q); return q; }
static Poly div_x_minus_r(const Poly&p,long long r){ if(p.size()<2){cerr<<"DIV_DEG_FAIL\n";std::exit(20);} int d=(int)p.size()-1; Poly q(d); q[d-1]=p[d]; for(int k=d-1;k>=1;--k) q[k-1]=p[k]+cpp_int(r)*q[k]; cpp_int rem=p[0]+cpp_int(r)*q[0]; if(rem!=0){cerr<<"DIV_REMAINDER_FAIL r="<<r<<" rem="<<rem<<"\n";std::exit(21);} trim(q); return q; }
static cpp_int factorial_int(int n){ cpp_int x=1; for(int i=2;i<=n;++i)x*=i; return x; }
static void partitions_rec(int rem,int max_part,vector<int>&cur,const std::function<void(const vector<int>&)>&visit){ if(rem==0){visit(cur);return;} int hi=std::min(rem,max_part); for(int first=hi;first>=1;--first){cur.push_back(first);partitions_rec(rem-first,first,cur,visit);cur.pop_back();} }
static cpp_int hook_dimension(const vector<int>&lam,int n,const cpp_int&fact){ cpp_int hooks=1; int rows=(int)lam.size(), width=lam.empty()?0:lam[0]; vector<int> colh(width,0); for(int j=0;j<width;++j) while(colh[j]<rows && lam[colh[j]]>j) ++colh[j]; for(int i=0;i<rows;++i) for(int j=0;j<lam[i];++j){ int h=(lam[i]-j)+(colh[j]-i-1); hooks*=h; } if(fact%hooks!=0){cerr<<"HOOK_NONINTEGRAL n="<<n<<"\n";std::exit(22);} return fact/hooks; }
static long long partition_number_euler(int n){ vector<long long> p(n+1);p[0]=1;for(int m=1;m<=n;++m){long long s=0;for(int k=1;;++k){int g1=k*(3*k-1)/2,g2=k*(3*k+1)/2;if(g1>m)break;long long sg=(k&1)?1:-1;s+=sg*p[m-g1];if(g2<=m)s+=sg*p[m-g2];}p[m]=s;}return p[n]; }
static vector<cpp_int> exact_row(int n,long long&pc){ cpp_int fact=factorial_int(n); vector<cpp_int> ell(n+2);vector<int>cur;pc=0;partitions_rec(n,n,cur,[&](const vector<int>&lam){++pc;cpp_int f=hook_dimension(lam,n,fact);ell[lam[0]]+=f*f;});if(pc!=partition_number_euler(n)){cerr<<"PARTITION_COUNT_FAIL n="<<n<<" got="<<pc<<" expected="<<partition_number_euler(n)<<"\n";std::exit(23);}cpp_int sum=0;for(int k=1;k<=n;++k)sum+=ell[k];if(sum!=fact){cerr<<"PLANCHEREL_SUM_FAIL n="<<n<<"\n";std::exit(24);}return ell; }
static long double to_ld(const cpp_int&x){ return x.convert_to<long double>(); }

int main(){
    auto t0=std::chrono::steady_clock::now();
    const int J=100, FULLN=80;
    cout<<"P0282 completed-residual boundary transfer / defect100 / row80 exact certificate\n";

    vector<Poly>P(J+2); P[0]=Poly{1}; P[1]=Poly{1,-2,1};
    for(int j=1;j<=J;++j){
        Poly inside=add(shift_arg(P[j],-1),scale(shift_arg(P[j-1],-1),cpp_int(j)));
        P[j+1]=sub(mul_n2(inside),mul_linear(P[j],-(j+1),2));
        if((int)P[j+1].size()-1!=2*(j+1) || P[j+1].back()!=1){cerr<<"P_DEG_MONIC_FAIL j="<<j+1<<"\n";return 2;}
    }
    cout<<"generated_P0_through_P"<<(J+1)<<" exact_integer_polynomials=True\n";

    long long boundary_coeffs=0;
    cpp_int boundary_global_min=0; bool boundary_set=false; int boundary_min_j=-1,boundary_min_i=-1;
    int lower_first_j=-1,lower_first_i=-1; cpp_int lower_first_value=0;
    for(int j=4;j<=J;++j){
        Poly D=sub(scale(mul(P[j],P[j]),cpp_int(j+1)),scale(mul(P[j-1],P[j+1]),cpp_int(j)));
        int q=(j+1)/2; Poly H=D;
        for(int r=0;r<q;++r){ if(eval(D,r)!=0){cerr<<"FORCED_ROOT_FAIL j="<<j<<" r="<<r<<"\n";return 3;} H=div_x_minus_r(H,r); }
        Poly HB=shift_arg(H,2*j-1);
        for(size_t i=0;i<HB.size();++i){
            ++boundary_coeffs;
            if(HB[i]<=0){cerr<<"BOUNDARY_COEFF_NONPOSITIVE j="<<j<<" i="<<i<<" value="<<HB[i]<<"\n";return 4;}
            if(!boundary_set || HB[i]<boundary_global_min){boundary_set=true;boundary_global_min=HB[i];boundary_min_j=j;boundary_min_i=(int)i;}
        }
        if(lower_first_j<0){
            Poly HL=shift_arg(H,2*j-2);
            for(size_t i=0;i<HL.size();++i) if(HL[i]<=0){lower_first_j=j;lower_first_i=(int)i;lower_first_value=HL[i];break;}
        }
    }
    if(lower_first_j!=4 || lower_first_i!=0 || lower_first_value!=cpp_int(-13903488)){
        cerr<<"LOWER_SHIFT_OBSTRUCTION_MISMATCH j="<<lower_first_j<<" i="<<lower_first_i<<" value="<<lower_first_value<<"\n";return 5;
    }
    cout<<"forced_factor_quotient_shift_n=m+2j-1 positive_coefficients range_j=4.."<<J
        <<" total="<<boundary_coeffs<<" global_min="<<boundary_global_min<<" at_j="<<boundary_min_j<<" coeff_index="<<boundary_min_i<<"\n";
    cout<<"one_step_lower_shift_n=m+2j-2 first_nonpositive_j="<<lower_first_j<<" coeff_index="<<lower_first_i<<" value="<<lower_first_value<<" exact=True\n";

    long long pc6=0; vector<cpp_int> row6=exact_row(6,pc6);
    cpp_int e3=row6[3],e4=row6[2],e5=row6[1];
    cpp_int t3=eval(P[3],6)/factorial_int(3), t4=eval(P[4],6)/factorial_int(4), t5=eval(P[5],6)/factorial_int(5);
    if(e3!=381 || e4!=131 || e5!=1 || t3!=381 || t4!=156 || t5!=444){cerr<<"N6_COMPLETED_SOURCE_VALUES_FAIL\n";return 6;}
    cpp_int source_margin=e4*e4-e3*e5;
    cpp_int completed_margin=t4*t4-t3*t5;
    if(source_margin!=16780 || completed_margin!=-144828 || t4-e4!=25){cerr<<"N6_OBSTRUCTION_MARGIN_FAIL\n";return 7;}
    cpp_int cj=factorial_int(6)/(factorial_int(3)*factorial_int(4)); cj*=cj;
    if(cj!=25){cerr<<"EXTREMAL_CORRECTION_FAIL\n";return 8;}
    cout<<"lower_boundary_exact_obstruction j=4 n=6 source_E3_E4_E5="<<e3<<","<<e4<<","<<e5
        <<" completed="<<t3<<","<<t4<<","<<t5<<" source_margin="<<source_margin
        <<" completed_margin="<<completed_margin<<" extremal_mu=(4)_correction="<<cj<<"\n";

    long long pc=0; vector<cpp_int> row=exact_row(FULLN,pc);
    cpp_int minnum=0,minden=1,minmargin=0; int mink=-1; bool setmin=false;
    for(int k=2;k<FULLN;++k){
        cpp_int num=row[k]*row[k],den=row[k-1]*row[k+1],mar=num-den;
        if(mar<0){cerr<<"ROW80_NEGATIVE_MARGIN k="<<k<<"\n";return 9;}
        if(!setmin||num*minden<minnum*den){setmin=true;minnum=num;minden=den;minmargin=mar;mink=k;}
    }
    cout<<std::setprecision(18);
    cout<<"row80_partitions="<<pc<<" expected="<<partition_number_euler(FULLN)<<" factorial_sum_check=True all_source_margins_nonnegative=True\n";
    cout<<"row80_min_k="<<mink<<" defect="<<(FULLN-mink)<<" min_ratio~"<<(to_ld(minnum)/to_ld(minden))<<"\n";
    cout<<"row80_min_ratio_exact="<<minnum<<"/"<<minden<<"\n";
    cout<<"row80_min_margin_exact="<<minmargin<<"\n";
    cout<<"frozen_metric_movement=N_exact 79->80 when_chained_to_archived_n_le_79_certificates=True\n";
    auto t1=std::chrono::steady_clock::now();
    cout<<"elapsed_seconds="<<std::chrono::duration<double>(t1-t0).count()<<"\n";
    cout<<"ALL_EXACT_CHECKS_PASS\n";
}
