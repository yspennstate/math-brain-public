// Full-state deterministic propagation on S_n, with a factorial rank.
// One thread; double precision. No matrix of size (n!)^2 is formed.
#include <algorithm>
#include <array>
#include <chrono>
#include <cmath>
#include <cstdint>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <numeric>
#include <string>
#include <vector>
#include <sys/resource.h>
#include <unistd.h>

using Perm = std::array<int, 11>;
int n;
uint32_t fact[12];
uint32_t rank_perm(const Perm& p) {
    uint32_t r=0, used=0;
    for (int i=0;i<n;++i) {
        r += (p[i]-__builtin_popcount(used & ((1u<<p[i])-1u))) * fact[n-1-i];
        used |= 1u<<p[i];
    }
    return r;
}
int main(int argc,char** argv) {
    if(argc!=5) { std::cerr<<"usage: exact_walk n base|double max_steps csv\n";return 2; }
    if(getpriority(PRIO_PROCESS,0)<10) setpriority(PRIO_PROCESS,0,10);
    n=std::stoi(argv[1]);std::string model=argv[2];int maxt=std::stoi(argv[3]);
    if(n<3 || n>11 || (model!="base" && model!="double")) return 2;
    fact[0]=1;for(int i=1;i<=n;++i)fact[i]=fact[i-1]*i;
    uint32_t N=fact[n]; int k=model=="base"?3:5;
    const uint64_t array_bytes=uint64_t(N)*(4ULL*k+16ULL);
    // macOS rejects small RLIMIT_AS values; check the actual allocation plan.
    if(array_bytes>3500000000ULL) {std::cerr<<"array budget exceeded\n";return 2;}
    std::cerr<<"planned_array_bytes="<<array_bytes<<" nice="<<getpriority(PRIO_PROCESS,0)<<"\n";
    Perm id{};std::iota(id.begin(),id.begin()+n,0);
    std::vector<Perm> gs(k,id);
    std::swap(gs[0][0],gs[0][1]);
    for(int i=0;i<n;++i) { gs[1][i]=(i+1)%n;gs[2][i]=(i+n-1)%n; }
    if(k==5) {
        int m=(n%2)?n:n-1;
        for(int i=0;i<m;++i)gs[3][i]=2*i%m;
        for(int i=0;i<n;++i)gs[4][gs[3][i]]=i;
    }
    const auto start=std::chrono::steady_clock::now();
    std::vector<std::vector<uint32_t>> tr(k,std::vector<uint32_t>(N));
    Perm p=id,q;
    uint32_t r=0;
    do {
        for(int j=0;j<k;++j) {
            for(int i=0;i<n;++i)q[i]=p[gs[j][i]];
            tr[j][r]=rank_perm(q);
        }
        ++r;
    } while(std::next_permutation(p.begin(),p.begin()+n));
    std::cerr<<"built n="<<n<<" "<<model<<" states="<<N<<" seconds="
             <<std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count()<<"\n";
    std::vector<double> a(N,0),b(N);a[0]=1;
    std::ofstream out(argv[4]);out<<"n,model,t,tv,mass,l2sq,elapsed_s\n"<<std::setprecision(16);
    const double u=1.0/N, w=0.5/k;
    for(int t=0;t<=maxt;++t) {
        double tv=0, mass=0, l2=0;
        for(uint32_t x=0;x<N;++x) {double z=a[x]-u;tv+=std::abs(z);mass+=a[x];l2+=z*z;}
        tv*=0.5;l2*=N;
        out<<n<<","<<model<<","<<t<<","<<tv<<","<<mass<<","<<l2<<","
           <<std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count()<<"\n";
        if(t%50==0) {
            out.flush();std::cerr<<n<<" "<<model<<" t="<<t<<" tv="<<tv<<"\n";
            struct rusage interim;getrusage(RUSAGE_SELF,&interim);
            // ru_maxrss is bytes on macOS, kilobytes on Linux.
            uint64_t rss=interim.ru_maxrss;
#ifndef __APPLE__
            rss*=1024;
#endif
            if(rss>3900000000ULL){std::cerr<<"resident memory budget exceeded\n";return 2;}
        }
        if(tv<0.01 || t==maxt)break;
        // Gather each row. The set of generators is symmetric, so this is aP.
        if(k==3) {
            const auto *s0=tr[0].data(),*s1=tr[1].data(),*s2=tr[2].data();
            for(uint32_t x=0;x<N;++x)b[x]=0.5*a[x]+w*(a[s0[x]]+a[s1[x]]+a[s2[x]]);
        } else {
            const auto *s0=tr[0].data(),*s1=tr[1].data(),*s2=tr[2].data(),*s3=tr[3].data(),*s4=tr[4].data();
            for(uint32_t x=0;x<N;++x)b[x]=0.5*a[x]+w*(a[s0[x]]+a[s1[x]]+a[s2[x]]+a[s3[x]]+a[s4[x]]);
        }
        a.swap(b);
    }
    struct rusage usage;getrusage(RUSAGE_SELF,&usage);
    uint64_t rss=usage.ru_maxrss;
#ifndef __APPLE__
    rss*=1024;
#endif
    std::cerr<<"peak_rss_bytes="<<rss<<" elapsed_s="
             <<std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count()<<"\n";
}
