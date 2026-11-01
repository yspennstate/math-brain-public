#include <bits/stdc++.h>
using namespace std;
static const int MAXN=2200, MAXW=(MAXN+63)/64;
struct Bits{ uint64_t w[MAXW]; };
int N,WDS,Pmod; vector<int> vals,idxOf; Bits adjb[MAXN];
inline void zeroB(Bits&a){for(int k=0;k<WDS;k++)a.w[k]=0;} inline void setb(Bits&a,int v){a.w[v>>6]|=1ULL<<(v&63);} inline void clrb(Bits&a,int v){a.w[v>>6]&=~(1ULL<<(v&63));}
inline bool tst(const Bits&a,int v){return (a.w[v>>6]>>(v&63))&1ULL;} inline bool bany(const Bits&a){for(int k=0;k<WDS;k++)if(a.w[k])return true;return false;} inline int pc(const Bits&a){int s=0;for(int k=0;k<WDS;k++)s+=__builtin_popcountll(a.w[k]);return s;} inline int firstb(const Bits&a){for(int k=0;k<WDS;k++)if(a.w[k])return k*64+__builtin_ctzll(a.w[k]);return -1;}
inline Bits band(const Bits&a,const Bits&b){Bits c;for(int k=0;k<WDS;k++)c.w[k]=a.w[k]&b.w[k];return c;} inline void andnotB(Bits&a,const Bits&b){for(int k=0;k<WDS;k++)a.w[k]&=~b.w[k];}
struct CR{int n,o[MAXN],c[MAXN];}; inline CR color_sort(Bits P){CR r;r.n=0;int col=0;Bits U=P;while(bany(U)){++col;Bits Q=U;while(bany(Q)){int v=firstb(Q);r.o[r.n]=v;r.c[r.n]=col;++r.n;clrb(U,v);clrb(Q,v);andnotB(Q,adjb[v]);}}return r;}
static uint64_t mix64(uint64_t h,uint64_t x){x+=0x9e3779b97f4a7c15ULL;x=(x^(x>>30))*0xbf58476d1ce4e5b9ULL;x=(x^(x>>27))*0x94d049bb133111ebULL;x^=x>>31;h^=x+0x9e3779b97f4a7c15ULL+(h<<6)+(h>>2);return h;}
static uint64_t hash_bits(uint64_t h,const Bits&P){h=mix64(h,N);for(int k=0;k<WDS;k++)h=mix64(h,P.w[k]);return h;}
struct Solver{ uint64_t nodes=0,prunes=0,leaves=0,hash=0x123456789abcdef0ULL; vector<int> path,found_path;
 void ev(uint64_t tag,int need,const Bits&P,uint64_t extra=0){hash=mix64(hash,tag);hash=mix64(hash,need);hash=hash_bits(hash,P);hash=mix64(hash,extra);} 
 bool rec(Bits P,int need){++nodes;if(need<=0){found_path=path;ev(1,need,P);return true;}int cnt=pc(P);if(cnt<need){++prunes;ev(2,need,P,cnt);return false;}CR cr=color_sort(P);if(cr.n==0||cr.c[cr.n-1]<need){++prunes;ev(3,need,P,cr.n?cr.c[cr.n-1]:0);return false;}for(int i=cr.n-1;i>=0;--i){if(cr.c[i]<need){++prunes;ev(4,need,P,cr.c[i]);return false;}int v=cr.o[i];if(!tst(P,v))continue;ev(5,need,P,v);path.push_back(v);Bits P2=band(P,adjb[v]);if(rec(P2,need-1))return true;path.pop_back();clrb(P,v);}++leaves;ev(6,need,P);return false;}
};
long long modpow(long long a,long long e,int p){long long r=1;while(e){if(e&1)r=r*a%p;a=a*a%p;e>>=1;}return r;} int invmod(int x,int p){return (int)modpow(x,p-2,p);} 
int main(int argc,char**argv){if(argc<3){cerr<<"usage p omega [start_s3] [end_s3]\n";return 2;} int p=atoi(argv[1]),omega=atoi(argv[2]),sstart=argc>3?atoi(argv[3]):0,sendarg=argc>4?atoi(argv[4]):-1;Pmod=p;
 vector<char>qr(p);for(int x=1;x<p;x++)qr[1LL*x*x%p]=1; vals.clear();for(int x=2;x<p;x++)if(qr[x]&&qr[(x-1+p)%p])vals.push_back(x);N=vals.size();WDS=(N+63)/64;if(N>MAXN){cerr<<"N too big\n";return 7;}idxOf.assign(p,-1);for(int i=0;i<N;i++)idxOf[vals[i]]=i;for(int i=0;i<N;i++)zeroB(adjb[i]);for(int i=0;i<N;i++)for(int j=i+1;j<N;j++)if(qr[(vals[i]-vals[j]+p)%p]){setb(adjb[i],j);setb(adjb[j],i);}
 auto sidx=[&](int i){int y=(1-vals[i])%p;if(y<0)y+=p;return idxOf[y];};auto tidx=[&](int i){return idxOf[invmod(vals[i],p)];};
 vector<int> oid(N,-1),sreps; for(int i=0;i<N;i++)if(oid[i]<0){int id=sreps.size();queue<int>q;q.push(i);oid[i]=id;vector<int>mem;while(!q.empty()){int v=q.front();q.pop();mem.push_back(v);int z[2]={sidx(v),tidx(v)};for(int uu:z){if(uu<0){cerr<<"S3_FAIL\n";return 8;}if(oid[uu]<0){oid[uu]=id;q.push(uu);}else if(oid[uu]!=id){cerr<<"S3_COLLISION\n";return 9;}}}int r=*min_element(mem.begin(),mem.end(),[&](int a,int b){return vals[a]<vals[b];});sreps.push_back(r);} 
 Bits all;zeroB(all);for(int i=0;i<N;i++)setb(all,i);
 vector<int> hpath,hsol; uint64_t hnodes=0; function<bool(Bits,int)> hdfs=[&](Bits P,int need)->bool{++hnodes;if(need==0){hsol=hpath;return true;}if(pc(P)<need)return false;vector<pair<int,int>>ord;for(int i=0;i<N;i++)if(tst(P,i)){Bits Q=band(P,adjb[i]);ord.push_back({pc(Q),i});}sort(ord.rbegin(),ord.rend());for(auto [dg,v]:ord){if(!tst(P,v))continue;hpath.push_back(v);Bits Q=band(P,adjb[v]);if(hdfs(Q,need-1))return true;hpath.pop_back();clrb(P,v);if(pc(P)<need)break;}return false;};
 bool wf=hdfs(all,omega-2);if(!wf){cerr<<"WITNESS_FAIL\\n";return 10;}vector<int>w={0,1};for(int id:hsol)w.push_back(vals[id]);
 cout<<"I0099_V4_CERT p="<<p<<" omega="<<omega<<" Hn="<<N<<" s3reps="<<sreps.size()<<" witness=";for(size_t i=0;i<w.size();++i){if(i)cout<<",";cout<<w[i];}cout<<" witness_nodes="<<hnodes<<"\n";
 int send=sendarg<0?(int)sreps.size():min(sendarg,(int)sreps.size());sstart=max(sstart,0); uint64_t total=0, obligations=0; auto T=chrono::steady_clock::now();
 for(int si=sstart;si<send;++si){int ui=sreps[si],u=vals[ui]; Bits K=adjb[ui]; vector<int>kid; for(int j=0;j<N;j++)if(tst(K,j))kid.push_back(j); vector<int> localid(N,-1),vreps; bool ok=true;
   auto amap=[&](int j)->int{ long long y=1LL*u*invmod(vals[j],p)%p; return idxOf[(int)y];};
   auto bmap=[&](int j)->int{ long long num=(vals[j]-u+p)%p, den=(vals[j]-1+p)%p; long long y=num*invmod((int)den,p)%p; return idxOf[(int)y];};
   // V4 generated by a,b; c=ab
   int oid2=0; for(int j:kid)if(localid[j]<0){queue<int>q;q.push(j);localid[j]=oid2;vector<int>mem;while(!q.empty()){int v=q.front();q.pop();mem.push_back(v);int z[2]={amap(v),bmap(v)};for(int vv:z){if(vv<0||!tst(K,vv)){ok=false;continue;}if(localid[vv]<0){localid[vv]=oid2;q.push(vv);}else if(localid[vv]!=oid2)ok=false;}}int r=*min_element(mem.begin(),mem.end(),[&](int a,int b){return vals[a]<vals[b];});vreps.push_back(r);oid2++;}
   // verify adjacency preservation inside K for a,b
   if(ok){for(int x:kid)for(int y:kid)if(x<y){bool e=tst(adjb[x],y);int ax=amap(x),ay=amap(y),bx=bmap(x),by=bmap(y);if(ax<0||ay<0||bx<0||by<0||e!=tst(adjb[ax],ay)||e!=tst(adjb[bx],by)){ok=false;break;}}}
   if(!ok){cerr<<"V4_FAIL si="<<si<<" u="<<u<<"\n";return 11;}
   uint64_t snodes=0; for(int vi:vreps){Bits P=band(K,adjb[vi]);Solver ds;bool found=ds.rec(P,omega-3);if(found){cout<<"COUNTERFOUND si="<<si<<" u="<<u<<" v="<<vals[vi]<<"\n";return 3;}snodes+=ds.nodes;obligations++;}
   total+=snodes; cout<<"si="<<si<<" u="<<u<<" K="<<kid.size()<<" v4reps="<<vreps.size()<<" no_nodes="<<snodes<<"\n";
 }
 double sec=chrono::duration<double>(chrono::steady_clock::now()-T).count();cout<<"CERTIFIED_V4_RANGE p="<<p<<" omega="<<omega<<" s3="<<sstart<<".."<<send<<" all_no_one_larger=1 obligations="<<obligations<<" total_nodes="<<total<<" seconds="<<fixed<<setprecision(6)<<sec<<"\n";
}
