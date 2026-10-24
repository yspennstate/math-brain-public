#include <algorithm>
#include <array>
#include <iostream>
#include <string>
#include <vector>
using i128=__int128_t;
struct V { long long a,b,c,d,e,f; };
static std::string s128(i128 x){
  if(x==0) return "0"; bool neg=x<0; if(neg)x=-x; std::string s;
  while(x){ s.push_back(char('0'+x%10)); x/=10; }
  if(neg)s.push_back('-'); std::reverse(s.begin(),s.end()); return s;
}
int main(){
  std::vector<V> v={
#include "certificate_vectors.inc"
  };
  if(v.size()!=144){ std::cerr<<"wrong vector count\n"; return 2; }
  const int n=(int)v.size();
  std::vector<i128> H((size_t)n*n),Q((size_t)n*n),R((size_t)n*n);
  auto at=[&](std::vector<i128>& A,int i,int j)->i128&{return A[(size_t)i*n+j];};
  for(int i=0;i<n;i++) for(int j=0;j<n;j++){
    const auto& x=v[i]; const auto& y=v[j];
    at(H,i,j)=(i128)x.a*y.b+(i128)x.b*y.a-(i128)x.c*y.d-(i128)x.d*y.c-(i128)x.e*y.f-(i128)x.f*y.e;
    at(Q,i,j)=(i128)x.c*y.d+(i128)x.d*y.c;
    at(R,i,j)=(i128)x.e*y.f+(i128)x.f*y.e;
  }
  unsigned long long count=0,zeros=0; bool first=true; i128 minpos=0; std::array<int,4> minidx{};
  for(int i=0;i<n;i++) for(int j=i;j<n;j++) for(int k=j;k<n;k++) for(int l=k;l<n;l++){
    i128 p=at(H,i,j)*at(H,k,l)+at(H,i,k)*at(H,j,l)+at(H,i,l)*at(H,j,k)
      -2*(at(Q,i,j)*at(R,k,l)+at(Q,i,k)*at(R,j,l)+at(Q,i,l)*at(R,j,k)
          +at(Q,j,k)*at(R,i,l)+at(Q,j,l)*at(R,i,k)+at(Q,k,l)*at(R,i,j));
    ++count;
    if(p<0){
      std::cout<<"FAIL negative_cross_blossom index="<<i<<","<<j<<","<<k<<","<<l<<" value="<<s128(p)<<"\n";
      return 1;
    }
    if(p==0) ++zeros;
    else if(first||p<minpos){ first=false; minpos=p; minidx={i,j,k,l}; }
  }
  std::cout<<"PASS MOC4-B09-TWO-KNOT-CROSS-BLOSSOM-v1\n";
  std::cout<<"objects = "<<n<<"\n";
  std::cout<<"unordered_quadruples = "<<count<<"\n";
  std::cout<<"zero_numerators = "<<zeros<<"\n";
  std::cout<<"minimum_positive_integer_numerator = "<<s128(minpos)<<"\n";
  std::cout<<"minimum_index = "<<minidx[0]<<","<<minidx[1]<<","<<minidx[2]<<","<<minidx[3]<<"\n";
  std::cout<<"interpretation = every mixed four-linear value on the 72 t=0 and 72 t=1/10 knot vectors is nonnegative\n";
  return 0;
}
