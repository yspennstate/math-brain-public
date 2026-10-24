// PROB20-11 exact active-stage certificate for all four canonical K=5 states
// with sorted third-Bonferroni half-slacks (0,3). Standard C++20 only.
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
struct Key{int p0,p1,p2,d01,d02,d12; bool operator<(Key const&x)const{return tie(p0,p1,p2,d01,d02,d12)<tie(x.p0,x.p1,x.p2,x.d01,x.d02,x.d12);} };
map<Key,H> trimax;
H tmax_by(int p0,int p1,int p2,int d01,int d02,int d12){
 int ps[3]={p0,p1,p2}; int D[3][3]={{0,d01,d02},{d01,0,d12},{d02,d12,0}}; int q[3]={0,1,2};
 do{Key k{ps[q[0]],ps[q[1]],ps[q[2]],D[q[0]][q[1]],D[q[0]][q[2]],D[q[1]][q[2]]};auto it=trimax.find(k);if(it!=trimax.end())return it->second;}while(next_permutation(q,q+3)); abort();
}
H tmx3(int a,int b,int c){return tmax_by(par(a),par(b),par(c),fd(a,b),fd(a,c),fd(b,c));}
struct State{string name; int nv; vector<pair<int,int>> es; vector<int> ap; vector<int> ds; int neven; H U;};
long long C2(int n){return 1LL*n*(n-1)/2;} long long C3(int n){return 1LL*n*(n-1)*(n-2)/6;}
H coarse_U(const State&s){
 int ne=s.neven,no=12-ne; long long S1e=67LL*ne+232LL*no,S1o=232LL*ne+67LL*no; long long S2e=C2(no)*40+1LL*ne*no*10,S2o=C2(ne)*40+1LL*ne*no*10; long long S3e=1LL*ne*C2(no)+4LL*C3(no),S3o=4LL*C3(ne)+1LL*C2(ne)*no;
 map<tuple<int,int,int>,H> pairD; for(int p=0;p<2;p++){int a=p?1:0;for(int q=0;q<2;q++)for(int d:(p==q?vector<int>{2,4}:vector<int>{1,3})){bool have=false;H v{-1,-1};for(int b=0;b<N;b++)if(b!=a&&par(b)==q&&fd(a,b)==d){H h=pairh(a,b);if(!have){v=h;have=true;}else assert(h.e==v.e&&h.o==v.o);}assert(have);pairD[{p,q,d}]=v;}}
 auto pairB=[&](int p,int q)->H{if(!p&&!q)return{0,40};if(p&&q)return{40,0};return{10,10};}; map<array<int,3>,H> baseTri; for(int p0=0;p0<2;p0++)for(int p1=0;p1<2;p1++)for(int p2=0;p2<2;p2++){int a=p0==p1?6:5,b=p0==p2?6:5,c=p1==p2?6:5;baseTri[{p0,p1,p2}]=tmax_by(p0,p1,p2,a,b,c);} map<pair<int,int>,int> ed;
 for(int k=0;k<(int)s.es.size();k++){int i=s.es[k].first,j=s.es[k].second;if(i>j)swap(i,j);ed[{i,j}]=s.ds[k];H a=pairD[{s.ap[i],s.ap[j],s.ds[k]}],b=pairB(s.ap[i],s.ap[j]);S2e+=a.e-b.e;S2o+=a.o-b.o;}
 for(int i=0;i<s.nv;i++)for(int j=i+1;j<s.nv;j++)for(int k=j+1;k<s.nv;k++){bool t=ed.count({i,j})||ed.count({i,k})||ed.count({j,k});if(!t)continue;int a=ed.count({i,j})?ed[{i,j}]:(s.ap[i]==s.ap[j]?6:5),b=ed.count({i,k})?ed[{i,k}]:(s.ap[i]==s.ap[k]?6:5),c=ed.count({j,k})?ed[{j,k}]:(s.ap[j]==s.ap[k]?6:5);H x=tmax_by(s.ap[i],s.ap[j],s.ap[k],a,b,c),y=baseTri[{s.ap[i],s.ap[j],s.ap[k]}];S3e+=x.e-y.e;S3o+=x.o-y.o;}
 int activeE=count(s.ap.begin(),s.ap.end(),0),isoE=ne-activeE,isoO=(12-s.nv)-isoE;assert(isoE>=0&&isoO>=0);for(int z=0;z<(int)s.es.size();z++){int i=s.es[z].first,j=s.es[z].second,d=s.ds[z];for(auto [q,num]:vector<pair<int,int>>{{0,isoE},{1,isoO}}){if(!num)continue;H a=tmax_by(s.ap[i],s.ap[j],q,d,s.ap[i]==q?6:5,s.ap[j]==q?6:5),b=baseTri[{s.ap[i],s.ap[j],q}];S3e+=1LL*num*(a.e-b.e);S3o+=1LL*num*(a.o-b.o);}}
 return{(int)(S1e-S2e+S3e),(int)(S1o-S2o+S3o)};
}
vector<vector<int>> desired_matrix(const State&s){vector<vector<int>>D(s.nv,vector<int>(s.nv));map<pair<int,int>,int>ed;for(int k=0;k<(int)s.es.size();k++){auto[i,j]=s.es[k];if(i>j)swap(i,j);ed[{i,j}]=s.ds[k];}for(int i=0;i<s.nv;i++)for(int j=i+1;j<s.nv;j++){auto it=ed.find({i,j});D[i][j]=D[j][i]=(it==ed.end()?(s.ap[i]==s.ap[j]?6:5):it->second);}return D;}
struct SearchResult{long long survivors=0,nodes[13]{};int root,flip;H budget;};
SearchResult search_active(const State&s){auto D0=desired_matrix(s);int nv=s.nv;vector<int>deg(nv);set<pair<int,int>>E;for(auto[i,j]:s.es){deg[i]++;deg[j]++;if(i>j)swap(i,j);E.insert({i,j});}int root=0;for(int i=1;i<nv;i++)if(make_pair(deg[i],-s.ap[i])>make_pair(deg[root],-s.ap[root]))root=i;vector<int>neigh;for(int j=0;j<nv;j++)if(j!=root){int a=min(root,j),b=max(root,j);if(E.count({a,b}))neigh.push_back(j);}int first=neigh[0];for(int j:neigh)if(D0[root][j]<D0[root][first])first=j;vector<int>order{root,first};vector<char>used(nv);used[root]=used[first]=1;while((int)order.size()<nv){int best=-1,bs=-1,bd=-1,br=99;for(int v=0;v<nv;v++)if(!used[v]){int sc=0;for(int u:order)if(D0[v][u]<=4)sc++;if(best<0||make_tuple(sc,deg[v],-D0[root][v])>make_tuple(bs,bd,br)){best=v;bs=sc;bd=deg[v];br=-D0[root][v];}}order.push_back(best);used[best]=1;}vector<int>ap(nv);vector<vector<int>>D(nv,vector<int>(nv));for(int i=0;i<nv;i++){ap[i]=s.ap[order[i]];for(int j=0;j<nv;j++)D[i][j]=D0[order[i]][order[j]];}int flip=ap[0];H budget{s.U.e-1024,s.U.o-1024};if(flip){for(int&p:ap)p^=1;swap(budget.e,budget.o);}int d01=D[0][1],z1=(1<<d01)-1;assert(par(z1)==ap[1]&&fd(0,z1)==d01);vector<vector<int>>cand(nv);cand[0]={0};for(int v=1;v<nv;v++)for(int z=0;z<N;z++)if(par(z)==ap[v]&&fd(0,z)==D[0][v])cand[v].push_back(z);vector<int>chosen{0,z1};array<uint8_t,N>cnt{};auto apply=[&](int z,int delta){for(int x:blist[z])cnt[x]+=delta;};apply(0,1);apply(z1,1);SearchResult R;R.root=root;R.flip=flip;R.budget=budget;
 function<void(int,int,int,int,int)>rec=[&](int k,int de,int od,int ee,int eo){R.nodes[k]++;if(k==nv){R.survivors++;return;}for(int z:cand[k]){bool dup=false;for(int a:chosen)if(a==z)dup=true;if(dup)continue;bool ok=true;for(int j=0;j<(int)chosen.size();j++)if(fd(z,chosen[j])!=D[k][j]){ok=false;break;}if(!ok)continue;int nde=de,nod=od,nee=ee,neo=eo;for(int a=0;a<(int)chosen.size();a++)for(int b=a+1;b<(int)chosen.size();b++){H ac=trih(chosen[a],chosen[b],z),mx=tmx3(chosen[a],chosen[b],z);nde+=mx.e-ac.e;nod+=mx.o-ac.o;if(nde+nee>budget.e||nod+neo>budget.o)goto reject;}for(int x:blist[z]){int m=cnt[x];if(m>=3){int inc=(m-1)*(m-2)/2;if(par(x))neo+=inc;else nee+=inc;if(nde+nee>budget.e||nod+neo>budget.o)goto reject;}}chosen.push_back(z);apply(z,1);rec(k+1,nde,nod,nee,neo);apply(z,-1);chosen.pop_back();reject:;}};rec(2,0,0,0,0);return R;}
int main(){vector<int>B0;for(int x=0;x<N;x++)if(fd(0,x)<=3)B0.push_back(x);assert(B0.size()==299);for(int x=0;x<N;x++)if(par(x)==0)evenMask.set(x);oddMask=~evenMask;for(int c=0;c<N;c++){int k=0;for(int b:B0){int x=c^b;blist[c][k++]=x;balls[c].set(x);}}for(int b=1;b<N;b++){auto bb=balls[0]&balls[b];for(int c=b+1;c<N;c++){Key k{0,par(b),par(c),fd(0,b),fd(0,c),fd(b,c)};H h=halves(bb&balls[c]);auto it=trimax.find(k);if(it==trimax.end())trimax[k]=h;else{it->second.e=max(it->second.e,h.e);it->second.o=max(it->second.o,h.o);}}}vector<pair<Key,H>>add;for(auto&kv:trimax){auto k=kv.first,h=kv.second;add.push_back({Key{1,1-k.p1,1-k.p2,k.d01,k.d02,k.d12},H{h.o,h.e}});}for(auto&x:add)trimax[x.first]=x.second;
 vector<State>S={{"3edges+P4",8,{{0,1},{2,3},{4,5},{4,7},{5,6}},{0,0,0,0,1,1,0,1},{4,4,2,4,3},6,{1024,1027}},{"edge+tree_e4_3",7,{{0,1},{2,6},{3,5},{4,5},{5,6}},{0,0,0,1,1,1,0},{4,4,4,4,3},6,{1024,1027}},{"e5_1",5,{{0,4},{1,4},{2,3},{2,4},{3,4}},{1,1,1,1,1},{4,4,4,4,2},7,{1024,1027}},{"e5_4",5,{{0,1},{1,3},{1,4},{2,3},{2,4}},{1,1,0,1,0},{4,2,3,3,2},6,{1027,1024}}};long long expected[4]={210,252,240,120};
 for(int i=0;i<4;i++){H u=coarse_U(S[i]);assert(u.e==S[i].U.e&&u.o==S[i].U.o);auto r=search_active(S[i]);assert(r.survivors==0&&r.nodes[2]==1&&r.nodes[3]==expected[i]);for(int k=4;k<=S[i].nv;k++)assert(r.nodes[k]==0);cout<<S[i].name<<": U=("<<u.e<<","<<u.o<<") root="<<r.root<<" flip="<<r.flip<<" budget_after_translation=("<<r.budget.e<<","<<r.budget.o<<") nodes 2:"<<r.nodes[2]<<" 3:"<<r.nodes[3]<<" active_budget_survivors=0\n";}
 cout<<"K5 SLACK-(0,3) FOUR-STATE CERTIFICATE PASSED\nAll four canonical K=5 states with sorted half-slacks (0,3) are impossible already at the active-center stage.\n";
}
