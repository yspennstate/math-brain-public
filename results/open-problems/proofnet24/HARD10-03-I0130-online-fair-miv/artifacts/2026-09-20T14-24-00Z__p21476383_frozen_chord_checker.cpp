#include <bits/stdc++.h>
#include <omp.h>
using namespace std;
using i128=__int128_t;
static string s128(i128 x){ if(x==0)return "0"; bool neg=x<0; if(neg)x=-x; string s; while(x){s.push_back('0'+x%10);x/=10;} if(neg)s.push_back('-'); reverse(s.begin(),s.end()); return s; }
struct BaseGeom{int x,y,dh,c,m;};
static vector<pair<int,int>> old654_points(){ vector<pair<int,int>>ps; for(int i=0;i<=24;i++)for(int j=0;j<=24;j++)ps.push_back({40*i,40*j}); const int ex[][2]={{6,236},{13,233},{67,237},{26,236},{94,234},{84,234},{3,223},{3,233},{74,234},{114,234},{4,234},{176,236},{115,235}}; for(auto&p:ex)ps.push_back({4*p[0],4*p[1]}); const int cut[][2]={{179,959},{613,953},{649,949},{539,959},{775,955},{885,945},{561,941},{419,959},{586,946},{215,955},{579,959},{70,910},{527,947},{497,957},{900,940},{291,951}}; for(auto&p:cut)ps.push_back({p[0],p[1]}); return ps; }
static vector<BaseGeom> oldgeom(){vector<BaseGeom> as;for(auto[x,y]:old654_points())as.push_back({x,y,(9*x+11*y)/40,(11*x+9*y)/40,max(x,y)});return as;}
struct OldPair{ vector<long long> fi0,fi1; array<vector<long long>,5> fr0,fs0,fr1,fs1;};
static OldPair build_old_pair(long long P0,long long P1,long long Q,int M=2600,int H=612){
 auto as=oldgeom(); int A=as.size(); OldPair out; vector<long long> p0(M+1),c0(M+1),p1(M+1),c1(M+1);
 for(int h=0;h<H;h++){
#pragma omp parallel for schedule(static)
  for(int k=0;k<=M;k++){ long long best0=0,best1=0; int bi=-1;
   for(int ia=0;ia<A;ia++){auto a=as[ia]; long long hb0=9LL*a.x*Q-10LL*P0*a.m,lb0=-11LL*a.x*Q-10LL*P0*a.m,rb0=9LL*a.y*Q-10LL*P0*a.m; int kh=k+a.dh; long long hi0=hb0+(kh<=M?p0[kh]:0),lo0; if(k>=a.c)lo0=lb0+p0[k-a.c];else{int kl=a.c-k;lo0=rb0-40LL*k*Q+p0[kl];} long long z0=min(hi0,lo0); if(z0>best0){best0=z0;bi=ia;}}
   if(bi>=0){auto a=as[bi]; long long hb1=9LL*a.x*Q-10LL*P1*a.m,lb1=-11LL*a.x*Q-10LL*P1*a.m,rb1=9LL*a.y*Q-10LL*P1*a.m; int kh=k+a.dh; long long hi1=hb1+(kh<=M?p1[kh]:0),lo1; if(k>=a.c)lo1=lb1+p1[k-a.c];else{int kl=a.c-k;lo1=rb1-40LL*k*Q+p1[kl];} best1=min(hi1,lo1);} c0[k]=best0;c1[k]=best1; }
  p0.swap(c0);p1.swap(c1);
 }
 out.fi0=p0;out.fi1=p1;
 for(int r=1;r<=4;r++){ int sr=8-r; vector<long long> pr0(M+1),ps0(M+1),cr0(M+1),cs0(M+1),pr1(M+1),ps1(M+1),cr1(M+1),cs1(M+1);
  for(int h=0;h<H;h++){
#pragma omp parallel for schedule(static)
   for(int k=0;k<=M;k++){ long long br0=0,bs0=0,br1=0,bs1=0; int bir=-1,bis=-1;
    for(int ia=0;ia<A;ia++){auto a=as[ia]; long long hb0=(9LL*a.x*Q-10LL*P0*a.m)*8,lb0=(-11LL*a.x*Q-10LL*P0*a.m)*8,rb0=(9LL*a.y*Q-10LL*P0*a.m)*8; int kh=k+a.dh; long long HR0=hb0+(kh<=M?pr0[kh]:0),HS0=hb0+(kh<=M?ps0[kh]:0),LR0,LS0; if(k>=a.c){LR0=lb0+pr0[k-a.c];LS0=lb0+ps0[k-a.c];}else{int kl=a.c-k-1;long long xr=1LL*k*8+r,xs=1LL*k*8+sr;LR0=rb0-40LL*xr*Q+ps0[kl];LS0=rb0-40LL*xs*Q+pr0[kl];} long long zr0=min(HR0,LR0),zs0=min(HS0,LS0);if(zr0>br0){br0=zr0;bir=ia;}if(zs0>bs0){bs0=zs0;bis=ia;}}
    if(bir>=0){auto a=as[bir];long long hb1=(9LL*a.x*Q-10LL*P1*a.m)*8,lb1=(-11LL*a.x*Q-10LL*P1*a.m)*8,rb1=(9LL*a.y*Q-10LL*P1*a.m)*8;int kh=k+a.dh;long long HR1=hb1+(kh<=M?pr1[kh]:0),LR1;if(k>=a.c)LR1=lb1+pr1[k-a.c];else{int kl=a.c-k-1;long long xr=1LL*k*8+r;LR1=rb1-40LL*xr*Q+ps1[kl];}br1=min(HR1,LR1);} if(bis>=0){auto a=as[bis];long long hb1=(9LL*a.x*Q-10LL*P1*a.m)*8,lb1=(-11LL*a.x*Q-10LL*P1*a.m)*8,rb1=(9LL*a.y*Q-10LL*P1*a.m)*8;int kh=k+a.dh;long long HS1=hb1+(kh<=M?ps1[kh]:0),LS1;if(k>=a.c)LS1=lb1+ps1[k-a.c];else{int kl=a.c-k-1;long long xs=1LL*k*8+sr;LS1=rb1-40LL*xs*Q+pr1[kl];}bs1=min(HS1,LS1);} cr0[k]=br0;cs0[k]=bs0;cr1[k]=br1;cs1[k]=bs1; }
   pr0.swap(cr0);ps0.swap(cs0);pr1.swap(cr1);ps1.swap(cs1);
  }
  out.fr0[r]=pr0;out.fs0[r]=ps0;out.fr1[r]=pr1;out.fs1[r]=ps1;
 }
 return out;
}
static i128 gcd128(i128 a,i128 b){if(a<0)a=-a;if(b<0)b=-b;while(b){i128 r=a%b;a=b;b=r;}return a;}
struct RatAct{long long A,B,D;}; static vector<RatAct> Gextra={{7193,11628,11628},{871,3840,3840},{2591,3840,3840},{6858927,11100227,11162880},{13,704,704},{47,88,88},{377,1056,1056},{39,176,176},{641,1056,1056},{179,1056,1056},{3,88,88},{105,176,176},{61,176,176},{721,2112,2112},{17,176,176},{189,704,704},{509,1056,1056},{43,132,132},{311,1056,1056},{413,2112,2112},{35,704,704},{255,704,704},{289,1056,1056},{71,432,432},{193,2112,2112},{45,352,352},{215,2112,2112},{25,864,864},{145,704,704},{133,864,864},{25,1056,1056},{239,1728,1728},{185,1728,1728},{527,1728,1728},{23,352,352},{57,704,704},{139,528,528},{281,2112,2112},{245,1056,1056},{91,1056,1056},{815,1728,1728},{95,1728,1728},{5,66,66},{43530775821LL,208953177301LL,7426362113280LL},{435,704,704},{228175945101LL,1292743289321LL,1336500000000LL},{630860931LL,3574176551LL,3695155200LL}};
struct Act{bool base; long long A,B,D; i128 mul;int dh,cf,cc;};
struct GenPair{ i128 S; vector<i128> val0,val1;};
static GenPair build_gen_pair(long long P0,long long P1,long long Q,int M=25000,int H=416){
 i128 S=1;for(auto z:Gextra){i128 g=gcd128(S,(i128)z.D);S=(S/g)*z.D;} auto op=build_old_pair(P0,P1,Q);
 auto F0=[&](int J,bool one)->i128{if(J<0)J=-J;int k=J/8,r=J%8;if(k>=2600)return 0;if(r==0)return(i128)(one?op.fi1[k]:op.fi0[k])*8*S;if(r<=4)return(i128)(one?op.fr1[r][k]:op.fr0[r][k])*S;return(i128)(one?op.fs1[8-r][k]:op.fs0[8-r][k])*S;};
 vector<Act>acts;for(int p=0;p<=192;p++)acts.push_back({true,p,192,192,S/192,9*p+2112,11*p+1728,11*p+1728});for(auto z:Gextra){i128 mul=S/z.D;long long hn=1728*z.A+2112*z.B,cn=2112*z.A+1728*z.B;acts.push_back({false,z.A,z.B,z.D,mul,(int)((hn+z.D-1)/z.D),(int)(cn/z.D),(int)((cn+z.D-1)/z.D)});}
 vector<i128> p0(M+1),c0(M+1),p1(M+1),c1(M+1);for(int J=0;J<=M;J++){p0[J]=F0(J,false);p1[J]=F0(J,true);}
 for(int d=0;d<H;d++){
#pragma omp parallel for schedule(static)
  for(int J=0;J<=M;J++){i128 best0=F0(J,false),best1=F0(J,true);int bi=-1;
   for(int ia=0;ia<(int)acts.size();ia++){auto a=acts[ia];i128 m=max(a.A,a.B),rh0,rl0;if(a.base){rh0=(i128)8*((i128)45*a.A*Q-(i128)9600*P0)*S;rl0=(i128)8*((i128)-55*a.A*Q-(i128)9600*P0)*S;}else{rh0=(i128)8*((i128)8640*Q*a.A-(i128)9600*P0*m)*a.mul;rl0=(i128)8*((i128)-10560*Q*a.A-(i128)9600*P0*m)*a.mul;}int jh=J+a.dh;i128 hi0=rh0+(jh<=M?p0[jh]:0),lo0;if(a.base){int c=a.cf;if(J>=c)lo0=rl0+p0[J-c];else{int jl=c-J;i128 rr0=(i128)8*((i128)8640*Q-(i128)9600*P0)*S-(i128)40*Q*J*S;lo0=rr0+(jl<=M?p0[jl]:0);}}else{i128 cn=(i128)2112*a.A+1728*a.B;if((i128)J*a.D>=cn)lo0=rl0+p0[J-a.cf];else{int jl=a.cc-J;i128 rr0=(i128)8*((i128)8640*Q*a.B-(i128)9600*P0*m)*a.mul-(i128)40*Q*J*S;lo0=rr0+(jl<=M?p0[jl]:0);}}i128 z0=min(hi0,lo0);if(z0>best0){best0=z0;bi=ia;}}
   if(bi>=0){auto a=acts[bi];i128 m=max(a.A,a.B),rh1,rl1;if(a.base){rh1=(i128)8*((i128)45*a.A*Q-(i128)9600*P1)*S;rl1=(i128)8*((i128)-55*a.A*Q-(i128)9600*P1)*S;}else{rh1=(i128)8*((i128)8640*Q*a.A-(i128)9600*P1*m)*a.mul;rl1=(i128)8*((i128)-10560*Q*a.A-(i128)9600*P1*m)*a.mul;}int jh=J+a.dh;i128 hi1=rh1+(jh<=M?p1[jh]:0),lo1;if(a.base){int c=a.cf;if(J>=c)lo1=rl1+p1[J-c];else{int jl=c-J;i128 rr1=(i128)8*((i128)8640*Q-(i128)9600*P1)*S-(i128)40*Q*J*S;lo1=rr1+(jl<=M?p1[jl]:0);}}else{i128 cn=(i128)2112*a.A+1728*a.B;if((i128)J*a.D>=cn)lo1=rl1+p1[J-a.cf];else{int jl=a.cc-J;i128 rr1=(i128)8*((i128)8640*Q*a.B-(i128)9600*P1*m)*a.mul-(i128)40*Q*J*S;lo1=rr1+(jl<=M?p1[jl]:0);}}best1=min(hi1,lo1);}c0[J]=best0;c1[J]=best1;}
  p0.swap(c0);p1.swap(c1);
 }
 return {S,p0,p1};
}
int main(){long long P0=21476383,Q=4870886400,P1=P0+1;auto g=build_gen_pair(P0,P1,Q);if(s128(g.S)!="202391574968484000000000")return 10;struct T{int J;const char* v0;const char* v1;};T ts[]={{7015,"57719977623155054880651571200000000000","57719977421087306432117145600000000000"},{812,"151086287291137698427224853680000000000","151086286762215470511301347840000000000"},{4483,"89757393707928277928706048000000000000","89757393086181359625523200000000000000"},{2824,"115550511421873896362731622400000000000","115550510940020034677764915200000000000"}};for(auto t:ts){if(s128(g.val0[t.J])!=string(t.v0))return 11;if(s128(g.val1[t.J])!=string(t.v1))return 12;}cout<<"I0130_P21476383_FROZEN_CHORD_PASS\n";cout<<"S="<<s128(g.S)<<"\n";for(auto t:ts)cout<<"J="<<t.J<<" F0="<<s128(g.val0[t.J])<<" F1frozen="<<s128(g.val1[t.J])<<" diff="<<s128(g.val1[t.J]-g.val0[t.J])<<"\n";}
