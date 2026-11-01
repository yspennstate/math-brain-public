#include <bits/stdc++.h>
using namespace std;
using i128 = __int128_t;

struct Frac { long long num=0, den=1; };
static long long gg(long long a,long long b){ a=llabs(a); b=llabs(b); while(b){ long long t=a%b;a=b;b=t;} return a?a:1; }
static Frac normfrac(long long n,long long d){ if(d<0){n=-n;d=-d;} long long g=gg(n,d); return {n/g,d/g}; }
static bool gt_frac(long long an,long long ad,long long bn,long long bd){ return (i128)an*bd > (i128)bn*ad; }
static bool eq_frac(long long an,long long ad,long long bn,long long bd){ return (i128)an*bd == (i128)bn*ad; }

int main(){
    const int N=9, D=6;
    vector<int> subs;
    for(int S=0; S<(1<<N); ++S) if(__builtin_popcount((unsigned)S)<=D) subs.push_back(S);
    sort(subs.begin(), subs.end(), [](int a,int b){
        int pa=__builtin_popcount((unsigned)a), pb=__builtin_popcount((unsigned)b);
        if(pa!=pb) return pa<pb;
        int sa=0,sb=0; for(int i=0;i<9;++i){ if(a>>i&1) sa+=i; if(b>>i&1) sb+=i; }
        if(sa!=sb) return sa<sb;
        return a<b;
    });
    if((int)subs.size()!=466 || subs[0]!=0){ cerr<<"subset order fail\n"; return 2; }
    int idx[1<<N]; fill(begin(idx),end(idx),-1); for(int i=0;i<(int)subs.size();++i) idx[subs[i]]=i;
    vector<vector<int>> pred(subs.size());
    for(int qi=0; qi<(int)subs.size(); ++qi){
        int S=subs[qi];
        set<int> pp;
        for(int j=0;j<N;++j) if(S>>j&1){
            int del=S&~(1<<j); pp.insert(idx[del]);
            for(int i=0;i<j;++i) if(!(S>>i&1)){
                int sh=(S&~(1<<j))|(1<<i); pp.insert(idx[sh]);
            }
        }
        for(int p:pp){ if(p<0 || p>=qi){ cerr<<"linear extension fail\n"; return 2; } pred[qi].push_back(p); }
    }

    vector<unsigned char> in(subs.size(),0);
    vector<int> members; members.reserve(256);
    in[0]=1; members.push_back(0);
    unsigned long long leaves=0, standard_fail=0, standard_eq=0;
    long long stdmax_num=-1,stdmax_den=1; int stdmax_b=0; vector<int> stdmax_facets;
    vector<vector<int>> exceptions;

    auto eval_family = [&](){
        ++leaves;
        int b=(int)members.size();
        vector<int> fac;
        for(int A:members){
            bool maximal=true;
            for(int B:members) if(A!=B && (A&B)==A){ maximal=false; break; }
            if(maximal) fac.push_back(A);
        }
        int h=(int)fac.size();
        int deg[N]={0};
        for(int A:fac) for(int j=0;j<N;++j) if(A>>j&1) ++deg[j];
        long long zsum=0;
        for(int j=0;j<N;++j){ long long z=max(0,h-2*deg[j]); zsum += z*z; }
        long long qn=(long long)b*zsum, qd=(long long)h*h;
        if(gt_frac(qn,qd,192,1)){ ++standard_fail; exceptions.push_back(fac); }
        if(eq_frac(qn,qd,192,1)) ++standard_eq;
        if(stdmax_num<0 || gt_frac(qn,qd,stdmax_num,stdmax_den)){
            auto f=normfrac(qn,qd); stdmax_num=f.num; stdmax_den=f.den; stdmax_b=b; stdmax_facets=fac;
        }
    };

    function<void(int)> dfs = [&](int q){
        if(q==(int)subs.size()){ eval_family(); return; }
        int S=subs[q];
        // Exclude branch.
        dfs(q+1);
        // Include only if all immediate deletion/left-shift predecessors are present and
        // the new member is union-compatible with every already included member.
        bool ok=true;
        for(int p:pred[q]) if(!in[p]) {ok=false;break;}
        if(ok){ for(int A:members) if(__builtin_popcount((unsigned)(A|S))>D){ok=false;break;} }
        if(ok){ in[q]=1; members.push_back(S); dfs(q+1); members.pop_back(); in[q]=0; }
    };
    // The empty set is forced in every nonempty downset.
    dfs(1);

    if(leaves!=4677567ULL){ cerr<<"leaf count "<<leaves<<"\n"; return 3; }
    if(standard_fail!=34ULL){ cerr<<"fail count "<<standard_fail<<"\n"; return 3; }
    if(standard_eq!=1ULL){ cerr<<"eq count "<<standard_eq<<"\n"; return 3; }
    if(!eq_frac(stdmax_num,stdmax_den,5824,25) || stdmax_b!=91){ cerr<<"std max fail "<<stdmax_num<<"/"<<stdmax_den<<" b="<<stdmax_b<<"\n"; return 3; }
    vector<int> expected={31,47,79,143,259,261,262,265,266,268}; sort(stdmax_facets.begin(),stdmax_facets.end()); sort(expected.begin(),expected.end());
    if(stdmax_facets!=expected){ cerr<<"worst facets mismatch\n"; return 3; }

    // Repair every sporadic failure: put total mass 7/10 uniformly on rank-5 facets and
    // total mass 3/10 uniformly on lower-rank facets, then thin coordinates whose marginal
    // exceeds 1/2. Downward closure keeps every thinned subset inside the family.
    long long repmax_num=-1,repmax_den=1; int repmax_b=0;
    for(auto fac:exceptions){
        vector<int> hi,lo; for(int A:fac){ if(__builtin_popcount((unsigned)A)==5) hi.push_back(A); else lo.push_back(A); }
        if(hi.empty()||lo.empty()){ cerr<<"repair split missing\n"; return 4; }
        int h5=hi.size(), hl=lo.size();
        int d5[N]={0}, dl[N]={0};
        for(int A:hi) for(int j=0;j<N;++j) if(A>>j&1) ++d5[j];
        for(int A:lo) for(int j=0;j<N;++j) if(A>>j&1) ++dl[j];
        long long den=10LL*h5*hl;
        long long zsum=0;
        for(int j=0;j<N;++j){
            long long covnum=7LL*d5[j]*hl + 3LL*dl[j]*h5;
            long long z=max(0LL, den-2*covnum);
            zsum += z*z;
        }
        // Reconstruct family size exactly from its facets.
        bool present[1<<N]={false}; int b=0;
        for(int A:fac){
            for(int T=A;;T=(T-1)&A){ if(!present[T]){present[T]=true;++b;} if(T==0) break; }
        }
        long long qn=(long long)b*zsum, qd=den*den;
        if(gt_frac(qn,qd,192,1)){ cerr<<"repair failed q="<<qn<<"/"<<qd<<" b="<<b<<"\n"; return 4; }
        if(repmax_num<0 || gt_frac(qn,qd,repmax_num,repmax_den)){
            auto f=normfrac(qn,qd); repmax_num=f.num; repmax_den=f.den; repmax_b=b;
        }
    }
    if(!eq_frac(repmax_num,repmax_den,703,4) || repmax_b!=95){ cerr<<"repair max fail "<<repmax_num<<"/"<<repmax_den<<" b="<<repmax_b<<"\n"; return 4; }

    // Principal six-cube equality: all subsets of {0,...,5}.
    vector<int> cube; for(int T=0;T<(1<<6);++T) cube.push_back(T);
    int cb=cube.size(), ch=1; int cdeg[N]={0}; for(int j=0;j<6;++j)cdeg[j]=1;
    long long csum=0; for(int j=0;j<N;++j){ long long z=max(0,ch-2*cdeg[j]); csum+=z*z; }
    if(!eq_frac((long long)cb*csum,(long long)ch*ch,192,1)){ cerr<<"cube equality fail\n"; return 5; }

    // Komlos arithmetic for t=3 sqrt(3)/2: t^2=27/4, 192/t^2=256/9, and t<3.
    if(192*4*9 != 256*27){ cerr<<"coefficient identity fail\n"; return 5; }
    if(!(27 < 36)){ cerr<<"metric movement fail\n"; return 5; }

    cout << "R13 n=9 shifted-diameter-6 exact checker\n";
    cout << "subsets_processed= " << subs.size() << "\n";
    cout << "shifted_downsets_diameter_le_6= " << leaves << "\n";
    cout << "standard_certificate_failures= " << standard_fail << "\n";
    cout << "standard_equalities= " << standard_eq << "\n";
    cout << "max_standard_Q= " << stdmax_num << "/" << stdmax_den << "\n";
    cout << "max_standard_family_size= " << stdmax_b << "\n";
    cout << "max_standard_facets="; for(int x:stdmax_facets) cout << " " << x; cout << "\n";
    cout << "repair_rule= 7/10_rank5_plus_3/10_lower\n";
    cout << "repaired_exception_count= " << exceptions.size() << "\n";
    cout << "max_repaired_Q= " << repmax_num << "/" << repmax_den << "\n";
    cout << "max_repaired_family_size= " << repmax_b << "\n";
    cout << "principal_6_cube_Q= 192\n";
    cout << "target_t_squared= 27/4\n";
    cout << "row_coefficient= 256/9\n";
    cout << "metric_3sqrt3_over2_lt_3= PASS\n";
    cout << "ALL_EXACT_CHECKS_PASS\n";
    return 0;
}
