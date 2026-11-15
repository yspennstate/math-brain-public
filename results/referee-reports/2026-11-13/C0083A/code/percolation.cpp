#include <algorithm>
#include <chrono>
#include <cmath>
#include <cstdint>
#include <cstdlib>
#include <iomanip>
#include <iostream>
#include <numeric>
#include <random>
#include <stdexcept>
#include <vector>
#include <sys/resource.h>

// One CPU thread. Root exploration reveals each relevant edge only while its
// other endpoint is undiscovered. Geometric skips sample Bernoulli edge states.
struct Sampler {
    int n, d;
    uint64_t V = 1;
    std::vector<uint64_t> stride;
    std::vector<uint32_t> seen, queue;
    uint32_t stamp = 0;
    std::mt19937_64 rng;
    Sampler(int n_, int d_, uint64_t seed) : n(n_), d(d_), rng(seed) {
        if (n < 2 || d < 1) throw std::runtime_error("invalid graph");
        for (int j = 0; j < d; ++j) {
            stride.push_back(V);
            V *= n;
            if (V > (1ULL << 24)) throw std::runtime_error("V exceeds memory cap");
        }
        seen.resize(V, 0);
        queue.reserve(4096);
    }
    double uniform() { return ((rng() >> 11) + 0.5) * 0x1.0p-53; }
    uint64_t cluster(double p) {
        if (p == 0) return 1;
        if (p == 1) return V;
        if (!(p > 0 && p < 1)) throw std::runtime_error("invalid p");
        if (++stamp == 0) { std::fill(seen.begin(), seen.end(), 0); stamp = 1; }
        queue.clear(); queue.push_back(0); seen[0] = stamp;
        const double logq = std::log1p(-p);
        auto skip = [&]() { return std::floor(std::log(uniform()) / logq); };
        for (size_t head = 0; head < queue.size(); ++head) {
            uint64_t u = queue[head];
            for (int j = 0; j < d; ++j) {
                int digit = (u / stride[j]) % n;
                uint64_t base = u - digit * stride[j];
                double k = skip();
                while (k < n - 1) {
                    int value = static_cast<int>(k);
                    if (value >= digit) ++value;
                    uint32_t v = base + value * stride[j];
                    if (seen[v] != stamp) { seen[v] = stamp; queue.push_back(v); }
                    k += 1 + skip();
                }
            }
        }
        return queue.size();
    }
    void sample(double p, uint64_t count) {
        long double sum = 0, sq = 0;
        uint64_t largest = 0;
        for (uint64_t i = 0; i < count; ++i) {
            uint64_t x = cluster(p); sum += x; sq += (long double)x*x;
            largest = std::max(largest, x);
        }
        long double mean = sum/count;
        long double variance = (sq - sum*sum/count)/(count-1);
        std::cout << "{\"mean\":" << mean << ",\"se\":" << std::sqrt(variance/count)
                  << ",\"samples\":" << count << ",\"max_cluster\":" << largest << "}";
    }
};

struct DSU {
    std::vector<int> parent, size;
    DSU(int v) : parent(v), size(v,1) { std::iota(parent.begin(),parent.end(),0); }
    int root(int x) { while (x != parent[x]) { parent[x] = parent[parent[x]]; x=parent[x]; } return x; }
    void join(int a,int b) { a=root(a);b=root(b); if(a==b)return;
        if(size[a]<size[b])std::swap(a,b); parent[b]=a;size[a]+=size[b]; }
};

void exact(int n, int d) {
    Sampler graph(n,d,1);
    std::vector<std::pair<int,int>> edges;
    for (int u=0;u<(int)graph.V;++u) for(int j=0;j<d;++j) {
        int digit=(u/graph.stride[j])%n;
        for(int a=digit+1;a<n;++a) edges.emplace_back(u,u+(a-digit)*graph.stride[j]);
    }
    int E=edges.size();
    if(E>22)throw std::runtime_error("exact enumeration capped at 22 edges");
    std::vector<uint64_t> count(E+1), root_sum(E+1), square_sum(E+1);
    for(uint64_t mask=0;mask<(1ULL<<E);++mask) {
        DSU uf(graph.V);
        for(int k=0;k<E;++k)if(mask&(1ULL<<k))uf.join(edges[k].first,edges[k].second);
        int k=__builtin_popcountll(mask);++count[k];root_sum[k]+=uf.size[uf.root(0)];
        for(int v=0;v<(int)graph.V;++v)if(uf.root(v)==v)square_sum[k]+=uint64_t(uf.size[v])*uf.size[v];
    }
    for(int k=0;k<=E;++k)if(root_sum[k]*graph.V!=square_sum[k])
        throw std::runtime_error("transitivity audit failed");
    auto array=[](const std::vector<uint64_t>&v){std::cout<<'[';for(size_t i=0;i<v.size();++i){if(i)std::cout<<',';std::cout<<v[i];}std::cout<<']';};
    std::cout<<"{\"n\":"<<n<<",\"d\":"<<d<<",\"V\":"<<graph.V<<",\"E\":"<<E<<",\"count\":";
    array(count);std::cout<<",\"root_sum\":";array(root_sum);std::cout<<",\"square_sum\":";array(square_sum);std::cout<<'}';
}

int main(int argc,char**argv) {
    try {
        if (getpriority(PRIO_PROCESS, 0) < 10) {
            if(setpriority(PRIO_PROCESS,0,10))throw std::runtime_error("cannot set nice >=10");
        }
        // Explicit storage caps in Sampler and exact() keep the allocation below
        // 150 MiB for all accepted inputs; no worker threads are created.
        std::cout<<std::setprecision(17);
        if(argc<4)throw std::runtime_error("usage: exact n d | sample n d seed p count [...]");
        int n=std::stoi(argv[2]),d=std::stoi(argv[3]);
        if(std::string(argv[1])=="exact")exact(n,d);
        else {
            if(argc<7 || (argc-5)%2)throw std::runtime_error("sample needs seed and p/count pairs");
            Sampler s(n,d,std::stoull(argv[4])); std::cout<<'[';
            for(int i=5;i<argc;i+=2) { if(i>5)std::cout<<','; s.sample(std::stod(argv[i]),std::stoull(argv[i+1])); }
            std::cout<<']';
        }
        std::cout<<'\n';
    } catch(const std::exception&e) { std::cerr<<e.what()<<'\n';return 1; }
}
