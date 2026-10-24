#include <bits/stdc++.h>
using namespace std; using i64=long long; using i128=__int128_t;
struct DSU{vector<int>p,r;DSU(int n):p(n),r(n){iota(p.begin(),p.end(),0);}int f(int x){return p[x]==x?x:p[x]=f(p[x]);}bool u(int a,int b){a=f(a);b=f(b);if(a==b)return false;if(r[a]<r[b])swap(a,b);p[b]=a;if(r[a]==r[b])r[a]++;return true;}};
struct Stats{i64 Z=0;vector<i64>one;vector<vector<i64>>two;vector<i64>by_size;};
struct TStats{i64 d=0,c=0;vector<array<i64,2>>one;};
string out128(i128 x){if(x==0)return"0";bool neg=x<0;if(neg)x=-x;string s;while(x){s.push_back(char('0'+x%10));x/=10;}if(neg)s.push_back('-');reverse(s.begin(),s.end());return s;}
Stats stats(int n,const vector<pair<int,int>>&E){int m=E.size();Stats S;S.one.assign(m,0);S.two.assign(m,vector<i64>(m));S.by_size.assign(n+1,0);uint64_t N=1ULL<<m;for(uint64_t M=0;M<N;M++){DSU d(n);bool ok=1;int k=0;for(int i=0;i<m;i++)if(M>>i&1ULL){k++;if(!d.u(E[i].first,E[i].second)){ok=0;break;}}if(!ok)continue;S.Z++;S.by_size[k]++;for(int i=0;i<m;i++)if(M>>i&1ULL)S.one[i]++;for(int i=0;i<m;i++)if(M>>i&1ULL)for(int j=i+1;j<m;j++)if(M>>j&1ULL)S.two[i][j]++,S.two[j][i]++;}return S;}
TStats tstats(int n,const vector<pair<int,int>>&E,int x,int y){int m=E.size();TStats S;S.one.assign(m,{0,0});uint64_t N=1ULL<<m;for(uint64_t M=0;M<N;M++){DSU d(n);bool ok=1;for(int i=0;i<m;i++)if(M>>i&1ULL)if(!d.u(E[i].first,E[i].second)){ok=0;break;}if(!ok)continue;int c=d.f(x)==d.f(y);if(c)S.c++;else S.d++;for(int i=0;i<m;i++)if(M>>i&1ULL)S.one[i][c]++;}return S;}
i128 delta(const Stats&S,int i,int j){return (i128)S.one[i]*S.one[j]-(i128)S.Z*S.two[i][j];}
bool connected_without_edge(int n,const vector<pair<int,int>>&E,int skip){DSU d(n);for(int i=0;i<(int)E.size();i++)if(i!=skip)d.u(E[i].first,E[i].second);int r=d.f(0);for(int v=1;v<n;v++)if(d.f(v)!=r)return false;return true;}
int main(){
 // Core H0: 3x3 rook graph plus non-rook edge (0,4).
 vector<pair<int,int>> H;
 for(int a=0;a<9;a++)for(int b=a+1;b<9;b++){auto [ra,ca]=div(a,3);auto [rb,cb]=div(b,3);if(ra==rb||ca==cb)H.push_back({a,b});}
 H.push_back({0,4}); sort(H.begin(),H.end());
 auto SH=stats(9,H);
 i128 minD=-1;pair<int,int> arg{-1,-1};int neg=0;
 for(int i=0;i<(int)H.size();i++)for(int j=i+1;j<(int)H.size();j++){i128 d=delta(SH,i,j);if(minD<0||d<minD){minD=d;arg={i,j};}if(d<0)neg++;}
 vector<int> deg(9);for(auto [u,v]:H)deg[u]++,deg[v]++;
 int bridges=0;for(int i=0;i<(int)H.size();i++)if(!connected_without_edge(9,H,i))bridges++;
 cout<<"T07_PORT_TRANSFER_EXACT_CHECK\n";
 cout<<"CORE_H0 graph6=H{fQXgj n=9 m="<<H.size()<<" Z="<<SH.Z<<" pair_count="<<H.size()*(H.size()-1)/2<<" negative="<<neg<<" min_delta="<<out128(minD)<<" argmin_edges="<<H[arg.first].first<<"-"<<H[arg.first].second<<","<<H[arg.second].first<<"-"<<H[arg.second].second<<"\n";
 cout<<"CORE_H0 degrees=";for(int i=0;i<9;i++){if(i)cout<<",";cout<<deg[i];}cout<<" bridges="<<bridges<<"\n";
 cout<<"CORE_H0 forest_size_counts=";for(int k=0;k<(int)SH.by_size.size();k++)if(SH.by_size[k])cout<<k<<":"<<SH.by_size[k]<<" ";cout<<"\n";

 // Octahedron O6=K6 minus matching; port edge g=0-1. A=O6-g.
 set<pair<int,int>> miss={{0,5},{1,4},{2,3}};vector<pair<int,int>> O;
 for(int i=0;i<6;i++)for(int j=i+1;j<6;j++)if(!miss.count({i,j}))O.push_back({i,j});
 pair<int,int> g={0,1};int gi=find(O.begin(),O.end(),g)-O.begin();auto SO=stats(6,O);vector<pair<int,int>> A;for(auto e:O)if(e!=g)A.push_back(e);auto TA=tstats(6,A,0,1);
 vector<int> degA(6);for(auto [u,v]:A)degA[u]++,degA[v]++;int bridgesA=0;for(int i=0;i<(int)A.size();i++)if(!connected_without_edge(6,A,i))bridgesA++;
 cout<<"O6 n=6 m="<<O.size()<<" Z="<<SO.Z<<" port_edge_count="<<SO.one[gi]<<" ratio="<<SO.one[gi]<<"/"<<SO.Z<<"\n";
 cout<<"O6 forest_size_counts=";for(int k=0;k<(int)SO.by_size.size();k++)if(SO.by_size[k])cout<<k<<":"<<SO.by_size[k]<<" ";cout<<"\n";
 cout<<"GADGET_A=O6-g m="<<A.size()<<" D="<<TA.d<<" C="<<TA.c<<" activity="<<TA.c<<"/"<<TA.d<<" degrees=";for(int i=0;i<6;i++){if(i)cout<<",";cout<<degA[i];}cout<<" bridges="<<bridgesA<<"\n";
 // Interface signs J_p=D C_p-C D_p must be nonnegative; for this edge-transitive gadget they are exact integers.
 i128 minJ=-1;int negJ=0;for(int p=0;p<(int)A.size();p++){i128 J=(i128)TA.d*TA.one[p][1]-(i128)TA.c*TA.one[p][0];if(minJ<0||J<minJ)minJ=J;if(J<0)negJ++;}
 cout<<"GADGET_INTERFACE edge_count="<<A.size()<<" negative_J="<<negJ<<" min_J="<<out128(minJ)<<"\n";
 bool pass=(neg==0 && minD>0 && SH.Z==81112 && SO.Z==1083 && SO.one[gi]==361 && TA.d==361 && TA.c==361 && bridges==0 && bridgesA==0 && negJ==0);
 cout<<(pass?"ALL_EXACT_CHECKS_PASS":"EXACT_CHECK_FAILURE")<<"\n";
 return pass?0:1;
}
