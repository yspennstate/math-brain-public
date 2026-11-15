// Exact finite-window SAW counts. Single thread, deterministic sampling.
#include <array>
#include <chrono>
#include <cmath>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <queue>
#include <random>
#include <stdexcept>
#include <string>
#include <sys/resource.h>
#include <vector>

using Clock = std::chrono::steady_clock;
constexpr int R = 128, L = 2*R+1, V = L*L;
std::vector<std::array<int,4>> nbr(V);
std::vector<unsigned char> deg(V), seen(V);
std::array<std::uint64_t,40> counts{};
int nmax;

void dfs(int v, int depth) {
    ++counts[depth];
    if (depth == nmax) return;
    seen[v]=1;
    for(int j=0;j<deg[v];++j) {
        const int w=nbr[v][j];
        if(!seen[w]) dfs(w,depth+1);
    }
    seen[v]=0;
}

int id(int x,int y) { return (y+R)*L+x+R; }
void add(int a,int b) { nbr[a][deg[a]++]=b; nbr[b][deg[b]++]=a; }

int main(int argc,char**argv) {
    try {
        if(getpriority(PRIO_PROCESS,0)<10) throw std::runtime_error("Requires inherited nice >= 10");
        if(argc!=2) throw std::runtime_error("Usage: enumerate DATA_DIRECTORY");
        const std::string out=argv[1];
        std::ofstream csv(out+"/counts.csv");
        std::ofstream meta(out+"/samples.csv");
        csv<<"p,sample,seed,root,x,y,n,count,nth_root,log_count_per_n\n";
        meta<<"p,sample,seed,attempts,component_vertices,root,x,y,nmax,seconds,nice\n";
        for(int pi=0;pi<3;++pi) {
            const double p=std::array<double,3>{0.6,0.75,0.9}[pi];
            nmax=std::array<int,3>{28,24,21}[pi];
            for(int sample=0;sample<3;++sample) {
                std::uint64_t seed=680000ULL+10000*pi+100*sample;
                int attempts=0,component_size=0;
                std::vector<unsigned char> component(V);
                std::string bits;
                while(true) {
                    ++attempts;
                    std::fill(deg.begin(),deg.end(),0);
                    std::fill(component.begin(),component.end(),0);
                    bits.clear(); bits.reserve(2*V);
                    std::mt19937_64 rng(seed);
                    auto open=[&]() { return (rng()>>11)*0x1.0p-53 < p; };
                    for(int y=-R;y<=R;++y) for(int x=-R;x<=R;++x) {
                        bool h=false,u=false;
                        if(x<R) { h=open(); if(h)add(id(x,y),id(x+1,y)); }
                        if(y<R) { u=open(); if(u)add(id(x,y),id(x,y+1)); }
                        bits.push_back(h?'1':'0'); bits.push_back(u?'1':'0');
                    }
                    std::queue<int> q; q.push(id(0,0));component[id(0,0)]=1;
                    int faces=0;component_size=0;
                    while(!q.empty()) {
                        int a=q.front();q.pop();++component_size;
                        int x=a%L-R,y=a/L-R;
                        if(x==-R)faces|=1;if(x==R)faces|=2;
                        if(y==-R)faces|=4;if(y==R)faces|=8;
                        for(int j=0;j<deg[a];++j)if(!component[nbr[a][j]]){
                            component[nbr[a][j]]=1;q.push(nbr[a][j]);
                        }
                    }
                    if(faces==15)break;
                    if(attempts>=100)throw std::runtime_error("Proxy sample rejection limit");
                    ++seed;
                }
                const std::string tag="p"+std::to_string(int(std::round(100*p)))+"_s"+std::to_string(sample);
                std::ofstream edges(out+"/"+tag+"_edges.txt");
                edges<<"# radius p seed; bits: row-major sites, right/up at each site\n";
                edges<<R<<' '<<p<<' '<<seed<<'\n';
                for(int y=0;y<L;++y)edges<<bits.substr(2*y*L,2*L)<<'\n';
                edges.close();
                std::array<std::array<int,2>,3> targets{{{0,0},{8,0},{0,8}}};
                std::vector<int> used;
                for(int root=0;root<3;++root) {
                    int best=-1,bestdist=100000;
                    for(int y=-16;y<=16;++y)for(int x=-16;x<=16;++x) {
                        int a=id(x,y);
                        if(!component[a])continue;
                        bool duplicate=false;for(int b:used)if(a==b)duplicate=true;
                        if(duplicate)continue;
                        int d=std::abs(x-targets[root][0])+std::abs(y-targets[root][1]);
                        if(d<bestdist) { bestdist=d;best=a; }
                    }
                    if(best<0)throw std::runtime_error("No root near target");
                    used.push_back(best);
                    const int x=best%L-R,y=best/L-R;
                    if(R-std::max(std::abs(x),std::abs(y))<=nmax)throw std::runtime_error("Boundary too close");
                    counts.fill(0);std::fill(seen.begin(),seen.end(),0);
                    const auto start=Clock::now(); dfs(best,0);
                    const double secs=std::chrono::duration<double>(Clock::now()-start).count();
                    csv.precision(17);meta.precision(10);
                    for(int n=0;n<=nmax;++n) {
                        const double rate=n?std::log(double(counts[n]))/n:0;
                        csv<<p<<','<<sample<<','<<seed<<','<<root<<','<<x<<','<<y<<','<<n<<','<<counts[n]<<',';
                        if(n)csv<<std::exp(rate)<<','<<rate;
                        else csv<<"1,0";
                        csv<<'\n';
                    }
                    csv.flush();
                    meta<<p<<','<<sample<<','<<seed<<','<<attempts<<','<<component_size<<','<<root<<','<<x<<','<<y<<','<<nmax<<','<<secs<<','<<getpriority(PRIO_PROCESS,0)<<'\n';
                    meta.flush();
                    std::cout<<tag<<" root "<<root<<" ("<<x<<','<<y<<") n="<<nmax<<" count="<<counts[nmax]<<" seconds="<<secs<<std::endl;
                }
            }
        }
        rusage usage{}; getrusage(RUSAGE_SELF,&usage);
        std::cout<<"peak_rss_bytes="<<usage.ru_maxrss<<std::endl;
    } catch(const std::exception&e) { std::cerr<<e.what()<<std::endl;return 1; }
}
