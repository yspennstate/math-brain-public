#include <algorithm>
#include <array>
#include <cstdint>
#include <cmath>
#include <iomanip>
#include <iostream>
#include <limits>
#include <vector>

// P13 / T02 exact verifier for the genuine dependent binary-LCS strip.
// Floating arithmetic is used ONLY to propose an integer potential H.
// Every claimed bound is then checked by integer Bellman residuals.

struct StepResult {
    uint32_t next;
    uint8_t reward;
};

static inline StepResult step_state(uint32_t state, int uv, int w) {
    const int m = 2 * w;
    const uint32_t mask = (1u << m) - 1u;
    const uint32_t x = state & mask;
    const uint32_t g = (state >> m) & mask;
    const int u = (uv >> 1) & 1;
    const int v = uv & 1;

    int V[32];
    V[0] = 0;
    for (int i = 0; i < m; ++i) V[i + 1] = V[i] + int((g >> i) & 1u);

    int Q[32];
    const int a0 = (int((x >> 0) & 1u) == v);
    Q[0] = std::max(V[1], V[0] + a0);
    for (int k = 1; k < m; ++k) {
        const int ak = (int((x >> k) & 1u) == v); // same incoming Y-bit v in the whole column
        int z = Q[k - 1];
        z = std::max(z, V[k] + ak);
        z = std::max(z, V[k + 1]);
        Q[k] = z;
    }
    const int am = (u == v);
    Q[m] = std::max(Q[m - 1], V[m] + am);

    uint32_t gp = 0;
    for (int i = 0; i < m; ++i) {
        if (Q[i + 1] - Q[i]) gp |= (1u << i);
    }
    const uint32_t xp = (x >> 1) | (uint32_t(u) << (m - 1));
    const uint8_t reward = uint8_t(Q[w] - V[w]);
    return {xp | (gp << m), reward};
}

struct Node {
    uint32_t next[4];
    uint8_t reward_sum;
};

int main() {
    constexpr int w = 6;
    constexpr int m = 12;
    constexpr int iterations = 180;
    constexpr int64_t SCALE = 1000000000000000LL;
    constexpr uint32_t BAD = 0xffffffffu;
    constexpr int64_t L_NUM = 99083249LL;
    constexpr int64_t L_DEN = 125000000LL;

    const size_t total_formal = size_t(1) << (2 * m);
    std::vector<uint32_t> index(total_formal, BAD);
    std::vector<uint32_t> states;
    std::vector<Node> nodes;
    states.reserve(6000000);
    nodes.reserve(6000000);

    // z0=(0^m;0^m). Earlier analytic reset lemma: A^m maps every formal state to z0.
    index[0] = 0;
    states.push_back(0);
    nodes.push_back({{0, 0, 0, 0}, 0});

    // Exact exhaustive BFS of the unique recurrent class reachable from z0.
    for (size_t head = 0; head < states.size(); ++head) {
        const uint32_t s = states[head];
        Node nd{};
        nd.reward_sum = 0;
        for (int uv = 0; uv < 4; ++uv) {
            const auto z = step_state(s, uv, w);
            nd.reward_sum += z.reward;
            uint32_t j = index[z.next];
            if (j == BAD) {
                j = uint32_t(states.size());
                index[z.next] = j;
                states.push_back(z.next);
                nodes.push_back({{0, 0, 0, 0}, 0});
            }
            nd.next[uv] = j;
        }
        nodes[head] = nd;
    }

    std::cerr << "reachable=" << states.size() << "\n";

    // Candidate generation only: relative value iteration in double precision.
    std::vector<double> h(states.size(), 0.0), hn(states.size(), 0.0);
    for (int it = 0; it < iterations; ++it) {
        for (size_t i = 0; i < states.size(); ++i) {
            const Node &nd = nodes[i];
            hn[i] = (double(nd.reward_sum)
                    + h[nd.next[0]] + h[nd.next[1]]
                    + h[nd.next[2]] + h[nd.next[3]]) / 4.0;
        }
        const double base = hn[0];
        for (double &z : hn) z -= base;
        h.swap(hn);
        if (it % 10 == 9) {
            auto mm = std::minmax_element(h.begin(), h.end());
            std::cerr << "iter=" << (it + 1)
                      << " base=" << std::setprecision(15) << base
                      << " range=[" << *mm.first << "," << *mm.second << "]\n";
        }
    }

    // Freeze the proposed potential as exact integers.
    std::vector<int64_t> H(states.size());
    int64_t Hmin = std::numeric_limits<int64_t>::max();
    int64_t Hmax = std::numeric_limits<int64_t>::min();
    for (size_t i = 0; i < states.size(); ++i) {
        H[i] = int64_t(std::llround(h[i] * double(SCALE)));
        Hmin = std::min(Hmin, H[i]);
        Hmax = std::max(Hmax, H[i]);
    }

    // Exact Bellman residual numerator:
    // D(s)=SCALE*sum_a rho(s,a)+sum_a H(T_a s)-4 H(s).
    // Therefore D(s)/(4*SCALE)=rbar(s)+P h(s)-h(s).
    int64_t min_num = std::numeric_limits<int64_t>::max();
    int64_t max_num = std::numeric_limits<int64_t>::min();
    uint32_t argmin = 0, argmax = 0;
    for (size_t i = 0; i < states.size(); ++i) {
        const Node &nd = nodes[i];
        const int64_t num = int64_t(nd.reward_sum) * SCALE
            + H[nd.next[0]] + H[nd.next[1]] + H[nd.next[2]] + H[nd.next[3]]
            - 4 * H[i];
        if (num < min_num) { min_num = num; argmin = uint32_t(i); }
        if (num > max_num) { max_num = num; argmax = uint32_t(i); }
    }

    const int64_t denom = 4 * SCALE;
    const __int128 lhs = __int128(max_num) * L_DEN;
    const __int128 rhs = __int128(denom) * L_NUM;
    const bool upper_lt_L = (lhs < rhs);

    std::cout << "w=" << w << " m=" << m
              << " reachable=" << states.size()
              << " iterations=" << iterations
              << " SCALE=" << SCALE << "\n";
    std::cout << "min_num=" << min_num
              << " max_num=" << max_num
              << " denom=" << denom << "\n";
    std::cout << std::setprecision(15)
              << "lower=" << double(min_num) / double(denom)
              << " upper=" << double(max_num) / double(denom)
              << " width=" << double(max_num - min_num) / double(denom) << "\n";
    std::cout << "argmin_state=" << states[argmin]
              << " argmax_state=" << states[argmax] << "\n";
    std::cout << "Hmin=" << Hmin << " Hmax=" << Hmax
              << " Hosc=" << (Hmax - Hmin)
              << " over_SCALE=" << SCALE << "\n";
    std::cout << "upper_lt_L=" << (upper_lt_L ? "YES" : "NO") << "\n";

    // For this executed certificate, both quantities have denominator 4e15:
    // L = 3170663968000000 / 4000000000000000.
    const int64_t L_scaled_num = 3170663968000000LL;
    if (denom != 4000000000000000LL || !upper_lt_L) return 2;
    std::cout << "L_minus_upper_num=" << (L_scaled_num - max_num)
              << " common_denom=" << denom << "\n";

    // The following values are not assumptions; they are exact consequences of the scan above.
    if (states.size() != 5735086ULL) return 3;
    if (min_num != 3119319222655621LL) return 4;
    if (max_num != 3119319222655638LL) return 5;
    if (Hmax - Hmin != 4140891766281466LL) return 6;

    std::cout << "ALL_EXACT_CHECKS_PASS\n";
    return 0;
}
