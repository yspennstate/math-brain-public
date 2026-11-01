#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <unordered_map>
#include <vector>

struct Key {
    std::array<std::uint16_t,33> z{}; // z[0]=number of classes; z[1..] sorted class codes
    bool operator==(Key const& o) const noexcept { return z==o.z; }
};
struct KeyHash {
    std::size_t operator()(Key const& k) const noexcept {
        std::uint64_t h=1469598103934665603ULL;
        for (std::uint16_t x: k.z) {
            h ^= x;
            h *= 1099511628211ULL;
        }
        return (std::size_t)h;
    }
};

static inline std::uint16_t encode_class(const std::array<unsigned char,6>& c) {
    // Mixed radices [2,6,11,11,6,2]; exact/injective since
    // 0<=c_k<=binom(5,k) = [1,5,10,10,5,1].
    unsigned v=c[0];
    v=v*6+c[1];
    v=v*11+c[2];
    v=v*11+c[3];
    v=v*6+c[4];
    v=v*2+c[5];
    if (v>=17424U) std::abort();
    return (std::uint16_t)v;
}

static inline Key signature(const std::array<int,5>& w) {
    struct Atom { int sum; unsigned char rank; };
    // 64 entries are allocated although only 32 are used; this keeps the
    // doubling construction simple while remaining statically bounds-safe.
    std::array<Atom,64> a{};
    a[0]={0,0};
    int filled=1;
    for (int i=0;i<5;i++) {
        const int old=filled;
        for (int j=0;j<old;j++) {
            a[old+j] = {a[j].sum+w[i], (unsigned char)(a[j].rank+1)};
        }
        filled*=2;
    }
    if (filled!=32) std::abort();
    std::sort(a.begin(),a.begin()+32,[](Atom const& x, Atom const& y){
        if (x.sum!=y.sum) return x.sum<y.sum;
        return x.rank<y.rank;
    });
    std::array<std::uint16_t,32> codes{};
    int nclass=0;
    for (int i=0;i<32;) {
        const int s=a[i].sum;
        std::array<unsigned char,6> c{};
        int j=i;
        while (j<32 && a[j].sum==s) {
            if (a[j].rank>5) std::abort();
            ++c[a[j].rank];
            ++j;
        }
        codes[nclass++]=encode_class(c);
        i=j;
    }
    std::sort(codes.begin(),codes.begin()+nclass);
    Key k;
    k.z[0]=(std::uint16_t)nclass;
    for (int i=0;i<nclass;i++) k.z[i+1]=codes[i];
    return k;
}

int main() {
    constexpr int B=80;
    std::unordered_map<Key,std::array<int,5>,KeyHash> reps;
    reps.reserve(512);
    std::uint64_t tuples=0;
    for (int a=1;a<=B;a++)
    for (int b=a;b<=B;b++)
    for (int c=b;c<=B;c++)
    for (int d=c;d<=B;d++)
    for (int e=d;e<=B;e++) {
        ++tuples;
        std::array<int,5> w{a,b,c,d,e};
        Key k=signature(w);
        reps.emplace(k,w);
    }
    // C(80+5-1,5) = C(84,5) = 30,872,016.
    if (tuples != 30872016ULL) {
        std::cerr << "FAIL tuple count: " << tuples << "\n";
        return 2;
    }
    if (reps.size()!=216U) {
        std::cerr << "FAIL signature count: " << reps.size() << "\n";
        return 3;
    }
    std::vector<std::array<int,5>> out;
    out.reserve(reps.size());
    for (auto const& kv: reps) out.push_back(kv.second);
    std::sort(out.begin(),out.end());
    std::cout << "PASS\n";
    std::cout << "bound_B = " << B << "\n";
    std::cout << "nondecreasing_positive_integer_5_tuples = " << tuples << "\n";
    std::cout << "entropy_signatures = " << reps.size() << "\n";
    std::cout << "class_code_mixed_radix_bound = 17424\n";
    std::cout << "signature_key_uses_full_exact_array_equality = true\n";
    std::cout << "representatives:\n";
    for (auto const& w: out) {
        std::cout << '(' << w[0] << ',' << w[1] << ',' << w[2] << ',' << w[3] << ',' << w[4] << ")\n";
    }
    return 0;
}
