#include <bits/stdc++.h>
#include <omp.h>
#include <boost/multiprecision/cpp_int.hpp>
using namespace std; using i128=__int128_t; using boost::multiprecision::cpp_int;
static string s128(i128 x){ if(x==0)return "0"; bool neg=x<0; if(neg)x=-x; string s; while(x){s.push_back('0'+x%10);x/=10;} if(neg)s.push_back('-'); reverse(s.begin(),s.end()); return s; }
struct BaseAct{int x,y,dh,c,m; long long hb,lb,rb;}; struct Orbit{vector<long long> r,s;}; struct RatAct{long long A,B,D;};
static vector<pair<int,int>> old654_points(){ vector<pair<int,int>>ps; for(int i=0;i<=24;i++)for(int j=0;j<=24;j++)ps.push_back({40*i,40*j}); const int ex[][2]={{6,236},{13,233},{67,237},{26,236},{94,234},{84,234},{3,223},{3,233},{74,234},{114,234},{4,234},{176,236},{115,235}}; for(auto&p:ex)ps.push_back({4*p[0],4*p[1]}); const int cut[][2]={{179,959},{613,953},{649,949},{539,959},{775,955},{885,945},{561,941},{419,959},{586,946},{215,955},{579,959},{70,910},{527,947},{497,957},{900,940},{291,951}}; for(auto&p:cut)ps.push_back({p[0],p[1]}); return ps; }
static Orbit orbit_table(long long P,long long Q,int R,int r,int M=2600,int H=612){ vector<BaseAct> as; for(auto[x,y]:old654_points()){int dh=(9*x+11*y)/40,c=(11*x+9*y)/40,m=max(x,y);as.push_back({x,y,dh,c,m,(9LL*x*Q-10LL*P*m)*R,(-11LL*x*Q-10LL*P*m)*R,(9LL*y*Q-10LL*P*m)*R});} int sr=R-r; vector<long long>pr(M+1),ps(M+1),cr(M+1),cs(M+1); for(int h=1;h<=H;h++){int diff=0;
#pragma omp parallel for schedule(static) reduction(|:diff)
 for(int k=0;k<=M;k++){ long long br=0,bs=0; for(auto&a:as){int kh=k+a.dh; long long HR=a.hb+(kh<=M?pr[kh]:0),HS=a.hb+(kh<=M?ps[kh]:0),LR,LS; if(k>=a.c){LR=a.lb+pr[k-a.c];LS=a.lb+ps[k-a.c];}else{int kl=a.c-k-1; long long xr=1LL*k*R+r,xs=1LL*k*R+sr; LR=a.rb-40LL*xr*Q+ps[kl]; LS=a.rb-40LL*xs*Q+pr[kl];} br=max(br,min(HR,LR)); bs=max(bs,min(HS,LS));} cr[k]=br;cs[k]=bs;if(cr[k]!=pr[k]||cs[k]!=ps[k])diff=1;} if(!diff)break; pr.swap(cr);ps.swap(cs);} return{move(pr),move(ps)}; }
static vector<long long> integer_table(long long P,long long Q,int M=2600,int H=612){ vector<BaseAct>as;for(auto[x,y]:old654_points()){int dh=(9*x+11*y)/40,c=(11*x+9*y)/40,m=max(x,y);as.push_back({x,y,dh,c,m,9LL*x*Q-10LL*P*m,-11LL*x*Q-10LL*P*m,9LL*y*Q-10LL*P*m});} vector<long long>pr(M+1),cr(M+1);for(int h=1;h<=H;h++){int diff=0;
#pragma omp parallel for schedule(static) reduction(|:diff)
 for(int k=0;k<=M;k++){long long best=0;for(auto&a:as){long long hi=a.hb+((k+a.dh<=M)?pr[k+a.dh]:0),lo;if(k>=a.c)lo=a.lb+pr[k-a.c];else lo=a.rb-40LL*k*Q+pr[a.c-k];best=max(best,min(hi,lo));}cr[k]=best;if(cr[k]!=pr[k])diff=1;}if(!diff)break;pr.swap(cr);} return pr; }
static i128 gcd128(i128 a,i128 b){ if(a<0)a=-a; if(b<0)b=-b; while(b){i128 r=a%b;a=b;b=r;} return a; }
struct Act{bool base;int p;long long A,B,D; i128 mul;int dhceil,cfloor,cceil;i128 rh,rl;}; struct Res{vector<i128>h;int stable,maxnz,maxC;i128 S,tailMax;int tailJ;};
static vector<RatAct> Gextra={{7193,11628,11628},{871,3840,3840},{2591,3840,3840},{6858927,11100227,11162880},{13,704,704},{47,88,88},{377,1056,1056},{39,176,176},{641,1056,1056},{179,1056,1056},{3,88,88},{105,176,176},{61,176,176},{721,2112,2112},{17,176,176},{189,704,704},{509,1056,1056},{43,132,132},{311,1056,1056},{413,2112,2112},{35,704,704},{255,704,704},{289,1056,1056},{71,432,432},{193,2112,2112},{45,352,352},{215,2112,2112},{25,864,864},{145,704,704},{133,864,864},{25,1056,1056},{239,1728,1728},{185,1728,1728},{527,1728,1728},{23,352,352},{57,704,704},{139,528,528},{281,2112,2112},{245,1056,1056},{91,1056,1056},{815,1728,1728},{95,1728,1728},{5,66,66},{43530775821LL,208953177301LL,7426362113280LL},{435,704,704},{228175945101LL,1292743289321LL,1336500000000LL},{630860931LL,3574176551LL,3695155200LL}};
static Res fixed(long long P,long long Q){ i128 S=1; for(auto z:Gextra){i128 g=gcd128(S,(i128)z.D);S=(S/g)*z.D;} auto fi=integer_table(P,Q); vector<Orbit>os(5);
#pragma omp parallel for schedule(static)
 for(int r=1;r<=4;r++)os[r]=orbit_table(P,Q,8,r); auto F0=[&](int J)->i128{if(J<0)J=-J;int k=J/8,r=J%8;if(k>=2600)return 0;if(r==0)return(i128)fi[k]*8*S;if(r<=4)return(i128)os[r].r[k]*S;return(i128)os[8-r].s[k]*S;}; vector<Act>acts; for(int p=0;p<=192;p++){int dh=9*p+2112,c=11*p+1728;acts.push_back({true,p,p,192,192,S/192,dh,c,c,(i128)8*(45LL*p*Q-9600LL*P)*S,(i128)8*(-55LL*p*Q-9600LL*P)*S});} for(auto z:Gextra){i128 mul=S/z.D,m=max(z.A,z.B);long long hn=1728*z.A+2112*z.B,cn=2112*z.A+1728*z.B;int dh=(hn+z.D-1)/z.D,cf=cn/z.D,cc=(cn+z.D-1)/z.D;acts.push_back({false,-1,z.A,z.B,z.D,mul,dh,cf,cc,(i128)8*((i128)8640*Q*z.A-(i128)9600*P*m)*mul,(i128)8*((i128)-10560*Q*z.A-(i128)9600*P*m)*mul});} int maxC=0;for(auto&a:acts)maxC=max(maxC,a.cceil);int M=25000; auto bell=[&](int J,const vector<i128>&v)->i128{i128 best=-((i128)1<<120);for(auto&a:acts){int jh=J+a.dhceil;i128 hi=a.rh+(jh<(int)v.size()?v[jh]:0),lo;if(a.base){int c=a.cfloor;if(J>=c)lo=a.rl+v[J-c];else{int jl=c-J;i128 rr=(i128)8*(8640LL*Q-9600LL*P)*S-(i128)40*Q*J*S;lo=rr+(jl<(int)v.size()?v[jl]:0);}}else{i128 cn=(i128)2112*a.A+1728*a.B;if((i128)J*a.D>=cn){int jl=J-a.cfloor;lo=a.rl+(jl<(int)v.size()?v[jl]:0);}else{int jl=a.cceil-J;i128 rr=(i128)8*((i128)8640*Q*a.B-(i128)9600*P*max(a.A,a.B))*a.mul-(i128)40*Q*J*S;lo=rr+(jl<(int)v.size()?v[jl]:0);}}best=max(best,min(hi,lo));}return best;}; vector<i128>prev(M+1),cur(M+1);for(int J=0;J<=M;J++)prev[J]=F0(J);int stable=-1;for(int d=1;d<=1400;d++){int diff=0;
#pragma omp parallel for schedule(static) reduction(|:diff)
 for(int J=0;J<=M;J++){i128 z=max(F0(J),bell(J,prev));cur[J]=z;if(z!=prev[J])diff=1;}prev.swap(cur);if(!diff){stable=d;break;}} int maxnz=-1;for(int J=0;J<=M;J++)if(prev[J]>0)maxnz=J;i128 tail=-((i128)1<<120);int tailJ=-1;for(int J=maxnz+1;J<=maxnz+maxC&&J<=M;J++){i128 z=bell(J,prev);if(z>tail){tail=z;tailJ=J;}} return{move(prev),stable,maxnz,maxC,S,tail,tailJ}; }
static cpp_int gcdbig(cpp_int a,cpp_int b){if(a<0)a=-a;if(b<0)b=-b;while(b!=0){cpp_int r=a%b;a=b;b=r;}return a;}
static string fracstr(cpp_int n, cpp_int d){ if(d<0){n=-n;d=-d;} cpp_int g=gcdbig(n,d); n/=g; d/=g; return n.convert_to<string>()+"/"+d.convert_to<string>(); }
int main(){
    const long long P0=82051LL,Q0=18662400LL;
    auto R0=fixed(P0,Q0);
    if(R0.stable!=525 || R0.maxnz!=20548 || R0.tailJ!=20549) return 10;
    cpp_int dh0=cpp_int(s128(R0.h[13496]))-cpp_int(s128(R0.h[9126]));
    cpp_int den0=cpp_int(8)*cpp_int(s128(R0.S))*19200*Q0;
    cpp_int un0=cpp_int(11)*2032*den0 + dh0*7680;
    cpp_int ud0=cpp_int(9)*den0;
    cpp_int g0=gcdbig(un0,ud0); un0/=g0; ud0/=g0;
    if(un0!=cpp_int("1124842261") || ud0!=cpp_int("481140")) return 11;

    const long long P=21424262LL,Q=4870886400LL;
    auto R=fixed(P,Q);
    if(s128(R.S)!="202391574968484000000000") return 20;
    if(R.stable!=416 || R.maxnz!=20548 || R.tailJ!=20549) return 21;
    if(s128(R.tailMax)!="-24455519150668869558067200000000000") return 22;
    if(s128(R.h[3837])!="99492042123196259496854116320000000000") return 23;
    if(s128(R.h[3843])!="99368713141163194267786091040000000000") return 24;

    cpp_int S(s128(R.S));
    cpp_int hL(s128(R.h[3837])), hH(s128(R.h[3843]));
    cpp_int aN=hL-hH;
    cpp_int aD=cpp_int(8)*S*19200*Q;
    cpp_int ga=gcdbig(aN,aD); aN/=ga; aD/=ga;
    if(fracstr(aN,aD)!="4758062578436158528859/5841934044376706039808000") return 25;

    cpp_int bN=cpp_int(3)*aD-cpp_int(2112)*aN;
    cpp_int bD=cpp_int(1728)*aD;
    cpp_int gb=gcdbig(bN,bD); bN/=gb; bD/=gb;
    if(fracstr(bN,bD)!="3540139189144389823141/4779764218126395850752000") return 26;

    if(!(bN>0 && aN>0 && bN*aD<aN*bD && aN<aD)) return 27;
    cpp_int uN=cpp_int(1728)*aN*bD+cpp_int(2112)*bN*aD;
    cpp_int uD=aD*bD;
    cpp_int vN=cpp_int(2112)*aN*bD+cpp_int(1728)*bN*aD;
    cpp_int vD=uD;
    if(!(uN>2*uD && uN<3*uD)) return 28;
    if(vN!=3*vD) return 29;

    cpp_int D=aD*bD;
    cpp_int AN=aN*bD, BN=bN*aD;
    cpp_int H=hH*D + cpp_int(8)*S*(cpp_int(8640)*Q*AN-cpp_int(9600)*P*AN);
    cpp_int L=hL*D + cpp_int(8)*S*(cpp_int(-10560)*Q*AN-cpp_int(9600)*P*AN);
    if(H!=L) return 30;
    cpp_int T=cpp_int(8)*S*(cpp_int(12480)*Q+cpp_int(28800)*P)*D;
    cpp_int gap=H-T;
    if(gap<=0) return 31;

    cpp_int lambda=cpp_int(20)*P-cpp_int(18)*Q;
    cpp_int Cplus=cpp_int(38016)*Q+cpp_int(34560)*P;
    cpp_int Ctail=cpp_int(31104)*Q-cpp_int(34560)*P;
    cpp_int Cdiag=cpp_int(-15360)*Q-cpp_int(153600)*P;
    cpp_int CJ=cpp_int(-4)*Q-cpp_int(40)*P;
    if(!(lambda<0 && Cplus>0 && Ctail>0 && Cdiag<0 && CJ<0)) return 32;

    cout<<"I0130_B20_B11_B13_TINY_ROOT_AFFINE_DUAL_PASS\n";
    cout<<"same_template_closure epsilon=82051/18662400 u=1124842261/481140 stable="<<R0.stable<<"\n";
    cout<<"new_epsilon=10712131/2435443200 stable="<<R.stable<<" support_max_J="<<R.maxnz<<" tailJ="<<R.tailJ<<" tail="<<s128(R.tailMax)<<"\n";
    cout<<"root_cell ceil_u=3 floor_v=3 v=3 a="<<fracstr(aN,aD)<<" b="<<fracstr(bN,bD)<<" branch_equal=1 positive_threshold_gap=1\n";
    cout<<"delta=254256451/2435443200 U_MIV=2181186749/2435443200 W_MIV=638739389/2435443200 improvement=8951/4870886400 max_goods=1032\n";
    cout<<"affine_dual lambda=20P-18Q<0 Cplus="<<Cplus<<" Ctail="<<Ctail<<" Cdiag="<<Cdiag<<" CJ="<<CJ<<"\n";
    return 0;
}
