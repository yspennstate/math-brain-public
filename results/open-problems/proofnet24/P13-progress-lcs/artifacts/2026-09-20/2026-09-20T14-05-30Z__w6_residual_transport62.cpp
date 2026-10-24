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
using namespace std;
struct StepResult { uint32_t next; uint8_t reward; };
static inline StepResult step_state(uint32_t state, int uv, int w) {
    const int m=2*w; const uint32_t mask=(1u<<m)-1u;
    const uint32_t x=state&mask, g=(state>>m)&mask;
    const int u=(uv>>1)&1, v=uv&1;
    int V[32]; V[0]=0; for(int i=0;i<m;++i) V[i+1]=V[i]+int((g>>i)&1u);
    int Qv[32]; const int a0=(int((x>>0)&1u)==v); Qv[0]=std::max(V[1],V[0]+a0);
    for(int k=1;k<m;++k){ const int ak=(int((x>>k)&1u)==v); int z=Qv[k-1]; z=std::max(z,V[k]+ak); z=std::max(z,V[k+1]); Qv[k]=z; }
    const int am=(u==v); Qv[m]=std::max(Qv[m-1],V[m]+am);
    uint32_t gp=0; for(int i=0;i<m;++i) if(Qv[i+1]-Qv[i]) gp|=(1u<<i);
    const uint32_t xp=(x>>1)|(uint32_t(u)<<(m-1));
    const uint8_t reward=uint8_t(Qv[w]-V[w]);
    return {xp|(gp<<m),reward};
}
struct Node { uint32_t next[4]; uint8_t reward_sum; };
static __int128 p128(const char* z){__int128 x=0; for(;*z;z++) x=x*10+(*z-'0'); return x;}
static string i128s(__int128 x){ if(x==0)return "0"; bool neg=x<0; if(neg)x=-x; string s; while(x){s.push_back(char('0'+x%10)); x/=10;} if(neg)s.push_back('-'); reverse(s.begin(),s.end()); return s; }

int main(){
    constexpr int w=6,m=12,float_iterations=190,int_iterations=120;
    constexpr int64_t SCALE=2000000000000000000LL;
    constexpr uint32_t BAD=0xffffffffu;
    const size_t total=size_t(1)<<(2*m);
    vector<uint32_t> index(total,BAD), states; vector<Node> nodes;
    states.reserve(6000000); nodes.reserve(6000000); index[0]=0; states.push_back(0); nodes.push_back({{0,0,0,0},0});
    for(size_t head=0;head<states.size();++head){ uint32_t s=states[head]; Node nd{}; nd.reward_sum=0; for(int uv=0;uv<4;++uv){auto z=step_state(s,uv,w); nd.reward_sum+=z.reward; uint32_t j=index[z.next]; if(j==BAD){j=uint32_t(states.size()); index[z.next]=j; states.push_back(z.next); nodes.push_back({{0,0,0,0},0});} nd.next[uv]=j;} nodes[head]=nd; }
    cerr<<"reachable="<<states.size()<<"\n";
    vector<double> h(states.size(),0.0), hn(states.size(),0.0);
    for(int it=0;it<float_iterations;++it){ for(size_t i=0;i<states.size();++i){auto &nd=nodes[i]; hn[i]=((double)nd.reward_sum+h[nd.next[0]]+h[nd.next[1]]+h[nd.next[2]]+h[nd.next[3]])/4.0;} double base=hn[0]; for(auto &z:hn) z-=base; h.swap(hn); }
    vector<int64_t> H(states.size());
    for(size_t i=0;i<states.size();++i) H[i]=(int64_t) llround(h[i]*(double)SCALE);
    for(int jt=0;jt<int_iterations;++jt){ vector<int64_t> Hn(states.size()); for(size_t i=0;i<states.size();++i){auto &nd=nodes[i]; __int128 a=(__int128)nd.reward_sum*SCALE+H[nd.next[0]]+H[nd.next[1]]+H[nd.next[2]]+H[nd.next[3]]; Hn[i]=(a>=0)?(int64_t)((a+2)/4):(int64_t)(-(((-a)+2)/4));} int64_t base=Hn[0]; for(auto &z:Hn) z-=base; H.swap(Hn); }
    __int128 mn=((__int128)1<<126), mx=-((__int128)1<<126); vector<uint8_t> e(states.size());
    for(size_t i=0;i<states.size();++i){auto &nd=nodes[i]; __int128 num=(__int128)nd.reward_sum*SCALE+H[nd.next[0]]+H[nd.next[1]]+H[nd.next[2]]+H[nd.next[3]]-(__int128)4*H[i]; if(num<mn)mn=num; if(num>mx)mx=num;}
    if(states.size()!=5735086ULL || mn!=(__int128)6238638445311257066LL || mx!=(__int128)6238638445311257073LL){cerr<<"baseline mismatch\n";return 2;}
    for(size_t i=0;i<states.size();++i){auto &nd=nodes[i]; __int128 num=(__int128)nd.reward_sum*SCALE+H[nd.next[0]]+H[nd.next[1]]+H[nd.next[2]]+H[nd.next[3]]-(__int128)4*H[i]; e[i]=(uint8_t)(num-mn);}
    cout<<"baseline_min="<<i128s(mn)<<" baseline_max="<<i128s(mx)<<" span="<<i128s(mx-mn)<<"\n";
    // F_k(s)=4^k P^k e(s), F_0=e, F_{k+1}=sum_a F_k(T_a s).
    vector<__int128> cur(states.size()), nxt(states.size()); for(size_t i=0;i<states.size();++i) cur[i]=e[i];
    __int128 pow4=1;
    __int128 lastspread=-1;
    __int128 final_min=0,final_max=0,final_spread=0,final_pow4=0;
    for(int k=0;k<=62;k++){
      __int128 fmin=cur[0], fmax=cur[0]; uint32_t argmin=0,argmax=0;
      for(size_t i=1;i<cur.size();i++){if(cur[i]<fmin){fmin=cur[i];argmin=i;} if(cur[i]>fmax){fmax=cur[i];argmax=i;}}
      __int128 spread=fmax-fmin;
      long double width=(long double)spread/((long double)4.0L*SCALE*(long double)pow4);
      if(k<=20 || k%5==0 || k>=55) cout<<"k="<<k<<" pow4="<<i128s(pow4)<<" fmin="<<i128s(fmin)<<" fmax="<<i128s(fmax)<<" spread="<<i128s(spread)<<" width="<<setprecision(21)<<(double)width<<" argmin_state="<<states[argmin]<<" argmax_state="<<states[argmax]<<"\n";
      if(lastspread>=0 && spread > 4*lastspread){ cerr<<"span contraction failure at k="<<k<<"\n"; return 7; }
      if(k==62){ final_min=fmin; final_max=fmax; final_spread=spread; final_pow4=pow4; break; }
      for(size_t i=0;i<states.size();i++){auto &nd=nodes[i]; nxt[i]=cur[nd.next[0]]+cur[nd.next[1]]+cur[nd.next[2]]+cur[nd.next[3]];}
      cur.swap(nxt); pow4*=4; lastspread=spread;
    }
    const __int128 EXPECT_MIN=p128("46187259153232832797578610832579588314");
    const __int128 EXPECT_MAX=p128("46187472352913178494458641579756055169");
    const __int128 EXPECT_SPREAD=p128("213199680345696880030747176466855");
    const __int128 EXPECT_POW4=p128("21267647932558653966460912964485513216");
    if(final_min!=EXPECT_MIN || final_max!=EXPECT_MAX || final_spread!=EXPECT_SPREAD || final_pow4!=EXPECT_POW4) return 8;
    if(final_min<=0 || (__int128)7*final_pow4<=final_max) return 9;
    cout<<"k62_exact_width_num="<<i128s(final_spread)<<" denom=8e18*"<<i128s(final_pow4)<<"\n";
    cout<<"strict_inside_one_step_left_margin_num="<<i128s(final_min)<<" right_margin_num="<<i128s((__int128)7*final_pow4-final_max)<<" common_scale=8e18*"<<i128s(final_pow4)<<"\n";
    cout<<"ALL_EXACT_CHECKS_PASS\n";
}
