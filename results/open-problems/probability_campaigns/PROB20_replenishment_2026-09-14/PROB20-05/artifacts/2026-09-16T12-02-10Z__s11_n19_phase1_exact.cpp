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
using P19=array<unsigned char,19>;
P19 invp(const P19&p){P19 q;for(int i=0;i<19;i++)q[p[i]]=i;return q;}
P19 revc(const P19&p){P19 q;for(int i=0;i<19;i++)q[i]=18-p[18-i];return q;}
string enc(const P19&p){string s(19,'\0');for(int i=0;i<19;i++)s[i]=char(p[i]);return s;}
struct Mom { double ELQ,ELA,EHQ,EHA,EQ,EA,ETQ; };
Mom mom_for_k(int k){
 if(k==0) return {-0.49274272649821194,0.5072572735017881,-0.07194776030688184,0.9059180617881541,-0.28234524340254685,0.7065876676449712,-0.06930297812240624};
 if(k==1) return {-0.38761655698378217,0.6123834430162178,-0.014283723659716032,0.9229852395032743,-0.2009501403217491,0.767684341259746,-0.037323738794207244};
 if(k==2) return {-0.3034834012960555,0.6965165987039444,0.04295655886598408,0.9173040775486125,-0.13026342121503573,0.8069103381262785,-0.006586384279870463};
 if(k==3) return {-0.22977689526887907,0.770223104731121,0.10147711220257714,0.8887786272207449,-0.06414989153315095,0.8295008659759329,0.023988879394860704};
 return {-0.1630960894657213,0.8369039105342787,0.1630960894657213,0.8369039105342787,0.0,0.8369039105342787,0.055271112291511014};
}
static const long long DEN=1000000000000000LL;
struct Root {int d; long long lo,hi;};
static const Root roots[]={
 {19,4358898943540673LL,4358898943540674LL},{209,14456832294800960LL,14456832294800961LL},
 {247,15716233645501710LL,15716233645501711LL},{266,16309506430300090LL,16309506430300091LL},{38,6164414002968976LL,6164414002968977LL},
 {285,16881943016134132LL,16881943016134133LL},{57,7549834435270749LL,7549834435270750LL},
 {114,10677078252031311LL,10677078252031312LL},{190,13784048752090221LL,13784048752090222LL},{323,17972200755611428LL,17972200755611429LL}
};
const Root& rt(int d){for(auto &x:roots) if(x.d==d)return x; abort();}
void verify_roots(){ __int128 den2=(__int128)DEN*DEN; for(auto &x:roots){__int128 lo2=(__int128)x.lo*x.lo, hi2=(__int128)x.hi*x.hi, tar=(__int128)x.d*den2; if(!(lo2<=tar && tar<hi2)){cerr<<"ROOT BOUND FAIL "<<x.d<<"\n";exit(4);}} }
__int128 lb_num(int k,int A,int B,int C,int D,int E,int F){
 long long R=0; vector<pair<int,long long>> cs;
 if(k==0){ R=-6897LL*A-3135LL*B-5016LL*C+1444LL*E+722LL*F+887870LL; cs={{19,1408LL*B+704LL*C-128LL*E-64LL*F-181760LL},{209,242LL*A-242LL*B+22LL*D-22LL*E}}; }
 else if(k==1){ R=-6897LL*A-627LL*B-3762LL*C+1444LL*E+722LL*F+682670LL; cs={{247,286LL*A-286LL*B+26LL*D-26LL*E},{266,308LL*B+154LL*C-28LL*E-14LL*F-38640LL},{38,-44LL*A-22LL*C-4LL*D-2LL*F-160LL}}; }
 else if(k==2){ R=-6897LL*A+1881LL*B-2508LL*C+1444LL*E+722LL*F+500270LL; cs={{19,-176LL*A-88LL*C-16LL*D-8LL*F-1280LL},{285,330LL*A-330LL*B+30LL*D-30LL*E},{57,528LL*B+264LL*C-48LL*E-24LL*F-64320LL}}; }
 else if(k==3){ R=-6897LL*A+4389LL*B-1254LL*C+1444LL*E+722LL*F+340670LL; cs={{114,-132LL*A-66LL*C-12LL*D-6LL*F-1440LL},{190,220LL*B+110LL*C-20LL*E-10LL*F-26000LL},{323,374LL*A-374LL*B+34LL*D-34LL*E}}; }
 else { R=1045LL*A-1045LL*B+722LL*D+722LL*E+722LL*F+203870LL; cs={{38,-352LL*A+352LL*B-32LL*D-32LL*E-32LL*F-45440LL}}; }
 __int128 out=(__int128)R*DEN; for(auto [rad,c]:cs){auto &x=rt(rad);out+=(__int128)c*(c>=0?x.lo:x.hi);} return out;
}
static string i128str(__int128 x){ if(x==0)return"0"; bool neg=x<0;if(neg)x=-x;string s;while(x){s.push_back('0'+x%10);x/=10;}if(neg)s.push_back('-');reverse(s.begin(),s.end());return s;}
int main(int argc,char**argv){
 if(argc<3){cerr<<"usage: prog k reps.csv\n";return 2;} int k=atoi(argv[1]); if(k<0||k>4)return 2; verify_roots(); Mom mm=mom_for_k(k);
 vector<array<Slot,11>> tils;
 if(k<=1) for(int v=0;v<11;v++){ vector<int> rv; for(int q=0;q<11;q++) if(q!=v) rv.push_back(q); auto ff=factorization10(rv); for(int lr=0;lr<9;lr++) for(int hr=0;hr<9;hr++){ array<Slot,11> sl; int c=0; for(auto [aa,bb]:ff[lr])sl[c++]={'L',aa+bb-10}; for(auto [aa,bb]:ff[hr])sl[c++]={'H',aa+bb-10}; sl[c++]={'V',2*v-10}; tils.push_back(sl); }}
 array<int,11> sig; iota(sig.begin(),sig.end(),0); long long total=0,unipass=0,unifail=0,fixedpass=0,adaptpass=0,remain=0; long long min_unipass=1e18,max_unifail=-1e18; vector<long long> uses(891,0); unordered_set<string> reps; const int N=19; const long long rhs=8LL*N*N*N*N; __int128 minfix=0,minadapt=0; bool hfix=false,hadapt=false;
 do{
  ++total; int gp[N]; iota(gp,gp+N,0); for(int i=0;i<11;i++)gp[k+i]=k+sig[i];
  long long half=0; for(int i=0;i<N;i++) for(int j=i+1;j<N;j++){int dd=i-j,ee=gp[i]-gp[j]; half+=(long long)abs(dd-ee)*psi12(dd+ee);} long long margin=10*half-rhs;
  if(margin>=0){++unipass;min_unipass=min(min_unipass,margin);continue;} ++unifail;max_unifail=max(max_unifail,margin);
  struct Br{int j,s,d;}; vector<Br> br; for(int j=0;j<11;j++)br.push_back({j,j+sig[j],j-sig[j]}); sort(br.begin(),br.end(),[](auto&x,auto&y){if(x.s!=y.s)return x.s<y.s;if(x.d!=y.d)return x.d<y.d;return x.j<y.j;}); vector<Br> low(br.begin(),br.begin()+5),high(br.begin()+6,br.end()); Br vert=br[5]; sort(low.begin(),low.end(),[](auto&x,auto&y){return x.d<y.d;}); sort(high.begin(),high.end(),[](auto&x,auto&y){return x.d<y.d;}); int nums[5]={-9,-5,0,5,9}; int CSL=0,CSH=0,ZL=0,ZH=0; for(int i=0;i<5;i++){CSL+=low[i].s;ZL+=low[i].d*nums[i];CSH+=high[i].s-2;ZH+=high[i].d*nums[i];} int sV=vert.s,ZV=0; auto lb=lb_num(k,CSL,CSH,sV,ZL,ZH,ZV);
  if(lb>0){++fixedpass;if(!hfix||lb<minfix){minfix=lb;hfix=true;}continue;}
  bool ok=false; int s[11],dd[11]; for(int j=0;j<11;j++){s[j]=j+sig[j];dd[j]=j-sig[j];}
  if(k<=1){ for(int ti=0;ti<(int)tils.size()&&!ok;ti++){ double Cst[11][11]; auto&sl=tils[ti]; for(int j=0;j<11;j++)for(int cc=0;cc<11;cc++){double z=sl[cc].z/11.0,score; if(sl[cc].typ=='L')score=s[j]*mm.ELQ+dd[j]*z*mm.ELA; else if(sl[cc].typ=='H')score=(s[j]-2)*mm.EHQ+dd[j]*z*mm.EHA; else score=s[j]*mm.EQ+dd[j]*z*mm.EA; Cst[j][cc]=-score;} int asg[11];hungarian11(Cst,asg); CSL=CSH=sV=ZL=ZH=ZV=0; for(int j=0;j<11;j++){auto slot=sl[asg[j]]; if(slot.typ=='L'){CSL+=s[j];ZL+=dd[j]*slot.z;} else if(slot.typ=='H'){CSH+=s[j]-2;ZH+=dd[j]*slot.z;} else{sV=s[j];ZV=dd[j]*slot.z;}} auto lb2=lb_num(k,CSL,CSH,sV,ZL,ZH,ZV); if(lb2>0){ok=true;++adaptpass;++uses[ti];if(!hadapt||lb2<minadapt){minadapt=lb2;hadapt=true;}}} }
  if(ok)continue; ++remain; P19 p;for(int i=0;i<N;i++)p[i]=gp[i];P19 aa=invp(p),bb=revc(p),cc=invp(bb);P19 best=min(min(p,aa),min(bb,cc));reps.insert(enc(best));
 }while(next_permutation(sig.begin(),sig.end()));
 vector<string> vv(reps.begin(),reps.end()); sort(vv.begin(),vv.end()); ofstream ff(argv[2]); for(auto&s0:vv){for(int i=0;i<N;i++){if(i)ff<<",";ff<<(int)(unsigned char)s0[i];}ff<<"\n";}
 cout<<"k="<<k<<" total="<<total<<"\n"; cout<<"universal_pass="<<unipass<<" universal_fail="<<unifail<<" min_pass="<<min_unipass<<" max_fail="<<max_unifail<<"\n"; cout<<"fixed_exact_pass="<<fixedpass<<" minfix_num="<<(hfix?i128str(minfix):string("NA"))<<"\n"; cout<<"adaptive_exact_pass="<<adaptpass<<" nonzero_tilings="<<count_if(uses.begin(),uses.end(),[](long long x){return x>0;})<<" minadapt_num="<<(hadapt?i128str(minadapt):string("NA"))<<"\n"; cout<<"remain="<<remain<<" canonical_reps="<<reps.size()<<"\n"; bool chk=false;
 if(k==0) chk=(total==39916800LL&&unipass==6935898LL&&unifail==32980902LL&&min_unipass==2&&max_unifail==-8&&fixedpass==32914915LL&&adaptpass==63954LL&&remain==2033LL&&reps.size()==1277);
 if(k==1) chk=(total==39916800LL&&unipass==1683006LL&&unifail==38233794LL&&min_unipass==2&&max_unifail==-8&&fixedpass==38223239LL&&adaptpass==10176LL&&remain==379LL&&reps.size()==261);
 if(k==2) chk=(total==39916800LL&&unipass==140238LL&&unifail==39776562LL&&min_unipass==2&&max_unifail==-8&&fixedpass==39772416LL&&adaptpass==0LL&&remain==4146LL&&reps.size()==2914);
 if(k==3) chk=(total==39916800LL&&unipass==0LL&&unifail==39916800LL&&max_unifail==-9208&&fixedpass==39914279LL&&adaptpass==0LL&&remain==2521LL&&reps.size()==1734);
 if(k==4) chk=(total==39916800LL&&unipass==0LL&&unifail==39916800LL&&max_unifail==-23608&&fixedpass==39914630LL&&adaptpass==0LL&&remain==2170LL&&reps.size()==772);
 if(!chk){cerr<<"ASSERTION FAILURE\n";return 3;} cout<<"S11 N19 EXACT PHASE1 PASSED\n";
}
