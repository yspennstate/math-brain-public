// Lazy, fixed-site Dirichlet environments. One thread; no environment resampling.
#include <array>
#include <chrono>
#include <cmath>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <random>
#include <string>
#include <unordered_map>
#include <vector>
#include <sys/resource.h>

using Point = std::array<int,3>;
struct Hash {
  size_t operator()(const Point &x) const {
    size_t h=1469598103934665603ULL;
    for(auto v:x) { h ^= static_cast<unsigned>(v); h *= 1099511628211ULL; }
    return h;
  }
};
struct Model {std::string name; int d; std::array<double,6> alpha; bool low;};
struct Walk {
  int d; Point x{}; std::mt19937_64 &rng;
  std::vector<std::gamma_distribution<double>> gamma;
  std::unordered_map<Point,std::array<double,6>,Hash> env;
  Walk(const Model &m,std::mt19937_64 &r):d(m.d),rng(r) {
    for(int i=0;i<2*d;++i) gamma.emplace_back(m.alpha[i],1.0);
  }
  void step() {
    auto it=env.find(x);
    if(it==env.end()) {
      std::array<double,6> p{}; double total=0;
      for(int i=0;i<2*d;++i) {p[i]=gamma[i](rng); total+=p[i];}
      if(!(total>0)) throw std::runtime_error("gamma normalization failed");
      double sum=0;
      for(int i=0;i<2*d;++i) {sum+=p[i]/total; p[i]=sum;}
      p[2*d-1]=1;
      it=env.emplace(x,p).first;
    }
    const double u=std::generate_canonical<double,53>(rng);
    int direction=0;
    while(direction<2*d-1 && u>=it->second[direction]) ++direction;
    if(direction<d) ++x[direction]; else --x[direction-d];
  }
};

int main() {
  if(getpriority(PRIO_PROCESS,0)<10 && setpriority(PRIO_PROCESS,0,10)) return 2;
  const uint64_t seed=13720261113ULL;
  std::mt19937_64 rng(seed);
  const std::vector<Model> models={
    {"d2_moderate",2,{.55,.5,.5,.5,0,0},false},
    {"d3_moderate",3,{.55,.5,.5,.5,.5,.5},false},
    {"d2_trapping",2,{.10,.08,.08,.08,0,0},true},
    {"d3_trapping",3,{.07,.05,.05,.05,.05,.05},true}};
  const auto begin=std::chrono::steady_clock::now();
  std::ofstream slab("data/slab_counts.csv"), tail("data/renewal_proxies.csv"),
                validation("data/sampler_check.csv"), meta("data/simulation_metadata.txt");
  slab<<"model,d,L,replicates,step_cap,back,front,censored,max_sites\n";
  tail<<"model,replicate,horizon,tau_proxy,proxy_missing,range_sites\n";
  validation<<"model,direction,n,empirical_mean,theoretical_mean\n";
  meta<<"seed="<<seed<<"\nthreads=1\nnice="<<getpriority(PRIO_PROCESS,0)<<"\n";
  size_t maxsites=0; uint64_t steps=0;
  for(const auto&m:models) {
    double S=0; for(int k=0;k<2*m.d;++k) S+=m.alpha[k];
    std::array<double,6> sums{}; std::vector<std::gamma_distribution<double>> g;
    for(int k=0;k<2*m.d;++k) g.emplace_back(m.alpha[k],1);
    const int ncheck=100000;
    for(int n=0;n<ncheck;++n) {
      std::array<double,6> p{}; double s=0;
      for(int k=0;k<2*m.d;++k) s+=(p[k]=g[k](rng));
      for(int k=0;k<2*m.d;++k) sums[k]+=p[k]/s;
    }
    for(int k=0;k<2*m.d;++k)
      validation<<m.name<<","<<k<<","<<ncheck<<","<<std::setprecision(12)
                <<sums[k]/ncheck<<","<<m.alpha[k]/S<<"\n";
    for(int L:{4,8,16,32,64}) {
      int back=0,front=0,censored=0; size_t localmax=0;
      int count=m.low?500:1500, cap=m.low?100000:300000;
      for(int rep=0;rep<count;++rep) {
        Walk w(m,rng); int n=0;
        while(n<cap && std::abs(w.x[0])<L) {w.step(); ++n;}
        steps+=n; localmax=std::max(localmax,w.env.size());
        if(w.x[0]<=-L) ++back; else if(w.x[0]>=L) ++front; else ++censored;
      }
      maxsites=std::max(maxsites,localmax);
      slab<<m.name<<","<<m.d<<","<<L<<","<<count<<","<<cap<<","<<back
          <<","<<front<<","<<censored<<","<<localmax<<"\n";
      slab.flush(); std::cout<<m.name<<" L="<<L<<" back="<<back
                            <<" front="<<front<<" censored="<<censored<<std::endl;
    }
    const int count=m.low?300:600;
    for(int rep=0;rep<count;++rep) {
      Walk w(m,rng); std::vector<int> h(100001); std::vector<size_t> ranges(3);
      for(int n=1;n<=100000;++n) {
        w.step(); h[n]=w.x[0];
        if(n==10000) ranges[0]=w.env.size();
        if(n==30000) ranges[1]=w.env.size();
        if(n==100000) ranges[2]=w.env.size();
      }
      steps+=100000; maxsites=std::max(maxsites,w.env.size());
      int j=0;
      for(int H:{10000,30000,100000}) {
        std::vector<int> suffix(H+1); suffix[H]=h[H];
        for(int n=H-1;n>=0;--n) suffix[n]=std::min(suffix[n+1],h[n]);
        int previous=0,tau=H+1;
        for(int n=1;n<=H;++n) {
          if(h[n]>previous && suffix[n]>=h[n]) {tau=n; break;}
          previous=std::max(previous,h[n]);
        }
        tail<<m.name<<","<<rep<<","<<H<<","<<tau<<","<<(tau==H+1)
            <<","<<ranges[j++]<<"\n";
      }
    }
    tail.flush(); std::cout<<m.name<<" renewal proxies saved"<<std::endl;
  }
  struct rusage usage{}; getrusage(RUSAGE_SELF,&usage);
  meta<<"total_walk_steps="<<steps<<"\nmax_sites_one_environment="<<maxsites
      <<"\nru_maxrss_platform_units="<<usage.ru_maxrss
      <<"\nwall_seconds="<<std::chrono::duration<double>(std::chrono::steady_clock::now()-begin).count()<<"\n";
}
