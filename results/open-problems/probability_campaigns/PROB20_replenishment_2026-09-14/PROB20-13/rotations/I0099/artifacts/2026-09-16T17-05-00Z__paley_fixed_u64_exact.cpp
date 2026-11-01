#include <bits/stdc++.h>
using namespace std;
static const int MAXN=1300;
static const int MAXW=(MAXN+63)/64;
struct Bits{ uint64_t w[MAXW]; };
int N,WDS,Pmod; vector<int> verts; Bits adjb[MAXN];
inline void zeroB(Bits&a){for(int k=0;k<WDS;k++)a.w[k]=0;}
inline void setb(Bits&a,int v){a.w[v>>6]|=1ULL<<(v&63);} inline void clrb(Bits&a,int v){a.w[v>>6]&=~(1ULL<<(v&63));}
inline bool tst(const Bits&a,int v){return (a.w[v>>6]>>(v&63))&1ULL;} inline bool bany(const Bits&a){for(int k=0;k<WDS;k++)if(a.w[k])return true;return false;}
inline int pc(const Bits&a){int s=0;for(int k=0;k<WDS;k++)s+=__builtin_popcountll(a.w[k]);return s;}
inline int firstb(const Bits&a){for(int k=0;k<WDS;k++)if(a.w[k])return k*64+__builtin_ctzll(a.w[k]);return -1;}
inline Bits band(const Bits&a,const Bits&b){Bits c;for(int k=0;k<WDS;k++)c.w[k]=a.w[k]&b.w[k];return c;}
inline void andnotB(Bits&a,const Bits&b){for(int k=0;k<WDS;k++)a.w[k]&=~b.w[k];}
struct CR{int n;int o[MAXN],c[MAXN];};
inline CR color_sort(Bits P){CR r;r.n=0;int col=0;Bits U=P;while(bany(U)){++col;Bits Q=U;while(bany(Q)){int v=firstb(Q);r.o[r.n]=v;r.c[r.n]=col;++r.n;clrb(U,v);clrb(Q,v);andnotB(Q,adjb[v]);}}return r;}
static uint64_t mix64(uint64_t h,uint64_t x){x+=0x9e3779b97f4a7c15ULL;x=(x^(x>>30))*0xbf58476d1ce4e5b9ULL;x=(x^(x>>27))*0x94d049bb133111ebULL;x^=x>>31;h^=x+0x9e3779b97f4a7c15ULL+(h<<6)+(h>>2);return h;}
static uint64_t hash_bits(uint64_t h,const Bits&P){h=mix64(h,N);for(int k=0;k<WDS;k++)h=mix64(h,P.w[k]);return h;}
struct MaxSolver{uint64_t nodes=0;int best=0;vector<int>bestv;void rec(Bits P,vector<int>&cur){++nodes;if(!bany(P)){if((int)cur.size()>best){best=cur.size();bestv=cur;}return;}CR cr=color_sort(P);for(int i=cr.n-1;i>=0;--i){if((int)cur.size()+cr.c[i]<=best)return;int v=cr.o[i];if(!tst(P,v))continue;cur.push_back(v);Bits P2=band(P,adjb[v]);rec(P2,cur);cur.pop_back();clrb(P,v);}} void run(){Bits P;zeroB(P);for(int i=0;i<N;i++)setb(P,i);vector<int>cur;rec(P,cur);}};
struct DecisionSolver{uint64_t nodes=0,prunes=0,leaves=0,hash=0x123456789abcdef0ULL;void ev(uint64_t tag,int need,const Bits&P,uint64_t extra=0){hash=mix64(hash,tag);hash=mix64(hash,need);hash=hash_bits(hash,P);hash=mix64(hash,extra);}bool rec(Bits P,int need){++nodes;if(need<=0){ev(1,need,P);return true;}int cnt=pc(P);if(cnt<need){++prunes;ev(2,need,P,cnt);return false;}CR cr=color_sort(P);if(cr.n==0||cr.c[cr.n-1]<need){++prunes;ev(3,need,P,cr.n?cr.c[cr.n-1]:0);return false;}for(int i=cr.n-1;i>=0;--i){if(cr.c[i]<need){++prunes;ev(4,need,P,cr.c[i]);return false;}int v=cr.o[i];if(!tst(P,v))continue;ev(5,need,P,v);Bits P2=band(P,adjb[v]);if(rec(P2,need-1))return true;clrb(P,v);}++leaves;ev(6,need,P);return false;}bool run(int need){Bits P;zeroB(P);for(int i=0;i<N;i++)setb(P,i);return rec(P,need);}};
bool isprime(int n){if(n<2)return false;if(n%2==0)return n==2;for(int d=3;1LL*d*d<=n;d+=2)if(n%d==0)return false;return true;}
vector<char> build(int p){Pmod=p;vector<char>qr(p);for(int x=1;x<p;x++)qr[1LL*x*x%p]=1;verts.clear();for(int x=2;x<p;x++)if(qr[x]&&qr[(x-1+p)%p])verts.push_back(x);N=verts.size();WDS=(N+63)/64;if(N>MAXN){cerr<<"N exceeds MAXN\n";exit(7);}for(int i=0;i<N;i++)zeroB(adjb[i]);for(int i=0;i<N;i++)for(int j=i+1;j<N;j++)if(qr[(verts[i]-verts[j]+p)%p]){setb(adjb[i],j);setb(adjb[j],i);}return qr;}
bool witness_ok(int p,const vector<char>&qr,const vector<int>&W){for(int i=0;i<(int)W.size();i++)for(int j=0;j<i;j++)if(!qr[(W[i]-W[j]+p)%p])return false;return true;}
int main(int argc,char**argv){int pmin=argc>1?stoi(argv[1]):2341,pmax=argc>2?stoi(argv[2]):pmin;cout<<"I0099_FAST_EXACT_V1 pmin="<<pmin<<" pmax="<<pmax<<"\n";int count=0;auto allst=chrono::steady_clock::now();for(int p=pmin;p<=pmax;p++){if(p%4!=1||!isprime(p))continue;++count;auto st=chrono::steady_clock::now();auto qr=build(p);MaxSolver ms;ms.run();int omega=ms.best+2;vector<int>W={0,1};for(int id:ms.bestv)W.push_back(verts[id]);if(!witness_ok(p,qr,W)||(int)W.size()!=omega){cerr<<"WITNESS_FAIL p="<<p<<"\n";return 2;}DecisionSolver ds;int targetH=omega-1;bool found=ds.run(targetH);if(found){cerr<<"DECISION_FAIL p="<<p<<" targetH="<<targetH<<"\n";return 3;}double sec=chrono::duration<double>(chrono::steady_clock::now()-st).count();cout<<"p="<<p<<" omega="<<omega<<" Hn="<<N<<" witness=";for(int i=0;i<(int)W.size();i++){if(i)cout<<",";cout<<W[i];}cout<<" exclude="<<omega+1<<" targetH="<<targetH<<" max_nodes="<<ms.nodes<<" no_nodes="<<ds.nodes<<" prunes="<<ds.prunes<<" leaves="<<ds.leaves<<" proof64="<<hex<<ds.hash<<dec<<" seconds="<<fixed<<setprecision(6)<<sec<<"\n";}
double secs=chrono::duration<double>(chrono::steady_clock::now()-allst).count();cout<<"SUMMARY count="<<count<<" range="<<pmin<<".."<<pmax<<" all_witnesses_pass=1 all_one_larger_exclusions_pass=1 seconds="<<fixed<<setprecision(6)<<secs<<"\n";}
