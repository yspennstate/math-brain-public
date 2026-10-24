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
    uint32_t xp=(x>>1)|(uint32_t(u)<<(m-1));
    return{xp|(gp<<m),(uint8_t)(Q[w]-V[w])};
}
static inline uint32_t qid(uint32_t s){
    // Full width 7 has fourteen raw-X and fourteen gradient bits.
    // Retain the twelve interior bits of each kind.  The omitted left pair
    // enters only through c_v=(1-g_0)1{x_0=v}, encoded by c=0,1,2, and the
    // omitted right pair is retained verbatim.
    uint32_t x=s&((1u<<14)-1), g=(s>>14)&((1u<<14)-1);
    uint32_t corex=(x>>1)&4095u, coreg=(g>>1)&4095u;
    uint32_t c;
    if(g&1u) c=0; else c=(x&1u)?2u:1u;
    uint32_t r=((x>>13)&1u) | (((g>>13)&1u)<<1);
    return corex | (coreg<<12) | (c<<24) | (r<<26);
}
int main(){
    size_t total=1ull<<28;
    vector<uint64_t> vis((total+63)/64), qvis((total+63)/64);
    vector<uint32_t> q; q.reserve(67000000);
    auto seen=[&](uint32_t s){return(vis[s>>6]>>(s&63))&1ull;};
    auto mark=[&](uint32_t s){vis[s>>6]|=1ull<<(s&63);};
    auto qseen=[&](uint32_t s){return(qvis[s>>6]>>(s&63))&1ull;};
    auto qmark=[&](uint32_t s){qvis[s>>6]|=1ull<<(s&63);};
    mark(0); q.push_back(0); size_t qc=0;
    for(size_t h=0;h<q.size();h++){
        uint32_t s=q[h], z=qid(s);
        if(!qseen(z)){qmark(z);qc++;}
        for(int a=0;a<4;a++){
            auto t=st(s,a,7).next;
            if(!seen(t)){mark(t);q.push_back(t);}
        }
    }
    if(q.size()!=66008456ULL) return 2;
    if(qc!=56219024ULL) return 3;
    cout<<"R7="<<q.size()<<" quotient_distinct="<<qc
        <<" collapse="<<(q.size()-qc)
        <<" ratio="<<setprecision(15)<<double(qc)/q.size()<<"\n";
    cout<<"ALL_EXACT_CHECKS_PASS\n";
}
