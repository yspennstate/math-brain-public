#include <bits/stdc++.h>
#include <omp.h>
using namespace std;

static const int N = 11;
static const int U = 1 << N;
using Bits = array<uint64_t, U / 64>;

struct Stats {
    int v, c0, c1, rho;
    vector<int> occ;
};

struct QRec {
    Bits slice{};
    uint16_t card = 0;
    uint8_t d = 0, v = 0, c0 = 0, c1 = 0;
    array<int8_t, 10> q{};
    uint8_t qlen = 0;
};

static void gen_rec(int n, int pos, int maxv, vector<int>& p,
                    const function<void(const vector<int>&)>& f) {
    if (pos == n) { f(p); return; }
    p.push_back(-1); gen_rec(n, pos + 1, maxv, p, f); p.pop_back();
    p.push_back(-2); gen_rec(n, pos + 1, maxv, p, f); p.pop_back();
    for (int v = 0; v <= maxv + 1; ++v) {
        p.push_back(v);
        gen_rec(n, pos + 1, max(maxv, v), p, f);
        p.pop_back();
    }
}

static void gen_patterns(int n, const function<void(const vector<int>&)>& f) {
    vector<int> p; p.reserve(n);
    gen_rec(n, 0, -1, p, f);
}

static Stats stats(const vector<int>& p) {
    int maxv = -1, c0 = 0, c1 = 0;
    for (int s : p) {
        if (s >= 0) maxv = max(maxv, s);
        else if (s == -1) ++c0;
        else ++c1;
    }
    vector<int> occ(maxv + 1, 0);
    for (int s : p) if (s >= 0) ++occ[s];
    int rho = 0;
    for (int k : occ) rho += k - 1;
    return {(int)occ.size(), c0, c1, rho, occ};
}

static long long Fcoeff(const vector<int>& occ, int d) {
    vector<long long> dp(d + 1, 0); dp[0] = 1;
    for (int k : occ) {
        vector<long long> nd(d + 1, 0);
        for (int s = 0; s <= d; ++s) if (dp[s]) {
            for (int e = 0; s + k * e <= d; ++e)
                nd[s + k * e] += dp[s] * (1LL << e);
        }
        dp.swap(nd);
    }
    return dp[d];
}

static inline void set_bit(Bits& b, int w) { b[w >> 6] |= 1ULL << (w & 63); }
static inline bool has_bit(const Bits& b, int w) { return (b[w >> 6] >> (w & 63)) & 1ULL; }
static int bit_card(const Bits& b) {
    int c = 0; for (uint64_t x : b) c += __builtin_popcountll(x); return c;
}

static Bits exact_slice(const vector<int>& q, const Stats& st) {
    Bits out{};
    int d = N - (int)q.size(), v = st.v;
    vector<int> e(v, 0);
    function<void(int,int)> rec = [&](int i, int rem) {
        if (i == v) {
            if (rem != 0) return;
            vector<int> L(v);
            for (int x = 0; x < v; ++x) L[x] = 1 + e[x];
            int base = 0, pos = 0;
            vector<vector<int>> masks_by_var(v);
            for (int x = 0; x < v; ++x) masks_by_var[x].assign(L[x], 0);
            for (int s : q) {
                if (s == -1) ++pos;
                else if (s == -2) { base |= 1 << (N - 1 - pos); ++pos; }
                else {
                    for (int j = 0; j < L[s]; ++j)
                        masks_by_var[s][j] |= 1 << (N - 1 - (pos + j));
                    pos += L[s];
                }
            }
            if (pos != N) { cerr << "INTERNAL_LENGTH_ERROR\n"; exit(90); }
            vector<int> masks;
            for (auto &a : masks_by_var) for (int m : a) masks.push_back(m);
            vector<int> words{base};
            for (int m : masks) {
                int z = (int)words.size();
                for (int j = 0; j < z; ++j) words.push_back(words[j] | m);
            }
            for (int w : words) set_bit(out, w);
            return;
        }
        int k = st.occ[i];
        for (int z = 0; z * k <= rem; ++z) {
            e[i] = z;
            rec(i + 1, rem - z * k);
        }
        e[i] = 0;
    };
    rec(0, d);
    return out;
}

static Bits exact_slice_d1(const vector<int>& q, const Stats& st) {
    Bits out{};
    int v = st.v;
    for (int ex = 0; ex < v; ++ex) if (st.occ[ex] == 1) {
        vector<int> L(v, 1); L[ex] = 2;
        int base = 0, pos = 0;
        vector<vector<int>> masks_by_var(v);
        for (int x = 0; x < v; ++x) masks_by_var[x].assign(L[x], 0);
        for (int s : q) {
            if (s == -1) ++pos;
            else if (s == -2) { base |= 1 << (N - 1 - pos); ++pos; }
            else {
                for (int j = 0; j < L[s]; ++j)
                    masks_by_var[s][j] |= 1 << (N - 1 - (pos + j));
                pos += L[s];
            }
        }
        if (pos != N) { cerr << "INTERNAL_D1_LENGTH_ERROR\n"; exit(91); }
        vector<int> masks;
        for (auto &a : masks_by_var) for (int m : a) masks.push_back(m);
        vector<int> words{base};
        for (int m : masks) {
            int z = (int)words.size();
            for (int j = 0; j < z; ++j) words.push_back(words[j] | m);
        }
        for (int w : words) set_bit(out, w);
    }
    return out;
}

static bool dfs_atoms(const Bits& S, int b, const vector<uint16_t>& cand,
                      int start, int prev_min, uint16_t used, int budget,
                      int need, vector<uint16_t>& unions,
                      vector<uint16_t>& atoms) {
    if (need == 0) return true;
    if (budget - __builtin_popcount((unsigned)used) < need) return false;
    for (int ii = start; ii < (int)cand.size(); ++ii) {
        uint16_t a = cand[ii];
        if (a & used) continue;
        int mb = __builtin_ctz((unsigned)a);
        if (mb <= prev_min) continue;
        int np = __builtin_popcount((unsigned)(used | a));
        if (np > budget || budget - np < need - 1) continue;
        bool ok = true;
        for (uint16_t u : unions) if (!has_bit(S, b | (u | a))) { ok = false; break; }
        if (!ok) continue;
        int old = (int)unions.size();
        for (int j = 0; j < old; ++j) unions.push_back(unions[j] | a);
        atoms.push_back(a);
        if (dfs_atoms(S, b, cand, ii + 1, mb, used | a, budget,
                      need - 1, unions, atoms)) return true;
        atoms.pop_back();
        unions.resize(old);
    }
    return false;
}

static bool contains_partition_cube(const Bits& S, int target_v,
                                    int c0q, int c1q) {
    for (int b = 0; b < U; ++b) if (has_bit(S, b)) {
        int ones = __builtin_popcount((unsigned)b);
        if (ones < c1q) continue;
        int budget = N - ones - c0q;
        if (budget < target_v) continue;
        vector<uint16_t> cand;
        for (int w = 0; w < U; ++w) if (w != b && has_bit(S, w) && (w & b) == b) {
            int a = w ^ b;
            if (__builtin_popcount((unsigned)a) <= budget) cand.push_back((uint16_t)a);
        }
        if ((int)cand.size() < target_v) continue;
        sort(cand.begin(), cand.end(), [](uint16_t a, uint16_t b) {
            int ma = __builtin_ctz((unsigned)a), mb = __builtin_ctz((unsigned)b);
            return ma == mb ? a < b : ma < mb;
        });
        vector<uint16_t> unions{0}, atoms;
        if (dfs_atoms(S, b, cand, 0, -1, 0, budget, target_v, unions, atoms)) return true;
    }
    return false;
}

static long long canonical_count_formula(int n) {
    vector<vector<long long>> S(n + 1, vector<long long>(n + 1, 0));
    S[0][0] = 1;
    for (int i = 1; i <= n; ++i)
        for (int k = 1; k <= i; ++k)
            S[i][k] = S[i-1][k-1] + k * S[i-1][k];
    long long ans = 0;
    for (int t = 0; t <= n; ++t) {
        long long choose = 1;
        for (int j = 0; j < t; ++j) choose = choose * (n - j) / (j + 1);
        long long Bell = 0;
        for (int k = 0; k <= t; ++k) Bell += S[t][k];
        ans += choose * (1LL << (n-t)) * Bell;
    }
    return ans;
}

int main() {
    const long long expected8 = 94828, expected9 = 562595, expected10 = 3535027,
                    expected11 = 23430840;
    if (canonical_count_formula(8) != expected8 || canonical_count_formula(9) != expected9 ||
        canonical_count_formula(10) != expected10 || canonical_count_formula(11) != expected11) {
        cerr << "CANONICAL_FORMULA_MISMATCH\n"; return 80;
    }
    cout << "CANONICAL_COUNTS 8:" << expected8 << " 9:" << expected9
         << " 10:" << expected10 << " 11:" << expected11 << "\n";

    vector<vector<int>> d4_profiles{{1,1,5},{1,2,4},{1,3,3},{2,2,3}};
    long long d4max = 0;
    for (auto p : d4_profiles) d4max = max(d4max, Fcoeff(p,4));
    if (d4max != 80 || d4max >= 256) { cerr << "D4_PROFILE_CHECK_FAIL\n"; return 81; }
    cout << "D4_PROFILE_MAX_F " << d4max << " REQUIRED 256\n";

    long long raw[4] = {0,0,0,0}, cardsurv[4] = {0,0,0,0};

    for (int d = 3; d >= 2; --d) {
        int m = N - d;
        vector<QRec> qs;
        gen_patterns(m, [&](const vector<int>& q) {
            Stats st = stats(q);
            if (st.v > N - 2*d || st.rho < d || Fcoeff(st.occ,d) < (1LL << (2*d))) return;
            ++raw[d];
            Bits S = exact_slice(q, st);
            int target = st.v + 2*d;
            int card = bit_card(S);
            if (target > N || card < (1 << target)) return;
            ++cardsurv[d];
            QRec r; r.slice=S; r.card=card; r.d=d; r.v=st.v; r.c0=st.c0; r.c1=st.c1;
            r.qlen=m; for (int i=0;i<m;++i) r.q[i]=q[i];
            qs.push_back(r);
        });
        atomic<int> found(-1);
        #pragma omp parallel for schedule(dynamic,64)
        for (int i=0;i<(int)qs.size();++i) {
            if (found.load(memory_order_relaxed)>=0) continue;
            if (contains_partition_cube(qs[i].slice, qs[i].v + 2*d, qs[i].c0, qs[i].c1)) {
                int exp=-1; found.compare_exchange_strong(exp,i);
            }
        }
        if (found.load() >= 0) {
            cerr << "SURVIVOR_D" << d << " INDEX " << found.load() << "\n"; return 2;
        }
        cout << "D" << d << " RAW " << raw[d] << " CARD_SURV " << cardsurv[d]
             << " CUBE_SURV 0\n";
    }

    {
        int d=1, m=10;
        vector<QRec> qs; qs.reserve(600000);
        gen_patterns(m, [&](const vector<int>& q) {
            Stats st=stats(q);
            if (st.v > 9 || st.rho < 1 || Fcoeff(st.occ,1) < 4) return;
            ++raw[d];
            int target=st.v+2;
            if (target>N) return;
            Bits S=exact_slice_d1(q,st);
            int card=bit_card(S);
            if (card < (1<<target)) return;
            ++cardsurv[d];
            QRec r; r.slice=S; r.card=card; r.d=1; r.v=st.v; r.c0=st.c0; r.c1=st.c1;
            r.qlen=10; for(int i=0;i<10;++i) r.q[i]=q[i];
            qs.push_back(r);
        });
        atomic<int> found(-1);
        #pragma omp parallel for schedule(dynamic,64)
        for (int i=0;i<(int)qs.size();++i) {
            if (found.load(memory_order_relaxed)>=0) continue;
            if (contains_partition_cube(qs[i].slice, qs[i].v+2, qs[i].c0, qs[i].c1)) {
                int exp=-1; found.compare_exchange_strong(exp,i);
            }
        }
        if (found.load()>=0) { cerr << "SURVIVOR_D1 INDEX " << found.load() << "\n"; return 2; }
        cout << "D1 RAW " << raw[d] << " CARD_SURV " << cardsurv[d] << " CUBE_SURV 0\n";
    }

    cout << "NO_BAD_MINSLICE_SURVIVOR_N11\n";
    cout << "ALL_EXACT_CHECKS_PASS\n";
    return 0;
}
