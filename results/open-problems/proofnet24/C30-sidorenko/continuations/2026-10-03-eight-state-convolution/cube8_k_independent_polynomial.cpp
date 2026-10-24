// Independent density/certificate reconstruction from a fundamental-cycle
// Fourier flow polynomial. No use of the author's rooted-label enumerator.
// All exponents use base 32; total degree never exceeds 17.
#include <array>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>
using I = __int128_t;
using P = std::unordered_map<uint64_t,I>;
std::string dec(I x) { if(x==0)return "0"; bool neg=x<0; if(neg)x=-x;
  std::string s; while(x){s+=char('0'+x%10);x/=10;} if(neg)s+='-';
  return std::string(s.rbegin(),s.rend()); }
void clean(P& p) { for(auto i=p.begin();i!=p.end();)if(i->second==0)i=p.erase(i);else++i; }
void save(const P& p,const std::string& path) { std::ofstream o(path);
  for(auto [key,c]:p){for(int j=0;j<8;j++)o<<((key>>(5*j))&31)<<((j==7)?'\t':',');o<<dec(c)<<'\n';} }
I power(int a,int n){I v=1;while(n--)v*=a;return v;}
uint64_t fac[18];
void mean(P& p,int j,int left,uint64_t key,uint64_t denominator,I w) {
  if(j==7) { p[key+(uint64_t(left)<<(5*j))]-=I(fac[15]/(denominator*fac[left]))*w*power(8,left);return; }
  for(int v=0;v<=left;v++)mean(p,j+1,left-v,key+(uint64_t(v)<<(5*j)),denominator*fac[v],w*power(j+1,v));
}
int main(int argc,char**argv) {
  if(argc!=3)return 1;
  std::ifstream in(argv[1]); if(!in)return 2;
  P p; std::string line; while(std::getline(in,line)) {
    size_t tab=line.find('\t');std::string ex=line.substr(0,tab);uint64_t key=0;size_t pos=0;
    for(int j=0;j<8;j++){size_t end=ex.find(',',pos);key+=uint64_t(std::stoi(ex.substr(pos,end-pos)))<<(5*j);pos=end+1;}
    p[key]+=std::stoll(line.substr(tab+1));
  }
  // Direct one-variable convolutions, rather than a signed binomial sum.
  std::vector<int64_t> table[16][16];
  for(int a=0;a<=15;a++)for(int b=0;b<=15-a;b++) {
    std::vector<int64_t> t(1,1);
    for(int k=0;k<a+b;k++) { std::vector<int64_t> u(t.size()+1,0);int sign=k<a?1:-1;
      for(size_t j=0;j<t.size();j++){u[j]+=t[j];u[j+1]+=sign*t[j];}t=std::move(u); }
    table[a][b]=std::move(t);
  }
  // r=Hadamard(p): three commuting, self-inverse binary butterflies.
  for(int bit=4;bit;bit/=2)for(int i=0;i<8;i++)if(!(i&bit)) {
    int j=i+bit;P q; q.reserve(180000);
    uint64_t mask=~((uint64_t(31)<<(5*i))|(uint64_t(31)<<(5*j)));
    for(auto [key,c]:p){int a=(key>>(5*i))&31,b=(key>>(5*j))&31;uint64_t rest=key&mask;
      for(int k=0;k<=a+b;k++)if(table[a][b][k])q[rest+(uint64_t(a+b-k)<<(5*i))+(uint64_t(k)<<(5*j))]+=c*table[a][b][k];}
    clean(q);p=std::move(q);std::cout<<"inverse-Walsh pair "<<i<<","<<j<<": "<<p.size()<<" terms\n";
  }
  if(p.size()!=89168)return 3;
  for(auto [key,c]:p)if(c<=0 || c%(I(1)<<18)!=0)return 4;
  std::string prefix=argv[2];save(p,prefix+"_density.tsv");
  // Exceptional chamber: p_3>=p_5>=p_6>=p_7>=p_4>=p_2>=p_1>=p_0.
  const int order[8]={3,5,6,7,4,2,1,0};P q;
  for(auto [key,c]:p){uint64_t newkey=0;for(int i=0;i<8;i++)newkey+=((key>>(5*order[i]))&31)<<(5*i);q[newkey]=c;}p=std::move(q);
  for(int i=0;i<7;i++) {
    q.clear();q.reserve(180000);
    for(auto [key,c]:p){int a=(key>>(5*i))&31;uint64_t choose=1;
      for(int k=0;k<=a;k++){q[key-(uint64_t(k)<<(5*i))+(uint64_t(k)<<(5*(i+1)))]+=c*choose;choose=choose*(a-k)/(k+1);}}
    p=std::move(q);
  }
  fac[0]=1;for(int i=1;i<18;i++)fac[i]=fac[i-1]*i;
  mean(p,0,15,0,1,1);clean(p);
  int negatives=0;for(auto [key,c]:p)negatives+=c<0;
  std::cout<<"raw gap: "<<p.size()<<" terms, "<<negatives<<" negatives\n";
  if(p.size()!=170406 || negatives!=367)return 5;
  save(p,prefix+"_raw_gap.tsv");
  // Independent direct L^2 expansion: seven squares and 21 cross terms.
  q.clear();q.reserve(350000);
  for(auto [key,c]:p)for(int i=0;i<7;i++) {
    q[key+(uint64_t(2)<<(5*i))]+=c;
    for(int j=i+1;j<7;j++)q[key+(uint64_t(1)<<(5*i))+(uint64_t(1)<<(5*j))]+=2*c;
  }
  clean(q);if(q.size()!=345312)return 6;
  I mn=I(1)<<126,mx=0;for(auto [key,c]:q){if(c<=0)return 7;if(c<mn)mn=c;if(c>mx)mx=c;}
  save(q,prefix+"_multiplier.tsv");
  std::cout<<"PASS multiplier: "<<q.size()<<" strictly positive coefficients; min="<<dec(mn)<<", max="<<dec(mx)<<"\n";
}
