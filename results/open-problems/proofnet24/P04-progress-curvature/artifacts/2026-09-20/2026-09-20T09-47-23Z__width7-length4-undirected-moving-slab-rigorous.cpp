#include <bits/stdc++.h>
using namespace std;

// P04 / T10 rigorous finite-core certificate.
// Moving-centered width-7, length-4 UNDIRECTED slab for iid Exp(1) FPP.
// Physical edges inside departure columns 0,1,2,3 are ordinary undirected
// nearest-neighbor edges. Terminal-column vertical edges at x=4 are omitted.
// We stop at the first infection of any vertex in column 4.
//
// For each infection state S, exponential memorylessness gives
//   E(S)=1/m(S)+sum_j m_j(S)/m(S) E(S union {j}).
// Every transition strictly enlarges S.  With Q fixed, integer ceiling division
// propagates a rigorous rational upper bound.  The same positive recurrence
// with terminal reward displacement^2 certifies E[xi^2].

struct Val { uint64_t t, m2; };
static constexpr int L = 4;
static constexpr int W = 7;
static constexpr uint64_t Q = 1000000000000000ULL;
static vector<vector<int>> adjv;
static uint64_t target_mask;
static unordered_map<uint64_t, Val> memo;
static unsigned long long state_count = 0;

static Val rec(uint64_t mask) {
    auto it = memo.find(mask);
    if (it != memo.end()) return it->second;
    ++state_count;

    if (mask & target_mask) {
        int rr = -1;
        for (int r=0; r<W; ++r) {
            int id = L*W+r;
            if ((mask>>id)&1ULL) { rr=r; break; }
        }
        assert(rr >= 0);
        long long d = rr - W/2;
        Val v{0, (uint64_t)(d*d)*Q};
        memo.emplace(mask,v);
        return v;
    }

    int rates[64] = {0};
    int total = 0;
    uint64_t mm = mask;
    while (mm) {
        int i = __builtin_ctzll(mm);
        mm &= mm-1;
        for (int j : adjv[i]) if (!((mask>>j)&1ULL)) {
            ++rates[j];
            ++total;
        }
    }
    assert(total > 0);

    __int128 tsum = Q;
    __int128 m2sum = 0;
    for (int j=0; j<(L+1)*W; ++j) if (rates[j]) {
        Val c = rec(mask | (1ULL<<j));
        tsum += (__int128)rates[j]*c.t;
        m2sum += (__int128)rates[j]*c.m2;
    }
    uint64_t tu = (uint64_t)((tsum + total - 1)/total);
    uint64_t m2u = (uint64_t)((m2sum + total - 1)/total);
    Val v{tu,m2u};
    memo.emplace(mask,v);
    return v;
}

int main() {
    const int n=(L+1)*W;
    auto id=[](int x,int r){return x*W+r;};
    adjv.assign(n,{});

    // Horizontal physical edges in the slab, traversable both ways.
    for (int x=0; x<L; ++x) for (int r=0; r<W; ++r) {
        int a=id(x,r), b=id(x+1,r);
        adjv[a].push_back(b);
        adjv[b].push_back(a);
    }
    // Vertical physical edges only in departure columns 0,...,L-1.
    for (int x=0; x<L; ++x) for (int r=0; r<W-1; ++r) {
        int a=id(x,r), b=id(x,r+1);
        adjv[a].push_back(b);
        adjv[b].push_back(a);
    }

    target_mask=0;
    for (int r=0; r<W; ++r) target_mask |= 1ULL<<id(L,r);

    memo.reserve(40000000);
    Val root=rec(1ULL<<id(0,W/2));

    // Immutable expected outputs of this exact program/build-independent integer recursion.
    assert(state_count == 35188637ULL);
    assert(root.t == 2071160703929378ULL);
    assert(root.m2 == 2496533430161757ULL);
    assert(root.t < 2071161ULL*1000000000ULL); // E tau < 2.071161, loose readable check
    assert(root.m2 < 2496540ULL*1000000000ULL); // E xi^2 < 2.496540

    cout << "P04 T10 width-7 length-4 undirected moving-slab finite certificate\n";
    cout << "ALL_RIGOROUS_CHECKS_PASS = True\n";
    cout << "L = " << L << "\nW = " << W << "\nQ = " << Q << "\n";
    cout << "reachable_states = " << state_count << "\n";
    cout << "tau_upper_numerator = " << root.t << "\n";
    cout << "tau_upper_denominator = " << Q << "\n";
    cout << "axis_cap_numerator = " << root.t << "\n";
    cout << "axis_cap_denominator = " << (4ULL*Q) << "\n";
    cout << "xi2_upper_numerator = " << root.m2 << "\n";
    cout << "xi2_upper_denominator = " << Q << "\n";
    cout << setprecision(18);
    cout << "E_tau_upper_decimal = " << (long double)root.t/Q << "\n";
    cout << "axis_cap_decimal = " << (long double)root.t/Q/L << "\n";
    cout << "E_xi2_upper_decimal = " << (long double)root.m2/Q << "\n";
    cout.flush();
    _Exit(0); // avoid spending time destructing the 35M-state hash table
}
