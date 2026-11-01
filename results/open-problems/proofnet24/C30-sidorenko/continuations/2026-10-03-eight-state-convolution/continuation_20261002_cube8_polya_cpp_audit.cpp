// Independent exact C++ regeneration of the exceptional-chamber multiplier.
// Fixed-degree arithmetic bounds here are below 10^30, hence inside int128.
#include <cstdint>
#include <fstream>
#include <iostream>
#include <unordered_map>
#include <string>
#include <array>
using Int=__int128_t;
using Poly=std::unordered_map<uint64_t,Int>;
std::string decimal(Int x){if(!x)return "0";bool neg=x<0;if(neg)x=-x;std::string s;while(x){s+=char('0'+x%10);x/=10;}if(neg)s+='-';return std::string(s.rbegin(),s.rend());}
Int ipow(Int x,int n){Int y=1;while(n--)y*=x;return y;}
uint64_t fact[16];int choose[16][16];
void subtract_mean(Poly& P,int i,int left,uint64_t key,uint64_t denominator,Int weight){
 if(i==7){int v=left;key+=uint64_t(v)<<(6*i);denominator*=fact[v];weight*=ipow(i+1,v);P[key]-=Int(fact[15]/denominator)*weight;return;}
 for(int v=0;v<=left;v++)subtract_mean(P,i+1,left-v,key+(uint64_t(v)<<(6*i)),denominator*fact[v],weight*ipow(i+1,v));
}
void remove_zero(Poly& P){for(auto it=P.begin();it!=P.end();)if(!it->second)it=P.erase(it);else ++it;}
int main(){
 fact[0]=1;for(int i=1;i<16;i++)fact[i]=fact[i-1]*i;
 for(int n=0;n<16;n++){choose[n][0]=choose[n][n]=1;for(int k=1;k<n;k++)choose[n][k]=choose[n-1][k-1]+choose[n-1][k];}
 int order[8]={3,5,6,7,4,2,1,0};
 std::ifstream in("sidorenko_attempt/continuation_20261002_cube8_vertex_polynomial.tsv");uint64_t n,c;Poly P;
 while(in>>n>>c){uint64_t key=0;for(int i=0;i<8;i++)key+=((n>>(4*order[i]))&15)<<(6*i);P[key]=Int(c)*(Int(1)<<18);}
 for(int i=0;i<7;i++){
  Poly Q;Q.reserve(180000);
  for(auto [key,v]:P){int a=(key>>(6*i))&63;for(int k=0;k<=a;k++)Q[key-(uint64_t(k)<<(6*i))+(uint64_t(k)<<(6*(i+1)))]+=v*choose[a][k];}
  P=std::move(Q);
 }
 subtract_mean(P,0,15,0,1,1);remove_zero(P);
 for(int step=1;step<=2;step++){
  Poly Q;Q.reserve(350000);
  for(auto [key,v]:P)for(int i=0;i<7;i++)Q[key+(uint64_t(1)<<(6*i))]+=v;
  P=std::move(Q);remove_zero(P);
  int negative=0;for(auto [key,v]:P)negative+=v<0;
  std::cout<<"step "<<step<<" terms "<<P.size()<<" negative "<<negative<<std::endl;
 }
 if(P.size()!=345312)return 2;
 for(auto [key,v]:P)if(v<0)return 3;
 std::ofstream out("sidorenko_attempt/continuation_20261002_cube8_polya_cpp_audit.tsv");
 for(auto [key,v]:P)out<<key<<'\t'<<decimal(v)<<'\n';
 std::cout<<"PASS exact exceptional-chamber coefficient positivity"<<std::endl;
}
