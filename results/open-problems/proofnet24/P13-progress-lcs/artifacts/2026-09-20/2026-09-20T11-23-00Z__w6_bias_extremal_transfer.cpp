#include <algorithm>
#include <array>
#include <cstdint>
#include <cmath>
#include <iomanip>
#include <iostream>
#include <limits>
#include <climits>
#include <vector>

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

static void print_i128(__int128 x){ if(x==0){std::cout<<0;return;} if(x<0){std::cout<<'-';x=-x;} char b[64]; int n=0; while(x){b[n++]=char('0'+x%10);x/=10;} while(n--)std::cout<<b[n]; }

int main(){
    constexpr int w=6,m=12,iterations=190; constexpr int64_t SCALE=2000000000000000000LL; // 2e18
    constexpr uint32_t BAD=0xffffffffu;
    const size_t total=size_t(1)<<(2*m);
    std::vector<uint32_t> index(total,BAD), states; std::vector<Node> nodes;
    states.reserve(6000000); nodes.reserve(6000000); index[0]=0; states.push_back(0); nodes.push_back({{0,0,0,0},0});
    for(size_t head=0;head<states.size();++head){ uint32_t s=states[head]; Node nd{}; nd.reward_sum=0; for(int uv=0;uv<4;++uv){auto z=step_state(s,uv,w); nd.reward_sum+=z.reward; uint32_t j=index[z.next]; if(j==BAD){j=uint32_t(states.size()); index[z.next]=j; states.push_back(z.next); nodes.push_back({{0,0,0,0},0});} nd.next[uv]=j;} nodes[head]=nd; }
    std::cerr<<"reachable="<<states.size()<<"\n";
    std::vector<double> h(states.size(),0.0), hn(states.size(),0.0);
    for(int it=0;it<iterations;++it){ for(size_t i=0;i<states.size();++i){auto &nd=nodes[i]; hn[i]=( (double)nd.reward_sum + h[nd.next[0]]+h[nd.next[1]]+h[nd.next[2]]+h[nd.next[3]])/4.0;} double base=hn[0]; for(auto &z:hn) z-=base; h.swap(hn); if(it%20==19){auto mm=std::minmax_element(h.begin(),h.end()); std::cerr<<"iter="<<(it+1)<<" base="<<std::setprecision(21)<<(double)base<<" range=["<<(double)*mm.first<<","<<(double)*mm.second<<"]\n";} }
    std::vector<int64_t> H(states.size()); int64_t Hmin=LLONG_MAX,Hmax=LLONG_MIN;
    for(size_t i=0;i<states.size();++i){ double q=h[i]*(double)SCALE; H[i]=(int64_t) llround(q); Hmin=std::min(Hmin,H[i]); Hmax=std::max(Hmax,H[i]); }

    // Exact integer relative-value refinement: no floating arithmetic here.
    for(int jt=0;jt<120;++jt){
        std::vector<int64_t> Hn(states.size());
        for(size_t i=0;i<states.size();++i){ auto &nd=nodes[i]; __int128 a=(__int128)nd.reward_sum*SCALE + H[nd.next[0]]+H[nd.next[1]]+H[nd.next[2]]+H[nd.next[3]];
            if(a>=0) Hn[i]=(int64_t)((a+2)/4); else Hn[i]=(int64_t)(-(((-a)+2)/4));
        }
        int64_t base=Hn[0]; for(auto &z:Hn) z-=base; H.swap(Hn);
        if(jt%20==19) std::cerr<<"int_refine="<<(jt+1)<<" base="<<base<<"\n";
    }
    Hmin=LLONG_MAX; Hmax=LLONG_MIN; uint32_t Hargmin=0,Hargmax=0; for(size_t i=0;i<H.size();++i){auto z=H[i]; if(z<Hmin){Hmin=z;Hargmin=(uint32_t)i;} if(z>Hmax){Hmax=z;Hargmax=(uint32_t)i;}}

    __int128 mn=((__int128)1<<126), mx=-((__int128)1<<126); uint32_t argmn=0,argmx=0;
    for(size_t i=0;i<states.size();++i){auto &nd=nodes[i]; __int128 num=(__int128)nd.reward_sum*SCALE + H[nd.next[0]]+H[nd.next[1]]+H[nd.next[2]]+H[nd.next[3]] - (__int128)4*H[i]; if(num<mn){mn=num;argmn=i;} if(num>mx){mx=num;argmx=i;} }
    std::cout<<"w=6 reachable="<<states.size()<<" SCALE="<<SCALE<<" iterations="<<iterations<<"\nmin_num=";print_i128(mn);std::cout<<" max_num=";print_i128(mx);std::cout<<" denom=";print_i128((__int128)4*SCALE);std::cout<<"\nwidth_num=";print_i128(mx-mn);std::cout<<"\n";
    long double lower=(long double)mn/(4.0L*SCALE), upper=(long double)mx/(4.0L*SCALE);
    std::cout<<std::setprecision(21)<<"lower="<<(double)lower<<" upper="<<(double)upper<<" width="<<(double)(upper-lower)<<"\n";
    std::cout<<"argmin_residual_state="<<states[argmn]<<" argmax_residual_state="<<states[argmx]<<"\nHmin="<<Hmin<<" Hmax="<<Hmax<<" Hosc="<<(Hmax-Hmin)<<"\nHargmin_state="<<states[Hargmin]<<" Hargmax_state="<<states[Hargmax]<<"\n";
    const __int128 EXPECT_MIN = (__int128)6238638445311257066LL;
    const __int128 EXPECT_MAX = (__int128)6238638445311257073LL;
    const int64_t EXPECT_HMIN = -417968688415616699LL;
    const int64_t EXPECT_HMAX = 7863814844147315928LL;
    const __int128 DEN = (__int128)4*SCALE;
    const __int128 L_SCALED_NUM = (__int128)6341327936000000000LL;
    std::cout<<"L_minus_upper_num="; print_i128(L_SCALED_NUM-mx); std::cout<<" common_denom="; print_i128(DEN); std::cout<<"\n";
    std::cout<<"old_width_over_new_width=34000/7\n";
    std::cout<<std::setprecision(18)
             <<"z0_lower_boundary_coeff="<<(double)((long double)Hmax/SCALE)
             <<" z0_upper_boundary_coeff="<<(double)((long double)(-Hmin)/SCALE)
             <<" total_boundary_coeff="<<(double)((long double)(Hmax-Hmin)/SCALE)<<"\n";
    if(states.size()!=5735086ULL) return 2;
    if(mn!=EXPECT_MIN || mx!=EXPECT_MAX) return 3;
    if(Hmin!=EXPECT_HMIN || Hmax!=EXPECT_HMAX) return 4;
    if(L_SCALED_NUM<=mx) return 5;
    if(H[0]!=0) return 6;
    if(H[Hargmin]!=Hmin || H[Hargmax]!=Hmax) return 7;
    std::cout<<"ALL_EXACT_CHECKS_PASS\n";
}
