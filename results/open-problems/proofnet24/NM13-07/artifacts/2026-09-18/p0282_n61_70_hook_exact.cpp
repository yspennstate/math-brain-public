#include <boost/multiprecision/cpp_int.hpp>
#include <algorithm>
#include <iostream>
#include <map>
#include <string>
#include <vector>

using boost::multiprecision::cpp_int;
using std::cout;
using std::map;
using std::string;
using std::vector;

static cpp_int factorial_int(int n) {
    cpp_int x = 1;
    for (int i = 2; i <= n; ++i) x *= i;
    return x;
}

static void partitions_rec(int rem, int max_part, vector<int>& cur, const std::function<void(const vector<int>&)>& visit) {
    if (rem == 0) {
        visit(cur);
        return;
    }
    int hi = std::min(rem, max_part);
    for (int first = hi; first >= 1; --first) {
        cur.push_back(first);
        partitions_rec(rem - first, first, cur, visit);
        cur.pop_back();
    }
}

static cpp_int hook_dimension(const vector<int>& lam, int n, const cpp_int& fact) {
    cpp_int hooks = 1;
    int rows = (int)lam.size();
    for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < lam[i]; ++j) {
            int below = 0;
            for (int r = i + 1; r < rows; ++r) if (lam[r] > j) ++below;
            int h = (lam[i] - j) + below;
            hooks *= h;
        }
    }
    cpp_int q = fact / hooks;
    if (q * hooks != fact) {
        std::cerr << "nonintegral hook quotient at n=" << n << "\n";
        std::exit(2);
    }
    return q;
}

static string ratio_decimal_15(const cpp_int& num, const cpp_int& den) {
    cpp_int scaled = (num * cpp_int("1000000000000000")) / den;
    string s = scaled.convert_to<string>();
    while (s.size() < 16) s = "0" + s;
    return s.substr(0, s.size() - 15) + "." + s.substr(s.size() - 15);
}

int main() {
    const map<int,long long> p_expected = {
        {61,1121505},{62,1300156},{63,1505499},{64,1741630},{65,2012558},
        {66,2323520},{67,2679689},{68,3087735},{69,3554345},{70,4087968}
    };

    cout << "P0282 exact hook-length certificate for n=61..70 chaining archived n<=60 certificate\n";

    cpp_int global_num = 0, global_den = 1, global_margin = 0;
    int global_n = -1, global_k = -1;
    long long total_partitions = 0;

    for (int n = 61; n <= 70; ++n) {
        cpp_int fact = factorial_int(n);
        vector<cpp_int> ell(n + 1);
        vector<int> cur;
        long long pcount = 0;

        partitions_rec(n, n, cur, [&](const vector<int>& lam) {
            ++pcount;
            cpp_int f = hook_dimension(lam, n, fact);
            ell[lam[0]] += f * f;
        });

        if (pcount != p_expected.at(n)) {
            std::cerr << "partition-count mismatch n=" << n << " got=" << pcount << "\n";
            return 3;
        }
        total_partitions += pcount;

        cpp_int sum = 0;
        for (int k = 1; k <= n; ++k) sum += ell[k];
        if (sum != fact) {
            std::cerr << "Plancherel/factorial identity failed n=" << n << "\n";
            return 4;
        }

        cpp_int local_num = 0, local_den = 1;
        int local_k = -1;
        for (int k = 2; k < n; ++k) {
            cpp_int den = ell[k-1] * ell[k+1];
            cpp_int num = ell[k] * ell[k];
            cpp_int margin = num - den;
            if (margin < 0) {
                std::cerr << "NEGATIVE SOURCE MARGIN n=" << n << " k=" << k << "\n";
                return 5;
            }
            if (den != 0 && (local_k < 0 || num * local_den < local_num * den)) {
                local_num = num; local_den = den; local_k = k;
            }
            if (den != 0 && (global_n < 0 || num * global_den < global_num * den)) {
                global_num = num; global_den = den; global_margin = margin;
                global_n = n; global_k = k;
            }
        }

        cout << "n=" << n
             << " partitions=" << pcount
             << " local_min_k=" << local_k
             << " defect=" << (n-local_k)
             << " local_min_ratio~" << ratio_decimal_15(local_num, local_den)
             << " all_margins_nonnegative=True"
             << " factorial_check=True\n";
    }

    cout << "total_partitions_processed_61_70=" << total_partitions << "\n";
    cout << "global_min_location_61_70=(n=" << global_n << ",k=" << global_k << ",defect=" << (global_n-global_k) << ")\n";
    cout << "global_min_ratio_exact=" << global_num << "/" << global_den << "\n";
    cout << "global_min_margin_exact=" << global_margin << "\n";
    cout << "combined_scope_guard=with archived exact n<=60 certificate, N_exact=70; no all-n closure inferred\n";
    cout << "ALL_EXACT_CHECKS_PASS\n";
    return 0;
}
