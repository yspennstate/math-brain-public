// R7-06 / F0011 exact n=9 certificate.
//
// Exhaustively classifies every diagonal-switching-normalized symmetric {+/-1}
// 9x9 matrix.  No floating-point eigenvalue calculation is used.
//
// 1. Generate all unlabeled graphs through order 8 by exact canonical
//    augmentation.  Known class counts 1,1,2,4,11,34,156,1044,12346 are
//    asserted; completeness also follows inductively because deleting one
//    vertex from every k-vertex graph reaches a represented (k-1)-vertex graph.
// 2. Weight each order-8 graph by 8!/|Aut(G)|, so the weighted mass is 2^28.
// 3. Add all 2^9 diagonal sign patterns.  The total switching-normalized mass
//    is therefore 2^37.
// 4. Enumerate every possible integral spectrum exactly.  For an integral
//    spectrum lambda of a 9x9 sign matrix: |lambda_i|<=9, sum lambda_i^2=81,
//    and exactly one lambda_i is odd because M mod 2 = J_9 and
//    chi_{J_9}(x)=x^8(x-1) over F_2.
// 5. Match exact power sums tr(M^k), k=1,...,9.  Newton identities imply that
//    these determine the characteristic polynomial, so a match is an exact
//    integrality certificate.  p3 and M^2 are evaluated by closed formulas;
//    the remaining powers use integer matrix multiplication only.

#include <algorithm>
#include <array>
#include <chrono>
#include <cstdint>
#include <cstdlib>
#include <functional>
#include <iomanip>
#include <iostream>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>

using i64 = long long;
using u64 = unsigned long long;
static int PI[9][9][9];

static void init_pi(){
  for(int n=0;n<=8;++n){int b=0;for(int i=0;i<n;++i)for(int j=i+1;j<n;++j)PI[n][i][j]=PI[n][j][i]=b++;}
}

static uint32_t perm_code(uint32_t code,int n,const std::vector<int>&p){
  uint32_t out=0;int b=0;
  for(int a=0;a<n;++a)for(int c=a+1;c<n;++c){int i=p[a],j=p[c];if(i>j)std::swap(i,j);if((code>>PI[n][i][j])&1u)out|=1u<<b;++b;}
  return out;
}

// Isomorphisms preserve degree.  Put degree classes in increasing order and
// enumerate every permutation within equal-degree classes; the minimum bit
// string is therefore a complete canonical label for n<=8.
static uint32_t canon(uint32_t code,int n){
  int d[8]={0};
  for(int i=0;i<n;++i)for(int j=i+1;j<n;++j)if((code>>PI[n][i][j])&1u){++d[i];++d[j];}
  std::vector<std::pair<int,int>> dv;for(int i=0;i<n;++i)dv.push_back({d[i],i});std::sort(dv.begin(),dv.end());
  std::vector<int> p(n);std::vector<std::pair<int,int>> spans;int pos=0;
  for(int a=0;a<n;){int b=a,s=pos;while(b<n&&dv[b].first==dv[a].first)p[pos++]=dv[b++].second;spans.push_back({s,pos});a=b;}
  uint32_t best=UINT32_MAX;
  std::function<void(int)> rec=[&](int g){
    if(g==(int)spans.size()){best=std::min(best,perm_code(code,n,p));return;}
    auto [s,e]=spans[g];std::sort(p.begin()+s,p.begin()+e);do rec(g+1);while(std::next_permutation(p.begin()+s,p.begin()+e));
  };rec(0);return best;
}

static std::vector<uint32_t> unlabeled(int n){
  static const int expected[9]={1,1,2,4,11,34,156,1044,12346};
  std::vector<uint32_t> r={0};
  for(int k=1;k<=n;++k){
    std::unordered_set<uint32_t> nxt;nxt.reserve(expected[k]*2);
    for(uint32_t old:r){
      uint32_t base=0;
      for(int i=0;i<k-1;++i)for(int j=i+1;j<k-1;++j)if((old>>PI[k-1][i][j])&1u)base|=1u<<PI[k][i][j];
      for(int mask=0;mask<(1<<(k-1));++mask){uint32_t c=base;for(int i=0;i<k-1;++i)if((mask>>i)&1)c|=1u<<PI[k][i][k-1];nxt.insert(canon(c,k));}
    }
    r.assign(nxt.begin(),nxt.end());std::sort(r.begin(),r.end());
    if((int)r.size()!=expected[k]){std::cerr<<"UNLABELED_COUNT_MISMATCH n="<<k<<" got="<<r.size()<<" expected="<<expected[k]<<"\n";std::exit(2);}
  }
  return r;
}

static int aut_size(uint32_t code,int n){
  int d[8]={0};for(int i=0;i<n;++i)for(int j=i+1;j<n;++j)if((code>>PI[n][i][j])&1u){++d[i];++d[j];}
  std::vector<std::pair<int,int>> dv;for(int i=0;i<n;++i)dv.push_back({d[i],i});std::sort(dv.begin(),dv.end());
  std::vector<int> p(n);std::vector<std::pair<int,int>> spans;int pos=0;
  for(int a=0;a<n;){int b=a,s=pos;while(b<n&&dv[b].first==dv[a].first)p[pos++]=dv[b++].second;spans.push_back({s,pos});a=b;}
  int ans=0;std::function<void(int)> rec=[&](int g){
    if(g==(int)spans.size()){ans+=(perm_code(code,n,p)==code);return;}
    auto [s,e]=spans[g];std::sort(p.begin()+s,p.begin()+e);do rec(g+1);while(std::next_permutation(p.begin()+s,p.begin()+e));
  };rec(0);return ans;
}

struct Key{std::array<i64,9> p{};bool operator==(Key const&o)const{return p==o.p;}};
struct KH{size_t operator()(Key const&k)const{uint64_t h=1469598103934665603ull;for(i64 x:k.p){uint64_t y=(uint64_t)(x^(x>>32));h^=y;h*=1099511628211ull;}return(size_t)h;}};
struct P3{i64 a,b,c;bool operator==(P3 const&o)const{return a==o.a&&b==o.b&&c==o.c;}};
struct P3H{size_t operator()(P3 const&k)const{return(uint64_t)(k.a+32)*1000003ull^(uint64_t)(k.b+100000)*9176ull^(uint64_t)k.c*1315423911ull;}};
struct P4{i64 a,b,c,d;bool operator==(P4 const&o)const{return a==o.a&&b==o.b&&c==o.c&&d==o.d;}};
struct P4H{size_t operator()(P4 const&k)const{return P3H{}({k.a,k.b,k.c})^((uint64_t)k.d*0x9e3779b97f4a7c15ULL);}};
static i64 ipow(i64 x,int e){i64 y=1;while(e--)y*=x;return y;}

static void cand_rec(int pos,int last,int sq,std::array<i64,9>&lam,std::vector<std::array<i64,9>>&L,std::vector<Key>&K){
  if(pos==9){
    if(sq!=81)return;int odd=0;i64 tr=0;for(i64 x:lam){odd+=(std::llabs(x)&1ll);tr+=x;}if(odd!=1||std::llabs(tr)>9||((tr-9)&1ll))return;
    Key q;for(int e=1;e<=9;++e){i64 s=0;for(i64 x:lam)s+=ipow(x,e);q.p[e-1]=s;}L.push_back(lam);K.push_back(q);return;
  }
  for(int x=last;x<=9;++x){int ns=sq+x*x;if(ns<=81){lam[pos]=x;cand_rec(pos+1,x,ns,lam,L,K);}}
}

static void mul9(const i64 A[9][9],const i64 B[9][9],i64 C[9][9]){for(int i=0;i<9;++i)for(int j=0;j<9;++j){i64 s=0;for(int k=0;k<9;++k)s+=A[i][k]*B[k][j];C[i][j]=s;}}
static i64 tr9(const i64 A[9][9]){i64 s=0;for(int i=0;i<9;++i)s+=A[i][i];return s;}
static i64 trMA(const int M[9][9],const i64 A[9][9]){i64 s=0;for(int i=0;i<9;++i)for(int j=0;j<9;++j)s+=(i64)M[i][j]*A[j][i];return s;}

int main(){
  init_pi();auto started=std::chrono::steady_clock::now();
  auto graphs=unlabeled(8);
  std::cout<<"F0011 exact n=9 switching-normalized integral-spectrum census\n";
  std::cout<<"unlabeled_graph_counts_through_8=1,1,2,4,11,34,156,1044,"<<graphs.size()<<"\n";

  std::array<i64,9> lam{};std::vector<std::array<i64,9>> spectra;std::vector<Key> cp;
  cand_rec(0,-9,0,lam,spectra,cp);
  std::unordered_map<Key,int,KH> full;std::unordered_set<P3,P3H> pre3;std::unordered_set<P4,P4H> pre4;
  for(int i=0;i<(int)cp.size();++i){if(!full.emplace(cp[i],i).second){std::cerr<<"POWER_SUM_COLLISION\n";return 3;}auto&p=cp[i].p;pre3.insert({p[0],p[2],p[3]});pre4.insert({p[0],p[2],p[3],p[4]});}
  std::cout<<"candidate_integral_spectra="<<spectra.size()<<" distinct_p1p3p4="<<pre3.size()<<" distinct_p1p3p4p5="<<pre4.size()<<"\n";
  if(spectra.size()!=258||pre3.size()!=258||pre4.size()!=258)return 4;

  std::vector<u64> sc(spectra.size(),0);u64 integral=0,total=0,graphmass=0;i64 pass4=0,pass5=0,hits=0;
  for(uint32_t code:graphs){
    int aut=aut_size(code,8);if(aut<=0||40320%aut)return 5;u64 w=40320/aut;graphmass+=w;total+=w*512ull;
    int A[9][9]={{0}};for(int j=1;j<9;++j)A[0][j]=A[j][0]=1;
    for(int i=0;i<8;++i)for(int j=i+1;j<8;++j){int s=((code>>PI[8][i][j])&1u)?1:-1;A[i+1][j+1]=A[j+1][i+1]=s;}
    i64 T=0;for(int i=0;i<9;++i)for(int j=i+1;j<9;++j)for(int k=j+1;k<9;++k)T+=(i64)A[i][j]*A[j][k]*A[k][i];
    int c[9][9]={{0}};for(int i=0;i<9;++i)for(int j=i+1;j<9;++j){int z=0;for(int k=0;k<9;++k)if(k!=i&&k!=j)z+=A[i][k]*A[k][j];c[i][j]=c[j][i]=z;}
    for(int mask=0;mask<512;++mask){
      int d[9],M[9][9],p1=0;for(int i=0;i<9;++i){d[i]=((mask>>i)&1)?1:-1;p1+=d[i];for(int j=0;j<9;++j)M[i][j]=A[i][j];M[i][i]=d[i];}
      i64 p3=25ll*p1+6ll*T;
      i64 B[9][9];for(int i=0;i<9;++i)for(int j=0;j<9;++j)B[i][j]=(i==j)?9:(i64)A[i][j]*(d[i]+d[j])+c[i][j];
      i64 p4=0;for(int i=0;i<9;++i)for(int j=0;j<9;++j)p4+=B[i][j]*B[j][i];if(!pre3.count({p1,p3,p4}))continue;++pass4;
      i64 C[9][9];mul9(B,B,C);i64 p5=trMA(M,C);if(!pre4.count({p1,p3,p4,p5}))continue;++pass5;
      i64 D[9][9];mul9(B,C,D);i64 p6=tr9(D),p7=trMA(M,D);i64 E[9][9];mul9(C,C,E);i64 p8=tr9(E),p9=trMA(M,E);
      Key q{{(i64)p1,81,p3,p4,p5,p6,p7,p8,p9}};auto it=full.find(q);if(it!=full.end()){++hits;integral+=w;sc[it->second]+=w;}
    }
  }
  if(graphmass!=(1ull<<28)||total!=(1ull<<37))return 6;
  int realized=0;u64 fmax=0;std::vector<std::pair<u64,int>> ranked;for(int i=0;i<(int)sc.size();++i)if(sc[i]){++realized;fmax=std::max(fmax,sc[i]);ranked.push_back({sc[i],i});}
  std::sort(ranked.rbegin(),ranked.rend());
  std::cout<<"labeled_residual_graph_mass="<<graphmass<<" expected=268435456\n";
  std::cout<<"normalized_total="<<total<<" expected=137438953472\n";
  std::cout<<"prefix_survivors_unweighted: p1p3p4="<<pass4<<" p1p3p4p5="<<pass5<<" integral_hits="<<hits<<"\n";
  std::cout<<"integral_normalized_labeled="<<integral<<" expected=3685058\n";
  std::cout<<"exact_probability=1842529/68719476736\n";
  std::cout<<"realized_integral_spectra="<<realized<<" expected=124\n";
  std::cout<<"max_fixed_spectrum_normalized_mass="<<fmax<<" expected=317520\nmax_spectra:\n";
  for(auto [cnt,id]:ranked){if(cnt!=fmax)break;std::cout<<cnt<<" :";for(i64 x:spectra[id])std::cout<<" "<<x;std::cout<<"\n";}
  if(integral!=3685058ull||realized!=124||fmax!=317520ull||hits!=1066)return 7;
  std::cout<<"runtime_seconds="<<std::fixed<<std::setprecision(3)<<std::chrono::duration<double>(std::chrono::steady_clock::now()-started).count()<<"\n";
  std::cout<<"ALL_EXACT_ASSERTIONS_PASS\n";
  return 0;
}
