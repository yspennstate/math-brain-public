// Independent exact flip-rate Gillespie simulation. Infection is represented by 1.
#include <algorithm>
#include <array>
#include <chrono>
#include <cmath>
#include <cstdint>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <random>
#include <stdexcept>
#include <string>
#include <vector>

struct Chain {
    int n;
    bool boundary;
    std::vector<unsigned char> infected;
    std::vector<int> births, deaths, pos;
    explicit Chain(int size, bool edge) : n(size), boundary(edge), infected(n), pos(n, -1) {}
    bool legal(int x) const {
        return (x > 0 ? infected[x-1] : boundary) ||
               (x+1 < n ? infected[x+1] : boundary);
    }
    void remove(int x) {
        if (pos[x] < 0) return;
        auto &list = infected[x] ? deaths : births;
        int at = pos[x], last = list.back();
        list[at] = last;
        pos[last] = at;
        list.pop_back();
        pos[x] = -1;
    }
    void add(int x) {
        if (!legal(x)) return;
        auto &list = infected[x] ? deaths : births;
        pos[x] = static_cast<int>(list.size());
        list.push_back(x);
    }
    void start() {
        std::fill(infected.begin(), infected.end(), 0);
        std::fill(pos.begin(), pos.end(), -1);
        births.clear(); deaths.clear();
        infected[n/2] = 1;
        for (int x=0; x<n; ++x) add(x);
    }
    void flip(int x) {
        for (int y=std::max(0,x-1); y<=std::min(n-1,x+1); ++y) remove(y);
        infected[x] ^= 1;
        for (int y=std::max(0,x-1); y<=std::min(n-1,x+1); ++y) add(y);
    }
    void check() const {
        std::vector<int> seen(n);
        for (int x : births) {
            if (infected[x] || !legal(x) || births[pos[x]]!=x || ++seen[x]!=1)
                throw std::runtime_error("birth bookkeeping");
        }
        for (int x : deaths) {
            if (!infected[x] || !legal(x) || deaths[pos[x]]!=x || ++seen[x]!=1)
                throw std::runtime_error("death bookkeeping");
        }
        for(int x=0; x<n; ++x)
            if (bool(seen[x]) != legal(x)) throw std::runtime_error("missing site");
    }
};

int main(int argc, char** argv) {
    if(argc != 9 && argc != 10) {
        std::cerr << "q trajectories seed n infected_boundary batches check output.csv [horizon]\n";
        return 2;
    }
    double q=std::stod(argv[1]);
    int reps=std::stoi(argv[2]), n=std::stoi(argv[4]), batches=std::stoi(argv[6]);
    uint64_t seed=std::stoull(argv[3]);
    bool boundary=std::stoi(argv[5]), audit=std::stoi(argv[7]);
    if(reps%batches || n%2!=1 || !(q>0 && q<1)) return 3;
    const std::vector<double> all_times={0,.1,.25,.5,.75,1,1.5,2,3,4,5,6,8,10,12,16,20,24,32,40,48,64,80,96};
    double horizon=argc==10 ? std::stod(argv[9]) : 24;
    std::vector<double> times;
    for(double t : all_times) if(t<=horizon) times.push_back(t);
    std::mt19937_64 rng(seed);
    auto unif = [&]() { return (double(rng() >> 11)+.5)*0x1.0p-53; };
    Chain c(n,boundary);
    std::ofstream out(argv[8]);
    out << "q,batch,n,time,origin_infected,seed,sites,boundary_infected\n";
    out << std::setprecision(17);
    uint64_t flips=0, edge_hits=0;
    auto started=std::chrono::steady_clock::now();
    for(int b=0; b<batches; ++b) {
        std::vector<uint64_t> sums(times.size());
        for(int rep=0; rep<reps/batches; ++rep) {
            c.start();
            double t=0;
            size_t obs=0;
            bool edge_hit=false;
            while(obs<times.size()) {
                double birth_rate=q*c.births.size(), death_rate=(1-q)*c.deaths.size();
                double rate=birth_rate+death_rate;
                double next=rate>0 ? t-std::log(unif())/rate : INFINITY;
                while(obs<times.size() && times[obs]<next) {
                    sums[obs] += c.infected[n/2]; ++obs;
                }
                if(obs==times.size()) break;
                double u=unif()*rate;
                auto &list = u<birth_rate ? c.births : c.deaths;
                int at=std::min(int(unif()*list.size()),int(list.size())-1);
                int x=list[at];
                c.flip(x); t=next; ++flips;
                if(x==0 || x==n-1) edge_hit=true;
                if(audit) c.check();
            }
            edge_hits+=edge_hit;
        }
        for(size_t j=0; j<times.size(); ++j)
            out << q << ',' << b << ',' << reps/batches << ',' << times[j] << ','
                << sums[j] << ',' << seed << ',' << n << ',' << boundary << '\n';
    }
    std::cerr << "q=" << q << " reps=" << reps << " seed=" << seed
              << " flips=" << flips << " edge_hits=" << edge_hits << " seconds="
              << std::chrono::duration<double>(std::chrono::steady_clock::now()-started).count()
              << '\n';
}
