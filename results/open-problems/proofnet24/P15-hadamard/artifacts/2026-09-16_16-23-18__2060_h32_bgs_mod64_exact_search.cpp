#include <bits/stdc++.h>
using namespace std;

/*
Exact restricted-family checker for P15 Hadamard, target order 2060.

We seek H32-invariant cyclic supplementary difference families in Z_514
with block sizes (256,257,257,257) and lambda 512. The H32 subgroup is
<393> in Z_514^*, of order 32.

The final meet-in-the-middle test uses a deterministic additive map
    h(s) = sum_r w_r s_r   (mod 2^64)
from the 17-coordinate integer difference-signature lattice to Z/(2^64).
This is an exact necessary-condition projection: an exact signature equality
must give the same h-value. Therefore if no required h-value appears in the
complete table of B+B projected sums, exact equality is impossible. Hash
collisions can only create false positives (hits), never false negatives.
The program treats any hit as INCONCLUSIVE unless exact coordinates match.
In the executed run there are zero hits in every exact last-coordinate bucket.
*/

static constexpr int V = 514;
static constexpr int NORB = 16;
static constexpr int R = 17;

struct SigRec {
    array<int,R> s{};
    uint16_t mask{};
};

static inline uint64_t mix64(uint64_t x) {
    x ^= x >> 30;
    x *= 0xbf58476d1ce4e5b9ULL;
    x ^= x >> 27;
    x *= 0x94d049bb133111ebULL;
    x ^= x >> 31;
    return x;
}

static int modpow(int a, int e) {
    long long r=1, b=a;
    while(e){ if(e&1) r=r*b%V; b=b*b%V; e>>=1; }
    return (int)r;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    const int gen = 393;
    vector<int> H;
    int x=1;
    for(int k=0;k<32;k++) { H.push_back(x); x=(long long)x*gen%V; }
    set<int> Hset(H.begin(),H.end());
    if(Hset.size()!=32 || x!=1 || modpow(gen,16)==1) {
        cerr << "FAIL subgroup order check\n";
        return 2;
    }

    vector<int> orbit_id(V,-1);
    vector<vector<int>> all_orbits;
    for(int a=0;a<V;a++) if(orbit_id[a]<0) {
        set<int> S;
        for(int h:H) S.insert((long long)h*a%V);
        vector<int> o(S.begin(),S.end());
        int id=(int)all_orbits.size();
        for(int y:o) orbit_id[y]=id;
        all_orbits.push_back(o);
    }
    map<int,int> orbit_profile;
    for(auto &o:all_orbits) orbit_profile[(int)o.size()]++;
    if(orbit_profile[1]!=2 || orbit_profile[32]!=16 || (int)all_orbits.size()!=18) {
        cerr << "FAIL orbit profile\n";
        return 2;
    }

    vector<vector<int>> O;
    vector<int> elem_orbit(V,-1);
    vector<int> fixed;
    for(auto &o:all_orbits) {
        if(o.size()==32) {
            int id=(int)O.size();
            O.push_back(o);
            for(int y:o) elem_orbit[y]=id;
        } else if(o.size()==1) fixed.push_back(o[0]);
    }
    sort(fixed.begin(),fixed.end());
    if(fixed != vector<int>({0,257})) {
        cerr << "FAIL fixed points\n";
        return 2;
    }

    vector<char> seen(V,0);
    vector<int> reps;
    vector<int> shift_orbit_size;
    for(int t=1;t<V;t++) if(!seen[t]) {
        set<int> S;
        for(int h:H) S.insert((long long)h*t%V);
        for(int y:S) seen[y]=1;
        reps.push_back(*S.begin());
        shift_orbit_size.push_back((int)S.size());
    }
    if((int)reps.size()!=R) {
        cerr << "FAIL nonzero shift orbit count\n";
        return 2;
    }
    int singleton_count=0;
    for(int z:shift_orbit_size) singleton_count += (z==1);
    if(singleton_count!=1 || reps.back()!=257) {
        cerr << "FAIL nonzero shift orbit profile\n";
        return 2;
    }

    static int C[R][NORB][NORB];
    static int fixed0_linear[R][NORB];
    for(int r=0;r<R;r++) {
        int t=reps[r];
        for(int i=0;i<NORB;i++) {
            for(int a:O[i]) {
                int b=(a+t)%V;
                int j=elem_orbit[b];
                if(j>=0) C[r][i][j]++;
            }
        }
        for(int z : {t,(V-t)%V}) {
            int j=elem_orbit[z];
            if(j>=0) fixed0_linear[r][j]++;
        }
    }

    auto formula_sig = [&](uint16_t mask, bool include0) {
        array<int,R> s{};
        for(int r=0;r<R;r++) {
            int q=0;
            for(int i=0;i<NORB;i++) if(mask>>i&1) {
                q += C[r][i][i];
                if(include0) q += fixed0_linear[r][i];
                for(int j=i+1;j<NORB;j++) if(mask>>j&1)
                    q += C[r][i][j] + C[r][j][i];
            }
            s[r]=q;
        }
        return s;
    };

    auto direct_sig = [&](uint16_t mask, bool include0) {
        array<int,R> s{};
        vector<char> in(V,0);
        if(include0) in[0]=1;
        for(int i=0;i<NORB;i++) if(mask>>i&1)
            for(int a:O[i]) in[a]=1;
        int expected = include0 ? 257 : 256;
        int cnt=0; for(char b:in) cnt+=b;
        if(cnt!=expected) throw runtime_error("wrong candidate size");
        for(int r=0;r<R;r++) {
            int t=reps[r], q=0;
            for(int a=0;a<V;a++) if(in[a] && in[(a+t)%V]) q++;
            s[r]=q;
        }
        return s;
    };

    map<array<int,R>,uint16_t> Amap, Bmap;
    long long raw_masks=0;
    for(unsigned m=0;m<(1u<<NORB);m++) if(__builtin_popcount(m)==8) {
        raw_masks++;
        auto af=formula_sig((uint16_t)m,false);
        auto ad=direct_sig((uint16_t)m,false);
        auto bf=formula_sig((uint16_t)m,true);
        auto bd=direct_sig((uint16_t)m,true);
        if(af!=ad || bf!=bd) {
            cerr << "FAIL signature cross-check mask=" << m << "\n";
            return 2;
        }
        Amap.emplace(af,(uint16_t)m);
        Bmap.emplace(bf,(uint16_t)m);
    }
    if(raw_masks!=12870) {
        cerr << "FAIL 8-of-16 count\n";
        return 2;
    }

    for(unsigned m=0;m<(1u<<NORB);m++) if(__builtin_popcount(m)==8) {
        uint16_t cm = (uint16_t)(~m) & 0xFFFFu;
        auto sX = direct_sig((uint16_t)m,true);
        vector<char> in(V,0);
        in[257]=1;
        for(int i=0;i<NORB;i++) if(cm>>i&1)
            for(int a:O[i]) in[a]=1;
        array<int,R> sC{};
        for(int r=0;r<R;r++) {
            int t=reps[r], q=0;
            for(int a=0;a<V;a++) if(in[a] && in[(a+t)%V]) q++;
            sC[r]=q;
        }
        if(sX!=sC) {
            cerr << "FAIL complement-signature identity mask=" << m << "\n";
            return 2;
        }
    }

    vector<SigRec> A,B;
    A.reserve(Amap.size()); B.reserve(Bmap.size());
    for(auto &kv:Amap) A.push_back({kv.first,kv.second});
    for(auto &kv:Bmap) B.push_back({kv.first,kv.second});

    array<uint64_t,R> w{};
    uint64_t state=1234567891234567ULL;
    for(int r=0;r<R;r++) {
        state += 0x9e3779b97f4a7c15ULL;
        w[r] = mix64(state) | 1ULL;
    }
    auto Hsig = [&](const array<int,R>& s) {
        uint64_t h=0;
        for(int r=0;r<R;r++) h += (uint64_t)(uint32_t)s[r] * w[r];
        return h;
    };
    vector<uint64_t> hA(A.size()), hB(B.size());
    for(size_t i=0;i<A.size();i++) hA[i]=Hsig(A[i].s);
    for(size_t i=0;i<B.size();i++) hB[i]=Hsig(B[i].s);
    uint64_t hTarget=0;
    for(int r=0;r<R;r++) hTarget += (uint64_t)512 * w[r];

    map<int,vector<int>> bucketA,bucketB;
    for(int i=0;i<(int)A.size();i++) bucketA[A[i].s[R-1]].push_back(i);
    for(int i=0;i<(int)B.size();i++) bucketB[B[i].s[R-1]].push_back(i);

    cout << "target_order=2060\n";
    cout << "cyclic_length_v=514\n";
    cout << "multiplier_generator=" << gen << "\n";
    cout << "multiplier_subgroup_order=32\n";
    cout << "orbit_profile_size1=" << orbit_profile[1] << "\n";
    cout << "orbit_profile_size32=" << orbit_profile[32] << "\n";
    cout << "fixed_points=0,257\n";
    cout << "nonzero_shift_orbit_count=" << reps.size() << "\n";
    cout << "nonzero_shift_representatives=";
    for(size_t i=0;i<reps.size();i++) cout << (i?",":"") << reps[i];
    cout << "\n";
    cout << "raw_A_candidate_count=12870\n";
    cout << "raw_B_candidate_count=25740\n";
    cout << "fixed0_B_representative_count=12870\n";
    cout << "unique_A_signature_count=" << A.size() << "\n";
    cout << "unique_B_signature_count=" << B.size() << "\n";
    cout << "all_formula_vs_direct_signature_checks=PASSED\n";
    cout << "all_fixed0_vs_fixed257_complement_signature_checks=PASSED\n";
    cout << "projection_ring=Z/(2^64)\n";
    cout << "projection_weights_hex=";
    for(int r=0;r<R;r++) {
        if(r) cout << ",";
        cout << hex << setw(16) << setfill('0') << w[r] << dec << setfill(' ');
    }
    cout << "\n";

    long long total_pairs=0, total_probes=0, total_hits=0;
    for(int lastSum=0; lastSum<=512; lastSum+=64) {
        size_t pairRecords=0;
        for(auto &gx:bucketB) {
            int y=lastSum-gx.first;
            auto it=bucketB.find(y);
            if(it==bucketB.end() || gx.first>y) continue;
            size_t nx=gx.second.size(), ny=it->second.size();
            pairRecords += (gx.first<y) ? nx*ny : nx*(nx+1)/2;
        }
        total_pairs += (long long)pairRecords;

        size_t cap=1;
        while(cap < pairRecords*2 + 1) cap <<= 1;
        vector<uint64_t> keys(cap,0);
        vector<uint8_t> used(cap,0);
        size_t distinctResidues=0;
        auto insertResidue = [&](uint64_t h) {
            size_t p=mix64(h)&(cap-1);
            while(used[p]) {
                if(keys[p]==h) return;
                p=(p+1)&(cap-1);
            }
            used[p]=1; keys[p]=h; distinctResidues++;
        };
        auto hasResidue = [&](uint64_t h) {
            size_t p=mix64(h)&(cap-1);
            while(used[p]) {
                if(keys[p]==h) return true;
                p=(p+1)&(cap-1);
            }
            return false;
        };

        for(auto &gx:bucketB) {
            int y=lastSum-gx.first;
            auto it=bucketB.find(y);
            if(it==bucketB.end() || gx.first>y) continue;
            auto &X=gx.second; auto &Y=it->second;
            if(gx.first<y) {
                for(int i:X) for(int j:Y) insertResidue(hB[i]+hB[j]);
            } else {
                for(size_t p=0;p<X.size();p++)
                    for(size_t q=p;q<X.size();q++)
                        insertResidue(hB[X[p]]+hB[X[q]]);
            }
        }

        long long probes=0,hits=0;
        int needABLast=512-lastSum;
        for(auto &gx:bucketA) {
            int bLast=needABLast-gx.first;
            auto it=bucketB.find(bLast);
            if(it==bucketB.end()) continue;
            for(int ia:gx.second) for(int ib:it->second) {
                probes++;
                uint64_t needed = hTarget - hA[ia] - hB[ib];
                if(hasResidue(needed)) hits++;
            }
        }
        total_probes += probes; total_hits += hits;
        cout << "bucket_last_BB=" << lastSum
             << " Bpair_records=" << pairRecords
             << " distinct_projected_BB_residues=" << distinctResidues
             << " AB_complement_probes=" << probes
             << " projected_hits=" << hits << "\n";
        if(hits!=0) {
            cout << "INCONCLUSIVE: projected hit(s) occurred; exact collision resolution required.\n";
            return 3;
        }
    }

    cout << "total_Bpair_records=" << total_pairs << "\n";
    cout << "total_AB_complement_probes=" << total_probes << "\n";
    cout << "total_projected_hits=" << total_hits << "\n";
    cout << "EXACT_CERTIFICATE_PASSED: projected sumsets are disjoint in every exact last-coordinate bucket.\n";
    cout << "PROVED_RESTRICTED: no H32-invariant cyclic BGS difference family (514;256,257,257,257;512).\n";
    cout << "SCOPE: restricted-family nonexistence only; no claim about unrestricted H(2060).\n";
    return 0;
}
