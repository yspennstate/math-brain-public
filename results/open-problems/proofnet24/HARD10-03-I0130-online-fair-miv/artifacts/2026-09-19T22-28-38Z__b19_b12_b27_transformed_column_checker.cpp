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
static long long gcdll(long long a,long long b){return b?gcdll(b,a%b):a;} static long long lcmll(long long a,long long b){return a/gcdll(a,b)*b;}
struct Act{bool base;int p;long long A,B,D,mul;int dhceil,cfloor,cceil;i128 rh,rl;}; struct Res{vector<i128>h;int stable,maxnz,maxC;long long S;i128 tailMax;int tailJ;};
static vector<RatAct> Gextra={{7193,11628,11628},{871,3840,3840},{2591,3840,3840},{6858927,11100227,11162880},{13,704,704},{47,88,88},{377,1056,1056},{39,176,176},{641,1056,1056},{179,1056,1056},{3,88,88},{105,176,176},{61,176,176},{721,2112,2112},{17,176,176},{189,704,704},{509,1056,1056},{43,132,132},{311,1056,1056},{413,2112,2112},{35,704,704},{255,704,704},{289,1056,1056},{71,432,432},{193,2112,2112},{45,352,352},{215,2112,2112},{25,864,864},{145,704,704},{133,864,864},{25,1056,1056},{239,1728,1728},{185,1728,1728},{527,1728,1728},{23,352,352},{57,704,704},{139,528,528},{281,2112,2112},{245,1056,1056},{91,1056,1056},{815,1728,1728},{95,1728,1728},{5,66,66}};
static Res fixed(long long P,long long Q){ long long S=1; for(auto z:Gextra)S=lcmll(S,z.D); auto fi=integer_table(P,Q); vector<Orbit>os(5);
#pragma omp parallel for schedule(static)
 for(int r=1;r<=4;r++)os[r]=orbit_table(P,Q,8,r); auto F0=[&](int J)->i128{if(J<0)J=-J;int k=J/8,r=J%8;if(k>=2600)return 0;if(r==0)return(i128)fi[k]*8*S;if(r<=4)return(i128)os[r].r[k]*S;return(i128)os[8-r].s[k]*S;}; vector<Act>acts; for(int p=0;p<=192;p++){int dh=9*p+2112,c=11*p+1728;acts.push_back({true,p,p,192,192,S/192,dh,c,c,(i128)8*(45LL*p*Q-9600LL*P)*S,(i128)8*(-55LL*p*Q-9600LL*P)*S});} for(auto z:Gextra){long long mul=S/z.D,m=max(z.A,z.B);long long hn=1728*z.A+2112*z.B,cn=2112*z.A+1728*z.B;int dh=(hn+z.D-1)/z.D,cf=cn/z.D,cc=(cn+z.D-1)/z.D;acts.push_back({false,-1,z.A,z.B,z.D,mul,dh,cf,cc,(i128)8*((i128)8640*Q*z.A-(i128)9600*P*m)*mul,(i128)8*((i128)-10560*Q*z.A-(i128)9600*P*m)*mul});} int maxC=0;for(auto&a:acts)maxC=max(maxC,a.cceil);int M=26000; auto bell=[&](int J,const vector<i128>&v)->i128{i128 best=-((i128)1<<120);for(auto&a:acts){int jh=J+a.dhceil;i128 hi=a.rh+(jh<(int)v.size()?v[jh]:0),lo;if(a.base){int c=a.cfloor;if(J>=c)lo=a.rl+v[J-c];else{int jl=c-J;i128 rr=(i128)8*(8640LL*Q-9600LL*P)*S-(i128)40*Q*J*S;lo=rr+(jl<(int)v.size()?v[jl]:0);}}else{i128 cn=(i128)2112*a.A+1728*a.B;if((i128)J*a.D>=cn){int jl=J-a.cfloor;lo=a.rl+(jl<(int)v.size()?v[jl]:0);}else{int jl=a.cceil-J;i128 rr=(i128)8*((i128)8640*Q*a.B-(i128)9600*P*max(a.A,a.B))*a.mul-(i128)40*Q*J*S;lo=rr+(jl<(int)v.size()?v[jl]:0);}}best=max(best,min(hi,lo));}return best;}; vector<i128>prev(M+1),cur(M+1);for(int J=0;J<=M;J++)prev[J]=F0(J);int stable=-1;for(int d=1;d<=1200;d++){int diff=0;
#pragma omp parallel for schedule(static) reduction(|:diff)
 for(int J=0;J<=M;J++){i128 z=max(F0(J),bell(J,prev));cur[J]=z;if(z!=prev[J])diff=1;}prev.swap(cur);if(!diff){stable=d;break;}} int maxnz=-1;for(int J=0;J<=M;J++)if(prev[J]>0)maxnz=J;i128 tail=-((i128)1<<120);int tailJ=-1;for(int J=maxnz+1;J<=maxnz+maxC&&J<=M;J++){i128 z=bell(J,prev);if(z>tail){tail=z;tailJ=J;}} return{move(prev),stable,maxnz,maxC,S,tail,tailJ}; }

int main(){
    const long long Q=62500000000LL;
    const long long IA=43530775821LL, IB=208953177301LL, ID=7426362113280LL;
    Gextra.push_back({IA,IB,ID});

    const long long P0=274359209LL;
    auto R0=fixed(P0,Q);
    if(R0.S!=2398714962589440LL || R0.stable!=696 || R0.maxnz!=20550 || R0.tailJ!=20551) return 10;
    if(s128(R0.tailMax)!="-527282019615100007743488000") return 11;

    // B19(reuse): exact violated source-root wall column a=435/704,b=1.
    const long long A=435,B=704,D=704; const int J0=3840;
    i128 un0=(i128)1728*A+(i128)2112*B, vn0=(i128)2112*A+(i128)1728*B;
    if(un0*11!=(i128)34977*D || vn0!=(i128)3033*D) return 12;
    if((i128)11*vn0-(i128)9*un0!=(i128)7680*A) return 13;
    if((i128)11*un0-(i128)9*vn0!=(i128)7680*B) return 14;
    i128 H0=(i128)D*R0.h[7020] + (i128)8*R0.S*((i128)8640*Q*A-(i128)9600*P0*B);
    i128 L0=(i128)D*R0.h[807] + (i128)8*R0.S*((i128)-10560*Q*A-(i128)9600*P0*B);
    i128 G0=min(H0,L0)-(i128)D*R0.h[J0];
    if(s128(H0)!="10649114214811954129598637146112000") return 15;
    if(s128(L0)!="10648431236664918497531686551552000") return 16;
    if(s128(G0)!="4225933649613930573588288307200") return 17;
    if(G0<=0) return 18;

    // Insert only that exact violated column; no denominator grid.
    Gextra.push_back({A,B,D});
    const long long P1=274787000LL;
    auto R1=fixed(P1,Q);
    i128 T=(i128)8*((i128)12480*Q+(i128)28800*P1)*R1.S;
    i128 rootgap=R1.h[3840]-T;
    if(R1.S!=2398714962589440LL || R1.stable!=531 || R1.maxnz!=20548 || R1.tailJ!=20549) return 19;
    if(s128(R1.tailMax)!="-1833323327624224309248000000") return 20;
    if(s128(rootgap)!="1381233380235945984000000") return 21;
    if(rootgap<=0 || R1.tailMax>=0) return 22;

    // B12/B27 structural-coordinate invariant and next exact violated template.
    // u=1728a+2112b, v=2112a+1728b; inverse is
    // a=(11v-9u)/7680, b=(11u-9v)/7680.
    const long long A2=228175945101LL,B2=1292743289321LL,D2=1336500000000LL; const int J2=11158;
    i128 un2=(i128)1728*A2+(i128)2112*B2, vn2=(i128)2112*A2+(i128)1728*B2;
    if((i128)11*vn2-(i128)9*un2!=(i128)7680*A2) return 23;
    if((i128)11*un2-(i128)9*vn2!=(i128)7680*B2) return 24;
    if(vn2!=(i128)2032*D2) return 25;
    int dh2=(int)((un2+D2-1)/D2), cf2=(int)(vn2/D2);
    if(dh2!=2338 || cf2!=2032) return 26;
    cpp_int HH=cpp_int(s128(R1.h[J2+dh2]))*D2 + cpp_int(8)*R1.S*(cpp_int(8640)*Q*A2-cpp_int(9600)*P1*B2);
    cpp_int LL=cpp_int(s128(R1.h[J2-cf2]))*D2 + cpp_int(8)*R1.S*(cpp_int(-10560)*Q*A2-cpp_int(9600)*P1*B2);
    cpp_int GG=HH-cpp_int(s128(R1.h[J2]))*D2;
    const cpp_int EXPECT_EQ("4680287081995498772071090900213334016000000");
    const cpp_int EXPECT_GAIN("23601014910622346793132705013334016000000");
    if(HH!=LL || HH!=EXPECT_EQ || GG!=EXPECT_GAIN || GG<=0) return 27;

    // Raw finite transformed-cell template bound per integer state and orientation.
    const long long raw_cells=2LL*3841LL*3841LL;
    if(raw_cells!=29506562LL) return 28;

    cout<<"I0130_B19_B12_B27_TRANSFORMED_COLUMN_PASS\n";
    cout<<"previous_epsilon=274359209/62500000000 previous_stable="<<R0.stable<<" previous_support="<<R0.maxnz<<"\n";
    cout<<"root_separator=(435/704,1) u=34977/11 v=3033 high_index=7020 low_index=807 H="<<s128(H0)<<" L="<<s128(L0)<<" gain_num_over_704="<<s128(G0)<<"/704\n";
    cout<<"new_epsilon=274787/62500000 stable="<<R1.stable<<" support_max_J="<<R1.maxnz<<" tailJ="<<R1.tailJ<<" tailMax="<<s128(R1.tailMax)<<" rootgap="<<s128(rootgap)<<"\n";
    cout<<"delta=6524787/62500000 U_MIV=55975213/62500000 W_MIV=49175639/187500000 improvement=427791/62500000000 max_goods=1146\n";
    cout<<"transform_inverse=a=(11v-9u)/7680,b=(11u-9v)/7680 raw_state_orientation_templates="<<raw_cells<<"\n";
    cout<<"next_separator_J=11158 a=25352882789/148500000000 b=117522117211/121500000000 common=(228175945101,1292743289321)/1336500000000 u=813687984422/348046875 v=2032 high_index=13496 low_index=9126 branch_equal="<<HH<<" gain_num_over_D="<<GG<<"/1336500000000\n";
    return 0;
}
