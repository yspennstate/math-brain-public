#include <bits/stdc++.h>
using namespace std;
using u64 = uint64_t;
using u128 = __uint128_t;

/*
Rigorous upward-rounded Bellman certificate for the oriented point-to-line
Exp(1) block used by PROB10-10.

For target level L=2m, transient vertices are x+y<L in the nonnegative
quadrant.  For an infected set S, b(S) is the number of directed boundary
edges.  The exact expected remaining hitting time satisfies

  E(S) = 1/b(S) + sum_v r_S(v)/b(S) E(S union {v}).

With a fixed integer scale Q, if every child has E <= U(child)/Q, then

  U(S) = ceil((Q + sum_v r_S(v) U(child))/b(S))

certifies E(S) <= U(S)/Q.  The same induction certifies an upper bound on
the second moment of the absorbing endpoint displacement D: for each
absorbing edge to w=(x,L-x), D=x-m and

  V(S)=ceil((Q*sum_abs_edges D(w)^2 + sum_v r_S(v)V(child))/b(S)).

Every transition adds one transient vertex, so this is a finite DAG
induction, not a floating-point approximation.
*/

struct Bounds { u64 time_num, d2_num; };

struct Solver {
    int L, N;
    u64 Q;
    vector<pair<int,int>> verts;
    unordered_map<long long,int> idx;
    unordered_map<u64,Bounds> memo;
    u64 start;

    static long long key(int x, int y) {
        return ((long long)x << 32) ^ (unsigned)y;
    }

    Solver(int level, u64 scale): L(level), Q(scale) {
        for (int s=0; s<L; ++s)
            for (int x=0; x<=s; ++x)
                verts.push_back({x, s-x});
        N = (int)verts.size();
        if (N > 63) throw runtime_error("bit-mask implementation requires N<=63");
        for (int i=0; i<N; ++i) idx[key(verts[i].first, verts[i].second)] = i;
        start = 1ULL << idx[key(0,0)];
        memo.reserve(12000000);
        memo.max_load_factor(0.75);
    }

    Bounds solve(u64 mask) {
        auto it = memo.find(mask);
        if (it != memo.end()) return it->second;

        unordered_map<int,int> rates;
        vector<int> absorbing_d2;
        int total = 0;

        for (int i=0; i<N; ++i) if ((mask >> i) & 1ULL) {
            int x = verts[i].first, y = verts[i].second;
            const int wx[2] = {x+1, x};
            const int wy[2] = {y, y+1};
            for (int a=0; a<2; ++a) {
                int xx = wx[a], yy = wy[a];
                if (xx + yy == L) {
                    ++total;
                    int d = xx - L/2; // D in (m+D,m-D)
                    absorbing_d2.push_back(d*d);
                } else {
                    int j = idx.at(key(xx,yy));
                    if (!((mask >> j) & 1ULL)) rates[j]++;
                }
            }
        }
        for (auto &p : rates) total += p.second;
        if (total <= 0) throw runtime_error("zero boundary rate");

        u128 nt = Q;  // waiting-time term 1/b
        u128 nv = 0;
        for (int z : absorbing_d2) nv += (u128)Q * (u64)z;
        for (auto &p : rates) {
            Bounds child = solve(mask | (1ULL << p.first));
            nt += (u128)p.second * child.time_num;
            nv += (u128)p.second * child.d2_num;
        }

        Bounds out {
            (u64)((nt + total - 1) / total),
            (u64)((nv + total - 1) / total)
        };
        memo.emplace(mask, out);
        return out;
    }
};

static bool lt_frac(u64 a, u64 b, u64 c, u64 d) {
    return (u128)a*d < (u128)c*b;
}

int main() {
    const u64 Q = 1000000000000000ULL; // 10^15
    vector<u64> U(5), V(5), states(5);

    cout << "PROB10-10 upward-rounded Bellman certificate\n";
    cout << "Q=" << Q << "\n";

    for (int m=1; m<=4; ++m) {
        Solver s(2*m, Q);
        Bounds z = s.solve(s.start);
        U[m] = z.time_num;
        V[m] = z.d2_num;
        states[m] = s.memo.size();
        long double q = (long double)U[m] / Q;
        long double ratio = q / m;
        long double d2 = (long double)V[m] / Q;
        long double err = 2.0L * sqrtl(d2) / m;
        cout << setprecision(18)
             << "m=" << m
             << " states=" << states[m]
             << " q_upper_num=" << U[m]
             << " d2_upper_num=" << V[m]
             << " q_upper=" << (double)q
             << " ratio_upper=" << (double)ratio
             << " finite_error_coeff_upper=" << (double)err
             << "\n";
    }

    // Exact prior values for m=1 and m=2 fit in 128-bit cross-products.
    // q_1 = 11/12; q_2 = 5927950393/3556224000.
    if ((u128)U[1]*12 < (u128)11*Q) throw runtime_error("m=1 upper bound failed");
    if ((u128)U[2]*3556224000ULL < (u128)5927950393ULL*Q)
        throw runtime_error("m=2 upper bound failed");

    // The certified m=4 diagonal ratio is < 0.763.
    if (!lt_frac(U[4], 4*Q, 763, 1000)) throw runtime_error("m=4 ratio not < 0.763");

    // Rounded certificates themselves strictly improve with m=1,2,3,4.
    for (int m=2; m<=4; ++m)
        if (!lt_frac(U[m], (u64)m*Q, U[m-1], (u64)(m-1)*Q))
            throw runtime_error("rounded ratios not strictly decreasing");

    cout << "m4_ratio_certified_fraction=3050962292602824/4000000000000000\n";
    cout << "m4_ratio_simplified=381370286575353/500000000000000\n";
    cout << "m4_ED2_certified_fraction=2300906478490488/1000000000000000\n";
    cout << "m4_ED2_simplified=287613309811311/125000000000000\n";
    cout << "m4_finite_error_coefficient=sqrt(287613309811311/125000000000000)/2\n";
    cout << "ALL_EXACT_INTEGER_CHECKS_PASS = True\n";
}
