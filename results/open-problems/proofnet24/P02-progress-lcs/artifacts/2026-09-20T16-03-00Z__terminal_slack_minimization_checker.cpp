#include <boost/multiprecision/cpp_int.hpp>
#include <iostream>
#include <vector>
#include <array>
#include <string>
#include <cstdint>
#include <algorithm>
using boost::multiprecision::cpp_int;
using u128=unsigned __int128; using i128=__int128; using u64=unsigned long long; using i64=long long;
static cpp_int parse(const std::string&s){cpp_int x=0;for(char c:s)if(isdigit(c)){x*=10;x+=c-'0';}return x;}
static std::string s128(u128 x){if(!x)return"0";std::string s;while(x){s.push_back('0'+x%10);x/=10;}reverse(s.begin(),s.end());return s;}
u64 invmod(u64 a,u64 m){long long t=0,nt=1,r=m,nr=a%m;while(nr){long long q=r/nr;auto tt=t-q*nt;t=nt;nt=tt;auto rr=r-q*nr;r=nr;nr=rr;}if(t<0)t+=m;return t;}
const u64 p=256717,q=800000,d=q-p,b=4220452010631561279ULL,M=5000000000000000000ULL,h=707440146652911839ULL,alpha=1884560463669269501ULL;
const cpp_int a=parse("1995237757733917147310102692686664915858011319606812684127301");
std::array<cpp_int,8> c; std::array<u64,8> cinv; std::array<int,8> mult={2,4,4,4,4,4,4,4};
cpp_int powi(u64 x,int e){cpp_int z=1;while(e--)z*=x;return z;}
struct State{u64 s,V;cpp_int u;std::array<u64,7>R{};std::array<u128,7>W{};};
u64 parent_r(u64 s){return (u64)(((u128)h*s)%b);} 
i128 floordiv(i128 a0,i128 d0){if(a0>=0)return a0/d0; return - ((-a0+d0-1)/d0);}
i128 ceildiv(i128 a0,i128 d0){if(a0>=0)return (a0+d0-1)/d0;return -((-a0)/d0);} 

template<class F> void aggregate_pairs(u64 Rmax,u64 z,int m,F emit,unsigned long long &nscans){
  // Exact reparameterization: W=hR-nb, with 0<=W<=mM and W=z mod p.
  i128 cap=(i128)m*M;
  i128 nlo=ceildiv(-cap,(i128)b);
  i128 nhi=floordiv((i128)h*Rmax,(i128)b);
  static const u64 hinv=invmod(h%p,p);
  u64 bp=b%p;
  for(i128 nn=nlo;nn<=nhi;nn++){
    nscans++;
    i128 nb=nn*(i128)b;
    i128 L=ceildiv(nb,(i128)h); if(L<0)L=0;
    i128 U=floordiv(nb+cap,(i128)h); if(U>(i128)Rmax)U=Rmax;
    if(L>U)continue;
    long long nmod=(long long)(nn%(i128)p); if(nmod<0)nmod+=p;
    u64 rhs=(z + (u128)(u64)nmod*bp)%p;
    u64 r0=(u64)(((u128)rhs*hinv)%p);
    i128 R=L;
    u64 Lmod=(u64)(L%p);
    u64 add=(r0+p-Lmod)%p; R+=add;
    if(R>U)continue;
    u64 Ru=(u64)R;
    i128 Wi=(i128)h*Ru-nb;
    if(Wi<0||Wi>cap){std::cerr<<"range bug\n";exit(5);} 
    u128 W=(u128)Wi;
    if((u64)(W%p)!=z){std::cerr<<"res bug\n";exit(6);} 
    if((u64)(W%b)!=(u64)(((u128)h*Ru)%b)){std::cerr<<"b bug\n";exit(7);} 
    emit(Ru,W);
  }
}

u64 zdigit(const State&st,int k){cpp_int rem=st.u;for(int j=0;j<k;j++)rem-=c[j]*cpp_int(st.W[j]);cpp_int pk=powi(p,k);if(rem%pk!=0){std::cerr<<"div bug\n";exit(2);}cpp_int r=(rem/pk)%p;if(r<0)r+=p;u64 rr=r.convert_to<u64>();return (u64)(((u128)rr*cinv[k])%p);} 
long long Rmaxf(const State&st,int k,const cpp_int&Dn,const cpp_int&Dd){cpp_int used=a*st.s;for(int j=0;j<k;j++)used+=cpp_int(b)*c[j]*st.R[j];cpp_int N=Dn*st.V-Dd*used;if(N<=0)return-1;cpp_int den=Dd*cpp_int(b)*c[k];cpp_int rm=(N-1)/den;if(rm>1000000000){std::cerr<<"huge\n";exit(3);}return rm.convert_to<long long>();}
int main(){long long fn=7,fd=2;
 if((u64)(((u128)alpha*h)%b)!=1){std::cerr<<"inverse mismatch\n";return 9;}
 c[0]=powi(q,6)*d;for(int k=1;k<=6;k++)c[k]=powi(q,6-k)*d*powi(p,k);c[7]=powi(p,7);for(int k=0;k<8;k++){cpp_int ck=c[k]/powi(p,k);cinv[k]=invmod((u64)(ck%p),p);} 
 cpp_int N0=parse("655209040831815247751186134103526570372190622578374697627001555"),D0=parse("925139970226099634");cpp_int Dn=N0*fn,Dd=D0*fd;
 cpp_int cut=(Dn*M + Dd*a-1)/(Dd*a);long long CUT=cut.convert_to<long long>();std::vector<State> states;
 for(long long ss=0;ss<CUT;ss++){u64 s=ss;if(s==0){State st;st.s=0;st.V=b;st.u=a;states.push_back(st);}else{u64 r=parent_r(s);if(r>=1&&r<=M){State st;st.s=s;st.V=r;st.u=(a*r-s)/b;states.push_back(st);}if((u128)r+b<=M){State st;st.s=s;st.V=r+b;st.u=(a*st.V-s)/b;states.push_back(st);}}}
 if(CUT!=6212 || states.size()!=7361){std::cerr<<"parent count mismatch\n"; return 10;}
 std::cout<<"P02 T02 terminal-slack minimization checker"<<std::endl;
 std::cout<<"D_NEW_OVER_D_MM=7/2"<<std::endl;
 std::cout<<"CUT="<<CUT<<" parents="<<states.size()<<std::endl;
 const unsigned long long expected_states[6]={228,79,67,119,505,5686};
 for(int k=0;k<=5;k++){std::vector<State>nx;unsigned long long nsc=0,pairs=0;long long maxr=-1;for(const auto&st:states){long long rm=Rmaxf(st,k,Dn,Dd);if(rm<0)continue;maxr=std::max(maxr,rm);u64 z=zdigit(st,k);aggregate_pairs((u64)rm,z,mult[k],[&](u64 R,u128 W){pairs++;State ns=st;ns.R[k]=R;ns.W[k]=W;nx.push_back(std::move(ns));},nsc);}states.swap(nx); if(states.size()!=expected_states[k] || pairs!=expected_states[k]){std::cerr<<"stage mismatch k="<<k<<"\n";return 11;} std::cout<<"k="<<k<<" states="<<states.size()<<" nscans="<<nsc<<" pairs="<<pairs<<" maxR="<<maxr<<std::endl;if(states.empty())return 0;}
 unsigned long long nsc6=0,pairs6=0,w7range=0,surv=0;long long maxr6=-1; State wit;u64 wr6=0,wr7=0;u128 ww6=0,ww7=0;bool found=false;
 for(const auto&st:states){long long rm=Rmaxf(st,6,Dn,Dd);if(rm<0)continue;maxr6=std::max(maxr6,rm);u64 z=zdigit(st,6);cpp_int prefix=0;for(int j=0;j<6;j++)prefix+=c[j]*cpp_int(st.W[j]);aggregate_pairs((u64)rm,z,4,[&](u64 R6,u128 W6){pairs6++;cpp_int rem=st.u-prefix-c[6]*cpp_int(W6);if(rem<0||rem%c[7]!=0)return;cpp_int w7i=rem/c[7];if(w7i<0||w7i>cpp_int(4)*M)return;w7range++;u64 w7mb=(u64)(w7i%b);u64 R7=(u64)(((u128)alpha*w7mb)%b);cpp_int used=a*st.s;for(int j=0;j<6;j++)used+=cpp_int(b)*c[j]*st.R[j];used+=cpp_int(b)*c[6]*R6+cpp_int(b)*c[7]*R7;if(Dn*st.V>Dd*used){surv++;if(!found){found=true;wit=st;wr6=R6;wr7=R7;ww6=W6;ww7=w7i.convert_to<u128>();}}},nsc6);}
 if(pairs6!=176125 || w7range!=167 || surv!=0){std::cerr<<"terminal mismatch\n";return 12;}
 std::cout<<"final nsc6="<<nsc6<<" pairs6="<<pairs6<<" maxR6="<<maxr6<<" w7range="<<w7range<<" surviving="<<surv<<std::endl;if(found){std::cout<<"FOUND s="<<wit.s<<" V="<<wit.V<<" R=";for(int j=0;j<6;j++)std::cout<<wit.R[j]<<",";std::cout<<wr6<<","<<wr7<<" W6="<<s128(ww6)<<" W7="<<s128(ww7)<<std::endl;return 1;}std::cout<<"FAST_MIXED_MODULUS_LIFT_ENUMERATION=PASS"<<std::endl;
 std::cout<<"EXACT_TYPE7_MINIMAL_SLACK_CLOSURE=PASS"<<std::endl;
 std::cout<<"GLOBAL_TWO_STEP_DEFECT_7_OVER_2_DMM=PASS"<<std::endl;
 std::cout<<"ALL_EXACT_CHECKS_PASS"<<std::endl;return 0;}
