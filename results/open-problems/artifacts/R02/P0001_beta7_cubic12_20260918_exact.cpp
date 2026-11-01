// Exact unit-weight p-NC checker for all 85 connected simple cubic graphs on 12 vertices.
// Census provenance (read-only public source): austinulrigg/cubic-genus-sql, main,
// data/output/d1/n12/chunk_000000.jsonl blob 72c536d883f82a6d94aa67b419daeeb4c8b92d95
// data/output/d1/n12/chunk_000001.jsonl blob 469a614a4f8f424b0fb996eeeffe30fe93ead2f6
// README blob ba15a17d109f6f2d31ca27d2fec7a55586ce7bf0 states n=12 count is 85 and schema stores g6.
// The checker verifies: 85 distinct codes; each decodes to connected, simple, cubic n=12,m=18;
// then enumerates every one of 2^18 edge subsets, retaining forests, and checks
// Z_e Z_f - Z Z_ef >= 0 exactly for all 153 edge pairs.

#include <bits/stdc++.h>
using namespace std;

struct DSU {
    int p[12], r[12];
    DSU(){ for(int i=0;i<12;i++){p[i]=i;r[i]=0;} }
    int find(int x){ while(p[x]!=x){ p[x]=p[p[x]]; x=p[x]; } return x; }
    bool unite(int a,int b){ a=find(a); b=find(b); if(a==b) return false; if(r[a]<r[b]) swap(a,b); p[b]=a; if(r[a]==r[b]) r[a]++; return true; }
};

vector<pair<int,int>> decode_g6(const string &s){
    if(s.empty()) throw runtime_error("empty graph6");
    int n=(unsigned char)s[0]-63;
    if(n!=12) throw runtime_error("expected n=12");
    vector<int> bits;
    for(size_t k=1;k<s.size();++k){
        int d=(unsigned char)s[k]-63;
        if(d<0||d>63) throw runtime_error("bad graph6 char");
        for(int b=5;b>=0;--b) bits.push_back((d>>b)&1);
    }
    const int need=n*(n-1)/2;
    if((int)bits.size() < need) throw runtime_error("short graph6");
    vector<pair<int,int>> e;
    int t=0;
    for(int j=1;j<n;++j) for(int i=0;i<j;++i) if(bits[t++]) e.push_back({i,j});
    return e;
}

int main(){
    const vector<string> g6 = {
        "K??FEb_F?wD_","K??FEbGL@WB_","K??FEagT@WB_","K??FEaKY@gB_","K??FEaKR@oE_",
        "K?AEF@oM?w@o","K?AEB`gHcoB_","K?AEEHaM@oB_","K?AEEDcF@oF?","K?AEDDWX@oB_",
        "K?ABF@ce?sB_","K?ABEb_J?sB_","K?ABEagE`gH_","K?ABE`Ke@gDO","K?ABE`Ke@WEO",
        "K?ABBb_e?[B_","K?ABBb_E_wP_","K?ABB`gc_wP_","K?ABB`gEcgP_","K?ABCqWUBGCo",
        "K?ABArOb@WEO","K?ABApok?[P_","K?ABApoMCWOo","K?ABApoc`WP_","K?ABArCe@gDO",
        "K?ABCiWRB_DO","K?ABCiWFBOKO","K?ABCiKU@oKO","K?ABEDoM?wP_","K?ABEDWM?wS_",
        "K?ABEESU@WF?","K?ABBF_e?wB_","K?ABBFOe@WB_","K?ABBFOb@oB_","K?ABBFCe@oB_",
        "K?ABCfOY?wD_","K?ABCfOR@oD_","K?ABCfGT@oD_","K?ABCeWU@WK_","K?ABCdWT@WT?",
        "K?ABCfCY?wF?","K?ABCfCU@WF?","K?ABAdoi?wP_","K?ABAdgi?wQ_","K?ABAfCi?wF?",
        "K?AB?vOTDOD_","K?AB?tos@WP_","K?ABCN_U?wF?","K?ABCNOY?wF?","K?BD?qcKaoHG",
        "K?BD?pck?sHG","K?BD?pSw@SBG","K?`@F@gd?sAo","K?`@Eb_M?k@o","K?`@Eb_J?sAo",
        "K?`@Eb_F?[EO","K?`@E`gh?sAo","K?`@E`gFCcCo","K?`@E`gFCKEO","K?`@E`gEcKE_",
        "K?`@E`Wh?kDO","K?`@EaKY?kEO","K?`@EaKX?sEO","K?`@EROM?kCo","K?`@EQgLAcAo",
        "K?`@EQK[?kEO","K?`@Cr_T?[EO","K?`@CrGX?kEO","K?`@CrGT@KEO","K?`@CqW[AKCo",
        "K?`@CrCY?kEO","K?`DAagK_iH_","K?`D@`gE_iW_","K?`D@`cS_wPG","K?`D@bAJAgBG",
        "K?`D@`ae?iH_","K?`D@aQY?wGg","K?`@`ago_YI_","K?`CRAWK`gGg","K?`CPbGP`gEG",
        "K?`CPbGHb_Ag","K?`CPag[?kGg","K?`CPagXAcAg","K?`CPagWagAg","K?`CPagPagEG"
    };
    cout << "P0001 beta<=7 cubic-12 exact certificate\n";
    cout << "graph6_count=" << g6.size() << "\n";
    if(g6.size()!=85){ cerr << "FAIL: expected 85 codes\n"; return 2; }
    set<string> uniq(g6.begin(),g6.end());
    if(uniq.size()!=85){ cerr << "FAIL: duplicate graph6 strings\n"; return 3; }

    long long globalMin = LLONG_MAX;
    int globalGraph=-1, globalI=-1, globalJ=-1;
    int zeroGraphs=0;

    for(size_t gi=0; gi<g6.size(); ++gi){
        auto e = decode_g6(g6[gi]);
        if(e.size()!=18){ cerr << "FAIL g="<<gi<<" edge_count="<<e.size()<<"\n"; return 4; }
        int deg[12]={0};
        set<pair<int,int>> eset;
        DSU conn;
        for(auto [u,v]:e){
            if(u==v){ cerr<<"FAIL loop\n";return 5; }
            if(u>v) swap(u,v);
            if(!eset.insert({u,v}).second){ cerr<<"FAIL multiedge\n"; return 6; }
            deg[u]++;deg[v]++; conn.unite(u,v);
        }
        for(int v=0;v<12;v++) if(deg[v]!=3){ cerr<<"FAIL g="<<gi<<" degree\n";return 7; }
        int root=conn.find(0); for(int v=1;v<12;v++) if(conn.find(v)!=root){ cerr<<"FAIL disconnected\n";return 8; }

        unsigned long long Z=0, Ze[18]={0}, Zef[18][18]{};
        const uint32_t LIM = 1u<<18;
        for(uint32_t mask=0; mask<LIM; ++mask){
            DSU d; bool ok=true;
            uint32_t x=mask;
            while(x){
                int b=__builtin_ctz(x); x&=x-1;
                if(!d.unite(e[b].first,e[b].second)){ ok=false; break; }
            }
            if(!ok) continue;
            ++Z;
            int sel[12], k=0;
            x=mask;
            while(x){ int b=__builtin_ctz(x); x&=x-1; sel[k++]=b; ++Ze[b]; }
            for(int a=0;a<k;a++) for(int b=a+1;b<k;b++){
                int i=sel[a], j=sel[b]; if(i>j) swap(i,j); ++Zef[i][j];
            }
        }
        long long minD=LLONG_MAX; int mi=-1,mj=-1;
        for(int i=0;i<18;i++) for(int j=i+1;j<18;j++){
            __int128 d=(__int128)Ze[i]*Ze[j]-(__int128)Z*Zef[i][j];
            if(d<0){
                cerr << "FAIL negative Rayleigh g="<<gi<<" pair="<<i<<","<<j<<"\n";
                return 9;
            }
            if(d < minD){ minD=(long long)d; mi=i; mj=j; }
        }
        if(minD==0) ++zeroGraphs;
        if(minD<globalMin){ globalMin=minD;globalGraph=(int)gi;globalI=mi;globalJ=mj; }
        cout << "g=" << setw(2) << (gi+1) << " g6=" << g6[gi] << " Z=" << Z
             << " minDelta=" << minD << " pair=" << mi << "," << mj << " PASS\n";
    }
    cout << "zero_min_graphs="<<zeroGraphs<<"\n";
    cout << "global_minDelta="<<globalMin<<" graph="<<(globalGraph+1)<<" pair="<<globalI<<","<<globalJ<<"\n";
    cout << "ALL_85_CUBIC12_EXACT_CHECKS_PASS\n";
    return 0;
}
