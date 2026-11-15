// Independent exact flip-chain simulation; zero denotes infection.
#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdint>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <random>
#include <string>
#include <vector>
#include <sys/resource.h>

struct RateTree {
    int base=1;
    std::vector<double> a;
    explicit RateTree(int n) { while(base<n) base*=2; a.assign(2*base,0); }
    void set(int j,double rate) { int k=base+j; a[k]=rate; while((k/=2)>0) a[k]=a[2*k]+a[2*k+1]; }
    double total()const { return a[1]; }
    int choose(double u)const { int k=1; while(k<base) { if(u<a[2*k]) k*=2; else {u-=a[2*k];k=2*k+1;} } return k-base; }
};

int main(int argc,char** argv) {
    if(argc!=7) { std::cerr<<"q paths radius seed max_time histogram_path\n";return 2; }
    const double q=std::stod(argv[1]), p=1-q, maxt=std::stod(argv[5]);
    const int paths=std::stoi(argv[2]), rad=std::stoi(argv[3]), n=2*rad+1;
    const uint64_t seed=std::stoull(argv[4]);
    const int priority=getpriority(PRIO_PROCESS,0);
    assert(priority>=10 && q>0 && q<1 && rad>=1 && paths>1);
    std::mt19937_64 rng(seed);
    auto U=[&]() { return (double(rng()>>11)+0.5)*0x1.0p-53; };
    std::vector<double> times;
    for(double t: {0.,0.1,0.5,1.,2.,5.,10.,20.,50.,100.}) if(t<=maxt) times.push_back(t);
    if(times.back()!=maxt) times.push_back(maxt);
    std::vector<uint64_t> sums(times.size(),0), pairs(times.size(),0);
    std::vector<uint64_t> hist(n<=15 ? 1<<n : 0,0);
    uint64_t events=0, boundary_hits=0;
    int furthest=0;
    for(int sample=0;sample<paths;sample++) {
        std::vector<unsigned char> spin(n,1); spin[rad]=0;
        int zeros=1;
        RateTree rates(n);
        auto rate=[&](int j) {
            if(j<0 || j>=n) return 0.;
            bool enabled=(j>0 && spin[j-1]==0) || (j+1<n && spin[j+1]==0);
            return enabled ? (spin[j] ? q : p) : 0.;
        };
        for(int j=0;j<n;j++) rates.set(j,rate(j));
        double clock=0;
        for(size_t obs=0;obs<times.size();obs++) {
            while(clock<times[obs]) {
                double total=rates.total(); assert(total>0);
                double jump=clock-std::log(U())/total;
                if(jump>times[obs]) { clock=times[obs]; break; }
                clock=jump;
                int j=rates.choose(U()*total);
                assert(j>=0 && j<n && rate(j)>0);
                zeros += spin[j] ? 1 : -1;
                spin[j]^=1;
                assert(zeros>=1);
                if(spin[j]==0) { furthest=std::max(furthest,std::abs(j-rad)); if(j==0||j==n-1) boundary_hits++; }
                for(int k=std::max(0,j-1);k<=std::min(n-1,j+1);k++) rates.set(k,rate(k));
                events++;
            }
            sums[obs] += spin[rad]==0;
            pairs[obs] += spin[rad]==0 && spin[rad+1]==0;
        }
        double direct=0; for(int j=0;j<n;j++) direct+=rate(j);
        assert(std::abs(direct-rates.total())<1e-9*(1+direct));
        if(!hist.empty()) { int state=0; for(int j=0;j<n;j++) state|=int(spin[j])<<j;hist[state]++; }
    }
    std::cout<<std::setprecision(12)<<"q,time,paths,origin_zero_count,origin_zero_mean,origin_zero_se,pair_zero_mean\n";
    for(size_t k=0;k<times.size();k++) {
        double mean=double(sums[k])/paths;
        double se=std::sqrt(mean*(1-mean)/(paths-1));
        std::cout<<q<<','<<times[k]<<','<<paths<<','<<sums[k]<<','<<mean<<','<<se<<','<<double(pairs[k])/paths<<'\n';
    }
    if(!hist.empty()) {std::ofstream out(argv[6]);out<<"occupation_bits,count\n";for(size_t s=0;s<hist.size();s++) out<<s<<','<<hist[s]<<'\n';}
    struct rusage ru; getrusage(RUSAGE_SELF,&ru);
    std::cerr<<"seed="<<seed<<" nice="<<priority<<" paths="<<paths<<" sites="<<n<<" events="<<events<<" boundary_infections="<<boundary_hits<<" max_visited_distance="<<furthest<<" maxrss_bytes="<<ru.ru_maxrss<<'\n';
}
