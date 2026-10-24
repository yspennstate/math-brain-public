#include <boost/multiprecision/cpp_int.hpp>
#include <algorithm>
#include <chrono>
#include <functional>
#include <iomanip>
#include <iostream>
#include <vector>
using boost::multiprecision::cpp_int;
using std::cerr; using std::cout; using std::vector;

static cpp_int factorial_int(int n){ cpp_int x=1; for(int i=2;i<=n;++i) x*=i; return x; }
static cpp_int hook_dimension(const vector<int>& lam, int n, const cpp_int& fact){
    if(lam.empty()) return 1; int rows=(int)lam.size(), width=lam[0]; vector<int> colh(width,0);
    for(int c=0;c<width;++c) while(colh[c]<rows && lam[colh[c]]>c) ++colh[c];
    cpp_int hooks=1; for(int i=0;i<rows;++i) for(int c=0;c<lam[i];++c) hooks *= (lam[i]-c)+(colh[c]-i-1);
    if(fact%hooks!=0){ cerr<<"HOOK_DIV_FAIL n="<<n<<"\n"; std::exit(2); } return fact/hooks;
}
static void all_partitions_rec(int rem,int maxp,vector<int>&cur,const std::function<void(const vector<int>&)>&visit){
    if(rem==0){visit(cur);return;} int hi=std::min(rem,maxp); for(int a=hi;a>=1;--a){cur.push_back(a);all_partitions_rec(rem-a,a,cur,visit);cur.pop_back();}
}
static long long partition_number_euler(int n){
    vector<long long> p(n+1); p[0]=1; for(int m=1;m<=n;++m){ long long s=0; for(int k=1;;++k){
        int g1=k*(3*k-1)/2,g2=k*(3*k+1)/2; if(g1>m)break; long long sg=(k&1)?1:-1; s+=sg*p[m-g1]; if(g2<=m)s+=sg*p[m-g2]; } p[m]=s; } return p[n];
}
static vector<cpp_int> exact_row(int n,long long& pc){
    cpp_int fact=factorial_int(n); vector<cpp_int> ell(n+2); vector<int>cur; pc=0;
    all_partitions_rec(n,n,cur,[&](const vector<int>&lam){++pc; cpp_int f=hook_dimension(lam,n,fact);ell[lam[0]]+=f*f;});
    if(pc!=partition_number_euler(n)){cerr<<"PARTITION_COUNT_FAIL n="<<n<<" got="<<pc<<" expected="<<partition_number_euler(n)<<"\n";std::exit(3);} cpp_int sum=0;for(int k=1;k<=n;++k)sum+=ell[k];
    if(sum!=fact){cerr<<"PLANCHEREL_SUM_FAIL n="<<n<<"\n";std::exit(4);} return ell;
}
struct TailPartition { vector<int> lam; cpp_int f; };
static void tail_partitions_rec(int rem,int maxp,vector<int>&cur,vector<TailPartition>&out){
    if(rem==0){ int r=0; for(int x:cur)r+=x; out.push_back({cur,hook_dimension(cur,r,factorial_int(r))}); return; }
    int hi=std::min(rem,maxp);for(int a=hi;a>=1;--a){cur.push_back(a);tail_partitions_rec(rem-a,a,cur,out);cur.pop_back();}
}
static long double to_ld(const cpp_int& x){return x.convert_to<long double>();}

int main(){
    auto t0=std::chrono::steady_clock::now();
    const int N=84,SOLD=40,SNEW=47,J=66,NMAX=2*J;
    cout<<"P0282 combined exact certificate: complete row 84 plus adaptive depth-frontier seam through j=66\n";

    long long pc=0; auto row=exact_row(N,pc); cpp_int min_num=0,min_den=1,min_margin=0; int min_k=-1; bool rset=false;
    for(int k=2;k<N;++k){ cpp_int num=row[k]*row[k],den=row[k-1]*row[k+1],m=num-den; if(m<0){cerr<<"ROW84_NEG k="<<k<<"\n";return 5;}
        if(!rset||num*min_den<min_num*den){rset=true;min_num=num;min_den=den;min_margin=m;min_k=k;} }
    cout<<std::setprecision(18);
    cout<<"row84_partitions="<<pc<<" expected="<<partition_number_euler(N)<<" factorial_sum_check=True all_source_margins_nonnegative=True\n";
    cout<<"row84_min_k="<<min_k<<" defect="<<(N-min_k)<<" min_ratio~"<<(to_ld(min_num)/to_ld(min_den))<<"\n";
    cout<<"row84_min_ratio_exact="<<min_num<<"/"<<min_den<<"\n";
    cout<<"row84_min_margin_exact="<<min_margin<<"\n";
    cout<<"frozen_metric_movement=N_exact 83->84 when_chained_to_archived_n_le_83_certificates=True\n";

    int complete=(N+SNEW+1)/2;
    cout<<"coverage_formula=floor((N+S+1)/2) N="<<N<<" S="<<SNEW<<" gives_complete_defect_through="<<complete<<"\n";
    if(complete!=J){cerr<<"COVERAGE_ARITH_FAIL\n";return 6;}

    vector<cpp_int> F(J+3); F[0]=1;for(int i=1;i<(int)F.size();++i)F[i]=F[i-1]*i;
    vector<vector<cpp_int>> V(J+2,vector<cpp_int>(NMAX+1));
    for(int n=0;n<=NMAX;++n){V[0][n]=1;V[1][n]=cpp_int(n-1)*(n-1);} for(int q=1;q<=J;++q)for(int n=1;n<=NMAX;++n)
        V[q+1][n]=cpp_int(n)*n*(V[q][n-1]+cpp_int(q)*V[q-1][n-1])-cpp_int(2*n-q-1)*V[q][n];

    vector<vector<TailPartition>> tails(SNEW+3);vector<int>cur;long long tail_shapes=0;for(int r=0;r<=SNEW+2;++r){tail_partitions_rec(r,r,cur,tails[r]);tail_shapes+=tails[r].size();}
    cout<<"tail_partition_atlas r=0.."<<(SNEW+2)<<" shapes="<<tail_shapes<<"\n";
    long long amp_terms=0;
    auto completion_error=[&](int j,int t,int s)->cpp_int{
        int q=j+t,n=2*j-s,Ntail=n-q,rmax=s+2*t-2;if(rmax<0)return cpp_int(0);cpp_int total=0;
        for(int r=0;r<=rmax;++r){int M=q-r;for(const auto&tt:tails[r]){if(r&&M<tt.lam[0])continue;cpp_int dim_num=tt.f;
            for(int a=1;a<=r;++a){int la=(a-1<(int)tt.lam.size())?tt.lam[a-1]:0;dim_num*=M+a-la;}if(dim_num%F[r]!=0){cerr<<"TAIL_DIM_DIV_FAIL\n";std::exit(7);}cpp_int fmu=dim_num/F[r];
            cpp_int R=Ntail+1-M;for(int a=1;a<=r;++a){int la=(a-1<(int)tt.lam.size())?tt.lam[a-1]:0;R*=Ntail+a+1-la;}for(int i=r+2;i<=q;++i)R*=Ntail+i;if(R==0)continue;
            cpp_int num=fmu*R;if(num%F[q]!=0){cerr<<"TAIL_AMP_DIV_FAIL q="<<q<<" j="<<j<<" t="<<t<<" s="<<s<<" r="<<r<<"\n";std::exit(8);}cpp_int amp=num/F[q];total+=amp*amp;++amp_terms; }}return total; };

    long long seam_checks=0;cpp_int seam_min=0;int minj=-1,mins=-1,minn=-1;bool sset=false;
    int depth_counts[SNEW+1]={0};
    for(int s=SOLD+1;s<=SNEW;++s)for(int j=4;j<=J;++j){int n=2*j-s;if(n<j+2||n<=N)continue;cpp_int E[3];
        for(int t=-1;t<=1;++t){int q=j+t;if(V[q][n]%F[q]!=0){cerr<<"COMP_DIV_FAIL\n";return 9;}E[t+1]=V[q][n]/F[q]-completion_error(j,t,s);if(E[t+1]<0){cerr<<"NEG_SOURCE_COUNT\n";return 10;}}
        cpp_int m=E[1]*E[1]-E[0]*E[2];if(m<=0){cerr<<"SEAM_NONPOS s="<<s<<" j="<<j<<" n="<<n<<"\n";return 11;}if(!sset||m<seam_min){sset=true;seam_min=m;minj=j;mins=s;minn=n;}++seam_checks;++depth_counts[s];}
    cout<<"adaptive_uncovered_seam_checks="<<seam_checks<<" all_strictly_positive=True minimum_margin="<<seam_min<<" at_j="<<minj<<" s="<<mins<<" n="<<minn<<"\n";
    cout<<"depth_counts";for(int s=SOLD+1;s<=SNEW;++s)cout<<" s"<<s<<"="<<depth_counts[s];cout<<"\n";
    cout<<"tail_amplitude_terms_evaluated="<<amp_terms<<"\n";if(seam_checks!=16){cerr<<"SEAM_COUNT_UNEXPECTED got="<<seam_checks<<"\n";return 12;}

    long long direct=0;for(int s=SOLD+1;s<=SNEW;++s){int j=s+2,n=s+4,k=2;long long tpc=0;auto rr=exact_row(n,tpc);cpp_int expected[3]={rr[k+1],rr[k],rr[k-1]};
        for(int t=-1;t<=1;++t){int q=j+t;cpp_int got=V[q][n]/F[q]-completion_error(j,t,s);if(got!=expected[t+1]){cerr<<"DIRECT_FAIL s="<<s<<" t="<<t<<"\n";return 13;}}
        if(rr[k]*rr[k]-rr[k-1]*rr[k+1]<=0){cerr<<"DIRECT_MARGIN_FAIL\n";return 14;}++direct;}
    cout<<"independent_deep_endpoint_RSK_crosschecks="<<direct<<" s=41..47 PASS\n";
    cout<<"theorem_stitch=row_n<=84 + archived_adaptive_s<=40 + new_adaptive_seam_s41..47 implies_all_source_valid_defects_j<=66\n";
    auto t1=std::chrono::steady_clock::now();cout<<"elapsed_seconds="<<std::chrono::duration<double>(t1-t0).count()<<"\nALL_EXACT_CHECKS_PASS\n";
}
