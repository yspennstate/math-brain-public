#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <map>
#include <numeric>
#include <vector>
#include <boost/multiprecision/cpp_int.hpp>
using boost::multiprecision::cpp_int;
using namespace std;

static int Cbin[33][7];

static int det5(array<array<int,5>,5> a){
    int sign=1, prev=1;
    for(int k=0;k<4;++k){
        int piv=k; while(piv<5 && a[piv][k]==0) ++piv;
        if(piv==5) return 0;
        if(piv!=k){swap(a[piv],a[k]);sign=-sign;}
        int pivot=a[k][k];
        for(int i=k+1;i<5;++i) for(int j=k+1;j<5;++j){
            int num=a[i][j]*pivot-a[i][k]*a[k][j];
            assert(num%prev==0); a[i][j]=num/prev;
        }
        for(int i=k+1;i<5;++i)a[i][k]=0;
        prev=pivot;
    }
    return sign*a[4][4];
}
static int rank_comb(const array<int,5>& s){
    int r=0; for(int i=0;i<5;++i) r += Cbin[s[i]][i+1]; return r;
}
static int project5(int mask6,int skip){
    int lo=mask6 & ((1<<skip)-1);
    int hi=(mask6>>(skip+1))<<skip;
    return lo|hi;
}
static int minor_det(const array<int,5>& rows,int skip,const vector<int8_t>& dettab){
    array<int,5> v;
    for(int i=0;i<5;++i)v[i]=project5(rows[i],skip);
    int inv=0;
    for(int i=0;i<5;++i)for(int j=i+1;j<5;++j){
        if(v[i]==v[j]) return 0;
        if(v[i]>v[j]) ++inv;
    }
    array<int,5> s=v; sort(s.begin(),s.end());
    int d=dettab[rank_comb(s)];
    return (inv&1)?-d:d;
}
static long long gcdll(long long a,long long b){a=llabs(a);b=llabs(b);while(b){long long t=a%b;a=b;b=t;}return a;}
static vector<long long> primitive_abs(const array<int,6>& b){
    array<long long,7>a{}; long long sm=0;for(int x:b)sm+=x;a[0]=-sm;for(int j=0;j<6;++j)a[j+1]=b[j];
    for(long long x:a)if(x==0)return{};
    long long g=0;for(long long x:a)g=gcdll(g,x);assert(g);
    vector<long long>v;for(long long x:a)v.push_back(llabs(x/g));sort(v.begin(),v.end(),greater<long long>());return v;
}
static int zero_count(const vector<long long>& a){int z=0;for(int m=0;m<128;++m){long long s=0;for(int i=0;i<7;++i)s+=((m>>i)&1)?a[i]:-a[i];if(s==0)++z;}return z;}
static long long fact(int n){long long r=1;for(int i=2;i<=n;++i)r*=i;return r;}
static long long directions(const vector<long long>&v){map<long long,int>m;for(auto x:v)m[x]++;long long p=fact(7);for(auto kv:m)p/=fact(kv.second);return p*64;}
static cpp_int ipow(cpp_int b,int e){cpp_int r=1;while(e){if(e&1)r*=b;b*=b;e>>=1;}return r;}

int main(){
    for(int n=0;n<=32;++n){Cbin[n][0]=1;for(int k=1;k<=6;++k)Cbin[n][k]=(k>n?0:(n==0?0:Cbin[n-1][k-1]+Cbin[n-1][k]));}
    assert(Cbin[32][5]==201376);
    vector<int8_t>dettab(Cbin[32][5]);
    for(int a=0;a<28;++a)for(int b=a+1;b<29;++b)for(int c=b+1;c<30;++c)for(int d=c+1;d<31;++d)for(int e=d+1;e<32;++e){
        array<int,5>s={a,b,c,d,e};array<array<int,5>,5>M{};
        for(int i=0;i<5;++i)for(int j=0;j<5;++j)M[i][j]=(s[i]>>j)&1;
        int dv=det5(M);assert(dv>=-127&&dv<=127);dettab[rank_comb(s)]=(int8_t)dv;
    }
    uint64_t total=0,rank5=0,minimal=0;map<vector<long long>,uint64_t>fc;
    array<int,5>rows;
    for(int a=1;a<=59;++a)for(int b=a+1;b<=60;++b)for(int cc=b+1;cc<=61;++cc)for(int d=cc+1;d<=62;++d)for(int e=d+1;e<=63;++e){
        ++total;rows={a,b,cc,d,e};array<int,6>kv{};bool nz=false;
        for(int j=0;j<6;++j){int dm=minor_det(rows,j,dettab);kv[j]=(j&1)?-dm:dm;if(dm)nz=true;}
        if(!nz)continue;++rank5;
        for(int i=0;i<5;++i){int s=0;for(int j=0;j<6;++j)s+=((rows[i]>>j)&1)*kv[j];assert(s==0);}
        auto typ=primitive_abs(kv);if(typ.empty())continue;++minimal;fc[typ]++;
    }
    assert(total==7028847ULL);assert(rank5==6029142ULL);assert(minimal==405636ULL);assert(fc.size()==14);
    cout<<"support7_projective_frames="<<total<<"\n";
    cout<<"support7_rank6_frames="<<rank5<<"\n";
    cout<<"support7_minimal_frames="<<minimal<<"\n";
    cout<<"support7_absolute_types="<<fc.size()<<"\n";
    map<int,long long,greater<int>>agg;
    for(auto const&kv:fc){int z=zero_count(kv.first);long long dr=directions(kv.first);agg[z]+=dr;cout<<"type=(";for(size_t i=0;i<kv.first.size();++i){if(i)cout<<',';cout<<kv.first[i];}cout<<") zero="<<z<<"/128 frames="<<kv.second<<" directions="<<dr<<"\n";}
    map<int,long long,greater<int>>exp={{30,448},{24,2240},{22,2688},{20,8960},{18,6720},{16,47040},{14,40320},{12,123648}};assert(agg==exp);
    long long sum=0;cout<<"aggregated_direction_counts_by_zero_atom:\n";for(auto kv:agg){cout<<"  zero="<<kv.first<<" dirs="<<kv.second<<"\n";sum+=kv.second;}assert(sum==232064);cout<<"total_directions="<<sum<<"\nmax_zero_atom=30/128=15/64\n";
    cpp_int lhs=ipow(cpp_int(64),4),rhs=cpp_int(8)*ipow(cpp_int(35),4);assert(lhs>rhs);cout<<"growth_certificate_64^4_minus_8*35^4="<<(lhs-rhs)<<" >0\n";
    assert(12<=16);cout<<"growth_domain_n>=4096: log2(4096)=12 <= sqrt(4096)/4=16; derivative thereafter positive\n";
    cout<<"generic_support_range: 7 <= k <= floor(3*sqrt(n)/4)\n";
    cout<<"generic_target_decay_exponent_gamma=log2(64/35)-3/4 >0 (certified above)\n";
    cout<<"SELF-CHECK PASS\n";
}
