#include <bits/stdc++.h>
#include <omp.h>
using namespace std; using i128=__int128_t;
struct A{int A,B,dh,c,m; long long hbase,lbase,rbase;};
static vector<pair<int,int>> pairs654(){vector<pair<int,int>> p;for(int i=0;i<=24;i++)for(int j=0;j<=24;j++)p.push_back({40*i,40*j});const int ex[][2]={{6,236},{13,233},{67,237},{26,236},{94,234},{84,234},{3,223},{3,233},{74,234},{114,234},{4,234},{176,236},{115,235}};for(auto&x:ex)p.push_back({4*x[0],4*x[1]});const int cut[][2]={{179,959},{613,953},{649,949},{539,959},{775,955},{885,945},{561,941},{419,959},{586,946},{215,955},{579,959},{70,910},{527,947},{497,957},{900,940},{291,951}};for(auto&x:cut)p.push_back({x[0],x[1]});assert(p.size()==654);return p;}
struct Orbit{vector<long long> r,s;};
static Orbit solve(long long P,long long Q,long long rnum,long long R,int M,int H){auto ps0=pairs654();vector<A>as;as.reserve(ps0.size());for(auto [x,y]:ps0){int dh=(9*x+11*y)/40,c=(11*x+9*y)/40,m=max(x,y);as.push_back({x,y,dh,c,m,(9LL*x*Q-10LL*P*m)*R,(-11LL*x*Q-10LL*P*m)*R,(9LL*y*Q-10LL*P*m)*R});}long long snum=R-rnum;vector<long long>pr(M+1),ps(M+1),cr(M+1),cs(M+1);for(int h=1;h<=H;h++){for(int k=0;k<=M;k++){long long br=0,bs=0;for(auto &a:as){int kh=k+a.dh;long long HR=a.hbase+(kh<=M?pr[kh]:0),HS=a.hbase+(kh<=M?ps[kh]:0),LR,LS;if(k>=a.c){LR=a.lbase+pr[k-a.c];LS=a.lbase+ps[k-a.c];}else{int kl=a.c-k-1;long long common=-40LL*k*R*Q;LR=a.rbase+common-40LL*rnum*Q+ps[kl];LS=a.rbase+common-40LL*snum*Q+pr[kl];}br=max(br,min(HR,LR));bs=max(bs,min(HS,LS));}cr[k]=br;cs[k]=bs;}pr.swap(cr);ps.swap(cs);}return{move(pr),move(ps)};}
static pair<i128,i128> margins(long long nA,long long nB,long long P,long long Q){const long long R=309151;const int M=2600,H=612;long long U=11*nA+9*nB,V=9*nA+11*nB;long long um=U%R,vm=V%R;if(um<0)um+=R;if(vm<0)vm+=R;long long rL=(R-um)%R,rH=vm;long long kL=(480LL*R-U)/R,kH=(480LL*R+V)/R;Orbit L,Hh;
#pragma omp parallel sections num_threads(2)
{
#pragma omp section
{L=solve(P,Q,rL,R,M,H);}
#pragma omp section
{Hh=solve(P,Q,rH,R,M,H);}
}
i128 Hroot=(i128)360*nA*Q-(i128)400*P*nB+Hh.r[kH];i128 Lroot=-(i128)440*nA*Q-(i128)400*P*nB+L.r[kL];i128 T=((i128)12480*Q+(i128)28800*P)*R;return{Hroot-T,Lroot-T};}
static void p128(i128 x){if(x<0){cout<<'-';x=-x;}if(x==0){cout<<0;return;}string s;while(x){s.push_back('0'+x%10);x/=10;}reverse(s.begin(),s.end());cout<<s;}
int main(){
 const long long R=309151,nA=4590331,nB=24*R;
 assert((i128)617*16145>(i128)38*253330);
 const int rootK=480,maxShift=480,old654Support=2505,M=2600;
 assert(rootK+maxShift==960); assert(M>old654Support);
 auto cur=margins(nA,nB,617,253330);
 auto am=margins(nA-1,nB,617,253330);
 auto ap=margins(nA+1,nB,617,253330);
 auto bm=margins(nA,nB-1,617,253330);
 auto ep=margins(nA,nB,617001,253330000);
 assert(cur.first==(i128)2715305000LL && cur.second==0);
 assert(am.first==(i128)2624106200LL && am.second==0);
 assert(ap.first==(i128)2806503800LL && ap.second==0);
 assert(bm.first==(i128)2715551800LL && bm.second==(i128)-90952000LL);
 assert(ep.first==(i128)2597345344440LL && ep.second==(i128)-156634445660LL);
 long long U=11*nA+9*nB,V=9*nA+11*nB;
 long long rL=(R-(U%R))%R,rH=V%R;
 assert(rL==207123 && R-rL==102028);
 assert(rH==195896 && R-rH==113255);
 cout<<"I0130_B5_B12_B29_LOCAL_ENVELOPE_COMPACT_PASS\n";
 cout<<"current margins H=";p128(cur.first);cout<<" L=";p128(cur.second);cout<<"\n";
 cout<<"a_minus_one margins H=";p128(am.first);cout<<" L=";p128(am.second);cout<<"\n";
 cout<<"a_plus_one margins H=";p128(ap.first);cout<<" L=";p128(ap.second);cout<<"\n";
 cout<<"b_inward_one margins H=";p128(bm.first);cout<<" L=";p128(bm.second);cout<<"\n";
 cout<<"epsilon_plus_1_over_253330000 margins H=";p128(ep.first);cout<<" L=";p128(ep.second);cout<<"\n";
 cout<<"orbit_low={207123,102028}/309151 orbit_high={195896,113255}/309151\n";
 cout<<"compact_root_child_K=[0,960] old654_support_K<=2505 checked_M=2600\n";
 cout<<"status=NO_METRIC_MOVEMENT_LOCAL_DEFORMATION_OBSTRUCTION\n";
}
