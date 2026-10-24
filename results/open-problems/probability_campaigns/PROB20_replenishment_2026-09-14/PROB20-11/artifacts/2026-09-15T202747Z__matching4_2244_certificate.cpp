// PROB20-11 exact certificate for canonical K=4 matching class
// active parities 00001111, close distances (2,2,4,4), neven=6.
// Exact finite folded-cube computation; no floating point, MILP, heuristic, or timeout inference.
// Symmetry dependency: completeness of the normalized second even d2-edge representatives
// (125,126) and (125,189) is independently certified by the archived d2-edge stabilizer
// computation used in 2026-09-15T200900Z__matching4_classes12_certificate.py.
#include <bits/stdc++.h>
using namespace std;
static const int N=2048, MAXC=512;
int fd(int a,int b){int w=__builtin_popcount((unsigned)(a^b));return min(w,12-w);}
int par(int x){return __builtin_popcount((unsigned)x)&1;}
array<bitset<N>,N> balls;
bitset<N> EVENM,ODDM;
pair<int,int> tri(int a,int b,int c){auto z=balls[a]&balls[b]&balls[c];return {(int)(z&EVENM).count(),(int)(z&ODDM).count()};}
bool low(pair<int,int> e,int x){
    auto t=tri(e.first,e.second,x);
    if(t==make_pair(0,0)) return true;
    int p=par(e.first), d=fd(e.first,e.second);
    if(d==2){auto hi=p==0?make_pair(4,6):make_pair(6,4);assert(t==hi);}
    else if(d==4){auto hi=p==0?make_pair(1,3):make_pair(3,1);assert(t==hi);}
    else assert(false);
    return false;
}
long long excess3(const vector<int>&cs,const bitset<N>&half){
    array<int,N> f{};
    for(int c:cs)for(int x=0;x<N;x++)if(balls[c][x])f[x]++;
    long long h=0;
    for(int x=0;x<N;x++)if(half[x]&&f[x]>=4){long long k=f[x];h+=(k-1)*(k-2)*(k-3)/6;}
    return h;
}
struct Edge{int i,j,y;};
struct Stats{int n,edges;long long raw,budget,kept;int bestViol;array<int,6>bestPat;};
Stats runrep(pair<int,int> rep){
    vector<int>E={0,3,rep.first,rep.second};
    vector<int>O;
    for(int x=0;x<N;x++){if(par(x)!=1)continue;bool ok=true;for(int e:E)if(fd(x,e)!=5){ok=false;break;}if(ok)O.push_back(x);}
    int n=O.size();
    vector<int>xw(n);for(int i=0;i<n;i++)xw[i]=low({0,3},O[i])+low(rep,O[i]);
    vector<bitset<MAXC>>far(n),adj4(n);vector<Edge>edges;vector<vector<int>>ymap(n,vector<int>(n,-1));
    for(int i=0;i<n;i++)for(int j=i+1;j<n;j++){
        int d=fd(O[i],O[j]);
        if(d==6)far[i][j]=far[j][i]=1;
        else if(d==4){adj4[i][j]=adj4[j][i]=1;int y=0;for(int e:E)y+=low({O[i],O[j]},e);edges.push_back({i,j,y});ymap[i][j]=ymap[j][i]=y;}
    }
    long long raw=0,budget=0,kept=0;int bestViol=INT_MAX;array<int,6>bestPat{};
    for(auto&e1:edges){auto common=far[e1.i]&far[e1.j];
        for(int c=0;c<n;c++)if(common[c]){auto ds=adj4[c]&common;
            for(int d=c+1;d<n;d++)if(ds[d]){
                if(make_pair(c,d)<=make_pair(e1.i,e1.j))continue;
                int y2=ymap[c][d];if(y2<0)continue;raw++;
                int x=xw[e1.i]+xw[e1.j]+xw[c]+xw[d],y=e1.y+y2;
                int dE=4*x+3*y,dO=6*x+y;
                if(dE>8||dO>24)continue;
                budget++;
                vector<int>a=E;a.insert(a.end(),{O[e1.i],O[e1.j],O[c],O[d]});
                int hE=excess3(a,EVENM),hO=excess3(a,ODDM);
                int viol=max(hE-(8-dE),hO-(24-dO));
                if(viol<bestViol){bestViol=viol;bestPat={x,y,dE,dO,hE,hO};}
                if(hE<=8-dE&&hO<=24-dO)kept++;
            }
        }
    }
    return {n,(int)edges.size(),raw,budget,kept,budget?bestViol:-1,bestPat};
}
int main(){
    vector<int>B0;for(int x=0;x<N;x++)if(fd(0,x)<=3)B0.push_back(x);assert(B0.size()==299);
    for(int c=0;c<N;c++)for(int b:B0)balls[c].set(c^b);
    for(int x=0;x<N;x++)if(par(x)==0)EVENM.set(x);ODDM=~EVENM;
    Stats A=runrep({125,126}), B=runrep({125,189});
    assert(A.n==400&&A.edges==39000&&A.raw==24511500&&A.budget==0&&A.kept==0&&A.bestViol==-1);
    assert(B.n==412&&B.edges==41582&&B.raw==26465589&&B.budget==375057&&B.kept==0&&B.bestViol==4);
    array<int,6> expected={0,0,0,0,12,26};assert(B.bestPat==expected);
    cout<<"MATCHING4 2,2,4,4 CERTIFICATE PASSED\n";
    cout<<"small orbit: O="<<A.n<<" d4edges="<<A.edges<<" raw="<<A.raw<<" budget="<<A.budget<<" kept="<<A.kept<<"\n";
    cout<<"generic orbit: O="<<B.n<<" d4edges="<<B.edges<<" raw="<<B.raw<<" budget="<<B.budget<<" kept="<<B.kept<<" bestViolation="<<B.bestViol<<"\n";
    cout<<"best pattern x,y,dE,dO,hE,hO =";for(int z:B.bestPat)cout<<" "<<z;cout<<"\n";
    cout<<"CONCLUSION: canonical class (00001111; 2,2,4,4; neven=6) is impossible\n";
}
