// Lazy sampling of an iid Dirichlet environment on the unbounded square lattice.
#include <array>
#include <cmath>
#include <cstdint>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <random>
#include <stdexcept>
#include <string>
#include <sys/resource.h>
#include <unordered_map>
#include <vector>

struct Config { std::string name; std::array<double,4> alpha; };
struct Row { std::array<double,3> cdf; };
using RNG = std::mt19937_64;
uint64_t key(int32_t x, int32_t y) {
    return (uint64_t(uint32_t(x)) << 32) | uint32_t(y);
}
double uniform(RNG &rng) {
    return std::generate_canonical<double,53>(rng);
}
double open_uniform(RNG &rng) {
    double u;
    do { u = uniform(rng); } while (u == 0.0);
    return u;
}

int main(int argc, char**argv) {
    const int reps = argc > 1 ? std::stoi(argv[1]) : 24;
    const uint64_t steps = argc > 2 ? std::stoull(argv[2]) : 2000000;
    const uint64_t samples = argc > 3 ? std::stoull(argv[3]) : 1000000;
    const std::string out = argc > 4 ? argv[4] : "data";
    if (getpriority(PRIO_PROCESS,0) < 10) {
        if (setpriority(PRIO_PROCESS,0,10) != 0) throw std::runtime_error("nice 10 required");
    }
    std::vector<Config> configs;
    for(double k : {0.8, 1.0, 1.05, 1.2, 2.0, 3.0, 6.0}) {
        std::string name = "horizontal_k" + std::to_string(k);
        configs.push_back({name,{.375*k,.125*k,.125*k,.125*k}});
    }
    configs.push_back({"vertical_trap_k1.1",{.1,.4,.05,.4}});
    configs.push_back({"weak_drift_k1.05",{.30*1.05/1.55,.25*1.05/1.55,
                                          .25*1.05/1.55,.25*1.05/1.55}});
    std::ofstream paths(out+"/paths.csv"), episodes(out+"/episodes.csv"),
                  traps(out+"/traps.csv"), params(out+"/parameters.csv");
    for(auto *f : {&paths,&episodes,&traps,&params}) {
        if(!*f) throw std::runtime_error("Cannot open output directory");
        *f << std::setprecision(17);
    }
    params << "config,a_plus_x,a_plus_y,a_minus_x,a_minus_y,kappa,dx,dy\n";
    paths << "config,rep,seed,n,x,y,vx,vy,visited_sites,max_completed_run,censored_final_run\n";
    episodes << "config,rep,threshold,completed_runs_ge_threshold\n";
    traps << "config,axis,samples,threshold,exceedances,mean_T,max_T\n";
    const int dx[4]={1,0,-1,0},dy[4]={0,1,0,-1};
    const std::array<uint64_t,8> run_thresholds={1,2,10,100,1000,10000,100000,1000000};
    const std::vector<uint64_t> times={1000,10000,100000,1000000,steps};
    const uint64_t base_seed=13620261113ULL;
    for(size_t ci=0;ci<configs.size();ci++) {
        const auto &cfg=configs[ci];
        const auto &a=cfg.alpha;
        const double A=a[0]+a[1]+a[2]+a[3];
        const double k=2*A-std::max(a[0]+a[2],a[1]+a[3]);
        params<<cfg.name;
        for(double v:a) params<<','<<v;
        params<<','<<k<<','<<a[0]-a[2]<<','<<a[1]-a[3]<<'\n';
        std::array<std::gamma_distribution<double>,4> gamma={
            std::gamma_distribution<double>(a[0],1),std::gamma_distribution<double>(a[1],1),
            std::gamma_distribution<double>(a[2],1),std::gamma_distribution<double>(a[3],1)};
        for(int rep=0;rep<reps;rep++) {
            const uint64_t seed=base_seed+1000003*ci+7919*rep;
            RNG rng(seed);
            std::unordered_map<uint64_t,Row> env;
            env.reserve(131072);
            int32_t x=0,y=0;
            uint64_t oldlo=0,oldhi=0,run=0,maxrun=0;
            std::array<uint64_t,8> run_counts{};
            auto finish=[&](){
                maxrun=std::max(maxrun,run);
                for(size_t j=0;j<run_thresholds.size();j++)
                    run_counts[j]+=(run>=run_thresholds[j]);
            };
            for(uint64_t n=1;n<=steps;n++) {
                const auto before=key(x,y);
                auto it=env.find(before);
                if(it==env.end()) {
                    std::array<double,4> g;
                    double sum=0;
                    for(int j=0;j<4;j++) {g[j]=gamma[j](rng);sum+=g[j];}
                    if(!(sum>0)) throw std::runtime_error("Gamma underflow");
                    Row row{{g[0]/sum,(g[0]+g[1])/sum,(g[0]+g[1]+g[2])/sum}};
                    it=env.emplace(before,row).first;
                }
                const double u=uniform(rng);
                int dir=0;
                while(dir<3 && u>=it->second.cdf[dir]) dir++;
                x+=dx[dir];y+=dy[dir];
                const auto after=key(x,y);
                const auto lo=std::min(before,after),hi=std::max(before,after);
                if(run>0 && lo==oldlo && hi==oldhi) run++;
                else {if(run>0)finish();run=1;oldlo=lo;oldhi=hi;}
                bool checkpoint=false;
                for(auto t:times) if(n==t)checkpoint=true;
                if(checkpoint)
                    paths<<cfg.name<<','<<rep<<','<<seed<<','<<n<<','<<x<<','<<y<<','
                         <<double(x)/n<<','<<double(y)/n<<','<<env.size()<<','<<maxrun<<','<<run<<'\n';
            }
            for(size_t j=0;j<run_thresholds.size();j++)
                episodes<<cfg.name<<','<<rep<<','<<run_thresholds[j]<<','<<run_counts[j]<<'\n';
        }
        // Independent freshly sampled two-site traps; choose the strongest axis.
        const int axis=a[0]+a[2]>=a[1]+a[3]?0:1;
        const int reverse=axis+2;
        std::gamma_distribution<double> exit0(A-a[axis],1),inside0(a[axis],1),
                                        exit1(A-a[reverse],1),inside1(a[reverse],1);
        RNG rng(base_seed+500000003+1000003*ci);
        const std::vector<uint64_t> thresholds={2,4,10,20,40,100,200,400,1000,2000,4000,
                                               10000,20000,40000,100000,200000,1000000};
        std::vector<uint64_t> counts(thresholds.size(),0);
        long double total=0;uint64_t maxT=0;
        for(uint64_t j=0;j<samples;j++) {
            const double ga=exit0(rng),gb=inside0(rng),gc=exit1(rng),gd=inside1(rng);
            const double r=ga/(ga+gb),s=gc/(gc+gd);
            const double q=r+s-r*s;
            if(!(q>0 && q<=1))throw std::runtime_error("Invalid escape probability");
            const double cycles=q==1?0:std::floor(std::log(open_uniform(rng))/std::log1p(-q));
            if(cycles>1e18)throw std::runtime_error("Holding time out of integer range");
            const uint64_t T=2*uint64_t(cycles)+(uniform(rng)<r/q?1:2);
            total+=T;maxT=std::max(maxT,T);
            for(size_t z=0;z<thresholds.size();z++) counts[z]+=(T>thresholds[z]);
        }
        for(size_t z=0;z<thresholds.size();z++)
            traps<<cfg.name<<','<<axis<<','<<samples<<','<<thresholds[z]<<','<<counts[z]
                 <<','<<double(total/samples)<<','<<maxT<<'\n';
        paths.flush();episodes.flush();traps.flush();params.flush();
        rusage usage{};getrusage(RUSAGE_SELF,&usage);
        std::cout<<cfg.name<<" finished; maxrss "<<usage.ru_maxrss<<" (macOS bytes)\n"<<std::flush;
    }
}
