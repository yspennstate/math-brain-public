#include <cstdint>
#include <iostream>
#include <vector>
#include <bit>
int main(){
 for(auto [n,d]:std::vector<std::pair<int,int>>{{5,2},{6,2},{5,3}}){
  int N=1<<n;std::vector<uint64_t> generators,coords(n,0);
  for(int i=0;i<n;i++)for(int x=0;x<N;x++)if(x&(1<<i))coords[i]|=1ULL<<x;
  for(int s=0;s<N;s++)if(std::popcount((unsigned)s)<=d){uint64_t v=0;for(int x=0;x<N;x++)if((x&s)==s)v|=1ULL<<x;generators.push_back(v);}
  uint64_t R=0,stop=1ULL<<generators.size();long maxval=0;uint64_t witness=0;
  for(uint64_t a=1;a<stop;a++){
   R^=generators[std::countr_zero(a)];
   long v=(n-d)*std::popcount(R);
   for(auto m:coords)v-=2*std::popcount(R&m);
   if(v>maxval){maxval=v;witness=R;}
  }
  std::cout<<n<<" "<<d<<" cases "<<stop<<" max_violation "<<maxval<<" witness "<<witness<<std::endl;
 }
}
