// PROB20-11 exact active-stage certificate for the unique canonical K=5 state
// with sorted third-Bonferroni half-slacks (0,2). Standard C++20 only.
#include <bits/stdc++.h>
using namespace std;
static const int N=2048;
struct H{int e,o;};
int fd(int a,int b){int w=__builtin_popcount((unsigned)(a^b));return min(w,12-w);} 
int par(int x){return __builtin_popcount((unsigned)x)&1;}
array<bitset<N>,N> balls;
vector<array<int,299>> blist(N);
bitset<N> evenMask, oddMask;
H halves(const bitset<N>& m){return {(int)(m&evenMask).count(),(int)(m&oddMask).count()};}
H trih(int a,int b,int c){return halves(balls[a]&balls[b]&balls[c]);}
H pairh(int a,int b){return halves(balls[a]&balls[b]);}

// canonical tmax key sort vertices by all 6 permutations and take found max lookup
struct Key{int p0,p1,p2,d01,d02,d12; bool operator<(Key const&x)const{return tie(p0,p1,p2,d01,d02,d12)<tie(x.p0,x.p1,x.p2,x.d01,x.d02,x.d12);} };
map<Key,H> trimax;
H tmax_by(int p0,int p1,int p2,int d01,int d02,int d12){
 int ps[3]={p0,p1,p2}; int D[3][3]={{0,d01,d02},{d01,0,d12},{d02,d12,0}};
 int q[3]={0,1,2};
 do{Key k{ps[q[0]],ps[q[1]],ps[q[2]],D[q[0]][q[1]],D[q[0]][q[2]],D[q[1]][q[2]]};auto it=trimax.find(k);if(it!=trimax.end())return it->second;}while(next_permutation(q,q+3));
 cerr<<"missing tmax\n"; abort();
}
H tmx3(int a,int b,int c){return tmax_by(par(a),par(b),par(c),fd(a,b),fd(a,c),fd(b,c));}

struct State{string name; int nv; vector<pair<int,int>> es; vector<int> ap; vector<int> ds; int neven; H U;};

long long C2(int n){return 1LL*n*(n-1)/2;}
long long C3(int n){return 1LL*n*(n-1)*(n-2)/6;}

H coarse_U(const State&s){
    int ne=s.neven, no=12-ne;
    long long S1e=67LL*ne+232LL*no, S1o=232LL*ne+67LL*no;
    long long S2e=C2(no)*40LL+1LL*ne*no*10LL;
    long long S2o=C2(ne)*40LL+1LL*ne*no*10LL;
    long long S3e=1LL*ne*C2(no)+4LL*C3(no);
    long long S3o=4LL*C3(ne)+1LL*C2(ne)*no;
    map<tuple<int,int,int>,H> pairD;
    for(int p=0;p<2;p++){
        int a=(p==0?0:1);
        for(int q=0;q<2;q++){
            for(int d : (p==q?vector<int>{2,4}:vector<int>{1,3})){
                bool have=false; H val{-1,-1};
                for(int b=0;b<N;b++) if(b!=a && par(b)==q && fd(a,b)==d){
                    H h=pairh(a,b); if(!have){val=h;have=true;} else assert(h.e==val.e&&h.o==val.o);
                }
                assert(have); pairD[{p,q,d}]=val;
            }
        }
    }
    auto pairB=[&](int p,int q)->H{
        if(p==0&&q==0)return {0,40};
        if(p==1&&q==1)return {40,0};
        return {10,10};
    };
    map<array<int,3>,H> baseTri;
    for(int p0=0;p0<2;p0++)for(int p1=0;p1<2;p1++)for(int p2=0;p2<2;p2++){
        int d01=(p0==p1?6:5), d02=(p0==p2?6:5), d12=(p1==p2?6:5);
        baseTri[{p0,p1,p2}]=tmax_by(p0,p1,p2,d01,d02,d12);
    }
    map<pair<int,int>,int> ed;
    for(int k=0;k<(int)s.es.size();k++){int i=s.es[k].first,j=s.es[k].second;if(i>j)swap(i,j);ed[{i,j}]=s.ds[k];
        H a=pairD[{s.ap[i],s.ap[j],s.ds[k]}], b=pairB(s.ap[i],s.ap[j]);
        S2e += a.e-b.e; S2o += a.o-b.o;
    }
    for(int i=0;i<s.nv;i++)for(int j=i+1;j<s.nv;j++)for(int k=j+1;k<s.nv;k++){
        bool touched=ed.count({i,j})||ed.count({i,k})||ed.count({j,k}); if(!touched)continue;
        int dij=ed.count({i,j})?ed[{i,j}]:(s.ap[i]==s.ap[j]?6:5);
        int dik=ed.count({i,k})?ed[{i,k}]:(s.ap[i]==s.ap[k]?6:5);
        int djk=ed.count({j,k})?ed[{j,k}]:(s.ap[j]==s.ap[k]?6:5);
        H a=tmax_by(s.ap[i],s.ap[j],s.ap[k],dij,dik,djk), b=baseTri[{s.ap[i],s.ap[j],s.ap[k]}];
        S3e += a.e-b.e; S3o += a.o-b.o;
    }
    int activeE=count(s.ap.begin(),s.ap.end(),0);
    int isoE=ne-activeE, isoO=(12-s.nv)-isoE; assert(isoE>=0&&isoO>=0);
    for(int z=0;z<(int)s.es.size();z++){
        int i=s.es[z].first,j=s.es[z].second,d=s.ds[z];
        for(auto [q,num]:vector<pair<int,int>>{{0,isoE},{1,isoO}}){if(!num)continue;
            int diq=(s.ap[i]==q?6:5), djq=(s.ap[j]==q?6:5);
            H a=tmax_by(s.ap[i],s.ap[j],q,d,diq,djq), b=baseTri[{s.ap[i],s.ap[j],q}];
            S3e += 1LL*num*(a.e-b.e); S3o += 1LL*num*(a.o-b.o);
        }
    }
    return {(int)(S1e-S2e+S3e),(int)(S1o-S2o+S3o)};
}

vector<vector<int>> desired_matrix(const State&s){
 vector<vector<int>> D(s.nv,vector<int>(s.nv)); map<pair<int,int>,int> ed;
 for(int k=0;k<(int)s.es.size();k++){auto [i,j]=s.es[k];if(i>j)swap(i,j);ed[{i,j}]=s.ds[k];}
 for(int i=0;i<s.nv;i++)for(int j=i+1;j<s.nv;j++){auto it=ed.find({i,j});int d=(it==ed.end()?(s.ap[i]==s.ap[j]?6:5):it->second);D[i][j]=D[j][i]=d;}
 return D;
}

struct SearchResult{
 long long survivors=0; map<pair<int,int>,long long> costs; vector<array<int,12>> reps; vector<int> order, ap; int root,flip,neven2; H budget; long long nodes[13]{}; double seconds=0;
};

SearchResult search_active(const State&s,int repLimit=200000){
 auto D0=desired_matrix(s); int nv=s.nv; vector<int> deg(nv); set<pair<int,int>> E;
 for(auto [i,j]:s.es){deg[i]++;deg[j]++;if(i>j)swap(i,j);E.insert({i,j});}
 int root=0;for(int i=1;i<nv;i++) if(make_pair(deg[i],-s.ap[i])>make_pair(deg[root],-s.ap[root]))root=i;
 vector<int> neigh;for(int j=0;j<nv;j++)if(j!=root){int a=min(root,j),b=max(root,j);if(E.count({a,b}))neigh.push_back(j);} 
 int first=neigh[0];for(int j:neigh)if(D0[root][j]<D0[root][first])first=j;
 vector<int> order{root,first}; vector<char> used(nv);used[root]=used[first]=1;
 while((int)order.size()<nv){int best=-1,bscore=-1,bdeg=-1,bdroot=99;for(int v=0;v<nv;v++)if(!used[v]){int sc=0;for(int u:order)if(D0[v][u]<=4)sc++; if(best<0||make_tuple(sc,deg[v],-D0[root][v])>make_tuple(bscore,bdeg,bdroot)){best=v;bscore=sc;bdeg=deg[v];bdroot=-D0[root][v];}}order.push_back(best);used[best]=1;}
 vector<int> ap(nv);vector<vector<int>>D(nv,vector<int>(nv));for(int i=0;i<nv;i++){ap[i]=s.ap[order[i]];for(int j=0;j<nv;j++)D[i][j]=D0[order[i]][order[j]];}
 int flip=ap[0]; int neven2=s.neven; H budget{s.U.e-1024,s.U.o-1024};if(flip){for(int &p:ap)p^=1;neven2=12-neven2;swap(budget.e,budget.o);} assert(ap[0]==0);
 int d01=D[0][1]; int z1=(1<<d01)-1; assert(par(z1)==ap[1]&&fd(0,z1)==d01);
 vector<vector<int>> rootcands(nv);rootcands[0]={0};for(int v=1;v<nv;v++)for(int z=0;z<N;z++)if(par(z)==ap[v]&&fd(0,z)==D[0][v])rootcands[v].push_back(z);
 vector<int> chosen{0,z1}; array<uint8_t,N> cnt{}; auto apply=[&](int z,int delta){for(int x:blist[z])cnt[x]+=delta;};apply(0,1);apply(z1,1);
 SearchResult R;R.root=root;R.order=order;R.ap=ap;R.flip=flip;R.neven2=neven2;R.budget=budget;
 auto t0=chrono::steady_clock::now();
 function<void(int,int,int,int,int)> rec=[&](int k,int de,int do_,int ee,int eo){
  R.nodes[k]++;
  if(k==nv){R.survivors++;R.costs[{de+ee,do_+eo}]++;if((int)R.reps.size()<repLimit){array<int,12>a{};for(int i=0;i<nv;i++)a[i]=chosen[i];R.reps.push_back(a);}return;}
  for(int z:rootcands[k]){
   bool dup=false;for(int a:chosen)if(a==z){dup=true;break;}if(dup)continue;
   bool ok=true;for(int j=0;j<(int)chosen.size();j++)if(fd(z,chosen[j])!=D[k][j]){ok=false;break;}if(!ok)continue;
   int nde=de,ndo=do_,nee=ee,neo=eo;
   for(int ia=0;ia<(int)chosen.size();ia++)for(int ib=ia+1;ib<(int)chosen.size();ib++){
     H ac=trih(chosen[ia],chosen[ib],z), mx=tmx3(chosen[ia],chosen[ib],z); nde+=mx.e-ac.e;ndo+=mx.o-ac.o; if(nde+nee>budget.e||ndo+neo>budget.o)goto reject;
   }
   for(int x:blist[z]){int m=cnt[x];if(m>=3){int inc=(m-1)*(m-2)/2;if(par(x))neo+=inc;else nee+=inc;if(nde+nee>budget.e||ndo+neo>budget.o)goto reject;}}
   chosen.push_back(z);apply(z,1);rec(k+1,nde,ndo,nee,neo);apply(z,-1);chosen.pop_back();
   reject: ;
  }
 };
 rec(2,0,0,0,0);
 R.seconds=chrono::duration<double>(chrono::steady_clock::now()-t0).count();return R;
}

int main(){
 vector<int>B0;for(int x=0;x<N;x++)if(fd(0,x)<=3)B0.push_back(x);assert(B0.size()==299);
 for(int x=0;x<N;x++)if(par(x)==0)evenMask.set(x);oddMask=~evenMask;
 for(int c=0;c<N;c++){int k=0;for(int b:B0){int x=c^b;blist[c][k++]=x;balls[c].set(x);}}
 cerr<<"build trimax\n";auto T=chrono::steady_clock::now();
 for(int b=1;b<N;b++){auto bb=balls[0]&balls[b];for(int c=b+1;c<N;c++){Key key{0,par(b),par(c),fd(0,b),fd(0,c),fd(b,c)};H h=halves(bb&balls[c]);auto it=trimax.find(key);if(it==trimax.end())trimax[key]=h;else{it->second.e=max(it->second.e,h.e);it->second.o=max(it->second.o,h.o);}}}
 vector<pair<Key,H>> add;for(auto &kv:trimax){auto k=kv.first;auto h=kv.second;add.push_back({Key{1,1-k.p1,1-k.p2,k.d01,k.d02,k.d12},H{h.o,h.e}});}for(auto &kv:add)trimax[kv.first]=kv.second;
 cerr<<"trimax "<<trimax.size()<<" time "<<chrono::duration<double>(chrono::steady_clock::now()-T).count()<<"\n";
 vector<State>S={
 {"e5_3_slack02",5,{{0,4},{1,2},{1,3},{2,3},{3,4}},{0,0,1,1,0},{2,3,3,2,3},6,{1024,1026}}
 };

 for(size_t si=0;si<S.size();si++){
   auto &s=S[si]; H u=coarse_U(s); assert(u.e==1024&&u.o==1026);
   auto r=search_active(s,16); assert(r.survivors==0);
   assert(r.nodes[2]==1); assert(r.nodes[3]==90);
   for(int k=4;k<=s.nv;k++) assert(r.nodes[k]==0);
   cout<<s.name<<": U=("<<u.e<<","<<u.o<<") root="<<r.root<<" flip="<<r.flip
       <<" budget_after_translation=("<<r.budget.e<<","<<r.budget.o<<") nodes";
   for(int k=2;k<=s.nv;k++) if(r.nodes[k]) cout<<" "<<k<<":"<<r.nodes[k];
   cout<<" active_budget_survivors="<<r.survivors<<"\n";
 }
 cout<<"K5 SLACK-(0,2) CERTIFICATE PASSED\n";
 cout<<"The unique canonical K=5 state with sorted half-slacks (0,2) is impossible already at the active-center stage.\n";
}
