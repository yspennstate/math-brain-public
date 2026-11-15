// Independent detector: a downward step is a strict window minimum exactly
// when the last previous visit to its height precedes the window's start.
#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdint>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <map>
#include <random>
#include <set>
#include <vector>
#include <sys/resource.h>
struct Stats {
    long long k=0; long double s=0,ss=0;
    void add(long double x){++k;s+=x;ss+=x*x;}
    double mean()const{return double(s/k);}
    double se()const{return double(sqrtl((ss-s*s/k)/(k-1)/k));}
};
bool scan(const std::vector<int>& h,int t,int n,int a){
    if(h[t]-h[t-n]!=-a)return false;
    for(int j=t-n;j<t;++j)if(h[j]<=h[t])return false;
    return true;
}
void exhaustive(){
    uint64_t cases=0;
    const int H=18;
    for(unsigned mask=0;mask<(1u<<H);++mask){
        std::vector<int> h(H+1); std::map<int,int> last;last[0]=0;
        for(int t=1;t<=H;++t){
            int bit=(mask>>(t-1)&1)?1:-1; h[t]=h[t-1]+bit;
            int previous=last.count(h[t])?last[h[t]]:-1;
            for(int n=2;n<=std::min(10,t);++n)for(int a=1;a<=n;++a){
                bool detected=bit==-1&&h[t]-h[t-n]==-a&&previous<t-n;
                assert(detected==scan(h,t,n,a));++cases;
            }
            last[h[t]]=t;
        }
    }
    std::cout<<"exhaustive_detector_cases "<<cases<<"\n"<<std::flush;
}
void waiting(int n,int a,int reps,uint64_t seed,std::ofstream& out){
    std::mt19937_64 rng(seed);uint64_t bits=0;int left=0;
    auto step=[&](){if(!left){bits=rng();left=64;}int u=(bits&1)?1:-1;bits>>=1;--left;return u;};
    Stats T;int radius=n+1024;
    std::vector<int> last(2*radius+1,-1),stamp(2*radius+1,-1),ring(n+1);
    for(int rep=0;rep<reps;++rep){
        int pos=0,t=0;stamp[radius]=rep;last[radius]=0;ring[0]=0;
        while(true){
            int u=step();pos+=u;++t;
            if(std::abs(pos)>radius){
                int old=radius;radius*=2;
                std::vector<int> a1(2*radius+1,-1),a2(2*radius+1,-1);
                std::copy(last.begin(),last.end(),a1.begin()+radius-old);
                std::copy(stamp.begin(),stamp.end(),a2.begin()+radius-old);
                last.swap(a1);stamp.swap(a2);
            }
            int j=pos+radius;int previous=stamp[j]==rep?last[j]:-1;
            bool hit=t>=n&&u==-1&&pos-ring[(t-n)%(n+1)]==-a&&previous<t-n;
            stamp[j]=rep;last[j]=t;ring[t%(n+1)]=pos;
            if(hit){T.add(t);break;}
        }
    }
    out<<n<<','<<a<<','<<reps<<','<<seed<<','<<T.mean()<<','<<T.se()<<','<<T.mean()-n<<','<<T.mean()/n<<','<<T.mean()/(n*std::log(n))<<'\n';out.flush();
    std::cout<<"wait n="<<n<<" a="<<a<<" mean="<<T.mean()<<" se="<<T.se()<<'\n'<<std::flush;
}
void blocks(int n,int a,int reps,uint64_t seed,std::ofstream& out){
    std::mt19937_64 rng(seed);int m=n/2;Stats Q,N,R,V,ret;
    std::vector<int> h(n+m+1),x(m+1),y(m+1);
    for(int rep=0;rep<reps;++rep){
        for(int t=1;t<=n+m;++t)h[t]=h[t-1]+((rng()&1)?1:-1);
        int hits=0;
        // Direct scans, used only at the prescribed displacement.
        for(int s=0;s<=m;++s)hits+=scan(h,n+s,n,a);
        Q.add(hits>0);N.add(hits);
        std::set<int> range{0};int low=0,v=1,zret=1;
        for(int s=1;s<=m;++s){
            x[s]=h[s];y[s]=h[n+s]-h[n];
            if(y[s]<low){low=y[s];++v;range.insert(x[s]-y[s]);zret+=(x[s]==y[s]);}
        }
        R.add(range.size());V.add(v);ret.add(zret);
        if(hits)assert(range.count(h[n]-h[m]+h[m]+a));
    }
    out<<n<<','<<a<<','<<reps<<','<<seed<<','<<Q.mean()<<','<<Q.se()<<','<<N.mean()<<','<<N.se()<<','<<R.mean()<<','<<R.se()<<','<<V.mean()<<','<<ret.mean()<<'\n';out.flush();
    std::cout<<"block n="<<n<<" q="<<Q.mean()<<" range="<<R.mean()<<'\n'<<std::flush;
}
int main(){
    exhaustive();
    std::ofstream w("referee_results/waiting.csv");w<<std::setprecision(14)<<"n,a,trials,seed,mean_end,se,mean_start,mean_over_n,mean_over_nlogn\n";
    uint64_t seed=0xa913cf487112ull;
    for(auto args:std::vector<std::vector<int>>{{8,2,200000},{12,2,200000},{100,10,50000},{200,14,30000},{500,22,20000},{1000,30,25000},{1000,32,25000},{2000,44,15000},{10000,100,5000},{100000,316,1000}})
        waiting(args[0],args[1],args[2],seed++,w);
    std::ofstream b("referee_results/blocks.csv");b<<std::setprecision(14)<<"n,a,trials,seed,q,se_q,EN,se_N,ER,se_R,EV,G_sample\n";
    for(int n:{100,1000,10000}){
        int endpoint=int(std::floor(-std::sqrt(n)));if((endpoint-n)%2)++endpoint;
        blocks(n,-endpoint,n==10000?5000:20000,seed++,b);
    }
    rusage usage{};
    if(getrusage(RUSAGE_SELF,&usage)==0){
        std::ofstream r("referee_results/mc_resources.json");
        r<<"{\"maxrss_platform_units\":"<<usage.ru_maxrss<<",\"platform\":\"macOS (bytes)\",\"worker_threads\":1}\n";
    }
}
