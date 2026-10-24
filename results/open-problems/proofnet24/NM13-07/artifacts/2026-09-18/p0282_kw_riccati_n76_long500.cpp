#include <boost/multiprecision/cpp_int.hpp>
#include <algorithm>
#include <chrono>
#include <functional>
#include <iomanip>
#include <iostream>
#include <map>
#include <string>
#include <vector>
using boost::multiprecision::cpp_int;
using std::cout; using std::cerr; using std::string; using std::vector; using std::map;

static cpp_int factorial_int(int n){ cpp_int x=1; for(int i=2;i<=n;++i)x*=i; return x; }

static void partitions_rec(int rem,int max_part,vector<int>&cur,const std::function<void(const vector<int>&)>&visit){
    if(rem==0){visit(cur);return;}
    int hi=std::min(rem,max_part);
    for(int first=hi;first>=1;--first){cur.push_back(first);partitions_rec(rem-first,first,cur,visit);cur.pop_back();}
}

static cpp_int hook_dimension(const vector<int>&lam,int n,const cpp_int&fact){
    cpp_int hooks=1;
    int rows=(int)lam.size(), width=lam.empty()?0:lam[0];
    vector<int> colh(width,0);
    for(int j=0;j<width;++j){ while(colh[j]<rows && lam[colh[j]]>j) ++colh[j]; }
    for(int i=0;i<rows;++i) for(int j=0;j<lam[i];++j){
        int h=(lam[i]-j)+(colh[j]-i-1); hooks*=h;
    }
    cpp_int q=fact/hooks;
    if(q*hooks!=fact){ cerr<<"nonintegral hook quotient n="<<n<<"\n"; std::exit(2); }
    return q;
}

static long long partition_number_euler(int n){
    vector<long long> p(n+1,0); p[0]=1;
    for(int m=1;m<=n;++m){
        long long s=0;
        for(int k=1;;++k){
            int g1=k*(3*k-1)/2, g2=k*(3*k+1)/2;
            if(g1>m) break;
            long long sign=(k%2?1:-1);
            s += sign*p[m-g1];
            if(g2<=m) s += sign*p[m-g2];
        }
        p[m]=s;
    }
    return p[n];
}

static vector<cpp_int> exact_row(int n,long long& pcount){
    cpp_int fact=factorial_int(n);
    vector<cpp_int> ell(n+2);
    vector<int> cur; pcount=0;
    partitions_rec(n,n,cur,[&](const vector<int>&lam){++pcount; cpp_int f=hook_dimension(lam,n,fact); ell[lam[0]]+=f*f;});
    if(pcount!=partition_number_euler(n)){ cerr<<"partition count mismatch n="<<n<<"\n"; std::exit(3); }
    cpp_int sum=0; for(int k=1;k<=n;++k) sum+=ell[k];
    if(sum!=fact){ cerr<<"factorial sum mismatch n="<<n<<"\n"; std::exit(4); }
    return ell;
}

static long double to_ld(const cpp_int& x){ return x.convert_to<long double>(); }

int main(){
    auto start=std::chrono::steady_clock::now();
    cout<<"P0282 Kauers-Wang Riccati/Turan certificate: exact row76 + recurrence propagation\n";

    long long pc75=0,pc76=0;
    vector<cpp_int> a75=exact_row(75,pc75), a76=exact_row(76,pc76);
    cout<<"seed_row_75_partitions="<<pc75<<" seed_row_76_partitions="<<pc76<<"\n";

    bool minset=false; int mink=-1; cpp_int minnum=0,minden=1,minmargin=0;
    for(int k=2;k<76;++k){
        cpp_int num=a76[k]*a76[k], den=a76[k-1]*a76[k+1], margin=num-den;
        if(margin<0){ cerr<<"NEGATIVE SOURCE MARGIN n=76 k="<<k<<"\n"; return 5; }
        if(!minset || num*minden<minnum*den){minset=true;mink=k;minnum=num;minden=den;minmargin=margin;}
    }
    cout<<std::setprecision(15);
    cout<<"row76_all_source_margins_nonnegative=True min_k="<<mink
        <<" min_ratio~"<<(to_ld(minnum)/to_ld(minden))<<"\n";
    cout<<"row76_min_ratio_exact="<<minnum<<"/"<<minden<<"\n";
    cout<<"row76_min_margin_exact="<<minmargin<<"\n";

    // Reconstruct the recurrence-valid half of row 76 from row 75 and boundary a_{76,76}=1.
    int n=75, s=(n+1)/2; // ceil(n/2)=38
    vector<cpp_int> rec76(78); rec76[76]=1;
    int recon=0;
    for(int k=n;k>=s;--k){
        cpp_int d=cpp_int(n+1)*(n+1)*(a75[k]+a75[k+1]);
        cpp_int beta=n+k+1, alpha=n-k+1;
        cpp_int numer=d-beta*rec76[k+1];
        if(numer<0 || numer%alpha!=0){ cerr<<"KW2 divisibility/nonnegative fail 75->76 k="<<k<<"\n"; return 6; }
        rec76[k]=numer/alpha;
        if(rec76[k]!=a76[k]){ cerr<<"KW2 reconstruction mismatch 75->76 k="<<k<<"\n"; return 7; }
        ++recon;
    }
    cout<<"KW2_reconstruction_row76_exact_matches="<<recon<<" range_k="<<s<<".."<<n<<" plus_boundary_k=76\n";

    // Exact Turan identity and normalized monotonicity for the independently enumerated 75->76 transition.
    int transfer_checks=0; bool mono=true; int mono_fail=-1;
    bool prev_set=false; cpp_int prev_num=0,prev_den=1;
    for(int k=s+1;k<=n;++k){
        cpp_int dk=cpp_int(n+1)*(n+1)*(a75[k]+a75[k+1]);
        cpp_int dkm1=cpp_int(n+1)*(n+1)*(a75[k-1]+a75[k]);
        cpp_int T=a76[k]*a76[k]-a76[k-1]*a76[k+1];
        cpp_int alpha=n-k+1,beta=n+k+1,alpha_prev=n-k+2,beta_prev=n+k;
        cpp_int rhs=cpp_int(2)*(n+1)*a76[k]*a76[k]+(alpha*dkm1+beta_prev*dk)*a76[k]-dkm1*dk;
        cpp_int lhs=alpha_prev*beta*T;
        if(lhs!=rhs){ cerr<<"Turan transfer identity fail 75->76 k="<<k<<"\n"; return 8; }
        cpp_int Fnum=alpha_prev*beta*T, Fden=dk*dk; // exact normalized transfer slack
        if(prev_set && Fnum*prev_den<prev_num*Fden){mono=false;mono_fail=k;break;}
        prev_set=true; prev_num=Fnum; prev_den=Fden; ++transfer_checks;
    }
    cout<<"Turan_transfer_identity_checks="<<transfer_checks
        <<" F_normalized_monotone_increasing_k="<<(mono?"True":"False")
        <<" first_fail_k="<<mono_fail<<"\n";
    if(!mono) return 9;

    // Use only KW recurrence (2) from exact row 76 onward. This certifies a large recurrence-valid half-sector,
    // but it does NOT move N_exact beyond 76 because the complementary short sector is not generated here.
    vector<cpp_int> cur=a76;
    int propagated=0; long long lc_checks=0; int mono_rows=0;
    int first_mono_fail_row=-1, first_mono_fail_k=-1;
    for(int nn=76;nn<500;++nn){
        int ss=(nn+1)/2; // ceil(nn/2)
        vector<cpp_int> nxt(nn+3); nxt[nn+1]=1;
        for(int k=nn;k>=ss;--k){
            cpp_int d=cpp_int(nn+1)*(nn+1)*(cur[k]+cur[k+1]);
            cpp_int beta=nn+k+1, alpha=nn-k+1;
            cpp_int numer=d-beta*nxt[k+1];
            if(numer<0 || numer%alpha!=0){ cerr<<"propagation divisibility/nonnegative fail n="<<nn<<" k="<<k<<"\n"; return 10; }
            nxt[k]=numer/alpha;
        }
        for(int k=ss+1;k<=nn;++k){
            cpp_int T=nxt[k]*nxt[k]-nxt[k-1]*nxt[k+1];
            if(T<0){ cerr<<"negative propagated long-sector Turan n="<<(nn+1)<<" k="<<k<<"\n"; return 11; }
            ++lc_checks;
        }
        bool row_mono=true; bool row_prev=false; cpp_int row_num=0,row_den=1;
        for(int k=ss+1;k<=nn;++k){
            cpp_int dk=cpp_int(nn+1)*(nn+1)*(cur[k]+cur[k+1]);
            cpp_int T=nxt[k]*nxt[k]-nxt[k-1]*nxt[k+1];
            cpp_int alpha_prev=nn-k+2,beta=nn+k+1;
            cpp_int Fnum=alpha_prev*beta*T, Fden=dk*dk;
            if(row_prev && Fnum*row_den<row_num*Fden){
                row_mono=false; first_mono_fail_row=nn+1; first_mono_fail_k=k; break;
            }
            row_prev=true; row_num=Fnum; row_den=Fden;
        }
        if(!row_mono) break;
        ++mono_rows; ++propagated;
        cur.swap(nxt);
    }
    cout<<"KW2_propagated_exact_rows=77..500 count="<<propagated<<"\n";
    cout<<"long_sector_exact_logconcavity_checks="<<lc_checks<<" all_nonnegative=True\n";
    cout<<"F_monotone_rows="<<mono_rows<<"/424 first_mono_fail_row="<<first_mono_fail_row
        <<" first_mono_fail_k="<<first_mono_fail_k<<"\n";
    if(propagated!=424 || mono_rows!=424) return 12;

    cout<<"frozen_metric_scope_guard=N_exact moves only 75->76; recurrence-only long-sector propagation does not certify missing short-sector inequalities\n";
    auto end=std::chrono::steady_clock::now();
    std::chrono::duration<double> secs=end-start;
    cout<<"elapsed_seconds="<<std::setprecision(6)<<secs.count()<<"\n";
    cout<<"ALL_EXACT_CHECKS_PASS\n";
    return 0;
}
