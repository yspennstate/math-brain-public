#include <algorithm>
#include <array>
#include <cstdint>
#include <cmath>
#include <iomanip>
#include <iostream>
#include <limits>
#include <climits>
#include <vector>
#include <string>

struct StepResult { uint32_t next; uint8_t reward; };
static inline StepResult step_state(uint32_t state, int uv, int w) {
    const int m=2*w; const uint32_t mask=(1u<<m)-1u;
    const uint32_t x=state&mask, g=(state>>m)&mask;
    const int u=(uv>>1)&1, v=uv&1;
    int V[32]; V[0]=0; for(int i=0;i<m;++i) V[i+1]=V[i]+int((g>>i)&1u);
    int Q[32]; const int a0=(int((x>>0)&1u)==v); Q[0]=std::max(V[1],V[0]+a0);
    for(int k=1;k<m;++k){ const int ak=(int((x>>k)&1u)==v); int z=Q[k-1]; z=std::max(z,V[k]+ak); z=std::max(z,V[k+1]); Q[k]=z; }
    const int am=(u==v); Q[m]=std::max(Q[m-1],V[m]+am);
    uint32_t gp=0; for(int i=0;i<m;++i) if(Q[i+1]-Q[i]) gp|=(1u<<i);
    const uint32_t xp=(x>>1)|(uint32_t(u)<<(m-1));
    const uint8_t reward=uint8_t(Q[w]-V[w]);
    return {xp|(gp<<m),reward};
}
struct Node { uint32_t next[4]; uint8_t reward_sum; };
static std::string i128s(__int128 x){ if(x==0)return "0"; bool neg=x<0; if(neg)x=-x; std::string s; while(x){s.push_back(char('0'+x%10)); x/=10;} if(neg)s.push_back('-'); std::reverse(s.begin(),s.end()); return s; }

int main(){
    constexpr int w=6,m=12,float_iterations=190,int_iterations=120;
    constexpr int64_t SCALE=2000000000000000000LL;
    constexpr uint32_t BAD=0xffffffffu;
    const size_t total=size_t(1)<<(2*m);
    std::vector<uint32_t> index(total,BAD), states; std::vector<Node> nodes;
    states.reserve(6000000); nodes.reserve(6000000); index[0]=0; states.push_back(0); nodes.push_back({{0,0,0,0},0});
    for(size_t head=0;head<states.size();++head){ uint32_t s=states[head]; Node nd{}; nd.reward_sum=0; for(int uv=0;uv<4;++uv){auto z=step_state(s,uv,w); nd.reward_sum+=z.reward; uint32_t j=index[z.next]; if(j==BAD){j=uint32_t(states.size()); index[z.next]=j; states.push_back(z.next); nodes.push_back({{0,0,0,0},0});} nd.next[uv]=j;} nodes[head]=nd; }
    std::cerr<<"reachable="<<states.size()<<"\n";
    std::vector<double> h(states.size(),0.0), hn(states.size(),0.0);
    for(int it=0;it<float_iterations;++it){ for(size_t i=0;i<states.size();++i){auto &nd=nodes[i]; hn[i]=( (double)nd.reward_sum + h[nd.next[0]]+h[nd.next[1]]+h[nd.next[2]]+h[nd.next[3]])/4.0;} double base=hn[0]; for(auto &z:hn) z-=base; h.swap(hn); }
    std::vector<int64_t> H(states.size());
    for(size_t i=0;i<states.size();++i){ H[i]=(int64_t) llround(h[i]*(double)SCALE); }
    for(int jt=0;jt<int_iterations;++jt){
        std::vector<int64_t> Hn(states.size());
        for(size_t i=0;i<states.size();++i){ auto &nd=nodes[i]; __int128 a=(__int128)nd.reward_sum*SCALE + H[nd.next[0]]+H[nd.next[1]]+H[nd.next[2]]+H[nd.next[3]]; if(a>=0) Hn[i]=(int64_t)((a+2)/4); else Hn[i]=(int64_t)(-(((-a)+2)/4)); }
        int64_t base=Hn[0]; for(auto &z:Hn) z-=base; H.swap(Hn);
    }
    __int128 mn=((__int128)1<<126), mx=-((__int128)1<<126); std::vector<uint8_t> e(states.size());
    std::vector<__int128> D(states.size());
    int64_t Hmin=LLONG_MAX,Hmax=LLONG_MIN; for(auto z:H){Hmin=std::min(Hmin,z);Hmax=std::max(Hmax,z);}
    for(size_t i=0;i<states.size();++i){auto &nd=nodes[i]; __int128 num=(__int128)nd.reward_sum*SCALE + H[nd.next[0]]+H[nd.next[1]]+H[nd.next[2]]+H[nd.next[3]] - (__int128)4*H[i]; D[i]=num; if(num<mn)mn=num; if(num>mx)mx=num; }
    if(states.size()!=5735086ULL) return 2;
    if(mn!=(__int128)6238638445311257066LL || mx!=(__int128)6238638445311257073LL){std::cerr<<"baseline mismatch\n"; return 3;}
    for(size_t i=0;i<states.size();++i){ __int128 z=D[i]-mn; if(z<0||z>255) return 4; e[i]=(uint8_t)z; }
    std::cout<<"baseline_min="<<i128s(mn)<<" baseline_max="<<i128s(mx)<<" span="<<i128s(mx-mn)<<"\n";
    // E_k(s)=4^{k-1} sum_{t=0}^{k-1} P^t e(s), so E_{k+1}=4^k e+sum_a E_k(T_a s).
    std::vector<__int128> cur(states.size()), nxt(states.size());
    for(size_t i=0;i<states.size();++i) cur[i]=e[i];
    __int128 pow4=1;
    for(int k=1;k<=60;++k){
        __int128 emin=cur[0], emax=cur[0]; uint32_t argmin=0,argmax=0;
        for(size_t i=1;i<cur.size();++i){if(cur[i]<emin){emin=cur[i];argmin=i;} if(cur[i]>emax){emax=cur[i];argmax=i;}}
        __int128 spread=emax-emin;
        long double width=(long double)spread/((long double)4.0L*SCALE*(long double)k*(long double)pow4);
        std::cout<<"k="<<k<<" pow4="<<i128s(pow4)<<" emin="<<i128s(emin)<<" emax="<<i128s(emax)<<" spread="<<i128s(spread)
                 <<" width="<<std::setprecision(21)<<(double)width<<" argmin_state="<<states[argmin]<<" argmax_state="<<states[argmax]<<"\n";
        if(k==60) break;
        __int128 nextpow=pow4*4;
        for(size_t i=0;i<states.size();++i){auto &nd=nodes[i]; nxt[i]=nextpow*(__int128)e[i] + cur[nd.next[0]]+cur[nd.next[1]]+cur[nd.next[2]]+cur[nd.next[3]]; }
        cur.swap(nxt); pow4=nextpow;
    }
    std::cout<<"Hmin="<<Hmin<<" Hmax="<<Hmax<<" Hosc="<<(Hmax-Hmin)<<"\nALL_EXACT_CHECKS_PASS\n";
}
