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
static constexpr int NMAX=112,KMAX=30,L=NMAX+1;
using u64=uint64_t; using u128=unsigned __int128;
static cpp_int fact_int(int n){cpp_int x=1;for(int i=2;i<=n;++i)x*=i;return x;}
static bool isprime(u64 n){if(n<2)return false;if(n%2==0)return n==2;for(u64 d=3;d*d<=n;d+=2)if(n%d==0)return false;return true;}
static u64 modpow(u64 a,u64 e,u64 p){u64 r=1;while(e){if(e&1)r=(u128)r*a%p;a=(u128)a*a%p;e>>=1;}return r;}
static u64 cppmod(const cpp_int&x,u64 p){return (x%p).convert_to<u64>();}
struct S{int par=0;array<u64,L>a{};};
static S mul(const S&x,const S&y,u64 p){S z;int ps=x.par+y.par;z.par=ps&1;int sh=ps>>1;for(int n=sh;n<L;++n){u128 acc=0;int t=n-sh;for(int i=0;i<=t;++i)acc+=(u128)x.a[i]*y.a[t-i];z.a[n]=(u64)(acc%p);}return z;}
static void subeq(S&x,const S&y,u64 p){if(x.par!=y.par){cerr<<"PARITY_ADD_FAIL\n";std::exit(2);}for(int i=0;i<L;++i)x.a[i]=(x.a[i]>=y.a[i])?x.a[i]-y.a[i]:x.a[i]+p-y.a[i];}
static S inv_even(const S&x,u64 p){if(x.par||x.a[0]==0){cerr<<"NONUNIT_PIVOT\n";std::exit(3);}S y;y.a[0]=modpow(x.a[0],p-2,p);for(int n=1;n<L;++n){u128 acc=0;for(int i=1;i<=n;++i)acc+=(u128)x.a[i]*y.a[n-i];u64 ss=(u64)(acc%p);y.a[n]=(ss==0)?0:(u128)(p-ss)*y.a[0]%p;}return y;}
struct PR{u64 p;array<array<u64,L>,KMAX+1>tau{};};
static PR runprime(u64 p){
  array<u64,NMAX+KMAX+2>f{},fi{}; f[0]=1;
  for(int i=1;i<(int)f.size();++i)f[i]=(u128)f[i-1]*i%p;
  fi.back()=modpow(f.back(),p-2,p);
  for(int i=(int)f.size()-1;i>=1;--i)fi[i-1]=(u128)fi[i]*i%p;
  vector<vector<S>>A(KMAX,vector<S>(KMAX));
  for(int i=0;i<KMAX;++i)for(int j=0;j<KMAX;++j){int d=std::abs(i-j);S ss;ss.par=d&1;int b=d/2;for(int r=0;b+r<L&&r+d<(int)fi.size();++r)ss.a[b+r]=(u128)fi[r]*fi[r+d]%p;A[i][j]=ss;}
  S det;det.a[0]=1;PR out;out.p=p;out.tau[0][0]=1;
  for(int i=0;i<KMAX;++i){S piv=A[i][i];det=mul(det,piv,p);for(int n=0;n<L;++n)out.tau[i+1][n]=det.a[n];S ip=inv_even(piv,p);for(int r=i+1;r<KMAX;++r){S fac=mul(A[r][i],ip,p);for(int c=i+1;c<KMAX;++c){S q=mul(fac,A[i][c],p);subeq(A[r][c],q,p);}}}
  return out;
}
static cpp_int crt(const vector<PR>&R,int k,int n){cpp_int x=R[0].tau[k][n],M=R[0].p;for(size_t q=1;q<R.size();++q){u64 p=R[q].p,xm=cppmod(x,p),mm=cppmod(M,p),iv=modpow(mm,p-2,p),rr=R[q].tau[k][n],delta=(rr>=xm)?rr-xm:rr+p-xm,t=(u128)delta*iv%p;x+=M*t;M*=p;}return x;}
static int cutoff(int s){return (s + 4)/5 + 8; /* ceil(s/5+8) */}
static long double told(const cpp_int&x){return x.convert_to<long double>();}
int main(){
 auto t0=std::chrono::steady_clock::now();
 vector<u64>primes={1000001011ULL,1000002043ULL,1000003051ULL,1000004059ULL,1000005067ULL,1000006093ULL,1000007117ULL,1000008127ULL,1000009133ULL,1000010153ULL,1000011161ULL,1000012177ULL,1000013191ULL,1000014193ULL,1000015199ULL,1000016201ULL,1000017203ULL,1000018321ULL,1000019327ULL,1000020337ULL,1000021339ULL};
 for(size_t i=0;i<primes.size();++i){if(!isprime(primes[i])){cerr<<"NONPRIME_MODULUS "<<primes[i]<<"\n";return 6;}for(size_t q=0;q<i;++q)if(primes[q]==primes[i]){cerr<<"DUPLICATE_MODULUS\n";return 7;}}
 cout<<"P0282 affine-tail finite Plancherel exact certificate\n";
 cout<<"cutoff r_s=ceil(s/5+8), s=66..112; candidate 10000*n>=25661*j\n";
 vector<std::future<PR>>fut;for(u64 p:primes)fut.push_back(std::async(std::launch::async,[p]{return runprime(p);}));vector<PR>R;for(auto&f:fut)R.push_back(f.get());
 cpp_int M=1;for(u64 p:primes)M*=p;cpp_int f112=fact_int(112);if(M<=2*f112){cerr<<"CRT_RANGE_FAIL\n";return 8;}
 cout<<"primes="<<primes.size()<<" CRT_bits="<<boost::multiprecision::msb(M)+1<<" factorial112_bits="<<boost::multiprecision::msb(f112)+1<<" modulus_gt_2factorial112=True\n";
 long double worstq=0; bool setfinite=false; int worsts=-1, worstr=-1;
 for(int s=66;s<=112;++s){
   int j=s+1, rr=cutoff(s), k=rr-1;
   cpp_int fs=fact_int(s), scale=(fs*fs)%M;
   cpp_int u=(crt(R,k,s)*scale)%M;
   if(u<0||u>fs){cerr<<"COUNT_RANGE_FAIL s="<<s<<" k="<<k<<"\n";return 9;}
   cpp_int bad=fs-u;
   // Exact lower bound at K0=(15661/10000)j+1, T=(j+39)/5.
   cpp_int kN=cpp_int(15661)*j+10000;
   cpp_int dmN=cpp_int(68305)*j-340000; // 50000*(K0-T)
   cpp_int dp=cpp_int(500000000)*(j-1);
   cpp_int dq=kN*dmN;
   cpp_int xn=cpp_int(15661)*j, xd=10000;
   cpp_int A=xn*dq-xd*dp;
   cpp_int B=xn*(dq+dp);
   cpp_int Dn=cpp_int(j+1)*A*A, Dd=cpp_int(j)*B*B;
   // Tilt bound beta <= (bad/fs)/rho0^2, rho0=(5661j+30000)/(15661j+20000).
   cpp_int rn=cpp_int(5661)*j+30000, rd=cpp_int(15661)*j+20000;
   cpp_int bnum=bad*rd*rd, bden=fs*rn*rn;
   if(bnum>=bden){cerr<<"BETA_GE_ONE s="<<s<<"\n";return 10;}
   cpp_int qn=Dn*(bden-bnum), qd=Dd*bden;
   if(qn<=qd){cerr<<"FINITE_SOURCE_LOWER_FAIL s="<<s<<" r="<<rr<<"\n";return 11;}
   long double ratio=told(qn)/told(qd);
   if(!setfinite || ratio<worstq){setfinite=true; worstq=ratio; worsts=s; worstr=rr;}
 }
 cout<<"finite_combined_source_checks=47 s=66..112 all_Qlower_gt_1=True\n";
 cout<<std::setprecision(18)<<"finite_min_s="<<worsts<<" r="<<worstr<<" Qlower~"<<worstq<<"\n";
 auto t1=std::chrono::steady_clock::now();cout<<"elapsed_seconds="<<std::chrono::duration<double>(t1-t0).count()<<"\nALL_EXACT_CHECKS_PASS\n";
}
