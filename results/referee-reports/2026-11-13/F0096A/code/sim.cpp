// Single-threaded exact-sum configuration sampler and Posa rotation heuristic.
// Compile: clang++ -std=c++17 -O3 code/sim.cpp -o code/sim
#include <algorithm>
#include <chrono>
#include <cmath>
#include <cstdint>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <numeric>
#include <random>
#include <set>
#include <string>
#include <vector>
using namespace std;
using Clock=chrono::steady_clock;
struct Node {int l=-1,r=-1,p=-1,sz=1; uint64_t pri; bool rev=false;};
struct Path {
 vector<Node> t; int root=-1;
 Path(int n,mt19937_64 &rng):t(n){for(auto &x:t)x.pri=rng();}
 int size(int v){return v<0?0:t[v].sz;}
 void flip(int v){if(v>=0){swap(t[v].l,t[v].r);t[v].rev=!t[v].rev;}}
 void push(int v){if(v>=0 && t[v].rev){flip(t[v].l);flip(t[v].r);t[v].rev=false;}}
 void pull(int v){if(v<0)return;t[v].sz=1+size(t[v].l)+size(t[v].r);if(t[v].l>=0)t[t[v].l].p=v;if(t[v].r>=0)t[t[v].r].p=v;}
 int merge(int a,int b){if(a<0){if(b>=0)t[b].p=-1;return b;}if(b<0){t[a].p=-1;return a;}push(a);push(b);if(t[a].pri>t[b].pri){t[a].r=merge(t[a].r,b);pull(a);t[a].p=-1;return a;}t[b].l=merge(a,t[b].l);pull(b);t[b].p=-1;return b;}
 pair<int,int> split(int a,int k){if(a<0)return {-1,-1};push(a);if(size(t[a].l)>=k){auto z=split(t[a].l,k);t[a].l=z.second;pull(a);t[a].p=-1;if(z.first>=0)t[z.first].p=-1;return {z.first,a};}auto z=split(t[a].r,k-size(t[a].l)-1);t[a].r=z.first;pull(a);t[a].p=-1;if(z.second>=0)t[z.second].p=-1;return {a,z.second};}
 int at(int k){int a=root;while(a>=0){push(a);int s=size(t[a].l);if(k==s)return a;if(k<s)a=t[a].l;else{k-=s+1;a=t[a].r;}}return -1;}
 int rank(int v){vector<int> a;for(int w=v;w>=0;w=t[w].p)a.push_back(w);for(auto it=a.rbegin();it!=a.rend();++it)push(*it);int k=size(t[v].l);while(t[v].p>=0){int p=t[v].p;if(t[p].r==v)k+=1+size(t[p].l);v=p;}return k;}
 void append(int v){root=merge(root,v);}
 void rotate(int pivot){auto z=split(root,pivot+1);flip(z.second);root=merge(z.first,z.second);}
 vector<int> values(){vector<int> out;for(int i=0;i<size(root);++i)out.push_back(at(i));return out;}
};
struct Graph {int n,m;vector<int>d;vector<pair<int,int>> e;vector<vector<int>>a;long long degree_tries=0,pair_tries=0;};
long double mean_degree(long double l){long double w=1,s=1,t=3;for(int k=4;k<256;++k){w*=l/k;s+=w;t+=k*w;if(w<1e-28L*s)break;}return t/s;}
Graph sample(int n,int m,mt19937_64 &rng){
 Graph g;g.n=n;g.m=m;long double lo=0,hi=2*m/(long double)n;for(int z=0;z<100;++z){auto mid=(lo+hi)/2;if(mean_degree(mid)<2*m/(long double)n)lo=mid;else hi=mid;}long double l=(lo+hi)/2;
 vector<long double>p(3,0);long double w=1,s=0;for(int k=3;k<256;++k){if(k>3)w*=l/k;p.push_back(w);s+=w;}for(auto &v:p)v/=s;
 while(true){g.d.clear();
  while(true){++g.degree_tries;vector<int> counts(256);int left=n;long long total=0;long double remain=1;
   for(int k=3;k<256 && left;++k){long double q=min((long double)1,max((long double)0,p[k]/remain));int x=binomial_distribution<int>(left,(double)q)(rng);counts[k]=x;left-=x;total+=(long long)k*x;remain-=p[k];if(remain<=0 && left){counts[k]+=left;total+=(long long)k*left;left=0;}}
   if(left || total!=2*m)continue;for(int k=3;k<256;++k)g.d.insert(g.d.end(),counts[k],k);shuffle(g.d.begin(),g.d.end(),rng);break;
  }
  ++g.pair_tries;vector<int>st;st.reserve(2*m);for(int i=0;i<n;++i)for(int j=0;j<g.d[i];++j)st.push_back(i);shuffle(st.begin(),st.end(),rng);g.e.clear();g.a.assign(n,{});bool ok=true;
  for(int j=0;j<2*m;j+=2){int a=st[j],b=st[j+1];if(a==b || find(g.a[a].begin(),g.a[a].end(),b)!=g.a[a].end()){ok=false;break;}g.e.emplace_back(a,b);g.a[a].push_back(b);g.a[b].push_back(a);}if(ok)return g;
 }
}
struct Result {vector<int>cycle;long long steps=0,rotations=0;int longest=0;double seconds=0;};
Result solve(const Graph &g,mt19937_64 &rng,double seconds,int cap_factor){
 auto begin=Clock::now();Result res;Path p(g.n,rng);vector<char>used(g.n,0);int start=rng()%g.n;p.append(start);used[start]=1;int len=1;
 for(long long iter=0;iter<(long long)cap_factor*g.n;++iter){res.steps=iter+1;if((iter&4095)==0 && chrono::duration<double>(Clock::now()-begin).count()>seconds)break;
  if(rng()&1)p.flip(p.root);int end=p.at(len-1),first=p.at(0);vector<int>free;
  for(int v:g.a[end])if(!used[v])free.push_back(v);
  if(!free.empty()){int v=free[rng()%free.size()];p.append(v);used[v]=1;++len;res.longest=max(res.longest,len);continue;}
  bool close=len>2 && find(g.a[end].begin(),g.a[end].end(),first)!=g.a[end].end();
  if(close){if(len==g.n){res.cycle=p.values();break;}
   int outside=-1,inside=-1;for(int v=0;v<g.n && outside<0;++v)if(!used[v])for(int u:g.a[v])if(used[u]){outside=v;inside=u;break;}
   if(outside<0)break;int j=p.rank(inside);auto z=p.split(p.root,j+1);p.root=p.merge(z.second,z.first);p.append(outside);used[outside]=1;++len;res.longest=max(res.longest,len);continue;
  }
  vector<int> pivots;for(int v:g.a[end]){int j=p.rank(v);if(j<len-2)pivots.push_back(j);}if(!pivots.empty()){p.rotate(pivots[rng()%pivots.size()]);++res.rotations;}
 }
 res.seconds=chrono::duration<double>(Clock::now()-begin).count();return res;
}
bool verify(const Graph&g,const vector<int>&c){if((int)c.size()!=g.n)return false;vector<char>s(g.n,0);for(int i=0;i<g.n;++i){int u=c[i],v=c[(i+1)%g.n];if(u<0 || u>=g.n || s[u] || find(g.a[u].begin(),g.a[u].end(),v)==g.a[u].end())return false;s[u]=1;}return true;}
int main(int argc,char**argv){
 if(argc>1 && string(argv[1])=="samplecheck"){
  if(argc!=6)return 2;int n=stoi(argv[2]),m=stoi(argv[3]),reps=stoi(argv[4]);mt19937_64 rng(stoull(argv[5]));
  cout<<"mask,degree_tries,pair_tries\n";
  for(int rep=0;rep<reps;++rep){auto g=sample(n,m,rng);uint64_t mask=0;int k=0;for(int u=0;u<n;++u)for(int v=u+1;v<n;++v,++k)if(find(g.a[u].begin(),g.a[u].end(),v)!=g.a[u].end())mask|=uint64_t(1)<<k;cout<<mask<<','<<g.degree_tries<<','<<g.pair_tries<<'\n';}return 0;
 }
 if(argc<8){cerr<<"usage: sim n c repetitions seed seconds cap_factor prefix\n";return 2;}int n=stoi(argv[1]);double c=stod(argv[2]);int reps=stoi(argv[3]);uint64_t seed=stoull(argv[4]);double seconds=stod(argv[5]);int cap=stoi(argv[6]);string prefix=argv[7];int m=llround(c*n);mt19937_64 rng(seed);
 cout<<"n,c,rep,seed,m,degree_tries,pair_tries,max_degree,found,longest,steps,rotations,solve_seconds,sample_seconds,prefix\n";
 for(int r=0;r<reps;++r){auto begin=Clock::now();Graph g=sample(n,m,rng);double st=chrono::duration<double>(Clock::now()-begin).count();auto result=solve(g,rng,seconds,cap);if(!result.cycle.empty() && !verify(g,result.cycle)){cerr<<"invalid certificate\n";return 3;}string stem=prefix+"_"+to_string(r);ofstream graph(stem+".bin",ios::binary);int32_t header[2]={n,m};graph.write((char*)header,8);for(auto e:g.e){int32_t ab[2]={e.first,e.second};graph.write((char*)ab,8);}graph.close();ofstream cert(stem+".cycle");for(int v:result.cycle)cert<<v<<' ';cert<<'\n';cout<<n<<','<<setprecision(12)<<c<<','<<r<<','<<seed<<','<<m<<','<<g.degree_tries<<','<<g.pair_tries<<','<<*max_element(g.d.begin(),g.d.end())<<','<<!result.cycle.empty()<<','<<result.longest<<','<<result.steps<<','<<result.rotations<<','<<result.seconds<<','<<st<<','<<stem<<'\n'<<flush;
 }
}
