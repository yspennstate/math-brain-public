#include <iostream>
#include <algorithm>
#include <vector>
#include <array>
#include <cstdint>
using cpp_int = __int128;
// This executable computes only forest coefficient sums. The invoking audit
// proves the bound 2^m max(c)^(n-1)<2^127 before invoking it, and performs all
// coefficient products in Python arbitrary precision integers.
std::string decimal(cpp_int x){if(x==0)return "0";std::string s;while(x){s.push_back('0'+x%10);x/=10;}std::reverse(s.begin(),s.end());return s;}
struct Edge{int x,y,c;};
int n,m,ea,eb,fa,fb;
std::vector<Edge> edges;
std::vector<int> parent,sz;
std::array<std::vector<cpp_int>,4> poly;
std::uint64_t leaves=0;
int root(int x){while(parent[x]!=x)x=parent[x];return x;}
void visit(int i,int k,const cpp_int &weight){
 if(i==m){
  ++leaves;int a=root(ea),b=root(eb),c=root(fa),d=root(fb);
  bool ee=a!=b,ff=c!=d,both=ee&&ff&&!((a==c&&b==d)||(a==d&&b==c));
  poly[0][k]+=weight;if(ee)poly[1][k]+=weight;if(ff)poly[2][k]+=weight;if(both)poly[3][k]+=weight;return;
 }
 visit(i+1,k,weight);
 int x=root(edges[i].x),y=root(edges[i].y);if(x==y)return;
 if(sz[x]<sz[y])std::swap(x,y);int old=sz[x];parent[y]=x;sz[x]+=sz[y];
 cpp_int next=weight*edges[i].c;visit(i+1,k+1,next);
 parent[y]=y;sz[x]=old;
}
int main(){
 std::cin>>n>>m>>ea>>eb>>fa>>fb;edges.resize(m);for(auto &g:edges)std::cin>>g.x>>g.y>>g.c;
 parent.resize(n);sz.assign(n,1);for(int i=0;i<n;++i)parent[i]=i;for(auto &p:poly)p.resize(n);
 visit(0,0,cpp_int(1));
 std::cout<<"{\"forest_subsets\":"<<leaves<<",\"polynomials\":[";
 for(int j=0;j<4;++j){if(j)std::cout<<",";std::cout<<"[";for(int k=0;k<n;++k){if(k)std::cout<<",";std::cout<<"\""<<decimal(poly[j][k])<<"\"";}std::cout<<"]";}
 std::cout<<"]}\n";
}
