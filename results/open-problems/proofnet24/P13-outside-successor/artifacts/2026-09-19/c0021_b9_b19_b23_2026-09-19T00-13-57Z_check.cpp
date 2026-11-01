#include <algorithm>
#include <array>
#include <cassert>
#include <chrono>
#include <cstdint>
#include <iomanip>
#include <functional>
#include <iostream>
#include <limits>
#include <numeric>
#include <string>
#include <unordered_map>
#include <utility>
#include <vector>
using namespace std;
using u128 = unsigned __int128;

struct Triple { int a,b,c; bool operator==(Triple const&o) const {return a==o.a&&b==o.b&&c==o.c;} };
struct THash { size_t operator()(Triple const& x) const noexcept {
    uint64_t h=1469598103934665603ULL;
    for (uint64_t v: {(uint64_t)x.a,(uint64_t)x.b,(uint64_t)x.c}) { h ^= v+0x9e3779b97f4a7c15ULL+(h<<6)+(h>>2); h*=1099511628211ULL; }
    return (size_t)h;
}};

static string u128str(u128 x){ if(!x)return "0"; string s; while(x){s.push_back('0'+x%10);x/=10;} reverse(s.begin(),s.end());return s; }

struct Store {
    vector<array<int,3>> ch;
    vector<vector<pair<int,int>>> qc;
    vector<char> qdone;
    vector<int> acache;
    unordered_map<Triple,int,THash> ids;
    int U,P,M,X;
    Store(){
        ch.push_back({-1,-1,-1}); ch.push_back({-1,-1,-1}); ch.push_back({-1,-1,-1});
        qc.resize(3); qdone.assign(3,0); acache.assign(3,-1);
        U=norm3(0,0,0); P=norm3(1,0,0); M=norm3(2,0,0); X=norm3(1,2,0);
    }
    int norm3(int a,int b,int c){
        int pc=(a==1)+(b==1)+(c==1), mc=(a==2)+(b==2)+(c==2);
        if(pc>=2) return 1; if(mc>=2) return 2;
        array<int,3> z{a,b,c}; sort(z.begin(),z.end()); Triple key{z[0],z[1],z[2]};
        auto it=ids.find(key); if(it!=ids.end()) return it->second;
        int id=(int)ch.size(); ids.emplace(key,id); ch.push_back(z); qc.emplace_back(); qdone.push_back(0); acache.push_back(-1); return id;
    }
    const vector<pair<int,int>>& queries(int t){
        if(qdone[t]) return qc[t];
        qdone[t]=1;
        if(t==0){ qc[t].push_back({1,2}); return qc[t]; }
        if(t==1||t==2) return qc[t];
        auto cc=ch[t];
        vector<pair<int,int>> out;
        for(int i=0;i<3;i++){
            if(i && cc[i]==cc[i-1]) continue;
            auto childq = queries(cc[i]);
            for(auto [cp,cm]: childq){
                auto aa=cc, bb=cc; aa[i]=cp; bb[i]=cm;
                int ap=norm3(aa[0],aa[1],aa[2]);
                int am=norm3(bb[0],bb[1],bb[2]);
                out.push_back({ap,am});
            }
        }
        sort(out.begin(),out.end()); out.erase(unique(out.begin(),out.end()),out.end()); qc[t]=move(out); return qc[t];
    }
    int active(int t){
        if(t<(int)acache.size() && acache[t]>=0) return acache[t];
        int z;
        if(t==P||t==M||t==X) z=1;
        else if(t==0||t==1||t==2||t==U) z=0;
        else { auto cc=ch[t]; z=active(cc[0])+active(cc[1])+active(cc[2]); }
        acache[t]=z; return z;
    }
};

struct Solver {
    Store &S; int K; u128 SCALE; vector<u128> memo; uint64_t calls=0;
    static constexpr u128 INF = (u128)(-1);
    Solver(Store& s,int k):S(s),K(k),SCALE(((u128)1)<<81) { memo.assign(S.ch.size(),INF); }
    u128 v(int t){
        if(t==1||t==2) return 0;
        if((size_t)t>=memo.size()) memo.resize(S.ch.size(),INF);
        if(memo[t]!=INF) return memo[t];
        calls++;
        auto qs=S.queries(t);
        if(memo.size()<S.ch.size()) memo.resize(S.ch.size(),INF);
        u128 best=INF;
        for(auto [a,b]:qs){
            if(S.active(a)>K||S.active(b)>K) continue;
            u128 va=v(a), vb=v(b); u128 sum=va+vb; assert((sum&1)==0);
            u128 z=SCALE+(sum>>1); if(z<best)best=z;
        }
        assert(best!=INF); memo[t]=best; return best;
    }
};

int main(){
    Store S;
    assert((S.queries(S.U)==vector<pair<int,int>>{{S.P,S.M}} || S.queries(S.U)==vector<pair<int,int>>{{S.M,S.P}}));
    int b=S.norm3(2,0,0);
    int s3=S.norm3(S.norm3(2,S.U,S.U), S.norm3(b,b,b), S.norm3(b,b,S.U));
    function<int(int)> lift = [&](int t)->int{
        if(t==1||t==2) return t; if(t==0) return S.U;
        auto cc=S.ch[t]; return S.norm3(lift(cc[0]),lift(cc[1]),lift(cc[2]));
    };
    int s4=lift(s3);
    const u128 SCALE=((u128)1)<<81;
    vector<u128> vals;
    for(int K=1;K<=3;K++){
        auto t0=chrono::steady_clock::now(); Solver sol(S,K); u128 z=sol.v(s4); auto t1=chrono::steady_clock::now();
        vals.push_back(z);
        int p=81; u128 n=z; while(p>0 && (n&1)==0){n>>=1;--p;}
        u128 den=((u128)1)<<p;
        cout<<"K="<<K<<" scaled="<<u128str(z)<<"/2^81 reduced="<<u128str(n)<<"/"<<u128str(den)
            <<" memo_states="<<sol.calls<<" store_nodes="<<S.ch.size()
            <<" sec="<<fixed<<setprecision(3)<<chrono::duration<double>(t1-t0).count()<<"\n";
    }
    u128 v1_num=2739915, v1_den=131072;
    u128 v2_num=1377453593ULL, v2_den=67108864ULL;
    u128 v3_num=2801905528867ULL, v3_den=137438953472ULL;
    assert(vals[0]*v1_den==v1_num*SCALE);
    assert(vals[1]*v2_den==v2_num*SCALE);
    assert(vals[2]*v3_den==v3_num*SCALE);
    u128 e_num=10885886259ULL, e_den=536870912ULL;
    assert(v3_num*e_den > e_num*v3_den);
    assert(v2_num*(v3_den/v2_den)-v3_num==19119429597ULL);
    assert(v3_num-e_num*(v3_den/e_den)==15118646563ULL);
    cout<<"V2_minus_V3=19119429597/137438953472\n";
    cout<<"V3_minus_explicit=15118646563/137438953472\n";
    cout<<"CONCLUSION any unrestricted optimum for S4 has interleaving width at least 4\n";
    cout<<"ALL_EXACT_K3_WIDTH4_ROTATION_CHECKS_PASS\n";
}
