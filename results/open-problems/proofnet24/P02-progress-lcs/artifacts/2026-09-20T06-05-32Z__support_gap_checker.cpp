#include <bits/stdc++.h>
#include <boost/multiprecision/cpp_int.hpp>
using namespace std;
using boost::multiprecision::cpp_int;

struct CV { cpp_int weight; array<int,8> c; };

static cpp_int gcdc(cpp_int a, cpp_int b) {
    if (a < 0) a = -a; if (b < 0) b = -b;
    while (b != 0) { cpp_int r = a % b; a = b; b = r; }
    return a;
}
static cpp_int ceil_div(cpp_int n, const cpp_int& d) {
    // d>0; cpp_int division truncates toward zero.
    if (n >= 0) return (n + d - 1) / d;
    return n / d;
}

int main() {
    const cpp_int a("1995237757733917147310102692686664915858011319606812684127301");
    const cpp_int b("4220452010631561279");
    const cpp_int M("5000000000000000000");
    const cpp_int p=256717, q=800000, qp=q-p;
    array<cpp_int,8> w;
    for (int k=0;k<=6;k++) {
        cpp_int qpow=1, ppow=1;
        for (int j=0;j<6-k;j++) qpow*=q;
        for (int j=0;j<k;j++) ppow*=p;
        w[k]=qpow*qp*ppow;
    }
    cpp_int tail=1; for (int j=0;j<7;j++) tail*=p; w[7]=tail;
    const array<int,8> mult={2,4,4,4,4,4,4,4};
    const cpp_int Wstar=w[0]+w[7];

    vector<CV> all; all.reserve(234375);
    array<int,8> c{};
    for(c[0]=0;c[0]<=2;c[0]++)
    for(c[1]=0;c[1]<=4;c[1]++)
    for(c[2]=0;c[2]<=4;c[2]++)
    for(c[3]=0;c[3]<=4;c[3]++)
    for(c[4]=0;c[4]<=4;c[4]++)
    for(c[5]=0;c[5]<=4;c[5]++)
    for(c[6]=0;c[6]<=4;c[6]++)
    for(c[7]=0;c[7]<=4;c[7]++) {
        cpp_int s=0; for(int k=0;k<8;k++) s += w[k]*c[k];
        all.push_back({s,c});
    }
    sort(all.begin(),all.end(),[](const CV&A,const CV&B){return A.weight<B.weight;});
    vector<cpp_int> sums; sums.reserve(all.size());
    for (const auto& x:all) sums.push_back(x.weight);

    auto lb=[&](const cpp_int& x){return lower_bound(sums.begin(),sums.end(),x)-sums.begin();};
    auto ub=[&](const cpp_int& x){return upper_bound(sums.begin(),sums.end(),x)-sums.begin();};

    size_t tested_n=0, interval_pairs=0, compatible_pairs=0;
    for (const auto& N: all) {
        const cpp_int WN=N.weight;
        if (WN==0 || WN>=Wstar) continue;
        tested_n++;
        cpp_int lo=ceil_div(a-M*WN,b); if (lo<0) lo=0;
        cpp_int hi=(a-WN)/b;
        if (hi<0 || lo>hi) continue;
        cpp_int g=0;
        for(int k=0;k<8;k++) if(N.c[k]) g=gcdc(g,w[k]);
        size_t i0=lb(lo), i1=ub(hi);
        interval_pairs += i1-i0;
        for(size_t ti=i0;ti<i1;ti++) {
            const auto& T=all[ti];
            bool compatible=true;
            for(int k=0;k<8;k++) if(T.c[k]+N.c[k]>mult[k]) {compatible=false;break;}
            if(!compatible) continue;
            compatible_pairs++;
            cpp_int R=a-b*T.weight;
            if(R>=WN && R<=M*WN && R%g==0) {
                cerr << "FAIL: a below-threshold non-tight support survives necessary conditions\n";
                cerr << "WN="<<WN<<" WT="<<T.weight<<" R="<<R<<" g="<<g<<"\n";
                return 2;
            }
        }
    }

    // Verify the threshold itself is the first relaxed survivor claimed in the report.
    array<int,8> nstar={1,0,0,0,0,0,0,1};
    array<int,8> tstar={1,2,4,1,4,1,1,1};
    cpp_int wn=0,wt=0,g=0;
    for(int k=0;k<8;k++) {
        wn += w[k]*nstar[k]; wt += w[k]*tstar[k];
        if(nstar[k]) g=gcdc(g,w[k]);
        if(nstar[k]+tstar[k]>mult[k]) return 3;
    }
    cpp_int Rstar=a-b*wt;
    if(wn!=Wstar || !(Rstar>=wn && Rstar<=M*wn) || Rstar%g!=0) return 4;

    if(!(a>=Wstar*M)) return 5;
    if(!(Wstar>1939*w[7] && Wstar<1940*w[7])) return 6;

    cout << "P02 T02 exact label-support gap checker\n";
    cout << "count_vectors_total="<<all.size()<<"\n";
    cout << "below_threshold_nonzero_vectors="<<tested_n<<"\n";
    cout << "interval_pairs_scanned="<<interval_pairs<<"\n";
    cout << "compatible_pairs_scanned="<<compatible_pairs<<"\n";
    cout << "primitive_coefficients=";
    for(int k=0;k<8;k++) cout<<w[k]<<(k==7?'\n':',');
    cout << "multiplicities=2,4,4,4,4,4,4,4\n";
    cout << "m0="<<w[7]<<"\n";
    cout << "Wstar="<<Wstar<<"\n";
    cout << "Wstar_over_m0_between_1939_and_1940=PASS\n";
    cout << "a_ge_Wstar_times_M=PASS\n";
    cout << "threshold_candidate_ncounts=1,0,0,0,0,0,0,1\n";
    cout << "threshold_candidate_tcounts=1,2,4,1,4,1,1,1\n";
    cout << "threshold_candidate_R="<<Rstar<<"\n";
    cout << "ALL_BELOW_THRESHOLD_NECESSARY_CONFIGURATIONS_EXCLUDED=PASS\n";
    cout << "EXACT_SUPPORT_GAP_CERTIFICATE_PASS\n";
    cout << "ALL_EXACT_CHECKS_PASS\n";
    return 0;
}
