#include <boost/multiprecision/cpp_int.hpp>
#include <array>
#include <cstdint>
#include <iostream>
#include <limits>
#include <map>
#include <set>
#include <unordered_set>
using boost::multiprecision::cpp_int; using u64=uint64_t; using i64=long long;
struct M{u64 lo,hi;bool operator==(M const&o)const{return lo==o.lo&&hi==o.hi;}bool operator<(M const&o)const{return hi<o.hi||(hi==o.hi&&lo<o.lo);}};
struct H{size_t operator()(M const&m)const noexcept{return std::hash<u64>()(m.lo^(m.hi*0x9e3779b97f4a7c15ULL));}};
static constexpr int Q=1<<20; static const int PR[]={2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61};
std::map<int,int>lf;std::array<M,128>nb;i64 tl[65];int8_t chi[128][128];
cpp_int pw(int b,int e){cpp_int x=b,r=1;while(e){if(e&1)r*=x;e>>=1;if(e)x*=x;}return r;}
void initlog(){for(int p:PR)lf[p]=(p==2?Q:boost::multiprecision::msb(pw(p,Q)));}
i64 llo(int a){if(a<=1)return 0;int x=a;i64 z=0;for(int p:PR){int e=0;while(x%p==0){x/=p;e++;}z+=(i64)e*lf[p];}if(x!=1)std::exit(2);return z;}
i64 lhi63(){return 2LL*(lf[3]+1)+(lf[7]+1);} 
inline bool has(M m,int v){return v<64?((m.lo>>v)&1):((m.hi>>(v-64))&1);}inline M add(M m,int v){if(v<64)m.lo|=1ULL<<v;else m.hi|=1ULL<<(v-64);return m;}
inline M OR(M a,M b){return{a.lo|b.lo,a.hi|b.hi};}inline M AN(M a,M b){return{a.lo&~b.lo,a.hi&~b.hi};}inline bool emp(M m){return!(m.lo|m.hi);}inline int take(M&t){if(t.lo){int v=__builtin_ctzll(t.lo);t.lo&=t.lo-1;return v;}int v=64+__builtin_ctzll(t.hi);t.hi&=t.hi-1;return v;}inline int ip(M a,M b){return __builtin_popcountll(a.lo&b.lo)+__builtin_popcountll(a.hi&b.hi);} 
int edges(M m){int e2=0;M t=m;while(!emp(t)){int v=take(t);e2+=ip(nb[v],m);}return e2/2;}M bd(M m){M b{0,0},t=m;while(!emp(t)){int v=take(t);b=OR(b,nb[v]);}return AN(b,m);} 
void FV(M m,std::array<int,128>&F){F.fill(0);M t=m;while(!emp(t)){int v=take(t);for(int s=0;s<128;s++)F[s]+=chi[s][v];}}
i64 Lmask(M m,int mm,int e){std::array<int,128>F;FV(m,F);int B=7*mm-2*e;i64 T=tl[64-mm];for(int s=1;s<128;s++)T+=tl[std::abs(F[s])];return 24576LL*(B-7)*Q+7*T-3969LL*B*lhi63();}
i64 Ladd(std::array<int,128>const&F,int v,int mm,int e){int B=7*mm-2*e;i64 T=tl[64-mm];for(int s=1;s<128;s++)T+=tl[std::abs(F[s]+chi[s][v])];return 24576LL*(B-7)*Q+7*T-3969LL*B*lhi63();}
template<class S>std::pair<long long,i64> scan(S const&s,int mm,int e){long long c=0;i64 mn=LLONG_MAX;for(auto m:s){i64 z=Lmask(m,mm,e);c++;mn=std::min(mn,z);}return{c,mn};}
int main(){initlog();for(int a=0;a<=64;a++)tl[a]=(i64)a*a*llo(a);for(int v=0;v<128;v++){M z{0,0};for(int i=0;i<7;i++)z=add(z,v^(1<<i));nb[v]=z;for(int s=0;s<128;s++)chi[s][v]=(__builtin_popcount((unsigned)(s&v))&1)?-1:1;}
 std::set<M>L{{1,0}};for(int k=1;k<8;k++){std::set<M>N;for(auto m:L){M b=bd(m);while(!emp(b)){int v=take(b);N.insert(add(m,v));}}L.swap(N);}std::cout<<"connected_layer8="<<L.size()<<"\n";
 std::unordered_set<M,H>p11,p12,p13;p11.reserve(400000);p12.reserve(30000);p13.reserve(3000);for(auto m:L){int ep=edges(m);if(ep>12)continue;M b=bd(m);while(!emp(b)){int v=take(b),en=ep+ip(nb[v],m);if(en==11)p11.insert(add(m,v));else if(en==12)p12.insert(add(m,v));else if(en==13)p13.insert(add(m,v));}}
 auto a9_11=scan(p11,9,11),a9_12=scan(p12,9,12);std::cout<<"m9 connected e11 count="<<a9_11.first<<" minL="<<a9_11.second<<"; e12 count="<<a9_12.first<<" minL="<<a9_12.second<<"\n";
 long long d9=0;i64 d9m=LLONG_MAX;for(auto m:L)if(edges(m)==12)for(int v=0;v<128;v++)if(!has(m,v)&&ip(nb[v],m)==0){M z=add(m,v);d9++;d9m=std::min(d9m,Lmask(z,9,12));}std::cout<<"m9 disconnected e12 8+1 reps="<<d9<<" minL="<<d9m<<"; disconnected e11 excluded by m8_e11 impossibility certificate\n";
 std::unordered_set<M,H>q13,q14,q15;q13.reserve(600000);q14.reserve(50000);q15.reserve(5000);auto ex10=[&](auto const&P,int ep){for(auto m:P){M b=bd(m);while(!emp(b)){int v=take(b),en=ep+ip(nb[v],m);if(en==13)q13.insert(add(m,v));else if(en==14)q14.insert(add(m,v));else if(en==15)q15.insert(add(m,v));}}};ex10(p11,11);ex10(p12,12);ex10(p13,13);auto a10_13=scan(q13,10,13),a10_14=scan(q14,10,14);std::cout<<"m10 connected e13 count="<<a10_13.first<<" minL="<<a10_13.second<<"; e14 count="<<a10_14.first<<" minL="<<a10_14.second<<"; e15_count="<<q15.size()<<"\n";
 long long d10a=0,d10b=0;i64 d10ma=LLONG_MAX,d10mb=LLONG_MAX;for(auto m:p13)for(int v=0;v<128;v++)if(!has(m,v)&&ip(nb[v],m)==0){M z=add(m,v);d10a++;d10ma=std::min(d10ma,Lmask(z,10,13));}for(auto m:L)if(edges(m)==12)for(int v=0;v<128;v++)if(!has(m,v)&&ip(nb[v],m)==0)for(int i=0;i<7;i++){int w=v^(1<<i);if(v>w||has(m,w)||ip(nb[w],m)!=0)continue;M z=add(add(m,v),w);d10b++;d10mb=std::min(d10mb,Lmask(z,10,13));}std::cout<<"m10 disconnected e13 reps9+1="<<d10a<<" minL="<<d10ma<<" reps8+2="<<d10b<<" minL="<<d10mb<<"; e14 disconnected impossible (max13)\n";
 std::unordered_set<M,H>r15,r16,r17;r15.reserve(1200000);r16.reserve(100000);r17.reserve(10000);auto ex11=[&](auto const&P,int ep){for(auto m:P){M b=bd(m);while(!emp(b)){int v=take(b),en=ep+ip(nb[v],m);if(en==15)r15.insert(add(m,v));else if(en==16)r16.insert(add(m,v));else if(en==17)r17.insert(add(m,v));}}};ex11(q13,13);ex11(q14,14);ex11(q15,15);auto a11_15=scan(r15,11,15),a11_16=scan(r16,11,16);std::cout<<"m11 connected e15 count="<<a11_15.first<<" minL="<<a11_15.second<<"; e16 count="<<a11_16.first<<" minL="<<a11_16.second<<"; e17_count="<<r17.size()<<"\n";
 long long d11=0;i64 d11m=LLONG_MAX;for(auto m:q15)for(int v=0;v<128;v++)if(!has(m,v)&&ip(nb[v],m)==0){M z=add(m,v);d11++;d11m=std::min(d11m,Lmask(z,11,15));}std::cout<<"m11 disconnected e15 10+1 reps="<<d11<<" minL="<<d11m<<"; e16 disconnected impossible (max15)\n";
 long long c17=0,c18=0,c19=0;i64 m17=LLONG_MAX,m18=LLONG_MAX,m19=LLONG_MAX;auto ex12=[&](auto const&P,int ep){for(auto m:P){std::array<int,128>F;FV(m,F);M b=bd(m);while(!emp(b)){int v=take(b),en=ep+ip(nb[v],m);if(en>=17&&en<=19){i64 z=Ladd(F,v,12,en);if(en==17){c17++;m17=std::min(m17,z);}else if(en==18){c18++;m18=std::min(m18,z);}else{c19++;m19=std::min(m19,z);}}}}};ex12(r15,15);ex12(r16,16);ex12(r17,17);std::cout<<"m12 connected representations e17="<<c17<<" minL="<<m17<<" e18="<<c18<<" minL="<<m18<<" e19="<<c19<<" minL="<<m19<<"\n";
 long long d12=0;i64 d12m=LLONG_MAX;for(auto m:r17)for(int v=0;v<128;v++)if(!has(m,v)&&ip(nb[v],m)==0){M z=add(m,v);d12++;d12m=std::min(d12m,Lmask(z,12,17));}std::cout<<"m12 disconnected e17 11+1 reps="<<d12<<" minL="<<d12m<<"; e18/e19 disconnected impossible (max17)\n";
 bool ok=a9_11.second>0&&a9_12.second>0&&d9m>0&&a10_13.second>0&&a10_14.second>0&&d10ma>0&&d10mb>0&&a11_15.second>0&&a11_16.second>0&&d11m>0&&m17>0&&m18>0&&m19>0&&d12m>0;
 std::cout<<"NEAR_HARPER_M9_M12_CERTIFICATE="<<(ok?"PASS":"FAIL")<<"\n";return ok?0:5;}
