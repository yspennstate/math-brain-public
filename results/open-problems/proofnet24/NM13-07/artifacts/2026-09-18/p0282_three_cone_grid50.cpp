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

static cpp_int factorial_int(int n){ cpp_int x=1; for(int i=2;i<=n;++i) x*=i; return x; }
static cpp_int hook_dimension(const vector<int>& lam, int n, const cpp_int& fact){
    if(lam.empty()) return 1;
    int rows=(int)lam.size(), width=lam[0]; vector<int> colh(width,0);
    for(int c=0;c<width;++c) while(colh[c]<rows && lam[colh[c]]>c) ++colh[c];
    cpp_int hooks=1;
    for(int i=0;i<rows;++i) for(int c=0;c<lam[i];++c)
        hooks *= (lam[i]-c)+(colh[c]-i-1);
    if(fact%hooks!=0){ cerr<<"HOOK_DIV_FAIL n="<<n<<"\n"; std::exit(2); }
    return fact/hooks;
}
static void all_partitions_rec(int rem,int maxp,vector<int>&cur,const std::function<void(const vector<int>&)>&visit){
    if(rem==0){visit(cur);return;} int hi=std::min(rem,maxp);
    for(int a=hi;a>=1;--a){cur.push_back(a);all_partitions_rec(rem-a,a,cur,visit);cur.pop_back();}
}
static long long partition_number_euler(int n){
    vector<long long> p(n+1); p[0]=1;
    for(int m=1;m<=n;++m){ long long s=0; for(int k=1;;++k){
        int g1=k*(3*k-1)/2,g2=k*(3*k+1)/2; if(g1>m)break; long long sg=(k&1)?1:-1;
        s+=sg*p[m-g1]; if(g2<=m)s+=sg*p[m-g2]; } p[m]=s; }
    return p[n];
}
static vector<cpp_int> exact_row(int n,long long& pc){
    cpp_int fact=factorial_int(n); vector<cpp_int> ell(n+2); vector<int>cur; pc=0;
    all_partitions_rec(n,n,cur,[&](const vector<int>&lam){++pc; cpp_int f=hook_dimension(lam,n,fact); ell[lam[0]]+=f*f;});
    long long ep=partition_number_euler(n);
    if(pc!=ep){cerr<<"PARTITION_COUNT_FAIL n="<<n<<" got="<<pc<<" expected="<<ep<<"\n";std::exit(3);}
    cpp_int sum=0;for(int k=1;k<=n;++k)sum+=ell[k];
    if(sum!=fact){cerr<<"PLANCHEREL_SUM_FAIL n="<<n<<"\n";std::exit(4);}
    return ell;
}

struct RatioMin {
    bool set=false; cpp_int num=0, den=1; int k=-1,j=-1;
    void consider(const cpp_int& n,const cpp_int& d,int kk,int jj){
        if(d<=0) return;
        if(!set || n*den < num*d){set=true; num=n; den=d; k=kk; j=jj;}
    }
};

int main(){
    auto t0=std::chrono::steady_clock::now();
    const int GRID=50;
    cout << "P0282 exact diagnostic: Hankel coefficient three-cone grid through n="<<GRID<<"\n";
    cout << "three_cone_conditions=k_logconcavity,j_logconcavity,adjacent_TP2\n";

    vector<vector<cpp_int>> ell(GRID+1);
    vector<cpp_int> fact(GRID+1), fact2(GRID+1);
    fact[0]=1; fact2[0]=1;
    long long total_parts_grid=0;
    for(int n=1;n<=GRID;++n){
        fact[n]=factorial_int(n); fact2[n]=fact[n]*fact[n];
        long long pc=0; ell[n]=exact_row(n,pc); total_parts_grid+=pc;
    }
    cout << "grid_rows=1.."<<GRID<<" total_partitions_enumerated="<<total_parts_grid<<" all_partition_counts_and_factorial_sums_PASS=True\n";

    auto Aval=[&](int k,int j)->const cpp_int& { return ell[k+j][k]; };
    auto F2=[&](int k,int j)->const cpp_int& { return fact2[k+j]; };
    auto ratio_parts=[&](int k1,int j1,int k2,int j2,int k3,int j3,int k4,int j4){
        cpp_int num = Aval(k1,j1)*Aval(k2,j2)*F2(k3,j3)*F2(k4,j4);
        cpp_int den = Aval(k3,j3)*Aval(k4,j4)*F2(k1,j1)*F2(k2,j2);
        return std::pair<cpp_int,cpp_int>(num,den);
    };

    long long ck=0,cj=0,ctp=0,cchen=0;
    RatioMin mink,minj,mintp,minchen;

    for(int k=2;k<=GRID;++k){
        for(int j=0;k+j+1<=GRID;++j){
            auto r=ratio_parts(k,j,k,j,k-1,j,k+1,j); ++ck;
            if(r.first<r.second){cerr<<"K_LC_FAIL k="<<k<<" j="<<j<<" n="<<(k+j)<<"\n"; return 10;}
            mink.consider(r.first,r.second,k,j);
        }
    }
    for(int k=1;k<=GRID;++k){
        for(int j=1;k+j+1<=GRID;++j){
            auto r=ratio_parts(k,j,k,j,k,j-1,k,j+1); ++cj;
            if(r.first<r.second){cerr<<"J_LC_FAIL k="<<k<<" j="<<j<<" n="<<(k+j)<<"\n"; return 11;}
            minj.consider(r.first,r.second,k,j);
        }
    }
    for(int k=1;k<=GRID;++k){
        for(int j=0;k+j+2<=GRID;++j){
            auto r=ratio_parts(k,j,k+1,j+1,k+1,j,k,j+1); ++ctp;
            if(r.first<r.second){cerr<<"TP2_FAIL k="<<k<<" j="<<j<<"\n"; return 12;}
            mintp.consider(r.first,r.second,k,j);
        }
    }
    for(int k=2;k<GRID;++k){
        for(int j=1;k+j<=GRID;++j){
            auto r=ratio_parts(k,j,k,j,k-1,j+1,k+1,j-1); ++cchen;
            if(r.first<r.second){cerr<<"CHEN_GRID_FAIL k="<<k<<" j="<<j<<" n="<<(k+j)<<"\n"; return 13;}
            minchen.consider(r.first,r.second,k,j);
        }
    }

    cout<<"k_direction_logconcavity_checks="<<ck<<" all_PASS=True min_at_k="<<mink.k<<" j="<<mink.j<<" min_ratio_exact="<<mink.num<<"/"<<mink.den<<"\n";
    cout<<"j_direction_logconcavity_checks="<<cj<<" all_PASS=True min_at_k="<<minj.k<<" j="<<minj.j<<" min_ratio_exact="<<minj.num<<"/"<<minj.den<<"\n";
    cout<<"adjacent_TP2_checks="<<ctp<<" all_PASS=True min_at_k="<<mintp.k<<" j="<<mintp.j<<" min_ratio_exact="<<mintp.num<<"/"<<mintp.den<<"\n";
    cout<<"chen_diagonal_consistency_checks="<<cchen<<" all_PASS=True min_at_k="<<minchen.k<<" j="<<minchen.j<<" min_ratio_exact="<<minchen.num<<"/"<<minchen.den<<"\n";

    auto t1=std::chrono::steady_clock::now();
    cout<<"elapsed_seconds="<<std::chrono::duration<double>(t1-t0).count()<<"\n";
    cout<<"ALL_EXACT_CHECKS_PASS\n";
}
