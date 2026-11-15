#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <numeric>
#include <string>
#include <vector>
#include <intrin.h>
using U=unsigned long long;
struct Edge { unsigned id; U weight; };
struct Wide { U lo=0,hi=0; void add(U x,U y,U w) {
 U pHi,pLo=_umul128(x,y,&pHi),qHi,qLo=_umul128(pLo,w,&qHi);
 assert(pHi==0 || pHi<=~U(0)/w);qHi+=pHi*w;
 U sum;unsigned char carry=_addcarry_u64(0,lo,qLo,&sum);lo=sum;
 assert(hi<=~U(0)-qHi-carry);hi+=qHi+carry;
 } U div(U denominator)const {assert(hi<denominator);U remainder;return _udiv128(hi,lo,denominator,&remainder);} };
int main(int argc,char** argv) {
 assert(argc==3);int N=std::stoi(argv[1]),steps=std::stoi(argv[2]);assert(N%3==0&&N<=96&&N>=3&&steps<=100);
 const U S=U(1)<<32,A=89,B=218,edgeDen=3*B,den=108*U(N)*N;
 std::vector<std::array<int,3>> keys;
 std::vector<int> lookup((N+1)*(N+1),-1);
 for(int a=0;a<=N;a++)for(int b=0;b<=N-a;b++){int c=N-a-b;if(a>=b&&b>=c){lookup[a*(N+1)+b]=(int)keys.size();keys.push_back({a,b,c});}}
 const unsigned K=(unsigned)keys.size();int pure=lookup[N*(N+1)];assert(pure>=0);
 auto id=[&](std::array<int,3> p){std::sort(p.begin(),p.end(),std::greater<int>());int z=lookup[p[0]*(N+1)+p[1]];assert(z>=0);return(unsigned)z;};
 // Independently derive grid barycenters from integer numerators summing N*D.
 auto split=[&](std::array<U,3> nums,U D,U multiplier,std::vector<Edge>& out){
  std::array<int,3> base;std::array<U,3> rem;int deficit=N;
  for(int i=0;i<3;i++){base[i]=(int)(nums[i]/D);rem[i]=nums[i]%D;deficit-=base[i];}
  assert(deficit>=0&&deficit<=2);
  if(deficit==0){out.push_back({id(base),multiplier*D});return;}
  for(int i=0;i<3;i++){auto q=base;U w;if(deficit==1){q[i]++;w=rem[i];}else{for(int j=0;j<3;j++)if(j!=i)q[j]++;w=D-rem[i];}if(w)out.push_back({id(q),multiplier*w});}
 };
 auto merge=[](std::vector<Edge>& row){std::sort(row.begin(),row.end(),[](Edge x,Edge y){return x.id<y.id;});std::vector<Edge> reduced;for(auto e:row){if(!reduced.empty()&&reduced.back().id==e.id)reduced.back().weight+=e.weight;else reduced.push_back(e);}row.swap(reduced);};
 std::vector<std::vector<Edge>> physical(K);
 for(unsigned i=0;i<K;i++){std::array<U,3> z;for(int j=0;j<3;j++)z[j]=U(N)*(B-A)+3*A*keys[i][j];split(z,edgeDen,1,physical[i]);merge(physical[i]);U s=0;for(auto e:physical[i])s+=e.weight;assert(s==edgeDen);}
 std::vector<U> offset;offset.reserve(K*K+1);std::vector<Edge> entries;U zero=0;
 for(unsigned i=0;i<K;i++)for(unsigned j=0;j<K;j++){
  offset.push_back(entries.size());auto r=keys[j];std::sort(r.begin(),r.end());std::vector<std::array<int,3>> perms;
  do{perms.push_back(r);}while(std::next_permutation(r.begin(),r.end()));
  assert(324%perms.size()==0);U factor=324/perms.size();std::vector<Edge> row;
  for(auto h:perms){std::array<U,3> products;U dot=0;for(int k=0;k<3;k++){products[k]=U(keys[i][k])*h[k];dot+=products[k];}if(dot==0){zero++;continue;}for(auto &z:products)z*=N;split(products,dot,factor,row);}
  merge(row);U s=0;for(auto e:row){s+=e.weight;assert(e.weight>0&&e.weight<=den);entries.push_back(e);}assert(s==den);
 }
 offset.push_back(entries.size());
 std::cout<<"{\"grid\":"<<N<<",\"orbits\":"<<K<<",\"ordered_rows\":"<<K*K<<",\"entries\":"<<entries.size()<<",\"zero_orientations\":"<<zero<<",\"source\":\"fresh direct Bayes, no imported table\"}"<<std::endl;
 auto edge=[&](const std::vector<U>& x){std::vector<U> raw(K),v(K);for(unsigned i=0;i<K;i++)for(auto e:physical[i]){assert(x[i]<=~U(0)/e.weight);U z=x[i]*e.weight;assert(raw[e.id]<=~U(0)-z);raw[e.id]+=z;}U total=0,sum=0;for(unsigned i=0;i<K;i++){total+=raw[i];v[i]=raw[i]/edgeDen;sum+=v[i];}assert(total==S*edgeDen&&sum<=S);v[pure]+=S-sum;return v;};
 auto fuse=[&](const std::vector<U>& x,const std::vector<U>& y){std::vector<Wide> acc(K);for(unsigned i=0;i<K;i++)if(x[i])for(unsigned j=0;j<K;j++)if(y[j]){U row=U(i)*K+j;for(U pos=offset[row];pos<offset[row+1];pos++){auto e=entries[pos];acc[e.id].add(x[i],y[j],e.weight);}}std::vector<U> v(K);U sum=0;for(unsigned i=0;i<K;i++){v[i]=acc[i].div(S*den);assert(v[i]<=S);sum+=v[i];}assert(sum<=S);v[pure]+=S-sum;return v;};
 std::vector<U> masses(K);masses[pure]=S;
 for(int depth=1;depth<=steps;depth++){
  auto one=edge(masses);auto two=fuse(one,one);auto four=fuse(two,two);masses=fuse(two,four);
  assert(std::accumulate(masses.begin(),masses.end(),U(0))==S);
  U signal=0;for(unsigned i=0;i<K;i++){U sq=0;for(auto x:keys[i])sq+=U(x)*x;signal+=masses[i]*(3*sq-U(N)*N);}
  std::cout<<"{\"depth\":"<<depth<<",\"signal_numerator\":"<<signal<<",\"signal_denominator\":"<<S*3*U(N)*N<<",\"masses\":[";for(unsigned i=0;i<K;i++){if(i)std::cout<<",";std::cout<<masses[i];}std::cout<<"]}"<<std::endl;
 }
}
