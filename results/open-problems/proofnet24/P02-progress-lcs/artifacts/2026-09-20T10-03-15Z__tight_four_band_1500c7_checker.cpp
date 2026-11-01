#include <boost/multiprecision/cpp_int.hpp>
#include <bits/stdc++.h>
using namespace std; using boost::multiprecision::cpp_int;
using u256=boost::multiprecision::number<boost::multiprecision::cpp_int_backend<256,256,boost::multiprecision::unsigned_magnitude,boost::multiprecision::unchecked,void>>;
using u128=__uint128_t;
static uint64_t mod_cpp(const cpp_int& x,uint64_t m){ return (uint64_t)(x%m); }
static uint64_t mulmod(uint64_t x,uint64_t y,uint64_t m){ return (uint64_t)((u128)x*y%m); }
struct MixHash { size_t operator()(uint64_t x) const noexcept { x += 0x9e3779b97f4a7c15ULL; x=(x^(x>>30))*0xbf58476d1ce4e5b9ULL; x=(x^(x>>27))*0x94d049bb133111ebULL; return x^(x>>31);} };
int main(int argc,char**argv){
 const uint64_t p=256717,q=800000,d=q-p,b=4220452010631561279ULL;
 const cpp_int a("1995237757733917147310102692686664915858011319606812684127301");
 const uint64_t h=707440146652911839ULL, vstar=h+b;
 u256 c[8]; for(int k=0;k<=6;k++){u256 qq=1,pp=1;for(int j=0;j<6-k;j++)qq*=q;for(int j=0;j<k;j++)pp*=p;c[k]=qq*d*pp;} c[7]=1;for(int j=0;j<7;j++)c[7]*=p;
 cpp_int Dfloor=a/vstar, Drem=a%vstar;
 uint64_t K=argc>1?strtoull(argv[1],0,10):1500;
 cpp_int DNfloor=Dfloor + cpp_int(K)*c[7].convert_to<cpp_int>();
 const u256 Dlim=DNfloor.convert_to<u256>();
 uint64_t cm[8];for(int k=0;k<8;k++)cm[k]=(uint64_t)(c[k]%b); const uint64_t target=mod_cpp(a*a,b);
 const u256 Rmax=Dlim-c[0]-c[3]; const uint64_t max6=(uint64_t)(Rmax/c[6]);
 unordered_map<uint64_t,uint32_t,MixHash> any,pos; any.reserve(4000000);pos.reserve(4000000);any.max_load_factor(.75);pos.max_load_factor(.75);
 auto paircost=[&](uint32_t code)->u256{uint64_t s6=code>>16,s7=code&0xffff;return c[6]*s6+c[7]*s7;};
 uint64_t pair_count=0;
 for(uint64_t s6=0;s6<=max6;s6++){u256 rem=Rmax-c[6]*s6;uint64_t max7=(uint64_t)(rem/c[7]);uint64_t residue=mulmod(cm[6],s6,b)+cm[7];if(residue>=b)residue-=b;for(uint64_t s7=1;s7<=max7;s7++){uint32_t code=(uint32_t)((s6<<16)|s7);++pair_count;auto upd=[&](auto&mp){auto it=mp.find(residue);if(it==mp.end())mp.emplace(residue,code);else if(paircost(code)<paircost(it->second))it->second=code;};upd(any);if(s6>=1)upd(pos);residue+=cm[7];if(residue>=b)residue-=b;}}
 bool found=false;u256 best=0;array<uint64_t,8> bestS{};uint64_t pref=0,look=0;
 uint64_t max0=(uint64_t)(Dlim/c[0]);
 for(uint64_t s0=1;s0<=max0;s0++){u256 t0=c[0]*s0;uint64_t r0=mulmod(cm[0],s0,b);uint64_t max1=(uint64_t)((Dlim-t0-c[7])/c[1]);
  for(uint64_t s1=0;s1<=max1;s1++){u256 t1=t0+c[1]*s1;uint64_t r1=(r0+mulmod(cm[1],s1,b))%b;uint64_t max2=(uint64_t)((Dlim-t1-c[7])/c[2]);
   for(uint64_t s2=0;s2<=max2;s2++){u256 t2=t1+c[2]*s2;uint64_t r2=(r1+mulmod(cm[2],s2,b))%b;uint64_t max3=(uint64_t)((Dlim-t2-c[7])/c[3]);
    for(uint64_t s3=0;s3<=max3;s3++){if(s1+s2+s3==0)continue;u256 t3=t2+c[3]*s3;uint64_t r3=(r2+mulmod(cm[3],s3,b))%b;uint64_t max4=(uint64_t)((Dlim-t3-c[7])/c[4]);
     for(uint64_t s4=0;s4<=max4;s4++){u256 t4=t3+c[4]*s4;uint64_t r4=(r3+mulmod(cm[4],s4,b))%b;uint64_t max5=(uint64_t)((Dlim-t4-c[7])/c[5]);
      for(uint64_t s5=0;s5<=max5;s5++){++pref;u256 tp=t4+c[5]*s5;if(tp+c[7]>Dlim)continue;uint64_t rp=(r4+mulmod(cm[5],s5,b))%b;uint64_t need=(target>=rp)?target-rp:target+b-rp;auto &mp=(s4+s5>0)?any:pos;++look;auto it=mp.find(need);if(it==mp.end())continue;u256 T=tp+paircost(it->second);if(T<=Dlim){ cpp_int Ti=T.convert_to<cpp_int>(); if(Ti>Dfloor && (!found||T<best)){found=true;best=T;uint64_t code=it->second;bestS={s0,s1,s2,s3,s4,s5,(uint64_t)(code>>16),(uint64_t)(code&0xffff)};}} }
     }
    }
   }
  }
 }
 cout<<"Dfloor="<<Dfloor<<"\nDrem="<<Drem<<"\nDNfloor="<<DNfloor<<"\n";
 cout<<"pair_count="<<pair_count<<" any="<<any.size()<<" pos="<<pos.size()<<" pref="<<pref<<" look="<<look<<"\n";
 cout<<"found="<<found<<"\n"; if(found){cout<<"best="<<best<<"\nS=";for(auto z:bestS)cout<<z<<",";cout<<"\n";}
}
