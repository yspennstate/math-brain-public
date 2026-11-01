#include <bits/stdc++.h>
#include <boost/multiprecision/cpp_int.hpp>
using namespace std;
using boost::multiprecision::cpp_int;

struct Rat {
    cpp_int n,d;
    Rat(long long a=0,long long b=1):n(a),d(b){norm();}
    Rat(cpp_int a, cpp_int b):n(a),d(b){norm();}
    static cpp_int ab(cpp_int x){return x<0?-x:x;}
    static cpp_int gcd(cpp_int a, cpp_int b){a=ab(a);b=ab(b);while(b!=0){cpp_int r=a%b;a=b;b=r;}return a;}
    void norm(){ if(d<0){d=-d;n=-n;} cpp_int g=gcd(n,d); if(g!=0){n/=g;d/=g;} }
};
Rat operator+(const Rat&a,const Rat&b){return Rat(a.n*b.d+b.n*a.d,a.d*b.d);}
Rat operator/(const Rat&a,const Rat&b){return Rat(a.n*b.d,a.d*b.n);}
bool operator>(const Rat&a,const Rat&b){return a.n*b.d>b.n*a.d;}

struct Cyl{uint32_t mask; uint8_t suppmask; int s,cost;};
vector<Cyl> C; vector<int> byp[32];
const uint32_t ALL=0xffffffffu;
long long nodes=0,terminals=0,cheapSurv=0;
set<string> canons;
vector<array<int,6>> perms6;

string canonical(vector<int> ch){
    // Removing a redundant cylinder only helps a putative load-feasible cover.
    bool changed=true;
    while(changed){
        changed=false;
        for(int z=(int)ch.size()-1;z>=0;--z){
            uint32_t u=0;
            for(int i=0;i<(int)ch.size();++i) if(i!=z) u|=C[ch[i]].mask;
            if(u==ALL){ch.erase(ch.begin()+z);changed=true;break;}
        }
    }
    string best;
    for(auto &p:perms6){
        vector<int> sms;
        for(int ci:ch){
            int m=0;
            for(int j=0;j<6;j++) if(C[ci].suppmask>>j&1) m|=1<<p[j];
            sms.push_back(m);
        }
        sort(sms.begin(),sms.end());
        string s; for(int m:sms)s.push_back((char)m);
        if(best.empty()||s<best)best=s;
    }
    return best;
}

bool cheap_pass(const vector<int>&ch){
    // Exact dual tests with lambda uniform on a nonempty coordinate subset J.
    // For supports S_i subset J, contribution is 1/(|J||S_i|).
    // Feasibility at t=47/25 would require this <= c=625/2209.
    for(int J=1;J<64;J++){
        int lhs60=0;
        for(int ci:ch){int S=C[ci].suppmask;if((S&~J)==0)lhs60+=60/C[ci].s;}
        int jj=__builtin_popcount((unsigned)J);
        if((long long)lhs60*2209LL > 60LL*jj*625LL) return false;
    }
    return true;
}

void dfs(uint32_t used,int cost,vector<int>&ch){
    ++nodes;
    if(used==ALL){
        ++terminals;
        if(cheap_pass(ch)){++cheapSurv;canons.insert(canonical(ch));}
        return;
    }
    int rem=32-__builtin_popcount(used);
    // Width 2 has the best new-points/cost ratio: 16 points for cost 30.
    int minextra=(30*rem+15)/16;
    if(cost+minextra>101)return;
    uint32_t rr=(~used)&ALL;
    int p=__builtin_ctz(rr);
    for(int ci:byp[p]){
        if(find(ch.begin(),ch.end(),ci)!=ch.end())continue;
        const auto &cc=C[ci];
        if(cost+cc.cost>101)continue;
        if((cc.mask&~used)==0)continue;
        ch.push_back(ci);dfs(used|cc.mask,cost+cc.cost,ch);ch.pop_back();
    }
}

Rat dual_value(const string& key,const array<int,6>&W){
    long long SW=0;for(int w:W)SW+=w;
    Rat ans(0,1);
    for(unsigned char smc:key){
        int sm=(int)smc;
        Rat h(0,1);
        for(int j=0;j<6;j++)if(sm>>j&1)h=h+Rat(1,W[j]);
        ans=ans+(Rat(1,SW)/h);
    }
    return ans;
}

int main(){
    array<int,6> p={0,1,2,3,4,5};do{perms6.push_back(p);}while(next_permutation(p.begin(),p.end()));
    vector<array<int,6>> V(32);
    for(int b=0;b<32;b++){V[b][0]=1;for(int j=0;j<5;j++)V[b][j+1]=(b>>j&1)?1:-1;}
    for(int sm=1;sm<64;sm++){
        int s=__builtin_popcount((unsigned)sm);if(s<2)continue;
        int first=__builtin_ctz((unsigned)sm);vector<int>coords;for(int j=0;j<6;j++)if(sm>>j&1)coords.push_back(j);
        for(int pat=0;pat<(1<<(s-1));pat++){
            int sig[6]={0};sig[first]=1;int z=0;
            for(int j:coords)if(j!=first){sig[j]=(pat>>z&1)?1:-1;++z;}
            uint32_t mask=0;
            for(int b=0;b<32;b++){
                int base=0;bool have=false,ok=true;
                for(int j:coords){int v=V[b][j]*sig[j];if(!have){base=v;have=true;}else if(v!=base){ok=false;break;}}
                if(ok)mask|=1u<<b;
            }
            C.push_back({mask,(uint8_t)sm,s,60/s});
        }
    }
    if(C.size()!=358){cerr<<"bad cylinder count\n";return 2;}
    for(int i=0;i<(int)C.size();i++)for(int q=0;q<32;q++)if(C[i].mask>>q&1)byp[q].push_back(i);

    vector<int>ch;dfs(0,0,ch);

    const int masks[27][6]={
      {3,7,15,23,63,63},{3,7,15,27,63,63},{3,7,15,29,63,63},{3,7,15,31,47,55},
      {3,7,15,31,47,59},{3,7,15,31,47,61},{3,7,15,31,47,63},{3,7,15,31,55,55},
      {3,7,15,31,55,59},{3,7,15,31,55,61},{3,7,15,31,55,63},{3,7,15,31,59,59},
      {3,7,15,31,59,61},{3,7,15,31,59,63},{3,7,15,31,61,61},{3,7,15,31,61,62},
      {3,7,15,31,61,63},{3,7,15,31,63,63},{3,7,27,31,47,47},{3,7,29,31,47,47},
      {3,7,31,31,47,47},{3,15,15,23,55,55},{7,7,11,27,59,59},{7,7,27,27,43,43},
      {7,11,13,30,62,62},{7,11,23,23,43,43},{7,11,29,29,46,46}
    };
    const int ww[27][6]={
      {320,320,172,76,76,36},{319,319,159,100,65,37},{321,318,170,96,59,36},
      {317,317,170,93,52,52},{318,318,167,99,50,50},{318,317,170,98,48,48},
      {320,320,170,97,46,46},{316,316,168,81,67,51},{318,318,165,90,63,46},
      {319,318,169,89,61,44},{322,322,168,88,59,42},{319,319,162,96,61,43},
      {321,320,166,95,59,40},{323,323,166,94,57,38},{322,320,169,94,57,38},
      {321,321,169,94,57,38},{324,323,169,93,55,36},{326,326,169,92,53,34},
      {312,312,152,93,71,60},{314,310,163,88,65,60},{319,319,161,83,59,59},
      {297,297,143,108,94,61},{247,247,191,157,95,62},{234,234,185,144,102,102},
      {222,206,206,206,97,63},{230,230,163,163,107,107},{203,203,192,192,105,105}
    };
    set<string> expected;
    vector<array<int,6>> weights;
    for(int z=0;z<27;z++){
        string k;for(int q=0;q<6;q++)k.push_back((char)masks[z][q]);expected.insert(k);
        array<int,6>w{};for(int q=0;q<6;q++)w[q]=ww[z][q];weights.push_back(w);
    }
    if(canons!=expected){cerr<<"canonical survivor set mismatch got="<<canons.size()<<" expected=27\n";return 3;}
    Rat target(625,2209);
    Rat mindual(1000000000LL,1);int mini=-1;
    for(int z=0;z<27;z++){
        string k;for(int q=0;q<6;q++)k.push_back((char)masks[z][q]);
        Rat d=dual_value(k,weights[z]);
        if(!(d>target)){cerr<<"dual certificate failed z="<<z<<"\n";return 4;}
        if(mini<0 || mindual.n*d.d > d.n*mindual.d){mindual=d;mini=z;}
    }
    cout<<"R13_CYLINDER_188_EXACT_PASS\n";
    cout<<"projective_classes=32 cylinders_width_2_to_6="<<C.size()<<"\n";
    cout<<"target_t=47/25 target_c=625/2209\n";
    cout<<"aggregate_cost_cutoff_units_60=101 because 225000/2209=101.856...\n";
    cout<<"search_nodes="<<nodes<<" terminal_covers="<<terminals<<" cheap_dual_survivors="<<cheapSurv<<"\n";
    cout<<"canonical_support_survivors="<<canons.size()<<"\n";
    cout<<"minimum_embedded_dual_index="<<mini<<" numerator="<<mindual.n<<" denominator="<<mindual.d<<"\n";
    cout<<"minimum_embedded_dual_decimal~0.293655714226454 > 625/2209~0.282933454051607\n";
    cout<<"all_27_exact_rational_dual_certificates_pass=1\n";
}
