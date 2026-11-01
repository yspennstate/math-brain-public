#include <bits/stdc++.h>
#include <omp.h>
using namespace std; using i128=__int128_t;
struct A{int A,B,dh,c,m; long long hbase,lbase,rbase;};
static vector<pair<int,int>> pairs654(){vector<pair<int,int>> p;for(int i=0;i<=24;i++)for(int j=0;j<=24;j++)p.push_back({40*i,40*j});const int ex[][2]={{6,236},{13,233},{67,237},{26,236},{94,234},{84,234},{3,223},{3,233},{74,234},{114,234},{4,234},{176,236},{115,235}};for(auto&x:ex)p.push_back({4*x[0],4*x[1]});const int cut[][2]={{179,959},{613,953},{649,949},{539,959},{775,955},{885,945},{561,941},{419,959},{586,946},{215,955},{579,959},{70,910},{527,947},{497,957},{900,940},{291,951}};for(auto&x:cut)p.push_back({x[0],x[1]});return p;}
struct Orbit{vector<long long> r,s;};
static Orbit solve(long long P,long long Q,long long rnum,long long R,int M,int H){auto ps0=pairs654();vector<A>as;as.reserve(ps0.size());for(auto [x,y]:ps0){int dh=(9*x+11*y)/40,c=(11*x+9*y)/40,m=max(x,y);as.push_back({x,y,dh,c,m,(9LL*x*Q-10LL*P*m)*R,(-11LL*x*Q-10LL*P*m)*R,(9LL*y*Q-10LL*P*m)*R});}long long snum=R-rnum;vector<long long>pr(M+1),ps(M+1),cr(M+1),cs(M+1);for(int h=1;h<=H;h++){
#pragma omp parallel for schedule(static)
for(int k=0;k<=M;k++){long long br=0,bs=0;for(auto &a:as){int kh=k+a.dh;long long HR=a.hbase+(kh<=M?pr[kh]:0),HS=a.hbase+(kh<=M?ps[kh]:0),LR,LS;if(k>=a.c){LR=a.lbase+pr[k-a.c];LS=a.lbase+ps[k-a.c];}else{int kl=a.c-k-1;long long common=-40LL*k*R*Q;LR=a.rbase+common-40LL*rnum*Q+ps[kl];LS=a.rbase+common-40LL*snum*Q+pr[kl];}br=max(br,min(HR,LR));bs=max(bs,min(HS,LS));}cr[k]=br;cs[k]=bs;}pr.swap(cr);ps.swap(cs);}return{move(pr),move(ps)};}
static pair<i128,i128> margins(long long nA,long long nB,long long P,long long Q){const long long R=309151;const int M=2600,H=612;long long U=11*nA+9*nB,V=9*nA+11*nB;long long um=U%R,vm=V%R;if(um<0)um+=R;if(vm<0)vm+=R;long long rL=(R-um)%R,rH=vm;long long kL=(480LL*R-U)/R,kH=(480LL*R+V)/R;Orbit L,Hh;
#pragma omp parallel sections num_threads(2)
{
#pragma omp section
{L=solve(P,Q,rL,R,M,H);}
#pragma omp section
{Hh=solve(P,Q,rH,R,M,H);}
}
i128 Hroot=(i128)360*nA*Q-(i128)400*P*nB+Hh.r[kH];i128 Lroot=-(i128)440*nA*Q-(i128)400*P*nB+L.r[kL];i128 T=((i128)12480*Q+(i128)28800*P)*R;return{Hroot-T,Lroot-T};}
static string s128(i128 x){bool neg=x<0;if(neg)x=-x; if(x==0)return"0"; string s;while(x){s.push_back('0'+x%10);x/=10;}if(neg)s.push_back('-');reverse(s.begin(),s.end());return s;}
int main(){ long long R=309151,nB=24*R,P=617,Q=253330; for(long long nA: {4590331LL,4590100LL}){auto m=margins(nA,nB,P,Q); cout<<nA<<" H "<<s128(m.first)<<" L "<<s128(m.second)<<"\n";} }
