#include <algorithm>
#include <array>
#include <cassert>
#include <chrono>
#include <cmath>
#include <cstdint>
#include <deque>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <numeric>
#include <random>
#include <stdexcept>
#include <string>
#include <sys/resource.h>
#include <vector>

// A negative site state is one sleeping particle; otherwise the active count.
// Every instruction, including an ineffective sleep at a multiply occupied site,
// increments the odometer. No sink and no resetting of stacks are used.
struct Result {
    std::vector<int> state;
    std::vector<uint64_t> odo;
    uint64_t total=0, jumps=0, sleeps=0, failed=0, mass=0;
    bool finished=true;
};

struct Tape {
    std::mt19937_64 rng;
    double p;
    bool retain;
    std::vector<std::vector<unsigned char>> stack;
    Tape(uint64_t seed, double lambda, size_t n, bool save=false)
        : rng(seed), p(lambda/(1+lambda)), retain(save), stack(save?n:0) {}
    unsigned char sample() {
        double u=std::generate_canonical<double,53>(rng);
        if(u<p) return 0;
        return u < p+(1-p)/2 ? 1 : 2; // sleep, left, right
    }
    unsigned char at(size_t x,uint64_t i) {
        if(!retain) return sample();
        auto &s=stack[x];
        if(i==s.size()) s.push_back(sample());
        if(i>=s.size()) throw std::runtime_error("stack index skipped");
        return s[i];
    }
};

Result stabilize(const std::vector<int>& initial,Tape& tape,
                 uint64_t cap,int policy=0) {
    size_t n=initial.size();
    Result r;
    r.state=initial;
    r.odo.assign(n,0);
    std::deque<size_t> work;
    std::vector<unsigned char> queued(n,0);
    auto add=[&](size_t x) {
        if(r.state[x]>0&&!queued[x]) {queued[x]=1;work.push_back(x);}
    };
    for(size_t x=0;x<n;++x) {
        r.mass+=initial[x]<0 ? 1:initial[x];
        add(x);
    }
    if(r.mass>n) {r.finished=false;return r;}
    std::mt19937_64 scheduler(728103);
    while(!work.empty()) {
        if(r.total>=cap) {r.finished=false;break;}
        size_t x;
        if(policy==0) {x=work.back();work.pop_back();}
        else if(policy==1) {x=work.front();work.pop_front();}
        else {
            size_t j=scheduler()%work.size();
            std::swap(work[j],work.back());x=work.back();work.pop_back();
        }
        queued[x]=0;
        assert(r.state[x]>0);
        auto ins=tape.at(x,r.odo[x]);
        ++r.odo[x];++r.total;
        if(ins==0) {
            if(r.state[x]==1) {r.state[x]=-1;++r.sleeps;}
            else ++r.failed;
        } else {
            --r.state[x];++r.jumps;
            size_t y=ins==1 ? (x+n-1)%n:(x+1)%n;
            r.state[y]=r.state[y]<0 ? 2:r.state[y]+1;
            add(y);
        }
        add(x);
    }
    uint64_t final_mass=0;
    for(auto v:r.state) {
        final_mass+=v<0 ? 1:v;
        if(r.finished) assert(v<=0);
    }
    assert(final_mass==r.mass);
    assert(std::accumulate(r.odo.begin(),r.odo.end(),uint64_t(0))==r.total);
    assert(r.jumps+r.sleeps+r.failed==r.total);
    return r;
}

uint64_t seed_for(uint64_t x) {
    x+=0x9e3779b97f4a7c15ULL;
    x=(x^(x>>30))*0xbf58476d1ce4e5b9ULL;
    x=(x^(x>>27))*0x94d049bb133111ebULL;
    return x^(x>>31);
}

void verify() {
    std::mt19937_64 rng(8390003);
    size_t cases=0;
    for(int n:{7,19,53}) for(double lambda:{0.2,1.0,4.0,10.0}) {
        for(int k=0;k<30;++k) {
            std::vector<int> initial(n,0);
            int particles=1+k%(n/2+1);
            for(int j=0;j<particles;++j) ++initial[rng()%n];
            Tape t(rng(),lambda,n,true);
            auto a=stabilize(initial,t,10000000,0);
            auto b=stabilize(initial,t,10000000,1);
            auto c=stabilize(initial,t,10000000,2);
            if(!a.finished||!b.finished||!c.finished||a.state!=b.state||a.state!=c.state||
               a.odo!=b.odo||a.odo!=c.odo) throw std::runtime_error("abelian replay failed");
            ++cases;
        }
    }
    std::cout<<"Abelian replay: "<<cases<<" initial configurations, three legal orders: PASS\n";
    // Exact one-particle law: number of instructions is geometric(p) on {1,2,...}.
    for(double lambda:{0.1,1.0,4.0}) {
        constexpr int reps=100000;
        double sum=0;
        for(int j=0;j<reps;++j) {
            std::vector<int> v(31,0);v[0]=1;
            Tape t(seed_for(1000000+j),lambda,v.size());
            auto r=stabilize(v,t,1000000);
            if(!r.finished||r.sleeps!=1||r.failed!=0) throw std::runtime_error("one-particle invariant");
            sum+=r.total;
        }
        double mean=(1+lambda)/lambda;
        double se=std::sqrt((1+lambda)/(lambda*lambda)/reps);
        double z=(sum/reps-mean)/se;
        if(std::abs(z)>6) throw std::runtime_error("geometric mean check");
        std::cout<<"Single particle lambda="<<lambda<<" measured_mean="<<sum/reps
                 <<" exact_mean="<<mean<<" z="<<z<<": PASS\n";
    }
}

int main(int argc,char** argv) {
    try {
        if(argc<2) throw std::runtime_error("use --verify or --simulate OUTPUT.csv [REPS_SCALE]");
        std::cout<<"priority="<<getpriority(PRIO_PROCESS,0)<<" threads=1\n";
        if(getpriority(PRIO_PROCESS,0)<10) throw std::runtime_error("priority must be at least nice 10");
        if(std::string(argv[1])=="--verify") {verify();return 0;}
        if(std::string(argv[1])!="--simulate"||argc<3) throw std::runtime_error("bad arguments");
        std::ofstream out(argv[2]);
        if(!out) throw std::runtime_error("cannot open results");
        out<<"n,density,lambda,rep,seed,initial_mass,T,T_over_n,jumps,sleep_success,sleep_failure,max_odometer,finished,seconds";
        std::vector<int> thresholds={1,2,5,10,20,50,100,200,500,1000};
        for(auto k:thresholds) out<<",sites_ge_"<<k;
        out<<"\n"<<std::setprecision(12);
        std::vector<std::pair<double,double>> params={{0.02,0.1},{0.08,0.1},
            {0.1,1.0},{0.4,1.0},{0.2,4.0},{0.75,4.0},{0.8,10.0}};
        double scale=argc>3 ? std::stod(argv[3]):1;
        for(size_t ip=0;ip<params.size();++ip) {
            auto [density,lambda]=params[ip];
            if(density>=lambda/(1+lambda)) throw std::runtime_error("not in explicit fast regime");
            for(int n:{1000,3000,10000,30000,100000}) {
                int reps=std::max(1,int((n<=10000?200:n==30000?100:60)*scale));
                double mean=0;
                for(int rep=0;rep<reps;++rep) {
                    uint64_t seed=seed_for(930000000ULL+ip*10000000ULL+n*100ULL+rep);
                    std::mt19937_64 initial_rng(seed);
                    std::poisson_distribution<int> pois(density);
                    std::vector<int> initial(n);
                    for(auto &v:initial) v=pois(initial_rng);
                    Tape tape(seed_for(seed),lambda,n);
                    auto start=std::chrono::steady_clock::now();
                    auto r=stabilize(initial,tape,uint64_t(n)*10000);
                    double seconds=std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count();
                    out<<n<<','<<density<<','<<lambda<<','<<rep<<','<<seed<<','<<r.mass<<','
                       <<r.total<<','<<double(r.total)/n<<','<<r.jumps<<','<<r.sleeps<<','<<r.failed
                       <<','<<*std::max_element(r.odo.begin(),r.odo.end())<<','<<r.finished<<','<<seconds;
                    for(auto k:thresholds) out<<','<<std::count_if(r.odo.begin(),r.odo.end(),[&](auto v){return v>=uint64_t(k);});
                    out<<'\n';
                    mean+=double(r.total)/n;
                }
                out.flush();
                std::cout<<"density="<<density<<" lambda="<<lambda<<" n="<<n
                         <<" repetitions="<<reps<<" mean_T/n="<<mean/reps<<std::endl;
            }
        }
        struct rusage usage;
        getrusage(RUSAGE_SELF,&usage);
        std::cout<<"peak_rss_bytes_on_macOS="<<usage.ru_maxrss<<"\n";
    } catch(const std::exception& e) {std::cerr<<e.what()<<'\n';return 1;}
}
