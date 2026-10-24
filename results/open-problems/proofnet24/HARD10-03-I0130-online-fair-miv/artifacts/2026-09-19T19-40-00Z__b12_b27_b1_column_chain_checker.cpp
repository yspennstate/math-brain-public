#include <bits/stdc++.h>
#include <omp.h>
using namespace std; using i128=__int128_t;
static i128 parse128(const string&s){i128 x=0;for(char c:s)if(c>='0'&&c<='9')x=x*10+(c-'0');return x;}
static string s128(i128 x){if(x==0)return"0";bool neg=x<0;if(neg)x=-x;string s;while(x){s.push_back('0'+x%10);x/=10;}if(neg)s.push_back('-');reverse(s.begin(),s.end());return s;}
struct BaseAct{int x,y,dh,c,m; long long hb,lb,rb;}; struct Orbit{vector<long long>r,s;}; struct RatAct{long long A,B,D;};
static vector<pair<int,int>> old654_points(){vector<pair<int,int>>ps;for(int i=0;i<=24;i++)for(int j=0;j<=24;j++)ps.push_back({40*i,40*j});const int ex[][2]={{6,236},{13,233},{67,237},{26,236},{94,234},{84,234},{3,223},{3,233},{74,234},{114,234},{4,234},{176,236},{115,235}};for(auto&p:ex)ps.push_back({4*p[0],4*p[1]});const int cut[][2]={{179,959},{613,953},{649,949},{539,959},{775,955},{885,945},{561,941},{419,959},{586,946},{215,955},{579,959},{70,910},{527,947},{497,957},{900,940},{291,951}};for(auto&p:cut)ps.push_back({p[0],p[1]});return ps;}
static Orbit orbit_table(long long P,long long Q,int R,int r,int M=2600,int H=612){vector<BaseAct>as;for(auto[x,y]:old654_points()){int dh=(9*x+11*y)/40,c=(11*x+9*y)/40,m=max(x,y);as.push_back({x,y,dh,c,m,(9LL*x*Q-10LL*P*m)*R,(-11LL*x*Q-10LL*P*m)*R,(9LL*y*Q-10LL*P*m)*R});}int sr=R-r;vector<long long>pr(M+1),ps(M+1),cr(M+1),cs(M+1);for(int h=1;h<=H;h++){int diff=0;
#pragma omp parallel for schedule(static) reduction(|:diff)
for(int k=0;k<=M;k++){long long br=0,bs=0;for(auto&a:as){int kh=k+a.dh;long long HR=a.hb+(kh<=M?pr[kh]:0),HS=a.hb+(kh<=M?ps[kh]:0),LR,LS;if(k>=a.c){LR=a.lb+pr[k-a.c];LS=a.lb+ps[k-a.c];}else{int kl=a.c-k-1;long long xr=1LL*k*R+r,xs=1LL*k*R+sr;LR=a.rb-40LL*xr*Q+ps[kl];LS=a.rb-40LL*xs*Q+pr[kl];}br=max(br,min(HR,LR));bs=max(bs,min(HS,LS));}cr[k]=br;cs[k]=bs;if(cr[k]!=pr[k]||cs[k]!=ps[k])diff=1;}if(!diff)break;pr.swap(cr);ps.swap(cs);}return{move(pr),move(ps)};}
static vector<long long> integer_table(long long P,long long Q,int M=2600,int H=612){vector<BaseAct>as;for(auto[x,y]:old654_points()){int dh=(9*x+11*y)/40,c=(11*x+9*y)/40,m=max(x,y);as.push_back({x,y,dh,c,m,9LL*x*Q-10LL*P*m,-11LL*x*Q-10LL*P*m,9LL*y*Q-10LL*P*m});}vector<long long>pr(M+1),cr(M+1);for(int h=1;h<=H;h++){int diff=0;
#pragma omp parallel for schedule(static) reduction(|:diff)
for(int k=0;k<=M;k++){long long best=0;for(auto&a:as){long long hi=a.hb+((k+a.dh<=M)?pr[k+a.dh]:0),lo;if(k>=a.c)lo=a.lb+pr[k-a.c];else lo=a.rb-40LL*k*Q+pr[a.c-k];best=max(best,min(hi,lo));}cr[k]=best;if(cr[k]!=pr[k])diff=1;}if(!diff)break;pr.swap(cr);}return pr;}
static long long gcdll(long long a,long long b){return b?gcdll(b,a%b):a;} static long long lcmll(long long a,long long b){return a/gcdll(a,b)*b;} static long long ceil_rat(long long n,long long d){return n>=0?(n+d-1)/d:n/d;}
struct Act{bool base;int p;long long A,B,D,mul;int dhceil,cfloor,cceil;i128 rh,rl;}; struct Res{vector<i128>h;int stable,maxnz,maxC;long long S;i128 tailMax;int tailJ;};
static vector<RatAct> Gextra={{7193,11628,11628},{871,3840,3840},{2591,3840,3840},{6858927,11100227,11162880},{13,704,704},{47,88,88},{377,1056,1056},{39,176,176},{641,1056,1056},{179,1056,1056},{3,88,88}};
static Res fixed(long long P,long long Q){auto &extra=Gextra;long long S=1;for(auto z:extra)S=lcmll(S,z.D);auto fi=integer_table(P,Q);vector<Orbit>os(5);
#pragma omp parallel for schedule(static)
for(int r=1;r<=4;r++)os[r]=orbit_table(P,Q,8,r);auto F0=[&](int J)->i128{if(J<0)J=-J;int k=J/8,r=J%8;if(k>=2600)return 0;if(r==0)return(i128)fi[k]*8*S;if(r<=4)return(i128)os[r].r[k]*S;return(i128)os[8-r].s[k]*S;};vector<Act>acts;for(int p=0;p<=192;p++){int dh=9*p+2112,c=11*p+1728;acts.push_back({true,p,p,192,192,S/192,dh,c,c,(i128)8*(45LL*p*Q-9600LL*P)*S,(i128)8*(-55LL*p*Q-9600LL*P)*S});}for(auto z:extra){long long mul=S/z.D,m=max(z.A,z.B);long long hn=1728*z.A+2112*z.B,cn=2112*z.A+1728*z.B;int dh=(hn+z.D-1)/z.D,cf=cn/z.D,cc=(cn+z.D-1)/z.D;acts.push_back({false,-1,z.A,z.B,z.D,mul,dh,cf,cc,(i128)8*(8640LL*Q*z.A-9600LL*P*m)*mul,(i128)8*(-10560LL*Q*z.A-9600LL*P*m)*mul});}int maxC=0;for(auto&a:acts)maxC=max(maxC,a.cceil);int M=26000;auto bell=[&](int J,const vector<i128>&v)->i128{i128 best=-((i128)1<<120);for(auto&a:acts){int jh=J+a.dhceil;i128 hi=a.rh+(jh<(int)v.size()?v[jh]:0),lo;if(a.base){int c=a.cfloor;if(J>=c)lo=a.rl+v[J-c];else{int jl=c-J;i128 rr=(i128)8*(8640LL*Q-9600LL*P)*S-(i128)40*Q*J*S;lo=rr+(jl<(int)v.size()?v[jl]:0);}}else{i128 cn=(i128)2112*a.A+1728*a.B;if((i128)J*a.D>=cn){int jl=J-a.cfloor;lo=a.rl+(jl<(int)v.size()?v[jl]:0);}else{int jl=a.cceil-J;i128 rr=(i128)8*(8640LL*Q*a.B-9600LL*P*max(a.A,a.B))*a.mul-(i128)40*Q*J*S;lo=rr+(jl<(int)v.size()?v[jl]:0);}}best=max(best,min(hi,lo));}return best;};vector<i128>prev(M+1),cur(M+1);for(int J=0;J<=M;J++)prev[J]=F0(J);int stable=-1;for(int d=1;d<=700;d++){int diff=0;
#pragma omp parallel for schedule(static) reduction(|:diff)
for(int J=0;J<=M;J++){i128 z=max(F0(J),bell(J,prev));cur[J]=z;if(z!=prev[J])diff=1;}prev.swap(cur);if(!diff){stable=d;break;}}int maxnz=-1;for(int J=0;J<=M;J++)if(prev[J]>0)maxnz=J;i128 tail=-((i128)1<<120);int tailJ=-1;for(int J=maxnz+1;J<=maxnz+maxC&&J<=M;J++){i128 z=bell(J,prev);if(z>tail){tail=z;tailJ=J;}}return{move(prev),stable,maxnz,maxC,S,tail,tailJ};}
struct Sep{i128 gain;long long A,B;int J;};
static Sep b1(long long P,long long Q,const vector<i128>&h,long long S,int maxJ){vector<pair<long long,long long>>bp={{0,1},{1,1}};for(int k=1;k<1728;k++){long long g=gcdll(k,1728);bp.push_back({k/g,1728/g});}for(int k=1;k<2112;k++){long long g=gcdll(k,2112);bp.push_back({k/g,2112/g});}sort(bp.begin(),bp.end(),[](auto x,auto y){return(i128)x.first*y.second<(i128)y.first*x.second;});bp.erase(unique(bp.begin(),bp.end(),[](auto x,auto y){return(i128)x.first*y.second==(i128)y.first*x.second;}),bp.end());Sep G{-((i128)1<<120),0,1,-1};
#pragma omp parallel
{Sep L{-((i128)1<<120),0,1,-1};auto cons=[&](int J,long long A,long long B){if(A<0||A>B)return;long long hn=J*B+1728*A+2112*B,ln=J*B-2112*A-1728*B;int jh=ceil_rat(hn,B),jl=ceil_rat(llabs(ln),B);i128 H=(i128)B*(jh<(int)h.size()?h[jh]:0)+(i128)8*S*(8640LL*Q*A-9600LL*P*B);i128 LL;if(ln>=0)LL=(i128)B*(jl<(int)h.size()?h[jl]:0)+(i128)8*S*(-10560LL*Q*A-9600LL*P*B);else LL=(i128)B*(jl<(int)h.size()?h[jl]:0)+(i128)8*S*(8640LL*Q*B-9600LL*P*B)-(i128)40*Q*J*S*B;i128 g=min(H,LL)-(i128)B*h[J];{i128 lhs=g*L.B,rhs=L.gain*B; bool take=lhs>rhs; if(lhs==rhs){ if(L.J<0||J<L.J) take=true; else if(J==L.J && (i128)A*L.B<(i128)L.A*B) take=true;} if(take)L={g,A,B,J};}};
#pragma omp for schedule(dynamic,16)
for(int J=0;J<=maxJ;J++){for(auto[A,B]:bp)cons(J,A,B);for(size_t i=0;i+1<bp.size();i++){auto[A1,B1]=bp[i];auto[A2,B2]=bp[i+1];long long Am=A1*B2+A2*B1,Bm=2*B1*B2;long long hn=J*Bm+1728*Am+2112*Bm,ln=J*Bm-2112*Am-1728*Bm;int jh=ceil_rat(hn,Bm),jl=ceil_rat(llabs(ln),Bm);i128 HH=(jh<(int)h.size()?h[jh]:0),LL=(jl<(int)h.size()?h[jl]:0);i128 n,d;if(ln>=0){n=LL-HH;d=(i128)8*S*19200LL*Q;}else{n=LL-HH+(i128)8*S*8640LL*Q-(i128)40*Q*J*S;d=(i128)8*S*8640LL*Q;}if(n<0||n>d||n>LLONG_MAX||d>LLONG_MAX)continue;long long nn=(long long)n,dd=(long long)d,g=gcdll(nn,dd);nn/=g;dd/=g;if((i128)nn*B1<=(i128)A1*dd||(i128)nn*B2>=(i128)A2*dd)continue;cons(J,nn,dd);}}
#pragma omp critical
{i128 lhs=L.gain*G.B,rhs=G.gain*L.B; bool take=lhs>rhs; if(lhs==rhs){ if(G.J<0||L.J<G.J)take=true; else if(L.J==G.J && (i128)L.A*G.B<(i128)G.A*L.B)take=true;} if(take)G=L;}}
return G;}
int main(){
 long long P=55560,Q=13023360; const i128 plateau=parse128("314016922533888000");
 cout<<"I0130_B12_B27_B1_COLUMN_CHAIN_START\n";
 for(int it=0;it<5;it++){
   auto R=fixed(P,Q); i128 T=(i128)8*(12480LL*Q+28800LL*P)*R.S;
   auto E=b1(P,Q,R.h,R.S,R.maxnz+R.maxC);
   if(E.gain<=0 || E.gain!=(i128)E.B*plateau) return 30+it;
   cout<<"iter="<<it<<" cols="<<Gextra.size()<<" stable="<<R.stable<<" support_max_J="<<R.maxnz<<" rootgap="<<s128(R.h[3840]-T)<<" separator_J="<<E.J<<" a="<<E.A<<"/"<<E.B<<" normalized_gain="<<s128(E.gain/E.B)<<"\n";
   bool dup=false;for(auto z:Gextra)if(z.B==z.D && (i128)z.A*E.B==(i128)E.A*z.D){dup=true;break;} if(dup)return 40+it;
   Gextra.push_back({E.A,E.B,E.B});
 }
 cout<<"I0130_B12_B27_B1_COLUMN_CHAIN_PASS\n";
 cout<<"plateau_normalized_gain=314016922533888000\n";
 cout<<"interpretation=exact five-step positive-separator chain refutes closure of each successive finite candidate set; it does not refute existence of a larger finite universal column set.\n";
 return 0;
}
