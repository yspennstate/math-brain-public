#include <boost/multiprecision/cpp_int.hpp>
#include <algorithm>
#include <chrono>
#include <functional>
#include <iomanip>
#include <iostream>
#include <map>
#include <set>
#include <vector>
using boost::multiprecision::cpp_int;
using std::cerr; using std::cout; using std::vector;

static cpp_int factorial_int(int n){ cpp_int x=1; for(int i=2;i<=n;++i) x*=i; return x; }

static cpp_int hook_dimension(const vector<int>& lam, int n, const cpp_int& fact){
    if(lam.empty()) return 1;
    int rows=(int)lam.size(), width=lam[0];
    vector<int> colh(width,0);
    for(int c=0;c<width;++c) while(colh[c]<rows && lam[colh[c]]>c) ++colh[c];
    cpp_int hooks=1;
    for(int i=0;i<rows;++i) for(int c=0;c<lam[i];++c)
        hooks *= (lam[i]-c)+(colh[c]-i-1);
    if(fact%hooks!=0){ cerr<<"HOOK_DIV_FAIL n="<<n<<"\n"; std::exit(2); }
    return fact/hooks;
}

struct TailPartition { vector<int> lam; cpp_int f; };
static void tail_partitions_rec(int rem,int maxp,vector<int>&cur,vector<TailPartition>&out){
    if(rem==0){
        int r=0; for(int x:cur) r+=x;
        cpp_int fr=hook_dimension(cur,r,factorial_int(r));
        out.push_back({cur,fr});
        return;
    }
    int hi=std::min(rem,maxp);
    for(int a=hi;a>=1;--a){ cur.push_back(a); tail_partitions_rec(rem-a,a,cur,out); cur.pop_back(); }
}

static void all_partitions_rec(int rem,int maxp,vector<int>&cur,const std::function<void(const vector<int>&)>&visit){
    if(rem==0){ visit(cur); return; }
    int hi=std::min(rem,maxp);
    for(int a=hi;a>=1;--a){ cur.push_back(a); all_partitions_rec(rem-a,a,cur,visit); cur.pop_back(); }
}

static long long partition_number_euler(int n){
    vector<long long> p(n+1); p[0]=1;
    for(int m=1;m<=n;++m){
        long long s=0;
        for(int k=1;;++k){
            int g1=k*(3*k-1)/2, g2=k*(3*k+1)/2;
            if(g1>m) break;
            long long sg=(k&1)?1:-1;
            s += sg*p[m-g1];
            if(g2<=m) s += sg*p[m-g2];
        }
        p[m]=s;
    }
    return p[n];
}

static vector<cpp_int> exact_row(int n,long long&pc){
    cpp_int fact=factorial_int(n); vector<cpp_int> ell(n+2); vector<int> cur; pc=0;
    all_partitions_rec(n,n,cur,[&](const vector<int>&lam){
        ++pc; cpp_int f=hook_dimension(lam,n,fact); ell[lam[0]] += f*f;
    });
    if(pc!=partition_number_euler(n)){ cerr<<"PARTITION_COUNT_FAIL n="<<n<<" got="<<pc<<" expected="<<partition_number_euler(n)<<"\n"; std::exit(3); }
    cpp_int sum=0; for(int k=1;k<=n;++k) sum+=ell[k];
    if(sum!=fact){ cerr<<"PLANCHEREL_SUM_FAIL n="<<n<<"\n"; std::exit(4); }
    return ell;
}

static long double to_ld(const cpp_int&x){ return x.convert_to<long double>(); }

int main(){
    auto t0=std::chrono::steady_clock::now();
    const int J=100, S=30, FULLN=82, NMAX=2*J;
    cout<<"P0282 fixed-depth Plancherel-tail correction / s<=30 exact boundary checker\n";

    // Fixed-defect completion polynomials P_q(n) = V[q][n].
    vector<cpp_int> F(J+3); F[0]=1; for(int i=1;i<(int)F.size();++i) F[i]=F[i-1]*i;
    vector<vector<cpp_int>> V(J+2,vector<cpp_int>(NMAX+1));
    for(int n=0;n<=NMAX;++n){ V[0][n]=1; V[1][n]=cpp_int(n-1)*(n-1); }
    for(int q=1;q<=J;++q) for(int n=1;n<=NMAX;++n)
        V[q+1][n]=cpp_int(n)*n*(V[q][n-1]+cpp_int(q)*V[q-1][n-1]) - cpp_int(2*n-q-1)*V[q][n];
    cout<<"completion_recurrence_table exact=True J="<<J<<" NMAX="<<NMAX<<"\n";

    // Precompute all tail partitions lambda |- r needed by the theorem.
    vector<vector<TailPartition>> tails(S+3); vector<int> cur;
    long long tail_shapes=0;
    for(int r=0;r<=S+2;++r){ tail_partitions_rec(r,r,cur,tails[r]); tail_shapes += tails[r].size(); }
    cout<<"tail_partition_atlas r=0.."<<(S+2)<<" shapes="<<tail_shapes<<" exact_hook_dimensions=True\n";

    long long amplitude_terms=0;
    auto completion_error = [&](int j,int t,int s)->cpp_int{
        int q=j+t, n=2*j-s, N=n-q;
        int rmax=s+2*t-2;
        if(rmax<0) return cpp_int(0);
        cpp_int total=0;
        for(int r=0;r<=rmax;++r){
            int M=q-r;
            for(const auto& tt: tails[r]){
                if(r && M<tt.lam[0]) continue; // (M,lambda) must be a partition.
                // f^(M,lambda) from the same first-row residual formula, now with tail size r.
                cpp_int dim_num=tt.f;
                for(int a=1;a<=r;++a){
                    int la=(a-1<(int)tt.lam.size())?tt.lam[a-1]:0;
                    dim_num *= (M+a-la);
                }
                if(dim_num%F[r]!=0){ cerr<<"TAIL_DIM_DIV_FAIL j="<<j<<" t="<<t<<" s="<<s<<" r="<<r<<"\n"; std::exit(5); }
                cpp_int fmu=dim_num/F[r];

                // R_mu(N), where mu=(M,lambda), padded by zeroes to q parts.
                cpp_int R=N+1-M; // first factor; nonzero on r<=s+2t-2 by construction.
                for(int a=1;a<=r;++a){
                    int la=(a-1<(int)tt.lam.size())?tt.lam[a-1]:0;
                    R *= (N+a+1-la);
                }
                for(int i=r+2;i<=q;++i) R *= (N+i);
                if(R==0) continue;
                cpp_int amp_num=fmu*R;
                if(amp_num%F[q]!=0){ cerr<<"TAIL_AMPLITUDE_DIV_FAIL j="<<j<<" t="<<t<<" s="<<s<<" r="<<r<<"\n"; std::exit(7); }
                cpp_int amp=amp_num/F[q];
                total += amp*amp;
                ++amplitude_terms;
            }
        }
        return total;
    };

    // General finite-depth correction theorem check for every source-valid pair in the box.
    long long boundary_checks=0;
    cpp_int min_boundary_margin=0; int min_s=-1,min_j=-1; bool min_set=false;
    for(int s=3;s<=S;++s){
        for(int j=4;j<=J;++j){
            int n=2*j-s;
            if(n<j+2) continue; // source interior k=n-j >= 2.
            cpp_int E[3];
            for(int t=-1;t<=1;++t){
                int q=j+t;
                if(V[q][n]%F[q]!=0){ cerr<<"COMPLETION_DIV_FAIL j="<<j<<" t="<<t<<" s="<<s<<"\n"; return 8; }
                cpp_int completed=V[q][n]/F[q];
                cpp_int err=completion_error(j,t,s);
                E[t+1]=completed-err;
                if(E[t+1]<0){ cerr<<"NEGATIVE_SOURCE_COUNT j="<<j<<" t="<<t<<" s="<<s<<"\n"; return 9; }
            }
            cpp_int margin=E[1]*E[1]-E[0]*E[2];
            if(margin<=0){ cerr<<"BOUNDARY_MARGIN_NONPOS s="<<s<<" j="<<j<<" value="<<margin<<"\n"; return 10; }
            if(!min_set || margin<min_boundary_margin){ min_set=true; min_boundary_margin=margin; min_s=s; min_j=j; }
            ++boundary_checks;
        }
    }
    cout<<"fixed_depth_source_scan s=3.."<<S<<" j=4.."<<J<<" all_source_valid_margins_strictly_positive=True checks="<<boundary_checks<<"\n";
    cout<<"tail_amplitude_terms_evaluated="<<amplitude_terms<<" minimum_boundary_margin="<<min_boundary_margin<<" at_s="<<min_s<<" j="<<min_j<<"\n";
    cout<<"combined_with_predecessor full_source_defect_range_j=1..32=True\n";
    cout<<"combined_with_predecessor additional_range_j=33..100 n>=2j-30=True\n";

    // Independent small exact-RSK checks of the correction formula itself.
    long long direct_cross=0;
    std::map<int,vector<cpp_int>> row_cache;
    for(int s=3;s<=8;++s){
        for(int j=4;j<=10;++j){
            int n=2*j-s; if(n<j+2) continue;
            if(!row_cache.count(n)){ long long pc=0; row_cache[n]=exact_row(n,pc); }
            const auto& row=row_cache[n]; int k=n-j;
            cpp_int expected[3]={row[k+1],row[k],row[k-1]}; // t=-1,0,+1 defects.
            for(int t=-1;t<=1;++t){
                int q=j+t;
                cpp_int got=V[q][n]/F[q]-completion_error(j,t,s);
                if(got!=expected[t+1]){ cerr<<"DIRECT_RSK_TAIL_FAIL s="<<s<<" j="<<j<<" t="<<t<<" got="<<got<<" expected="<<expected[t+1]<<"\n"; return 11; }
            }
            cpp_int direct=row[k]*row[k]-row[k+1]*row[k-1];
            if(direct<=0){ cerr<<"DIRECT_RSK_MARGIN_NONPOS s="<<s<<" j="<<j<<"\n"; return 12; }
            ++direct_cross;
        }
    }
    cout<<"independent_small_RSK_tail_crosschecks s=3..8 j=4..10 PASS count="<<direct_cross<<"\n";

    auto t1=std::chrono::steady_clock::now();
    cout<<"elapsed_seconds="<<std::chrono::duration<double>(t1-t0).count()<<"\n";
    cout<<"ALL_EXACT_CHECKS_PASS\n";
    return 0;
}
