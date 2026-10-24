#include <algorithm>
#include <array>
#include <cstdlib>
#include <fstream>
#include <iostream>
#include <numeric>
using namespace std;

static inline int psi12(int k) {
    k = abs(k);
    if (k == 0) return 8;
    if (k == 1) return 13;
    return 12 * k;
}

int main(int argc, char** argv) {
    const char* outpath = argc >= 2 ? argv[1] : "s11_n11_universal_residual.csv";
    ofstream out(outpath);
    if (!out) { cerr << "cannot open output\n"; return 2; }

    array<int,11> p;
    iota(p.begin(), p.end(), 0);
    long long total = 0, pass = 0, fail = 0;
    int min_pass_margin = 1e9, max_fail_margin = -1000000000;
    const int rhs = 8 * 11 * 11 * 11 * 11; // 117128

    do {
        ++total;
        int half = 0;
        for (int i = 0; i < 11; ++i) {
            for (int j = i + 1; j < 11; ++j) {
                const int d = i - j;
                const int e = p[i] - p[j];
                half += abs(d - e) * psi12(d + e);
            }
        }
        const int S12 = 2 * half;
        const int margin = 5 * S12 - rhs;
        if (margin >= 0) {
            ++pass;
            min_pass_margin = min(min_pass_margin, margin);
        } else {
            ++fail;
            max_fail_margin = max(max_fail_margin, margin);
            for (int i = 0; i < 11; ++i) {
                if (i) out << ',';
                out << p[i];
            }
            out << ',' << margin << '\n';
        }
    } while (next_permutation(p.begin(), p.end()));

    cout << "total=" << total << '\n';
    cout << "pass=" << pass << '\n';
    cout << "fail=" << fail << '\n';
    cout << "min_pass_margin=" << min_pass_margin << '\n';
    cout << "max_fail_margin=" << max_fail_margin << '\n';

    if (total != 39916800LL) return 3;
    if (pass != 39489793LL) return 4;
    if (fail != 427007LL) return 5;
    if (min_pass_margin != 2) return 6;
    if (max_fail_margin != -8) return 7;
    cout << "EXACT S11 N11 PHASE1 PASSED\n";
    return 0;
}
