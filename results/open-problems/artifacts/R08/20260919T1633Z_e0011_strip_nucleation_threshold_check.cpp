#include <bits/stdc++.h>
using namespace std;
using u128=__uint128_t;
static constexpr uint64_t SCALE=1000000000ULL;
static constexpr uint64_t BR=144ULL;

enum class Target{Mixed,Poison};
uint64_t solve(int C,int steps,Target target){
    int R=2,NV=2*C,FULL=(1<<NV)-1,OFF=FULL-1,NST=1+2*OFF;
    vector<int> nb(NV,0); vector<pair<int,int>> edges;
    auto id=[&](int r,int c){return r*C+c;};
    for(int r=0;r<R;r++)for(int c=0;c<C;c++){
        int u=id(r,c); const int dr[4]={1,-1,0,0},dc[4]={0,0,1,-1};
        for(int k=0;k<4;k++){int rr=r+dr[k],cc=c+dc[k]; if(0<=rr&&rr<R&&0<=cc&&cc<C) nb[u]|=1<<id(rr,cc);} 
        if(c+1<C) edges.push_back({u,id(r,c+1)}); if(r+1<R) edges.push_back({u,id(r+1,c)});
    }
    for(auto [u,v]:edges) if(nb[u]&nb[v]) throw runtime_error("common neighbour invariant failed");
    auto idxC=[&](int m){return m;}; auto idxO=[&](int m){return OFF+m;};
    auto eachbit=[&](int m, auto f){while(m){int b=__builtin_ctz((unsigned)m); f(b); m&=m-1;}};
    vector<uint32_t> old(NST,0),cur(NST,0);
    const bool wantMixed=(target==Target::Mixed), wantPoison=(target==Target::Poison);
    for(int step=1;step<=steps;step++){
        { u128 num=0; int active=2*NV+(int)edges.size();
          for(int u=0;u<NV;u++) num+=(u128)(2*BR)*old[idxC(1<<u)];
          for(auto [u,v]:edges) num+=(u128)BR*old[idxO((1<<u)|(1<<v))];
          cur[0]=(uint64_t)(num/(active*BR)); }
        for(int m=1;m<FULL;m++){
            int vac=FULL^m,k=__builtin_popcount((unsigned)vac),ve=0;
            for(auto [u,v]:edges)if((vac>>u&1)&&(vac>>v&1))ve++;
            int active=2*k+ve;
            // Pure CO state.
            { u128 num=0;
              eachbit(vac,[&](int u){int nm=m|(1<<u); if(nm==FULL){if(wantPoison)num+=(u128)(2*BR)*SCALE;} else num+=(u128)(2*BR)*old[idxC(nm)];});
              for(auto [u,v]:edges){
                if((m>>u&1)||(m>>v&1))continue;
                int cu=nb[u]&m,cv=nb[v]&m,du=max(1,__builtin_popcount((unsigned)cu)),dv=max(1,__builtin_popcount((unsigned)cv));
                if(BR%(du*dv)) throw runtime_error("branch denominator"); int w=BR/(du*dv);
                if(cu==0&&cv==0){if(wantMixed)num+=(u128)BR*SCALE;}
                else if(cu==0){ eachbit(cv,[&](int b){int nm=m&~(1<<b); if(nm){if(wantMixed)num+=(u128)w*SCALE;} else num+=(u128)w*old[idxO(1<<u)];}); }
                else if(cv==0){ eachbit(cu,[&](int a){int nm=m&~(1<<a); if(nm){if(wantMixed)num+=(u128)w*SCALE;} else num+=(u128)w*old[idxO(1<<v)];}); }
                else { eachbit(cu,[&](int a){eachbit(cv,[&](int b){int nm=m&~(1<<a)&~(1<<b); if(nm)num+=(u128)w*old[idxC(nm)]; else num+=(u128)w*old[0];});}); }
              }
              cur[idxC(m)]=(uint64_t)(num/(active*BR)); }
            // Pure O state.
            { u128 num=0;
              eachbit(vac,[&](int u){int on=nb[u]&m; if(on==0){if(wantMixed)num+=(u128)(2*BR)*SCALE;} else {int d=__builtin_popcount((unsigned)on); if(BR%d)throw runtime_error("branch denominator O");int w=BR/d; eachbit(on,[&](int a){int nm=m&~(1<<a); if(nm)num+=(u128)(2*w)*old[idxO(nm)]; else num+=(u128)(2*w)*old[0];});}});
              for(auto [u,v]:edges){if((m>>u&1)||(m>>v&1))continue; int nm=m|(1<<u)|(1<<v); if(nm==FULL){if(wantPoison)num+=(u128)BR*SCALE;} else num+=(u128)BR*old[idxO(nm)];}
              cur[idxO(m)]=(uint64_t)(num/(active*BR)); }
        }
        old.swap(cur); fill(cur.begin(),cur.end(),0);
    }
    return old[0];
}
int main(){
    cout<<"R08 E0011 sharp thin-strip closed-nucleation threshold checker\n";
    cout<<"scale="<<SCALE<<" branch_scale="<<BR<<"\n";
    uint64_t thr_bad=(SCALE+63)/64; // ceil(1/64 * SCALE)
    uint64_t thr_good=(63*SCALE)/64; // exact 984375000
    cout<<"bad_threshold_1_over_64_scaled="<<thr_bad<<" good_threshold_63_over_64_scaled="<<thr_good<<"\n";
    for(int w=1;w<=8;w++){
        uint64_t p=solve(w,19,Target::Poison);
        cout<<"W="<<w<<" poison_by_19_lower="<<p<<"/"<<SCALE<<" float="<<setprecision(12)<<(double)p/SCALE<<"\n";
        if((u128)64*p <= (u128)SCALE){ cerr<<"FAIL w="<<w<<" poison lower bound does not exceed 1/64\n"; return 2; }
    }
    uint64_t m9=solve(9,35,Target::Mixed);
    cout<<"W=9 mixed_by_35_lower="<<m9<<"/"<<SCALE<<" float="<<setprecision(12)<<(double)m9/SCALE<<"\n";
    if((u128)64*m9 <= (u128)63*SCALE){ cerr<<"FAIL w=9 mixed lower bound does not exceed 63/64\n"; return 3; }
    uint64_t m8=solve(8,35,Target::Mixed);
    cout<<"W=8 mixed_by_35_lower_diagnostic="<<m8<<"/"<<SCALE<<" float="<<setprecision(12)<<(double)m8/SCALE<<"\n";
    uint64_t m10=solve(10,19,Target::Mixed);
    cout<<"W=10 mixed_by_19_lower="<<m10<<"/"<<SCALE<<" float="<<setprecision(12)<<(double)m10/SCALE<<"\n";
    if((u128)64*m10 <= (u128)63*SCALE){ cerr<<"FAIL w=10 mixed lower bound does not exceed 63/64\n"; return 4; }
    cout<<"PASS: every 2xw closed strip with w<=8 has >1/64 probability of monochromatic poison by 19 effective adsorptions; 2x9 has >63/64 probability of hitting a stable mixed state by 35 effective adsorptions before poison.\n";
    cout<<"All updates are downward-rounded to grid 1/1e9, so printed target probabilities are rigorous lower bounds.\n";
}
