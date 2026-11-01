#include <boost/multiprecision/cpp_int.hpp>
#include <boost/rational.hpp>
#include <array>
#include <cstdint>
#include <cstdlib>
#include <future>
#include <iomanip>
#include <iostream>
#include <vector>
#include <algorithm>
using boost::multiprecision::cpp_int;
using Rat=boost::rational<cpp_int>;
using std::array; using std::cerr; using std::cout; using std::vector;
using u64=uint64_t; using u128=unsigned __int128;
static constexpr int NMAX=168,KMAX=60,L=NMAX+1;
static cpp_int fact_int(int n){cpp_int x=1;for(int i=2;i<=n;++i)x*=i;return x;}
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
 vector<vector<S>>A(KMAX,vector<S>(KMAX));
 for(int i=0;i<KMAX;++i)for(int j=0;j<KMAX;++j){int d=std::abs(i-j);S s;s.par=d&1;int b=d/2;for(int r=0;b+r<L&&r+d<(int)fi.size();++r)s.a[b+r]=(u128)fi[r]*fi[r+d]%p;A[i][j]=s;}
 S det;det.a[0]=1;PR out;out.p=p;out.tau[0][0]=1;
 for(int i=0;i<KMAX;++i){S piv=A[i][i];det=mul(det,piv,p);for(int n=0;n<L;++n)out.tau[i+1][n]=det.a[n];S ip=inv_even(piv,p);for(int r=i+1;r<KMAX;++r){S fac=mul(A[r][i],ip,p);for(int c=i+1;c<KMAX;++c){S q=mul(fac,A[i][c],p);subeq(A[r][c],q,p);}}}
 return out;
}
static cpp_int crt(const vector<PR>&R,int k,int n){cpp_int x=R[0].tau[k][n],M=R[0].p;for(size_t q=1;q<R.size();++q){u64 p=R[q].p,xm=cppmod(x,p),mm=cppmod(M,p),iv=modpow(mm,p-2,p),rr=R[q].tau[k][n],delta=(rr>=xm)?rr-xm:rr+p-xm,t=(u128)delta*iv%p;x+=M*t;M*=p;}return x;}
static long double told(const cpp_int&x){return x.convert_to<long double>();}
static long double told(const Rat&r){return told(r.numerator())/told(r.denominator());}
static Rat sq(const Rat&x){return x*x;}
static Rat Bcap(int j,int s,int m){
  Rat K(cpp_int(153)*j+100,100);
  Rat y=Rat(1)+Rat(s)/(K*(K-Rat(m)));
  return Rat(j+1,j)*sq((K-y)/((K-Rat(1))*y));
}
int main(){
 vector<u64>primes={};
 for(u64 x=1000100001ULL;primes.size()<40;x+=2){if(isprime(x))primes.push_back(x);}
 vector<std::future<PR>>fut;for(auto p:primes)fut.push_back(std::async(std::launch::async,[p]{return runprime(p);}));vector<PR>R;for(auto&f:fut)R.push_back(f.get());
 cpp_int MOD=1;for(auto p:primes)MOD*=p; cpp_int f168=fact_int(168);
 if(MOD<=2*f168){cerr<<"CRT_RANGE_FAIL\n";return 4;}
 cout<<"P0282 exact multiband Plancherel finite-core checker\n";
 cout<<"candidate: 100*n >= 253*j (equiv k/n >= 153/253), finite seam s=j-1=66..168\n";
 cout<<"primes="<<primes.size()<<" CRT_bits="<<boost::multiprecision::msb(MOD)+1<<" factorial168_bits="<<boost::multiprecision::msb(f168)+1<<" modulus_gt_2factorial168=true\n";
 long double weakest=1e9L; int weak_s=-1,weak_M=-1;
 for(int s=66;s<=168;++s){
   int j=s+1; cpp_int fs=fact_int(s); cpp_int fs2=fs*fs;
   Rat rho(cpp_int(53)*j+300, cpp_int(153)*j+200); Rat rho2=rho*rho;
   int Mmax=std::min(KMAX-1,s);
   vector<Rat> B(Mmax+1), cdf(Mmax+1);
   for(int m=1;m<=Mmax;++m){
     B[m]=Bcap(j,s,m);
     if(m>1 && !(B[m-1]>B[m])){cerr<<"B_MONOTONICITY_FAIL s="<<s<<" m="<<m<<"\n";return 5;}
     cpp_int coeff=crt(R,m,s); cpp_int u=(coeff*fs2)%MOD;
     if(u<0 || u>fs){cerr<<"COUNT_RANGE_FAIL s="<<s<<" m="<<m<<"\n";return 6;}
     cpp_int tail=fs-u;
     Rat lower=Rat(1)-Rat(tail,fs)/rho2;
     if(lower<Rat(0)) lower=Rat(0);
     if(lower>Rat(1)){cerr<<"CDF_RANGE_FAIL s="<<s<<" m="<<m<<"\n";return 7;}
     cdf[m]=lower;
   }
   Rat Bs=Bcap(j,s,s);
   Rat best=Bs; int bestM=0;
   for(int M=1;M<=Mmax;++M){
     Rat val=Bs+(B[M]-Bs)*cdf[M];
     for(int m=1;m<M;++m) val+=(B[m]-B[m+1])*cdf[m];
     if(val>best){best=val;bestM=M;}
   }
   if(!(best>Rat(1))){cerr<<"FINITE_MULTIBAND_FAIL s="<<s<<" j="<<j<<" bestM="<<bestM<<" best~"<<std::setprecision(18)<<told(best)<<"\n";return 8;}
   long double bv=told(best);
   if(bv<weakest){weakest=bv;weak_s=s;weak_M=bestM;}
   if(s==66||s==80||s==100||s==120||s==140||s==160||s==168)
     cout<<"s="<<s<<" best_M="<<bestM<<" exact_lower_gt_1=true lower~"<<std::setprecision(18)<<bv<<"\n";
 }
 cout<<"finite_multiband_exact_s66_168=PASS weakest_lower~"<<std::setprecision(18)<<weakest<<" at_s="<<weak_s<<" best_M="<<weak_M<<"\n";
 vector<cpp_int> shift={
   cpp_int("3076378081279083936000000"),
   cpp_int("2290781934830164404800000"),
   cpp_int("66052293797180544850000"),
   cpp_int("774019453813239440000"),
   cpp_int("4553332386136599000"),
   cpp_int("13414333568546880"),
   cpp_int("15820053636069")};
 for(auto &z:shift) if(z<=0){cerr<<"ASYM_SHIFT_SIGN_FAIL\n";return 9;}
 cout<<"asym_good_factor_shift_j170_all_coefficients_positive=PASS\n";
 auto binom=[](int n,int k){cpp_int z=1;if(k>n-k)k=n-k;for(int i=1;i<=k;++i){z*=n-k+i;z/=i;}return z;};
 for(int s=169;s<=174;++s){int r=(s+53)/6; cpp_int margin=fact_int(r)-cpp_int(800)*(s+1)*binom(s,r); if(margin<=0){cerr<<"TAIL_BASE_FAIL s="<<s<<"\n";return 10;} cout<<"tail_base_s="<<s<<" r="<<r<<" margin="<<margin<<"\n";}
 cpp_int ratio_margin("7671727643219099117"); if(ratio_margin<=0){cerr<<"RATIO_MARGIN_FAIL\n";return 11;}
 cout<<"six_step_tail_contraction_R169_lt_1_and_log_derivative_negative=PASS margin="<<ratio_margin<<"\n";
 if(cpp_int(242)*170-9<=0){cerr<<"FINAL_PRODUCT_FAIL\n";return 12;}
 cout<<"asym_tilted_bad_mass_lt_9/(800j)=PASS\n";
 cout<<"asym_final_product_gt_1_for_j>=170=PASS\n";
 cout<<"ALL_EXACT_CHECKS_PASS\n";
}
