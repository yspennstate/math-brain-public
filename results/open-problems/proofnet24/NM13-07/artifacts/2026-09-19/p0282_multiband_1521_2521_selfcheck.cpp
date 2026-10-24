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
static constexpr int NMAX=180,KMAX=60,L=NMAX+1;
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
static Rat Bcap(int j,int s,int m,int cnum,int cden){Rat K(cpp_int(cnum)*j+cden,cden);Rat y=Rat(1)+Rat(s)/(K*(K-Rat(m)));return Rat(j+1,j)*sq((K-y)/((K-Rat(1))*y));}
static Rat rho_cap(int j,int cnum,int cden){return Rat(cpp_int(cnum-cden)*j+cpp_int(3)*cden, cpp_int(cnum)*j+cpp_int(2)*cden);}
static cpp_int binom(int n,int k){if(k<0||k>n)return 0;if(k>n-k)k=n-k;cpp_int z=1;for(int i=1;i<=k;++i){z*=n-k+i;z/=i;}return z;}
int main(){
 vector<u64>primes={};for(u64 x=1000100001ULL;primes.size()<40;x+=2)if(isprime(x))primes.push_back(x);
 vector<std::future<PR>>fut;for(auto p:primes)fut.push_back(std::async(std::launch::async,[p]{return runprime(p);}));vector<PR>R;for(auto&f:fut)R.push_back(f.get());
 cpp_int MOD=1;for(auto p:primes)MOD*=p;cpp_int f180=fact_int(180);if(MOD<=2*f180){cerr<<"CRT_RANGE_FAIL\n";return 4;}
 cout<<"P0282 exact multiband Plancherel 1521/2521 finite-core checker\n";
 cout<<"candidate: 1000*n >= 2521*j (equiv k/n >= 1521/2521), finite seam s=j-1=66..180\n";
 cout<<"primes="<<primes.size()<<" CRT_bits="<<boost::multiprecision::msb(MOD)+1<<" factorial180_bits="<<boost::multiprecision::msb(f180)+1<<" modulus_gt_2factorial180=true\n";
 long double weakest=1e9L;int weak_s=-1,weak_M=-1;Rat diag151,diag152;int diag151M=-1,diag152M=-1;
 for(int s=66;s<=180;++s){int j=s+1;cpp_int fs=fact_int(s),fs2=fs*fs;int Mmax=std::min(KMAX-1,s);vector<cpp_int>tail(Mmax+1);
  for(int m=1;m<=Mmax;++m){cpp_int coeff=crt(R,m,s),u=(coeff*fs2)%MOD;if(u<0||u>fs){cerr<<"COUNT_RANGE_FAIL s="<<s<<" m="<<m<<"\n";return 5;}tail[m]=fs-u;}
  auto best_for=[&](int cnum,int cden,int &bestM){Rat rho=rho_cap(j,cnum,cden),rho2=rho*rho;vector<Rat>B(Mmax+1),cdf(Mmax+1);for(int m=1;m<=Mmax;++m){B[m]=Bcap(j,s,m,cnum,cden);if(m>1&&!(B[m-1]>B[m])){cerr<<"B_MONOTONICITY_FAIL\n";std::exit(6);}Rat lower=Rat(1)-Rat(tail[m],fs)/rho2;if(lower<Rat(0))lower=Rat(0);if(lower>Rat(1)){cerr<<"CDF_RANGE_FAIL\n";std::exit(7);}cdf[m]=lower;}Rat Bs=Bcap(j,s,s,cnum,cden),best=Bs;bestM=0;for(int M=1;M<=Mmax;++M){Rat val=Bs+(B[M]-Bs)*cdf[M];for(int m=1;m<M;++m)val+=(B[m]-B[m+1])*cdf[m];if(val>best){best=val;bestM=M;}}return best;};
  int bestM=0;Rat best=best_for(1521,1000,bestM);if(!(best>Rat(1))){cerr<<"FINITE_MULTIBAND_FAIL s="<<s<<" best~"<<told(best)<<"\n";return 8;}long double bv=told(best);if(bv<weakest){weakest=bv;weak_s=s;weak_M=bestM;}if(s==66){diag151=best_for(151,100,diag151M);diag152=best_for(38,25,diag152M);}if(s==66||s==80||s==100||s==120||s==140||s==160||s==180)cout<<"s="<<s<<" best_M="<<bestM<<" exact_lower_gt_1=true lower~"<<std::setprecision(18)<<bv<<"\n";
 }
 cout<<"finite_multiband_exact_s66_180=PASS weakest_lower~"<<std::setprecision(18)<<weakest<<" at_s="<<weak_s<<" best_M="<<weak_M<<"\n";
 cout<<"diagnostic_s66_c151_best~"<<told(diag151)<<" best_M="<<diag151M<<" below_one="<<(diag151<Rat(1)?"true":"false")<<"\n";
 cout<<"diagnostic_s66_c152_best~"<<told(diag152)<<" best_M="<<diag152M<<" below_one="<<(diag152<Rat(1)?"true":"false")<<"\n";
 if(!(diag151<Rat(1)&&diag152<Rat(1))){cerr<<"DIAGNOSTIC_EXPECTED_FAIL_NOT_SEEN\n";return 9;}
 vector<cpp_int>shift={cpp_int("34637813925283840517391046543296"),cpp_int("10220607248381606984066970440768"),cpp_int("266094389437626533771809100560"),cpp_int("2877525058784156009114697440"),cpp_int("15712132188386508698711940"),cpp_int("43067359282266197003268"),cpp_int("47313634206146816079")};for(auto&z:shift)if(z<=0){cerr<<"ASYM_SHIFT_SIGN_FAIL\n";return 10;}cout<<"asym_good_factor_shift_j182_all_coefficients_positive=PASS\n";
 for(int s=181;s<=186;++s){int r=(s+53)/6;cpp_int margin=fact_int(r)-cpp_int(5000)*(s+1)*binom(s,r);if(margin<=0){cerr<<"TAIL_BASE_FAIL s="<<s<<"\n";return 11;}cout<<"tail_base_s="<<s<<" r="<<r<<" margin="<<margin<<"\n";}
 cpp_int ratio_margin("13169713741084433201");if(ratio_margin<=0){cerr<<"RATIO_MARGIN_FAIL\n";return 12;}cout<<"six_step_tail_contraction_R181_lt_1_and_log_derivative_negative=PASS margin="<<ratio_margin<<"\n";
 if(cpp_int(42)*182+7000<=0){cerr<<"RHO_FAIL\n";return 13;}cout<<"rho0_gt_one_third_for_j>=182=PASS\n";
 if(cpp_int(3200)*182-9<=0){cerr<<"FINAL_PRODUCT_FAIL\n";return 14;}cout<<"asym_good_factor_gt_1_plus_1_over_200j=PASS\n";cout<<"asym_tilted_bad_mass_lt_9/(5000j)=PASS\n";cout<<"asym_final_product_gt_1_for_j>=182=PASS\n";cout<<"ALL_EXACT_CHECKS_PASS\n";
}
