// Exact exhaustive audit of HARD8-08 Lemma 5.1 (P19 peer).
// Enumerates all 2^21 simple graphs on 7 labelled vertices.
// Checks independently by exact backtracking that chi(G)>=6 iff complement(G)
// is a subgraph of a star. No randomness / floating point / solver.

#include <array>
#include <cstdint>
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

static vector<pair<int,int>> edges;

bool k_colorable(uint32_t mask, int k) {
    array<uint8_t,7> adj{};
    for (int e=0;e<21;e++) if (mask & (1u<<e)) {
        auto [u,v]=edges[e];
        adj[u] |= uint8_t(1u<<v);
        adj[v] |= uint8_t(1u<<u);
    }
    array<int,7> ord{0,1,2,3,4,5,6};
    sort(ord.begin(), ord.end(), [&](int a,int b){
        return __builtin_popcount((unsigned)adj[a]) > __builtin_popcount((unsigned)adj[b]);
    });
    array<int,7> col; col.fill(-1);
    auto dfs = [&](auto&& self, int pos)->bool {
        if (pos==7) return true;
        int v=ord[pos];
        bool used[7]={false,false,false,false,false,false,false};
        for(int u=0;u<7;u++) if ((adj[v]>>u)&1u) {
            if (col[u]>=0) used[col[u]]=true;
        }
        for(int c=0;c<k;c++) if(!used[c]) {
            col[v]=c;
            if(self(self,pos+1)) return true;
            col[v]=-1;
        }
        return false;
    };
    return dfs(dfs,0);
}

bool complement_subgraph_of_star(uint32_t gmask) {
    const uint32_t ALL=(1u<<21)-1u;
    uint32_t cmask=ALL^gmask;
    if(cmask==0) return true;
    for(int center=0;center<7;center++) {
        bool ok=true;
        for(int e=0;e<21;e++) if(cmask&(1u<<e)) {
            auto [u,v]=edges[e];
            if(u!=center && v!=center) { ok=false; break; }
        }
        if(ok) return true;
    }
    return false;
}

int main(){
    for(int i=0;i<7;i++) for(int j=i+1;j<7;j++) edges.push_back({i,j});
    if(edges.size()!=21) return 2;
    uint64_t count_chi_ge6=0, count_starcomp=0, mismatches=0;
    const uint32_t total=1u<<21;
    for(uint32_t m=0;m<total;m++){
        bool lhs=!k_colorable(m,5);
        bool rhs=complement_subgraph_of_star(m);
        count_chi_ge6 += lhs;
        count_starcomp += rhs;
        if(lhs!=rhs){
            mismatches++;
            if(mismatches<=10) cerr<<"MISMATCH "<<m<<" lhs="<<lhs<<" rhs="<<rhs<<"\n";
        }
    }
    cout<<"P19_LEMMA_5_1_EXHAUSTIVE_AUDIT\n";
    cout<<"LABELLED_GRAPHS_CHECKED "<<total<<"\n";
    cout<<"CHI_GE_6_COUNT "<<count_chi_ge6<<"\n";
    cout<<"COMPLEMENT_STAR_SUBGRAPH_COUNT "<<count_starcomp<<"\n";
    cout<<"MISMATCHES "<<mismatches<<"\n";
    if(mismatches) return 1;
    cout<<"ALL_CHECKS_PASSED\n";
    return 0;
}
