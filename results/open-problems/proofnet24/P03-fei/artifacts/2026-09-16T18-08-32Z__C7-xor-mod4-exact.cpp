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
using namespace std; using boost::multiprecision::cpp_int; using i64=long long;
static constexpr int DMAX=64*79,QLOG=(1<<20); static constexpr i64 INF=numeric_limits<i64>::max()/4;
static const vector<int> PR={2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61};
cpp_int ipow(int b,int e){cpp_int r=1,x=b;while(e){if(e&1)r*=x;e>>=1;if(e)x*=x;}return r;}
map<int,int> lf; void init_logs(){for(int p:PR){if(p==2)lf[p]=QLOG;else lf[p]=boost::multiprecision::msb(ipow(p,QLOG));}}
map<int,int> factor_int(int x){map<int,int> f;for(int p:PR)while(x%p==0){f[p]++;x/=p;}assert(x==1);return f;}
i64 log_lo(int a){if(a<=1)return 0;i64 s=0;for(auto [p,e]:factor_int(a))s+=(i64)e*lf[p];return s;}
i64 log_hi(int a){if(a<=1)return 0;i64 s=0;for(auto [p,e]:factor_int(a))s+=(i64)e*(p==2?lf[p]:lf[p]+1);return s;}
i64 t_lo(int a){return a<=1?0:(i64)a*a*log_lo(a);} 
int C(int n,int k){if(k<0||k>n)return 0;static int c[8][8];static bool z=false;if(!z){for(int i=0;i<8;i++){c[i][0]=c[i][i]=1;for(int j=1;j<i;j++)c[i][j]=c[i-1][j-1]+c[i-1][j];}z=true;}return c[n][k];}
int Kraw(int d,int w){int s=0;for(int j=0;j<=d;j++)s += ((j&1)?-1:1)*C(w,j)*C(7-w,d-j); return s;}
pair<int,int> counts(int d,int w){int tot=C(7,d),k=Kraw(d,w);assert(((tot+k)&1)==0);return {(tot+k)/2,(tot-k)/2};}
vector<i64> group_dp(int m,int cnt,int Q,int residue){
 vector<int> av;for(int a=residue;a<=m;a+=4)av.push_back(a);if(av.empty()) return vector<i64>(Q+1,INF);
 vector<i64> dp(Q+1,INF),nd(Q+1,INF);dp[0]=0;
 for(int rep=0;rep<cnt;rep++){fill(nd.begin(),nd.end(),INF);for(int s=0;s<=Q;s++)if(dp[s]<INF){for(int a:av){int q=a*a;if(s+q>Q)break;i64 nv=dp[s]+t_lo(a);if(nv<nd[s+q])nd[s+q]=nv;}}dp.swap(nd);}return dp;
}
vector<i64> minT(int m,int w){assert((m&1)==0);int Q=m*(128-m);const long long BASE=DMAX+1;struct G{int d,cnt,res;vector<pair<int,i64>> o;}; vector<G> gs;
 for(int d=1;d<=7;d++){auto [c0,c1]=counts(d,w);for(int e=0;e<2;e++){int cnt=e?c1:c0;if(!cnt)continue;int r=(m-2*e)%4;if(r<0)r+=4;auto gd=group_dp(m,cnt,Q,r);G g{d,cnt,r,{}};for(int q=0;q<=Q;q++)if(gd[q]<INF)g.o.push_back({q,gd[q]});gs.push_back(move(g));}}
 unordered_map<long long,i64> dp,nd;dp.reserve(100000);dp[0]=0;for(auto &g:gs){nd.clear();nd.reserve(min<size_t>(8000000,max<size_t>(1000,dp.size()*2)));for(auto &kv:dp){int qs=kv.first/BASE,ds=kv.first%BASE;i64 v=kv.second;for(auto &ot:g.o){int q=ot.first,nq=qs+q;if(nq>Q)break;int nds=ds+g.d*q;if(nds>DMAX)continue;long long key=(long long)nq*BASE+nds;i64 nv=v+ot.second;auto it=nd.find(key);if(it==nd.end()||nv<it->second)nd[key]=nv;}}dp.swap(nd);}vector<i64> ans(80,INF);for(int B=0;B<80;B++){auto it=dp.find((long long)Q*BASE+64*B);if(it!=dp.end())ans[B]=it->second;}return ans;}
i64 Llo(int m,int B,i64 Tnon){int a0=64-m;i64 T0=t_lo(a0);return 24576LL*(B-7)*QLOG+7*(T0+Tnon)-3969LL*B*log_hi(63);} 
int main(){
 init_logs();
 map<int,vector<int>> residual={
  {14,{50,52,54,56}}, {16,{50,52,54,56,58,60}}, {18,{58,60,62,64}},
  {20,{62,64,66,68}}, {22,{66,68,70}}, {24,{66,68,70,72,74}},
  {26,{70,72,74}}, {28,{70,72,74,76}}, {30,{70,72,74,76}},
  {32,{66,68,70,72,74,76}}, {34,{74,76}}
 };
 vector<pair<int,int>> expected={
  {14,56},{16,60},{18,64},{20,68},{24,72},{24,74},{26,74},
  {28,74},{28,76},{30,76},{32,74},{32,76},{34,74},{34,76}
 };
 map<pair<int,int>,i64> worstLower;
 map<pair<int,int>,bool> anyState;
 for(auto &mb:residual){
   int m=mb.first;
   for(int B:mb.second){ worstLower[{m,B}]=INF; anyState[{m,B}]=false; }
   for(int w=0;w<=7;w++){
     auto a=minT(m,w);
     for(int B:mb.second){
       if(a[B]>=INF) continue;
       anyState[{m,B}]=true;
       i64 L=Llo(m,B,a[B]);
       worstLower[{m,B}]=min(worstLower[{m,B}],L);
     }
   }
 }
 vector<pair<int,int>> cert,open;
 cout<<"P03_C7_XOR_MOD4_EXACT_CERTIFICATE\n";
 for(auto &mb:residual){
   int m=mb.first;
   for(int B:mb.second){
     auto key=make_pair(m,B);
     if(!anyState[key] || worstLower[key]>0){
       cert.push_back(key);
       cout<<"NEW_CERT m="<<m<<" B="<<B<<" universal_Lnum="<<(anyState[key]?worstLower[key]:INF)<<"\n";
     } else {
       open.push_back(key);
       cout<<"STILL_OPEN m="<<m<<" B="<<B<<" relaxation_Lnum="<<worstLower[key]<<"\n";
     }
   }
 }
 sort(cert.begin(),cert.end()); sort(expected.begin(),expected.end());
 cout<<"EVEN_RESIDUAL_INPUT_COUNT="<<(cert.size()+open.size())<<"\n";
 cout<<"MOD4_NEW_CERT_COUNT="<<cert.size()<<"\n";
 cout<<"MOD4_EVEN_STILL_OPEN_COUNT="<<open.size()<<"\n";
 cout<<"NEW_CERT_LIST"; for(auto [m,B]:cert) cout<<" ("<<m<<","<<B<<")"; cout<<"\n";
 if(cert!=expected){ cerr<<"unexpected certified cell set\n"; return 2; }
 if(cert.size()!=14 || open.size()!=31){ cerr<<"unexpected counts\n"; return 3; }
 cout<<"P03-C7-XOR-MOD4-CERTIFICATE=PASS\n";
 return 0;
}
