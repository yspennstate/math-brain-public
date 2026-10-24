#include <bits/stdc++.h>
#include <omp.h>
using namespace std;
using i128=__int128_t;
static string s128(i128 x){ if(x==0)return "0"; bool neg=x<0; if(neg)x=-x; string s; while(x){s.push_back('0'+x%10);x/=10;} if(neg)s.push_back('-'); reverse(s.begin(),s.end()); return s; }
struct BaseGeom{int x,y,dh,c,m;};
static vector<pair<int,int>> old654_points(){ vector<pair<int,int>>ps; for(int i=0;i<=24;i++)for(int j=0;j<=24;j++)ps.push_back({40*i,40*j}); const int ex[][2]={{6,236},{13,233},{67,237},{26,236},{94,234},{84,234},{3,223},{3,233},{74,234},{114,234},{4,234},{176,236},{115,235}}; for(auto&p:ex)ps.push_back({4*p[0],4*p[1]}); const int cut[][2]={{179,959},{613,953},{649,949},{539,959},{775,955},{885,945},{561,941},{419,959},{586,946},{215,955},{579,959},{70,910},{527,947},{497,957},{900,940},{291,951}}; for(auto&p:cut)ps.push_back({p[0],p[1]}); return ps; }
static vector<BaseGeom> oldgeom(){vector<BaseGeom> as;for(auto[x,y]:old654_points())as.push_back({x,y,(9*x+11*y)/40,(11*x+9*y)/40,max(x,y)});return as;}

struct OldRes{ vector<long long> fi; array<vector<long long>,5> fr,fs; vector<int> wi; array<vector<int>,5> wr,ws;}; // weights in units 1/960
static OldRes build_old(long long P,long long Q,int M=2600,int H=612){
 auto as=oldgeom(); int A=as.size(); OldRes out;
 vector<long long> prev(M+1),cur(M+1); vector<int> wp(M+1),wc(M+1);
 for(int h=0;h<H;h++){
#pragma omp parallel for schedule(static)
  for(int k=0;k<=M;k++){
   long long best=0; int bw=0;
   for(int ia=0;ia<A;ia++){auto a=as[ia]; long long hb=9LL*a.x*Q-10LL*P*a.m, lb=-11LL*a.x*Q-10LL*P*a.m, rb=9LL*a.y*Q-10LL*P*a.m; int kh=k+a.dh; long long hi=hb+(kh<=M?prev[kh]:0),lo; int wh=(kh<=M?wp[kh]:0), wl;
    if(k>=a.c){lo=lb+prev[k-a.c];wl=wp[k-a.c];} else {int kl=a.c-k; lo=rb-40LL*k*Q+prev[kl]; wl=wp[kl];}
    long long z=min(hi,lo); if(z>best){best=z; bw=a.m+max(wh,wl);} }
   cur[k]=best; wc[k]=bw;
  }
  prev.swap(cur); wp.swap(wc);
 }
 out.fi=prev; out.wi=wp;
 for(int r=1;r<=4;r++){
  int sr=8-r; vector<long long> pr(M+1),ps(M+1),cr(M+1),cs(M+1); vector<int> wpr(M+1),wps(M+1),wcr(M+1),wcs(M+1);
  for(int h=0;h<H;h++){
#pragma omp parallel for schedule(static)
   for(int k=0;k<=M;k++){
    long long br=0,bs=0; int bwr=0,bws=0;
    for(int ia=0;ia<A;ia++){auto a=as[ia]; long long hb=(9LL*a.x*Q-10LL*P*a.m)*8,lb=(-11LL*a.x*Q-10LL*P*a.m)*8,rb=(9LL*a.y*Q-10LL*P*a.m)*8; int kh=k+a.dh;
      long long HR=hb+(kh<=M?pr[kh]:0), HS=hb+(kh<=M?ps[kh]:0), LR,LS; int whr=(kh<=M?wpr[kh]:0), whs=(kh<=M?wps[kh]:0), wlr,wls;
      if(k>=a.c){LR=lb+pr[k-a.c];LS=lb+ps[k-a.c];wlr=wpr[k-a.c];wls=wps[k-a.c];}
      else {int kl=a.c-k-1; long long xr=1LL*k*8+r,xs=1LL*k*8+sr; LR=rb-40LL*xr*Q+ps[kl]; LS=rb-40LL*xs*Q+pr[kl]; wlr=wps[kl];wls=wpr[kl];}
      long long zr=min(HR,LR),zs=min(HS,LS); if(zr>br){br=zr;bwr=a.m+max(whr,wlr);} if(zs>bs){bs=zs;bws=a.m+max(whs,wls);} }
    cr[k]=br;cs[k]=bs;wcr[k]=bwr;wcs[k]=bws;
   }
   pr.swap(cr);ps.swap(cs);wpr.swap(wcr);wps.swap(wcs);
  }
  out.fr[r]=pr;out.fs[r]=ps;out.wr[r]=wpr;out.ws[r]=wps;
 }
 return out;
}
static i128 gcd128(i128 a,i128 b){if(a<0)a=-a;if(b<0)b=-b;while(b){i128 r=a%b;a=b;b=r;}return a;}
struct RatAct{long long A,B,D;}; static vector<RatAct> Gextra={{7193,11628,11628},{871,3840,3840},{2591,3840,3840},{6858927,11100227,11162880},{13,704,704},{47,88,88},{377,1056,1056},{39,176,176},{641,1056,1056},{179,1056,1056},{3,88,88},{105,176,176},{61,176,176},{721,2112,2112},{17,176,176},{189,704,704},{509,1056,1056},{43,132,132},{311,1056,1056},{413,2112,2112},{35,704,704},{255,704,704},{289,1056,1056},{71,432,432},{193,2112,2112},{45,352,352},{215,2112,2112},{25,864,864},{145,704,704},{133,864,864},{25,1056,1056},{239,1728,1728},{185,1728,1728},{527,1728,1728},{23,352,352},{57,704,704},{139,528,528},{281,2112,2112},{245,1056,1056},{91,1056,1056},{815,1728,1728},{95,1728,1728},{5,66,66},{43530775821LL,208953177301LL,7426362113280LL},{435,704,704},{228175945101LL,1292743289321LL,1336500000000LL},{630860931LL,3574176551LL,3695155200LL}};
struct Act{bool base; long long A,B,D; i128 mul;int dh,cf,cc;};
struct GenRes{ i128 S; vector<i128> val,w;}; // weight scaled by S
static GenRes build_gen(long long P,long long Q,int M=25000,int H=416){
 i128 S=1;for(auto z:Gextra){i128 g=gcd128(S,(i128)z.D);S=(S/g)*z.D;} auto op=build_old(P,Q); if(S%960!=0){cerr<<"Smod\n";exit(2);} i128 oldmul=S/960;
 auto F0=[&](int J)->i128{if(J<0)J=-J;int k=J/8,r=J%8;if(k>=2600)return 0;if(r==0)return(i128)op.fi[k]*8*S;if(r<=4)return(i128)op.fr[r][k]*S;return(i128)op.fs[8-r][k]*S;};
 auto W0=[&](int J)->i128{if(J<0)J=-J;int k=J/8,r=J%8;if(k>=2600)return 0;if(r==0)return(i128)op.wi[k]*oldmul;if(r<=4)return(i128)op.wr[r][k]*oldmul;return(i128)op.ws[8-r][k]*oldmul;};
 vector<Act>acts;for(int p=0;p<=192;p++)acts.push_back({true,p,192,192,S/192,9*p+2112,11*p+1728,11*p+1728}); for(auto z:Gextra){i128 mul=S/z.D; long long hn=1728*z.A+2112*z.B,cn=2112*z.A+1728*z.B; acts.push_back({false,z.A,z.B,z.D,mul,(int)((hn+z.D-1)/z.D),(int)(cn/z.D),(int)((cn+z.D-1)/z.D)});}
 vector<i128> prev(M+1),cur(M+1),wp(M+1),wc(M+1); for(int J=0;J<=M;J++){prev[J]=F0(J);wp[J]=W0(J);} 
 for(int d=0;d<H;d++){
#pragma omp parallel for schedule(static)
  for(int J=0;J<=M;J++){
   i128 best=F0(J), bw=W0(J);
   for(int ia=0;ia<(int)acts.size();ia++){auto a=acts[ia]; i128 m=max(a.A,a.B); i128 rh,rl,mw; if(a.base){rh=(i128)8*((i128)45*a.A*Q-(i128)9600*P)*S;rl=(i128)8*((i128)-55*a.A*Q-(i128)9600*P)*S;mw=S;} else {rh=(i128)8*((i128)8640*Q*a.A-(i128)9600*P*m)*a.mul;rl=(i128)8*((i128)-10560*Q*a.A-(i128)9600*P*m)*a.mul;mw=m*a.mul;}
    int jh=J+a.dh; i128 hi=rh+(jh<=M?prev[jh]:0),lo; i128 wh=(jh<=M?wp[jh]:0),wl;
    if(a.base){int c=a.cf;if(J>=c){lo=rl+prev[J-c];wl=wp[J-c];}else{int jl=c-J;i128 rr=(i128)8*((i128)8640*Q-(i128)9600*P)*S-(i128)40*Q*J*S;lo=rr+(jl<=M?prev[jl]:0);wl=(jl<=M?wp[jl]:0);}}
    else{i128 cn=(i128)2112*a.A+1728*a.B;if((i128)J*a.D>=cn){lo=rl+prev[J-a.cf];wl=wp[J-a.cf];}else{int jl=a.cc-J;i128 rr=(i128)8*((i128)8640*Q*a.B-(i128)9600*P*m)*a.mul-(i128)40*Q*J*S;lo=rr+(jl<=M?prev[jl]:0);wl=(jl<=M?wp[jl]:0);}}
    i128 z=min(hi,lo); if(z>best){best=z;bw=mw+max(wh,wl);} }
   cur[J]=best;wc[J]=bw;
  }
  prev.swap(cur);wp.swap(wc);
 }
 return {S,prev,wp};
}
int main(){
 long long P=21454951LL,Q=4870886400LL; auto g=build_gen(P,Q);
 if(s128(g.S)!="202391574968484000000000") return 10;
 struct T{int J; const char* v;};
 T ts[]={{7016,"57721999155541552891783987200000000000"},{811,"151136423214451135550133350400000000000"},{4480,"89844598037244560704230071378582323200"},{2823,"115582335272231743319992012800000000000"}};
 for(auto t:ts){ if(s128(g.val[t.J])!=string(t.v)) return 11; if(g.w[t.J]*960 != g.S*(i128)799781) return 12; }
 cout<<"I0130_EXACT_PATH_WEIGHT_PASS\n";
 cout<<"P1="<<P<<" Q="<<Q<<" S="<<s128(g.S)<<"\n";
 cout<<"generated_plus_old654_worst_path_weight=799781/960\n";
 for(auto t:ts) cout<<"J="<<t.J<<" value="<<s128(g.val[t.J])<<" weight_num_over_S="<<s128(g.w[t.J])<<"/"<<s128(g.S)<<"\n";
 cout<<"target_states_all_same_weight=1\n";
 return 0;
}
