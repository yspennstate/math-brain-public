// Continuous-time FA-1f on a finite interval, with frozen zeros outside.
// Spin 0 is infected. Only currently legal rate-one proposal clocks are sampled.
#include <algorithm>
#include <array>
#include <cmath>
#include <cstdint>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <stdexcept>
#include <string>
#include <vector>
#include <sys/resource.h>

struct RNG {
    std::array<uint64_t,4> s;
    static uint64_t mix(uint64_t &x) {
        uint64_t z=(x+=0x9e3779b97f4a7c15ULL);
        z=(z^(z>>30))*0xbf58476d1ce4e5b9ULL;
        z=(z^(z>>27))*0x94d049bb133111ebULL;
        return z^(z>>31);
    }
    explicit RNG(uint64_t seed) { for(auto &v:s) v=mix(seed); }
    static uint64_t rotl(uint64_t x,int k) { return (x<<k)|(x>>(64-k)); }
    uint64_t next() {
        uint64_t result=rotl(s[1]*5,7)*9, t=s[1]<<17;
        s[2]^=s[0];s[3]^=s[1];s[1]^=s[2];s[0]^=s[3];s[2]^=t;s[3]=rotl(s[3],45);
        return result;
    }
    double uniform() { return (next()>>11)*0x1.0p-53; }
    double exponential(double rate) {
        double u; do {u=uniform();} while(u==0);
        return -std::log(u)/rate;
    }
    // Exact uniform integer via rejection; no modulo bias.
    int integer(int n) {
        uint64_t m=uint64_t(n), threshold=(-m)%m, v;
        do { v=next(); } while(v<threshold);
        return int(v%m);
    }
};

struct Chain {
    int n;
    std::vector<unsigned char> eta;
    std::vector<int> active, pos;
    RNG &rng;
    Chain(int length,RNG &r):n(length),eta(n+2,0),pos(n+2,-1),rng(r){}
    bool legal(int x) const { return eta[x-1]==0 || eta[x+1]==0; }
    void refresh(int x) {
        if(x<1||x>n) return;
        if(legal(x) && pos[x]<0) {pos[x]=int(active.size());active.push_back(x);}
        else if(!legal(x) && pos[x]>=0) {
            int p=pos[x], last=active.back();active[p]=last;pos[last]=p;active.pop_back();pos[x]=-1;
        }
    }
    void initialize(const std::string &law,double q) {
        // Both non-equilibrium laws have stationary infection density 0.2.
        if(law=="renewal") {
            // Gap between infections = 1+Geom(1/4), so consecutive zeros are forbidden.
            bool infected=rng.uniform()<0.2;
            for(int x=1;x<=n;x++) {
                eta[x]=infected?0:1;
                infected=infected?false:rng.uniform()<0.25;
            }
        } else if(law=="hmm") {
            // Stationary symmetric latent Markov chain, switch probability 0.03.
            bool latent=rng.uniform()<0.5;
            for(int x=1;x<=n;x++) {
                eta[x]=rng.uniform()<(latent?0.38:0.02)?0:1;
                if(rng.uniform()<0.03) latent=!latent;
            }
        } else if(law=="equilibrium") {
            for(int x=1;x<=n;x++) eta[x]=rng.uniform()<q?0:1;
        } else if(law=="single") {
            std::fill(eta.begin()+1,eta.end()-1,1);eta[n/2]=0;
        } else throw std::runtime_error("unknown law");
        active.clear();std::fill(pos.begin(),pos.end(),-1);
        for(int x=1;x<=n;x++) refresh(x);
    }
    void audit() const {
        int count=0;
        for(int x=1;x<=n;x++) {
            if(legal(x)!=(pos[x]>=0)) throw std::runtime_error("active membership");
            if(pos[x]>=0) {
                if(active[pos[x]]!=x) throw std::runtime_error("active inverse");
                count++;
            }
        }
        if(count!=int(active.size())) throw std::runtime_error("active size");
    }
    void update(double q) {
        int x=active[rng.integer(int(active.size()))];
        unsigned char spin=rng.uniform()<q?0:1;
        if(eta[x]!=spin) {eta[x]=spin;refresh(x-1);refresh(x+1);}
    }
    void observe(std::ostream &out,int rep,double t,int width) const {
        int left=(n-width)/2+1, right=left+width-1, empty=0,pair=0;
        for(int x=left;x<=right;x++) empty+=eta[x]==0;
        for(int x=left;x<right;x++) pair+=(eta[x]==0 && eta[x+1]==0);
        int mid=n/2;
        out<<rep<<','<<t<<','<<double(empty)/width<<','<<double(pair)/(width-1)<<','
           <<int(eta[mid]==0)<<','<<int(eta[mid]==0&&eta[mid+1]==0)<<'\n';
    }
};
int main(int argc,char**argv) {
    if(argc<7) {std::cerr<<"simulate LAW Q N REPS SEED OUT [WIDTH] [audit|long]\n";return 2;}
    std::string law=argv[1];double q=std::stod(argv[2]);int n=std::stoi(argv[3]), reps=std::stoi(argv[4]);
    uint64_t seed=std::stoull(argv[5]);int width=argc>7?std::stoi(argv[7]):256;
    bool audit=argc>8&&std::string(argv[8])=="audit";
    if(q<=0||q>=1||n<width||width<2||reps<2) return 2;
    int priority=getpriority(PRIO_PROCESS,0);
    if(priority<10 && setpriority(PRIO_PROCESS,0,10)!=0) throw std::runtime_error("cannot set nice>=10");
    std::vector<double> times={0,0.25,0.5,0.75,1,1.5,2,2.5,3,4,5,6,7,8,10,12,15,18,21,24,28,32,36,40,45,50,55,60};
    if(argc>8&&std::string(argv[8])=="long") {
        for(double extra: {75.,100.,125.,150.,200.,250.,300.,400.,500.,600.}) times.push_back(extra);
    }
    std::ofstream out(argv[6]);out<<std::setprecision(12)<<"rep,time,density,pair,origin,origin_pair\n";
    if(!out) return 2;
    for(int rep=0;rep<reps;rep++) {
        RNG rng(seed+0x9e3779b97f4a7c15ULL*uint64_t(rep));Chain chain(n,rng);chain.initialize(law,q);
        size_t k=0;double t=0;
        chain.observe(out,rep,times[k++],width);
        while(k<times.size()) {
            if(chain.active.empty()) throw std::runtime_error("no legal sites with infected exterior");
            double next=t+rng.exponential(chain.active.size());
            while(k<times.size()&&times[k]<=next) {chain.observe(out,rep,times[k++],width);}
            if(k==times.size()) break;
            t=next;chain.update(q);
            if(audit) chain.audit();
        }
        if(rep%100==99) {out.flush();std::cerr<<law<<" q="<<q<<" "<<rep+1<<"/"<<reps<<'\n';}
    }
    std::cerr<<"priority "<<getpriority(PRIO_PROCESS,0)<<'\n';
}
