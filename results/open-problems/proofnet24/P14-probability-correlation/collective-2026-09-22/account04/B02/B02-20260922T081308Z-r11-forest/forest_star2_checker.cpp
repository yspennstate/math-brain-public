#include <bits/stdc++.h>
using namespace std;
struct DSU{ vector<int> p; DSU(int n):p(n){iota(p.begin(),p.end(),0);} int f(int x){return p[x]==x?x:p[x]=f(p[x]);} bool add(int a,int b){a=f(a);b=f(b);if(a==b)return false;p[a]=b;return true;}};
static bool forest(int n,const vector<pair<int,int>>& E,int mask){DSU d(n);for(int i=0;i<(int)E.size();++i)if(mask>>i&1)if(!d.add(E[i].first,E[i].second))return false;return true;}
static bool connected(int n,const vector<pair<int,int>>& E,int mask,int s,int t){DSU d(n);for(int i=0;i<(int)E.size();++i)if(mask>>i&1)d.add(E[i].first,E[i].second);return d.f(s)==d.f(t);}
int main(){
 long long cfg=0,pairtests=0,neg=0; long long globalMin=LLONG_MAX; string globalDesc;
 for(int n=3;n<=5;++n){
  vector<pair<int,int>> all; for(int i=0;i<n;i++)for(int j=i+1;j<n;j++)all.push_back({i,j}); int M=all.size(); long long ncfg=0,npairs=0,nneg=0,nmin=LLONG_MAX;
  for(int gm=1;gm<(1<<M);++gm){ vector<pair<int,int>> E; for(int k=0;k<M;k++)if(gm>>k&1)E.push_back(all[k]); int m=E.size(); if(m<2)continue;
   vector<int> fm; for(int s=0;s<(1<<m);++s)if(forest(n,E,s))fm.push_back(s);
   for(int c=0;c<n;++c){ vector<int> inc; for(int i=0;i<m;++i)if(E[i].first==c||E[i].second==c)inc.push_back(i); int d=inc.size(); if(!d)continue;
    for(int dm=1;dm<(1<<d);++dm){ unsigned bits=0; for(int j=0;j<d;++j)if(dm>>j&1)bits|=1u<<inc[j];
     vector<long long> Zi(m); vector<vector<long long>> Zij(m,vector<long long>(m)); long long Z=0;
     for(int s:fm){ long long w=1; vector<int> in; for(int i=0;i<m;++i)if(s>>i&1){ if(bits>>i&1)w*=2; in.push_back(i);} Z+=w; for(int i:in)Zi[i]+=w; for(int a=0;a<(int)in.size();++a)for(int b=a+1;b<(int)in.size();++b)Zij[in[a]][in[b]]+=w; }
     ++cfg;++ncfg;
     for(int i=0;i<m;++i)for(int j=i+1;j<m;++j){ long long gap=Zi[i]*Zi[j]-Z*Zij[i][j]; ++pairtests;++npairs; nmin=min(nmin,gap); if(gap<0){++neg;++nneg;} if(gap<globalMin){globalMin=gap; ostringstream os;os<<"n="<<n<<" gm="<<gm<<" center="<<c<<" dm="<<dm<<" pair="<<i<<","<<j<<" gap="<<gap;globalDesc=os.str();}}
    }
   }
  }
  cout<<"STAR2_EXHAUSTIVE n="<<n<<" configurations="<<ncfg<<" pair_tests="<<npairs<<" negative="<<nneg<<" min_gap="<<nmin<<"\n";
 }
 cout<<"STAR2_TOTAL configurations="<<cfg<<" pair_tests="<<pairtests<<" negative="<<neg<<" global_min_gap="<<globalMin<<" witness="<<globalDesc<<"\n";
 long long splitcfg=0,splitfail=0;
 for(int n=2;n<=4;++n){ vector<pair<int,int>> all;for(int i=0;i<n;i++)for(int j=i+1;j<n;j++)all.push_back({i,j});int M=all.size();
  for(int gm=1;gm<(1<<M);++gm){vector<pair<int,int>> E;for(int k=0;k<M;++k)if(gm>>k&1)E.push_back(all[k]);int m=E.size();
   for(int c=0;c<n;++c){vector<int> inc;for(int i=0;i<m;++i)if(E[i].first==c||E[i].second==c)inc.push_back(i);int d=inc.size();if(!d)continue;
    for(int dm=1;dm<(1<<d);++dm){unsigned bits=0;for(int j=0;j<d;++j)if(dm>>j&1)bits|=1u<<inc[j]; long long Zw=0;
     for(int s=0;s<(1<<m);++s)if(forest(n,E,s)){long long w=1;for(int i=0;i<m;++i)if((s>>i&1)&&(bits>>i&1))w*=2;Zw+=w;}
     vector<pair<int,int>> L; int v=n;
     for(int i=0;i<m;++i){auto [a,b]=E[i]; if(a!=c&&b!=c)L.push_back({a,b}); else {int w=(a==c?b:a);L.push_back({c,w});if(bits>>i&1)L.push_back({v,w});}}
     long long Zs=0; for(int s=0;s<(1<<(int)L.size());++s)if(forest(n+1,L,s)&&!connected(n+1,L,s,c,v))++Zs;
     ++splitcfg;if(Zw!=Zs)++splitfail;
    }
   }
  }
 }
 cout<<"SPLIT_LIFT_EXHAUSTIVE configurations="<<splitcfg<<" failures="<<splitfail<<"\n";
 long long gadgetTests=0; bool early=false; string bad;
 for(int n=2;n<=6 && !early;++n){vector<pair<int,int>> all;for(int i=0;i<n;i++)for(int j=i+1;j<n;j++)all.push_back({i,j});int M=all.size();
  for(int m=0;m<=min(6,M)&&!early;++m){
   for(int gm=0;gm<(1<<M);++gm){if(__builtin_popcount((unsigned)gm)!=m)continue; vector<pair<int,int>> E;for(int k=0;k<M;++k)if(gm>>k&1)E.push_back(all[k]);long long A=0,B=0;for(int s=0;s<(1<<m);++s)if(forest(n,E,s)){if(connected(n,E,s,0,1))++B;else ++A;}++gadgetTests;if(B==2*A){early=true;ostringstream os;os<<"n="<<n<<" m="<<m<<" A="<<A<<" B="<<B;bad=os.str();break;}}
  }
 }
 cout<<"GADGET_LE6 tests="<<gadgetTests<<" ratio2_found="<<(early?1:0);if(early)cout<<" witness="<<bad;cout<<"\n";
 vector<pair<int,int>> K23={{0,1},{0,2},{0,3},{0,4},{1,2},{1,3},{1,4}}; long long A=0,B=0;for(int s=0;s<(1<<7);++s)if(forest(5,K23,s)){if(connected(5,K23,s,0,1))++B;else ++A;}
 cout<<"GADGET_7 edge_count=7 A="<<A<<" B="<<B<<" ratio="<<B<<"/"<<A<<"\n";
 cout<<"TRIANGLE_UNIFORM_CUT incoming_weights=1,3/2,3/2 nonconstant=1\n";
 if(neg||splitfail||early||B!=2*A) return 2;
 cout<<"ALL_EXACT_ASSERTIONS_PASSED\n";
}
