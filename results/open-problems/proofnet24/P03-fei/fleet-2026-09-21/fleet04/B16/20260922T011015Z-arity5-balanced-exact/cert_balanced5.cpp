#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <vector>
#include <boost/multiprecision/cpp_int.hpp>
using boost::multiprecision::cpp_int;
static const int P[6]={2,3,5,7,11,13};
static const uint64_t Q=1u<<16;
static inline int pc(uint32_t x){return __builtin_popcount(x);}
static inline int par(uint32_t x){return __builtin_parity(x);}
struct D{std::array<int16_t,16> W{};uint8_t b=0,w=0,dep=0;};
static D calc(uint16_t tt){D d;d.w=pc(tt);for(int s=0;s<16;s++){int z=0;for(int x=0;x<16;x++)z+=(((tt>>x)&1)?-1:1)*(par(s&x)?-1:1);d.W[s]=z;}for(int i=0;i<4;i++)for(int x=0;x<16;x++)if(!(x>>i&1)){int q=(((tt>>x)&1)!=((tt>>(x^(1<<i)))&1));d.b+=q;if(q)d.dep|=1<<i;}return d;}
static std::vector<std::array<int,4>> perms(){std::vector<std::array<int,4>>v;std::array<int,4>a={0,1,2,3};do v.push_back(a);while(std::next_permutation(a.begin(),a.end()));return v;}
static uint16_t tr(uint16_t f,const std::array<int,4>&p,int n,int o){uint16_t g=0;for(int x=0;x<16;x++){int y=0;for(int i=0;i<4;i++)y|=((((x>>p[i])&1)^((n>>i)&1))<<i);g|=((((f>>y)&1)^o)<<x);}return g;}
static std::vector<uint16_t> reps(){auto pp=perms();std::vector<char>s(65536);std::vector<uint16_t>r;for(int f=0;f<65536;f++)if(!s[f]){r.push_back(f);for(auto&p:pp)for(int n=0;n<16;n++)for(int o=0;o<2;o++)s[tr(f,p,n,o)]=1;}return r;}
static cpp_int ipow(cpp_int b,uint64_t e){cpp_int r=1;while(e){if(e&1)r*=b;e>>=1;if(e)b*=b;}return r;}
static std::array<uint64_t,6> floors(){std::array<uint64_t,6>k{};for(int j=0;j<6;j++)k[j]=boost::multiprecision::msb(ipow(cpp_int(P[j]),Q));return k;}
static int vp(int a,int p){int v=0;while(a&&a%p==0){a/=p;v++;}return v;}
struct Cnt{uint64_t strict=0,tie=0,inc=0,minpos=~0ull;uint16_t tg=0,th=0;int tB=-1;};
static int sign_cert(const std::array<long long,6>&e,const std::array<uint64_t,6>&K,uint64_t&poslower){bool zero=true;for(auto x:e)if(x)zero=false;if(zero)return 0;__int128 lo=0,hi=0;for(int j=0;j<6;j++){long long x=e[j];if(j==0){lo+=(__int128)x*Q;hi+=(__int128)x*Q;}else if(x>0){lo+=(__int128)x*K[j];hi+=(__int128)x*(K[j]+1);}else if(x<0){lo+=(__int128)x*(K[j]+1);hi+=(__int128)x*K[j];}}if(lo>0){poslower=(uint64_t)lo;return 1;}if(hi<0)return -1;return 2;}
static bool prime_tt(uint32_t tt){for(int i=0;i<5;i++){bool dep=false;for(int x=0;x<32;x++)if(!(x>>i&1)&&(((tt>>x)&1)!=((tt>>(x^(1<<i)))&1))){dep=true;break;}if(!dep)return false;}for(int mask=0;mask<32;mask++){int k=pc(mask);if(k<2||k>4)continue;std::array<uint32_t,16> rows{};int nr=0;std::vector<int>A,C;for(int i=0;i<5;i++)((mask>>i)&1?A:C).push_back(i);for(int av=0;av<(1<<(int)A.size());av++){uint32_t row=0;for(int cv=0;cv<(1<<(int)C.size());cv++){int x=0;for(int j=0;j<(int)A.size();j++)x|=((av>>j)&1)<<A[j];for(int j=0;j<(int)C.size();j++)x|=((cv>>j)&1)<<C[j];row|=((tt>>x)&1)<<cv;}bool seen=false;for(int z=0;z<nr;z++)if(rows[z]==row)seen=true;if(!seen)rows[nr++]=row;}if(nr<=2)return false;}return true;}
int main(){auto K=floors();std::vector<D>d(65536);for(int f=0;f<65536;f++)d[f]=calc(f);auto R=reps();uint64_t balanced=0,full=0;Cnt six,sharp;uint32_t sharp_tt=0;bool sharp_prime=false;
for(uint16_t g:R)for(uint32_t hu=0;hu<65536;hu++){uint16_t h=hu;if(d[g].w+d[h].w!=16)continue;balanced++;int B=d[g].b+d[h].b+pc(g^h);std::array<long long,6>S{};for(int s=0;s<16;s++){int ww[2]={(int)d[g].W[s]+d[h].W[s],(int)d[g].W[s]-d[h].W[s]};for(int t=0;t<2;t++){int a=abs(ww[t])/2;if(a<=1)continue;int rem=a;for(int j=0;j<6;j++){int v=vp(rem,P[j]);if(v){S[j]+=(long long)a*a*v;for(int q=0;q<v;q++)rem/=P[j];}}if(rem!=1){std::cerr<<"factorfail\n";return 2;}}}
 std::array<long long,6>e6=S;e6[0]-=(1792-48*B);uint64_t pl=0;int sg=sign_cert(e6,K,pl);if(sg<0){std::cerr<<"H<=6(I-1) counterexample\n";return 3;}if(sg==2)six.inc++;else if(sg==0){six.tie++;if(six.tB<0){six.tg=g;six.th=h;six.tB=B;}}else{six.strict++;six.minpos=std::min(six.minpos,pl);}
 uint8_t dep=d[g].dep|d[h].dep;if(g!=h)dep|=16;if(dep!=31)continue;full++;std::array<long long,6>es{};for(int j=0;j<6;j++)es[j]=5*S[j];es[0]+=352LL*(B-16)-5120;es[1]-=72LL*(B-16);pl=0;sg=sign_cert(es,K,pl);if(sg<0){std::cerr<<"sharp counterexample\n";return 4;}if(sg==2)sharp.inc++;else if(sg==0){sharp.tie++;if(sharp.tB<0){sharp.tg=g;sharp.th=h;sharp.tB=B;sharp_tt=((uint32_t)h<<16)|g;sharp_prime=prime_tt(sharp_tt);}}else{sharp.strict++;sharp.minpos=std::min(sharp.minpos,pl);}
}
std::cout<<"NPN4_reps="<<R.size()<<" Q="<<Q<<"\n";
std::cout<<"balanced="<<balanced<<" six_strict="<<six.strict<<" six_ties="<<six.tie<<" six_inconclusive="<<six.inc<<" six_minpos="<<six.minpos<<"\n";
std::cout<<"fullsupport_balanced="<<full<<" sharp_strict="<<sharp.strict<<" sharp_ties="<<sharp.tie<<" sharp_inconclusive="<<sharp.inc<<" sharp_minpos="<<sharp.minpos<<"\n";
std::cout<<"sharp_first_tie g="<<sharp.tg<<" h="<<sharp.th<<" B="<<sharp.tB<<" tt=0x"<<std::hex<<sharp_tt<<std::dec<<" composition_prime="<<(sharp_prime?1:0)<<"\n";
return (six.inc||sharp.inc)?5:0;}
