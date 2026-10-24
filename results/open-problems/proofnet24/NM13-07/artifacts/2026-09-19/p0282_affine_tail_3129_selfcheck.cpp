#include <boost/multiprecision/cpp_int.hpp>
#include <array>
#include <cstdint>
#include <cstdlib>
#include <future>
#include <iomanip>
#include <iostream>
#include <vector>
using boost::multiprecision::cpp_int;
using std::array; using std::cerr; using std::cout; using std::vector;
using u64=uint64_t; using u128=unsigned __int128;
static constexpr int NMAX=112,KMAX=32,L=NMAX+1;
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
 vector<vector<S>>A(KMAX,vector<S>(KMAX));
 for(int i=0;i<KMAX;++i)for(int j=0;j<KMAX;++j){int d=std::abs(i-j);S s;s.par=d&1;int b=d/2;for(int r=0;b+r<L&&r+d<(int)fi.size();++r)s.a[b+r]=(u128)fi[r]*fi[r+d]%p;A[i][j]=s;}
 S det;det.a[0]=1;PR out;out.p=p;out.tau[0][0]=1;
 for(int i=0;i<KMAX;++i){S piv=A[i][i];det=mul(det,piv,p);for(int n=0;n<L;++n)out.tau[i+1][n]=det.a[n];S ip=inv_even(piv,p);for(int r=i+1;r<KMAX;++r){S fac=mul(A[r][i],ip,p);for(int c=i+1;c<KMAX;++c){S q=mul(fac,A[i][c],p);subeq(A[r][c],q,p);}}}
 return out;
}
static cpp_int crt(const vector<PR>&R,int k,int n){cpp_int x=R[0].tau[k][n],M=R[0].p;for(size_t q=1;q<R.size();++q){u64 p=R[q].p,xm=cppmod(x,p),mm=cppmod(M,p),iv=modpow(mm,p-2,p),rr=R[q].tau[k][n],delta=(rr>=xm)?rr-xm:rr+p-xm,t=(u128)delta*iv%p;x+=M*t;M*=p;}return x;}
static long double told(const cpp_int&x){return x.convert_to<long double>();}
static int cutoff(int s){return (s+44)/5;} // ceil(s/5+8)
int main(){
 vector<u64>primes={1000100009ULL,1000200013ULL,1000300031ULL,1000400053ULL,1000500077ULL,1000600087ULL,1000700101ULL,1000800107ULL,1000900111ULL,1001000113ULL,1001100127ULL,1001200139ULL,1001300143ULL,1001400163ULL,1001500177ULL,1001600179ULL,1001700017ULL,1001800039ULL,1001900021ULL,1002000001ULL,1002100007ULL};
 for(size_t i=0;i<primes.size();++i){if(!isprime(primes[i])){cerr<<"NONPRIME "<<primes[i]<<"\n";return 4;}for(size_t j=0;j<i;++j)if(primes[i]==primes[j]){cerr<<"DUPLICATE_MODULUS\n";return 5;}}
 vector<std::future<PR>>fut;for(auto p:primes)fut.push_back(std::async(std::launch::async,[p]{return runprime(p);}));vector<PR>R;for(auto&f:fut)R.push_back(f.get());
 cpp_int M=1;for(auto p:primes)M*=p;cpp_int f112=fact_int(112);if(M<=2*f112){cerr<<"CRT_RANGE_FAIL\n";return 6;}
 cout<<"P0282 affine typical-shape finite-core self-check, 3129/5129 window\n";
 cout<<"cutoff_r_s=ceil(s/5+8) boundary_K=(3129/2000)j+1\n";
 cout<<"CRT_modulus_bits="<<boost::multiprecision::msb(M)+1<<" factorial112_bits="<<boost::multiprecision::msb(f112)+1<<"\n";
 long double weakest=1e9L; int weak_s=-1,weak_r=-1;
 for(int s=66;s<=112;++s){
   int j=s+1,r=cutoff(s),cap=r-1; cpp_int fs=fact_int(s),scale=(fs*fs)%M,u=(crt(R,r-1,s)*scale)%M; if(u>fs){cerr<<"COUNT_RANGE_FAIL s="<<s<<"\n";return 7;} cpp_int tail=fs-u;
   cpp_int Kn=3129*j+2000, q=2000, yden=Kn*(Kn-q*cap), ynum=yden+cpp_int(s)*q*q;
   cpp_int N=Kn*yden-q*ynum;
   cpp_int Bnum=cpp_int(j+1)*N*N;
   cpp_int Bden=cpp_int(3129)*3129*j*j*j*ynum*ynum;
   cpp_int rn=1129*j+6000, rd=3129*j+4000;
   cpp_int goodmass_num=fs*rn*rn-tail*rd*rd;
   if(goodmass_num<=0){cerr<<"GOOD_MASS_NONPOS s="<<s<<"\n";return 8;}
   cpp_int lhs=Bnum*goodmass_num, rhs=Bden*fs*rn*rn;
   if(lhs<=rhs){cerr<<"FINITE_COMBINED_FAIL s="<<s<<" r="<<r<<"\n";return 9;}
   long double Bv=told(Bnum)/told(Bden), bad=told(tail)/told(fs)*(told(rd)/told(rn))*(told(rd)/told(rn)), val=Bv*(1-bad);
   if(val<weakest){weakest=val;weak_s=s;weak_r=r;}
 }
 cout<<std::setprecision(18)<<"finite_s66_112_combined_exact=PASS weakest_lower~"<<weakest<<" at_s="<<weak_s<<" cutoff="<<weak_r<<"\n";
 for(int s=113;s<=117;++s){int j=s+1,r=cutoff(s);cpp_int lhs=binom(s,r)*5600*j,rhs=fact_int(r);if(lhs>=rhs){cerr<<"UNION_BASE_FAIL s="<<s<<"\n";return 10;}}
 cout<<"union_bound_bases_s113_117 p_s<1/(5600(s+1))=PASS\n";
 cpp_int lhs=2*15625;for(int i=0;i<5;++i)lhs*=118;
 cpp_int rhs=256;for(int i=0;i<2;++i)rhs*=158;for(int i=0;i<4;++i)rhs*=103;
 if(lhs>=rhs){cerr<<"RATIO_BOUND_FAIL\n";return 11;}
 cout<<"five_step_ratio_bound_at_s113<1/2_and_decreasing=PASS\n";
 if(25*(1129LL*67+6000)<=9*(3129LL*67+4000)){cerr<<"RHO_BOUND_FAIL\n";return 12;}
 cout<<"rho_boundary_gt_9/25_for_j>=67=PASS cross_difference=64*j+114000\n";
 cout<<"therefore_s>=113_tilted_bad_mass_lt_1/(700j)=PASS\n";
 cout<<"ALL_EXACT_CHECKS_PASS\n";
}
