// Exact root-fixed enumeration is valid for convolution hosts by translation.
// This enumerates all 8^9 rooted labels and uses no numerical arithmetic.
#include <array>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <unordered_map>
int main(){
 std::unordered_map<uint64_t,uint64_t> count;count.reserve(180000);
 for(int code=0;code<4096;code++){
  std::array<int,5> x={0,code&7,(code>>3)&7,(code>>6)&7,(code>>9)&7};
  uint64_t tri[5][8];
  for(int j=0;j<5;j++)for(int y=0;y<8;y++){
   uint64_t q=0;
   for(int i=0;i<5;i++)if((j-i+5)%5==0||(j-i+5)%5==1||(j-i+5)%5==4)q+=uint64_t(1)<<(4*(x[i]^y));
   tri[j][y]=q;
  }
  for(int y0=0;y0<8;y0++)for(int y1=0;y1<8;y1++)for(int y2=0;y2<8;y2++){
   uint64_t q=tri[0][y0]+tri[1][y1]+tri[2][y2];
   for(int y3=0;y3<8;y3++)for(int y4=0;y4<8;y4++)count[q+tri[3][y3]+tri[4][y4]]++;
  }
 }
 std::ofstream out("sidorenko_attempt/continuation_20261002_cube8_vertex_polynomial.tsv");
 uint64_t total=0;
 for(auto [key,c]:count){out<<key<<'\t'<<c<<'\n';total+=c;}
 if(total!=uint64_t(1)<<27)return 2;
 std::cout<<"PASS rooted assignments "<<total<<" monomials "<<count.size()<<"\n";
}
