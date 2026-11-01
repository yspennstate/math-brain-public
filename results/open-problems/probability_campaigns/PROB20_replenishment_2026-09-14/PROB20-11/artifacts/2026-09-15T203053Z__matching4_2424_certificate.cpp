// PROB20-11 exact certificate for canonical K=4 matching class
// active parities 00001111, close distances (2,4,2,4), neven=6.
// Exact finite folded-cube computation; no floating point, MILP, heuristic, or timeout inference.
// Symmetry dependency: completeness of normalized even representatives (125,190),(125,413)
// is independently certified by the archived distance-2/distance-4 stabilizer computation.
#include <bits/stdc++.h>
using namespace std;
static const int N=2048, MAXC=512;
int fd(int a,int b){ int w=__builtin_popcount((unsigned)(a^b)); return min(w,12-w); }
int par(int x){ return __builtin_popcount((unsigned)x)&1; }
array<bitset<N>,N> balls;
bitset<N> EVM,ODM;
pair<int,int> tri(int a,int b,int c){ auto z=balls[a]&balls[b]&balls[c]; return {(int)(z&EVM).count(),(int)(z&ODM).count()}; }
bool low(pair<int,int> e,int x){
    auto t=tri(e.first,e.second,x);
    if(t==make_pair(0,0)) return true;
    int p=par(e.first), d=fd(e.first,e.second);
    pair<int,int> hi;
    if(d==2) hi=p?make_pair(6,4):make_pair(4,6);
    else if(d==4) hi=p?make_pair(3,1):make_pair(1,3);
    else assert(false);
    assert(t==hi);
    return false;
}
long long ex3(const vector<int>& cs,const bitset<N>& half){
    bitset<N> c0,c1,c2,c3;
    for(int c:cs){
        bitset<N> carry=balls[c], t;
        t=c0^carry; carry=c0&carry; c0=t;
        t=c1^carry; carry=c1&carry; c1=t;
        t=c2^carry; carry=c2&carry; c2=t;
        t=c3^carry; carry=c3&carry; c3=t;
        assert(carry.none());
    }
    long long h=0;
    array<bitset<N>,4> planes={c0,c1,c2,c3};
    for(int k=4;k<=(int)cs.size();k++){
        bitset<N> m=half;
        for(int bit=0;bit<4;bit++) m &= ((k>>bit)&1)?planes[bit]:~planes[bit];
        h += 1LL*(k-1)*(k-2)*(k-3)/6 * (long long)m.count();
    }
    return h;
}
struct Edge{int i,j,y;};
struct Keep{vector<int>a;int x2,x4,y2,y4,dE,dO,hE,hO;};

vector<Keep> runrep(pair<int,int> rep){
    vector<int> E={0,3,rep.first,rep.second};
    vector<int> O;
    for(int x=0;x<N;x++){
        if(par(x)!=1) continue;
        bool ok=true;
        for(int e:E) if(fd(x,e)!=5){ok=false;break;}
        if(ok) O.push_back(x);
    }
    int n=O.size();
    vector<array<int,2>> xw(n);
    for(int i=0;i<n;i++) xw[i]={low({0,3},O[i]),low(rep,O[i])};
    vector<bitset<MAXC>> far(n);
    vector<Edge> d2,d4;
    for(int i=0;i<n;i++) for(int j=i+1;j<n;j++){
        int d=fd(O[i],O[j]);
        if(d==6) far[i][j]=far[j][i]=1;
        else if(d==2 || d==4){
            int y=0; for(int e:E) y+=low({O[i],O[j]},e);
            if(d==2) d2.push_back({i,j,y}); else d4.push_back({i,j,y});
        }
    }
    long long raw=0,bud=0;
    vector<Keep> kept;
    map<array<int,8>,long long> kp;
    int best=INT_MAX; array<int,8> bp{};
    for(auto &a:d2){
        auto common=far[a.i]&far[a.j];
        for(auto &b:d4){
            if(!common[b.i] || !common[b.j]) continue;
            raw++;
            int x2=xw[a.i][0]+xw[a.j][0]+xw[b.i][0]+xw[b.j][0];
            int x4=xw[a.i][1]+xw[a.j][1]+xw[b.i][1]+xw[b.j][1];
            int y2=a.y, y4=b.y;
            int dE=4*x2+x4+6*y2+3*y4;
            int dO=6*x2+3*x4+4*y2+y4;
            if(dE>16 || dO>16) continue;
            bud++;
            vector<int> act=E; act.insert(act.end(),{O[a.i],O[a.j],O[b.i],O[b.j]});
            int hE=ex3(act,EVM), hO=ex3(act,ODM);
            int v=max(hE-(16-dE),hO-(16-dO));
            if(v<best){best=v;bp={x2,x4,y2,y4,dE,dO,hE,hO};}
            if(hE<=16-dE && hO<=16-dO){
                kept.push_back({act,x2,x4,y2,y4,dE,dO,hE,hO});
                kp[{x2,x4,y2,y4,dE,dO,hE,hO}]++;
            }
        }
    }
    if(rep==make_pair(125,190)){
        assert(n==368 && d2.size()==6208 && d4.size()==33192 && raw==9187200 && bud==754368 && kept.size()==960);
        array<int,8>a={0,0,0,0,0,0,11,11};
        array<int,8>b={0,1,0,1,4,4,11,11};
        array<int,8>c={0,1,0,1,4,4,12,12};
        assert(kp.size()==3 && kp[a]==192 && kp[b]==192 && kp[c]==576);
    } else {
        assert(rep==make_pair(125,413));
        assert(n==374 && d2.size()==6412 && d4.size()==34332 && raw==9797568 && bud==954372 && kept.size()==144);
        array<int,8>a={0,0,0,0,0,0,16,16}; assert(kp.size()==1 && kp[a]==144);
    }
    cerr<<"rep "<<rep.first<<","<<rep.second<<" O="<<n<<" d2="<<d2.size()<<" d4="<<d4.size()<<" raw="<<raw<<" bud="<<bud<<" kept="<<kept.size()<<" best="<<(bud?best:-1)<<" bp";
    if(bud) for(int z:bp) cerr<<" "<<z;
    cerr<<"\n";
    for(auto [p,c]:kp){ cerr<<" pat"; for(int z:p) cerr<<" "<<z; cerr<<" :"<<c<<"\n"; }
    return kept;
}

int main(){
    vector<int>B0; for(int x=0;x<N;x++) if(fd(0,x)<=3) B0.push_back(x); assert(B0.size()==299);
    for(int c=0;c<N;c++) for(int b:B0) balls[c].set(c^b);
    for(int x=0;x<N;x++) if(par(x)==0) EVM.set(x); ODM=~EVM;
    vector<Keep> all;
    for(auto r:{pair<int,int>{125,190},pair<int,int>{125,413}}){ auto k=runrep(r); all.insert(all.end(),k.begin(),k.end()); }
    cerr<<"TOTAL="<<all.size()<<"\n";
    long long awp=0,quart=0,crossbud=0,covers=0;
    int maxE=0,maxO=0,maxEp=0,maxOp=0,maxU=0;
    for(auto &K:all){
        auto &a=K.a;
        vector<int>E(a.begin(),a.begin()+4), O(a.begin()+4,a.end());
        pair<int,int>e1={E[0],E[1]}, e2={E[2],E[3]}, o2={O[0],O[1]}, o4={O[2],O[3]};
        vector<array<int,3>> Ec,Oc;
        for(int x=0;x<N;x++){
            if(par(x)==0){
                bool ok=true; for(int e:E) if(fd(x,e)!=6){ok=false;break;} if(ok) for(int o:O) if(fd(x,o)!=5){ok=false;break;}
                if(ok){ int y2=low(o2,x),y4=low(o4,x); int dE=6*y2+3*y4,dO=4*y2+y4; if(dE<=16&&dO<=16) Ec.push_back({x,y2,y4}); }
            } else {
                bool ok=true; for(int o:O) if(fd(x,o)!=6){ok=false;break;} if(ok) for(int e:E) if(fd(x,e)!=5){ok=false;break;}
                if(ok){ int x2=low(e1,x),x4=low(e2,x); int dE=4*x2+x4,dO=6*x2+3*x4; if(dE<=16&&dO<=16) Oc.push_back({x,x2,x4}); }
            }
        }
        maxE=max(maxE,(int)Ec.size()); maxO=max(maxO,(int)Oc.size());
        vector<array<int,4>> Ep,Op;
        for(int i=0;i<(int)Ec.size();i++) for(int j=i+1;j<(int)Ec.size();j++) if(fd(Ec[i][0],Ec[j][0])==6){
            int y2=Ec[i][1]+Ec[j][1],y4=Ec[i][2]+Ec[j][2]; if(6*y2+3*y4<=16&&4*y2+y4<=16) Ep.push_back({Ec[i][0],Ec[j][0],y2,y4});
        }
        for(int i=0;i<(int)Oc.size();i++) for(int j=i+1;j<(int)Oc.size();j++) if(fd(Oc[i][0],Oc[j][0])==6){
            int x2=Oc[i][1]+Oc[j][1],x4=Oc[i][2]+Oc[j][2]; if(4*x2+x4<=16&&6*x2+3*x4<=16) Op.push_back({Oc[i][0],Oc[j][0],x2,x4});
        }
        maxEp=max(maxEp,(int)Ep.size()); maxOp=max(maxOp,(int)Op.size());
        if(!Ep.empty()&&!Op.empty()) awp++;
        for(auto ep:Ep) for(auto op:Op){
            quart++;
            int x2=K.x2+op[2],x4=K.x4+op[3],y2=K.y2+ep[2],y4=K.y4+ep[3];
            int dE=4*x2+x4+6*y2+3*y4,dO=6*x2+3*x4+4*y2+y4;
            if(dE>16||dO>16) continue;
            if(fd(ep[0],op[0])!=5||fd(ep[0],op[1])!=5||fd(ep[1],op[0])!=5||fd(ep[1],op[1])!=5) continue;
            crossbud++;
            vector<int> full=a; full.insert(full.end(),{ep[0],ep[1],op[0],op[1]});
            bitset<N> u; for(int c:full)u|=balls[c]; maxU=max(maxU,(int)u.count()); if(u.count()==N)covers++;
        }
    }
    assert(all.size()==1104);
    assert(awp==144 && maxE==9 && maxO==9 && maxEp==4 && maxOp==4);
    assert(quart==2304 && crossbud==0 && covers==0);
    cerr<<"awp="<<awp<<" maxE="<<maxE<<" maxO="<<maxO<<" maxEp="<<maxEp<<" maxOp="<<maxOp<<" quart="<<quart<<" crossbud="<<crossbud<<" covers="<<covers<<"\n";
    cout<<"MATCHING4 2,4,2,4 CERTIFICATE PASSED\n";
    cout<<"CONCLUSION: canonical class (00001111; 2,4,2,4; neven=6) is impossible\n";
}
