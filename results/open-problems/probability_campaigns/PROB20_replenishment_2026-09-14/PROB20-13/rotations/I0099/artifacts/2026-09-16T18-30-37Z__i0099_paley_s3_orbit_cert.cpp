#include <bits/stdc++.h>
using namespace std;
static const int MAXN=1600, MAXW=(MAXN+63)/64;
struct Bits{ uint64_t w[MAXW]; };
int N,WDS,Pmod; vector<int> vals,idxOf; Bits adjb[MAXN];
inline void zeroB(Bits&a){for(int k=0;k<WDS;k++)a.w[k]=0;} inline void setb(Bits&a,int v){a.w[v>>6]|=1ULL<<(v&63);} inline void clrb(Bits&a,int v){a.w[v>>6]&=~(1ULL<<(v&63));}
inline bool tst(const Bits&a,int v){return (a.w[v>>6]>>(v&63))&1ULL;} inline bool bany(const Bits&a){for(int k=0;k<WDS;k++)if(a.w[k])return true;return false;} inline int pc(const Bits&a){int s=0;for(int k=0;k<WDS;k++)s+=__builtin_popcountll(a.w[k]);return s;} inline int firstb(const Bits&a){for(int k=0;k<WDS;k++)if(a.w[k])return k*64+__builtin_ctzll(a.w[k]);return -1;}
inline Bits band(const Bits&a,const Bits&b){Bits c;for(int k=0;k<WDS;k++)c.w[k]=a.w[k]&b.w[k];return c;} inline void andnotB(Bits&a,const Bits&b){for(int k=0;k<WDS;k++)a.w[k]&=~b.w[k];}
struct CR{int n,o[MAXN],c[MAXN];}; inline CR color_sort(Bits P){CR r;r.n=0;int col=0;Bits U=P;while(bany(U)){++col;Bits Q=U;while(bany(Q)){int v=firstb(Q);r.o[r.n]=v;r.c[r.n]=col;++r.n;clrb(U,v);clrb(Q,v);andnotB(Q,adjb[v]);}}return r;}
static uint64_t mix64(uint64_t h,uint64_t x){x+=0x9e3779b97f4a7c15ULL;x=(x^(x>>30))*0xbf58476d1ce4e5b9ULL;x=(x^(x>>27))*0x94d049bb133111ebULL;x^=x>>31;h^=x+0x9e3779b97f4a7c15ULL+(h<<6)+(h>>2);return h;}
static uint64_t hash_bits(uint64_t h,const Bits&P){h=mix64(h,N);for(int k=0;k<WDS;k++)h=mix64(h,P.w[k]);return h;}
struct Solver{
  uint64_t nodes=0,prunes=0,leaves=0,hash=0x123456789abcdef0ULL; vector<int> path,found_path;
  void ev(uint64_t tag,int need,const Bits&P,uint64_t extra=0){hash=mix64(hash,tag);hash=mix64(hash,need);hash=hash_bits(hash,P);hash=mix64(hash,extra);}
  bool rec(Bits P,int need){++nodes;if(need<=0){found_path=path;ev(1,need,P);return true;}int cnt=pc(P);if(cnt<need){++prunes;ev(2,need,P,cnt);return false;}CR cr=color_sort(P);if(cr.n==0||cr.c[cr.n-1]<need){++prunes;ev(3,need,P,cr.n?cr.c[cr.n-1]:0);return false;}for(int i=cr.n-1;i>=0;--i){if(cr.c[i]<need){++prunes;ev(4,need,P,cr.c[i]);return false;}int v=cr.o[i];if(!tst(P,v))continue;ev(5,need,P,v);path.push_back(v);Bits P2=band(P,adjb[v]);if(rec(P2,need-1))return true;path.pop_back();clrb(P,v);}++leaves;ev(6,need,P);return false;}
};
long long modpow(long long a,long long e,int p){long long r=1;while(e){if(e&1)r=r*a%p;a=a*a%p;e>>=1;}return r;}
int invmod(int x,int p){return (int)modpow(x,p-2,p);} 
int main(int argc,char**argv){
  if(argc<3){cerr<<"usage p omega [start_rep] [end_rep_exclusive]\n";return 2;} int p=atoi(argv[1]), omega=atoi(argv[2]), start=argc>3?atoi(argv[3]):0, endarg=argc>4?atoi(argv[4]):-1; Pmod=p;
  vector<char> qr(p);for(int x=1;x<p;x++)qr[1LL*x*x%p]=1; vals.clear();for(int x=2;x<p;x++)if(qr[x]&&qr[(x-1+p)%p])vals.push_back(x);N=vals.size();WDS=(N+63)/64;if(N>MAXN){cerr<<"N too big\n";return 7;}idxOf.assign(p,-1);for(int i=0;i<N;i++)idxOf[vals[i]]=i;for(int i=0;i<N;i++)zeroB(adjb[i]);for(int i=0;i<N;i++)for(int j=i+1;j<N;j++)if(qr[(vals[i]-vals[j]+p)%p]){setb(adjb[i],j);setb(adjb[j],i);}
  auto sidx=[&](int i){int y=(1-vals[i])%p;if(y<0)y+=p;return idxOf[y];}; auto tidx=[&](int i){return idxOf[invmod(vals[i],p)];};
  bool auto_ok=true;for(int i=0;i<N;i++)if(sidx(i)<0||tidx(i)<0)auto_ok=false; for(int i=0;i<N&&auto_ok;i++)for(int j=i+1;j<N;j++){bool a=tst(adjb[i],j);if(a!=tst(adjb[sidx(i)],sidx(j))||a!=tst(adjb[tidx(i)],tidx(j))){auto_ok=false;break;}}
  vector<int> orbit_id(N,-1), reps, osz;for(int i=0;i<N;i++)if(orbit_id[i]<0){int oid=reps.size();queue<int>q;q.push(i);orbit_id[i]=oid;vector<int>mem;while(!q.empty()){int v=q.front();q.pop();mem.push_back(v);int z[2]={sidx(v),tidx(v)};for(int u:z)if(orbit_id[u]<0){orbit_id[u]=oid;q.push(u);}else if(orbit_id[u]!=oid){cerr<<"orbit collision\n";return 8;}}int r=*min_element(mem.begin(),mem.end(),[&](int a,int b){return vals[a]<vals[b];});reps.push_back(r);osz.push_back(mem.size());}
  int covered=0;for(int z:osz)covered+=z; if(!auto_ok||covered!=N){cerr<<"S3_AUTOMORPHISM_FAIL\n";return 9;}
  Bits all;zeroB(all);for(int i=0;i<N;i++)setb(all,i);Solver fs;bool wf=fs.rec(all,omega-2); if(!wf){cerr<<"WITNESS_SEARCH_FAIL\n";return 10;} vector<int>w={0,1};for(int id:fs.found_path)w.push_back(vals[id]);if((int)w.size()!=omega){cerr<<"WITNESS_SIZE_FAIL\n";return 11;}for(int i=0;i<omega;i++)for(int j=0;j<i;j++)if(!qr[(w[i]-w[j]+p)%p]){cerr<<"WITNESS_EDGE_FAIL\n";return 12;}
  int R=reps.size(),end=endarg<0?R:min(endarg,R);start=max(0,start);if(start>end){cerr<<"bad range\n";return 13;}
  cout<<"I0099_S3_ORBIT_CERT_V1 p="<<p<<" omega="<<omega<<" Hn="<<N<<" reps="<<R<<" s3_auto_ok=1 covered="<<covered<<" range="<<start<<".."<<end<<"\n";
  cout<<"witness=";for(int i=0;i<(int)w.size();i++){if(i)cout<<",";cout<<w[i];}cout<<" witness_search_nodes="<<fs.nodes<<" witness_ok=1\n";
  uint64_t agg=0x6a09e667f3bcc909ULL,totalnodes=0,totalpr=0,totalleaves=0;auto st=chrono::steady_clock::now();
  for(int ri=start;ri<end;ri++){int r=reps[ri];Solver ds;Bits P=adjb[r];bool found=ds.rec(P,omega-2);if(found){cout<<"COUNTERFOUND ri="<<ri<<" rep="<<vals[r]<<"\n";return 3;} totalnodes+=ds.nodes;totalpr+=ds.prunes;totalleaves+=ds.leaves;agg=mix64(agg,ri);agg=mix64(agg,vals[r]);agg=mix64(agg,osz[ri]);agg=mix64(agg,ds.nodes);agg=mix64(agg,ds.hash);cout<<"ri="<<ri<<" rep="<<vals[r]<<" orbit="<<osz[ri]<<" need_after_rep="<<(omega-2)<<" no_nodes="<<ds.nodes<<" prunes="<<ds.prunes<<" leaves="<<ds.leaves<<" proof64="<<hex<<ds.hash<<dec<<"\n";}
  double sec=chrono::duration<double>(chrono::steady_clock::now()-st).count();cout<<"CERTIFIED_RANGE p="<<p<<" omega="<<omega<<" reps="<<start<<".."<<end<<" all_no_one_larger=1 total_nodes="<<totalnodes<<" prunes="<<totalpr<<" leaves="<<totalleaves<<" agg64="<<hex<<agg<<dec<<" seconds="<<fixed<<setprecision(6)<<sec<<"\n";return 0;
}
