#include <algorithm>
#include <array>
#include <cmath>
#include <cstdlib>
#include <fstream>
#include <iostream>
#include <numeric>
#include <string>
#include <tuple>
#include <unordered_set>
#include <vector>
using namespace std;
static inline int psi12(int k){ k=abs(k); if(k==0) return 8; if(k==1) return 13; return 12*k; }
static void hungarian11(const double cost[11][11], int assign[11]){
 const int n=11; double u[12]={},v[12]={}; int p[12]={},way[12]={};
 for(int i=1;i<=n;i++){ p[0]=i; int j0=0; double minv[12]; bool used[12]={}; for(int j=1;j<=n;j++) minv[j]=1e100;
  do{ used[j0]=true; int i0=p[j0],j1=0; double delta=1e100; for(int j=1;j<=n;j++) if(!used[j]){ double cur=cost[i0-1][j-1]-u[i0]-v[j]; if(cur<minv[j]){minv[j]=cur;way[j]=j0;} if(minv[j]<delta){delta=minv[j];j1=j;} } for(int j=0;j<=n;j++) if(used[j]){u[p[j]]+=delta;v[j]-=delta;} else if(j) minv[j]-=delta; j0=j1; }while(p[j0]!=0);
  do{int j1=way[j0]; p[j0]=p[j1]; j0=j1;}while(j0);
 }
 for(int j=1;j<=n;j++) assign[p[j]-1]=j-1;
}
vector<vector<pair<int,int>>> factorization10(vector<int> vv){ vector<vector<pair<int,int>>> out; for(int r=0;r<9;r++){ vector<pair<int,int>> ps; ps.push_back({vv[9],vv[r]}); for(int i=1;i<5;i++) ps.push_back({vv[(r+i)%9],vv[(r-i+9)%9]}); out.push_back(ps);} return out; }
struct Slot{char typ;int z;};
using P17=array<unsigned char,17>;
P17 invp(const P17&p){P17 q;for(int i=0;i<17;i++)q[p[i]]=i;return q;}
P17 revc(const P17&p){P17 q;for(int i=0;i<17;i++)q[i]=16-p[16-i];return q;}
string enc(const P17&p){string s(17,'\0');for(int i=0;i<17;i++)s[i]=char(p[i]);return s;}
struct Mom { double ELQ,ELA,EHQ,EHA,EQ,EA,ETQ; };
Mom mom_for_k(int k){
 if(k==0) return {-0.4637335556401042,0.5362664443598958,-0.01614422587494608,0.9133083068521242,-0.23993889075752514,0.72478737560601,-0.043391122570186264};
 if(k==1) return {-0.3525954013352942,0.6474045986647058,0.0485745254506681,0.9067987813932494,-0.15201043794231306,0.7771016900289776,-0.007906759541635893};
 if(k==2) return {-0.2636508152045334,0.7363491847954666,0.11502473788754056,0.8740605288499306,-0.0743130386584964,0.8052048568226986,0.02713624663827023};
 return {-0.18572916089188046,0.8142708391081196,0.18572916089188046,0.8142708391081196,0.0,0.8142708391081196,0.0631259434523272};
}
static const long long DEN=1000000000000000LL;
struct Root {int d; long long lo,hi;};
static const Root roots[]={
 {187,13674794331177343LL,13674794331177344LL},{51,7141428428542849LL,7141428428542850LL},
 {34,5830951894845300LL,5830951894845301LL},{221,14866068747318505LL,14866068747318506LL},{170,13038404810405297LL,13038404810405298LL},
 {17,4123105625617660LL,4123105625617661LL},{255,15968719422671311LL,15968719422671312LL},{102,10099504938362077LL,10099504938362078LL}
};
const Root& rt(int d){for(auto &x:roots) if(x.d==d)return x; abort();}
void verify_roots(){ __int128 den2=(__int128)DEN*DEN; for(auto &x:roots){__int128 lo2=(__int128)x.lo*x.lo, hi2=(__int128)x.hi*x.hi, tar=(__int128)x.d*den2; if(!(lo2<=tar && tar<hi2)){cerr<<"ROOT BOUND FAIL "<<x.d<<"\n";exit(4);}} }
__int128 lb_num(int k,int A,int B,int C,int D,int E,int F){
 long long R=0; vector<pair<int,long long>> cs;
 if(k==0){ R=-12342LL*A-1122LL*B-6732LL*C+2312LL*E+1156LL*F+1025780LL; cs={{187,484LL*A-484LL*B+44LL*D-44LL*E},{51,1056LL*B+528LL*C-96LL*E-48LL*F-128640LL}}; }
 else if(k==1){ R=-12342LL*A+3366LL*B-4488LL*C+2312LL*E+1156LL*F+699380LL; cs={{34,-88LL*A-44LL*C-8LL*D-4LL*F-320LL},{221,572LL*A-572LL*B+52LL*D-52LL*E},{170,440LL*B+220LL*C-40LL*E-20LL*F-52000LL}}; }
 else if(k==2){ R=-12342LL*A+7854LL*B-2244LL*C+2312LL*E+1156LL*F+413780LL; cs={{17,-352LL*A-176LL*C-32LL*D-16LL*F-2560LL},{255,660LL*A-660LL*B+60LL*D-60LL*E},{34,704LL*B+352LL*C-64LL*E-32LL*F-80640LL}}; }
 else { R=374LL*A-374LL*B+1156LL*D+1156LL*E+1156LL*F+168980LL; cs={{102,-264LL*A+264LL*B-24LL*D-24LL*E-24LL*F-32160LL}}; }
 __int128 out=(__int128)R*DEN; for(auto [rad,c]:cs){auto &x=rt(rad);out+=(__int128)c*(c>=0?x.lo:x.hi);} return out;
}
int main(int argc,char**argv){
 if(argc<3){cerr<<"usage: prog k reps.csv\n";return 2;} int k=atoi(argv[1]); if(k<0||k>3)return 2; verify_roots(); Mom mm=mom_for_k(k);
 vector<array<Slot,11>> tils;
 if(k<=1) for(int v=0;v<11;v++){ vector<int> rv; for(int q=0;q<11;q++) if(q!=v) rv.push_back(q); auto ff=factorization10(rv); for(int lr=0;lr<9;lr++) for(int hr=0;hr<9;hr++){ array<Slot,11> sl; int c=0; for(auto [a,b]:ff[lr])sl[c++]={'L',a+b-10}; for(auto [a,b]:ff[hr])sl[c++]={'H',a+b-10}; sl[c++]={'V',2*v-10}; tils.push_back(sl); }}
 array<int,11> sig; iota(sig.begin(),sig.end(),0); long long total=0,unipass=0,unifail=0,fixedpass=0,adaptpass=0,remain=0; long long min_unipass=1e18,max_unifail=-1e18; vector<long long> uses(891,0); unordered_set<string> reps; const int N=17; const long long rhs=8LL*N*N*N*N;
 do{
  ++total; int gp[N]; iota(gp,gp+N,0); for(int i=0;i<11;i++)gp[k+i]=k+sig[i];
  long long half=0; for(int i=0;i<N;i++) for(int j=i+1;j<N;j++){int d=i-j,e=gp[i]-gp[j]; half+=(long long)abs(d-e)*psi12(d+e);} long long margin=10*half-rhs;
  if(margin>=0){++unipass;min_unipass=min(min_unipass,margin);continue;} ++unifail;max_unifail=max(max_unifail,margin);
  struct Br{int j,s,d;}; vector<Br> br; for(int j=0;j<11;j++)br.push_back({j,j+sig[j],j-sig[j]}); sort(br.begin(),br.end(),[](auto&x,auto&y){if(x.s!=y.s)return x.s<y.s;if(x.d!=y.d)return x.d<y.d;return x.j<y.j;}); vector<Br> low(br.begin(),br.begin()+5),high(br.begin()+6,br.end()); Br vert=br[5]; sort(low.begin(),low.end(),[](auto&x,auto&y){return x.d<y.d;}); sort(high.begin(),high.end(),[](auto&x,auto&y){return x.d<y.d;}); int nums[5]={-9,-5,0,5,9}; int CSL=0,CSH=0,ZL=0,ZH=0; for(int i=0;i<5;i++){CSL+=low[i].s;ZL+=low[i].d*nums[i];CSH+=high[i].s-2;ZH+=high[i].d*nums[i];} int sV=vert.s,ZV=0;
  if(lb_num(k,CSL,CSH,sV,ZL,ZH,ZV)>0){++fixedpass;continue;}
  bool ok=false; int s[11],d[11]; for(int j=0;j<11;j++){s[j]=j+sig[j];d[j]=j-sig[j];}
  if(k<=1){ for(int ti=0;ti<(int)tils.size()&&!ok;ti++){ double Cst[11][11]; auto&sl=tils[ti]; for(int j=0;j<11;j++)for(int c=0;c<11;c++){double z=sl[c].z/11.0,score; if(sl[c].typ=='L')score=s[j]*mm.ELQ+d[j]*z*mm.ELA; else if(sl[c].typ=='H')score=(s[j]-2)*mm.EHQ+d[j]*z*mm.EHA; else score=s[j]*mm.EQ+d[j]*z*mm.EA; Cst[j][c]=-score;} int asg[11];hungarian11(Cst,asg); CSL=CSH=sV=ZL=ZH=ZV=0; for(int j=0;j<11;j++){auto slot=sl[asg[j]]; if(slot.typ=='L'){CSL+=s[j];ZL+=d[j]*slot.z;} else if(slot.typ=='H'){CSH+=s[j]-2;ZH+=d[j]*slot.z;} else{sV=s[j];ZV=d[j]*slot.z;}} if(lb_num(k,CSL,CSH,sV,ZL,ZH,ZV)>0){ok=true;++adaptpass;++uses[ti];}} }
  if(ok)continue; ++remain; P17 p;for(int i=0;i<N;i++)p[i]=gp[i];P17 a=invp(p),b=revc(p),c=invp(b);P17 best=min(min(p,a),min(b,c));reps.insert(enc(best));
 }while(next_permutation(sig.begin(),sig.end()));
 ofstream f(argv[2]); for(auto&s0:reps){for(int i=0;i<N;i++){if(i)f<<",";f<<(int)(unsigned char)s0[i];}f<<"\n";}
 cout<<"k="<<k<<" total="<<total<<"\n"; cout<<"universal_pass="<<unipass<<" universal_fail="<<unifail<<" min_pass="<<min_unipass<<" max_fail="<<max_unifail<<"\n"; cout<<"fixed_exact_pass="<<fixedpass<<"\n"; cout<<"adaptive_exact_pass="<<adaptpass<<" nonzero_tilings="<<count_if(uses.begin(),uses.end(),[](long long x){return x>0;})<<"\n"; cout<<"remain="<<remain<<" canonical_reps="<<reps.size()<<"\n";
 bool chk=false;
 if(k==0) chk=(total==39916800LL&&unipass==19376735LL&&unifail==20540065LL&&min_unipass==2&&max_unifail==-8&&fixedpass==20454983LL&&adaptpass==82413LL&&remain==2669LL&&reps.size()==1681);
 if(k==1) chk=(total==39916800LL&&unipass==11216695LL&&unifail==28700105LL&&min_unipass==2&&max_unifail==-8&&fixedpass==28683934LL&&adaptpass==15615LL&&remain==556LL&&reps.size()==362);
 if(k==2) chk=(total==39916800LL&&unipass==5989097LL&&unifail==33927703LL&&min_unipass==2&&max_unifail==-8&&fixedpass==33920087LL&&adaptpass==0LL&&remain==7616LL&&reps.size()==5383);
 if(k==3) chk=(total==39916800LL&&unipass==4349090LL&&unifail==35567710LL&&min_unipass==2&&max_unifail==-8&&fixedpass==35561443LL&&adaptpass==0LL&&remain==6267LL&&reps.size()==2238);
 if(!chk){cerr<<"ASSERTION FAILURE\n";return 3;} cout<<"S11 N17 EXACT PHASE1 PASSED\n";
}
