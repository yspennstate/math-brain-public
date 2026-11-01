#include <bits/stdc++.h>
using namespace std; using ll=long long; using Key=array<ll,12>;
/* Exact R20/KNSV n=12 one-cross-edge checker.
   KNSV's 5-vertex loopless multigraph separator has common simple support BASE
   and excess-copy slots SLOT[side].  Replace each of the four excess copies by
   an arbitrary connected labelled simple two-terminal network, no terminal edge,
   with positive internal sizes summing to 7.  Then add exactly one edge between
   internal vertices of two distinct slots.  This exhausts the stated labelled
   one-cross-edge family.  All calculations are integer-exact.

   If U(G)=U(H), the q^0 forest layer gives det(zI+L_G)=det(zI+L_H), so the
   Laplacian power traces agree.  For adding uv, B=bb^T, b=e_u-e_v.  Writing
   s_j=b^T L^j b and d_k=tr((L+B)^k)-tr(L^k), the rank-one log-det identity gives
      d_k = k s_{k-1} + sum_{m=1}^{k-1} s_{m-1} d_{k-m}.
   We use k<=12, enough to determine the 12x12 characteristic polynomial.
   Final survivors are additionally compared by the exact ordinary-U coefficients
   coming from all selected edge subsets of cardinality <=5.
*/
static const pair<int,int> BASE[6]={{0,2},{2,4},{4,1},{1,3},{3,0},{0,4}};
static const int SLOT[2][4]={{1,2,3,3},{1,3,4,4}};
struct Net{vector<pair<int,int>> e;}; vector<Net> nets[5]; vector<array<int,4>> comps;
int root(int*p,int x){while(p[x]!=x){p[x]=p[p[x]];x=p[x];}return x;}
bool connected(int r,int mask,const vector<pair<int,int>>&a){int p[6];iota(p,p+r+2,0);for(int i=0;i<(int)a.size();++i)if(mask>>i&1){int x=root(p,a[i].first),y=root(p,a[i].second);if(x!=y)p[y]=x;}int z=root(p,0);for(int i=1;i<r+2;++i)if(root(p,i)!=z)return false;return true;}
void enum_nets(){for(int r=1;r<=4;++r){vector<pair<int,int>> a;for(int i=0;i<r+2;++i)for(int j=i+1;j<r+2;++j)if(!(i==0&&j==1))a.push_back({i,j});for(int m=0;m<(1<<(int)a.size());++m)if(connected(r,m,a)){Net N;for(int i=0;i<(int)a.size();++i)if(m>>i&1)N.e.push_back(a[i]);nets[r].push_back(move(N));}cout<<"connected_networks_r"<<r<<"="<<nets[r].size()<<"\n";}}
void gencomp(int pos,int rem,array<int,4> c){if(pos==3){c[3]=rem;if(rem>0)comps.push_back(c);return;}for(int x=1;x<=rem-(3-pos);++x){c[pos]=x;gencomp(pos+1,rem-x,c);}}
struct G{uint16_t adj[12]{};ll L[12][12]{};vector<pair<int,int>> cross;};
G build(int side,const array<int,4>&r,const array<int,4>&id){G g;int deg[12]{};auto add=[&](int a,int b){if((g.adj[a]>>b)&1)abort();g.adj[a]|=1u<<b;g.adj[b]|=1u<<a;++deg[a];++deg[b];};for(auto e:BASE)add(e.first,e.second);array<vector<int>,4> V;int nx=5;for(int s=0;s<4;++s){auto [a,b]=BASE[SLOT[side][s]];vector<int> mp(r[s]+2);mp[0]=a;mp[1]=b;for(int j=0;j<r[s];++j){mp[2+j]=nx;V[s].push_back(nx++);}for(auto e:nets[r[s]][id[s]].e)add(mp[e.first],mp[e.second]);}if(nx!=12)abort();for(int s=0;s<4;++s)for(int t=s+1;t<4;++t)for(int u:V[s])for(int v:V[t])g.cross.push_back({u,v});for(int i=0;i<12;++i){g.L[i][i]=deg[i];for(int j=0;j<12;++j)if((g.adj[i]>>j)&1)g.L[i][j]=-1;}return g;}
struct Pow{ll P[12][12][12]{};Key tr{};};
Pow powers(const G&g){Pow q;for(int i=0;i<12;++i)q.P[0][i][i]=1;for(int i=0;i<12;++i)for(int j=0;j<12;++j)q.P[1][i][j]=g.L[i][j];for(int i=0;i<12;++i)q.tr[0]+=q.P[1][i][i];for(int e=2;e<=11;++e){for(int i=0;i<12;++i)for(int j=0;j<12;++j){__int128 z=0;for(int k=0;k<12;++k)z+=(__int128)q.P[e-1][i][k]*g.L[k][j];if(z>LLONG_MAX||z<LLONG_MIN)abort();q.P[e][i][j]=(ll)z;}for(int i=0;i<12;++i)q.tr[e-1]+=q.P[e][i][i];}__int128 z=0;for(int i=0;i<12;++i)for(int k=0;k<12;++k)z+=(__int128)q.P[11][i][k]*g.L[k][i];if(z>LLONG_MAX||z<LLONG_MIN)abort();q.tr[11]=(ll)z;return q;}
Key add_edge_key(const Pow&q,int u,int v){ll s[12]{},d[13]{};for(int j=0;j<12;++j)s[j]=q.P[j][u][u]+q.P[j][v][v]-2*q.P[j][u][v];Key out{};for(int k=1;k<=12;++k){__int128 z=(__int128)k*s[k-1];for(int m=1;m<k;++m)z+=(__int128)s[m-1]*d[k-m];if(z>LLONG_MAX||z<LLONG_MIN)abort();d[k]=(ll)z;__int128 y=(__int128)q.tr[k-1]+d[k];if(y>LLONG_MAX||y<LLONG_MIN)abort();out[k-1]=(ll)y;}return out;}
Key direct_added_key(const G&g,int u,int v){ll L[12][12];for(int i=0;i<12;++i)for(int j=0;j<12;++j)L[i][j]=g.L[i][j];++L[u][u];++L[v][v];--L[u][v];--L[v][u];ll P[12][12]{},Q[12][12]{};for(int i=0;i<12;++i)for(int j=0;j<12;++j)P[i][j]=L[i][j];Key out{};for(int e=1;e<=12;++e){for(int i=0;i<12;++i)out[e-1]+=P[i][i];if(e<12){for(int i=0;i<12;++i)for(int j=0;j<12;++j){__int128 z=0;for(int k=0;k<12;++k)z+=(__int128)P[i][k]*L[k][j];if(z>LLONG_MAX||z<LLONG_MIN)abort();Q[i][j]=(ll)z;}for(int i=0;i<12;++i)for(int j=0;j<12;++j)P[i][j]=Q[i][j];}}return out;}
template<class F>void each_assignment(int side,F f){for(auto r:comps){array<int,4> id{};for(int a=0;a<(int)nets[r[0]].size();++a){id[0]=a;for(int b=0;b<(int)nets[r[1]].size();++b){id[1]=b;for(int c=0;c<(int)nets[r[2]].size();++c){id[2]=c;for(int d=0;d<(int)nets[r[3]].size();++d){id[3]=d;f(r,id);}}}}}}
struct Rec{array<int,4>r,id;uint8_t u,v;Key k;};
vector<Key> keys(int side,long long&instances){vector<Key> out;out.reserve(1900000);instances=0;each_assignment(side,[&](auto&r,auto&id){G g=build(side,r,id);Pow q=powers(g);for(auto [u,v]:g.cross){out.push_back(add_edge_key(q,u,v));++instances;}});sort(out.begin(),out.end());return out;}
struct DSU{int p[12],sz[12];DSU(){for(int i=0;i<12;++i)p[i]=i,sz[i]=1;}int f(int x){while(p[x]!=x)x=p[x];return x;}void un(int a,int b){a=f(a);b=f(b);if(a==b)return;if(sz[a]<sz[b])swap(a,b);p[b]=a;sz[a]+=sz[b];}};
uint64_t monocode(const vector<pair<int,int>>&E,const int*idx,int e){DSU d;for(int i=0;i<e;++i)d.un(E[idx[i]].first,E[idx[i]].second);int s[12]{},c=0;for(int i=0;i<12;++i)if(d.f(i)==i)s[c++]=d.sz[d.f(i)];sort(s,s+c);int cyc=e-12+c;uint64_t z=(uint64_t)(cyc&15)|((uint64_t)c<<4);for(int i=0;i<c;++i)z|=(uint64_t)s[i]<<(8+4*i);return z;}
string smallU5(const G&g,int eu,int ev){vector<pair<int,int>> E;for(int i=0;i<12;++i)for(int j=i+1;j<12;++j)if((g.adj[i]>>j)&1)E.push_back({i,j});E.push_back({eu,ev});sort(E.begin(),E.end());map<uint64_t,ll>C;int idx[5];C[monocode(E,idx,0)]++;function<void(int,int,int)> rec=[&](int st,int need,int dep){if(!need){C[monocode(E,idx,dep)]++;return;}for(int i=st;i<=(int)E.size()-need;++i){idx[dep]=i;rec(i+1,need-1,dep+1);}};for(int e=1;e<=5;++e)rec(0,e,0);string s;for(auto&p:C)s+=to_string(p.first)+":"+to_string(p.second)+";";return s;}
int main(){ios::sync_with_stdio(false);enum_nets();array<int,4> z{};gencomp(0,7,z);long long assignments=0;for(auto r:comps){long long p=1;for(int x:r)p*=nets[x].size();assignments+=p;}cout<<"positive_compositions="<<comps.size()<<"\nlabelled_assignments_per_side="<<assignments<<"\n";cout<<"safe_matrix_bound_12x11x22^11="<<77130015786295296LL<<"\ntrace_bound_12x22^12="<<154260031572590592LL<<"\n";
 array<int,4> rr=comps.front(),ii{};G gcheck=build(0,rr,ii);auto [cu,cv]=gcheck.cross.front();if(add_edge_key(powers(gcheck),cu,cv)!=direct_added_key(gcheck,cu,cv))abort();cout<<"rank_one_trace_recurrence_selfcheck=PASS\n";
 long long n0,n1;auto A=keys(0,n0),B=keys(1,n1);cout<<"side0_cross_instances="<<n0<<"\nside1_cross_instances="<<n1<<"\n";A.erase(unique(A.begin(),A.end()),A.end());B.erase(unique(B.begin(),B.end()),B.end());vector<Key>C;set_intersection(A.begin(),A.end(),B.begin(),B.end(),back_inserter(C));cout<<"unique_side0_trace12="<<A.size()<<"\nunique_side1_trace12="<<B.size()<<"\ncommon_trace12="<<C.size()<<"\n";
 vector<Rec> R[2];for(int side=0;side<2;++side)each_assignment(side,[&](auto&r,auto&id){G g=build(side,r,id);Pow q=powers(g);for(auto [u,v]:g.cross){Key k=add_edge_key(q,u,v);if(binary_search(C.begin(),C.end(),k))R[side].push_back({r,id,(uint8_t)u,(uint8_t)v,k});}});cout<<"side0_instances_on_common_trace12="<<R[0].size()<<"\nside1_instances_on_common_trace12="<<R[1].size()<<"\n";
 unordered_set<string> S;S.reserve(R[0].size()*2+1);for(auto&r:R[0]){G g=build(0,r.r,r.id);S.insert(smallU5(g,r.u,r.v));}long long match=0;for(auto&r:R[1]){G g=build(1,r.r,r.id);if(S.count(smallU5(g,r.u,r.v)))++match;}cout<<"side0_distinct_smallU5="<<S.size()<<"\nside1_instances_matching_smallU5="<<match<<"\nVERDICT=PARTIAL_ONE_CROSS_EDGE_FILTER_SURVIVES\n";
}
