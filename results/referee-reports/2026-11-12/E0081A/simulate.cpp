#include <algorithm>
#include <cmath>
#include <cstdint>
#include <cstdlib>
#include <iomanip>
#include <iostream>
#include <random>
#include <string>
#include <unordered_set>
#include <vector>

// Single-threaded simulations. T is the END time, including the first n steps.
struct Bits {
    std::mt19937_64 gen;
    uint64_t reservoir=0; int left=0;
    explicit Bits(uint64_t seed):gen(seed){}
    int step() {
        if (!left) { reservoir=gen(); left=64; }
        int z=(reservoir&1)?1:-1; reservoir>>=1; --left; return z;
    }
};
struct Moments {
    long long count=0; long double mean=0, m2=0;
    void add(long double x) { ++count; auto d=x-mean; mean+=d/count; m2+=d*(x-mean); }
    long double se()const{return count>1?std::sqrt(m2/(count-1)/count):0;}
};
long long waiting(int n,int a,Bits& rng) {
    // Increasing queue of positions among the preceding n time indices.
    std::vector<int> history(n+1), values(n+2);
    std::vector<long long> times(n+2);
    int head=0,tail=1,cap=n+2,pos=0; values[0]=0;times[0]=0;
    for(long long t=1;;++t) {
        pos+=rng.step();
        while(head!=tail && times[head]<t-n) head=(head+1)%cap;
        if(t>=n && pos-history[(t-n)%(n+1)]==-a && pos<values[head]) return t;
        history[t%(n+1)]=pos;
        while(head!=tail) {
            int back=(tail+cap-1)%cap;
            if(values[back]<pos) break;
            tail=back;
        }
        values[tail]=pos;times[tail]=t;tail=(tail+1)%cap;
    }
}
long long waiting_brute(int n,int a,Bits& rng) {
    std::vector<int> history(n+1);int pos=0;
    for(long long t=1;;++t) {
        pos+=rng.step();
        bool hit=t>=n&&pos-history[(t-n)%(n+1)]==-a;
        if(hit)for(long long j=t-n;j<t;++j)if(history[j%(n+1)]<=pos){hit=false;break;}
        if(hit)return t;
        history[t%(n+1)]=pos;
    }
}
void check(int n,int a) {
    // Exhaust every path through time 2n (n<=10), comparing the queue with
    // direct examination of all n increments at each candidate endpoint.
    const int horizon=2*n,cap=n+2;
    for(uint64_t word=0;word<(uint64_t(1)<<horizon);++word) {
        std::vector<int> s(horizon+1),qv(cap);
        std::vector<int> qt(cap);int head=0,tail=1;
        for(int t=1;t<=horizon;++t) {
            s[t]=s[t-1]+((word>>(t-1)&1)?1:-1);
            while(head!=tail&&qt[head]<t-n)head=(head+1)%cap;
            bool fast=t>=n&&s[t]-s[t-n]==-a&&s[t]<qv[head];
            bool slow=t>=n&&s[t]-s[t-n]==-a;
            if(slow)for(int j=t-n;j<t;++j)if(s[j]<=s[t])slow=false;
            if(fast!=slow){std::cerr<<"queue mismatch\n";std::exit(2);}
            while(head!=tail){int b=(tail+cap-1)%cap;if(qv[b]<s[t])break;tail=b;}
            qv[tail]=s[t];qt[tail]=t;tail=(tail+1)%cap;
        }
    }
    std::cout<<"exhaustive detector check passed n="<<n<<" a="<<a<<"\n";
}
int main(int argc,char**argv) {
    if(argc<2){std::cerr<<"simulate check n a | wait n a reps seed | range m reps seed\n";return 1;}
    std::string mode=argv[1];
    if(mode=="check"){check(std::atoi(argv[2]),std::atoi(argv[3]));return 0;}
    if(mode=="wait"||mode=="brute") {
        int n=std::atoi(argv[2]),a=std::atoi(argv[3]),reps=std::atoi(argv[4]);
        uint64_t seed=std::strtoull(argv[5],nullptr,10);Bits rng(seed);Moments stats;
        for(int i=0;i<reps;++i)stats.add(mode=="wait"?waiting(n,a,rng):waiting_brute(n,a,rng));
        std::cout<<"n,a,reps,seed,mean,se,ci95_low,ci95_high,mean_over_n,mean_over_nlogn\n";
        std::cout<<std::setprecision(12)<<n<<","<<a<<","<<reps<<","<<seed<<","<<double(stats.mean)<<","<<double(stats.se())<<","<<double(stats.mean-1.96L*stats.se())<<","<<double(stats.mean+1.96L*stats.se())<<","<<double(stats.mean/n)<<","<<double(stats.mean/n/std::log(n))<<"\n";
        return 0;
    }
    if(mode=="range") {
        int m=std::atoi(argv[2]),reps=std::atoi(argv[3]);uint64_t seed=std::strtoull(argv[4],nullptr,10);
        Bits rng(seed);Moments range,visits;
        for(int r=0;r<reps;++r) {
            int x=0,y=0,low=0,count=1;std::unordered_set<int> sites{0};
            for(int t=1;t<=m;++t){x+=rng.step();y+=rng.step();if(y<low){low=y;++count;sites.insert(x-y);}}
            range.add(sites.size());visits.add(count);
        }
        std::cout<<"m,reps,seed,range_mean,range_se,visits_mean,range_logm_over_sqrtm\n";
        std::cout<<std::setprecision(12)<<m<<","<<reps<<","<<seed<<","<<double(range.mean)<<","<<double(range.se())<<","<<double(visits.mean)<<","<<double(range.mean*std::log(m)/std::sqrt(m))<<"\n";
        return 0;
    }
    return 1;
}
