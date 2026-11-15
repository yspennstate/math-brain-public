#include <algorithm>
#include <cmath>
#include <cstdint>
#include <deque>
#include <iomanip>
#include <iostream>
#include <random>
#include <string>
#include <vector>

// One thread, O(n) memory, no censoring. Ending-time convention T=n+F.
int main(int argc, char** argv) {
    if (argc != 7) return 2;
    std::string family=argv[1];
    int n=std::stoi(argv[2]); double alpha=std::stod(argv[3]);
    int reps=std::stoi(argv[4]); uint64_t seed=std::stoull(argv[5]);
    int gaussian=std::stoi(argv[6]);
    int a=static_cast<int>(std::floor(alpha*std::sqrt(n)));
    if ((a-n)%2) ++a;
    if (family=="FP" && a>=0) return 3;
    std::mt19937_64 rng(seed);
    std::normal_distribution<double> normal;
    long double sum=0, sumsq=0;
    uint64_t bits=0; int left=0;
    auto step=[&](){
        if (gaussian) return normal(rng);
        if (!left) {bits=rng(); left=64;}
        double x=(bits&1)?1:-1; bits>>=1; --left; return x;
    };
    for (int rep=0; rep<reps; ++rep) {
        std::vector<double> ring(n+1,0);
        std::deque<std::pair<int64_t,double>> minima;
        minima.emplace_back(0,0);
        double s=0, initial=0; int64_t t=0;
        for (;;) {
            ++t; s+=step();
            while (!minima.empty() && minima.front().first<t-n) minima.pop_front();
            bool hit=false;
            if (t>=n) {
                double window=s-ring[(t-n)%(n+1)];
                if (gaussian) {
                    double value=window/std::sqrt(n)-alpha;
                    if (t==n) initial=value;
                    hit=(initial*value<=0);
                } else if (window==a) {
                    hit=(family=="BR" || minima.front().second>s);
                }
            }
            ring[t%(n+1)]=s;
            if (hit) break;
            while (!minima.empty() && minima.back().second>=s) minima.pop_back();
            minima.emplace_back(t,s);
        }
        sum+=t; sumsq+=static_cast<long double>(t)*t;
    }
    long double mean=sum/reps;
    long double se=std::sqrt((sumsq/reps-mean*mean)/(reps-1));
    std::cout<<std::setprecision(13)<<family<<","<<n<<","<<alpha<<","<<a
             <<","<<reps<<","<<seed<<","<<gaussian<<","<<mean<<","<<se
             <<","<<mean/n<<","<<se/n<<"\n";
}
