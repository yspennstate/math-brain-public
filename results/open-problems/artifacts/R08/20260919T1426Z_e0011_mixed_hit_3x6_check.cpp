#include <bits/stdc++.h>
using namespace std;

int main(){
    constexpr int R=3,C=6,NV=R*C;
    constexpr int FULL=(1<<NV)-1;
    constexpr int OFF=FULL-1;
    constexpr int NST=1+2*OFF;
    constexpr uint64_t SCALE=1000000000ULL;
    constexpr uint64_t BR=144ULL;
    vector<int> nb(NV,0);
    vector<pair<int,int>> edges;
    auto id=[&](int r,int c){return r*C+c;};
    for(int r=0;r<R;r++)for(int c=0;c<C;c++){
        int u=id(r,c);
        const int dr[4]={1,-1,0,0}, dc[4]={0,0,1,-1};
        for(int k=0;k<4;k++){int rr=r+dr[k],cc=c+dc[k];if(0<=rr&&rr<R&&0<=cc&&cc<C)nb[u]|=1<<id(rr,cc);}
        if(c+1<C)edges.push_back({u,id(r,c+1)});
        if(r+1<R)edges.push_back({u,id(r+1,c)});
    }
    for(auto [u,v]:edges) assert((nb[u]&nb[v])==0); // adjacent square-lattice sites have no common neighbour
    auto idxC=[&](int m){return m;};
    auto idxO=[&](int m){return OFF+m;};
    vector<uint32_t> old(NST,0), cur(NST,0);
    auto eachbit=[&](int m, auto f){while(m){int b=__builtin_ctz((unsigned)m);f(b);m&=m-1;}};

    for(int step=1;step<=28;step++){
        {
            __uint128_t num=0;
            int active=2*NV+(int)edges.size();
            for(int u=0;u<NV;u++) num+=(__uint128_t)(2*BR)*old[idxC(1<<u)];
            for(auto [u,v]:edges) num+=(__uint128_t)BR*old[idxO((1<<u)|(1<<v))];
            cur[0]=(uint64_t)(num/(active*BR));
        }
        for(int m=1;m<FULL;m++){
            int vac=FULL^m;
            int k=__builtin_popcount((unsigned)vac);
            int ve=0;for(auto [u,v]:edges)if((vac>>u&1)&&(vac>>v&1))ve++;
            int active=2*k+ve;
            {
                __uint128_t num=0;
                eachbit(vac,[&](int u){int nm=m|(1<<u);if(nm!=FULL)num+=(__uint128_t)(2*BR)*old[idxC(nm)];});
                for(auto [u,v]:edges){
                    if((m>>u&1)||(m>>v&1))continue;
                    int cu=nb[u]&m, cv=nb[v]&m;
                    int du=max(1,__builtin_popcount((unsigned)cu));
                    int dv=max(1,__builtin_popcount((unsigned)cv));
                    assert(BR%(du*dv)==0);
                    int w=BR/(du*dv);
                    if(cu==0 && cv==0){
                        num+=(__uint128_t)BR*SCALE;
                    }else if(cu==0){
                        eachbit(cv,[&](int b){int nm=m&~(1<<b); if(nm) num+=(__uint128_t)w*SCALE; else num+=(__uint128_t)w*old[idxO(1<<u)];});
                    }else if(cv==0){
                        eachbit(cu,[&](int a){int nm=m&~(1<<a); if(nm) num+=(__uint128_t)w*SCALE; else num+=(__uint128_t)w*old[idxO(1<<v)];});
                    }else{
                        eachbit(cu,[&](int a){eachbit(cv,[&](int b){
                            int nm=m&~(1<<a)&~(1<<b);
                            if(nm) num+=(__uint128_t)w*old[idxC(nm)]; else num+=(__uint128_t)w*old[0];
                        });});
                    }
                }
                cur[idxC(m)]=(uint64_t)(num/(active*BR));
            }
            {
                __uint128_t num=0;
                eachbit(vac,[&](int u){
                    int on=nb[u]&m;
                    if(on==0){num+=(__uint128_t)(2*BR)*SCALE;}
                    else{
                        int d=__builtin_popcount((unsigned)on); assert(BR%d==0); int w=BR/d;
                        eachbit(on,[&](int a){int nm=m&~(1<<a); if(nm)num+=(__uint128_t)(2*w)*old[idxO(nm)]; else num+=(__uint128_t)(2*w)*old[0];});
                    }
                });
                for(auto [u,v]:edges){
                    if((m>>u&1)||(m>>v&1))continue;
                    int nm=m|(1<<u)|(1<<v);
                    if(nm!=FULL)num+=(__uint128_t)BR*old[idxO(nm)];
                }
                cur[idxO(m)]=(uint64_t)(num/(active*BR));
            }
        }
        old.swap(cur); fill(cur.begin(),cur.end(),0);
        cout<<"STEP "<<step<<" empty_lower="<<old[0]<<"/"<<SCALE<<" float="<<setprecision(12)<<(double)old[0]/SCALE<<"\n";
    }
    cout<<"states="<<NST<<" rectangle_edges="<<edges.size()<<" branch_scale="<<BR<<"\n";
    cout<<"threshold_scaled="<<(63*SCALE/64)<<"\n";
    if((__uint128_t)64*old[0] <= (__uint128_t)63*SCALE){cerr<<"FAIL threshold not crossed\n";return 2;}
    cout<<"PASS exact downward-rounded R08/E0011 3x6 closed-patch mixed-hit certificate\n";
    cout<<"statement: starting all vacant on closed 3x6, probability of hitting a stable mixed CO/O state before either monochromatic poison, within <=28 effective adsorptions, is >63/64\n";
    cout<<"rounding_grid=1/1000000000; every update is floored, hence every stored value is a rigorous lower bound\n";
    return 0;
}
