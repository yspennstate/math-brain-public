#include <bits/stdc++.h>
#include <omp.h>
#include <boost/multiprecision/cpp_int.hpp>
using namespace std; using i128=__int128_t; using boost::multiprecision::cpp_int;
static string s128(i128 x){ if(x==0)return "0"; bool neg=x<0; if(neg)x=-x; string s; while(x){s.push_back('0'+x%10);x/=10;} if(neg)s.push_back('-'); reverse(s.begin(),s.end()); return s; }
struct BaseGeom{int x,y,dh,c,m;};
static vector<pair<int,int>> old654_points(){ vector<pair<int,int>>ps; for(int i=0;i<=24;i++)for(int j=0;j<=24;j++)ps.push_back({40*i,40*j}); const int ex[][2]={{6,236},{13,233},{67,237},{26,236},{94,234},{84,234},{3,223},{3,233},{74,234},{114,234},{4,234},{176,236},{115,235}}; for(auto&p:ex)ps.push_back({4*p[0],4*p[1]}); const int cut[][2]={{179,959},{613,953},{649,949},{539,959},{775,955},{885,945},{561,941},{419,959},{586,946},{215,955},{579,959},{70,910},{527,947},{497,957},{900,940},{291,951}}; for(auto&p:cut)ps.push_back({p[0],p[1]}); return ps; }
static vector<BaseGeom> oldgeom(){vector<BaseGeom> as;for(auto[x,y]:old654_points())as.push_back({x,y,(9*x+11*y)/40,(11*x+9*y)/40,max(x,y)});return as;}
struct OldPolicy {int M,H; vector<short> pol_int; array<vector<short>,5> pol_r,pol_s; vector<long long> final_int; array<vector<long long>,5> final_r,final_s;};
static OldPolicy build_old_policy(long long P,long long Q,int M=2600,int H=612){auto as=oldgeom(); int A=as.size(); OldPolicy op;op.M=M;op.H=H;op.pol_int.assign((size_t)H*(M+1),-1);for(int r=1;r<=4;r++){op.pol_r[r].assign((size_t)H*(M+1),-1);op.pol_s[r].assign((size_t)H*(M+1),-1);} vector<long long> prev(M+1),cur(M+1);
 for(int h=0;h<H;h++){
#pragma omp parallel for schedule(static)
 for(int k=0;k<=M;k++){long long best=0;short bi=-1; for(short ia=0;ia<A;ia++){auto a=as[ia];long long hb=9LL*a.x*Q-10LL*P*a.m, lb=-11LL*a.x*Q-10LL*P*a.m, rb=9LL*a.y*Q-10LL*P*a.m;long long hi=hb+((k+a.dh<=M)?prev[k+a.dh]:0),lo;if(k>=a.c)lo=lb+prev[k-a.c];else lo=rb-40LL*k*Q+prev[a.c-k];long long z=min(hi,lo);if(z>best){best=z;bi=ia;}}cur[k]=best;op.pol_int[(size_t)h*(M+1)+k]=bi;} prev.swap(cur);} op.final_int=prev;
 for(int r=1;r<=4;r++){int sr=8-r;vector<long long> pr(M+1),ps(M+1),cr(M+1),cs(M+1);for(int h=0;h<H;h++){
#pragma omp parallel for schedule(static)
 for(int k=0;k<=M;k++){long long br=0,bs=0;short bir=-1,bis=-1;for(short ia=0;ia<A;ia++){auto a=as[ia];long long hb=(9LL*a.x*Q-10LL*P*a.m)*8,lb=(-11LL*a.x*Q-10LL*P*a.m)*8,rb=(9LL*a.y*Q-10LL*P*a.m)*8;int kh=k+a.dh;long long HR=hb+(kh<=M?pr[kh]:0),HS=hb+(kh<=M?ps[kh]:0),LR,LS;if(k>=a.c){LR=lb+pr[k-a.c];LS=lb+ps[k-a.c];}else{int kl=a.c-k-1;long long xr=1LL*k*8+r,xs=1LL*k*8+sr;LR=rb-40LL*xr*Q+ps[kl];LS=rb-40LL*xs*Q+pr[kl];}long long zr=min(HR,LR),zs=min(HS,LS);if(zr>br){br=zr;bir=ia;}if(zs>bs){bs=zs;bis=ia;}}cr[k]=br;cs[k]=bs;op.pol_r[r][(size_t)h*(M+1)+k]=bir;op.pol_s[r][(size_t)h*(M+1)+k]=bis;}pr.swap(cr);ps.swap(cs);}op.final_r[r]=pr;op.final_s[r]=ps;}
 return op;}
struct OldEval{vector<long long> fi;array<vector<long long>,5> fr,fs;};
static OldEval eval_old_policy(const OldPolicy&op,long long P,long long Q){auto as=oldgeom();int M=op.M,H=op.H;OldEval oe;vector<long long>prev(M+1),cur(M+1);for(int h=0;h<H;h++){
#pragma omp parallel for schedule(static)
 for(int k=0;k<=M;k++){short ia=op.pol_int[(size_t)h*(M+1)+k];if(ia<0){cur[k]=0;continue;}auto a=as[ia];long long hb=9LL*a.x*Q-10LL*P*a.m,lb=-11LL*a.x*Q-10LL*P*a.m,rb=9LL*a.y*Q-10LL*P*a.m;long long hi=hb+((k+a.dh<=M)?prev[k+a.dh]:0),lo;if(k>=a.c)lo=lb+prev[k-a.c];else lo=rb-40LL*k*Q+prev[a.c-k];cur[k]=min(hi,lo);}prev.swap(cur);}oe.fi=prev;
 for(int r=1;r<=4;r++){int sr=8-r;vector<long long>pr(M+1),ps(M+1),cr(M+1),cs(M+1);for(int h=0;h<H;h++){
#pragma omp parallel for schedule(static)
 for(int k=0;k<=M;k++){short iar=op.pol_r[r][(size_t)h*(M+1)+k],ias=op.pol_s[r][(size_t)h*(M+1)+k];auto calc=[&](short ia,bool isS)->long long{if(ia<0)return 0;auto a=as[ia];long long hb=(9LL*a.x*Q-10LL*P*a.m)*8,lb=(-11LL*a.x*Q-10LL*P*a.m)*8,rb=(9LL*a.y*Q-10LL*P*a.m)*8;int kh=k+a.dh;long long hi=hb+(kh<=M?(isS?ps[kh]:pr[kh]):0),lo;if(k>=a.c)lo=lb+(isS?ps[k-a.c]:pr[k-a.c]);else{int kl=a.c-k-1;long long x=1LL*k*8+(isS?sr:r);lo=rb-40LL*x*Q+(isS?pr[kl]:ps[kl]);}return min(hi,lo);};cr[k]=calc(iar,false);cs[k]=calc(ias,true);}pr.swap(cr);ps.swap(cs);}oe.fr[r]=pr;oe.fs[r]=ps;}return oe;}
static i128 gcd128(i128 a,i128 b){if(a<0)a=-a;if(b<0)b=-b;while(b){i128 r=a%b;a=b;b=r;}return a;}
struct RatAct{long long A,B,D;}; static vector<RatAct> Gextra={{7193,11628,11628},{871,3840,3840},{2591,3840,3840},{6858927,11100227,11162880},{13,704,704},{47,88,88},{377,1056,1056},{39,176,176},{641,1056,1056},{179,1056,1056},{3,88,88},{105,176,176},{61,176,176},{721,2112,2112},{17,176,176},{189,704,704},{509,1056,1056},{43,132,132},{311,1056,1056},{413,2112,2112},{35,704,704},{255,704,704},{289,1056,1056},{71,432,432},{193,2112,2112},{45,352,352},{215,2112,2112},{25,864,864},{145,704,704},{133,864,864},{25,1056,1056},{239,1728,1728},{185,1728,1728},{527,1728,1728},{23,352,352},{57,704,704},{139,528,528},{281,2112,2112},{245,1056,1056},{91,1056,1056},{815,1728,1728},{95,1728,1728},{5,66,66},{43530775821LL,208953177301LL,7426362113280LL},{435,704,704},{228175945101LL,1292743289321LL,1336500000000LL},{630860931LL,3574176551LL,3695155200LL}};
struct Act{bool base; long long A,B,D; i128 mul;int dh,cf,cc;};
struct GenPolicy{int M,H; i128 S; vector<short> pol; vector<i128> finalv; OldPolicy old;};
static GenPolicy build_gen_policy(long long P,long long Q,int M=25000,int H=416){GenPolicy gp;gp.M=M;gp.H=H;gp.old=build_old_policy(P,Q); i128 S=1;for(auto z:Gextra){i128 g=gcd128(S,(i128)z.D);S=(S/g)*z.D;}gp.S=S;auto &op=gp.old; auto F0=[&](int J)->i128{if(J<0)J=-J;int k=J/8,r=J%8;if(k>=2600)return 0;if(r==0)return(i128)op.final_int[k]*8*S;if(r<=4)return(i128)op.final_r[r][k]*S;return(i128)op.final_s[8-r][k]*S;};vector<Act>acts;for(int p=0;p<=192;p++)acts.push_back({true,p,192,192,S/192,9*p+2112,11*p+1728,11*p+1728});for(auto z:Gextra){i128 mul=S/z.D;long long hn=1728*z.A+2112*z.B,cn=2112*z.A+1728*z.B;acts.push_back({false,z.A,z.B,z.D,mul,(int)((hn+z.D-1)/z.D),(int)(cn/z.D),(int)((cn+z.D-1)/z.D)});}gp.pol.assign((size_t)H*(M+1),-1);vector<i128>prev(M+1),cur(M+1);for(int J=0;J<=M;J++)prev[J]=F0(J);for(int d=0;d<H;d++){
#pragma omp parallel for schedule(static)
 for(int J=0;J<=M;J++){i128 best=F0(J);short bi=-1;for(short ia=0;ia<(short)acts.size();ia++){auto a=acts[ia];i128 m=max(a.A,a.B);i128 rh,rl;if(a.base){rh=(i128)8*((i128)45*a.A*Q-(i128)9600*P)*S;rl=(i128)8*((i128)-55*a.A*Q-(i128)9600*P)*S;}else{rh=(i128)8*((i128)8640*Q*a.A-(i128)9600*P*m)*a.mul;rl=(i128)8*((i128)-10560*Q*a.A-(i128)9600*P*m)*a.mul;}int jh=J+a.dh;i128 hi=rh+(jh<=M?prev[jh]:0),lo;if(a.base){int c=a.cf;if(J>=c)lo=rl+prev[J-c];else{int jl=c-J;i128 rr=(i128)8*((i128)8640*Q-(i128)9600*P)*S-(i128)40*Q*J*S;lo=rr+(jl<=M?prev[jl]:0);}}else{i128 cn=(i128)2112*a.A+1728*a.B;if((i128)J*a.D>=cn)lo=rl+prev[J-a.cf];else{int jl=a.cc-J;i128 rr=(i128)8*((i128)8640*Q*a.B-(i128)9600*P*m)*a.mul-(i128)40*Q*J*S;lo=rr+(jl<=M?prev[jl]:0);}}i128 z=min(hi,lo);if(z>best){best=z;bi=ia;}}cur[J]=best;gp.pol[(size_t)d*(M+1)+J]=bi;}prev.swap(cur);}gp.finalv=prev;return gp;}
static vector<i128> eval_gen_policy(const GenPolicy&gp,long long P,long long Q){int M=gp.M,H=gp.H;i128 S=gp.S;auto oe=eval_old_policy(gp.old,P,Q);auto F0=[&](int J)->i128{if(J<0)J=-J;int k=J/8,r=J%8;if(k>=2600)return 0;if(r==0)return(i128)oe.fi[k]*8*S;if(r<=4)return(i128)oe.fr[r][k]*S;return(i128)oe.fs[8-r][k]*S;};vector<Act>acts;for(int p=0;p<=192;p++)acts.push_back({true,p,192,192,S/192,9*p+2112,11*p+1728,11*p+1728});for(auto z:Gextra){i128 mul=S/z.D;long long hn=1728*z.A+2112*z.B,cn=2112*z.A+1728*z.B;acts.push_back({false,z.A,z.B,z.D,mul,(int)((hn+z.D-1)/z.D),(int)(cn/z.D),(int)((cn+z.D-1)/z.D)});}vector<i128>prev(M+1),cur(M+1);for(int J=0;J<=M;J++)prev[J]=F0(J);for(int d=0;d<H;d++){
#pragma omp parallel for schedule(static)
 for(int J=0;J<=M;J++){short ia=gp.pol[(size_t)d*(M+1)+J];if(ia<0){cur[J]=F0(J);continue;}auto a=acts[ia];i128 m=max(a.A,a.B);i128 rh,rl;if(a.base){rh=(i128)8*((i128)45*a.A*Q-(i128)9600*P)*S;rl=(i128)8*((i128)-55*a.A*Q-(i128)9600*P)*S;}else{rh=(i128)8*((i128)8640*Q*a.A-(i128)9600*P*m)*a.mul;rl=(i128)8*((i128)-10560*Q*a.A-(i128)9600*P*m)*a.mul;}int jh=J+a.dh;i128 hi=rh+(jh<=M?prev[jh]:0),lo;if(a.base){int c=a.cf;if(J>=c)lo=rl+prev[J-c];else{int jl=c-J;i128 rr=(i128)8*((i128)8640*Q-(i128)9600*P)*S-(i128)40*Q*J*S;lo=rr+(jl<=M?prev[jl]:0);}}else{i128 cn=(i128)2112*a.A+1728*a.B;if((i128)J*a.D>=cn)lo=rl+prev[J-a.cf];else{int jl=a.cc-J;i128 rr=(i128)8*((i128)8640*Q*a.B-(i128)9600*P*m)*a.mul-(i128)40*Q*J*S;lo=rr+(jl<=M?prev[jl]:0);}}cur[J]=min(hi,lo);}prev.swap(cur);}return prev;}
static cpp_int gcdbig(cpp_int a,cpp_int b){if(a<0)a=-a;if(b<0)b=-b;while(b!=0){cpp_int r=a%b;a=b;b=r;}return a;}
static string frac(cpp_int n,cpp_int d){if(d<0){n=-n;d=-d;}cpp_int g=gcdbig(n,d);n/=g;d/=g;return n.convert_to<string>()+"/"+d.convert_to<string>();}
struct BR{cpp_int n,d;BR(cpp_int N=0,cpp_int D=1):n(N),d(D){norm();}void norm(){if(d<0){n=-n;d=-d;}cpp_int g=gcdbig(n,d);if(g!=0){n/=g;d/=g;}}};
static BR operator+(const BR&a,const BR&b){return BR(a.n*b.d+b.n*a.d,a.d*b.d);}static BR operator-(const BR&a,const BR&b){return BR(a.n*b.d-b.n*a.d,a.d*b.d);}static BR operator*(const BR&a,const BR&b){return BR(a.n*b.n,a.d*b.d);}static BR operator/(const BR&a,const BR&b){return BR(a.n*b.d,a.d*b.n);}static bool lt(const BR&a,const BR&b){return a.n*b.d<b.n*a.d;}static bool eq(const BR&a,const BR&b){return a.n*b.d==b.n*a.d;}static string brs(const BR&a){return a.n.convert_to<string>()+"/"+a.d.convert_to<string>();}
int main(){
    const long long Q=4870886400LL,P0=21424262LL,P1=P0+1;
    auto gp=build_gen_policy(P0,Q,25000,416);
    auto e1=eval_gen_policy(gp,P1,Q);
    const string hL0s="99492042123196259496854116320000000000";
    const string hH0s="99368713141163194267786091040000000000";
    const string hL1s="99492041516555666793032754480000000000";
    const string hH1s="99368712270804749368108228560000000000";
    if(s128(gp.finalv[3837])!=hL0s || s128(gp.finalv[3843])!=hH0s) return 10;
    if(s128(e1[3837])!=hL1s || s128(e1[3843])!=hH1s) return 11;
    cpp_int S(s128(gp.S)), hL0(hL0s), hH0(hH0s), hL1(hL1s), hH1(hH1s);
    cpp_int aN=hL0-hH0;
    cpp_int aD=cpp_int(8)*S*19200*Q;
    cpp_int H0=hH0*aD+cpp_int(8)*S*(cpp_int(8640)*Q-cpp_int(9600)*P0)*aN;
    cpp_int L0=hL0*aD+cpp_int(8)*S*(cpp_int(-10560)*Q-cpp_int(9600)*P0)*aN;
    cpp_int T0=cpp_int(8)*S*(cpp_int(12480)*Q+cpp_int(28800)*P0)*aD;
    if(H0!=L0) return 12;
    cpp_int G0=H0-T0;
    cpp_int H1=hH1*aD+cpp_int(8)*S*(cpp_int(8640)*Q-cpp_int(9600)*P1)*aN;
    cpp_int L1=hL1*aD+cpp_int(8)*S*(cpp_int(-10560)*Q-cpp_int(9600)*P1)*aN;
    cpp_int T1=cpp_int(8)*S*(cpp_int(12480)*Q+cpp_int(28800)*P1)*aD;
    cpp_int G1=min(H1,L1)-T1;
    if(!(G0>0 && G1<0 && H1<L1)) return 13;
    cpp_int thetaN=G0,thetaD=G0-G1; cpp_int gt=gcdbig(thetaN,thetaD);thetaN/=gt;thetaD/=gt;
    cpp_int epsN=cpp_int(P0)*thetaD+thetaN,epsD=cpp_int(Q)*thetaD; cpp_int ge=gcdbig(epsN,epsD);epsN/=ge;epsD/=ge;
    cpp_int UN=cpp_int(9)*epsD-cpp_int(10)*epsN,UD=cpp_int(10)*epsD;cpp_int gu=gcdbig(UN,UD);UN/=gu;UD/=gu;
    cpp_int WN=cpp_int(30)*UN-cpp_int(19)*UD,WD=cpp_int(30)*UD;cpp_int gw=gcdbig(WN,WD);WN/=gw;WD/=gw;
    cout<<"I0130_FIXED_POLICY_CONCAVITY_SECANT_PASS\n";
    cout<<"P0="<<P0<<" Q="<<Q<<" P1="<<P1<<" stable_depth=416 max_goods=1032\n";
    cout<<"h0_L="<<hL0<<" h0_H="<<hH0<<"\n";
    cout<<"frozen_P1_L="<<hL1<<" frozen_P1_H="<<hH1<<"\n";
    cout<<"root_gap0_num="<<G0<<" root_gap1_num="<<G1<<" high_is_limiting_at_P1=1\n";
    cout<<"theta="<<frac(thetaN,thetaD)<<"\n";
    cout<<"epsilon_secant="<<frac(epsN,epsD)<<"\n";
    cout<<"U_MIV="<<frac(UN,UD)<<"\n";
    cout<<"W_MIV="<<frac(WN,WD)<<"\n";
    BR tt(1,75), one(1,1);
    BR HL=BR(hL0)*(one-tt)+BR(hL1)*tt;
    BR HH=BR(hH0)*(one-tt)+BR(hH1)*tt;
    BR PP=BR(P0)+tt;
    BR aa=(HL-HH)/BR(cpp_int(8)*S*19200*Q);
    BR bb=(BR(3)-BR(2112)*aa)/BR(1728);
    BR uu=BR(1728)*aa+BR(2112)*bb, vv=BR(2112)*aa+BR(1728)*bb;
    if(!(lt(BR(0),bb)&&lt(bb,aa)&&lt(aa,BR(1))&&lt(BR(2),uu)&&lt(uu,BR(3))&&eq(vv,BR(3)))) return 20;
    BR EH=HH+BR(cpp_int(8)*S)*(BR(8640LL*Q)-BR(9600)*PP)*aa;
    BR EL=HL+BR(cpp_int(8)*S)*(BR(-10560LL*Q)-BR(9600)*PP)*aa;
    if(!eq(EH,EL)) return 21;
    BR TT=BR(cpp_int(8)*S)*(BR(12480LL*Q)+BR(28800)*PP);
    BR GG=EH-TT;
    if(!lt(BR(0),GG)) return 22;
    BR eps=BR(P0,Q)+BR(1,75LL*Q);
    BR U=BR(9,10)-eps, W=U-BR(19,30);
    if(brs(aa)!="713709407114023485799259/876290106656505905971200000") return 23;
    if(brs(bb)!="531020858023058767000741/716964632718959377612800000") return 24;
    if(brs(uu)!="3051599644925650328920741/1026902468738092858560000") return 25;
    if(brs(GG)!="1012311492739373792194846955000/21141") return 26;
    if(brs(U)!="327178012349/365316480000") return 27;
    if(brs(W)!="95810908349/365316480000") return 28;
    cout<<"theta_clean=1/75 chord_root_action_a="<<brs(aa)<<" b="<<brs(bb)<<" u="<<brs(uu)<<" v="<<brs(vv)<<"\n";
    cout<<"chord_equalized_gap="<<brs(GG)<<"\n";
    cout<<"clean_epsilon="<<brs(eps)<<" clean_U_MIV="<<brs(U)<<" clean_W_MIV="<<brs(W)<<"\n";
    cout<<"I0130_CHORD_EQUALIZER_1_OVER_75_PASS\n";
    return 0;
}
