// Finite FK tori: exact enumeration and random-scan single-edge heat bath.
// Build: c++ -O3 -std=c++17 code/fk.cpp -o code/fk
#include <algorithm>
#include <array>
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
using Vec = std::array<int,3>;
struct Edge { int u,v,axis; };
struct Graph {
    int d,L,n; std::vector<Edge> edges;
    std::vector<std::vector<std::pair<int,int>>> adj;
    Graph(int dim,int side):d(dim),L(side),n(1) {
        if(d<2 || d>3 || L<2) throw std::runtime_error("bad torus");
        for(int a=0;a<d;a++) n*=L;
        adj.resize(n);
        for(int u=0;u<n;u++) {
            int stride=1;
            for(int a=0;a<d;a++,stride*=L) {
                int x=(u/stride)%L;
                int v=u+(x==L-1 ? -(L-1)*stride : stride);
                int e=edges.size(); edges.push_back({u,v,a});
                adj[u].push_back({v,e}); adj[v].push_back({u,e});
            }
        }
    }
};
struct DSU {
    std::vector<int> parent,size,wrap; std::vector<Vec> delta;
    DSU(int n):parent(n),size(n),wrap(n),delta(n) { reset(); }
    void reset() {
        std::iota(parent.begin(),parent.end(),0);
        std::fill(size.begin(),size.end(),1); std::fill(wrap.begin(),wrap.end(),0);
        std::fill(delta.begin(),delta.end(),Vec{0,0,0});
    }
    int find(int x) {
        if(parent[x]==x) return x;
        int p=parent[x], r=find(p);
        for(int a=0;a<3;a++) delta[x][a]+=delta[p][a];
        return parent[x]=r;
    }
    void join(Edge e) {
        int ru=find(e.u),rv=find(e.v); Vec w;
        for(int a=0;a<3;a++) w[a]=delta[e.u][a]-delta[e.v][a]+(a==e.axis);
        if(ru==rv) {
            for(int a=0;a<3;a++) if(w[a]!=0) wrap[ru]|=(1<<a);
        } else if(size[ru]>=size[rv]) {
            parent[rv]=ru; delta[rv]=w; size[ru]+=size[rv]; wrap[ru]|=wrap[rv];
        } else {
            parent[ru]=rv;
            for(int a=0;a<3;a++) delta[ru][a]=-w[a];
            size[rv]+=size[ru]; wrap[rv]|=wrap[ru];
        }
    }
};
struct Obs { uint64_t k=0,s2=0,excl=0,nonwrap=0,wrapping=0,maxsize=0; };
Obs observe(const Graph& g,const std::vector<uint8_t>& open,DSU& uf) {
    uf.reset();
    for(size_t e=0;e<open.size();e++) if(open[e]) uf.join(g.edges[e]);
    Obs o;
    for(int x=0;x<g.n;x++) if(uf.parent[x]==x) {
        uint64_t s=uf.size[x]; o.k++; o.s2+=s*s;
        o.maxsize=std::max(o.maxsize,s);
        if(uf.wrap[x]) o.wrapping=1; else o.nonwrap+=s*s;
    }
    o.excl=o.s2-o.maxsize*o.maxsize; return o;
}
void enumerate(int d,int L,const std::string& path) {
    Graph g(d,L); const int m=g.edges.size();
    if(m>24) throw std::runtime_error("enumeration capped at 24 edges");
    struct Bin { uint64_t count=0,s2=0,excl=0,nonwrap=0,wrapping=0,maxsize=0; };
    std::vector<Bin> hist((m+1)*(g.n+1));
    std::vector<uint8_t> open(m); DSU uf(g.n);
    for(uint64_t mask=0;mask<(1ULL<<m);mask++) {
        for(int e=0;e<m;e++) open[e]=(mask>>e)&1;
        Obs o=observe(g,open,uf);
        auto &b=hist[__builtin_popcountll(mask)*(g.n+1)+o.k];
        b.count++; b.s2+=o.s2; b.excl+=o.excl; b.nonwrap+=o.nonwrap;
        b.wrapping+=o.wrapping; b.maxsize+=o.maxsize;
    }
    std::ofstream out(path);
    out<<"d,L,edges,open,k,count,sum_s2,sum_excl,sum_nonwrap,wrap_count,sum_max\n";
    for(int a=0;a<=m;a++) for(int k=1;k<=g.n;k++) {
        auto b=hist[a*(g.n+1)+k]; if(!b.count) continue;
        out<<d<<','<<L<<','<<m<<','<<a<<','<<k<<','<<b.count<<','<<b.s2<<','
           <<b.excl<<','<<b.nonwrap<<','<<b.wrapping<<','<<b.maxsize<<'\n';
    }
    std::cerr<<"enumerated d="<<d<<" L="<<L<<" states="<<(1ULL<<m)<<'\n';
}
struct HeatBath {
    const Graph& g; std::vector<uint8_t> open; std::vector<uint32_t> seen;
    std::vector<int> queue; uint32_t stamp=0;
    std::mt19937_64 rng; std::uniform_real_distribution<double> unif{0.,1.};
    std::uniform_int_distribution<int> edgepick;
    double p,a;
    HeatBath(const Graph& graph,double prob,double q,uint64_t seed,bool full):
        g(graph),open(g.edges.size(),full),seen(g.n),queue(g.n),rng(seed),
        edgepick(0,int(g.edges.size())-1),p(prob),a(p/(p+q*(1-p))) {}
    bool connected(int start,int target) {
        if(++stamp==0) {std::fill(seen.begin(),seen.end(),0);stamp=1;}
        int head=0,tail=0;queue[tail++]=start;seen[start]=stamp;
        while(head<tail) {
            int x=queue[head++];
            for(auto [y,e]:g.adj[x]) if(open[e] && seen[y]!=stamp) {
                if(y==target) return true;
                seen[y]=stamp;queue[tail++]=y;
            }
        }
        return false;
    }
    void sweep() {
        for(size_t j=0;j<open.size();j++) {
            int e=edgepick(rng); double u=unif(rng); open[e]=0;
            if(u<p) open[e]=1;
            else if(u<a) open[e]=!connected(g.edges[e].u,g.edges[e].v);
        }
    }
};
void monte(const std::string& jobs,const std::string& path) {
    std::ifstream in(jobs); std::ofstream out(path);
    out<<"d,L,q,p,chain,start,seed,sample,chi,chi_excl,chi_nonwrap,wrap,largest,density,clusters\n";
    out<<std::setprecision(12);
    int d,L,chain,start,burn,sweeps,stride;double q,p;uint64_t seed;
    while(in>>d>>L>>q>>p>>chain>>start>>seed>>burn>>sweeps>>stride) {
        if(!(q>0 && q<=1 && p>0 && p<1)) throw std::runtime_error("bad q/p");
        Graph g(d,L); DSU uf(g.n); HeatBath hb(g,p,q,seed,start);
        for(int s=0;s<burn;s++) hb.sweep();
        int sample=0;
        for(int s=1;s<=sweeps;s++) {
            hb.sweep();if(s%stride) continue;
            Obs o=observe(g,hb.open,uf);
            int opened=std::accumulate(hb.open.begin(),hb.open.end(),0);
            out<<d<<','<<L<<','<<q<<','<<p<<','<<chain<<','<<start<<','<<seed<<','<<sample++
               <<','<<double(o.s2)/g.n<<','<<double(o.excl)/g.n
               <<','<<double(o.nonwrap)/g.n<<','<<o.wrapping
               <<','<<double(o.maxsize)/g.n<<','<<double(opened)/g.edges.size()
               <<','<<double(o.k)/g.n<<'\n';
        }
        out.flush();
        std::cerr<<"done "<<d<<' '<<L<<' '<<q<<' '<<p<<' '<<chain<<'\n';
    }
}
int main(int argc,char**argv) {
    try {
        if(argc==5 && std::string(argv[1])=="enum") enumerate(std::stoi(argv[2]),std::stoi(argv[3]),argv[4]);
        else if(argc==4 && std::string(argv[1])=="mc") monte(argv[2],argv[3]);
        else throw std::runtime_error("usage: fk enum d L hist.csv | fk mc jobs.txt samples.csv");
    }catch(const std::exception& e) {std::cerr<<e.what()<<'\n';return 1;}
}
