// Two independent, synchronous, non-lazy walks in one sampled environment.
#include <algorithm>
#include <cmath>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <random>
#include <unordered_map>
#include <vector>
#include <sys/resource.h>

struct Pos { int x=0, h=0; };
struct Comb {
    double gamma;
    int cap;
    std::mt19937_64 rng;
    std::unordered_map<int,int> heights;
    Comb(double g,int c,uint64_t s):gamma(g),cap(c),rng(s){}
    int height(int x) {
        auto it=heights.find(x);
        if(it!=heights.end()) return it->second;
        // U in (0,1), H=floor(U^(-1/gamma)). P(H>=k)=k^(-gamma).
        long double u=(static_cast<long double>(rng())+0.5L)/18446744073709551616.0L;
        long double logh=-std::log(u)/gamma;
        int h=logh>=std::log(static_cast<long double>(cap)) ? cap :
            std::min(cap,static_cast<int>(std::floor(std::exp(logh))));
        heights[x]=h;
        return h;
    }
};
void step(Pos& p,Comb& c,std::mt19937_64& r) {
    int h=c.height(p.x);
    if(p.h==0) {
        int z=std::uniform_int_distribution<int>(0,h>0 ? 2 : 1)(r);
        if(z==0) --p.x;
        else if(z==1) ++p.x;
        else ++p.h;
    } else if(p.h==h) --p.h;
    else p.h += std::uniform_int_distribution<int>(0,1)(r) ? 1 : -1;
}
#ifndef SIMULATOR_NO_MAIN
int main(int argc,char**argv) {
    const int environments=argc>1 ? std::stoi(argv[1]) : 32;
    const int pairs=argc>2 ? std::stoi(argv[2]) : 8;
    const int power=argc>3 ? std::stoi(argv[3]) : 17;
    if(environments<1 || pairs<1 || power<1 || power>20) return 2;
    const int T=1<<power;
    // A failed query cannot silently turn this into unprioritized research compute.
    errno=0;
    int priority=getpriority(PRIO_PROCESS,0);
    if(errno || priority<10) { std::cerr<<"Requires inherited nice >=10\n"; return 3; }
    std::ofstream out("data/collisions.csv");
    out<<"gamma,environment,pair,time,total,backbone,last_total,last_backbone,max_abs_x,max_height\n";
    out.precision(17);
    std::vector<double> gammas={0.28,1.0/3.0,0.40};
    for(size_t gi=0;gi<gammas.size();++gi) {
        for(int e=0;e<environments;++e) {
            Comb c(gammas[gi],T+1,1700327ULL+gi*1000003ULL+e*73471ULL);
            for(int p=0;p<pairs;++p) {
                // Environment generator is independent of both trajectory generators.
                uint64_t seed=982451653ULL+gi*1000000007ULL+e*32452843ULL+p*49979687ULL;
                std::mt19937_64 r1(seed),r2(seed+67867967ULL);
                Pos a,b;
                int total=0,base=0,last=0,lastbase=0,mx=0,mh=0,next=1;
                for(int n=1;n<=T;++n) {
                    step(a,c,r1); step(b,c,r2);
                    mx=std::max({mx,std::abs(a.x),std::abs(b.x)});
                    mh=std::max({mh,a.h,b.h});
                    if(a.x==b.x && a.h==b.h) {
                        ++total; last=n;
                        if(a.h==0) {++base; lastbase=n;}
                    }
                    if(n==next) {
                        out<<gammas[gi]<<','<<e<<','<<p<<','<<n<<','<<total<<','<<base
                           <<','<<last<<','<<lastbase<<','<<mx<<','<<mh<<'\n';
                        next*=2;
                    }
                }
            }
        }
        std::cerr<<"completed gamma="<<gammas[gi]<<" at T="<<T<<"\n";
    }
}

#endif
