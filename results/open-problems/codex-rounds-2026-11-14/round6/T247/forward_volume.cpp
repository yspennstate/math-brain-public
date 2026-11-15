// Exact-in-law radius and determinant simulation, with no matrix products.
#include <algorithm>
#include <array>
#include <cassert>
#include <chrono>
#include <cmath>
#include <csignal>
#include <cstdint>
#include <cstdlib>
#include <iomanip>
#include <iostream>
#include <random>
#include <sys/resource.h>
#include <unistd.h>
#include <vector>

int main() {
    alarm(180);
    assert(getpriority(PRIO_PROCESS, 0) >= 15);
    const auto start = std::chrono::steady_clock::now();
    constexpr uint64_t seed = 2476003;
    std::mt19937_64 rng(seed);
    std::normal_distribution<double> normal;
    const std::array<double, 3> times{.025, .05, .1};
    constexpr int samples = 3;
    bool first = true;
    std::cout << std::setprecision(17) << "{\"seed\":" << seed << ",\"samples\":" << samples << ",\"paths\":[\n";
    for (int n : {16, 32, 64}) {
        const double a = 1.0/(64*n*n);
        // These parameters satisfy the theorem's wider deterministic class.
        // They approximate, but do not equal, Gaussian critical parameters.
        const double lam = 2*a-5*a*a;
        const double gain2 = std::exp(lam);
        const double b = (4.0/3)*a*a*a;
        const double qinitial = a-b;
        const double cn = 2.0*n/(n+2);
        std::array<int64_t, 3> checkpoints{};
        for (int j=0; j<3; ++j) checkpoints[j] = std::llround(times[j]*n/a);
        for (int rep=0; rep<samples; ++rep) {
            double q=qinitial, H=0, linearS=0, sumq=0, sumr2=0;
            double maxradius=std::abs(q/a-1), sumU2=0, sumU=0, Nproxy=0;
            std::vector<double> u(n), bias(n);
            int checkpoint=0;
            for (int64_t layer=1; layer<=checkpoints.back(); ++layer) {
                double norm2=0;
                for (int i=0; i<n; ++i) {
                    u[i]=normal(rng);
                    norm2+=u[i]*u[i];
                    bias[i]=normal(rng);
                }
                const double scale=std::sqrt(n*q/norm2);
                double activation2=0, loggate=0;
                for (int i=0; i<n; ++i) {
                    const double z=scale*u[i]+std::sqrt(b)*bias[i];
                    const double h=std::tanh(z), h2=h*h;
                    activation2+=h2;
                    loggate+=2*std::log1p(-h2);
                }
                const double next=gain2*activation2/n;
                const double U=(next-q)/q;
                H+=lam+loggate/n;
                linearS+=lam-2*(q+b);
                sumq+=q;
                sumr2+=(q+b)*(q+b);
                sumU+=U;
                sumU2+=U*U;
                Nproxy+=U-(2*a-cn*q);
                q=next;
                maxradius=std::max(maxradius,std::abs(q/a-1));
                assert(q>a/2 && q<2*a);
                if (layer==checkpoints[checkpoint]) {
                    const double logratio=std::log(q/qinitial);
                    const double compensated=H-logratio+4*sumq/(n+2);
                    const double scalar_interval=15*sumr2;
                    const double log_remainder=std::abs(sumU-logratio);
                    assert(log_remainder<=8*sumU2+1e-9);
                    const double bound=std::abs(H-linearS)+scalar_interval+8*sumU2
                        +std::abs(Nproxy)+(300+452)*layer*a*a;
                    assert(std::abs(compensated)<=bound+1e-8);
                    if (!first) std::cout << ",\n";
                    first=false;
                    std::cout << "{\"n\":" << n << ",\"a\":" << a
                        << ",\"log_gain_squared\":" << lam << ",\"b\":" << b
                        << ",\"replicate\":" << rep << ",\"L\":" << layer
                        << ",\"La_squared\":" << layer*a*a << ",\"La_over_n\":" << layer*a/n
                        << ",\"H\":" << H << ",\"predicted_H\":" << -4*layer*a/n
                        << ",\"logS_linear_approximation\":" << linearS
                        << ",\"certified_logS_error\":" << scalar_interval
                        << ",\"compensated_H\":" << compensated
                        << ",\"pathwise_comparison_bound\":" << bound
                        << ",\"max_abs_radius_error\":" << maxradius
                        << ",\"final_radius_ratio\":" << q/a
                        << ",\"sum_squared_relative_increments\":" << sumU2
                        << ",\"log_radius_remainder\":" << log_remainder << "}";
                    ++checkpoint;
                    if (checkpoint==3) break;
                }
            }
        }
    }
    rusage usage{};
    getrusage(RUSAGE_SELF,&usage);
    double rss=usage.ru_maxrss;
#ifndef __APPLE__
    rss*=1024;
#endif
    assert(rss<1e9);
    const double elapsed=std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count();
    std::cout << "\n],\"runtime_seconds\":" << elapsed << ",\"peak_rss_bytes\":" << rss
        << ",\"niceness\":" << getpriority(PRIO_PROCESS,0) << ",\"threads\":1}\n";
}
