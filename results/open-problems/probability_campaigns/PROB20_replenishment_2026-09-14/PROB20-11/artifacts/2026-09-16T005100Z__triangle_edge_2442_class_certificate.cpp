#include <bits/stdc++.h>
using namespace std;

// PROB20-11 exact certificate for the canonical K=4 state
//   active parities 00011, close distances (2,4,4,2), n_even=6,
//   third-Bonferroni half bounds U=(1031,1058).
// It proves that no completion exists by exhaustive folded-cube enumeration.
// Standard C++17 only; integer arithmetic only; no solver/time-limit semantics.

static constexpr int N=2048, W=32;
using BS=array<unsigned long long,W>;
BS ball[N];
int trimaxv[2][2][2][7][7][7][2];

inline int fd(int a,int b){ int w=__builtin_popcount((unsigned)(a^b)); return min(w,12-w); }
inline int parity(int x){ return __builtin_popcount((unsigned)x)&1; }

int triple_half(int a,int b,int c,int h){
    int s=0;
    for(int q=0;q<W;q++){
        unsigned long long v=ball[a][q]&ball[b][q]&ball[c][q];
        while(v){
            int t=__builtin_ctzll(v), z=64*q+t;
            if(z<N && parity(z)==h) ++s;
            v&=v-1;
        }
    }
    return s;
}

long long choose3(int n){ return n>=3 ? 1LL*n*(n-1)*(n-2)/6 : 0; }

int deficit(const vector<int>& cs,int h){
    int ans=0;
    for(int i=0;i<(int)cs.size();i++) for(int j=i+1;j<(int)cs.size();j++) for(int k=j+1;k<(int)cs.size();k++){
        int a=cs[i],b=cs[j],c=cs[k];
        int mx=trimaxv[parity(a)][parity(b)][parity(c)][fd(a,b)][fd(a,c)][fd(b,c)][h];
        assert(mx>=0);
        int ac=triple_half(a,b,c,h);
        assert(ac<=mx);
        ans += mx-ac;
    }
    return ans;
}

int excess(const vector<int>& cs,int h){
    int ans=0;
    for(int z=0;z<N;z++) if(parity(z)==h){
        int m=0;
        for(int c:cs) if(fd(c,z)<=3) ++m;
        if(m>0) ans += (int)choose3(m-1);
    }
    return ans;
}

int cost(const vector<int>& cs,int h){ return deficit(cs,h)+excess(cs,h); }

// A complete orbit invariant for the normalized active configuration.
// Rows are the two nonzero normalized triangle vertices and the two endpoints
// of the odd close edge. Coordinate permutations merely permute the 12 column
// patterns. Independent row complementation does not change a folded center,
// and swapping the two odd-edge endpoints preserves the labeled geometry.
string orbit_key(int r0,int r1,int x,int y){
    int rows[4]={r0,r1,x,y}, hist[16]={0};
    for(int col=0;col<12;col++){
        int p=0;
        for(int i=0;i<4;i++) p|=((rows[i]>>col)&1)<<i;
        ++hist[p];
    }
    string best; bool init=false;
    for(int flip=0;flip<16;flip++) for(int sw=0;sw<2;sw++){
        int q[16]={0};
        for(int p=0;p<16;p++) if(hist[p]){
            int v=p^flip, bits[4];
            for(int i=0;i<4;i++) bits[i]=(v>>i)&1;
            if(sw) swap(bits[2],bits[3]);
            int u=0; for(int i=0;i<4;i++) u|=bits[i]<<i;
            q[u]+=hist[p];
        }
        string s(16,'\0'); for(int i=0;i<16;i++) s[i]=(char)q[i];
        if(!init || s<best){best=s;init=true;}
    }
    return best;
}

struct Orbit { int x=-1,y=-1,size=0; };

vector<int> even_isolate_pool(const vector<int>& active){
    vector<int> out;
    for(int z=0;z<N;z++) if(parity(z)==0){
        bool ok=true;
        for(int c:active){
            int need = parity(c)==0 ? 6 : 5;
            if(fd(z,c)!=need){ok=false;break;}
        }
        if(ok) out.push_back(z);
    }
    return out;
}

int max_even_extension(const vector<int>& active,const vector<int>& pool){
    int best=0;
    function<void(vector<int>&,int)> rec=[&](vector<int>& chosen,int start){
        best=max(best,(int)chosen.size());
        for(int i=start;i<(int)pool.size();i++){
            int z=pool[i];
            bool ok=true;
            for(int q:chosen) if(fd(z,q)!=6){ok=false;break;}
            if(!ok) continue;
            vector<int> cs=active;
            cs.insert(cs.end(),chosen.begin(),chosen.end());
            cs.push_back(z);
            // For this canonical class the exact half budgets are
            // U_E-1024 = 7 and U_O-1024 = 34.
            if(cost(cs,0)>7 || cost(cs,1)>34) continue;
            chosen.push_back(z);
            rec(chosen,i+1);
            chosen.pop_back();
        }
    };
    vector<int> chosen;
    rec(chosen,0);
    return best;
}

int main(){
    // Folded radius-3 balls in F_2^12/<1>, represented by 11-bit words.
    for(int c=0;c<N;c++){
        ball[c].fill(0);
        for(int z=0;z<N;z++) if(fd(c,z)<=3) ball[c][z>>6] |= 1ULL<<(z&63);
    }

    // Exact orbitwise maxima for triple intersections on each parity half.
    memset(trimaxv,0xff,sizeof(trimaxv));
    for(int b=1;b<N;b++) for(int c=b+1;c<N;c++){
        int v[3]={0,b,c}, p[3]={0,parity(b),parity(c)}, D[3][3];
        for(int i=0;i<3;i++) for(int j=0;j<3;j++) D[i][j]=fd(v[i],v[j]);
        int ac[2]={triple_half(0,b,c,0),triple_half(0,b,c,1)};
        int idx[3]={0,1,2};
        do{
            for(int h=0;h<2;h++){
                int &m=trimaxv[p[idx[0]]][p[idx[1]]][p[idx[2]]]
                    [D[idx[0]][idx[1]]][D[idx[0]][idx[2]]][D[idx[1]][idx[2]]][h];
                m=max(m,ac[h]);
            }
        }while(next_permutation(idx,idx+3));
        int pc[3]={1-p[0],1-p[1],1-p[2]}; idx[0]=0;idx[1]=1;idx[2]=2;
        do{
            int &m0=trimaxv[pc[idx[0]]][pc[idx[1]]][pc[idx[2]]]
                [D[idx[0]][idx[1]]][D[idx[0]][idx[2]]][D[idx[1]][idx[2]]][0];
            int &m1=trimaxv[pc[idx[0]]][pc[idx[1]]][pc[idx[2]]]
                [D[idx[0]][idx[1]]][D[idx[0]][idx[2]]][D[idx[1]][idx[2]]][1];
            m0=max(m0,ac[1]); m1=max(m1,ac[0]);
        }while(next_permutation(idx,idx+3));
    }

    // Normalize the even (2,4,4) triangle to 0,3,29.
    vector<int> tri={0,3,29};
    assert(fd(0,3)==2 && fd(0,29)==4 && fd(3,29)==4);

    // Odd endpoints of the disjoint close edge must both be at cross-distance 5.
    vector<int> odd;
    for(int x=0;x<N;x++) if(parity(x)==1 && fd(x,0)==5 && fd(x,3)==5 && fd(x,29)==5) odd.push_back(x);
    assert(odd.size()==518);

    long long raw=0, survivors=0;
    map<string,Orbit> orbits;
    map<pair<int,int>,int> costdist;
    for(int i=0;i<(int)odd.size();i++) for(int j=i+1;j<(int)odd.size();j++) if(fd(odd[i],odd[j])==2){
        ++raw;
        vector<int> active=tri; active.push_back(odd[i]); active.push_back(odd[j]);
        int ce=cost(active,0), co=cost(active,1);
        ++costdist[{ce,co}];
        if(ce<=7){
            ++survivors;
            string key=orbit_key(3,29,odd[i],odd[j]);
            auto &o=orbits[key];
            if(o.size==0){o.x=odd[i];o.y=odd[j];}
            ++o.size;
        }
    }
    assert(raw==10878);
    assert(survivors==2058);
    assert(orbits.size()==7);

    vector<array<int,5>> stats;
    for(auto &kv:orbits){
        Orbit o=kv.second;
        vector<int> active={0,3,29,o.x,o.y};
        auto pool=even_isolate_pool(active);
        int mx=max_even_extension(active,pool);
        stats.push_back({o.size,cost(active,0),cost(active,1),(int)pool.size(),mx});
    }
    sort(stats.begin(),stats.end());
    const vector<array<int,5>> expected={
        {63,3,5,50,2},
        {105,5,9,54,2},
        {105,7,15,58,2},
        {210,7,15,48,2},
        {315,5,8,56,2},
        {630,6,11,59,2},
        {630,7,15,58,2}
    };
    assert(stats==expected);

    cout << "CERTIFICATE PASSED\n";
    cout << "canonical class: 00011 (2,4,4,2), n_even=6, U=(1031,1058)\n";
    cout << "odd cross-distance-5 vertices = 518\n";
    cout << "raw odd d=2 edges = 10878\n";
    cout << "active states within even-half budget 7 = 2058\n";
    cout << "complete stabilizer orbits = 7\n";
    for(auto s:stats)
        cout << "orbit size="<<s[0]<<" active_cost=("<<s[1]<<","<<s[2]<<") even_pool="<<s[3]<<" max_budget_feasible_even_extension="<<s[4]<<"\n";
    cout << "Every orbit permits at most two of the three required additional even centers.\n";
    cout << "CONCLUSION: this canonical K=4 class is impossible.\n";
}
