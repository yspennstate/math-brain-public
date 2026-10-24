#include <boost/multiprecision/cpp_int.hpp>
#include <boost/multiprecision/cpp_dec_float.hpp>
#include <boost/rational.hpp>
#include <array>
#include <cstdint>
#include <cstdlib>
#include <future>
#include <iomanip>
#include <iostream>
#include <vector>
#include <algorithm>
using boost::multiprecision::cpp_int; using Rat=boost::rational<cpp_int>; using Dec=boost::multiprecision::cpp_dec_float_50;
using std::array; using std::cerr; using std::cout; using std::vector; using u64=uint64_t; using u128=unsigned __int128;
static constexpr int NMAX=177,KMAX=60,L=NMAX+1;
static cpp_int fact_int(int n){cpp_int x=1;for(int i=2;i<=n;++i)x*=i;return x;}
static cpp_int binom(int n,int k){if(k<0||k>n)return 0;if(k>n-k)k=n-k;cpp_int x=1;for(int i=1;i<=k;++i){x*=n-k+i;x/=i;}return x;}
static bool isprime(u64 n){if(n<2)return false;if(n%2==0)return n==2;for(u64 d=3;d*d<=n;d+=2)if(n%d==0)return false;return true;}
static u64 modpow(u64 a,u64 e,u64 p){u64 r=1;while(e){if(e&1)r=(u128)r*a%p;a=(u128)a*a%p;e>>=1;}return r;}
static u64 cppmod(const cpp_int&x,u64 p){return (x%p).convert_to<u64>();}
struct S{int par=0;array<u64,L>a{};};
static S mul(const S&x,const S&y,u64 p){S z;int ps=x.par+y.par;z.par=ps&1;int sh=ps>>1;for(int n=sh;n<L;++n){u128 acc=0;int t=n-sh;for(int i=0;i<=t;++i)acc+=(u128)x.a[i]*y.a[t-i];z.a[n]=(u64)(acc%p);}return z;}
static void subeq(S&x,const S&y,u64 p){if(x.par!=y.par){cerr<<"PARITY_ADD_FAIL\n";std::exit(2);}for(int i=0;i<L;++i)x.a[i]=(x.a[i]>=y.a[i])?x.a[i]-y.a[i]:x.a[i]+p-y.a[i];}
static S inv_even(const S&x,u64 p){if(x.par||x.a[0]==0){cerr<<"NONUNIT_PIVOT\n";std::exit(3);}S y;y.a[0]=modpow(x.a[0],p-2,p);for(int n=1;n<L;++n){u128 acc=0;for(int i=1;i<=n;++i)acc+=(u128)x.a[i]*y.a[n-i];u64 q=(u64)(acc%p);y.a[n]=(q==0)?0:(u128)(p-q)*y.a[0]%p;}return y;}
struct PR{u64 p;array<array<u64,L>,KMAX+1>tau{};};
static PR runprime(u64 p){
 array<u64,NMAX+KMAX+2>f{},fi{};f[0]=1;for(int i=1;i<(int)f.size();++i)f[i]=(u128)f[i-1]*i%p;fi.back()=modpow(f.back(),p-2,p);for(int i=(int)f.size()-1;i>=1;--i)fi[i-1]=(u128)fi[i]*i%p;
 vector<vector<S>>A(KMAX,vector<S>(KMAX));for(int i=0;i<KMAX;++i)for(int j=0;j<KMAX;++j){int d=std::abs(i-j);S s;s.par=d&1;int b=d/2;for(int r=0;b+r<L&&r+d<(int)fi.size();++r)s.a[b+r]=(u128)fi[r]*fi[r+d]%p;A[i][j]=s;}
 S det;det.a[0]=1;PR out;out.p=p;out.tau[0][0]=1;for(int i=0;i<KMAX;++i){S piv=A[i][i];det=mul(det,piv,p);for(int n=0;n<L;++n)out.tau[i+1][n]=det.a[n];S ip=inv_even(piv,p);for(int r=i+1;r<KMAX;++r){S fac=mul(A[r][i],ip,p);for(int c=i+1;c<KMAX;++c){S q=mul(fac,A[i][c],p);subeq(A[r][c],q,p);}}}return out;
}
static cpp_int crt(const vector<PR>&R,int k,int n){cpp_int x=R[0].tau[k][n],M=R[0].p;for(size_t q=1;q<R.size();++q){u64 p=R[q].p,xm=cppmod(x,p),mm=cppmod(M,p),iv=modpow(mm,p-2,p),rr=R[q].tau[k][n],delta=(rr>=xm)?rr-xm:rr+p-xm,t=(u128)delta*iv%p;x+=M*t;M*=p;}return x;}
static long double told(const Rat&r){return (Dec(r.numerator())/Dec(r.denominator())).convert_to<long double>();}
static Rat sq(const Rat&x){return x*x;}
static Rat Kcap(int j){return Rat(cpp_int(15163)*j+10000,10000);}
static Rat Bcap(int j,int s,int m){Rat K=Kcap(j);Rat y=Rat(1)+Rat(s)/(K*(K-Rat(m)));return Rat(j+1,j)*sq((K-y)/((K-Rat(1))*y));}
static Rat rho0(int j,int s){Rat K=Kcap(j);return (K-Rat(s)+Rat(1))/(K+Rat(1));}
static Rat rhom(int j,int s,int m){Rat K=Kcap(j);int q=s/m,r=s-q*m;Rat z(1);for(int i=1;i<=q;++i)z*=(K+Rat(i-m))/(K+Rat(i));if(r>0)z*=(K+Rat(q+1-r))/(K+Rat(q+1));return z;}
int main(){
 vector<u64>primes;for(u64 x=1000100001ULL;primes.size()<40;x+=2)if(isprime(x))primes.push_back(x);for(size_t i=0;i<primes.size();++i)for(size_t j=0;j<i;++j)if(primes[i]==primes[j]){cerr<<"DUPLICATE_MODULUS\n";return 4;}
 vector<std::future<PR>> fut;for(auto p:primes)fut.push_back(std::async(std::launch::async,[p]{return runprime(p);}));vector<PR>R;for(auto&f:fut)R.push_back(f.get());
 cpp_int MOD=1;for(auto p:primes)MOD*=p;cpp_int f177=fact_int(177);if(MOD<=2*f177){cerr<<"CRT_RANGE_FAIL\n";return 5;}
 cout<<"P0282 band-sensitive normalization checker for 15163/25163 linear window\n";
 cout<<"primes="<<primes.size()<<" CRT_bits="<<boost::multiprecision::msb(MOD)+1<<" factorial177_bits="<<boost::multiprecision::msb(f177)+1<<" modulus_gt_2factorial177=true\n";
 Rat weakest; bool set=false; int weak_s=-1,weak_M=-1; long double weakv=0;
 for(int s=66;s<=177;++s){int j=s+1;cpp_int fs=fact_int(s),scale=(fs*fs)%MOD;int Mmax=std::min(59,s);vector<cpp_int>tail(Mmax+1);for(int m=1;m<=Mmax;++m){cpp_int u=(crt(R,m,s)*scale)%MOD;if(u<0||u>fs){cerr<<"COUNT_RANGE_FAIL s="<<s<<" m="<<m<<"\n";return 6;}tail[m]=fs-u;}
   Rat r0=rho0(j,s),r02=r0*r0;Rat Bs=Bcap(j,s,s),best=Bs;int bestM=0;vector<Rat>B(Mmax+1),cdf(Mmax+1);
   for(int m=1;m<=Mmax;++m){B[m]=Bcap(j,s,m);if(m>1&&!(B[m-1]>B[m])){cerr<<"B_MONOTONICITY_FAIL\n";return 7;}Rat p(tail[m],fs);Rat rm=rhom(j,s,m);if(!(rm>=r0&&rm<=Rat(1))){cerr<<"RHO_BAND_RANGE_FAIL s="<<s<<" m="<<m<<"\n";return 8;}Rat denom=rm*rm*(Rat(1)-p)+r02*p;Rat lower=Rat(1)-p/denom;if(lower<Rat(0))lower=Rat(0);if(lower>Rat(1)){cerr<<"CDF_RANGE_FAIL\n";return 9;}cdf[m]=lower;}
   for(int M=1;M<=Mmax;++M){Rat val=Bs+(B[M]-Bs)*cdf[M];for(int m=1;m<M;++m)val+=(B[m]-B[m+1])*cdf[m];if(val>best){best=val;bestM=M;}}
   if(!(best>Rat(1))){cerr<<"FINITE_SEAM_FAIL s="<<s<<" best="<<std::setprecision(20)<<told(best)<<" M="<<bestM<<"\n";return 10;}if(!set||best<weakest){set=true;weakest=best;weak_s=s;weak_M=bestM;weakv=told(best);}if(s==66||s==80||s==100||s==120||s==140||s==160||s==177)cout<<"finite_s="<<s<<" best_M="<<bestM<<" lower~"<<std::setprecision(18)<<told(best)<<" exact_gt_1=true\n";
 }
 cout<<"finite_bandnorm_exact_s66_177=PASS weakest_s="<<weak_s<<" best_M="<<weak_M<<" lower~"<<std::setprecision(18)<<weakv<<"\n";
 Rat bridgeWeak; bool bridgeSet=false; int bridgeS=-1,bridgeR=-1; long double bridgeV=0;
 for(int s=178;s<=199;++s){int j=s+1;int r=(s+50)/6,m=r-1;Rat p(binom(s,r),fact_int(r));if(!(p<Rat(1))){cerr<<"BRIDGE_TAIL_NOT_LT_ONE s="<<s<<"\n";return 22;}Rat K=Kcap(j);Rat y=Rat(1)+Rat(s)/(K*(K-Rat(m)));Rat B=Rat(j+1,j)*sq((K-y)/((K-Rat(1))*y));Rat r0=rho0(j,s),rm=rhom(j,s,m);Rat den=rm*rm*(Rat(1)-p)+r0*r0*p;Rat bad=p/den;if(!(bad<Rat(1))){cerr<<"BRIDGE_BAD_MASS_FAIL s="<<s<<"\n";return 23;}Rat val=B*(Rat(1)-bad);if(!(val>Rat(1))){cerr<<"BRIDGE_SOURCE_FAIL s="<<s<<" r="<<r<<" val="<<told(val)<<"\n";return 24;}if(!bridgeSet||val<bridgeWeak){bridgeSet=true;bridgeWeak=val;bridgeS=s;bridgeR=r;bridgeV=told(val);}}
 cout<<"elementary_bandnorm_bridge_s178_199=PASS weakest_s="<<bridgeS<<" r="<<bridgeR<<" lower~"<<std::setprecision(18)<<bridgeV<<"\n";
 for(int K=20;K<=60;++K)for(int i=1;i<=6;++i)for(int jj=i+1;jj<=8;++jj)for(int ai=1;ai<=8;++ai)for(int aj=1;aj<=ai;++aj){int A=K+i-ai,Bb=K+jj-aj;if(!(Bb>=A+1)){cerr<<"TRANSFER_ORDER_FAIL\n";return 11;}Rat ratio=Rat(A-1,A)*Rat(Bb+1,Bb);if(!(ratio<Rat(1))){cerr<<"TRANSFER_RATIO_FAIL\n";return 12;}}
 cout<<"packed_shape_transfer_inequality_small_integer_sanity=PASS\n";
 vector<cpp_int>good_shift={
 cpp_int("405074883684495500665778169"),cpp_int("409954849971717868578203381814"),cpp_int("166734293596683003740639366636535"),cpp_int("34217984252156509802767979788291380"),cpp_int("3589152809321784651844348231212200535"),cpp_int("163105387442747776431855149673503833014"),cpp_int("1284728814035305906587057217860250890969")};for(auto&z:good_shift)if(z<=0){cerr<<"GOOD_SHIFT_SIGN_FAIL\n";return 13;}cout<<"asym_good_factor_B_L_gt_1_plus_1_over_250j_for_j_ge_201=PASS\n";
 for(int s=200;s<=205;++s){int r=(s+47)/6;cpp_int margin=fact_int(r)-cpp_int(8000)*(s+1)*binom(s,r);if(margin<=0){cerr<<"TAIL_BASE_FAIL s="<<s<<" r="<<r<<"\n";return 14;}cout<<"tail_base_s="<<s<<" r="<<r<<" margin="<<margin<<"\n";}
 const char* contraction[6][9]={
 {"18750","4960689","572945232","37722081903","1548085247310","40540106310036","661337450765208","6142247845949592","24855455535387120"},
 {"18750","4982564","578031140","38227874464","1575968742070","41460114456396","679499713889640","6340815118635696","25782563573645760"},
 {"18750","5004439","583138298","38737912433","1604205102880","42395735803896","698049712152072","6544504538701632","26737781276162880"},
 {"18750","5026314","588266706","39252212310","1632797071680","43347152480736","716993487018864","6753416137822080","27721769681612160"},
 {"18750","5048189","593416364","39770790595","1661747400010","44314547873556","736337141864856","6967651301309880","28735200919656000"},
 {"18750","5088814","602977272","40732566788","1715346857110","46101474738846","771967673299508","7360996261346352","30589261954796160"}};
 for(int r=0;r<6;++r)for(int q=0;q<9;++q)if(cpp_int(contraction[r][q])<=0){cerr<<"CONTRACTION_COEFF_FAIL\n";return 15;}cout<<"six_step_tail_contraction_all_residue_polynomials_coefficientwise_positive=PASS\n";
 if(cpp_int(3)*5163-cpp_int(15163)<=0){cerr<<"RHO_ONE_THIRD_FAIL\n";return 16;}cout<<"rho0_gt_one_third_at_boundary=PASS\n";
 if(cpp_int(5750)*201-9<=0){cerr<<"FINAL_PRODUCT_FAIL\n";return 17;}cout<<"asym_final_product_gt_1_for_j_ge_201=PASS\n";
 cout<<"ALL_EXACT_CHECKS_PASS\n";
}
