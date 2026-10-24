#include <bits/stdc++.h>
using namespace std;
static const int MAXN=1200, MAXW=(MAXN+63)/64;
struct Bits{ uint64_t w[MAXW]; };
int N,WDS,pmod; vector<int> vals; Bits adjb[MAXN];
inline void zeroB(Bits&a){for(int k=0;k<WDS;k++)a.w[k]=0;}
inline void setb(Bits&a,int v){a.w[v>>6]|=1ULL<<(v&63);} inline void clrb(Bits&a,int v){a.w[v>>6]&=~(1ULL<<(v&63));}
inline bool tst(const Bits&a,int v){return (a.w[v>>6]>>(v&63))&1ULL;} inline bool bany(const Bits&a){for(int k=0;k<WDS;k++)if(a.w[k])return true;return false;}
inline int pc(const Bits&a){int s=0;for(int k=0;k<WDS;k++)s+=__builtin_popcountll(a.w[k]);return s;} inline int firstb(const Bits&a){for(int k=0;k<WDS;k++)if(a.w[k])return k*64+__builtin_ctzll(a.w[k]);return -1;}
inline Bits band(const Bits&a,const Bits&b){Bits c;for(int k=0;k<WDS;k++)c.w[k]=a.w[k]&b.w[k];return c;} inline void andnotB(Bits&a,const Bits&b){for(int k=0;k<WDS;k++)a.w[k]&=~b.w[k];}
struct CR{int n,o[MAXN],c[MAXN];};
inline CR color_sort(Bits P){CR r;r.n=0;int col=0;Bits U=P;while(bany(U)){++col;Bits Q=U;while(bany(Q)){int v=firstb(Q);r.o[r.n]=v;r.c[r.n]=col;++r.n;clrb(U,v);clrb(Q,v);andnotB(Q,adjb[v]);}}return r;}
long long modpow(long long a,long long e,int p){long long r=1;while(e){if(e&1)r=r*a%p;a=a*a%p;e>>=1;}return r;}
uint64_t nodes=0,prunes=0; int best=0; vector<int> path,bestpath;
void expand(Bits P){++nodes; if(!bany(P)){if((int)path.size()>best){best=path.size();bestpath=path;cerr<<"bestH="<<best<<" nodes="<<nodes<<"\n";}return;} CR cr=color_sort(P); for(int i=cr.n-1;i>=0;--i){ if((int)path.size()+cr.c[i]<=best){++prunes;return;} int v=cr.o[i]; if(!tst(P,v))continue; path.push_back(v); Bits P2=band(P,adjb[v]); if(bany(P2)) expand(P2); else if((int)path.size()>best){best=path.size();bestpath=path;cerr<<"bestH="<<best<<" nodes="<<nodes<<"\n";} path.pop_back(); clrb(P,v); }}
int main(int argc,char**argv){int p=argc>1?atoi(argv[1]):3557; pmod=p; vector<char>qr(p);for(int x=1;x<p;x++)qr[1LL*x*x%p]=1;for(int x=2;x<p;x++)if(qr[x]&&qr[(x-1+p)%p])vals.push_back(x);N=vals.size();WDS=(N+63)/64; cerr<<"N="<<N<<"\n"; for(int i=0;i<N;i++)zeroB(adjb[i]);for(int i=0;i<N;i++)for(int j=i+1;j<N;j++)if(qr[(vals[i]-vals[j]+p)%p]){setb(adjb[i],j);setb(adjb[j],i);} Bits all;zeroB(all);for(int i=0;i<N;i++)setb(all,i); auto t=chrono::steady_clock::now();expand(all);double sec=chrono::duration<double>(chrono::steady_clock::now()-t).count(); cout<<"p="<<p<<" omega="<<best+2<<" Hbest="<<best<<" nodes="<<nodes<<" prunes="<<prunes<<" sec="<<sec<<" witness=0,1";for(int i:bestpath)cout<<","<<vals[i];cout<<"\n";}
