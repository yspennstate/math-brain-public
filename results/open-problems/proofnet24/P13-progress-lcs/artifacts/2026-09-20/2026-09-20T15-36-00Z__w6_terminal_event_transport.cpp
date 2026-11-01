#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <limits>
#include <string>
#include <vector>
#include <boost/multiprecision/cpp_int.hpp>
using namespace std;
using boost::multiprecision::cpp_int;

struct Step { uint32_t next; uint8_t reward; };
static inline Step step_state(uint32_t state, int uv, int w){
    const int m=2*w; const uint32_t mask=(1u<<m)-1u;
    const uint32_t x=state&mask, g=(state>>m)&mask;
    const int u=(uv>>1)&1, v=uv&1;
    int reward=0;
    int carr[32]; carr[0]=0;
    for(int i=1;i<=m;i++){
        int gi=(g>>(i-1))&1u;
        int xi=(x>>(i-1))&1u;
        carr[i]=(1-gi)*(carr[i-1] || (xi==v));
    }
    uint32_t gp=0;
    for(int i=1;i<m;i++){
        int gi1=(g>>i)&1u;
        int gpi=gi1+carr[i+1]-carr[i];
        if(gpi) gp |= 1u<<(i-1);
    }
    int gpm=(1-carr[m])*(u==v);
    if(gpm) gp |= 1u<<(m-1);
    reward=((g>>w)&1u)+carr[w+1]; // g_{w+1}+d_{w+1}, 1-based.
    const uint32_t xp=(x>>1)|(uint32_t(u)<<(m-1));
    return {xp|(gp<<m),(uint8_t)reward};
}
static string i128s(__int128 x){
    if(x==0) return "0"; bool neg=x<0; if(neg)x=-x; string s;
    while(x){ s.push_back(char('0'+int(x%10))); x/=10; }
    if(neg)s.push_back('-'); reverse(s.begin(),s.end()); return s;
}
static inline int phi(uint32_t state,int w){
    const int m=2*w; const uint32_t mask=(1u<<m)-1u; const uint32_t g=(state>>m)&mask;
    int z=0;
    // phi = sum_{i=w+1}^{m-1} g_i + 2 g_m.
    for(int i=w+1;i<=m-1;i++) z += int((g>>(i-1))&1u);
    z += 2*int((g>>(m-1))&1u);
    return z;
}
struct Node{uint32_t nxt[4]; uint8_t reward_sum; uint8_t gm;};
int main(){
    constexpr int w=6,m=12; constexpr uint32_t BAD=0xffffffffu;
    const size_t total=size_t(1)<<(2*m);
    vector<uint32_t> index(total,BAD), states; vector<Node> nodes;
    states.reserve(5800000); nodes.reserve(5800000); index[0]=0; states.push_back(0); nodes.push_back({{0,0,0,0},0,0});
    for(size_t h=0;h<states.size();h++){
        uint32_t s=states[h]; Node nd{}; nd.reward_sum=0; nd.gm=((s>>(m+(m-1)))&1u);
        for(int a=0;a<4;a++){
            Step z=step_state(s,a,w); nd.reward_sum += z.reward;
            uint32_t j=index[z.next]; if(j==BAD){j=uint32_t(states.size());index[z.next]=j;states.push_back(z.next);nodes.push_back({{0,0,0,0},0,0});}
            nd.nxt[a]=j;
        }
        nodes[h]=nd;
    }
    cout << "reachable=" << states.size() << "\n";
    if(states.size()!=5735086ULL) return 2;

    // Exact pointwise identity: r + P phi - phi = 1-g_m.
    // Multiply by 4: sum_a reward + sum_a phi(T_a s) - 4 phi(s) = 4(1-g_m).
    size_t id_checks=0;
    for(size_t i=0;i<states.size();i++){
        const auto &nd=nodes[i];
        int lhs=int(nd.reward_sum)-4*phi(states[i],w);
        for(int a=0;a<4;a++) lhs += phi(states[nd.nxt[a]],w);
        int rhs=4*(1-int(nd.gm));
        if(lhs!=rhs){ cerr<<"identity failure i="<<i<<" lhs="<<lhs<<" rhs="<<rhs<<"\n"; return 3; }
        id_checks++;
    }
    cout << "pointwise_coboundary_checks=" << id_checks << " PASS\n";

    // F_k(s)=4^k P^k g_m(s), exact integer recurrence.
    vector<__int128> cur(states.size()), nxt(states.size());
    for(size_t i=0;i<states.size();i++) cur[i]=nodes[i].gm;
    __int128 pow4=1;
    __int128 min30=0,max30=0,pow30=0,min31=0,max31=0,pow31=0,min62=0,max62=0,pow62=0;
    for(int k=0;k<=62;k++){
        __int128 mn=cur[0],mx=cur[0];
        for(size_t i=1;i<cur.size();i++){mn=min(mn,cur[i]);mx=max(mx,cur[i]);}
        if(k==30){min30=mn;max30=mx;pow30=pow4;}
        if(k==31){min31=mn;max31=mx;pow31=pow4;}
        if(k==62){min62=mn;max62=mx;pow62=pow4;break;}
        for(size_t i=0;i<states.size();i++){
            const auto &nd=nodes[i];
            nxt[i]=cur[nd.nxt[0]]+cur[nd.nxt[1]]+cur[nd.nxt[2]]+cur[nd.nxt[3]];
        }
        cur.swap(nxt); pow4*=4;
    }
    cout<<"k30 pow4="<<i128s(pow30)<<" min="<<i128s(min30)<<" max="<<i128s(max30)<<" spread="<<i128s(max30-min30)<<"\n";
    cout<<"k31 pow4="<<i128s(pow31)<<" min="<<i128s(min31)<<" max="<<i128s(max31)<<" spread="<<i128s(max31-min31)<<"\n";
    cout<<"k62 pow4="<<i128s(pow62)<<" min="<<i128s(min62)<<" max="<<i128s(max62)<<" spread="<<i128s(max62-min62)<<"\n";

    const __int128 E30MIN=(__int128)237795384677590044LL, E30MAX=(__int128)270210112419958892LL;
    const __int128 E31MIN=(__int128)957102063065457189LL, E31MAX=(__int128)1076664734642680290LL;
    auto p128=[](const char* z){__int128 x=0;for(;*z;z++)x=x*10+(*z-'0');return x;};
    const __int128 E62MIN=p128("4663938790599173885795905174720472033");
    const __int128 E62MAX=p128("4707842623226368321561270898837713032");
    const __int128 P30=p128("1152921504606846976"),P31=p128("4611686018427387904"),P62=p128("21267647932558653966460912964485513216");
    if(min30!=E30MIN||max30!=E30MAX||pow30!=P30||min31!=E31MIN||max31!=E31MAX||pow31!=P31||min62!=E62MIN||max62!=E62MAX||pow62!=P62) return 4;

    // Threshold p > 1-L = 25916751/125000000 certifies gamma_w=1-p < L.
    const cpp_int THNUM=25916751, THDEN=125000000;
    auto C=[](__int128 x){ return cpp_int(i128s(x)); };
    cpp_int cross30=THDEN*C(min30)-THNUM*C(pow30);
    cpp_int cross31=THDEN*C(min31)-THNUM*C(pow31);
    cpp_int cross62=THDEN*C(min62)-THNUM*C(pow62);
    cout<<"threshold_cross_k30="<<cross30<<" (must be <0)\n";
    cout<<"threshold_cross_k31="<<cross31<<" (must be >0)\n";
    cout<<"threshold_cross_k62="<<cross62<<" (must be >0)\n";
    if(!(cross30<0 && cross31>0 && cross62>0)) return 5;

    // Strict nesting [1-max/4^k,1-min/4^k] from k=31 to 62.
    cpp_int lower_inward = C(max31)*C(pow62)-C(max62)*C(pow31);
    cpp_int upper_inward = C(min62)*C(pow31)-C(min31)*C(pow62);
    cout<<"nest_lower_inward_cross="<<lower_inward<<"\n";
    cout<<"nest_upper_inward_cross="<<upper_inward<<"\n";
    if(!(lower_inward>0 && upper_inward>0)) return 6;

    cpp_int ratio_num=C(max31-min31)*C(pow62), ratio_den=C(max62-min62)*C(pow31);
    cout<<"width31_num="<<i128s(max31-min31)<<" denom="<<i128s(pow31)<<"\n";
    cout<<"width62_num="<<i128s(max62-min62)<<" denom="<<i128s(pow62)<<"\n";
    cout<<"width_ratio_exact_num="<<ratio_num<<" denom="<<ratio_den<<"\n";
    long double w31=(long double)(max31-min31)/(long double)pow31;
    long double w62=(long double)(max62-min62)/(long double)pow62;
    long double lo31=1.0L-(long double)max31/(long double)pow31;
    long double hi31=1.0L-(long double)min31/(long double)pow31;
    long double lo62=1.0L-(long double)max62/(long double)pow62;
    long double hi62=1.0L-(long double)min62/(long double)pow62;
    cout.setf(ios::fixed); cout.precision(18);
    cout<<"diag_interval_k31=["<<(double)lo31<<","<<(double)hi31<<"] width="<<(double)w31<<"\n";
    cout<<"diag_interval_k62=["<<(double)lo62<<","<<(double)hi62<<"] width="<<(double)w62<<" ratio="<<(double)(w31/w62)<<"\n";
    cout<<"ALL_EXACT_CHECKS_PASS\n";
}
