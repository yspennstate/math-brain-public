#include <boost/multiprecision/cpp_int.hpp>
#include <iostream>
#include <vector>
#include <array>
#include <string>
#include <cstdint>
#include <algorithm>
using boost::multiprecision::cpp_int;
using u128=unsigned __int128; using i128=__int128; using u64=unsigned long long;
static cpp_int parse(const std::string&s){cpp_int x=0;for(char c:s)if(isdigit(c)){x*=10;x+=c-'0';}return x;}
u64 invmod(u64 a,u64 m){long long t=0,nt=1,r=m,nr=a%m;while(nr){long long q=r/nr;auto tt=t-q*nt;t=nt;nt=tt;auto rr=r-q*nr;r=nr;nr=rr;}if(t<0)t+=m;return t;}
const u64 p=256717,q=800000,d=q-p,b=4220452010631561279ULL,M=5000000000000000000ULL,h=707440146652911839ULL,alpha=1884560463669269501ULL;
const cpp_int a=parse("1995237757733917147310102692686664915858011319606812684127301");
std::array<cpp_int,8> c; std::array<u64,8> cinv; std::array<int,8> mult={2,4,4,4,4,4,4,4};
cpp_int powi(u64 x,int e){cpp_int z=1;while(e--)z*=x;return z;}
struct State{u64 s,V;cpp_int u;std::array<u64,6>R{};std::array<u128,6>W{};};
u64 parent_r(u64 s){return (u64)(((u128)h*s)%b);} 
i128 floordiv(i128 a0,i128 d0){if(a0>=0)return a0/d0; return - ((-a0+d0-1)/d0);}
i128 ceildiv(i128 a0,i128 d0){if(a0>=0)return (a0+d0-1)/d0;return -((-a0)/d0);} 
template<class F> void aggregate_pairs(u64 Rmax,u64 z,int m,F emit,unsigned long long &nscans){i128 cap=(i128)m*M; i128 nlo=ceildiv(-cap,(i128)b); i128 nhi=floordiv((i128)h*Rmax,(i128)b); static const u64 hinv=invmod(h%p,p); u64 bp=b%p; for(i128 nn=nlo;nn<=nhi;nn++){nscans++;i128 nb=nn*(i128)b;i128 L=ceildiv(nb,(i128)h);if(L<0)L=0;i128 U=floordiv(nb+cap,(i128)h);if(U>(i128)Rmax)U=Rmax;if(L>U)continue;long long nmod=(long long)(nn%(i128)p);if(nmod<0)nmod+=p;u64 rhs=(z+(u128)(u64)nmod*bp)%p;u64 r0=(u64)(((u128)rhs*hinv)%p);i128 R=L;u64 Lmod=(u64)(L%p);R+=(r0+p-Lmod)%p;if(R>U)continue;u64 Ru=(u64)R;i128 Wi=(i128)h*Ru-nb;if(Wi<0||Wi>cap){std::cerr<<"range bug\n";exit(5);}emit(Ru,(u128)Wi);}}
u64 zdigit(const State&st,int k){cpp_int rem=st.u;for(int j=0;j<k;j++)rem-=c[j]*cpp_int(st.W[j]);cpp_int pk=powi(p,k);if(rem%pk!=0){std::cerr<<"div bug\n";exit(2);}cpp_int r=(rem/pk)%p;if(r<0)r+=p;u64 rr=r.convert_to<u64>();return (u64)(((u128)rr*cinv[k])%p);} 
long long Rmaxf(const State&st,int k,const cpp_int&Dn,const cpp_int&Dd){cpp_int used=a*st.s;for(int j=0;j<k;j++)used+=cpp_int(b)*c[j]*st.R[j];cpp_int N=Dn*st.V-Dd*used;if(N<=0)return-1;cpp_int den=Dd*cpp_int(b)*c[k];cpp_int rm=(N-1)/den;if(rm>1000000000){std::cerr<<"huge Rmax\n";exit(3);}return rm.convert_to<long long>();}

int main(){long long fn=9,fd=1;
 c[0]=powi(q,6)*d;for(int k=1;k<=6;k++)c[k]=powi(q,6-k)*d*powi(p,k);c[7]=powi(p,7);for(int k=0;k<8;k++){cpp_int ck=c[k]/powi(p,k);cinv[k]=invmod((u64)(ck%p),p);}cpp_int p6=powi(p,6);
 if((u64)(((u128)alpha*h)%b)!=1){std::cerr<<"inverse mismatch\n";return 18;}
 for(int k=0;k<=6;k++){cpp_int pk=powi(p,k),pk1=pk*p;if(c[k]%pk!=0||c[k]%pk1==0){std::cerr<<"p-adic valuation mismatch\n";return 19;}}
 cpp_int N0=parse("655209040831815247751186134103526570372190622578374697627001555"),D0=parse("925139970226099634");cpp_int Dn=N0*fn,Dd=D0*fd;
 cpp_int cut=(Dn*M+Dd*a-1)/(Dd*a);long long CUT=cut.convert_to<long long>();std::vector<State> states;
 for(long long ss=0;ss<CUT;ss++){u64 s=ss;if(s==0){State st;st.s=0;st.V=b;st.u=a;states.push_back(st);}else{u64 r=parent_r(s);if(r>=1&&r<=M){State st;st.s=s;st.V=r;st.u=(a*r-s)/b;states.push_back(st);}if((u128)r+b<=M){State st;st.s=s;st.V=r+b;st.u=(a*st.V-s)/b;states.push_back(st);}}}
 std::cout<<"P02 T02 three-type joint-tail checker\n";std::cout<<"D_NEW_OVER_D_MM=9\n";std::cout<<"CUT="<<CUT<<" parents="<<states.size()<<"\n";if(CUT!=15974||states.size()!=18926){std::cerr<<"parent count mismatch\n";return 21;}
 const unsigned long long expected_states[5]={1533,1182,2256,11286,148080};
 const unsigned long long expected_scans[5]={28041558,10574353,20489512,102171516,1345424982};
 const long long expected_maxR[5]={52727,150782,423248,1165159,3515813};
 for(int k=0;k<=4;k++){std::vector<State>nx;unsigned long long nsc=0;long long maxr=-1;for(const auto&st:states){long long rm=Rmaxf(st,k,Dn,Dd);if(rm<0)continue;maxr=std::max(maxr,rm);u64 z=zdigit(st,k);aggregate_pairs((u64)rm,z,mult[k],[&](u64 R,u128 W){State ns=st;ns.R[k]=R;ns.W[k]=W;nx.push_back(std::move(ns));},nsc);}states.swap(nx);std::cout<<"k="<<k<<" states="<<states.size()<<" nscans="<<nsc<<" maxR="<<maxr<<"\n";if(states.size()!=expected_states[k]||nsc!=expected_scans[k]||maxr!=expected_maxR[k]){std::cerr<<"prefix count mismatch k="<<k<<"\n";return 20;}}
 unsigned long long residue_too_big=0, slacktriples=0, witness_lifts=0, survivors=0, positive_rem=0; bool found=false; State fs;u64 fR5=0,fR6=0,fR7=0;u128 fW5=0,fW6=0,fW7=0;cpp_int fS=0;
 cpp_int p5=powi(p,5); const u64 A=(u64)q*d, B=(u64)p*d, C=(u64)p*p; const u64 Ainv=invmod(A%p,p), dinv=invmod(d%p,p);
 for(const auto&st:states){
   cpp_int rem=st.u;for(int j=0;j<5;j++)rem-=c[j]*cpp_int(st.W[j]);if(rem<0)continue;positive_rem++;if(rem%p5!=0){std::cerr<<"rem5 divisibility bug\n";return 4;} cpp_int E=rem/p5;
   cpp_int used=a*st.s;for(int j=0;j<5;j++)used+=cpp_int(b)*c[j]*st.R[j];cpp_int N=Dn*st.V-Dd*used;if(N<=0)continue;cpp_int den=Dd*cpp_int(b)*p5;cpp_int Smax=(N-1)/den;
   cpp_int rr=(cpp_int(alpha)*(E%b))%b;if(rr<0)rr+=b;if(rr>Smax){residue_too_big++;continue;}
   for(cpp_int SS=rr;SS<=Smax;SS+=b){if(SS>cpp_int(UINT64_MAX)){std::cerr<<"S overflow\n";return 13;}u64 S=SS.convert_to<u64>();
     // A R5 + p(d R6+p R7)=S. First R5 fixed mod p.
     u64 r50=(u64)(((u128)(S%p)*Ainv)%p);u64 maxR5=S/A;
     for(u64 R5=r50;R5<=maxR5;R5+=p){u64 remS=S-A*R5;if(remS%p){std::cerr<<"S/p bug\n";return 14;}u64 S2=remS/p;u64 r60=(u64)(((u128)(S2%p)*dinv)%p);u64 maxR6=S2/d;
       for(u64 R6=r60;R6<=maxR6;R6+=p){u64 rem2=S2-d*R6;if(rem2%p){std::cerr<<"R7 bug\n";return 15;}u64 R7=rem2/p;slacktriples++;
         u64 rw5=(u64)(((u128)h*R5)%b), rw6=(u64)(((u128)h*R6)%b), rw7=(u64)(((u128)h*R7)%b);
         for(int l5=0;l5<=5;l5++){u128 W5=(u128)rw5+(u128)l5*b;if(W5>(u128)4*M)break;cpp_int num1=E-cpp_int(A)*cpp_int(W5);if(num1<0||num1%p!=0)continue;cpp_int E2=num1/p;
           for(int l6=0;l6<=5;l6++){u128 W6=(u128)rw6+(u128)l6*b;if(W6>(u128)4*M)break;cpp_int num2=E2-cpp_int(d)*cpp_int(W6);if(num2<0||num2%p!=0)continue;cpp_int W7i=num2/p;if(W7i<0||W7i>cpp_int(4)*M)continue;if((u64)(W7i%b)!=rw7)continue;witness_lifts++;survivors++;if(!found){found=true;fs=st;fR5=R5;fR6=R6;fR7=R7;fW5=W5;fW6=W6;fW7=W7i.convert_to<u128>();fS=S;}
           }
         }
       }
     }
   }
 }
 std::cout<<"joint3 positive_rem="<<positive_rem<<" residue_too_big="<<residue_too_big<<" slacktriples="<<slacktriples<<" witness_lifts="<<witness_lifts<<" survivors="<<survivors<<"\n";
 if(positive_rem!=131080||residue_too_big!=104175||slacktriples!=3529814||witness_lifts!=0||survivors!=0){std::cerr<<"joint-tail count mismatch\n";return 22;}
 if(found){std::cerr<<"unexpected survivor\n";return 23;}
 std::cout<<"PREFIX_MIXED_MODULUS_ENUMERATION=PASS\n";
 std::cout<<"EXACT_THREE_TYPE_JOINT_TAIL_CLOSURE=PASS\n";
 std::cout<<"GLOBAL_TWO_STEP_DEFECT_9_DMM=PASS\n";
 std::cout<<"ALL_EXACT_CHECKS_PASS\n";
 return 0;
}
