// PROB20-11 exact certificate for canonical K=4 matching class
// active parities 00001111, close distances (2,2,2,4), neven=6.
// Exact finite folded-cube computation; no floating point, MILP, heuristic, or timeout inference.
// Symmetry dependency: completeness of normalized second even d2-edge representatives
// (125,126),(125,189) is independently certified by archived d2 stabilizer certificates.
#include <bits/stdc++.h>
using namespace std;
static const int N=2048, MAXC=512;
int fd(int a,int b){int w=__builtin_popcount((unsigned)(a^b)); return min(w,12-w);} 
int par(int x){return __builtin_popcount((unsigned)x)&1;}
array<bitset<N>,N> balls; bitset<N> EVM,ODM;
pair<int,int> tri(int a,int b,int c){auto z=balls[a]&balls[b]&balls[c]; return {(int)(z&EVM).count(),(int)(z&ODM).count()};}
bool low(pair<int,int> e,int x){
    auto t=tri(e.first,e.second,x); if(t==make_pair(0,0)) return true;
    int p=par(e.first),d=fd(e.first,e.second); pair<int,int> hi;
    if(d==2) hi=p?make_pair(6,4):make_pair(4,6); else if(d==4) hi=p?make_pair(3,1):make_pair(1,3); else assert(false);
    assert(t==hi); return false;
}
long long ex3(const vector<int>&cs,const bitset<N>&half){
    bitset<N>c0,c1,c2,c3;
    for(int c:cs){bitset<N>carry=balls[c],t;t=c0^carry;carry=c0&carry;c0=t;t=c1^carry;carry=c1&carry;c1=t;t=c2^carry;carry=c2&carry;c2=t;t=c3^carry;carry=c3&carry;c3=t;assert(carry.none());}
    array<bitset<N>,4>p={c0,c1,c2,c3}; long long h=0;
    for(int k=4;k<=(int)cs.size();k++){bitset<N>m=half;for(int b=0;b<4;b++)m&=((k>>b)&1)?p[b]:~p[b];h+=1LL*(k-1)*(k-2)*(k-3)/6*m.count();} return h;
}
struct Edge{int i,j,y;};
struct Keep{vector<int>a;int x,y2,y4,dE,dO,hE,hO;};

vector<Keep> runrep(pair<int,int> rep){
    vector<int>E={0,3,rep.first,rep.second};
    vector<int>O;
    for(int x=0;x<N;x++){if(par(x)!=1)continue;bool ok=true;for(int e:E)if(fd(x,e)!=5){ok=false;break;}if(ok)O.push_back(x);}
    int n=O.size(); vector<int>xw(n);for(int i=0;i<n;i++)xw[i]=low({0,3},O[i])+low(rep,O[i]);
    vector<bitset<MAXC>>far(n);vector<Edge>d2,d4;
    for(int i=0;i<n;i++)for(int j=i+1;j<n;j++){int d=fd(O[i],O[j]);if(d==6)far[i][j]=far[j][i]=1;else if(d==2||d==4){int y=0;for(int e:E)y+=low({O[i],O[j]},e);if(d==2)d2.push_back({i,j,y});else d4.push_back({i,j,y});}}
    long long raw=0,bud=0;vector<Keep>kept;map<array<int,7>,long long>kp;int best=INT_MAX;array<int,7>bp{};
    for(auto&a:d2){auto common=far[a.i]&far[a.j];for(auto&b:d4){if(!common[b.i]||!common[b.j])continue;raw++;
        int x=xw[a.i]+xw[a.j]+xw[b.i]+xw[b.j];int y2=a.y,y4=b.y;int dE=4*x+6*y2+3*y4,dO=6*x+4*y2+y4;
        if(dE>18||dO>26)continue;bud++;
        vector<int>act=E;act.insert(act.end(),{O[a.i],O[a.j],O[b.i],O[b.j]});int hE=ex3(act,EVM),hO=ex3(act,ODM);int v=max(hE-(18-dE),hO-(26-dO));if(v<best){best=v;bp={x,y2,y4,dE,dO,hE,hO};}
        if(hE<=18-dE&&hO<=26-dO){kept.push_back({act,x,y2,y4,dE,dO,hE,hO});kp[{x,y2,y4,dE,dO,hE,hO}]++;}
    }}
    if(rep==make_pair(125,126)){
        array<int,7> want={4,0,0,16,24,9,14};
        assert(n==400 && d2.size()==6800 && d4.size()==39000 && raw==12628800 && bud==590400 && kept.empty() && best==12 && bp==want);
    } else {
        array<int,7> want={0,0,0,0,0,20,27};
        assert(rep==make_pair(125,189));
        assert(n==412 && d2.size()==7376 && d4.size()==41582 && raw==14277000 && bud==1881288 && kept.empty() && best==2 && bp==want);
    }
    cerr<<"rep "<<rep.first<<","<<rep.second<<" O="<<n<<" d2="<<d2.size()<<" d4="<<d4.size()<<" raw="<<raw<<" bud="<<bud<<" kept="<<kept.size()<<" best="<<(bud?best:-1)<<" bp";if(bud)for(int z:bp)cerr<<" "<<z;cerr<<"\n";
    for(auto[p,c]:kp){cerr<<" pat";for(int z:p)cerr<<" "<<z;cerr<<" :"<<c<<"\n";}
    return kept;
}

int main(){
    vector<int>B0;for(int x=0;x<N;x++)if(fd(0,x)<=3)B0.push_back(x);assert(B0.size()==299);
    for(int c=0;c<N;c++)for(int b:B0)balls[c].set(c^b);
    for(int x=0;x<N;x++)if(par(x)==0)EVM.set(x);ODM=~EVM;
    vector<Keep>all;
    for(auto r:{pair<int,int>{125,126},pair<int,int>{125,189}}){auto k=runrep(r);all.insert(all.end(),k.begin(),k.end());}
    assert(all.empty());
    cout<<"MATCHING4 2,2,2,4 CERTIFICATE PASSED\n";
    cout<<"CONCLUSION: canonical class (00001111; 2,2,2,4; neven=6) is impossible\n";
}
