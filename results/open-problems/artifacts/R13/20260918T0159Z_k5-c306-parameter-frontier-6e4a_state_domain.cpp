#include <bits/stdc++.h>
using namespace std; using A=array<int,5>;
int main(){
 vector<A>S(16);for(int m=0;m<16;m++){S[m][0]=1;for(int j=0;j<4;j++)S[m][j+1]=(m>>j&1)?1:-1;}
 vector<set<int>> obs(17); vector<int> c;
 for(int k=1;k<=16;k++){
  c.assign(k,0);
  function<void(int,int)> rec=[&](int p,int z){if(p==k){for(int sb=0;sb<(1<<(k-1));sb++){A v=S[c[0]];for(int t=1;t<k;t++){int sg=(sb>>(t-1)&1)?1:-1;for(int j=0;j<5;j++)v[j]+=sg*S[c[t]][j];}int n=0;for(int x:v)n+=x*x;obs[k].insert(n);}return;}for(int x=z;x<=16-(k-p);x++){c[p]=x;rec(p+1,x+1);}};rec(0,0);
  cout<<"k="<<k<<" E={";bool f=0;for(int n:obs[k]){if(f)cout<<",";cout<<n;f=1;}cout<<"} M="<<*obs[k].rbegin()<<"\n";
 }
}
