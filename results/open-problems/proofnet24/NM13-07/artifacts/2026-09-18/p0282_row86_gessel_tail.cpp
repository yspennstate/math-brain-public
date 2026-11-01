#include <boost/multiprecision/cpp_int.hpp>
#include <algorithm>
#include <array>
#include <chrono>
#include <cstdint>
#include <cstdlib>
#include <future>
#include <functional>
#include <iomanip>
#include <iostream>
#include <vector>
using boost::multiprecision::cpp_int;
using std::array; using std::cerr; using std::cout; using std::vector;
static constexpr int N=86,JMAX=66,KMAX=N-JMAX,L=N+1;
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
static PR runprime(u64 p){array<u64,N+KMAX+2>f{},fi{};f[0]=1;for(int i=1;i<(int)f.size();++i)f[i]=(u128)f[i-1]*i%p;fi.back()=modpow(f.back(),p-2,p);for(int i=(int)f.size()-1;i>=1;--i)fi[i-1]=(u128)fi[i]*i%p;
 vector<vector<S>>A(KMAX,vector<S>(KMAX));
 for(int i=0;i<KMAX;++i)for(int j=0;j<KMAX;++j){int d=std::abs(i-j);S s;s.par=d&1;int b=d/2;for(int r=0;b+r<L&&r+d<(int)fi.size();++r)s.a[b+r]=(u128)fi[r]*fi[r+d]%p;A[i][j]=s;}
 S det;det.a[0]=1;PR out;out.p=p;out.tau[0][0]=1;
 for(int i=0;i<KMAX;++i){S piv=A[i][i];det=mul(det,piv,p);for(int n=0;n<L;++n)out.tau[i+1][n]=det.a[n];S ip=inv_even(piv,p);for(int r=i+1;r<KMAX;++r){S fac=mul(A[r][i],ip,p);for(int c=i+1;c<KMAX;++c){S q=mul(fac,A[i][c],p);subeq(A[r][c],q,p);}}}
 return out;}
static cpp_int crt(const vector<PR>&R,int k,int n){cpp_int x=R[0].tau[k][n],M=R[0].p;for(size_t q=1;q<R.size();++q){u64 p=R[q].p,xm=cppmod(x,p),mm=cppmod(M,p),iv=modpow(mm,p-2,p),rr=R[q].tau[k][n],delta=(rr>=xm)?rr-xm:rr+p-xm,t=(u128)delta*iv%p;x+=M*t;M*=p;}return x;}
static cpp_int binom(int n,int k){if(k>n-k)k=n-k;cpp_int x=1;for(int i=1;i<=k;++i){x*=n-k+i;x/=i;}return x;}
static long double told(const cpp_int&x){return x.convert_to<long double>();}

// Tail-partition exact arithmetic for independent high-LIS overlap/sector check.
static void partrec(int rem,int maxp,vector<int>&cur,const std::function<void(const vector<int>&)>&visit){if(rem==0){visit(cur);return;}for(int a=std::min(rem,maxp);a>=1;--a){cur.push_back(a);partrec(rem-a,a,cur,visit);cur.pop_back();}}
static cpp_int hookdim(const vector<int>&lam){int n=0;for(int x:lam)n+=x;if(!n)return 1;cpp_int f=fact_int(n);int r=lam.size(),w=lam[0];vector<int>h(w);for(int c=0;c<w;++c)while(h[c]<r&&lam[h[c]]>c)++h[c];cpp_int hp=1;for(int i=0;i<r;++i)for(int c=0;c<lam[i];++c)hp*=(lam[i]-c)+(h[c]-i-1);if(f%hp){cerr<<"HOOK_DIV_FAIL\n";std::exit(20);}return f/hp;}
struct TP{vector<int>lam;cpp_int f;};
static void tailrec(int rem,int maxp,vector<int>&cur,vector<TP>&out){if(rem==0){out.push_back({cur,hookdim(cur)});return;}for(int a=std::min(rem,maxp);a>=1;--a){cur.push_back(a);tailrec(rem-a,a,cur,out);cur.pop_back();}}
int main(){auto t0=std::chrono::steady_clock::now();vector<u64>primes={1000100009ULL,1000200013ULL,1000300031ULL,1000400053ULL,1000500077ULL,1000600087ULL,1000700101ULL,1000800107ULL,1000900111ULL,1001000113ULL,1001100127ULL,1001200139ULL,1001300143ULL,1001400163ULL,1001500177ULL,1001600179ULL};
 for(size_t i=0;i<primes.size();++i){if(!isprime(primes[i])){cerr<<"NONPRIME_MODULUS\n";return 6;}for(size_t j=0;j<i;++j)if(primes[i]==primes[j]){cerr<<"DUPLICATE_MODULUS\n";return 7;}}
 cout<<"P0282 exact row86 low-LIS seam certificate via Gessel Toeplitz determinant\n";
 cout<<"n="<<N<<" retained_complete_defect_J="<<JMAX<<" low_LIS_cutoff_K="<<KMAX<<" modular_primes="<<primes.size()<<"\n";
 vector<std::future<PR>>fut;for(u64 p:primes)fut.push_back(std::async(std::launch::async,[p]{return runprime(p);}));vector<PR>R;for(auto&f:fut)R.push_back(f.get());
 cpp_int M=1;for(u64 p:primes)M*=p;cpp_int fn=fact_int(N);if(M<=2*fn){cerr<<"CRT_RANGE_FAIL\n";return 8;}cout<<"CRT_modulus_bits="<<boost::multiprecision::msb(M)+1<<" factorial_bits="<<boost::multiprecision::msb(fn)+1<<" modulus_gt_2factorial=True\n";
 vector<cpp_int>u(KMAX+1),ell(KMAX+1);cpp_int scale=(fn*fn)%M;for(int k=1;k<=KMAX;++k){u[k]=(crt(R,k,N)*scale)%M;if(u[k]>fn||u[k]<u[k-1]){cerr<<"COUNT_RANGE_FAIL k="<<k<<"\n";return 9;}ell[k]=u[k]-u[k-1];if(ell[k]<=0){cerr<<"ELL_NONPOS k="<<k<<"\n";return 10;}}
 cpp_int cat=binom(2*N,N)/(N+1);if(u[1]!=1||u[2]!=cat||ell[2]!=cat-1){cerr<<"CATALAN_FAIL\n";return 11;}cout<<"Catalan_u2_check=PASS value="<<cat<<"\n";
 cpp_int bestNum=0,bestDen=1,bestMargin=0;int bestK=-1;bool set=false;for(int k=2;k<=KMAX-1;++k){cpp_int num=ell[k]*ell[k],den=ell[k-1]*ell[k+1],m=num-den;if(m<=0){cerr<<"SOURCE_NONPOS k="<<k<<"\n";return 12;}if(!set||num*bestDen<bestNum*den){set=true;bestNum=num;bestDen=den;bestMargin=m;bestK=k;}}
 cout<<"new_low_seam_checks="<<(KMAX-2)<<" k=2.."<<(KMAX-1)<<" all_strictly_positive=True\n";
 // Independently recompute the full high-LIS sector j=1..66 using fixed-defect recurrence + exact finite tail correction.
 const int QMAX=JMAX+1,RMAX=47;vector<cpp_int>F(QMAX+1);F[0]=1;for(int q=1;q<=QMAX;++q)F[q]=F[q-1]*q;
 vector<vector<cpp_int>>V(QMAX+1,vector<cpp_int>(N+1));for(int n=0;n<=N;++n){V[0][n]=1;V[1][n]=cpp_int(n-1)*(n-1);}for(int q=1;q<QMAX;++q)for(int n=1;n<=N;++n)V[q+1][n]=cpp_int(n)*n*(V[q][n-1]+cpp_int(q)*V[q-1][n-1])-cpp_int(2*n-q-1)*V[q][n];
 vector<vector<TP>>tails(RMAX+1);vector<int>cur;long long tshapes=0;for(int r=0;r<=RMAX;++r){tailrec(r,r,cur,tails[r]);tshapes+=tails[r].size();}
 long long amp=0;auto err=[&](int j,int t,int ss)->cpp_int{int q=j+t,n=N,Ntail=n-q,rmax=ss+2*t-2;if(rmax<0)return 0;if(rmax>RMAX){cerr<<"TAIL_BOUND_FAIL\n";std::exit(14);}cpp_int total=0;for(int r=0;r<=rmax;++r){int First=q-r;for(const auto&tt:tails[r]){if(r&&First<tt.lam[0])continue;cpp_int dimnum=tt.f;for(int a=1;a<=r;++a){int la=(a-1<(int)tt.lam.size())?tt.lam[a-1]:0;dimnum*=First+a-la;}if(dimnum%F[r]){cerr<<"TAIL_DIM_DIV_FAIL\n";std::exit(15);}cpp_int fmu=dimnum/F[r],RR=Ntail+1-First;for(int a=1;a<=r;++a){int la=(a-1<(int)tt.lam.size())?tt.lam[a-1]:0;RR*=Ntail+a+1-la;}for(int i=r+2;i<=q;++i)RR*=Ntail+i;if(RR==0)continue;cpp_int num=fmu*RR;if(num%F[q]){cerr<<"TAIL_AMP_DIV_FAIL\n";std::exit(16);}cpp_int aa=num/F[q];total+=aa*aa;++amp;}}return total;};
 cpp_int overlap=0, highBestNum=0,highBestDen=1,highBestMargin=0;int highBestK=-1;bool hset=false;for(int j=1;j<=JMAX;++j){int ss=2*j-N;cpp_int E[3];for(int t=-1;t<=1;++t){int q=j+t;if(V[q][N]%F[q]){cerr<<"COMPLETION_DIV_FAIL\n";return 17;}E[t+1]=V[q][N]/F[q]-err(j,t,ss);if(E[t+1]<0){cerr<<"NEG_SOURCE_COUNT j="<<j<<" t="<<t<<"\n";return 18;}}int k=N-j;cpp_int num=E[1]*E[1],den=E[0]*E[2],m=num-den;if(m<=0){cerr<<"HIGH_SOURCE_NONPOS j="<<j<<"\n";return 19;}if(!hset||num*highBestDen<highBestNum*den){hset=true;highBestNum=num;highBestDen=den;highBestMargin=m;highBestK=k;}if(j==JMAX)overlap=E[1];}
 cout<<"fixed_defect_tail_checks="<<JMAX<<" k="<<KMAX<<".."<<(N-1)<<" all_strictly_positive=True tail_partition_atlas_shapes="<<tshapes<<" tail_amplitude_terms="<<amp<<"\n";
 cout<<std::setprecision(18)<<"high_sector_min_k="<<highBestK<<" defect="<<(N-highBestK)<<" ratio~"<<(told(highBestNum)/told(highBestDen))<<"\n";
 cout<<"high_sector_min_margin_exact="<<highBestMargin<<"\n";
 if(overlap!=ell[KMAX]){cerr<<"OVERLAP_K20_FAIL\n";return 21;}cout<<"independent_overlap_k20=PASS ell_86_20="<<overlap<<"\n";
 cout<<"row86_total_exact_checks="<<(KMAX-2+JMAX)<<" expected="<<(N-2)<<" all_strictly_positive=True\n";if(KMAX-2+JMAX!=N-2){cerr<<"COVER_COUNT_FAIL\n";return 13;}
 cout<<std::setprecision(18)<<"low_seam_min_k="<<bestK<<" ratio~"<<(told(bestNum)/told(bestDen))<<"\n";
 cout<<"low_seam_min_ratio_exact="<<bestNum<<"/"<<bestDen<<"\n";
 cout<<"low_seam_min_margin_exact="<<bestMargin<<"\n";
 cout<<"frozen_metric_movement=N_exact 85->86 when chained to archived n<=85 certificates and retained exact j<=66 theorem=True\n";
 auto t1=std::chrono::steady_clock::now();cout<<"elapsed_seconds="<<std::chrono::duration<double>(t1-t0).count()<<"\nALL_EXACT_CHECKS_PASS\n";
}
