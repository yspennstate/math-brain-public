#include <array>
#include <algorithm>
#include <cstdint>
#include <iostream>
#include <numeric>

int main() {
    constexpr int m = 11;
    std::array<int,m> p{};
    std::iota(p.begin(), p.end(), 0);

    std::int64_t total = 0, indecomp = 0;
    std::int64_t c1 = 0, c2 = 0, c3 = 0, c4 = 0;

    do {
        ++total;
        int mx = -1;
        bool decomposable = false;
        for (int i=0; i<m-1; ++i) {
            mx = std::max(mx, p[i]);
            if (mx == i) { decomposable = true; break; }
        }
        if (decomposable) continue;
        ++indecomp;

        int hist[21] = {0};
        for (int i=0; i<m; ++i) ++hist[i-p[i]+10];
        int SD = 0;
        for (int a=0; a<21; ++a) if (hist[a])
            for (int b=a+1; b<21; ++b) if (hist[b])
                SD += hist[a]*hist[b]*(b-a);

        // Exact residual cutoffs from D=SD/11 < 55*rho.
        // k=1: rho=157/500 => SD < 605*157/500 = 189.97 => SD<=189.
        // k=2: rho=33/125  => SD < 605*33/125  = 159.72 => SD<=159.
        // k=3: rho=23/100  => SD < 605*23/100  = 139.15 => SD<=139.
        // k=4: rho=41/200  => SD < 605*41/200  = 124.025=> SD<=124.
        if (SD <= 189) ++c1;
        if (SD <= 159) ++c2;
        if (SD <= 139) ++c3;
        if (SD <= 124) ++c4;
    } while (std::next_permutation(p.begin(), p.end()));

    std::cout << "total=" << total << "\n";
    std::cout << "indecomposable=" << indecomp << "\n";
    std::cout << "k1_equal_slab_residual=" << c1 << "\n";
    std::cout << "k2_equal_slab_residual=" << c2 << "\n";
    std::cout << "k3_equal_slab_residual=" << c3 << "\n";
    std::cout << "k4_equal_slab_residual=" << c4 << "\n";

    if (total != 39916800LL) return 1;
    if (indecomp != 31998903LL) return 2;
    if (c1 != 258261LL) return 3;
    if (c2 != 18122LL) return 4;
    if (c3 != 826LL) return 5;
    if (c4 != 24LL) return 6;

    std::cout << "EXACT S11 INTEGER ENUMERATION PASSED\n";
    return 0;
}
