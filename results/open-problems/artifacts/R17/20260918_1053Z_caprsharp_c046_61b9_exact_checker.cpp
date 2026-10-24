#include <bits/stdc++.h>
using namespace std;

struct PairBits { uint64_t a=0,b=0; int al=0, bl=0; };

static PairBits build_pair(const vector<int>& c,const vector<int>& l){
    PairBits p; int r=(int)c.size();
    auto pa=[&](int x){ if(x) p.a |= 1ULL<<p.al; ++p.al; };
    auto pb=[&](int x){ if(x) p.b |= 1ULL<<p.bl; ++p.bl; };
    for(int i=0;i<r;i++){
        int d=1-c[i];
        if(l[i]>=0){ for(int q=0;q<l[i];q++) pa(d); pa(c[i]); pb(c[i]); }
        else { pa(c[i]); for(int q=0;q<-l[i];q++) pb(d); pb(c[i]); }
    }
    return p;
}

static int lcs_len(PairBits p){
    if(p.bl>=64){ cerr << "bit width overflow\n"; exit(10); }
    uint64_t full=(p.bl==64)?~0ULL:((1ULL<<p.bl)-1);
    uint64_t m1=p.b, m0=(~p.b)&full, S=0;
    for(int i=0;i<p.al;i++){
        uint64_t m=((p.a>>i)&1ULL)?m1:m0;
        uint64_t x=m|S, y=(S<<1)|1ULL;
        S=x & ~(x-y);
    }
    return __builtin_popcountll(S);
}

static int sid(int c,int l){ return c*3+(l+1); }
static pair<int,int> unsid(int z){ return {z/3,(z%3)-1}; }

int main(){
    for(int r=2;r<=7;r++){
        vector<int> c(r,0), orig(r,0), capr(r,0), caprm1(r,0);
        orig.front()=r+1; orig.back()=-(r+1);
        capr.front()=r; capr.back()=-r;
        caprm1.front()=r-1; caprm1.back()=-(r-1);
        int Lo=lcs_len(build_pair(c,orig));
        int Lr=lcs_len(build_pair(c,capr));
        int Lm=lcs_len(build_pair(c,caprm1));
        if(!(Lo>=r+1 && Lr>=r+1 && Lm==r)){
            cerr << "sharpness family failure r="<<r<<" "<<Lo<<" "<<Lr<<" "<<Lm<<"\n";
            return 2;
        }
        cout << "sharp_r="<<r<<" original_lcs="<<Lo<<" cap_r_lcs="<<Lr<<" cap_r_minus_1_lcs="<<Lm<<"\n";
    }
    cout << "EXACT_CAP_R_SHARPNESS_FAMILY_PASS\n";

    const long long TOTAL=279936; // 6^7
    vector<unsigned char> ismin(TOTAL,0);
    long long cnt=0;
    for(long long code=0; code<TOTAL; ++code){
        long long t=code; vector<int> z(7),c(7),l(7);
        for(int i=6;i>=0;i--){ z[i]=(int)(t%6); t/=6; tie(c[i],l[i])=unsid(z[i]); }
        if(lcs_len(build_pair(c,l))<=7) continue;
        vector<int> cp(c.begin(),c.begin()+6), lp(l.begin(),l.begin()+6);
        vector<int> cs(c.begin()+1,c.end()), ls(l.begin()+1,l.end());
        if(lcs_len(build_pair(cp,lp))>6 || lcs_len(build_pair(cs,ls))>6) continue;
        ismin[code]=1; ++cnt;
    }
    if(cnt!=3156){ cerr << "unexpected minimal7 count "<<cnt<<"\n"; return 3; }

    auto encode=[&](const vector<int>& z){ long long q=0; for(int x:z)q=q*6+x; return q; };
    for(long long code=0; code<TOTAL; ++code) if(ismin[code]){
        long long t=code; vector<int> z(7);
        for(int i=6;i>=0;i--){z[i]=(int)(t%6);t/=6;}
        vector<int> zc(7),zs(7);
        for(int i=0;i<7;i++){
            auto [c,l]=unsid(z[i]);
            zc[i]=sid(1-c,l);
            zs[i]=sid(c,-l);
        }
        if(!ismin[encode(zc)] || !ismin[encode(zs)]){
            cerr << "symmetry closure failure\n"; return 4;
        }
    }
    cout << "small_alphabet={c in {0,1}, l in {-1,0,1}}\n";
    cout << "seven_factor_words_checked="<<TOTAL<<"\n";
    cout << "minimal_deficient_seven_small_alphabet="<<cnt<<"\n";
    cout << "EXACT_MIN7_SMALL_ALPHABET_COUNT_PASS\n";
    cout << "EXACT_COMPLEMENT_SWAP_CLOSURE_PASS\n";
    cout << "ALL_EXACT_CHECKS_PASS\n";
}
