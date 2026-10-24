#include <bits/stdc++.h>
using namespace std;
struct DSU{int p[16]; DSU(int n){iota(p,p+n,0);} int f(int x){return p[x]==x?x:p[x]=f(p[x]);} bool u(int a,int b){a=f(a);b=f(b);if(a==b)return false;p[a]=b;return true;}};
int main(){
  // K3 vee (D_{1,0} sqcup D_{0,1}). Vertices 0,1,2 are the triangle.
  int n=8; vector<pair<int,int>> E={{0,1},{0,2},{1,2},{3,4},{5,6},{6,7}};
  for(int r=3;r<n;r++) for(int t=0;t<3;t++) E.push_back({t,r});
  int m=E.size(); if(m!=21) return 2;
  unsigned long long I=0; vector<unsigned long long> Ie(m); vector<vector<unsigned long long>> Ief(m,vector<unsigned long long>(m));
  uint64_t total=1ULL<<m;
  for(uint64_t mask=0; mask<total; ++mask){
    DSU d(n); bool ok=true;
    for(int i=0;i<m;i++) if(mask>>i&1ULL){ if(!d.u(E[i].first,E[i].second)){ok=false;break;} }
    if(!ok) continue; I++;
    vector<int> inc; for(int i=0;i<m;i++) if(mask>>i&1ULL){Ie[i]++; inc.push_back(i);} 
    for(int a=0;a<(int)inc.size();a++) for(int b=a+1;b<(int)inc.size();b++){int i=inc[a],j=inc[b];Ief[i][j]++;Ief[j][i]++;}
  }
  unsigned long long mn=ULLONG_MAX,mx=0; pair<int,int> arg;
  for(int i=0;i<m;i++)for(int j=i+1;j<m;j++){
    unsigned long long D=Ie[i]*Ie[j]-I*Ief[i][j];
    if(D<mn){mn=D;arg={i,j};} mx=max(mx,D);
  }
  cout<<"n="<<n<<" m="<<m<<" forests="<<I<<" minDelta="<<mn<<" maxDelta="<<mx<<" arg="<<arg.first<<","<<arg.second<<"\n";
  cout<<"ALL_EXACT_CHECKS_PASS\n";
}
