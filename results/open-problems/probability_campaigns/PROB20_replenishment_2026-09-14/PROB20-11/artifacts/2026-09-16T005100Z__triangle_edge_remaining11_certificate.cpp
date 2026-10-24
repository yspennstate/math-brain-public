#include <bits/stdc++.h>
using namespace std;

// PROB20-11 exact certificate eliminating the eleven K=4 triangle+disjoint-edge
// canonical states left after the 2026-09-15 checkpoints.
// Standard C++17, integer/exhaustive folded-cube computation only.

static constexpr int N=2048, W=32;
using BS=array<unsigned long long,W>;
BS ball[N];
int TM[2][2][2][7][7][7][2];

inline int fd(int a,int b){int w=__builtin_popcount((unsigned)(a^b)); return min(w,12-w);} 
inline int pa(int x){return __builtin_popcount((unsigned)x)&1;}

int triple_half(int a,int b,int c,int h){
    int s=0;
    for(int q=0;q<W;q++){
        unsigned long long v=ball[a][q]&ball[b][q]&ball[c][q];
        while(v){int t=__builtin_ctzll(v), z=64*q+t; if(z<N&&pa(z)==h) ++s; v&=v-1;}
    }
    return s;
}
long long C3(int n){return n>=3?1LL*n*(n-1)*(n-2)/6:0;}
int deficit(const vector<int>&cs,int h){
    int ans=0;
    for(int i=0;i<(int)cs.size();i++)for(int j=i+1;j<(int)cs.size();j++)for(int k=j+1;k<(int)cs.size();k++){
        int a=cs[i],b=cs[j],c=cs[k];
        int mx=TM[pa(a)][pa(b)][pa(c)][fd(a,b)][fd(a,c)][fd(b,c)][h];
        int ac=triple_half(a,b,c,h); assert(mx>=ac); ans+=mx-ac;
    }
    return ans;
}
int excess(const vector<int>&cs,int h){
    int ans=0;
    for(int z=0;z<N;z++) if(pa(z)==h){
        int m=0; for(int c:cs) if(fd(c,z)<=3) ++m;
        if(m) ans+=(int)C3(m-1);
    }
    return ans;
}
int cost(const vector<int>&cs,int h){return deficit(cs,h)+excess(cs,h);} 

// Complete equivalence invariant under coordinate permutations, independent row
// complementation (same folded centers), optional swap of the two normalized
// nonzero triangle rows, and swap of the close-edge endpoints.
string orbit_key(int r0,int r1,int x,int y,bool swapTri){
    int r[4]={r0,r1,x,y}, hist[16]={0};
    for(int col=0;col<12;col++){int p=0;for(int i=0;i<4;i++)p|=((r[i]>>col)&1)<<i; ++hist[p];}
    string best; bool init=false;
    for(int flip=0;flip<16;flip++) for(int st=0;st<(swapTri?2:1);st++) for(int se=0;se<2;se++){
        int q[16]={0};
        for(int p=0;p<16;p++) if(hist[p]){
            int v=p^flip,b[4]; for(int i=0;i<4;i++) b[i]=(v>>i)&1;
            if(st) swap(b[0],b[1]); if(se) swap(b[2],b[3]);
            int u=0;for(int i=0;i<4;i++)u|=b[i]<<i; q[u]+=hist[p];
        }
        string s(16,'\0');for(int i=0;i<16;i++)s[i]=(char)q[i];
        if(!init||s<best){best=s;init=true;}
    }
    return best;
}
struct Orb{int x=-1,y=-1,n=0;};

vector<int> isolate_pool(const vector<int>&active,int p){
    vector<int> out;
    for(int z=0;z<N;z++) if(pa(z)==p){
        bool ok=true;
        for(int c:active){int need=(pa(c)==p?6:5); if(fd(z,c)!=need){ok=false;break;}}
        if(ok) out.push_back(z);
    }
    return out;
}
int max_extension(const vector<int>&active,const vector<int>&pool,int b0,int b1){
    int best=0;
    function<void(vector<int>&,int)> rec=[&](vector<int>&ch,int st){
        best=max(best,(int)ch.size());
        for(int i=st;i<(int)pool.size();i++){
            int z=pool[i]; bool ok=true; for(int q:ch) if(fd(z,q)!=6){ok=false;break;} if(!ok) continue;
            vector<int> cs=active; cs.insert(cs.end(),ch.begin(),ch.end()); cs.push_back(z);
            if(cost(cs,0)>b0||cost(cs,1)>b1) continue;
            ch.push_back(z); rec(ch,i+1); ch.pop_back();
        }
    };
    vector<int> ch; rec(ch,0); return best;
}

struct Summary{long long raw=0,surv=0;int orbits=0,maxext=-1,min0=1e9,min1=1e9;};

Summary run_odd_edge(const string&name,const vector<int>&T,int edgeDist,int b0,int b1,bool swapTri){
    vector<int> odd;
    for(int x=0;x<N;x++) if(pa(x)==1&&fd(x,T[0])==5&&fd(x,T[1])==5&&fd(x,T[2])==5) odd.push_back(x);
    map<string,Orb> om; Summary S;
    for(int i=0;i<(int)odd.size();i++)for(int j=i+1;j<(int)odd.size();j++)if(fd(odd[i],odd[j])==edgeDist){
        ++S.raw; vector<int>a=T;a.push_back(odd[i]);a.push_back(odd[j]); int c0=cost(a,0),c1=cost(a,1);S.min0=min(S.min0,c0);S.min1=min(S.min1,c1);
        if(c0<=b0&&c1<=b1){++S.surv; auto&o=om[orbit_key(T[1],T[2],odd[i],odd[j],swapTri)];if(!o.n){o.x=odd[i];o.y=odd[j];}++o.n;}
    }
    S.orbits=om.size(); S.maxext=0;
    for(auto &kv:om){auto o=kv.second;vector<int>a=T;a.push_back(o.x);a.push_back(o.y);auto p=isolate_pool(a,0);S.maxext=max(S.maxext,max_extension(a,p,b0,b1));}
    cout<<name<<": raw="<<S.raw<<" active_survivors="<<S.surv<<" orbits="<<S.orbits<<" max_even_extension="<<S.maxext<<"\n";
    return S;
}

Summary run_even_edge(const string&name,const vector<int>&T,int edgeDist,int b0,int b1,bool swapTri){
    vector<int> ev;
    for(int x=0;x<N;x++) if(pa(x)==0 && x!=T[0]&&x!=T[1]&&x!=T[2] && fd(x,T[0])==6&&fd(x,T[1])==6&&fd(x,T[2])==6) ev.push_back(x);
    map<string,Orb> om; Summary S;
    for(int i=0;i<(int)ev.size();i++)for(int j=i+1;j<(int)ev.size();j++)if(fd(ev[i],ev[j])==edgeDist){
        ++S.raw;vector<int>a=T;a.push_back(ev[i]);a.push_back(ev[j]);int c0=cost(a,0),c1=cost(a,1);S.min0=min(S.min0,c0);S.min1=min(S.min1,c1);
        if(c0<=b0&&c1<=b1){++S.surv;auto&o=om[orbit_key(T[1],T[2],ev[i],ev[j],swapTri)];if(!o.n){o.x=ev[i];o.y=ev[j];}++o.n;}
    }
    S.orbits=om.size();S.maxext=0;
    for(auto&kv:om){auto o=kv.second;vector<int>a=T;a.push_back(o.x);a.push_back(o.y);auto p=isolate_pool(a,1);S.maxext=max(S.maxext,max_extension(a,p,b0,b1));}
    cout<<name<<": raw="<<S.raw<<" active_survivors="<<S.surv<<" orbits="<<S.orbits<<" max_odd_extension="<<S.maxext<<" min_active_cost=("<<S.min0<<","<<S.min1<<")\n";
    return S;
}

Summary run_mixed_2223(const vector<int>&T,int b0,int b1){
    vector<int> ev;for(int x=0;x<N;x++)if(pa(x)==0&&x!=T[0]&&x!=T[1]&&x!=T[2]&&fd(x,T[0])==6&&fd(x,T[1])==6&&fd(x,T[2])==6)ev.push_back(x);
    Summary S;
    for(int x:ev)for(int y=0;y<N;y++)if(pa(y)==1&&fd(y,T[0])==5&&fd(y,T[1])==5&&fd(y,T[2])==5&&fd(x,y)==3){
        ++S.raw;vector<int>a=T;a.push_back(x);a.push_back(y);int c0=cost(a,0),c1=cost(a,1);S.min0=min(S.min0,c0);S.min1=min(S.min1,c1);if(c0<=b0&&c1<=b1)++S.surv;
    }
    cout<<"00001 2223 ne5: raw="<<S.raw<<" active_survivors="<<S.surv<<" min_active_cost=("<<S.min0<<","<<S.min1<<")\n";return S;
}

int main(){
    for(int c=0;c<N;c++){ball[c].fill(0);for(int z=0;z<N;z++)if(fd(c,z)<=3)ball[c][z>>6]|=1ULL<<(z&63);}
    memset(TM,0xff,sizeof(TM));
    for(int b=1;b<N;b++)for(int c=b+1;c<N;c++){
        int v[3]={0,b,c},p[3]={0,pa(b),pa(c)},D[3][3];for(int i=0;i<3;i++)for(int j=0;j<3;j++)D[i][j]=fd(v[i],v[j]);int ac[2]={triple_half(0,b,c,0),triple_half(0,b,c,1)},id[3]={0,1,2};
        do{for(int h=0;h<2;h++){int&m=TM[p[id[0]]][p[id[1]]][p[id[2]]][D[id[0]][id[1]]][D[id[0]][id[2]]][D[id[1]][id[2]]][h];m=max(m,ac[h]);}}while(next_permutation(id,id+3));
        int pc[3]={1-p[0],1-p[1],1-p[2]};id[0]=0;id[1]=1;id[2]=2;
        do{int&m0=TM[pc[id[0]]][pc[id[1]]][pc[id[2]]][D[id[0]][id[1]]][D[id[0]][id[2]]][D[id[1]][id[2]]][0];int&m1=TM[pc[id[0]]][pc[id[1]]][pc[id[2]]][D[id[0]][id[1]]][D[id[0]][id[2]]][D[id[1]][id[2]]][1];m0=max(m0,ac[1]);m1=max(m1,ac[0]);}while(next_permutation(id,id+3));
    }
    vector<int>T244={0,3,29},T224={0,3,12},T222={0,3,5};
    assert(fd(0,3)==2&&fd(0,29)==4&&fd(3,29)==4);
    assert(fd(0,3)==2&&fd(0,12)==2&&fd(3,12)==4);
    assert(fd(0,3)==2&&fd(0,5)==2&&fd(3,5)==2);

    auto A=run_odd_edge("00011 2442 ne6",T244,2,7,34,false); assert(A.raw==10878&&A.surv==2058&&A.orbits==7&&A.maxext==2);
    auto B=run_even_edge("00000 2244 ne5",T224,4,9,15,true); assert(B.raw==4830&&B.surv==0&&B.min1==16);
    auto C=run_odd_edge("00011 2224 ne6",T222,4,11,70,true); assert(C.raw==84294&&C.surv==2394&&C.orbits==2&&C.maxext==2);
    auto D=run_odd_edge("00011 2242 ne6",T224,2,11,46,true); assert(D.raw==12348&&D.surv==2044&&D.orbits==3&&D.maxext==2);
    auto E=run_mixed_2223(T222,18,13); assert(E.raw==18396&&E.surv==0&&E.min1==20);
    auto F=run_even_edge("00000 2242 ne5",T224,2,14,16,true); assert(F.raw==1260&&F.surv==0&&F.min1==28);
    auto G=run_odd_edge("00011 2222 ne5",T222,2,54,20,true); assert(G.raw==13104&&G.surv==2016&&G.orbits==2&&G.maxext==0);
    auto H=run_odd_edge("00011 2222 ne6",T222,2,21,72,true); assert(H.raw==13104&&H.surv==7686&&H.orbits==8&&H.maxext==2);
    auto I=run_odd_edge("00011 2224 ne5",T222,4,35,21,true); assert(I.raw==84294&&I.surv==49329&&I.orbits==13&&I.maxext==0);
    auto J=run_even_edge("00000 2224 ne5",T222,4,22,32,true); assert(J.raw==4095&&J.surv==315&&J.orbits==1&&J.maxext==0);
    auto K=run_even_edge("00000 2222 ne5",T222,2,27,33,true); assert(K.raw==1260&&K.surv==0&&K.min1==55);

    cout<<"CERTIFICATE PASSED\n";
    cout<<"All eleven previously remaining canonical K=4 triangle+disjoint-edge states are impossible.\n";
    cout<<"Therefore every hypothetical 12-center folded radius-3 cover has at least five close center pairs.\n";
}
