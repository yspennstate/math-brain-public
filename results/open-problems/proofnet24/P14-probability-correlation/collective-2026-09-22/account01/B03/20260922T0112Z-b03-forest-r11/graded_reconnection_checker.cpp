#include <bits/stdc++.h>
using namespace std;

static bool is_forest_mask(int n, const vector<pair<int,int>>& E, int mask){
    int p[8]; iota(p,p+n,0);
    auto find=[&](int x){ while(p[x]!=x){p[x]=p[p[x]]; x=p[x];} return x; };
    for(int k=0;k<(int)E.size();k++) if(mask>>k&1){
        int a=find(E[k].first), b=find(E[k].second);
        if(a==b) return false;
        p[a]=b;
    }
    return true;
}

int main(){
    cout << "FOREST_GRADED_RECONNECTION_EXACT_CHECK\n";
    long long total_instances=0;
    for(int n=2;n<=6;n++){
        vector<pair<int,int>> E;
        for(int i=0;i<n;i++) for(int j=i+1;j<n;j++) E.push_back({i,j});
        const int M=E.size(), S=1<<M;
        vector<unsigned char> forest(S), pc(S);
        for(int mask=0;mask<S;mask++){
            pc[mask]=__builtin_popcount((unsigned)mask);
            forest[mask]=is_forest_mask(n,E,mask);
        }
        long long instances=0, negative=0, positive_coeffs=0;
        for(int G=0;G<S;G++){
            if(pc[G]<2) continue;
            for(int e=0;e<M;e++) if(G>>e&1)
            for(int f=e+1;f<M;f++) if(G>>f&1){
                int K=G & ~(1<<e) & ~(1<<f);
                long long N[32]={},A[32]={},B[32]={},C[32]={};
                for(int H=K;;H=(H-1)&K){
                    if(forest[H]){
                        int k=pc[H];
                        N[k]++;
                        if(forest[H|(1<<e)]) A[k]++;
                        if(forest[H|(1<<f)]) B[k]++;
                        if(forest[H|(1<<e)|(1<<f)]) C[k]++;
                    }
                    if(H==0) break;
                }
                for(int s=0;s<=2*M;s++){
                    long long d=0;
                    for(int i=0;i<=M;i++){
                        int j=s-i; if(j<0||j>M) continue;
                        d += A[i]*B[j] - N[i]*C[j];
                    }
                    if(d<0){
                        negative++;
                        cout << "NEGATIVE n="<<n<<" Gmask="<<G<<" e="<<e<<" f="<<f<<" degree="<<s<<" value="<<d<<"\n";
                        return 2;
                    }
                    if(d>0) positive_coeffs++;
                }
                instances++;
            }
        }
        total_instances += instances;
        cout << "n="<<n<<" pair_instances="<<instances<<" negative_coefficients="<<negative<<" positive_coefficients="<<positive_coeffs<<"\n";
    }

    // Exact fixed-multiplicity obstruction in K4, e=01, f=23.
    {
        int n=4; vector<pair<int,int>> E;
        for(int i=0;i<n;i++)for(int j=i+1;j<n;j++)E.push_back({i,j});
        auto idx=[&](pair<int,int> x){ if(x.first>x.second) swap(x.first,x.second); for(int k=0;k<(int)E.size();k++) if(E[k]==x) return k; return -1; };
        int e=idx({0,1}), f=idx({2,3});
        int K=((1<<(int)E.size())-1) & ~(1<<e) & ~(1<<f);
        long long domain=0,codomain=0;
        for(int F=K;;F=(F-1)&K){
            if(!is_forest_mask(n,E,F)){ if(F==0)break; else continue; }
            int H=K^F; // multiplicity exactly one for every K edge
            if(is_forest_mask(n,E,H)){
                if(is_forest_mask(n,E,H|(1<<e)|(1<<f))) domain++;
                if(is_forest_mask(n,E,F|(1<<e)) && is_forest_mask(n,E,H|(1<<f))) codomain++;
            }
            if(F==0) break;
        }
        cout << "K4_opposite_allMultiplicity1_domain_NC="<<domain<<" codomain_AB="<<codomain<<"\n";
        if(domain!=4 || codomain!=2) return 3;
    }

    cout << "total_pair_instances_n_le_6="<<total_instances<<"\n";
    cout << "ALL_EXACT_ASSERTIONS_PASSED\n";
    return 0;
}
