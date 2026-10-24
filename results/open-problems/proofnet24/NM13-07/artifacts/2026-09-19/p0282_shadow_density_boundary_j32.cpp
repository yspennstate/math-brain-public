#include <boost/multiprecision/cpp_int.hpp>
#include <algorithm>
#include <array>
#include <chrono>
#include <cstdint>
#include <cstdlib>
#include <future>
#include <iomanip>
#include <iostream>
#include <vector>
using boost::multiprecision::cpp_int;
using std::array; using std::cerr; using std::cout; using std::vector;
static constexpr int NMAX=65,KMAX=34,L=NMAX+1;
using u64=uint64_t; using u128=unsigned __int128;
static cpp_int fact_int(int n){cpp_int x=1;for(int i=2;i<=n;++i)x*=i;return x;}
static bool isprime(u64 n){if(n<2)return false;if(n%2==0)return n==2;for(u64 d=3;d*d<=n;d+=2)if(n%d==0)return false;return true;}
static u64 modpow(u64 a,u64 e,u64 p){u64 r=1;while(e){if(e&1)r=(u128)r*a%p;a=(u128)a*a%p;e>>=1;}return r;}
static u64 cppmod(const cpp_int&x,u64 p){return (x%p).convert_to<u64>();}
struct S{int par=0;array<u64,L>a{};};
static S mul(const S&x,const S&y,u64 p){S z;int ps=x.par+y.par;z.par=ps&1;int sh=ps>>1;for(int n=sh;n<L;++n){u128 acc=0;int t=n-sh;for(int i=0;i<=t;++i)acc+=(u128)x.a[i]*y.a[t-i];z.a[n]=(u64)(acc%p);}return z;}
static void subeq(S&x,const S&y,u64 p){if(x.par!=y.par){cerr<<"PARITY_ADD_FAIL\n";std::exit(2);}for(int i=0;i<L;++i)x.a[i]=(x.a[i]>=y.a[i])?x.a[i]-y.a[i]:x.a[i]+p-y.a[i];}
static S inv_even(const S&x,u64 p){if(x.par||x.a[0]==0){cerr<<"NONUNIT_PIVOT\n";std::exit(3);}S y;y.a[0]=modpow(x.a[0],p-2,p);for(int n=1;n<L;++n){u128 acc=0;for(int i=1;i<=n;++i)acc+=(u128)x.a[i]*y.a[n-i];u64 s=(u64)(acc%p);y.a[n]=(s==0)?0:(u128)(p-s)*y.a[0]%p;}return y;}
struct PR{u64 p;array<array<u64,L>,KMAX+1>tau{};};
static PR runprime(u64 p){
  array<u64,NMAX+KMAX+2>f{},fi{}; f[0]=1;
  for(int i=1;i<(int)f.size();++i)f[i]=(u128)f[i-1]*i%p;
  fi.back()=modpow(f.back(),p-2,p);
  for(int i=(int)f.size()-1;i>=1;--i)fi[i-1]=(u128)fi[i]*i%p;
  vector<vector<S>>A(KMAX,vector<S>(KMAX));
  for(int i=0;i<KMAX;++i)for(int j=0;j<KMAX;++j){int d=std::abs(i-j);S s;s.par=d&1;int b=d/2;for(int r=0;b+r<L&&r+d<(int)fi.size();++r)s.a[b+r]=(u128)fi[r]*fi[r+d]%p;A[i][j]=s;}
  S det;det.a[0]=1;PR out;out.p=p;out.tau[0][0]=1;
  for(int i=0;i<KMAX;++i){S piv=A[i][i];det=mul(det,piv,p);for(int n=0;n<L;++n)out.tau[i+1][n]=det.a[n];S ip=inv_even(piv,p);for(int r=i+1;r<KMAX;++r){S fac=mul(A[r][i],ip,p);for(int c=i+1;c<KMAX;++c){S q=mul(fac,A[i][c],p);subeq(A[r][c],q,p);}}}
  return out;
}
static cpp_int crt(const vector<PR>&R,int k,int n){cpp_int x=R[0].tau[k][n],M=R[0].p;for(size_t q=1;q<R.size();++q){u64 p=R[q].p,xm=cppmod(x,p),mm=cppmod(M,p),iv=modpow(mm,p-2,p),rr=R[q].tau[k][n],delta=(rr>=xm)?rr-xm:rr+p-xm,t=(u128)delta*iv%p;x+=M*t;M*=p;}return x;}
static cpp_int binom(int n,int k){if(k<0||k>n)return 0;if(k>n-k)k=n-k;cpp_int x=1;for(int i=1;i<=k;++i){x*=n-k+i;x/=i;}return x;}
static cpp_int rook_total(int n,int j){return fact_int(j)*binom(n,j)*binom(n,j);}
static long double told(const cpp_int&x){return x.convert_to<long double>();}
int main(){
 auto t0=std::chrono::steady_clock::now();
 vector<u64>primes={1000100009ULL,1000200013ULL,1000300031ULL,1000400053ULL,1000500077ULL,1000600087ULL,1000700101ULL,1000800107ULL,1000900111ULL,1001000113ULL,1001100127ULL,1001200139ULL,1001300143ULL,1001400163ULL,1001500177ULL,1001600179ULL};
 for(size_t i=0;i<primes.size();++i){if(!isprime(primes[i])){cerr<<"NONPRIME_MODULUS\n";return 6;}for(size_t j=0;j<i;++j)if(primes[i]==primes[j]){cerr<<"DUPLICATE_MODULUS\n";return 7;}}
 cout<<"P0282 exact Gessel boundary certificate for normalized shadow-density log-concavity defects 27..32\n";
 cout<<"NMAX="<<NMAX<<" KMAX="<<KMAX<<" modular_primes="<<primes.size()<<"\n";
 vector<std::future<PR>>fut;for(u64 p:primes)fut.push_back(std::async(std::launch::async,[p]{return runprime(p);}));vector<PR>R;for(auto&f:fut)R.push_back(f.get());
 cpp_int M=1;for(u64 p:primes)M*=p;cpp_int fn=fact_int(NMAX);if(M<=2*fn){cerr<<"CRT_RANGE_FAIL\n";return 8;}
 cout<<"CRT_modulus_bits="<<boost::multiprecision::msb(M)+1<<" factorial65_bits="<<boost::multiprecision::msb(fn)+1<<" modulus_gt_2factorial=True\n";
 int checks=0; cpp_int bestNum=0,bestDen=1; int bestj=-1,bestn=-1,bestk=-1; bool set=false;
 for(int n=29;n<=NMAX;++n){
   cpp_int f=fact_int(n),scale=(f*f)%M;
   vector<cpp_int>u(KMAX+1),ell(KMAX+1);
   for(int k=1;k<=KMAX;++k){u[k]=(crt(R,k,n)*scale)%M;if(u[k]>f||u[k]<u[k-1]){cerr<<"COUNT_RANGE_FAIL n="<<n<<" k="<<k<<"\n";return 9;}ell[k]=u[k]-u[k-1];}
   if(u[1]!=1){cerr<<"U1_FAIL n="<<n<<"\n";return 10;}
   cpp_int cat=binom(2*n,n)/(n+1); if(u[2]!=cat){cerr<<"CATALAN_FAIL n="<<n<<"\n";return 11;}
   for(int j=27;j<=32;++j){
     if(n<j+2||n>2*j+1) continue;
     int k=n-j; if(k<2||k+1>KMAX){cerr<<"K_RANGE_FAIL\n";return 12;}
     cpp_int Em=ell[k+1], Ej=ell[k], Ep=ell[k-1];
     cpp_int Rm=rook_total(n,j-1), Rj=rook_total(n,j), Rp=rook_total(n,j+1);
     cpp_int lhs=Ej*Ej*Rm*Rp;
     cpp_int rhs=Em*Ep*Rj*Rj;
     if(lhs<=rhs){cerr<<"DENSITY_LC_FAIL j="<<j<<" n="<<n<<" k="<<k<<"\n";return 13;}
     ++checks;
     if(!set||lhs*bestDen<bestNum*rhs){set=true;bestNum=lhs;bestDen=rhs;bestj=j;bestn=n;bestk=k;}
   }
 }
 if(checks!=177){cerr<<"CHECK_COUNT_FAIL got="<<checks<<"\n";return 14;}
 cout<<"boundary_checks="<<checks<<" all_shadow_density_margins_strictly_positive=True\n";
 cout<<"boundary_min_at_j="<<bestj<<" n="<<bestn<<" k="<<bestk<<" ratio~"<<std::setprecision(18)<<(told(bestNum)/told(bestDen))<<"\n";
 cout<<"boundary_min_ratio_exact="<<bestNum<<"/"<<bestDen<<"\n";
 cout<<"boundary_coverage=all j=27..32 and n=j+2..2j+1\n";
 auto t1=std::chrono::steady_clock::now();cout<<"elapsed_seconds="<<std::chrono::duration<double>(t1-t0).count()<<"\nALL_EXACT_CHECKS_PASS\n";
}
