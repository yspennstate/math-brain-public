// PROB20-11 exact certificate for canonical K=4 matching class
// active parities 00001111, close distances (2,4,4,4), neven=6.
// Exact finite folded-cube computation; no MILP, floating point, heuristic, or timeout inference.
// Symmetry dependency: the two normalized even-active representatives (125,190) and
// (125,413) and orbit completeness are independently certified by the archived
// distance-2-edge stabilizer computation used in 2026-09-15T205500Z__matching4_2442_certificate.py.
#include <bits/stdc++.h>
using namespace std;
static const int N=2048, MAXC=512;
int fd(int a,int b){int w=__builtin_popcount((unsigned)(a^b)); return min(w,12-w);} 
int par(int x){return __builtin_popcount((unsigned)x)&1;}
array<bitset<N>,N> balls,D4,D5,D6;
bitset<N> EVENM,ODDM;
pair<int,int> tri(int a,int b,int c){auto z=balls[a]&balls[b]&balls[c]; return {(int)(z&EVENM).count(),(int)(z&ODDM).count()};}
bool low(pair<int,int> e,int x){return tri(e.first,e.second,x)==make_pair(0,0);} 
long long excess3(const vector<int>& cs, const bitset<N>& half){
    array<int,N> f{}; for(int c:cs){ for(int x=0;x<N;x++) if(balls[c][x]) f[x]++; }
    long long h=0; for(int x=0;x<N;x++) if(half[x] && f[x]>=4){ long long k=f[x]; h+=(k-1)*(k-2)*(k-3)/6; } return h;
}
struct Edge{int i,j,y;};
struct Keep{vector<int> active; int x2,x4,y,dE,dO,hE,hO;};
vector<Keep> runrep(pair<int,int> rep){
    vector<int> ev={0,3,rep.first,rep.second};
    vector<int> O; for(int x=0;x<N;x++){if(par(x)!=1)continue; bool ok=1; for(int e:ev) if(fd(x,e)!=5){ok=0;break;} if(ok)O.push_back(x);} int n=O.size();
    vector<array<int,2>> xw(n); for(int i=0;i<n;i++) xw[i]={low({0,3},O[i]),low(rep,O[i])};
    vector<bitset<MAXC>> far(n),adj4(n); vector<Edge> edges; vector<vector<int>> ymap(n,vector<int>(n,-1));
    for(int i=0;i<n;i++)for(int j=i+1;j<n;j++){int d=fd(O[i],O[j]); if(d==6){far[i][j]=far[j][i]=1;} else if(d==4){adj4[i][j]=adj4[j][i]=1; int y=0; for(int e:ev)y+=low({O[i],O[j]},e); edges.push_back({i,j,y}); ymap[i][j]=ymap[j][i]=y;}}
    long long raw=0,bud=0; vector<Keep> kept; map<array<int,7>,long long> pats;
    for(auto &e1:edges){ auto common=far[e1.i]&far[e1.j];
        for(int c=0;c<n;c++) if(common[c]){auto ds=adj4[c]&common; for(int d=c+1;d<n;d++) if(ds[d]){ if(make_pair(c,d)<=make_pair(e1.i,e1.j))continue; int y2=ymap[c][d]; if(y2<0)continue; raw++;
            int x2=xw[e1.i][0]+xw[e1.j][0]+xw[c][0]+xw[d][0]; int x4=xw[e1.i][1]+xw[e1.j][1]+xw[c][1]+xw[d][1]; int y=e1.y+y2;
            int dE=4*x2+x4+3*y, dO=6*x2+3*x4+y; if(dE>6||dO>14)continue; bud++;
            vector<int> act=ev; act.insert(act.end(),{O[e1.i],O[e1.j],O[c],O[d]}); int hE=excess3(act,EVENM),hO=excess3(act,ODDM); pats[{x2,x4,y,dE,dO,hE,hO}]++;
            if(hE<=6-dE && hO<=14-dO) kept.push_back({act,x2,x4,y,dE,dO,hE,hO});
        }}
    }
    map<array<int,7>,int> kp; for(auto &k:kept)kp[{k.x2,k.x4,k.y,k.dE,k.dO,k.hE,k.hO}]++;
    if(rep==make_pair(125,190)){
        assert(n==368 && edges.size()==33192 && raw==15833964 && bud==126984 && kept.size()==336);
        array<int,7> k1={0,0,0,0,0,6,8}; assert(kp.size()==1 && kp[k1]==336);
    } else {
        assert(rep==make_pair(125,413));
        assert(n==374 && edges.size()==34332 && raw==16779204 && bud==162144 && kept.size()==792);
        assert(kp.size()==3);
        array<int,7> k2={0,0,0,0,0,4,12}; assert(kp[k2]==72);
        array<int,7> k3={0,0,0,0,0,6,12}; assert(kp[k3]==288);
        array<int,7> k4={0,0,0,0,0,6,14}; assert(kp[k4]==432);
    }
    cerr<<"rep "<<rep.first<<","<<rep.second<<" O="<<n<<" edges="<<edges.size()<<" raw="<<raw<<" budget="<<bud<<" kept="<<kept.size()<<"\n";
    for(auto [a,c]:kp){cerr<<" pat";for(int z:a)cerr<<" "<<z;cerr<<" :"<<c<<"\n";}
    return kept;
}
int main(){
    vector<int>B0;for(int x=0;x<N;x++)if(fd(0,x)<=3)B0.push_back(x); assert(B0.size()==299);
    for(int c=0;c<N;c++){for(int b:B0)balls[c].set(c^b); for(int x=0;x<N;x++){int d=fd(c,x); if(d==4)D4[c].set(x); else if(d==5)D5[c].set(x); else if(d==6)D6[c].set(x);}}
    for(int x=0;x<N;x++)if(par(x)==0)EVENM.set(x); ODDM=~EVENM;
    vector<Keep> all; for(auto r: {pair<int,int>{125,190},pair<int,int>{125,413}}){auto k=runrep(r); all.insert(all.end(),k.begin(),k.end());}
    cerr<<"TOTAL kept="<<all.size()<<"\n";
    long long active_with_pairs=0, quartets=0, valid_budget_quartets=0, cover_count=0; int maxUnion=0,maxEc=0,maxOc=0,maxEp=0,maxOp=0; vector<int> best;
    for(auto &K:all){
        auto &a=K.active; vector<int>Eact(a.begin(),a.begin()+4), Oact(a.begin()+4,a.end());
        pair<int,int> e2={Eact[2],Eact[3]}; pair<int,int> o1={Oact[0],Oact[1]},o2={Oact[2],Oact[3]};
        vector<pair<int,int>> Ec,Oc;
        for(int x=0;x<N;x++){
            if(par(x)==0){bool ok=1; for(int e:Eact)if(fd(x,e)!=6){ok=0;break;} if(ok)for(int o:Oact)if(fd(x,o)!=5){ok=0;break;} if(ok){int y=low(o1,x)+low(o2,x); if(y<=2)Ec.push_back({x,y});}}
            else {bool ok=1; for(int o:Oact)if(fd(x,o)!=6){ok=0;break;} if(ok)for(int e:Eact)if(fd(x,e)!=5){ok=0;break;} if(ok){int x2=low({0,3},x),x4=low(e2,x); if(4*x2+x4<=6 && 6*x2+3*x4<=14)Oc.push_back({x,100*x2+x4});}}
        }
        maxEc=max(maxEc,(int)Ec.size());maxOc=max(maxOc,(int)Oc.size());
        vector<array<int,3>> Ep,Op;
        for(int i=0;i<(int)Ec.size();i++)for(int j=i+1;j<(int)Ec.size();j++)if(fd(Ec[i].first,Ec[j].first)==6){int y=Ec[i].second+Ec[j].second; if(y<=2)Ep.push_back({Ec[i].first,Ec[j].first,y});}
        for(int i=0;i<(int)Oc.size();i++)for(int j=i+1;j<(int)Oc.size();j++)if(fd(Oc[i].first,Oc[j].first)==6){int x2=Oc[i].second/100+Oc[j].second/100;int x4=Oc[i].second%100+Oc[j].second%100;if(4*x2+x4<=6&&6*x2+3*x4<=14)Op.push_back({Oc[i].first,Oc[j].first,100*x2+x4});}
        maxEp=max(maxEp,(int)Ep.size());maxOp=max(maxOp,(int)Op.size()); if(!Ep.empty()&&!Op.empty())active_with_pairs++;
        for(auto ep:Ep){int y=ep[2]; for(auto op:Op){quartets++;int x2=op[2]/100,x4=op[2]%100;int dE=4*x2+x4+3*y,dO=6*x2+3*x4+y;if(dE>6||dO>14)continue; if(fd(ep[0],op[0])!=5||fd(ep[0],op[1])!=5||fd(ep[1],op[0])!=5||fd(ep[1],op[1])!=5)continue; valid_budget_quartets++;
                vector<int> full=a;full.push_back(ep[0]);full.push_back(ep[1]);full.push_back(op[0]);full.push_back(op[1]); bitset<N> u;for(int c:full)u|=balls[c];int uc=u.count();if(uc>maxUnion){maxUnion=uc;best=full;}if(uc==N)cover_count++;
            }}
    }
    assert(all.size()==1128);
    assert(active_with_pairs==144);
    assert(maxEc==6 && maxOc==12 && maxEp==3 && maxOp==6);
    assert(quartets==576);
    assert(valid_budget_quartets==0);
    assert(cover_count==0);
    cerr<<"active_with_pairs="<<active_with_pairs<<" maxEc="<<maxEc<<" maxOc="<<maxOc<<" maxEp="<<maxEp<<" maxOp="<<maxOp<<" quartets="<<quartets<<" cross+budget valid="<<valid_budget_quartets<<" covers="<<cover_count<<"\n";
    cout<<"MATCHING4 2,4,4,4 CERTIFICATE PASSED\n";
    cout<<"CONCLUSION: canonical class (00001111; 2,4,4,4; neven=6) is impossible\n";
}
