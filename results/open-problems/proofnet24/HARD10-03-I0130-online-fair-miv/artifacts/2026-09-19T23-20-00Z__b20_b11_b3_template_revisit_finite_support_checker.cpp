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
static long long gcdll(long long a,long long b){return b?gcdll(b,a%b):a;}
static i128 gcd128(i128 a,i128 b){ if(a<0)a=-a; if(b<0)b=-b; while(b){i128 r=a%b;a=b;b=r;} return a; }
struct Act{bool base;int p;long long A,B,D; i128 mul;int dhceil,cfloor,cceil;i128 rh,rl;}; struct Res{vector<i128>h;int stable,maxnz,maxC;i128 S,tailMax;int tailJ;};
static vector<RatAct> Gextra={{7193,11628,11628},{871,3840,3840},{2591,3840,3840},{6858927,11100227,11162880},{13,704,704},{47,88,88},{377,1056,1056},{39,176,176},{641,1056,1056},{179,1056,1056},{3,88,88},{105,176,176},{61,176,176},{721,2112,2112},{17,176,176},{189,704,704},{509,1056,1056},{43,132,132},{311,1056,1056},{413,2112,2112},{35,704,704},{255,704,704},{289,1056,1056},{71,432,432},{193,2112,2112},{45,352,352},{215,2112,2112},{25,864,864},{145,704,704},{133,864,864},{25,1056,1056},{239,1728,1728},{185,1728,1728},{527,1728,1728},{23,352,352},{57,704,704},{139,528,528},{281,2112,2112},{245,1056,1056},{91,1056,1056},{815,1728,1728},{95,1728,1728},{5,66,66}};
static Res fixed(long long P,long long Q){ i128 S=1; for(auto z:Gextra){i128 g=gcd128(S,(i128)z.D);S=(S/g)*z.D;} auto fi=integer_table(P,Q); vector<Orbit>os(5);
#pragma omp parallel for schedule(static)
 for(int r=1;r<=4;r++)os[r]=orbit_table(P,Q,8,r); auto F0=[&](int J)->i128{if(J<0)J=-J;int k=J/8,r=J%8;if(k>=2600)return 0;if(r==0)return(i128)fi[k]*8*S;if(r<=4)return(i128)os[r].r[k]*S;return(i128)os[8-r].s[k]*S;}; vector<Act>acts; for(int p=0;p<=192;p++){int dh=9*p+2112,c=11*p+1728;acts.push_back({true,p,p,192,192,S/192,dh,c,c,(i128)8*(45LL*p*Q-9600LL*P)*S,(i128)8*(-55LL*p*Q-9600LL*P)*S});} for(auto z:Gextra){i128 mul=S/z.D,m=max(z.A,z.B);long long hn=1728*z.A+2112*z.B,cn=2112*z.A+1728*z.B;int dh=(hn+z.D-1)/z.D,cf=cn/z.D,cc=(cn+z.D-1)/z.D;acts.push_back({false,-1,z.A,z.B,z.D,mul,dh,cf,cc,(i128)8*((i128)8640*Q*z.A-(i128)9600*P*m)*mul,(i128)8*((i128)-10560*Q*z.A-(i128)9600*P*m)*mul});} int maxC=0;for(auto&a:acts)maxC=max(maxC,a.cceil);int M=25000; auto bell=[&](int J,const vector<i128>&v)->i128{i128 best=-((i128)1<<120);for(auto&a:acts){int jh=J+a.dhceil;i128 hi=a.rh+(jh<(int)v.size()?v[jh]:0),lo;if(a.base){int c=a.cfloor;if(J>=c)lo=a.rl+v[J-c];else{int jl=c-J;i128 rr=(i128)8*(8640LL*Q-9600LL*P)*S-(i128)40*Q*J*S;lo=rr+(jl<(int)v.size()?v[jl]:0);}}else{i128 cn=(i128)2112*a.A+1728*a.B;if((i128)J*a.D>=cn){int jl=J-a.cfloor;lo=a.rl+(jl<(int)v.size()?v[jl]:0);}else{int jl=a.cceil-J;i128 rr=(i128)8*((i128)8640*Q*a.B-(i128)9600*P*max(a.A,a.B))*a.mul-(i128)40*Q*J*S;lo=rr+(jl<(int)v.size()?v[jl]:0);}}best=max(best,min(hi,lo));}return best;}; vector<i128>prev(M+1),cur(M+1);for(int J=0;J<=M;J++)prev[J]=F0(J);int stable=-1;for(int d=1;d<=1200;d++){int diff=0;
#pragma omp parallel for schedule(static) reduction(|:diff)
 for(int J=0;J<=M;J++){i128 z=max(F0(J),bell(J,prev));cur[J]=z;if(z!=prev[J])diff=1;}prev.swap(cur);if(!diff){stable=d;break;}} int maxnz=-1;for(int J=0;J<=M;J++)if(prev[J]>0)maxnz=J;i128 tail=-((i128)1<<120);int tailJ=-1;for(int J=maxnz+1;J<=maxnz+maxC&&J<=M;J++){i128 z=bell(J,prev);if(z>tail){tail=z;tailJ=J;}} return{move(prev),stable,maxnz,maxC,S,tail,tailJ}; }

static pair<long long,int> base_stats(long long P,long long Q){
 auto fi=integer_table(P,Q); vector<Orbit>os(5);
 #pragma omp parallel for schedule(static)
 for(int r=1;r<=4;r++)os[r]=orbit_table(P,Q,8,r);
 long long mx=0; int sup=-1;
 for(int J=0;J<20800;J++){int k=J/8,r=J%8; long long z;if(r==0)z=fi[k]*8;else if(r<=4)z=os[r].r[k];else z=os[8-r].s[k]; if(z>mx)mx=z; if(z>0)sup=J;}
 return {mx,sup};
}

static void print_res(const char*tag,long long P,long long Q,const Res&R){i128 T=(i128)8*((i128)12480*Q+(i128)28800*P)*R.S; cout<<tag<<" P/Q="<<P<<"/"<<Q<<" S="<<s128(R.S)<<" stable="<<R.stable<<" maxnz="<<R.maxnz<<" tailJ="<<R.tailJ<<" tail="<<s128(R.tailMax)<<" rootgap="<<s128(R.h[3840]-T)<<" h11158="<<s128(R.h[11158])<<"\n";}

int main(){
    const long long P=82051LL, Q=18662400LL;
    Gextra.push_back({43530775821LL,208953177301LL,7426362113280LL});
    Gextra.push_back({435,704,704});
    Gextra.push_back({228175945101LL,1292743289321LL,1336500000000LL});

    auto R=fixed(P,Q);
    i128 T=(i128)8*((i128)12480*Q+(i128)28800*P)*R.S;
    i128 rootgap=R.h[3840]-T;
    if(s128(R.S)!="936998032261500000000") return 10;
    if(R.stable!=525 || R.maxnz!=20548 || R.tailJ!=20549) return 11;
    if(s128(R.tailMax)!="-214098394310903462400000000000") return 12;
    if(rootgap!=0) return 13;

    auto BS=base_stats(P,Q);
    const long long BASE_MAX=3018119553120LL, BASE_SUPPORT=18450LL;
    if(BS.first!=BASE_MAX || BS.second!=BASE_SUPPORT) return 14;
    const long long LOW_SLACK=20LL*P;
    const long long NBOUND=BASE_MAX/LOW_SLACK;
    const long long JBOUND=BASE_SUPPORT+3840LL*NBOUND;
    if(LOW_SLACK!=1641020LL || NBOUND!=1839172LL || JBOUND!=7062438930LL) return 15;

    const int J=11158, jh=13496, jl=9126;
    cpp_int dh = cpp_int(s128(R.h[jh]))-cpp_int(s128(R.h[jl]));
    cpp_int numA = -dh*7680;
    cpp_int denA = cpp_int(8)*cpp_int(s128(R.S))*19200*Q;
    cpp_int un = cpp_int(11)*2032*denA-numA;
    cpp_int ud = 9*denA;
    auto gcdbig=[](cpp_int a,cpp_int b){if(a<0)a=-a;if(b<0)b=-b;while(b!=0){cpp_int r=a%b;a=b;b=r;}return a;};
    cpp_int gu=gcdbig(un,ud); un/=gu; ud/=gu;
    if(un!=cpp_int("1124842261") || ud!=cpp_int("481140")) return 16;
    if(!(un>cpp_int(2337)*ud && un<=cpp_int(2338)*ud && un>=cpp_int(2032)*ud)) return 17;

    cpp_int D=7680*ud;
    cpp_int A=cpp_int(11)*2032*ud-9*un;
    cpp_int B=11*un-cpp_int(9)*2032*ud;
    cpp_int ga=gcdbig(A,D), gb=gcdbig(B,D);
    if(A/ga!=cpp_int("70095659") || D/ga!=cpp_int("410572800")) return 18;
    if(B/gb!=cpp_int("324925141") || D/gb!=cpp_int("335923200")) return 19;

    cpp_int H=cpp_int(s128(R.h[jh]))*D + cpp_int(8)*cpp_int(s128(R.S))*(cpp_int(8640)*Q*A-cpp_int(9600)*P*B);
    cpp_int L=cpp_int(s128(R.h[jl]))*D + cpp_int(8)*cpp_int(s128(R.S))*(cpp_int(-10560)*Q*A-cpp_int(9600)*P*B);
    cpp_int G=H-cpp_int(s128(R.h[J]))*D;
    if(H!=L) return 20;
    const cpp_int EXPECT_GAIN("94821089185756558987234528296960000");
    if(G!=EXPECT_GAIN || G<=0) return 21;

    cpp_int dH = -cpp_int(9)*8640*Q-cpp_int(11)*9600*P;
    cpp_int dL =  cpp_int(9)*10560*Q-cpp_int(11)*9600*P;
    if(!(dH<0 && dL>0)) return 22;

    cout<<"I0130_B20_B11_B3_TEMPLATE_REVISIT_FINITE_SUPPORT_PASS\n";
    cout<<"epsilon=82051/18662400 stable="<<R.stable
        <<" support_max_J="<<R.maxnz<<" tailJ="<<R.tailJ
        <<" tailMax="<<s128(R.tailMax)<<" rootgap="<<s128(rootgap)<<"\n";
    cout<<"delta=1948291/18662400 U_MIV=16714109/18662400 W_MIV=4894589/18662400 improvement=3239/1458000000000 max_goods=1140\n";
    cout<<"full_continuum_support_theorem base_max="<<BASE_MAX
        <<" base_support="<<BASE_SUPPORT<<" low_slack="<<LOW_SLACK
        <<" active_steps_bound="<<NBOUND<<" J_support_bound="<<JBOUND<<"\n";
    cout<<"same_template_revisit J=11158 v=2032 u=1124842261/481140 ceil_u=2338"
        <<" a=70095659/410572800 b=324925141/335923200"
        <<" equal_branches=1 gain_num_over_D="<<G<<"/"<<D
        <<" dHdu_sign=negative dLdu_sign=positive\n";
    return 0;
}
