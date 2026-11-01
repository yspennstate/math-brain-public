#include <boost/multiprecision/cpp_int.hpp>
#include <bits/stdc++.h>
using namespace std;
using boost::multiprecision::cpp_int;
using u256=boost::multiprecision::number<boost::multiprecision::cpp_int_backend<256,256,boost::multiprecision::unsigned_magnitude,boost::multiprecision::unchecked,void>>;
using u128=__uint128_t;

static uint64_t mod_cpp(const cpp_int& x,uint64_t m){ return (uint64_t)(x%m); }
static uint64_t mulmod(uint64_t x,uint64_t y,uint64_t m){ return (uint64_t)((u128)x*y%m); }
struct MixHash {
    size_t operator()(uint64_t x) const noexcept {
        x += 0x9e3779b97f4a7c15ULL;
        x=(x^(x>>30))*0xbf58476d1ce4e5b9ULL;
        x=(x^(x>>27))*0x94d049bb133111ebULL;
        return x^(x>>31);
    }
};

int main(){
    const uint64_t p=256717, q=800000, d=q-p;
    const uint64_t b=4220452010631561279ULL;
    const uint64_t M=5000000000000000000ULL;
    const cpp_int a("1995237757733917147310102692686664915858011319606812684127301");
    const uint64_t alpha=mod_cpp(a,b);
    // Exact inverse of alpha modulo b, independently checked below.
    const uint64_t h=707440146652911839ULL;
    if(mulmod(alpha,h,b)!=1){ cerr<<"inverse check failed\n"; return 2; }
    const uint64_t vstar=h+b;
    if(!(vstar<=M && M<2*b)){ cerr<<"witness-range check failed\n"; return 3; }
    const cpp_int Dfloor=a/vstar;
    const cpp_int Drem=a%vstar;
    if(Drem==0){ cerr<<"Dstar unexpectedly integral\n"; return 4; }

    u256 c[8];
    for(int k=0;k<=6;k++){
        u256 qq=1,pp=1;
        for(int j=0;j<6-k;j++) qq*=q;
        for(int j=0;j<k;j++) pp*=p;
        c[k]=qq*d*pp;
    }
    c[7]=1; for(int j=0;j<7;j++) c[7]*=p;
    const u256 D_R=c[0]+c[3]+c[6]+c[7];
    const u256 D_C=D_R+u256(2200)*c[7]+1;
    const u256 Dlim=Dfloor.convert_to<u256>();
    if(!(Dlim>D_C)){ cerr<<"new floor does not improve old defect\n"; return 5; }

    // Tight-row relaxation inherited from the four-band theorem:
    // T=sum c_k S_k, S0>=1, S7>=1,
    // S1+S2+S3>=1, S4+S5+S6>=1, and T == a^2 (mod b).
    // We prove there is no such T <= floor(a/vstar).
    uint64_t cm[8]; for(int k=0;k<8;k++) cm[k]=(uint64_t)(c[k]%b);
    const uint64_t target=mod_cpp(a*a,b);

    // Meet-in-the-middle compression: precompute every feasible (S6,S7)
    // pair under the largest possible remaining budget.  The mandatory
    // S0 and {1,2,3} bands cost at least c0+c3.
    const u256 Rmax=Dlim-c[0]-c[3];
    const uint64_t max6=(uint64_t)(Rmax/c[6]);
    unordered_map<uint64_t,uint32_t,MixHash> any,pos;
    any.reserve(4000000); pos.reserve(4000000);
    any.max_load_factor(0.75); pos.max_load_factor(0.75);
    auto paircost=[&](uint32_t code)->u256{
        uint64_t s6=code>>16, s7=code&0xffff;
        return c[6]*s6+c[7]*s7;
    };
    uint64_t pair_count=0, duplicate_residues=0;
    for(uint64_t s6=0;s6<=max6;s6++){
        const u256 rem=Rmax-c[6]*s6;
        const uint64_t max7=(uint64_t)(rem/c[7]);
        uint64_t residue=mulmod(cm[6],s6,b)+cm[7];
        if(residue>=b) residue-=b;
        for(uint64_t s7=1;s7<=max7;s7++){
            const uint32_t code=(uint32_t)((s6<<16)|s7);
            ++pair_count;
            auto update=[&](auto& mp){
                auto it=mp.find(residue);
                if(it==mp.end()) mp.emplace(residue,code);
                else {
                    ++duplicate_residues;
                    if(paircost(code)<paircost(it->second)) it->second=code;
                }
            };
            update(any);
            if(s6>=1) update(pos);
            residue+=cm[7]; if(residue>=b) residue-=b;
        }
    }

    bool found=false;
    u256 best=0;
    array<uint64_t,8> bestS{};
    uint64_t prefix_count=0, lookup_count=0;
    const uint64_t max0=(uint64_t)(Dlim/c[0]);
    for(uint64_t s0=1;s0<=max0;s0++){
        const u256 t0=c[0]*s0;
        const uint64_t r0=mulmod(cm[0],s0,b);
        const uint64_t max1=(uint64_t)((Dlim-t0-c[7])/c[1]);
        for(uint64_t s1=0;s1<=max1;s1++){
            const u256 t1=t0+c[1]*s1;
            const uint64_t r1=(r0+mulmod(cm[1],s1,b))%b;
            const uint64_t max2=(uint64_t)((Dlim-t1-c[7])/c[2]);
            for(uint64_t s2=0;s2<=max2;s2++){
                const u256 t2=t1+c[2]*s2;
                const uint64_t r2=(r1+mulmod(cm[2],s2,b))%b;
                const uint64_t max3=(uint64_t)((Dlim-t2-c[7])/c[3]);
                for(uint64_t s3=0;s3<=max3;s3++){
                    if(s1+s2+s3==0) continue;
                    const u256 t3=t2+c[3]*s3;
                    const uint64_t r3=(r2+mulmod(cm[3],s3,b))%b;
                    const uint64_t max4=(uint64_t)((Dlim-t3-c[7])/c[4]);
                    for(uint64_t s4=0;s4<=max4;s4++){
                        const u256 t4=t3+c[4]*s4;
                        const uint64_t r4=(r3+mulmod(cm[4],s4,b))%b;
                        const uint64_t max5=(uint64_t)((Dlim-t4-c[7])/c[5]);
                        for(uint64_t s5=0;s5<=max5;s5++){
                            ++prefix_count;
                            const u256 tp=t4+c[5]*s5;
                            if(tp+c[7]>Dlim) continue;
                            const uint64_t rp=(r4+mulmod(cm[5],s5,b))%b;
                            const uint64_t need=(target>=rp)?target-rp:target+b-rp;
                            // If S4=S5=0, band {4,5,6} forces S6>=1.
                            auto& mp=(s4+s5>0)?any:pos;
                            ++lookup_count;
                            auto it=mp.find(need);
                            if(it==mp.end()) continue;
                            const u256 pc=paircost(it->second);
                            const u256 T=tp+pc;
                            if(T<=Dlim && (!found||T<best)){
                                found=true; best=T;
                                const uint64_t code=it->second;
                                bestS={s0,s1,s2,s3,s4,s5,(uint64_t)(code>>16),(uint64_t)(code&0xffff)};
                            }
                        }
                    }
                }
            }
        }
    }

    cout<<"P02 T02 residue-optimal non-tight defect plus tight-row semigroup exclusion\n";
    cout<<"alpha=a_mod_b="<<alpha<<"\n";
    cout<<"h=alpha_inverse_mod_b="<<h<<"\n";
    cout<<"vstar=h+b="<<vstar<<"\n";
    cout<<"M="<<M<<"\n";
    cout<<"a_mod_vstar="<<Drem<<"\n";
    cout<<"D_floor=floor(a/vstar)="<<Dfloor<<"\n";
    cout<<"D_C_previous="<<D_C<<"\n";
    cout<<"target_a2_mod_b="<<target<<"\n";
    cout<<"pair_count="<<pair_count<<"\n";
    cout<<"pair_residue_count_any="<<any.size()<<"\n";
    cout<<"pair_residue_count_s6_positive="<<pos.size()<<"\n";
    cout<<"pair_duplicate_residue_updates="<<duplicate_residues<<"\n";
    cout<<"prefix_count="<<prefix_count<<"\n";
    cout<<"lookup_count="<<lookup_count<<"\n";
    cout<<"congruent_relaxed_tuple_at_or_below_D_floor="<<(found?1:0)<<"\n";
    if(found){
        cout<<"best_T="<<best<<"\nS=";
        for(auto z:bestS) cout<<z<<",";
        cout<<"\n";
        cerr<<"unexpected feasible relaxed tuple\n";
        return 6;
    }
    cout<<"RESIDUE_INVERSE_AND_WITNESS_RANGE=PASS\n";
    cout<<"D_STAR_NONINTEGRAL_AND_STRICTLY_BEATS_D_C=PASS\n";
    cout<<"NO_TIGHT_ROW_RELAXED_SEMIGROUP_POINT_AT_OR_BELOW_FLOOR_D_STAR=PASS\n";
    cout<<"ALL_EXACT_CHECKS_PASS\n";
    return 0;
}
