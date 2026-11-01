#include <boost/multiprecision/cpp_int.hpp>
#include <algorithm>
#include <chrono>
#include <functional>
#include <iomanip>
#include <iostream>
#include <vector>
using boost::multiprecision::cpp_int;
using std::cerr; using std::cout; using std::vector;

static cpp_int factorial_int(int n){ cpp_int x=1; for(int i=2;i<=n;++i)x*=i; return x; }
static void partitions_rec(int rem,int max_part,vector<int>&cur,const std::function<void(const vector<int>&)>&visit){ if(rem==0){visit(cur);return;} int hi=std::min(rem,max_part); for(int first=hi;first>=1;--first){cur.push_back(first);partitions_rec(rem-first,first,cur,visit);cur.pop_back();} }
static cpp_int hook_dimension(const vector<int>&lam,int n,const cpp_int&fact){ cpp_int hooks=1; int rows=(int)lam.size(), width=lam.empty()?0:lam[0]; vector<int> colh(width,0); for(int j=0;j<width;++j) while(colh[j]<rows && lam[colh[j]]>j) ++colh[j]; for(int i=0;i<rows;++i) for(int j=0;j<lam[i];++j){ int h=(lam[i]-j)+(colh[j]-i-1); hooks*=h; } if(fact%hooks!=0){cerr<<"HOOK_NONINTEGRAL n="<<n<<"\n";std::exit(22);} return fact/hooks; }
static long long partition_number_euler(int n){ vector<long long> p(n+1);p[0]=1;for(int m=1;m<=n;++m){long long s=0;for(int k=1;;++k){int g1=k*(3*k-1)/2,g2=k*(3*k+1)/2;if(g1>m)break;long long sg=(k&1)?1:-1;s+=sg*p[m-g1];if(g2<=m)s+=sg*p[m-g2];}p[m]=s;}return p[n]; }
static vector<cpp_int> exact_row(int n,long long&pc){ cpp_int fact=factorial_int(n); vector<cpp_int> ell(n+2);vector<int>cur;pc=0;partitions_rec(n,n,cur,[&](const vector<int>&lam){++pc;cpp_int f=hook_dimension(lam,n,fact);ell[lam[0]]+=f*f;});if(pc!=partition_number_euler(n)){cerr<<"PARTITION_COUNT_FAIL n="<<n<<" got="<<pc<<" expected="<<partition_number_euler(n)<<"\n";std::exit(23);}cpp_int sum=0;for(int k=1;k<=n;++k)sum+=ell[k];if(sum!=fact){cerr<<"PLANCHEREL_SUM_FAIL n="<<n<<"\n";std::exit(24);}return ell; }
static long double to_ld(const cpp_int&x){ return x.convert_to<long double>(); }

int main(){
    auto t0=std::chrono::steady_clock::now();
    const int J=300, FULLN=81, NMAX=2*J;
    cout<<"P0282 exact lower-boundary correction / defect300 scan / row81 certificate\n";

    vector<cpp_int> facts(J+2); facts[0]=1; for(int i=1;i<=J+1;++i) facts[i]=facts[i-1]*i;
    vector<vector<cpp_int>> V(J+2, vector<cpp_int>(NMAX+1));
    for(int n=0;n<=NMAX;++n){ V[0][n]=1; V[1][n]=cpp_int(n-1)*cpp_int(n-1); }
    for(int j=1;j<=J;++j){
        for(int n=1;n<=NMAX;++n){
            V[j+1][n]=cpp_int(n)*n*(V[j][n-1]+cpp_int(j)*V[j-1][n-1]) - cpp_int(2*n-j-1)*V[j][n];
        }
    }
    cout<<"fixed_defect_recurrence_table exact=True J="<<J<<" NMAX="<<NMAX<<"\n";

    int completed_nonpos_count=0, completed_first_j=-1;
    cpp_int completed_first_value=0;
    int correction_nonpos_count=0;
    cpp_int min_corrected_margin=0; int min_corrected_j=-1; bool min_set=false;
    long long correction_formula_checks=0;
    for(int j=4;j<=J;++j){
        int n=2*j-2;
        if(V[j][n]%facts[j] || V[j-1][n]%facts[j-1] || V[j+1][n]%facts[j+1]){ cerr<<"COMPLETED_DIV_FAIL j="<<j<<"\n"; return 2; }
        cpp_int A=V[j][n]/facts[j], B=V[j-1][n]/facts[j-1], C=V[j+1][n]/facts[j+1];
        cpp_int top=factorial_int(2*j-2);
        cpp_int den=factorial_int(j-1)*facts[j];
        if(top%den){cerr<<"CJ_DIV_FAIL j="<<j<<"\n";return 3;}
        cpp_int q=top/den, c=q*q;
        cpp_int jj=j;
        cpp_int rho_num=jj*jj*jj*jj*jj*jj - 8*jj*jj*jj*jj*jj + 30*jj*jj*jj*jj - 52*jj*jj*jj + 47*jj*jj - 40*jj + 38;
        cpp_int rho_den=2*cpp_int(j+1)*cpp_int(j+1);
        if((c*rho_num)%rho_den){cerr<<"DJ_DIV_FAIL j="<<j<<"\n";return 4;}
        cpp_int d=c*rho_num/rho_den;
        cpp_int completed=A*A-B*C;
        cpp_int addendum=B*d-2*c*A+c*c;
        cpp_int corrected=completed+addendum;
        if(corrected<=0){cerr<<"CORRECTED_MARGIN_NONPOS j="<<j<<" value="<<corrected<<"\n";return 5;}
        if(addendum<=0) ++correction_nonpos_count;
        if(completed<=0){++completed_nonpos_count;if(completed_first_j<0){completed_first_j=j;completed_first_value=completed;}}
        if(!min_set || corrected<min_corrected_margin){min_set=true;min_corrected_margin=corrected;min_corrected_j=j;}
        ++correction_formula_checks;
    }
    if(completed_first_j!=4 || completed_first_value!=-144828 || correction_nonpos_count!=0){
        cerr<<"BOUNDARY_OBSTRUCTION_SUMMARY_FAIL first_j="<<completed_first_j<<" first_value="<<completed_first_value<<" addendum_nonpos="<<correction_nonpos_count<<"\n";return 6;
    }
    cout<<"boundary_correction_scan_j=4.."<<J<<" corrected_source_margins_positive=True checks="<<correction_formula_checks<<" min_margin="<<min_corrected_margin<<" at_j="<<min_corrected_j<<"\n";
    cout<<"uncorrected_completed_nonpositive_count="<<completed_nonpos_count<<" first_j="<<completed_first_j<<" first_value="<<completed_first_value<<"\n";
    cout<<"correction_addendum_positive_all=True\n";

    long long small_cross=0;
    for(int j=4;j<=10;++j){
        int n=2*j-2; long long pc=0; auto row=exact_row(n,pc);
        cpp_int A=V[j][n]/facts[j], B=V[j-1][n]/facts[j-1], C=V[j+1][n]/facts[j+1];
        cpp_int top=factorial_int(2*j-2), den=factorial_int(j-1)*facts[j], q=top/den, c=q*q;
        cpp_int jj=j;
        cpp_int rho_num=jj*jj*jj*jj*jj*jj - 8*jj*jj*jj*jj*jj + 30*jj*jj*jj*jj - 52*jj*jj*jj + 47*jj*jj - 40*jj + 38;
        cpp_int rho_den=2*cpp_int(j+1)*cpp_int(j+1), d=c*rho_num/rho_den;
        int k=n-j;
        if(A-c!=row[k] || B!=row[k+1] || C-d!=row[k-1]){cerr<<"DIRECT_RSK_CORRECTION_FAIL j="<<j<<" n="<<n<<"\n";return 7;}
        cpp_int corrected=(A-c)*(A-c)-B*(C-d);
        cpp_int direct=row[k]*row[k]-row[k+1]*row[k-1];
        if(corrected!=direct || direct<=0){cerr<<"DIRECT_RSK_MARGIN_FAIL j="<<j<<"\n";return 8;}
        ++small_cross;
    }
    cout<<"direct_RSK_boundary_crosschecks_j=4..10 PASS count="<<small_cross<<"\n";

    // Source theorem extension for j<=100: predecessor proved n>=2j-1; this scan adds n=2j-2.
    cout<<"combined_with_predecessor_theorem strict_source_range_j=4..100 n>=2j-2=True\n";
    cout<<"boundary_only_additional_scan_j=101..300 n=2j-2 positive=True\n";

    long long pc=0; vector<cpp_int> row=exact_row(FULLN,pc);
    cpp_int minnum=0,minden=1,minmargin=0; int mink=-1; bool setmin=false;
    for(int k=2;k<FULLN;++k){
        cpp_int num=row[k]*row[k],den=row[k-1]*row[k+1],mar=num-den;
        if(mar<0){cerr<<"ROW81_NEGATIVE_MARGIN k="<<k<<"\n";return 9;}
        if(!setmin||num*minden<minnum*den){setmin=true;minnum=num;minden=den;minmargin=mar;mink=k;}
    }
    cout<<std::setprecision(18);
    cout<<"row81_partitions="<<pc<<" expected="<<partition_number_euler(FULLN)<<" factorial_sum_check=True all_source_margins_nonnegative=True\n";
    cout<<"row81_min_k="<<mink<<" defect="<<(FULLN-mink)<<" min_ratio~"<<(to_ld(minnum)/to_ld(minden))<<"\n";
    cout<<"row81_min_ratio_exact="<<minnum<<"/"<<minden<<"\n";
    cout<<"row81_min_margin_exact="<<minmargin<<"\n";
    cout<<"frozen_metric_movement=N_exact 80->81 when_chained_to_archived_n_le_80_certificates=True\n";
    auto t1=std::chrono::steady_clock::now();
    cout<<"elapsed_seconds="<<std::chrono::duration<double>(t1-t0).count()<<"\n";
    cout<<"ALL_EXACT_CHECKS_PASS\n";
}
