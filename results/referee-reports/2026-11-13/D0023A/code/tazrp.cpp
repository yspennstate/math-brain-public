// Exact snapshots of the continuous-time ring ZRP by Poisson uniformization.
#include <algorithm>
#include <cmath>
#include <cstdint>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <numeric>
#include <random>
#include <stdexcept>
#include <string>
#include <vector>
#include <sys/resource.h>

static double unit(std::mt19937_64& gen) {
    return std::generate_canonical<double, 53>(gen);
}

static uint64_t evolve(std::vector<int>& n, const std::vector<double>& rates,
                       double duration, std::mt19937_64& gen, uint64_t& moves) {
    const int L = int(n.size());
    std::poisson_distribution<uint64_t> poisson(L * duration);
    std::uniform_int_distribution<int> site(0, L-1);
    const uint64_t count = poisson(gen);
    for (uint64_t j=0; j<count; ++j) {
        const int i = site(gen);
        const double u = unit(gen);
        if (n[i] > 0 && u < rates[i]) {
            --n[i]; ++n[(i+1)%L]; ++moves;
        }
    }
    return count;
}

static void validate() {
    std::ofstream out("data/tiny_endpoints.csv");
    out << "n0,n1,n2,count\n";
    int counts[5][5] = {};
    std::mt19937_64 gen(238019);
    const std::vector<double> rates{0.3,0.55,0.9};
    for (int rep=0; rep<50000; ++rep) {
        std::vector<int> n{2,1,1};
        uint64_t moves=0;
        evolve(n,rates,20.0,gen,moves);
        ++counts[n[0]][n[1]];
    }
    for (int x=0;x<=4;++x) for(int y=0;y<=4-x;++y)
        out << x << ',' << y << ',' << 4-x-y << ',' << counts[x][y] << '\n';
}

int main(int argc, char** argv) {
    if (getpriority(PRIO_PROCESS,0) < 10 && setpriority(PRIO_PROCESS,0,10))
        throw std::runtime_error("could not set nice 10");
    std::cerr << "nice=" << getpriority(PRIO_PROCESS,0) << ", one thread\n";
    if (argc>1 && std::string(argv[1])=="--validate") { validate(); return 0; }
    std::ofstream stats("data/dynamics.csv"), ratefile("data/rates.csv"), states("data/states.jsonl");
    stats << std::setprecision(15); ratefile << std::setprecision(17);
    stats << "run,seed,kappa,L,N,time,tau,attempts,moves,total,max_index,max_rate_rank,max_mass,slowest_mass,top5_mass,top10_mass,slowset_count,slowset_mass,slowset_excess_estimate,bulk_density,rho_c,min_rate,rate_gap\n";
    ratefile << "run,index,rate,rate_rank\n";
    int run=0;
    const double c=0.3, s=1-c;
    const std::vector<double> checkpoints{0,0.005,0.01,0.02,0.05,0.1,0.2,0.5,1,2,4};
    for (double kappa : {1.5,2.0,3.0}) for (int L : {128,384}) for(int rep=0;rep<6;++rep) {
        ++run;
        const uint64_t seed=20261113000ULL+1000ULL*run;
        std::mt19937_64 env(seed), gen(seed+1);
        const double rho_c=c*kappa/(s*(kappa-1));
        const int N=std::lround((rho_c+2.0)*L);
        std::vector<int> n(L),order(L),rank(L);
        std::vector<double> rates(L), critical(L);
        for(int i=0;i<L;++i) {
            rates[i]=c+s*std::pow(unit(env),1/kappa);
            critical[i]=c/(rates[i]-c);
            n[i]=((i+1)*N)/L-(i*N)/L;
        }
        std::iota(order.begin(),order.end(),0);
        std::sort(order.begin(),order.end(),[&](int i,int j){return rates[i]<rates[j];});
        for(int r=0;r<L;++r)rank[order[r]]=r+1;
        for(int i=0;i<L;++i)ratefile << run<<','<<i<<','<<rates[i]<<','<<rank[i]<<'\n';
        const double scale=std::pow(double(L),1+1/kappa);
        const double cutoff=c+s*std::pow(double(L),-1/(2*kappa));
        double previous=0;
        uint64_t attempts=0,moves=0;
        for(double tau:checkpoints) {
            const double t=tau*scale;
            attempts+=evolve(n,rates,t-previous,gen,moves); previous=t;
            int total=std::accumulate(n.begin(),n.end(),0);
            if(total!=N || *std::min_element(n.begin(),n.end())<0)
                throw std::runtime_error("mass or nonnegativity failure");
            const int maxi=std::max_element(n.begin(),n.end())-n.begin();
            int top5=0,top10=0,slowcount=0,slowmass=0;
            double baseline=0;
            for(int i=0;i<L;++i) {
                if(rank[i]<=5)top5+=n[i];
                if(rank[i]<=10)top10+=n[i];
                if(rates[i]<=cutoff){++slowcount;slowmass+=n[i];baseline+=critical[i];}
            }
            const double denom=N-rho_c*L;
            const double bulk=double(N-slowmass)/(L-slowcount);
            stats << run<<','<<seed<<','<<kappa<<','<<L<<','<<N<<','<<t<<','<<tau<<','<<attempts<<','<<moves<<','<<total<<','<<maxi<<','<<rank[maxi]<<','<<n[maxi]<<','<<n[order[0]]<<','<<top5<<','<<top10<<','<<slowcount<<','<<slowmass<<','<<(slowmass-baseline)/denom<<','<<bulk<<','<<rho_c<<','<<rates[order[0]]<<','<<rates[order[1]]-rates[order[0]]<<'\n';
            states << "{\"run\":"<<run<<",\"time\":"<<std::setprecision(17)<<t<<",\"tau\":"<<tau<<",\"eta\":[";
            for(int i=0;i<L;++i){if(i)states<<',';states<<n[i];}
            states << "]}\n";
        }
        stats.flush(); ratefile.flush(); states.flush();
        std::cerr << "run "<<run<<" kappa="<<kappa<<" L="<<L<<" attempts="<<attempts<<"\n";
    }
}
