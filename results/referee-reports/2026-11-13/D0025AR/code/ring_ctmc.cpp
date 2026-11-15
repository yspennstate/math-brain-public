// Independent ring simulator. Fixed-time Poisson uniformization of departure clocks.
#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdint>
#include <cstdlib>
#include <iomanip>
#include <iostream>
#include <numeric>
#include <random>
#include <string>
#include <vector>
#include <sys/resource.h>
#include <sys/time.h>
#include <cerrno>
int main(int argc,char**argv) {
 if(argc!=11) { std::cerr<<"n K density slow_probability env_seed dyn_seed burn measure blocks initial\n";return 2; }
 int n=std::stoi(argv[1]), K=std::stoi(argv[2]), blocks=std::stoi(argv[9]);
 double rho=std::stod(argv[3]), prob=std::stod(argv[4]), burn=std::stod(argv[7]), duration=std::stod(argv[8]);
 uint64_t es=std::stoull(argv[5]), ds=std::stoull(argv[6]); std::string init=argv[10];
 if(n<2||n>1000000||K<1||K>100||rho<0||rho>K||blocks<1||duration<=0) return 3;
 errno=0; int priority=getpriority(PRIO_PROCESS,0); if(errno||priority<10){std::cerr<<"nice must be >=10\n";return 4;}
 std::mt19937_64 erng(es), rng(ds); std::bernoulli_distribution slow_coin(prob);
 std::vector<uint8_t> slow(n); int ns=0;
 for(int i=0;i<n;i++) ns+=(slow[i]=slow_coin(erng));
 std::vector<int> eta(n,0),before(n); std::vector<uint64_t> bonds(n,0);
 int mass=std::llround(rho*n); std::vector<int> slots(n*K);std::iota(slots.begin(),slots.end(),0);
 if(init=="packed") {for(int i=0;i<mass;i++)eta[i/K]++;}
 else {std::shuffle(slots.begin(),slots.end(),rng);for(int i=0;i<mass;i++)eta[slots[i]/K]++;}
 slots.clear(); slots.shrink_to_fit();
 std::uniform_int_distribution<int> site(0,n-1); uint64_t total=0;
 auto window=[&](double t,bool count) {
   std::poisson_distribution<uint64_t> attempts(n*t); auto m=attempts(rng);uint64_t jumps=0;
   for(uint64_t z=0;z<m;z++) { int i=site(rng),j=i+1==n?0:i+1;
     if(eta[i]>0&&eta[j]<K&&(!slow[i]||(rng()&1))) {eta[i]--;eta[j]++;jumps++;if(count)bonds[i]++;}
   }
   assert(std::accumulate(eta.begin(),eta.end(),0)==mass);
   for(int x:eta)assert(x>=0&&x<=K);
   return jumps;
 };
 window(burn,false); before=eta; std::vector<double> currents;
 for(int b=0;b<blocks;b++) {uint64_t j=window(duration/blocks,true);total+=j;currents.push_back(j/(n*(duration/blocks)));}
 for(int i=0;i<n;i++){int im=i?i-1:n-1;assert(int64_t(eta[i]-before[i])==int64_t(bonds[im])-int64_t(bonds[i]));}
 auto mm=std::minmax_element(bonds.begin(),bonds.end()); double current=total/(n*duration),sd=0;
 for(auto v:currents)sd+=(v-current)*(v-current);sd=std::sqrt(sd/std::max(1,blocks-1));
 int run=0,longest=0;for(int i=0;i<2*n;i++){run=slow[i%n]?run+1:0;longest=std::max(longest,std::min(run,n));}
 rusage usage{};getrusage(RUSAGE_SELF,&usage);
 std::cout<<std::setprecision(12)<<"{\"n\":"<<n<<",\"K\":"<<K<<",\"rho\":"<<double(mass)/n
 <<",\"p_slow\":"<<prob<<",\"r\":0.5,\"env_seed\":"<<es<<",\"dyn_seed\":"<<ds<<",\"n_slow\":"<<ns
 <<",\"longest_slow_run\":"<<longest<<",\"burn\":"<<burn<<",\"measure\":"<<duration<<",\"initial\":\""<<init
 <<"\",\"current\":"<<current<<",\"block_sd\":"<<sd<<",\"bond_min\":"<<*mm.first/duration<<",\"bond_max\":"<<*mm.second/duration
 <<",\"nice\":"<<priority<<",\"maxrss_native\":"<<usage.ru_maxrss<<",\"blocks\":[";
 for(size_t b=0;b<currents.size();b++){if(b)std::cout<<",";std::cout<<currents[b];}std::cout<<"],\"slow_sites\":["; if(n<=100){bool comma=false;for(int i=0;i<n;i++)if(slow[i]){if(comma)std::cout<<",";std::cout<<i;comma=true;}}std::cout<<"]}\n";
}
