// Complete exact Walsh transform of the distinct vertex polynomial.
#include <array>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <unordered_map>
#include <string>
using Int=__int128_t;
std::string decimal(Int x){if(!x)return "0";bool neg=x<0;if(neg)x=-x;std::string s;while(x){s+=char('0'+x%10);x/=10;}if(neg)s+='-';return std::string(s.rbegin(),s.rend());}
int main(){
 int choose[16][16]={};for(int n=0;n<16;n++){choose[n][0]=choose[n][n]=1;for(int k=1;k<n;k++)choose[n][k]=choose[n-1][k-1]+choose[n-1][k];}
 int coeff[16][16][16]={};
 for(int a=0;a<=15;a++)for(int b=0;b<=15-a;b++)for(int k=0;k<=a+b;k++)for(int i=0;i<=a;i++)if(k-i>=0&&k-i<=b)coeff[a][b][k]+=choose[a][i]*choose[b][k-i]*(((k-i)&1)?-1:1);
 std::ifstream in("sidorenko_attempt/continuation_20261002_cube8_vertex_polynomial.tsv");uint64_t key,c;
 std::unordered_map<uint64_t,Int>P;while(in>>key>>c)P[key]=Int(c)*(Int(1)<<18);
 for(int bit=1;bit<8;bit*=2)for(int i=0;i<8;i++)if(!(i&bit)){
  int j=i|bit;std::unordered_map<uint64_t,Int>Q;Q.reserve(180000);
  uint64_t mask=~((uint64_t(15)<<(4*i))|(uint64_t(15)<<(4*j)));
  for(auto [n,v]:P){int a=(n>>(4*i))&15,b=(n>>(4*j))&15;uint64_t rest=n&mask;
   for(int k=0;k<=a+b;k++)if(coeff[a][b][k])Q[rest+(uint64_t(a+b-k)<<(4*i))+(uint64_t(k)<<(4*j))]+=v*coeff[a][b][k];
  }
  P.clear();for(auto [n,v]:Q)if(v)P[n]=v;
  std::cout<<"pair "<<i<<","<<j<<" nonzero "<<P.size()<<std::endl;
 }
 Int scale=Int(1)<<45;
 std::ofstream out("sidorenko_attempt/continuation_20261002_cube8_walsh_audit.tsv");
 for(auto [n,v]:P){if(v%scale){std::cerr<<"normalization failure\n";return 2;}out<<n<<'\t'<<decimal(v/scale)<<'\n';}
 std::cout<<"PASS entire Walsh polynomial terms "<<P.size()<<std::endl;
}
