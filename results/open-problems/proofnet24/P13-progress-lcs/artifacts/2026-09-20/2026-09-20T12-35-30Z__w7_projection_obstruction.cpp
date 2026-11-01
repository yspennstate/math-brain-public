#include <bits/stdc++.h>
using namespace std;
struct SR{uint32_t next;uint8_t reward;};
static inline SR st(uint32_t state,int uv,int w){
    int m=2*w; uint32_t mask=(1u<<m)-1; uint32_t x=state&mask,g=(state>>m)&mask;
    int u=(uv>>1)&1,v=uv&1; int V[32]; V[0]=0;
    for(int i=0;i<m;i++) V[i+1]=V[i]+((g>>i)&1);
    int Q[32]; int a0=(((x>>0)&1)==v); Q[0]=max(V[1],V[0]+a0);
    for(int k=1;k<m;k++){int ak=(((x>>k)&1)==v);Q[k]=max({Q[k-1],V[k]+ak,V[k+1]});}
    int am=(u==v); Q[m]=max(Q[m-1],V[m]+am); uint32_t gp=0;
    for(int i=0;i<m;i++) if(Q[i+1]-Q[i]) gp|=1u<<i;
    uint32_t xp=(x>>1)|(uint32_t(u)<<(m-1)); return{xp|(gp<<m),(uint8_t)(Q[w]-V[w])};
}
// Right-anchored width-6 projection of width-7 state: retain positions 3..14.
static inline uint32_t pr(uint32_t s){uint32_t M=(1u<<14)-1,x=s&M,g=(s>>14)&M;return ((x>>2)&4095)|(((g>>2)&4095)<<12);}
int main(){
    vector<uint8_t> r6(1u<<24); vector<uint32_t> q6; q6.reserve(6000000); r6[0]=1; q6.push_back(0);
    for(size_t h=0;h<q6.size();h++) for(int a=0;a<4;a++){auto t=st(q6[h],a,6).next;if(!r6[t]){r6[t]=1;q6.push_back(t);}}
    cout<<"R6="<<q6.size()<<"\n";
    size_t total=1ull<<28; vector<uint64_t> vis((total+63)/64); vector<uint32_t> q; q.reserve(67000000);
    auto seen=[&](uint32_t s){return(vis[s>>6]>>(s&63))&1ull;}; auto mark=[&](uint32_t s){vis[s>>6]|=1ull<<(s&63);};
    mark(0); q.push_back(0); vector<uint8_t> pset(1u<<24); size_t badocc=0;
    for(size_t h=0;h<q.size();h++){uint32_t s=q[h],p=pr(s);pset[p]=1;if(!r6[p])badocc++;for(int a=0;a<4;a++){auto t=st(s,a,7).next;if(!seen(t)){mark(t);q.push_back(t);}}}
    vector<uint32_t> outs; size_t pcount=0; for(uint32_t p=0;p<(1u<<24);p++) if(pset[p]){pcount++; if(!r6[p])outs.push_back(p);}
    cout<<"R7="<<q.size()<<" proj_distinct="<<pcount<<" bad_distinct="<<outs.size()<<" bad_occ="<<badocc<<"\n";
    long long toR=0,toOut=0,toOther=0;
    for(auto p:outs) for(int a=0;a<4;a++){auto t=st(p,a,6).next;if(r6[t])toR++;else if(pset[t])toOut++;else toOther++;}
    cout<<"outs="<<outs.size()<<" edges_to_R6="<<toR<<" edges_to_out="<<toOut<<" edges_to_other="<<toOther<<"\n";
    vector<uint8_t> good=r6; size_t rem=outs.size();
    for(int d=1;d<=30;d++){size_t add=0;for(auto p:outs) if(!good[p]){bool ok=true;for(int a=0;a<4;a++) if(!good[st(p,a,6).next]){ok=false;break;}if(ok){good[p]=2;add++;}}for(auto p:outs)if(good[p]==2)good[p]=1;rem-=add;cout<<"peel_depth="<<d<<" add="<<add<<" rem="<<rem<<"\n";if(!add)break;}
    long long f1=0,f2=0,fx=0,none=0;
    for(auto p:outs){uint32_t x=p&4095,g=p>>12; bool ok1=false,ok2=false,okx=false;
        for(int b=0;b<2;b++){uint32_t gg=(g&~1u)|b;if(r6[x|(gg<<12)])ok1=true;}
        for(int mask=0;mask<4;mask++){uint32_t gg=(g&~3u)|mask;if(r6[x|(gg<<12)])ok2=true;}
        for(int xb=0;xb<4;xb++){uint32_t xx=(x&~3u)|xb;if(r6[xx|(g<<12)])okx=true;}
        if(ok1)f1++; else if(ok2)f2++; else if(okx)fx++; else none++;
    }
    cout<<"map_flip_g1="<<f1<<" additional_g12="<<f2<<" additional_x12="<<fx<<" none="<<none<<"\n";
    if(q6.size()!=5735086ULL || q.size()!=66008456ULL || outs.size()!=64202ULL || badocc!=183840ULL) return 2;
    if(toR!=231094 || toOut!=25636 || toOther!=78) return 3;
    if(rem!=2706) return 4;
    if(f1!=43818 || f2!=17892 || fx!=2104 || none!=388) return 5;
    cout<<"ALL_EXACT_CHECKS_PASS\n";
}
