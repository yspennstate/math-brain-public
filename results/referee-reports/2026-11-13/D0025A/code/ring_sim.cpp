// Continuous-time site-disordered simple K-exclusion, uniformized at rate n.
#include <algorithm>
#include <cmath>
#include <cstdint>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <numeric>
#include <random>
#include <string>
#include <vector>
#include <sys/resource.h>
struct RNG {
 using result_type=uint64_t; uint64_t s;
 static constexpr uint64_t min(){return 0;}
 static constexpr uint64_t max(){return UINT64_MAX;}
 uint64_t operator()(){uint64_t z=(s+=0x9e3779b97f4a7c15ULL);z=(z^(z>>30))*0xbf58476d1ce4e5b9ULL;z=(z^(z>>27))*0x94d049bb133111ebULL;return z^(z>>31);}
 double uniform(){return ((*this)()>>11)*0x1.0p-53;}
 uint64_t index(uint64_t n){
  uint64_t x=(*this)(); __uint128_t m=(__uint128_t)x*n;
  uint64_t lo=(uint64_t)m;
  if(lo<n){uint64_t threshold=(-n)%n;while(lo<threshold){x=(*this)();m=(__uint128_t)x*n;lo=(uint64_t)m;}}
  return uint64_t(m>>64);
 }
};
int main(int argc,char**argv){
 if(argc!=11){std::cerr<<"n K density r p environment_seed dynamics_seed burn measure init\n";return 2;}
 int n=std::stoi(argv[1]),K=std::stoi(argv[2]);double rho=std::stod(argv[3]),r=std::stod(argv[4]),p=std::stod(argv[5]);
 uint64_t es=std::stoull(argv[6]),ds=std::stoull(argv[7]);double burn=std::stod(argv[8]),measure=std::stod(argv[9]);std::string init=argv[10];
 if(n<2||n>1000000||K<1||K>64||int64_t(n)*K>10000000||rho<0||rho>K||r<=0||r>1||p<0||p>1)return 2;
 RNG er{es},dr{ds};std::vector<double>rate(n);std::vector<int>eta(n,0);int slow=0;
 for(auto &a:rate){a=er.uniform()<p?r:1.;slow+=a<1;}
 int run=0,longest=0,end=0;
 for(int i=0;i<2*n;++i){run=rate[i%n]<1?std::min(n,run+1):0;if(run>longest){longest=run;end=i%n;}}
 int start=(end-longest+1+n)%n;int M=std::lround(n*rho);
 if(init=="random"){
  // Sample exactly M of n*K slots without replacement. This is an initial law only.
  int left=M,total=n*K;
  for(int i=0;i<n;++i)for(int j=0;j<K;++j){if(dr.uniform()<double(left)/total){++eta[i];--left;}--total;}
 }else if(init=="packed"){
  int rem=M;for(int j=0;rem>0;++j){int i=(start-1-j+n*2)%n;int take=std::min(K,rem);eta[i]=take;rem-=take;}
 }else if(init=="phase"){
  // Two local-density regions aligned with a longest slow run; then fix total mass.
  double lo=.15*K,hi=.85*K;
  double frac=std::max(0.,std::min(1.,(rho-lo)/(hi-lo)));
  int highlen=std::lround(n*frac),sum=0;
  for(int j=0;j<n;++j){int i=(start-1-j+2*n)%n;double prob=(j<highlen?hi:lo)/K;
   for(int k=0;k<K;++k)if(dr.uniform()<prob)++eta[i];sum+=eta[i];}
  while(sum<M){int i=dr.index(n);if(eta[i]<K){++eta[i];++sum;}}
  while(sum>M){int i=dr.index(n);if(eta[i]>0){--eta[i];--sum;}}
 }else return 2;
 std::vector<uint64_t>bond(n,0);uint64_t all=0;
 auto advance=[&](double time,bool count){
  std::poisson_distribution<uint64_t>pois(n*time);uint64_t attempts=pois(dr);
  for(uint64_t z=0;z<attempts;++z){int i=dr.index(n);double u=dr.uniform();int j=i+1==n?0:i+1;
   if(u<rate[i]&&eta[i]>0&&eta[j]<K){--eta[i];++eta[j];if(count){++all;++bond[i];}}
  }
 };
 advance(burn,false);std::vector<double>blocks;constexpr int B=8;
 for(int b=0;b<B;++b){auto before=all;advance(measure/B,true);blocks.push_back(double(all-before)/(n*measure/B));}
 if(std::accumulate(eta.begin(),eta.end(),0)!=M||*std::min_element(eta.begin(),eta.end())<0||*std::max_element(eta.begin(),eta.end())>K)return 3;
 double current=double(all)/(n*measure),s=0;for(double v:blocks)s+=(v-current)*(v-current);s=std::sqrt(s/(B-1));
 int width=std::max(1,n/100);double minrho=K,maxrho=0;
 for(int i=0;i<n;i+=width){int sum=0,len=std::min(width,n-i);for(int j=i;j<i+len;++j)sum+=eta[j];minrho=std::min(minrho,double(sum)/len);maxrho=std::max(maxrho,double(sum)/len);}
 int nice_value=getpriority(PRIO_PROCESS,0);
 std::cout<<std::setprecision(12)<<n<<','<<K<<','<<double(M)/n<<','<<r<<','<<p<<','<<es<<','<<ds<<','<<burn<<','<<measure<<','<<init<<','<<slow<<','<<longest<<','<<current<<','<<s<<','<<double(*std::min_element(bond.begin(),bond.end()))/measure<<','<<double(*std::max_element(bond.begin(),bond.end()))/measure<<','<<minrho<<','<<maxrho<<','<<nice_value;
 for(double v:blocks)std::cout<<','<<v;std::cout<<'\n';
 rusage usage{};getrusage(RUSAGE_SELF,&usage);
#ifdef __APPLE__
 uint64_t peak_bytes=usage.ru_maxrss;
#else
 uint64_t peak_bytes=uint64_t(usage.ru_maxrss)*1024;
#endif
 std::cerr<<"{\"peak_rss_bytes\":"<<peak_bytes<<",\"nice\":"<<nice_value<<",\"threads\":1}\n";
}
