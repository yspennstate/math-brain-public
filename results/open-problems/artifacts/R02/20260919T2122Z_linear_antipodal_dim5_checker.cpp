#include <array>
#include <cstdint>
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int H[16][16];
    for (int a = 0; a < 16; ++a)
        for (int x = 0; x < 16; ++x)
            H[a][x] = __builtin_parity((unsigned)(a & x)) ? -1 : 1;

    long long total_supports = 0;
    long long total_signings_examined = 0;

    for (int parity = 0; parity <= 1; ++parity) {
        const int threshold = parity ? 5 : 6;
        long long supports = 0;
        long long signings_examined = 0;
        int largest_certificate_seen = 0;

        for (int mask = 0; mask < (1 << 16); ++mask) {
            int s = __builtin_popcount((unsigned)mask);
            if ((s & 1) != parity) continue;
            ++supports;

            vector<int> pos;
            for (int x = 0; x < 16; ++x)
                if ((mask >> x) & 1) pos.push_back(x);

            int certificate = 99;
            if (s == 0) {
                certificate = 0;
            } else {
                // Fix the first selected sign to +1 (global-sign quotient).
                int coeff[16] = {0};
                for (int a = 0; a < 16; ++a)
                    for (int x : pos) coeff[a] += H[a][x];

                int lim = 1 << (s - 1);
                for (int g = 0; g < lim; ++g) {
                    if (g > 0) {
                        int cur = g ^ (g >> 1);
                        int old = (g - 1) ^ ((g - 1) >> 1);
                        int bit = __builtin_ctz((unsigned)(cur ^ old));
                        int x = pos[bit + 1];
                        int old_sign = ((old >> bit) & 1) ? -1 : 1;
                        int new_sign = ((cur >> bit) & 1) ? -1 : 1;
                        int delta = new_sign - old_sign;
                        for (int a = 0; a < 16; ++a)
                            coeff[a] += delta * H[a][x];
                    }

                    int max_abs = 0;
                    for (int a = 0; a < 16; ++a) {
                        int v = coeff[a] < 0 ? -coeff[a] : coeff[a];
                        if (v > max_abs) max_abs = v;
                    }
                    if (max_abs < certificate) certificate = max_abs;
                    ++signings_examined;
                    if (certificate <= threshold) break;
                }
            }

            if (certificate > threshold) {
                cout << "FAIL parity=" << parity
                     << " support_mask=" << mask
                     << " support_size=" << s
                     << " best_seen=" << certificate << "\n";
                return 1;
            }
            if (certificate > largest_certificate_seen)
                largest_certificate_seen = certificate;
        }

        cout << (parity ? "odd" : "even")
             << "_supports_checked=" << supports << "\n";
        cout << (parity ? "odd" : "even")
             << "_threshold=" << threshold << "\n";
        cout << (parity ? "odd" : "even")
             << "_signings_examined_until_certificate=" << signings_examined << "\n";
        cout << (parity ? "odd" : "even")
             << "_largest_returned_certificate=" << largest_certificate_seen << "\n";

        total_supports += supports;
        total_signings_examined += signings_examined;
    }

    if (total_supports != (1 << 16)) return 2;

    cout << "total_supports_checked=" << total_supports << "\n";
    cout << "total_signings_examined_until_certificate=" << total_signings_examined << "\n";
    cout << "FINITE_LEMMA: every even support O subset F2^4 has a signing q with ||H16 q||_inf <= 6.\n";
    cout << "FINITE_LEMMA: every odd support O subset F2^4 has a signing q with ||H16 q||_inf <= 5.\n";
    cout << "COROLLARY_SCOPE: complement-closed binary linear codes of dimension <=5.\n";
    cout << "PASS\n";
    return 0;
}
