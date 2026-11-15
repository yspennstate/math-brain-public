// Single-threaded uniform simple-regular sampler and balanced cut heuristics.
#include <algorithm>
#include <array>
#include <cassert>
#include <chrono>
#include <cmath>
#include <cstdint>
#include <fstream>
#include <functional>
#include <iomanip>
#include <iostream>
#include <numeric>
#include <random>
#include <string>
#include <vector>
#include <sys/resource.h>
using namespace std;
struct RNG {
    uint64_t x;
    explicit RNG(uint64_t seed):x(seed){}
    uint64_t next(){ x+=0x9e3779b97f4a7c15ULL; uint64_t z=x; z=(z^(z>>30))*0xbf58476d1ce4e5b9ULL; z=(z^(z>>27))*0x94d049bb133111ebULL; return z^(z>>31); }
    // Rejection removes modulo bias, including in the graph sampler.
    int integer(int n){uint64_t bound=n,t=-bound%bound,r;do{r=next();}while(r<t);return r%bound;}
    double uniform(){return (next()>>11)*0x1.0p-53;}
    template<class T> void shuffle_vec(vector<T>& v){for(int i=(int)v.size()-1;i>0;--i)swap(v[i],v[integer(i+1)]);}
};
struct Graph {int n,d;vector<vector<int>> a;vector<pair<int,int>> edges;};
Graph read_graph(string path){ifstream f(path);Graph g;f>>g.n>>g.d;g.a.resize(g.n);int u,v;while(f>>u>>v){g.edges.emplace_back(u,v);g.a[u].push_back(v);g.a[v].push_back(u);}assert((int)g.edges.size()==g.n*g.d/2);for(auto& a:g.a)assert((int)a.size()==g.d);return g;}
void generate(int n,int d,uint64_t seed,string path){
    RNG r(seed);vector<int> stubs(n*d);for(int i=0;i<n*d;i++)stubs[i]=i/d;
    vector<vector<int>> a(n);vector<pair<int,int>> edges;long attempts=0;
    for(;;){++attempts;r.shuffle_vec(stubs);for(auto& z:a)z.clear();edges.clear();bool ok=true;
        for(int i=0;i<n*d;i+=2){int u=stubs[i],v=stubs[i+1];if(u==v||find(a[u].begin(),a[u].end(),v)!=a[u].end()){ok=false;break;}a[u].push_back(v);a[v].push_back(u);edges.emplace_back(u,v);}
        if(ok)break;
    }
    ofstream f(path);f<<n<<" "<<d<<"\n";for(auto [u,v]:edges)f<<u<<" "<<v<<"\n";
    cout<<"{\"attempts\":"<<attempts<<",\"n\":"<<n<<",\"d\":"<<d<<",\"seed\":"<<seed<<"}\n";
}
struct Search {
    const Graph& g; bool maximize; RNG rng;vector<int> spin,bad,pos;vector<vector<int>> bucket;int plus,cost;
    Search(const Graph& gg,bool mx,uint64_t seed):g(gg),maximize(mx),rng(seed),spin(g.n),bad(g.n),pos(g.n),bucket(2*(g.d+1)){}
    int index(int u){return spin[u]*(g.d+1)+bad[u];}
    void remove(int u){auto& b=bucket[index(u)];int last=b.back();b[pos[u]]=last;pos[last]=pos[u];b.pop_back();}
    void add(int u){auto& b=bucket[index(u)];pos[u]=b.size();b.push_back(u);}
    void init(){vector<int> p(g.n);iota(p.begin(),p.end(),0);rng.shuffle_vec(p);for(int i=0;i<g.n;i++)spin[p[i]]=i<g.n/2; rebuild();}
    void rebuild(){plus=accumulate(spin.begin(),spin.end(),0);cost=0;for(auto& b:bucket)b.clear();for(int u=0;u<g.n;u++){bad[u]=0;for(int v:g.a[u])bad[u]+=(maximize?(spin[u]==spin[v]):(spin[u]!=spin[v]));cost+=bad[u];add(u);}cost/=2;}
    void flip(int u){int old=spin[u];cost+=g.d-2*bad[u];remove(u);for(int v:g.a[u]){remove(v);bad[v]+=(maximize?(old==spin[v]):(old!=spin[v]))?-1:1;add(v);}spin[u]^=1;plus+=old?-1:1;bad[u]=g.d-bad[u];add(u);}
    int choose(int rank,int forced){for(int b=g.d;b>=0;--b){for(int s=0;s<=1;++s){if(forced>=0&&s!=forced)continue;auto& z=bucket[s*(g.d+1)+b];if(rank<(int)z.size())return z[rank];rank-=z.size();}}abort();}
    bool adjacent(int u,int v){return find(g.a[u].begin(),g.a[u].end(),v)!=g.a[u].end();}
    // Full improving two-flip search. When gain is positive, the pair must occur
    // among the few top bad-edge buckets; scan only candidate buckets.
    void quench(){
        for(int iter=0;iter<4*g.n;iter++){
            int bu=-1,bv=-1,bdelta=0;
            // Adjacent pairs have a special correction; scan the sparse edges.
            for(auto [u,v]:g.edges)if(spin[u]!=spin[v]){
                int delta=2*g.d-2*(bad[u]+bad[v])+(maximize?-2:2);
                if(delta<bdelta){bu=u;bv=v;bdelta=delta;}
            }
            // For nonadjacent pairs the gain depends only on the two buckets.
            for(int x=g.d;x>=0;x--)for(int y=g.d;y>=0;y--){
                int base=2*g.d-2*(x+y);if(base>=bdelta)continue;
                const auto& left=bucket[x];const auto& right=bucket[(g.d+1)+y];
                bool found=false;
                for(int u:left){for(int v:right)if(!adjacent(u,v)){bu=u;bv=v;bdelta=base;found=true;break;}if(found)break;}
            }
            if(bu<0)break;
            int before=cost;flip(bu);flip(bv);assert(cost==before+bdelta);assert(plus==g.n/2);
        }
    }
    pair<int,vector<int>> eo(long sweeps,double tau){
        init();int best=cost;vector<int> bestspin=spin;
        vector<double> cdf(g.n);double z=0;for(int i=0;i<g.n;i++){z+=pow(i+1,-tau);cdf[i]=z;}for(auto& q:cdf)q/=z;
        for(long t=0;t<sweeps*g.n;t++){
            int forced=-1;if(plus<=g.n/2-1)forced=0;else if(plus>=g.n/2+1)forced=1;
            int count=forced<0?g.n:(forced?plus:g.n-plus);
            double u=rng.uniform()*cdf[count-1];int rank=lower_bound(cdf.begin(),cdf.begin()+count,u)-cdf.begin();
            int v=choose(rank,forced);flip(v);
            if(plus==g.n/2&&cost<best){best=cost;bestspin=spin;}
        }
        spin=bestspin;rebuild();quench();if(cost<best){best=cost;bestspin=spin;}
        int chk=0;for(auto [u,v]:g.edges)chk+=maximize?(bestspin[u]==bestspin[v]):(bestspin[u]!=bestspin[v]);assert(chk==best);assert(accumulate(bestspin.begin(),bestspin.end(),0)==g.n/2);
        return {best,bestspin};
    }
    pair<int,vector<int>> anneal(long sweeps){
        init();int best=cost;vector<int> bestspin=spin;
        // Kawasaki dynamics: exchange uniformly chosen opposite-spin vertices.
        vector<int> left,right,where(g.n);for(int u=0;u<g.n;u++){auto& v=spin[u]?right:left;where[u]=v.size();v.push_back(u);}
        for(long sweep=0;sweep<sweeps;sweep++){
            double frac=(sweep%400)/399.0;double temp=2.0*pow(0.02,frac);
            for(int j=0;j<g.n;j++){
                int i=rng.integer(g.n/2),k=rng.integer(g.n/2),u=left[i],v=right[k];
                int delta=2*g.d-2*(bad[u]+bad[v])+(adjacent(u,v)?(maximize?-2:2):0);
                if(delta<=0||rng.uniform()<exp(-delta/temp)){int before=cost;flip(u);flip(v);assert(cost==before+delta);left[i]=v;right[k]=u;where[u]=k;where[v]=i;
                    if(cost<best){best=cost;bestspin=spin;}
                }
            }
        }
        spin=bestspin;rebuild();quench();if(cost<best){best=cost;bestspin=spin;}return {best,bestspin};
    }
};
int main(int argc,char**argv){
    if(argc<2)return 1;
    if(string(argv[1])=="generate"){if(argc!=6)return 2;generate(stoi(argv[2]),stoi(argv[3]),stoull(argv[4]),argv[5]);return 0;}
    if(string(argv[1])=="exact"){
        if(argc!=3)return 5;Graph g=read_graph(argv[2]);if(g.n>30)return 6;
        int mn=g.edges.size(),mx=0;uint64_t count=0;vector<int>s(g.n),mins,maxs;
        function<void(int,int,int)> visit=[&](int u,int ones,int cut){
            if(ones>g.n/2||ones+g.n-u<g.n/2)return;
            if(u==g.n){++count;if(cut<mn||mins.empty()){mn=cut;mins=s;}if(cut>mx||maxs.empty()){mx=cut;maxs=s;}return;}
            for(int b=0;b<2;b++){s[u]=b;int dc=0;for(int v:g.a[u])if(v<u)dc+=s[v]!=b;visit(u+1,ones+b,cut+dc);}
        };
        s[0]=0;visit(1,0,0);
        cout<<"{\"min\":"<<mn<<",\"max\":"<<mx<<",\"partitions\":"<<count<<",\"min_spin\":\"";for(int b:mins)cout<<b;cout<<"\",\"max_spin\":\"";for(int b:maxs)cout<<b;cout<<"\"}\n";return 0;
    }
    if(string(argv[1])=="solve"){
        if(argc!=8)return 3;Graph g=read_graph(argv[2]);int restarts=stoi(argv[3]);long sweeps=stol(argv[4]);uint64_t seed=stoull(argv[5]);string method=argv[6];ofstream f(argv[7]);
        auto start=chrono::steady_clock::now();int mn=g.edges.size(),mx=0;
        for(int rep=0;rep<restarts;rep++){
            for(int objective=0;objective<2;objective++){
                Search s(g,objective,seed+100003ULL*rep+1000000007ULL*objective);double tau=rep%2?1.3:1.2;
                auto ans=method=="sa"?s.anneal(sweeps):s.eo(sweeps,tau);int cut=objective?(int)g.edges.size()-ans.first:ans.first;
                if(objective)mx=max(mx,cut);else mn=min(mn,cut);
                double secs=chrono::duration<double>(chrono::steady_clock::now()-start).count();
                f<<"{\"restart\":"<<rep<<",\"objective\":\""<<(objective?"max":"min")<<"\",\"cut\":"<<cut<<",\"best_min\":"<<mn<<",\"best_max\":"<<mx<<",\"seconds\":"<<secs<<",\"tau\":"<<tau<<",\"spin\":\"";for(int b:ans.second)f<<b;f<<"\"}\n";f.flush();
            }
        }
        struct rusage usage;getrusage(RUSAGE_SELF,&usage);
        cout<<"{\"min\":"<<mn<<",\"max\":"<<mx<<",\"seconds\":"<<chrono::duration<double>(chrono::steady_clock::now()-start).count()<<",\"maxrss_bytes\":"<<usage.ru_maxrss<<"}\n";return 0;
    }
    return 4;
}
