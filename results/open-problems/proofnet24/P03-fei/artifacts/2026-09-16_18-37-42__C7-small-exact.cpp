#include <boost/multiprecision/cpp_int.hpp>
#include <bits/stdc++.h>
using namespace std; using boost::multiprecision::cpp_int; using i64=long long;
static constexpr int QLOG=1<<20;
static const vector<int> PR={2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61};
cpp_int ipow(int b,int e){cpp_int x=b,r=1;while(e){if(e&1)r*=x;e>>=1;if(e)x*=x;}return r;}
map<int,int> lf; void logs(){for(int p:PR){if(p==2)lf[p]=QLOG;else lf[p]=boost::multiprecision::msb(ipow(p,QLOG));}}
map<int,int> fac(int x){map<int,int>f;for(int p:PR)while(x%p==0){f[p]++;x/=p;}assert(x==1);return f;}
i64 llo(int a){if(a<=1)return 0;i64 z=0;for(auto[p,e]:fac(a))z+=(i64)e*lf[p];return z;}
i64 lhi(int a){if(a<=1)return 0;i64 z=0;for(auto[p,e]:fac(a))z+=(i64)e*(p==2?lf[p]:lf[p]+1);return z;}
i64 tlo(int a){return a<=1?0:(i64)a*a*llo(a);} 
struct M{uint64_t a,b; bool operator==(M const&o)const{return a==o.a&&b==o.b;}};struct H{size_t operator()(M const&m)const noexcept{return m.a*0x9e3779b97f4a7c15ULL ^ (m.b+0x517cc1b727220a95ULL+(m.a<<6)+(m.a>>2));}};
inline bool has(M m,int v){return v<64?((m.a>>v)&1):((m.b>>(v-64))&1);} inline void add(M&m,int v){if(v<64)m.a|=1ULL<<v;else m.b|=1ULL<<(v-64);} 
int pop(M m){return __builtin_popcountll(m.a)+__builtin_popcountll(m.b);} 
int edges(M m){int e2=0;for(int v=0;v<128;v++)if(has(m,v))for(int i=0;i<7;i++)if(has(m,v^(1<<i)))e2++;return e2/2;}
i64 Lmask(M m){int mm=pop(m),e=edges(m),B=7*mm-2*e; i64 T=tlo(64-mm);for(int s=1;s<128;s++){int F=0;for(int x=0;x<128;x++)if(has(m,x))F+=((__builtin_popcount((unsigned)(s&x))&1)?-1:1);T+=tlo(abs(F));}return (i64)24576*(B-7)*QLOG+7*T-(i64)3969*B*lhi(63);}
int main(){logs();unordered_set<M,H> lay,nxt;lay.reserve(10);lay.insert({1,0});map<pair<int,int>,pair<long long,i64>> stat;
 for(int k=1;k<=8;k++){
   for(auto m:lay){int e=edges(m);bool target=(k==4&&e==3)||(k==6&&e==6)||(k==7&&e==8)||(k==8&&(e==9||e==10||e==11)); if(target){auto key=make_pair(k,e);i64 L=Lmask(m);auto &q=stat[key];if(q.first==0)q.second=L;else q.second=min(q.second,L);q.first++;}}
   cout<<"connected_layer k="<<k<<" count="<<lay.size()<<"\n";if(k==8)break;
   nxt.clear();nxt.reserve(lay.size()*5);
   for(auto m:lay){uint64_t ca=0,cb=0;for(int v=0;v<128;v++)if(has(m,v))for(int i=0;i<7;i++){int w=v^(1<<i);if(!has(m,w)){if(w<64)ca|=1ULL<<w;else cb|=1ULL<<(w-64);}}uint64_t z=ca;while(z){int t=__builtin_ctzll(z);z&=z-1;M q=m;add(q,t);nxt.insert(q);}z=cb;while(z){int t=__builtin_ctzll(z);z&=z-1;M q=m;add(q,t+64);nxt.insert(q);}}
   lay.swap(nxt);
 }
 cout<<"CONNECTED_TARGETS\n";for(auto &kv:stat)cout<<"m="<<kv.first.first<<" e="<<kv.first.second<<" B="<<(7*kv.first.first-2*kv.first.second)<<" count="<<kv.second.first<<" min_Lnum="<<kv.second.second<<" status="<<(kv.second.second>0?"CERT_STRICT":"FAIL")<<"\n";
 // disconnected m=8,e=9: only possible edge-max partition 7+1. Rebuild connected 7-sets containing 0 with e=9, add an isolated singleton.
 lay.clear();lay.insert({1,0});for(int k=1;k<7;k++){nxt.clear();nxt.reserve(lay.size()*5);for(auto m:lay){uint64_t ca=0,cb=0;for(int v=0;v<128;v++)if(has(m,v))for(int i=0;i<7;i++){int w=v^(1<<i);if(!has(m,w)){if(w<64)ca|=1ULL<<w;else cb|=1ULL<<(w-64);}}uint64_t z=ca;while(z){int t=__builtin_ctzll(z);z&=z-1;M q=m;add(q,t);nxt.insert(q);}z=cb;while(z){int t=__builtin_ctzll(z);z&=z-1;M q=m;add(q,t+64);nxt.insert(q);}}lay.swap(nxt);} 
 long long dc=0;i64 dmin=LLONG_MAX;for(auto m:lay)if(edges(m)==9){for(int v=0;v<128;v++)if(!has(m,v)){bool adj=false;for(int i=0;i<7;i++)if(has(m,v^(1<<i))){adj=true;break;}if(!adj){M q=m;add(q,v);assert(edges(q)==9);dc++;dmin=min(dmin,Lmask(q));}}}
 cout<<"disconnected_m8_e9_generated="<<dc<<" min_Lnum="<<dmin<<" status="<<(dmin>0?"CERT_STRICT":"FAIL")<<"\n";
 // e=11 target is impossible if connected target count zero; disconnected 8-set has at most 9 edges by Harper maxima emax(7)+emax(1)=9.
 cout<<"m8_e11_connected_count="<<stat[{8,11}].first<<"; disconnected_max_edges=9; status="<<(stat[{8,11}].first==0?"IMPOSSIBLE":"FAIL")<<"\n";
 bool ok=true;for(auto key: {make_pair(4,3),make_pair(6,6),make_pair(7,8),make_pair(8,10),make_pair(8,9)}){auto q=stat[key];if(q.first==0||q.second<=0)ok=false;}if(dmin<=0)ok=false;if(stat[{8,11}].first!=0)ok=false;
 cout<<"SMALL_RESIDUAL_CERTIFICATE="<<(ok?"PASS":"FAIL")<<"\n";return ok?0:2;
}
