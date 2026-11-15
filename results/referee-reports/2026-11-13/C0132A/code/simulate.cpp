#include <algorithm>
#include <array>
#include <chrono>
#include <cmath>
#include <cstdint>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <set>
#include <stdexcept>
#include <string>
#include <vector>

// SplitMix64; two independent streams supply the two projection walks.
struct RNG {
    uint64_t state;
    uint64_t next() {
        uint64_t z = (state += 0x9e3779b97f4a7c15ULL);
        z = (z ^ (z >> 30)) * 0xbf58476d1ce4e5b9ULL;
        z = (z ^ (z >> 27)) * 0x94d049bb133111ebULL;
        return z ^ (z >> 31);
    }
};
uint64_t mix(uint64_t z) {
    z = (z ^ (z >> 30)) * 0xbf58476d1ce4e5b9ULL;
    z = (z ^ (z >> 27)) * 0x94d049bb133111ebULL;
    return z ^ (z >> 31);
}
uint64_t pack(const std::array<int,3>& p) {
    constexpr int offset = 1 << 20;
    uint64_t key = 0;
    for (int j=0; j<3; ++j) {
        if (p[j] < -offset || p[j] >= offset)
            throw std::runtime_error("coordinate packing limit reached");
        key |= uint64_t(p[j] + offset) << (21*j);
    }
    return key + 1; // Zero is the empty-table sentinel; occupied keys fit in 64 bits.
}
struct FlatSet {
    std::vector<uint64_t> tab;
    size_t count=0;
    explicit FlatSet(size_t n) : tab(n,0) {}
    bool add(uint64_t key) {
        size_t i=mix(key)&(tab.size()-1);
        while (tab[i] && tab[i]!=key) i=(i+1)&(tab.size()-1);
        if (tab[i]) return false;
        if (count*10 >= tab.size()*7) throw std::runtime_error("table load limit reached");
        tab[i]=key; ++count; return true;
    }
};

// Consumed sites of the origin's vertical column may have several components.
// Only the component containing zero contributes to the probability of hitting zero.
struct Column {
    std::set<int> sites;
    int lo=0, hi=0;
    uint64_t entries=0, successes=0, zero_probability_entries=0;
    long double compensator=0, variance=0;
    bool active=false, hit=false;
    void consume(int y) {
        sites.insert(y);
        while (sites.count(lo-1)) --lo;
        while (sites.count(hi+1)) ++hi;
    }
    long double probability(int y) const {
        if (y==0) return 1;
        if (y<lo || y>hi) return 0;
        if (y>0) return (long double)(hi+1-y)/(hi+1);
        return (long double)(y-lo+1)/(1-lo);
    }
    void enter(int y) {
        if (active) throw std::runtime_error("overlapping column episodes");
        long double q=probability(y);
        ++entries; compensator+=q; variance+=q*(1-q);
        zero_probability_entries += q==0;
        active=true; hit=y==0;
    }
    void leave() {
        if (active) successes+=hit;
        active=false; hit=false;
    }
};

int main(int argc,char** argv) {
    if (argc<6) {
        std::cerr<<"usage: simulate d1 steps seeds first_seed output.csv [trace.txt]\n"; return 2;
    }
    int d1=std::stoi(argv[1]);
    uint64_t steps=std::stoull(argv[2]), seeds=std::stoull(argv[3]), first_seed=std::stoull(argv[4]);
    if ((d1!=1 && d1!=2) || steps>10000000 || !steps) return 2;
    std::ofstream out(argv[5]), trace;
    if (!out) throw std::runtime_error("cannot open output");
    if (argc>6) trace.open(argv[6]);
    out<<"d1,d2,seed,n,range,first_departures,revisit_departures,origin_returns,last_origin,window_visits,window_hit,endpoint_origin,first_norm2,revisit_norm2,column_entries,column_zero_q,column_q_sum,column_q_variance,column_successes,column_pending_hit,column_lo,column_hi,column_sites\n";
    std::vector<uint64_t> checkpoints;
    for (uint64_t n=1000; n<=steps; n*=10) checkpoints.push_back(n);
    if (checkpoints.empty() || checkpoints.back()!=steps) checkpoints.push_back(steps);
    std::vector<uint64_t> events=checkpoints;
    for (auto n:checkpoints) events.push_back(n/2);
    std::sort(events.begin(),events.end());
    events.erase(std::unique(events.begin(),events.end()),events.end());
    size_t capacity=16;
    while (capacity < (steps+1)*10/7+2) capacity*=2;
    auto start=std::chrono::steady_clock::now();
    for (uint64_t seed=first_seed; seed<first_seed+seeds; ++seed) {
        FlatSet visited(capacity);
        RNG ra{mix(seed ^ 0x243f6a8885a308d3ULL)}, rb{mix(seed ^ 0x13198a2e03707344ULL)};
        std::array<int,3> p{0,0,0};
        uint64_t first=0, returns=0, last=0;
        size_t event=0;
        std::vector<uint64_t> half_returns(checkpoints.size(),0);
        Column col;
        bool fresh=visited.add(pack(p));
        for (uint64_t t=0; t<steps; ++t) {
            bool base_zero=true;
            for (int j=0;j<d1;++j) base_zero &= p[j]==0;
            uint64_t bits=(fresh?ra:rb).next();
            int axis=fresh ? (d1==1 ? 0 : int((bits>>1)&1)) : d1;
            int sign=(bits&1) ? 1 : -1;
            if (trace) trace<<seed<<' '<<t<<' '<<p[0]<<' '<<p[1]<<' '<<p[2]<<' '<<fresh<<' '<<axis<<' '<<sign<<'\n';
            if (fresh) {
                ++first;
                if (base_zero) { col.consume(p[d1]); col.leave(); }
            }
            p[axis]+=sign;
            bool new_base_zero=true, origin=true;
            for (int j=0;j<d1;++j) new_base_zero &= p[j]==0;
            for (int j=0;j<3;++j) origin &= p[j]==0;
            if (fresh && new_base_zero) col.enter(p[d1]);
            if (col.active && new_base_zero && p[d1]==0) col.hit=true;
            if (origin) {++returns; last=t+1;}
            fresh=visited.add(pack(p));
            uint64_t n=t+1;
            if (n!=events[event]) continue;
            for (size_t i=0;i<checkpoints.size();++i) if (n==checkpoints[i]/2) half_returns[i]=returns;
            auto it=std::find(checkpoints.begin(),checkpoints.end(),n);
            if (it!=checkpoints.end()) {
                size_t i=it-checkpoints.begin();
                uint64_t a2=0;
                for (int j=0;j<d1;++j) a2+=int64_t(p[j])*p[j];
                uint64_t b2=int64_t(p[d1])*p[d1];
                if (visited.count!=first+fresh) throw std::runtime_error("clock/range identity failed");
                out<<d1<<",1,"<<seed<<','<<n<<','<<visited.count<<','<<first<<','<<n-first<<','<<returns<<','<<last<<','<<returns-half_returns[i]<<','<<(last>n/2)<<','<<origin<<','<<a2<<','<<b2<<','<<col.entries<<','<<col.zero_probability_entries<<','<<std::setprecision(17)<<col.compensator<<','<<col.variance<<','<<col.successes<<','<<(col.active&&col.hit)<<','<<col.lo<<','<<col.hi<<','<<col.sites.size()<<'\n';
            }
            if (++event==events.size()) break;
        }
        out.flush();
        if ((seed-first_seed+1)%8==0 || seed+1==first_seed+seeds) {
            double elapsed=std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count();
            std::cerr<<"M("<<d1<<",1) seeds "<<seed-first_seed+1<<'/'<<seeds<<", elapsed "<<elapsed<<" s, table "<<capacity*8/(1024*1024)<<" MiB\n";
        }
    }
}
