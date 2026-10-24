#include <boost/multiprecision/cpp_int.hpp>
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <limits>
#include <map>
#include <string>
#include <unordered_map>
#include <utility>
#include <vector>
using namespace std;
using boost::multiprecision::cpp_int;
using i64=long long;
static constexpr int NVAR=7, NV=128, HALF=64, B_CUTOFF=80, DMAX=64*79, QLOG=(1<<20);
static constexpr i64 INF=numeric_limits<i64>::max()/4;
static const vector<int> PRIMES={2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61};

cpp_int ipow(int base,int exp){cpp_int b=base,r=1;while(exp){if(exp&1)r*=b;exp>>=1;if(exp)b*=b;}return r;}
map<int,int> lf;
void init_logs(){for(int p:PRIMES){if(p==2){lf[p]=QLOG;continue;}cpp_int z=ipow(p,QLOG);lf[p]=boost::multiprecision::msb(z);}}
map<int,int> factor_int(int x){map<int,int> f;for(int p:PRIMES)while(x%p==0){f[p]++;x/=p;}assert(x==1);return f;}
i64 log_lo(int a){if(a<=1)return 0;i64 s=0;for(auto [p,e]:factor_int(a))s+=(i64)e*lf[p];return s;}
i64 log_hi(int a){if(a<=1)return 0;i64 s=0;for(auto [p,e]:factor_int(a))s+=(i64)e*(p==2?lf[p]:lf[p]+1);return s;}
i64 t_lo(int a){return a<=1?0:(i64)a*a*log_lo(a);}
int pc(unsigned x){return __builtin_popcount(x);} 
int gbd(int m){int s=0;for(int i=0;i<m;i++)s+=pc((unsigned)i);return 7*m-2*s;}
int comb7(int d){static int c[8]={1,7,21,35,35,21,7,1};return c[d];}

vector<i64> group_dp(int m,int cnt,int Q){
 vector<int> av;for(int a=(m&1);a<=m;a+=2)av.push_back(a);
 vector<i64> dp(Q+1,INF),nd(Q+1,INF);dp[0]=0;
 for(int rep=0;rep<cnt;rep++){
  fill(nd.begin(),nd.end(),INF);
  for(int s=0;s<=Q;s++)if(dp[s]<INF){
   for(int a:av){int q=a*a;if(s+q>Q)break;i64 nv=dp[s]+t_lo(a);if(nv<nd[s+q])nd[s+q]=nv;}
  }
  dp.swap(nd);
 }
 return dp;
}

vector<i64> minT_by_B(int m){
 int Q=m*(128-m); const long long BASE=DMAX+1;
 vector<vector<pair<int,i64>>> opts(8);
 for(int d=1;d<=7;d++){
  auto gd=group_dp(m,comb7(d),Q);
  for(int q=0;q<=Q;q++)if(gd[q]<INF)opts[d].push_back({q,gd[q]});
 }
 unordered_map<long long,i64> dp,nd;dp.reserve(100000);dp[0]=0;
 for(int d=1;d<=7;d++){
  nd.clear(); size_t est=min<size_t>(8000000,max<size_t>(1000,dp.size()*2));nd.reserve(est);
  for(auto &kv:dp){int qs=kv.first/BASE,ds=kv.first%BASE;i64 v=kv.second;
   for(auto &ot:opts[d]){int q=ot.first,nq=qs+q;if(nq>Q)break;int nds=ds+d*q;if(nds>DMAX)continue;long long key=(long long)nq*BASE+nds;i64 nv=v+ot.second;auto it=nd.find(key);if(it==nd.end()||nv<it->second)nd[key]=nv;}
  }
  dp.swap(nd);
 }
 vector<i64> ans(B_CUTOFF,INF);
 for(int B=0;B<B_CUTOFF;B++){long long key=(long long)Q*BASE+64*B;auto it=dp.find(key);if(it!=dp.end())ans[B]=it->second;}
 return ans;
}

i64 Llo(int m,int B,i64 Tnon){
 int a0=64-m; i64 T0=t_lo(a0);
 i64 exact=(i64)24576*(B-7)*QLOG;
 i64 neg=(i64)3969*B*log_hi(63);
 return exact+7*(T0+Tnon)-neg;
}

array<int,128> walsh_gamma(int m){
 array<int,128> f{},W{};for(int x=0;x<128;x++)f[x]=(x<m)?-1:1;
 for(int s=0;s<128;s++){int z=0;for(int x=0;x<128;x++)z+=((pc((unsigned)(s&x))&1)?-1:1)*f[x];W[s]=z;}return W;
}
int boundary_gamma(int m){int B=0;for(int x=0;x<m;x++)for(int i=0;i<7;i++)if((x^(1<<i))>=m)B++;return B;}
i64 gamma_Llo(int m){auto W=walsh_gamma(m);int B=boundary_gamma(m);i64 T=0;for(int s=0;s<128;s++)T+=t_lo(abs(W[s])/2);return (i64)24576*(B-7)*QLOG+7*T-(i64)3969*B*log_hi(63);}

int main(int argc,char**argv){
 init_logs(); int lo=1,hi=64;if(argc>1)lo=atoi(argv[1]);if(argc>2)hi=atoi(argv[2]);
 cout<<"C7_PARTIAL_EXACT_VERIFIER range="<<lo<<".."<<hi<<" QLOG="<<QLOG<<"\n";
 // high-boundary certificate: C7* - h2(5/28)/(5/28)>0, times 1120.
 // =110336 -39690 log2 3 +1120 log2 5 -26117 log2 7 +5152 log2 23.
 i64 high=(i64)110336*QLOG-(i64)39690*log_hi(3)+(i64)1120*log_lo(5)-(i64)26117*log_hi(7)+(i64)5152*log_lo(23);
 cout<<"highB_gap_1120Q_lower_num="<<high<<"\n";
 cout<<"HIGH_B_B>=80_CERTIFICATE="<<(high>0?"PASS":"FAIL")<<"\n";
 if(high<=0)return 4;
 int total=0,cert=0,imp=0,un=0,gamma_cert=0;
 vector<pair<int,int>> residual;
 for(int m=lo;m<=hi;m++){
  int gg=gbd(m);if(gg>=80)continue;
  auto ans=minT_by_B(m);
  for(int B=gg;B<80;B+=2){total++;
   if(ans[B]>=INF){imp++;cout<<"cell m="<<m<<" B="<<B<<" MOMENT_IMPOSSIBLE\n";continue;}
   i64 L=Llo(m,B,ans[B]);
   if(L>0){cert++;cout<<"cell m="<<m<<" B="<<B<<" RELAX_CERT Lnum="<<L<<"\n";}
   else {un++;residual.push_back({m,B});cout<<"cell m="<<m<<" B="<<B<<" RELAX_UNRES Lnum="<<L<<"\n";}
  }
 }
 vector<pair<int,int>> res2;
 for(auto [m,B]:residual){
   if(B==gbd(m)){
     int bg=boundary_gamma(m);assert(bg==B);
     i64 L=gamma_Llo(m);
     if(m==1 && B==7){cout<<"gamma m=1 B=7 EXACT_ONEPOINT_EQUALITY\n";}
     else if(L>0){gamma_cert++;cout<<"gamma m="<<m<<" B="<<B<<" HARPER_EQUALITY_CLASS_CERT Lnum="<<L<<"\n";}
     else {cout<<"gamma m="<<m<<" B="<<B<<" STILL_UNRES Lnum="<<L<<"\n";res2.push_back({m,B});}
   } else res2.push_back({m,B});
 }
 cout<<"SUMMARY range="<<lo<<".."<<hi<<" formal_lowB_cells="<<total<<" relax_cert="<<cert<<" moment_impossible="<<imp<<" relax_unresolved="<<un<<" harper_min_cert="<<gamma_cert<<" final_residual="<<res2.size()<<"\n";
 cout<<"FINAL_RESIDUALS";for(auto [m,B]:res2)cout<<" ("<<m<<","<<B<<")";cout<<"\n";
 return 0;
}
