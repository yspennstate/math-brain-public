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
using P20=array<unsigned char,20>;
P20 invp(const P20&p){P20 q;for(int i=0;i<20;i++)q[p[i]]=i;return q;}
P20 revc(const P20&p){P20 q;for(int i=0;i<20;i++)q[i]=19-p[19-i];return q;}
string enc(const P20&p){string s(20,'\0');for(int i=0;i<20;i++)s[i]=char(p[i]);return s;}
struct Mom { double ELQ,ELA,EHQ,EHA,EQ,EA,ETQ; };
Mom mom_for_k(int k){
 if(k==0) return {-0.5055867675269559,0.4944132324730442,-0.09584963459975641,0.8949019575324559,-0.3007182010633561,0.69465759500275,-0.08040228449676301};
 if(k==1) return {-0.4031224520754886,0.5968775479245114,-0.040612122229664274,0.9217109012856504,-0.22186728715257642,0.7592942246050809,-0.04967812669974006};
 if(k==2) return {-0.32111959546868196,0.678880404531318,0.013506625133968362,0.9270532467731128,-0.1538064851673568,0.8029668256522154,-0.0204578494986687};
 if(k==3) return {-0.2492793798565508,0.7507206201434492,0.06799602748484194,0.9110069328305631,-0.09064167618585443,0.8308637764870062,0.00826101054564111};
 return {-0.18428696976559852,0.8157130302344014,0.12437324586232992,0.8733347232119693,-0.029956861951634293,0.8445238767231854,0.037243284750088784};
}
static const long long DEN=1000000000000000LL;
struct Root {int d; long long lo,hi;};
static const Root roots[]={
 {2,1414213562373095LL,1414213562373096LL},{3,1732050807568877LL,1732050807568878LL},{5,2236067977499789LL,2236067977499790LL},{10,3162277660168379LL,3162277660168380LL},{15,3872983346207416LL,3872983346207417LL},{30,5477225575051661LL,5477225575051662LL},{55,7416198487095662LL,7416198487095663LL},{65,8062257748298549LL,8062257748298550LL},{70,8366600265340755LL,8366600265340756LL},{85,9219544457292887LL,9219544457292888LL},{95,9746794344808963LL,9746794344808964LL}
};
const Root& rt(int d){for(auto &x:roots) if(x.d==d)return x; abort();}
void verify_roots(){ __int128 den2=(__int128)DEN*DEN; for(auto &x:roots){__int128 lo2=(__int128)x.lo*x.lo, hi2=(__int128)x.hi*x.hi, tar=(__int128)x.d*den2; if(!(lo2<=tar && tar<hi2)){cerr<<"ROOT BOUND FAIL "<<x.d<<"\n";exit(4);}} }
__int128 lb_num(int k,int A,int B,int C,int D,int E,int F){
 long long R=0; vector<pair<int,long long>> cs;
 if(k==0){ R=-1815LL*A-1155LL*B-1485LL*C+400LL*E+200LL*F+278500LL; cs={{55,121LL*A-121LL*B+11LL*D-11LL*E},{10,594LL*B+297LL*C-54LL*E-27LL*F-78840LL}}; }
 else if(k==1){ R=-1815LL*A-495LL*B-1155LL*C+400LL*E+200LL*F+221500LL; cs={{10,-22LL*A-11LL*C-2LL*D-F-80LL},{65,143LL*A-143LL*B+13LL*D-13LL*E},{5,704LL*B+352LL*C-64LL*E-32LL*F-90880LL}}; }
 else if(k==2){ R=-1815LL*A+165LL*B-825LL*C+400LL*E+200LL*F+170500LL; cs={{5,-88LL*A-44LL*C-8LL*D-4LL*F-640LL},{3,825LL*A-825LL*B+75LL*D-75LL*E},{70,154LL*B+77LL*C-14LL*E-7LL*F-19320LL}}; }
 else if(k==3){ R=-1815LL*A+825LL*B-495LL*C+400LL*E+200LL*F+125500LL; cs={{30,-66LL*A-33LL*C-6LL*D-3LL*F-720LL},{85,187LL*A-187LL*B+17LL*D-17LL*E},{15,264LL*B+132LL*C-24LL*E-12LL*F-32160LL}}; }
 else { R=-1815LL*A+1485LL*B-165LL*C+400LL*E+200LL*F+86500LL; cs={{10,-176LL*A-88LL*C-16LL*D-8LL*F-2560LL},{95,209LL*A-209LL*B+19LL*D-19LL*E},{2,550LL*B+275LL*C-50LL*E-25LL*F-65000LL}}; }
 __int128 out=(__int128)R*DEN; for(auto [rad,c]:cs){auto &x=rt(rad);out+=(__int128)c*(c>=0?x.lo:x.hi);} return out;
}
static string i128str(__int128 x){ if(x==0)return"0"; bool neg=x<0;if(neg)x=-x;string s;while(x){s.push_back('0'+x%10);x/=10;}if(neg)s.push_back('-');reverse(s.begin(),s.end());return s;}
int main(int argc,char**argv){
 if(argc<3){cerr<<"usage: prog k reps.csv\n";return 2;} int k=atoi(argv[1]); if(k<0||k>4)return 2; verify_roots(); Mom mm=mom_for_k(k);
 vector<array<Slot,11>> tils;
 if(k<=1) for(int v=0;v<11;v++){ vector<int> rv; for(int q=0;q<11;q++) if(q!=v) rv.push_back(q); auto ff=factorization10(rv); for(int lr=0;lr<9;lr++) for(int hr=0;hr<9;hr++){ array<Slot,11> sl; int c=0; for(auto [aa,bb]:ff[lr])sl[c++]={'L',aa+bb-10}; for(auto [aa,bb]:ff[hr])sl[c++]={'H',aa+bb-10}; sl[c++]={'V',2*v-10}; tils.push_back(sl); }}
 array<int,11> sig; iota(sig.begin(),sig.end(),0); long long total=0,unipass=0,unifail=0,fixedpass=0,adaptpass=0,remain=0; long long min_unipass=1e18,max_unifail=-1e18; vector<long long> uses(891,0); unordered_set<string> reps; const int N=20; const long long rhs=8LL*N*N*N*N; __int128 minfix=0,minadapt=0; bool hfix=false,hadapt=false;
 do{
  ++total; int gp[N]; iota(gp,gp+N,0); for(int i=0;i<11;i++)gp[k+i]=k+sig[i];
  long long half=0; for(int i=0;i<N;i++) for(int j=i+1;j<N;j++){int dd=i-j,ee=gp[i]-gp[j]; half+=(long long)abs(dd-ee)*psi12(dd+ee);} long long margin=10*half-rhs;
  if(margin>=0){++unipass;min_unipass=min(min_unipass,margin);continue;} ++unifail;max_unifail=max(max_unifail,margin);
  struct Br{int j,s,d;}; vector<Br> br; for(int j=0;j<11;j++)br.push_back({j,j+sig[j],j-sig[j]}); sort(br.begin(),br.end(),[](auto&x,auto&y){if(x.s!=y.s)return x.s<y.s;if(x.d!=y.d)return x.d<y.d;return x.j<y.j;}); vector<Br> low(br.begin(),br.begin()+5),high(br.begin()+6,br.end()); Br vert=br[5]; sort(low.begin(),low.end(),[](auto&x,auto&y){return x.d<y.d;}); sort(high.begin(),high.end(),[](auto&x,auto&y){return x.d<y.d;}); int nums[5]={-9,-5,0,5,9}; int CSL=0,CSH=0,ZL=0,ZH=0; for(int i=0;i<5;i++){CSL+=low[i].s;ZL+=low[i].d*nums[i];CSH+=high[i].s-2;ZH+=high[i].d*nums[i];} int sV=vert.s,ZV=0; auto lb=lb_num(k,CSL,CSH,sV,ZL,ZH,ZV);
  if(lb>0){++fixedpass;if(!hfix||lb<minfix){minfix=lb;hfix=true;}continue;}
  bool ok=false; int s[11],dd[11]; for(int j=0;j<11;j++){s[j]=j+sig[j];dd[j]=j-sig[j];}
  if(k<=1){ for(int ti=0;ti<(int)tils.size()&&!ok;ti++){ double Cst[11][11]; auto&sl=tils[ti]; for(int j=0;j<11;j++)for(int cc=0;cc<11;cc++){double z=sl[cc].z/11.0,score; if(sl[cc].typ=='L')score=s[j]*mm.ELQ+dd[j]*z*mm.ELA; else if(sl[cc].typ=='H')score=(s[j]-2)*mm.EHQ+dd[j]*z*mm.EHA; else score=s[j]*mm.EQ+dd[j]*z*mm.EA; Cst[j][cc]=-score;} int asg[11];hungarian11(Cst,asg); CSL=CSH=sV=ZL=ZH=ZV=0; for(int j=0;j<11;j++){auto slot=sl[asg[j]]; if(slot.typ=='L'){CSL+=s[j];ZL+=dd[j]*slot.z;} else if(slot.typ=='H'){CSH+=s[j]-2;ZH+=dd[j]*slot.z;} else{sV=s[j];ZV=dd[j]*slot.z;}} auto lb2=lb_num(k,CSL,CSH,sV,ZL,ZH,ZV); if(lb2>0){ok=true;++adaptpass;++uses[ti];if(!hadapt||lb2<minadapt){minadapt=lb2;hadapt=true;}}} }
  if(ok)continue; ++remain; P20 p;for(int i=0;i<N;i++)p[i]=gp[i];P20 aa=invp(p),bb=revc(p),cc=invp(bb);P20 best=min(min(p,aa),min(bb,cc));reps.insert(enc(best));
 }while(next_permutation(sig.begin(),sig.end()));
 vector<string> vv(reps.begin(),reps.end()); sort(vv.begin(),vv.end()); ofstream ff(argv[2]); for(auto&s0:vv){for(int i=0;i<N;i++){if(i)ff<<",";ff<<(int)(unsigned char)s0[i];}ff<<"\n";}
 cout<<"k="<<k<<" total="<<total<<"\n"; cout<<"universal_pass="<<unipass<<" universal_fail="<<unifail<<" min_pass="<<(unipass?to_string(min_unipass):string("NA"))<<" max_fail="<<max_unifail<<"\n"; cout<<"fixed_exact_pass="<<fixedpass<<" minfix_num="<<(hfix?i128str(minfix):string("NA"))<<"\n"; cout<<"adaptive_exact_pass="<<adaptpass<<" nonzero_tilings="<<count_if(uses.begin(),uses.end(),[](long long x){return x>0;})<<" minadapt_num="<<(hadapt?i128str(minadapt):string("NA"))<<"\n"; cout<<"remain="<<remain<<" canonical_reps="<<reps.size()<<"\n"; bool chk=false;
 if(k==0) chk=(total==39916800LL&&unipass==2867990LL&&unifail==37048810LL&&min_unipass==0&&max_unifail==-10&&fixedpass==36986700LL&&adaptpass==60174LL&&remain==1936LL&&reps.size()==1215);
 if(k==1) chk=(total==39916800LL&&unipass==268044LL&&unifail==39648756LL&&min_unipass==0&&max_unifail==-10&&fixedpass==39639458LL&&adaptpass==8974LL&&remain==324LL&&reps.size()==234);
 if(k==2) chk=(total==39916800LL&&unipass==0LL&&unifail==39916800LL&&max_unifail==-30640&&fixedpass==39913451LL&&adaptpass==0LL&&remain==3349LL&&reps.size()==2367);
 if(k==3) chk=(total==39916800LL&&unipass==0LL&&unifail==39916800LL&&max_unifail==-88240&&fixedpass==39914916LL&&adaptpass==0LL&&remain==1884LL&&reps.size()==1299);
 if(k==4) chk=(total==39916800LL&&unipass==0LL&&unifail==39916800LL&&max_unifail==-117040&&fixedpass==39915381LL&&adaptpass==0LL&&remain==1419LL&&reps.size()==926);
 if(!chk){cerr<<"ASSERTION FAILURE\n";return 3;} cout<<"S11 N20 EXACT PHASE1 PASSED\n";
}
