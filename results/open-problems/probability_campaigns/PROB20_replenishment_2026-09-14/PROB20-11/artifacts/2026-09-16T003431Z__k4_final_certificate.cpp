#include <algorithm>
#include <array>
#include <bitset>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <functional>
#include <map>
#include <numeric>
#include <set>
#include <string>
#include <tuple>
#include <unordered_map>
#include <utility>
#include <vector>
using namespace std;

static constexpr int N=2048;
using BS=bitset<N>;
static array<BS,N> balls;
static BS EVENM, ODDM;

static inline int pc(unsigned x){ return __builtin_popcount(x); }
static inline int fd(int a,int b){ int w=pc((unsigned)(a^b)); return min(w,12-w); }
static inline int par(int x){ return pc((unsigned)x)&1; }

struct H2 { int e=-1,o=-1; };
static unordered_map<uint32_t,H2> trimax;
static uint32_t key6(int p0,int p1,int p2,int d01,int d02,int d12){
    uint32_t k=p0; k=k*2+p1; k=k*2+p2; k=k*7+d01; k=k*7+d02; k=k*7+d12; return k;
}
static pair<int,int> halves(const BS& m){ return {(int)(m&EVENM).count(),(int)(m&ODDM).count()}; }
static pair<int,int> tri_actual(int a,int b,int c){ return halves(balls[a]&balls[b]&balls[c]); }

static pair<int,int> tri_max(int p0,int p1,int p2,int d01,int d02,int d12){
    int ps[3]={p0,p1,p2}; int D[3][3]={{0,d01,d02},{d01,0,d12},{d02,d12,0}};
    array<int,3> q={0,1,2};
    do {
        auto it=trimax.find(key6(ps[q[0]],ps[q[1]],ps[q[2]],D[q[0]][q[1]],D[q[0]][q[2]],D[q[1]][q[2]]));
        if(it!=trimax.end()) return {it->second.e,it->second.o};
    } while(next_permutation(q.begin(),q.end()));
    assert(false); return {-1,-1};
}
static pair<int,int> triple_max_centers(int a,int b,int c){ return tri_max(par(a),par(b),par(c),fd(a,b),fd(a,c),fd(b,c)); }

static int deficit_half(const vector<int>& cs,int half){
    int ans=0,m=cs.size();
    for(int i=0;i<m;i++) for(int j=i+1;j<m;j++) for(int k=j+1;k<m;k++){
        auto mx=triple_max_centers(cs[i],cs[j],cs[k]); auto ac=tri_actual(cs[i],cs[j],cs[k]);
        int M=half?mx.second:mx.first, A=half?ac.second:ac.first; assert(A<=M); ans+=M-A;
    }
    return ans;
}
static int excess_half(const vector<int>& cs,int half){
    int m=cs.size(), ans=0; const BS& hm=half?ODDM:EVENM;
    int lim=1<<m;
    for(int mask=0;mask<lim;mask++){
        int r=__builtin_popcount((unsigned)mask); if(r<4) continue;
        BS z=hm; for(int i=0;i<m;i++) if(mask>>i&1) z &= balls[cs[i]];
        ans += ((r-4)%2==0 ? 1 : -1) * (int)z.count();
    }
    assert(ans>=0); return ans;
}
static pair<int,int> cost2(const vector<int>& cs){
    return {deficit_half(cs,0)+excess_half(cs,0),deficit_half(cs,1)+excess_half(cs,1)};
}

using Hist=array<unsigned char,16>;
static Hist base_hist4(const array<int,4>& rows){
    Hist h{};
    for(int col=0;col<12;col++){
        int p=0; for(int i=0;i<4;i++) p|=((rows[i]>>col)&1)<<i; h[p]++;
    }
    return h;
}
static Hist canon_rows4(const array<int,4>& rows,bool swap_t,bool swap_edge){
    Hist h=base_hist4(rows),best{}; bool first=true;
    for(int flip=0;flip<16;flip++) for(int st=0;st<=(swap_t?1:0);st++) for(int se=0;se<=(swap_edge?1:0);se++){
        Hist q{};
        for(int p=0;p<16;p++){
            int v=p^flip; int b[4]; for(int i=0;i<4;i++) b[i]=(v>>i)&1;
            if(st) swap(b[0],b[1]); if(se) swap(b[2],b[3]);
            int w=b[0]|(b[1]<<1)|(b[2]<<2)|(b[3]<<3); q[w]+=h[p];
        }
        if(first || q<best){best=q;first=false;}
    }
    return best;
}

static int clique_cap(const vector<int>& v,int need){
    if(need<=0) return 0; int n=v.size(),best=0; bool hit=false;
    vector<vector<int>> adj(n);
    for(int i=0;i<n;i++) for(int j=i+1;j<n;j++) if(fd(v[i],v[j])==6){ adj[i].push_back(j); adj[j].push_back(i); }
    function<void(vector<int>,int)> rec=[&](vector<int> P,int d){
        if(hit) return; best=max(best,d); if(d>=need){hit=true;best=need;return;} if(d+(int)P.size()<=best) return;
        while(!P.empty()&&!hit){ if(d+(int)P.size()<=best) return; int x=P.back(); P.pop_back(); vector<int> Q; Q.reserve(P.size());
            for(int u:P) if(binary_search(adj[x].begin(),adj[x].end(),u)) Q.push_back(u); rec(Q,d+1);
        }
    };
    vector<int>P(n); iota(P.begin(),P.end(),0); rec(P,0); return best;
}

struct State{string name,ps; vector<int>T; int ed,ne; pair<int,int>U; long raw,good;};
struct Orb{long n=0; int x=0,y=0,ce=0,co=0;};

int main(){
    vector<int>B0; for(int x=0;x<N;x++) if(fd(0,x)<=3) B0.push_back(x); assert(B0.size()==299);
    for(int c=0;c<N;c++) for(int b:B0) balls[c].set(c^b);
    for(int x=0;x<N;x++) (par(x)?ODDM:EVENM).set(x);
    assert(EVENM.count()==1024 && ODDM.count()==1024);

    for(int b=1;b<N;b++){
        BS bb=balls[0]&balls[b]; int pb=par(b),d0b=fd(0,b);
        for(int c=b+1;c<N;c++){
            uint32_t k=key6(0,pb,par(c),d0b,fd(0,c),fd(b,c)); auto h=halves(bb&balls[c]); auto &z=trimax[k]; z.e=max(z.e,h.first); z.o=max(z.o,h.second);
        }
    }
    vector<pair<uint32_t,H2>> add; add.reserve(trimax.size());
    for(int p1=0;p1<2;p1++) for(int p2=0;p2<2;p2++) for(int a=0;a<=6;a++) for(int b=0;b<=6;b++) for(int c=0;c<=6;c++){
        auto it=trimax.find(key6(0,p1,p2,a,b,c)); if(it!=trimax.end()) add.push_back({key6(1,1-p1,1-p2,a,b,c),H2{it->second.o,it->second.e}});
    }
    for(auto &kv:add) trimax[kv.first]=kv.second;

    vector<int>T244={0,3,29},T224={0,3,12},T222={0,3,5};
    assert(make_tuple(fd(0,3),fd(0,29),fd(3,29))==make_tuple(2,4,4));
    assert(make_tuple(fd(0,3),fd(0,12),fd(3,12))==make_tuple(2,2,4));
    assert(make_tuple(fd(0,3),fd(0,5),fd(3,5))==make_tuple(2,2,2));
    vector<State>S={
      {"S1","00011",T244,2,6,{1031,1058},10878,2058},
      {"S2","00000",T224,4,5,{1033,1039},4830,0},
      {"S3","00011",T222,4,6,{1035,1094},84294,2394},
      {"S4","00011",T224,2,6,{1035,1070},12348,2044},
      {"S5","00001",T222,3,5,{1042,1037},18396,0},
      {"S6","00000",T224,2,5,{1038,1040},1260,0},
      {"S7","00011",T222,2,5,{1078,1044},13104,2016},
      {"S8","00011",T222,2,6,{1045,1096},13104,7686},
      {"S9","00011",T222,4,5,{1059,1045},84294,49329},
      {"S10","00000",T222,4,5,{1046,1056},4095,315},
      {"S11","00000",T222,2,5,{1051,1057},1260,0}
    };
    map<string,pair<int,int>> zeroMin={{"S2",{0,16}},{"S5",{1,20}},{"S6",{0,28}},{"S11",{0,55}}};
    int eliminated=0;
    for(auto &s:S){
        int sl0=s.U.first-1024, sl1=s.U.second-1024; int p3=s.ps[3]-'0',p4=s.ps[4]-'0';
        vector<int>X,Y; int d3=p3?5:6,d4=p4?5:6;
        for(int x=0;x<N;x++) if(par(x)==p3 && find(s.T.begin(),s.T.end(),x)==s.T.end()) { bool ok=true; for(int t:s.T) if(fd(x,t)!=d3) ok=false; if(ok) X.push_back(x); }
        if(p3==p4) Y=X; else for(int y=0;y<N;y++) if(par(y)==p4 && find(s.T.begin(),s.T.end(),y)==s.T.end()) { bool ok=true; for(int t:s.T) if(fd(y,t)!=d4) ok=false; if(ok) Y.push_back(y); }
        long raw=0; int minE=999,minO=999; map<Hist,Orb> orbs;
        auto process=[&](int x,int y){ raw++; vector<int> cs=s.T; cs.push_back(x);cs.push_back(y); auto co=cost2(cs); minE=min(minE,co.first);minO=min(minO,co.second); if(co.first>sl0||co.second>sl1) return; Hist k=canon_rows4({s.T[1],s.T[2],x,y},s.T==T222,p3==p4); auto &o=orbs[k]; if(o.n==0){o.x=x;o.y=y;o.ce=co.first;o.co=co.second;} o.n++; };
        if(p3==p4){ for(size_t i=0;i<X.size();i++) for(size_t j=i+1;j<X.size();j++) if(fd(X[i],X[j])==s.ed) process(X[i],X[j]); }
        else { for(int x:X) for(int y:Y) if(fd(x,y)==s.ed) process(x,y); }
        long good=0; for(auto &kv:orbs) good+=kv.second.n; assert(raw==s.raw && good==s.good);
        cout<<s.name<<" raw="<<raw<<" budget_active="<<good<<" orbits="<<orbs.size()<<"\n";
        if(good==0){ auto z=zeroMin.at(s.name); assert(minE==z.first&&minO==z.second); assert(minE>sl0||minO>sl1); eliminated++; continue; }
        int activeEven=count(s.ps.begin(),s.ps.end(),'0'),activeOdd=5-activeEven,needE=s.ne-activeEven,needO=(12-s.ne)-activeOdd;
        bool allfail=true; int exceptional=0;
        for(auto &kv:orbs){ auto &o=kv.second; vector<int> active=s.T;active.push_back(o.x);active.push_back(o.y); vector<int> ep,op;
            if(needE) for(int z=0;z<N;z++) if(par(z)==0 && find(active.begin(),active.end(),z)==active.end()){
                bool ok=true;for(int c:active) if(fd(z,c)!=(par(c)==0?6:5)) ok=false; if(!ok) continue; auto cc=active;cc.push_back(z);auto q=cost2(cc);if(q.first<=sl0&&q.second<=sl1)ep.push_back(z);
            }
            if(needO) for(int z=0;z<N;z++) if(par(z)==1 && find(active.begin(),active.end(),z)==active.end()){
                bool ok=true;for(int c:active) if(fd(z,c)!=(par(c)==1?6:5)) ok=false; if(!ok) continue; auto cc=active;cc.push_back(z);auto q=cost2(cc);if(q.first<=sl0&&q.second<=sl1)op.push_back(z);
            }
            int me=needE?clique_cap(ep,needE):0, mo=needO?clique_cap(op,needO):0;
            cout<<"  orbit n="<<o.n<<" cost="<<o.ce<<","<<o.co<<" Epool="<<ep.size()<<" Ecap="<<me<<" Opool="<<op.size()<<" Ocap="<<mo<<"\n";
            if((needE==0||me>=needE)&&(needO==0||mo>=needO)){
                exceptional++;
                if(s.name=="S8"){
                    assert(o.n==756 && o.ce==10 && o.co==13 && ep.size()==55 && op.size()==120);
                    int d6trip=0, feasible=0; map<pair<int,int>,int> cd;
                    for(size_t i=0;i<ep.size();i++) for(size_t j=i+1;j<ep.size();j++) if(fd(ep[i],ep[j])==6) for(size_t k=j+1;k<ep.size();k++) if(fd(ep[i],ep[k])==6&&fd(ep[j],ep[k])==6){
                        d6trip++; auto cc=active;cc.push_back(ep[i]);cc.push_back(ep[j]);cc.push_back(ep[k]);auto q=cost2(cc);cd[q]++;if(q.first<=sl0&&q.second<=sl1)feasible++;
                    }
                    assert(d6trip==120 && feasible==0 && cd.size()==1 && cd.begin()->first==make_pair(10,82) && cd.begin()->second==120);
                } else allfail=false;
            }
        }
        if(s.name=="S8"){assert(exceptional==1); eliminated++;}
        else { assert(allfail && exceptional==0); eliminated++; }
    }
    assert(eliminated==11);
    cout<<"CERTIFICATE PASSED\n";
    cout<<"All final 11 canonical K=4 triangle+disjoint-edge states are impossible.\n";
    cout<<"Every hypothetical 12-center folded radius-3 cover has at least 5 close pairs.\n";
}
