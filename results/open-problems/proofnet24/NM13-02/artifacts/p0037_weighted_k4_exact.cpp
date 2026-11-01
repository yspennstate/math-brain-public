#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <numeric>
#include <set>
#include <unordered_set>
#include <utility>
#include <vector>

using namespace std;

// Exact finite certificate for NM13-02 / P0037.
//
// It proves the finite combinatorial core of:
//   For every assignment of positive edge weights to K4, the weighted UST
//   satisfies the BK inequality for all increasing events.
//
// No floating point arithmetic is used.

static const array<pair<int,int>,6> EDGES = {{{0,1},{0,2},{0,3},{1,2},{1,3},{2,3}}};

struct Event {
    vector<uint8_t> witnesses; // nonempty singleton/pair edge masks
    uint16_t occ = 0;          // which of the 16 K4 trees satisfy the event
    uint8_t singleton_mask = 0;
    array<uint16_t,64> L{};    // L[s]: trees with an event witness disjoint from some singleton in s
};

struct Cell {
    // Exponent vector of a degree-6 monomial, encoded base 3.
    int code = 0;
    array<uint8_t,6> exp{};
    uint16_t U = 0;                 // second-tree indices occurring in this product cell
    array<int8_t,16> partner{};     // for each u in U, unique first-tree index t
};

int pop16(uint16_t x) { return __builtin_popcount((unsigned)x); }

bool is_tree_mask(uint8_t mask) {
    if (__builtin_popcount((unsigned)mask) != 3) return false;
    int p[4] = {0,1,2,3};
    auto find = [&](int x) {
        int y=x;
        while (p[y]!=y) y=p[y];
        while (p[x]!=x) { int z=p[x]; p[x]=y; x=z; }
        return y;
    };
    for (int e=0;e<6;e++) if ((mask>>e)&1) {
        auto [u,v]=EDGES[e];
        int a=find(u), b=find(v);
        if (a==b) return false;
        p[a]=b;
    }
    return true;
}

int encode_exp(const array<uint8_t,6>& a) {
    int code=0, mul=1;
    for (int i=0;i<6;i++) { code += mul*a[i]; mul*=3; }
    return code;
}

array<uint8_t,6> decode_exp(int code) {
    array<uint8_t,6> a{};
    for (int i=0;i<6;i++) { a[i]=code%3; code/=3; }
    return a;
}

uint8_t permute_edge_mask(uint8_t mask, const array<int,4>& p) {
    uint8_t out=0;
    for (int e=0;e<6;e++) if ((mask>>e)&1) {
        int a=p[EDGES[e].first], b=p[EDGES[e].second];
        if (a>b) swap(a,b);
        int ee=-1;
        for (int j=0;j<6;j++) if (EDGES[j]==make_pair(a,b)) { ee=j; break; }
        assert(ee>=0);
        out |= uint8_t(1u<<ee);
    }
    return out;
}

int main() {
    // 1. Enumerate all 16 spanning trees of K4.
    vector<uint8_t> trees;
    for (int m=0;m<64;m++) if (is_tree_mask((uint8_t)m)) trees.push_back((uint8_t)m);
    assert(trees.size()==16);

    // Map tree edge-mask to tree index.
    array<int8_t,64> tree_index; tree_index.fill(-1);
    for (int i=0;i<16;i++) tree_index[trees[i]]=i;

    // Containment masks for every singleton/pair witness.
    array<uint16_t,64> contain{};
    for (int q=1;q<64;q++) if (__builtin_popcount((unsigned)q)<=2) {
        uint16_t cm=0;
        for (int t=0;t<16;t++) if ((trees[t]&q)==q) cm |= uint16_t(1u<<t);
        contain[q]=cm;
    }

    // 2. Enumerate every reduced nontrivial increasing event.
    // An antichain consists of arbitrary singleton witnesses S and arbitrary
    // pair witnesses avoiding S. This is unique for rank 3 after deleting
    // redundant witnesses.
    vector<uint8_t> pairs;
    for (int i=0;i<6;i++) for (int j=i+1;j<6;j++) pairs.push_back(uint8_t((1u<<i)|(1u<<j)));

    vector<Event> events;
    for (int sm=0;sm<64;sm++) {
        vector<uint8_t> singles;
        for (int i=0;i<6;i++) if ((sm>>i)&1) singles.push_back(uint8_t(1u<<i));
        vector<uint8_t> allowed_pairs;
        for (uint8_t q:pairs) if ((q&sm)==0) allowed_pairs.push_back(q);
        const int total = 1 << allowed_pairs.size();
        for (int choice=0;choice<total;choice++) {
            Event e;
            e.singleton_mask=(uint8_t)sm;
            e.witnesses=singles;
            for (int j=0;j<(int)allowed_pairs.size();j++) if ((choice>>j)&1)
                e.witnesses.push_back(allowed_pairs[j]);
            if (e.witnesses.empty()) continue; // whole-space/empty-witness case is trivial separately
            for (uint8_t q:e.witnesses) e.occ |= contain[q];
            if (!e.occ) continue;

            array<uint16_t,6> q_without_edge{};
            for (int edge=0;edge<6;edge++) {
                uint16_t v=0;
                for (uint8_t q:e.witnesses) if ((q&(1u<<edge))==0) v |= contain[q];
                q_without_edge[edge]=v;
            }
            for (int s=0;s<64;s++) {
                uint16_t v=0;
                for (int edge=0;edge<6;edge++) if ((s>>edge)&1)
                    v |= contain[1u<<edge] & q_without_edge[edge];
                e.L[s]=v;
            }
            events.push_back(std::move(e));
        }
    }
    assert(events.size()==40068);

    // 3. Exact S4 orbit count for B14.
    vector<array<int,4>> perms;
    array<int,4> p={0,1,2,3};
    do { perms.push_back(p); } while (next_permutation(p.begin(),p.end()));
    assert(perms.size()==24);

    auto event_key = [](const vector<uint8_t>& w) {
        // witnesses are <=63, sorted key in a 128-bit-like pair of uint64s is inconvenient;
        // use a byte string for an exact hash key.
        string s; s.reserve(w.size());
        for (uint8_t x:w) s.push_back(char(x));
        return s;
    };
    unordered_set<string> all_event_keys;
    all_event_keys.reserve(events.size()*2);
    for (const auto& e:events) {
        vector<uint8_t> w=e.witnesses; sort(w.begin(),w.end());
        all_event_keys.insert(event_key(w));
    }
    unordered_set<string> seen_events;
    seen_events.reserve(events.size()*2);
    int event_orbits=0;
    for (const auto& e:events) {
        vector<uint8_t> base=e.witnesses; sort(base.begin(),base.end());
        string bk=event_key(base);
        if (seen_events.count(bk)) continue;
        event_orbits++;
        for (const auto& pp:perms) {
            vector<uint8_t> w;
            for (uint8_t q:e.witnesses) w.push_back(permute_edge_mask(q,pp));
            sort(w.begin(),w.end());
            string k=event_key(w);
            assert(all_event_keys.count(k));
            seen_events.insert(k);
        }
    }
    assert(seen_events.size()==events.size());
    assert(event_orbits==1958);

    // 4. Build the 101 product-monomial cells of F_A F_B and Z F_square.
    map<int,Cell> cmap;
    for (int ti=0;ti<16;ti++) for (int ui=0;ui<16;ui++) {
        array<uint8_t,6> ex{};
        for (int e=0;e<6;e++) ex[e]=uint8_t(((trees[ti]>>e)&1)+((trees[ui]>>e)&1));
        int code=encode_exp(ex);
        if (!cmap.count(code)) {
            Cell c; c.code=code; c.exp=ex; c.partner.fill(-1); cmap[code]=c;
        }
        Cell& c=cmap[code];
        c.U |= uint16_t(1u<<ui);
        if (c.partner[ui]>=0) assert(c.partner[ui]==ti);
        c.partner[ui]=ti;
    }
    assert(cmap.size()==101);

    vector<Cell> cells; cells.reserve(cmap.size());
    map<int,int> cell_index;
    for (auto &kv:cmap) { cell_index[kv.first]=cells.size(); cells.push_back(kv.second); }

    array<uint8_t,6> alpha{}; alpha.fill(1);
    const int center_code=encode_exp(alpha);
    const int center_idx=cell_index.at(center_code);
    assert(cells[center_idx].U && pop16(cells[center_idx].U)==12);

    // 5. Compute S4 orbits of product cells. There must be 9; checking one representative
    // for every event pair suffices for coefficient sign away from the S4-fixed center.
    auto permute_exp = [&](const array<uint8_t,6>& ex, const array<int,4>& pp) {
        array<uint8_t,6> out{};
        for (int e=0;e<6;e++) {
            uint8_t one=uint8_t(1u<<e);
            uint8_t pe=permute_edge_mask(one,pp);
            int j=__builtin_ctz((unsigned)pe);
            out[j]=ex[e];
        }
        return out;
    };
    set<int> unseen;
    for (auto &c:cells) unseen.insert(c.code);
    vector<int> reps;
    while (!unseen.empty()) {
        int code=*unseen.begin();
        reps.push_back(cell_index.at(code));
        auto ex=decode_exp(code);
        for (const auto& pp:perms) {
            int pc=encode_exp(permute_exp(ex,pp));
            assert(cell_index.count(pc));
            unseen.erase(pc);
        }
    }
    assert(reps.size()==9);

    // Precompute, for every cell and event A, the bit mask of second-tree indices u
    // whose unique partner t in that cell satisfies A.
    const int N=events.size(), C=cells.size();
    vector<uint16_t> apart((size_t)C*N);
    for (int ci=0;ci<C;ci++) {
        const Cell& c=cells[ci];
        for (int a=0;a<N;a++) {
            uint16_t m=0;
            uint16_t U=c.U;
            while (U) {
                int u=__builtin_ctz((unsigned)U); U &= uint16_t(U-1);
                int t=c.partner[u]; assert(t>=0);
                if ((events[a].occ>>t)&1) m |= uint16_t(1u<<u);
            }
            apart[(size_t)ci*N+a]=m;
        }
    }

    auto coeff = [&](int ci, int a, int b, uint16_t square_mask) {
        const Cell& c=cells[ci];
        int first=pop16(apart[(size_t)ci*N+a] & events[b].occ);
        int second=pop16(c.U & square_mask);
        return first-second;
    };

    // Complementary exponent-cell pairs beta,gamma with beta+gamma=2*alpha.
    vector<pair<int,int>> complementary;
    for (int ci=0;ci<C;ci++) {
        if (ci==center_idx) continue;
        array<uint8_t,6> ex2{};
        for (int e=0;e<6;e++) ex2[e]=uint8_t(2-cells[ci].exp[e]);
        int cc=encode_exp(ex2);
        if (!cell_index.count(cc)) continue;
        int cj=cell_index.at(cc);
        if (ci<cj) complementary.push_back({ci,cj});
    }
    assert(complementary.size()==36);

    // 6. Exhaustive exact certificate over all ordered reduced-event pairs.
    // For noncenter coefficients, S4 orbit representatives suffice.
    vector<int> noncenter_reps;
    for (int r:reps) if (r!=center_idx) noncenter_reps.push_back(r);
    assert(noncenter_reps.size()==8);

    array<long long,3> center_negative_count{}; // index 1,2
    long long negative_center_total=0;
    int minimum_center=100;
    array<int,8> min_noncenter; min_noncenter.fill(100);
    long long ordered_pairs=0;
    long long certified_negative_pairs=0;

    for (int a=0;a<N;a++) {
        // preload first-event data used for all b
        const uint8_t sa=events[a].singleton_mask;
        for (int b=0;b<N;b++) {
            ordered_pairs++;
            uint16_t square_mask = events[a].L[events[b].singleton_mask] | events[b].L[sa];

            for (int r=0;r<8;r++) {
                int c=coeff(noncenter_reps[r],a,b,square_mask);
                if (c<min_noncenter[r]) min_noncenter[r]=c;
                if (c<0) {
                    cerr << "NEGATIVE_NONCENTER_COEFF a="<<a<<" b="<<b<<" rep="<<r<<" c="<<c<<"\n";
                    return 3;
                }
            }

            int c0=coeff(center_idx,a,b,square_mask);
            minimum_center=min(minimum_center,c0);
            if (c0<0) {
                const int k=-c0;
                if (k>2) {
                    cerr << "CENTER_BELOW_MINUS2 a="<<a<<" b="<<b<<" c="<<c0<<"\n";
                    return 4;
                }
                negative_center_total++;
                center_negative_count[k]++;

                bool certified=false;
                for (auto [ci,cj]:complementary) {
                    int x=coeff(ci,a,b,square_mask);
                    int y=coeff(cj,a,b,square_mask);
                    if (x<0 || y<0) {
                        cerr << "NEGATIVE_COMPLEMENT_COEFF a="<<a<<" b="<<b<<"\n";
                        return 5;
                    }
                    // AM-GM: x m_beta + y m_gamma >= 2 sqrt(xy) m_alpha.
                    // The integer inequality 4xy >= k^2 certifies domination of k*m_alpha.
                    if (x>0 && y>0 && 4*x*y >= k*k) { certified=true; break; }
                }
                if (!certified) {
                    cerr << "NO_AMGM_CERTIFICATE a="<<a<<" b="<<b<<" center="<<c0<<"\n";
                    return 6;
                }
                certified_negative_pairs++;
            }
        }
    }

    assert(ordered_pairs==1LL*N*N);
    assert(minimum_center==-2);
    assert(center_negative_count[1]==17796);
    assert(center_negative_count[2]==1650);
    assert(negative_center_total==19446);
    assert(certified_negative_pairs==negative_center_total);
    for (int x:min_noncenter) assert(x==0);

    cout << "K4_SPANNING_TREES=16\n";
    cout << "REDUCED_EVENTS=" << N << "\n";
    cout << "S4_EVENT_ORBITS=" << event_orbits << "\n";
    cout << "PRODUCT_MONOMIAL_CELLS=" << C << "\n";
    cout << "S4_CELL_ORBITS=" << reps.size() << "\n";
    cout << "COMPLEMENTARY_CELL_PAIRS=" << complementary.size() << "\n";
    cout << "ORDERED_EVENT_PAIRS=" << ordered_pairs << "\n";
    cout << "NONCENTER_ORBIT_MIN_COEFFICIENTS=";
    for (int i=0;i<8;i++) cout << (i?",":"") << min_noncenter[i];
    cout << "\n";
    cout << "CENTER_MIN_COEFFICIENT=" << minimum_center << "\n";
    cout << "CENTER_NEGATIVE_MINUS1=" << center_negative_count[1] << "\n";
    cout << "CENTER_NEGATIVE_MINUS2=" << center_negative_count[2] << "\n";
    cout << "CENTER_NEGATIVE_TOTAL=" << negative_center_total << "\n";
    cout << "AMGM_CERTIFIED_NEGATIVE_CENTER_PAIRS=" << certified_negative_pairs << "\n";
    cout << "ALL_EXACT_CHECKS_PASS\n";
    return 0;
}
