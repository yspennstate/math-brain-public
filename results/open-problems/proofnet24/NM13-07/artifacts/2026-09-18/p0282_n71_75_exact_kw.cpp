#include <boost/multiprecision/cpp_int.hpp>
#include <algorithm>
#include <functional>
#include <iostream>
#include <string>
#include <vector>
#include <map>
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
    int rows=(int)lam.size();
    int width=lam.empty()?0:lam[0];
    vector<int> colh(width,0);
    for(int j=0;j<width;++j){ while(colh[j]<rows && lam[colh[j]]>j) ++colh[j]; }
    for(int i=0;i<rows;++i){
        for(int j=0;j<lam[i];++j){
            int h=(lam[i]-j)+(colh[j]-i-1);
            hooks*=h;
        }
    }
    cpp_int q=fact/hooks;
    if(q*hooks!=fact){ cerr<<"nonintegral hook quotient at n="<<n<<"\n"; std::exit(2); }
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

static string ratio_decimal_15(const cpp_int&num,const cpp_int&den){
    cpp_int scaled=(num*cpp_int("1000000000000000"))/den;
    string s=scaled.convert_to<string>(); while(s.size()<16)s="0"+s;
    return s.substr(0,s.size()-15)+"."+s.substr(s.size()-15);
}

struct MinRec { bool set=false; cpp_int num=0,den=1,margin=0; int n=-1,k=-1; };
static void upd(MinRec& r,int n,int k,const cpp_int& num,const cpp_int& den,const cpp_int& margin){
    if(den==0) return;
    if(!r.set || num*r.den < r.num*den){r.set=true;r.num=num;r.den=den;r.margin=margin;r.n=n;r.k=k;}
}

int main(){
    const int LO=70, HI=75;
    cout<<"P0282 exact extension certificate: hook sums + Euler partition counts + Kauers-Wang long-sector recurrences\n";
    map<int, vector<cpp_int>> rows;
    long long total_new_partitions=0;
    MinRec global_new;

    for(int n=LO;n<=HI;++n){
        cpp_int fact=factorial_int(n);
        vector<cpp_int> ell(n+2);
        vector<int> cur;
        long long pcount=0;
        partitions_rec(n,n,cur,[&](const vector<int>&lam){ ++pcount; cpp_int f=hook_dimension(lam,n,fact); ell[lam[0]] += f*f; });
        long long pexp=partition_number_euler(n);
        if(pcount!=pexp){ cerr<<"Euler partition-count mismatch n="<<n<<" got="<<pcount<<" expected="<<pexp<<"\n"; return 3; }
        cpp_int sum=0; for(int k=1;k<=n;++k) sum+=ell[k];
        if(sum!=fact){ cerr<<"Plancherel/factorial identity failed n="<<n<<"\n"; return 4; }

        MinRec all, longsec, shortsec;
        int split=(n+1)/2; // ceil(n/2)
        for(int k=2;k<n;++k){
            cpp_int den=ell[k-1]*ell[k+1], num=ell[k]*ell[k], margin=num-den;
            if(margin<0){ cerr<<"NEGATIVE SOURCE MARGIN n="<<n<<" k="<<k<<"\n"; return 5; }
            upd(all,n,k,num,den,margin);
            if(k>=split) upd(longsec,n,k,num,den,margin); else upd(shortsec,n,k,num,den,margin);
            if(n>=71) upd(global_new,n,k,num,den,margin);
        }
        if(n>=71) total_new_partitions += pcount;
        rows[n]=std::move(ell);
        cout<<"n="<<n<<" partitions="<<pcount
            <<" all_min_k="<<all.k<<" all_min_ratio~"<<ratio_decimal_15(all.num,all.den)
            <<" long_min_k="<<longsec.k<<" long_min_ratio~"<<ratio_decimal_15(longsec.num,longsec.den);
        if(shortsec.set) cout<<" short_min_k="<<shortsec.k<<" short_min_ratio~"<<ratio_decimal_15(shortsec.num,shortsec.den);
        else cout<<" short_min_k=NA";
        cout<<" all_margins_nonnegative=True factorial_check=True euler_p_check=True\n";
    }

    long long rec2=0, rec1=0;
    for(int n=LO;n<HI;++n){
        auto &an=rows.at(n); auto &ap=rows.at(n+1);
        int k0=(n+1)/2; // ceil(n/2)
        for(int k=k0;k<=n;++k){
            cpp_int lhs=cpp_int(n+1)*(n+1)*(an[k]+an[k+1]);
            cpp_int rhs=cpp_int(n-k+1)*ap[k]+cpp_int(n+k+1)*ap[k+1];
            if(lhs!=rhs){ cerr<<"KW recurrence (2) failed n="<<n<<" k="<<k<<"\n"; return 6; }
            ++rec2;
        }
    }
    for(int n=LO+1;n<HI;++n){
        auto &am=rows.at(n-1); auto &an=rows.at(n); auto &ap=rows.at(n+1);
        int k0=n/2+1; // strict k>n/2 so every shifted entry stays in the proved long-LIS sector
        for(int k=k0;k<=n;++k){
            cpp_int lhs=ap[k]+cpp_int(n)*n*am[k];
            cpp_int rhs=an[k+1]+cpp_int(2*n-1)*an[k]+an[k-1];
            if(lhs!=rhs){ cerr<<"KW recurrence (1) failed n="<<n<<" k="<<k<<"\n"; return 7; }
            ++rec1;
        }
    }

    cout<<"new_rows_certified=71..75\n";
    cout<<"total_partitions_processed_71_75="<<total_new_partitions<<"\n";
    cout<<"KW_recurrence2_exact_checks="<<rec2<<"\n";
    cout<<"KW_recurrence1_exact_checks="<<rec1<<"\n";
    cout<<"global_min_location_71_75=(n="<<global_new.n<<",k="<<global_new.k<<")\n";
    cout<<"global_new_min_ratio_exact="<<global_new.num<<"/"<<global_new.den<<"\n";
    cout<<"global_new_min_margin_exact="<<global_new.margin<<"\n";
    cout<<"combined_scope_guard=chaining archived exact n<=70 certificate gives N_exact=75; no all-n closure inferred\n";
    cout<<"ALL_EXACT_CHECKS_PASS\n";
    return 0;
}
