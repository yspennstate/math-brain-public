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
using P18=array<unsigned char,18>;
P18 invp(const P18&p){P18 q;for(int i=0;i<18;i++)q[p[i]]=i;return q;}
P18 revc(const P18&p){P18 q;for(int i=0;i<18;i++)q[i]=17-p[17-i];return q;}
string enc(const P18&p){string s(18,'\0');for(int i=0;i<18;i++)s[i]=char(p[i]);return s;}
struct Mom { double ELQ,ELA,EHQ,EHA,EQ,EA,ETQ; };
Mom mom_for_k(int k){
 if(k==0) return {-0.47884269335295226,0.5211573066470477,-0.045591279275244326,0.912367575072058,-0.2622169863140983,0.7167624408595529,-0.05706230183867869};
 if(k==1) return {-0.3708358214474121,0.6291641785525879,0.015156567172626985,0.9184342676413891,-0.17783962713739254,0.7737992230969886,-0.023528052672603272};
 if(k==2) return {-0.28439722094151354,0.7156027790584865,0.07639369620425128,0.9002046143861544,-0.10400176236863115,0.8079036967223204,0.009104059205295284};
 return {-0.2086709846308729,0.791329015369127,0.14013957361242316,0.8573112907841404,-0.034265705509224885,0.8243201530766338,0.04203008798392646};
}
static const long long DEN=1000000000000000LL;
struct Root {int d; long long lo,hi;};
static const Root roots[]={
 {22,4690415759823429LL,4690415759823430LL},{7,2645751311064590LL,2645751311064591LL},
 {26,5099019513592784LL,5099019513592785LL},{6,2449489742783178LL,2449489742783179LL},
 {2,1414213562373095LL,1414213562373096LL},{30,5477225575051661LL,5477225575051662LL},{5,2236067977499789LL,2236067977499790LL},
 {3,1732050807568877LL,1732050807568878LL},{34,5830951894845300LL,5830951894845301LL}
};
const Root& rt(int d){for(auto &x:roots) if(x.d==d)return x; abort();}
void verify_roots(){ __int128 den2=(__int128)DEN*DEN; for(auto &x:roots){__int128 lo2=(__int128)x.lo*x.lo, hi2=(__int128)x.hi*x.hi, tar=(__int128)x.d*den2; if(!(lo2<=tar && tar<hi2)){cerr<<"ROOT BOUND FAIL "<<x.d<<"\n";exit(4);}} }
__int128 lb_num(int k,int A,int B,int C,int D,int E,int F){
 long long R=0; vector<pair<int,long long>> cs;
 if(k==0){ R=-1089LL*A-297LL*B-693LL*C+216LL*E+108LL*F+114660LL; cs={{22,121LL*A-121LL*B+11LL*D-11LL*E},{7,308LL*B+154LL*C-28LL*E-14LL*F-38640LL}}; }
 else if(k==1){ R=-1133LL*A+99LL*B-517LL*C-4LL*D+216LL*E+106LL*F+83900LL; cs={{26,143LL*A-143LL*B+13LL*D-13LL*E},{6,264LL*B+132LL*C-24LL*E-12LL*F-32160LL}}; }
 else if(k==2){ R=-1089LL*A+495LL*B-297LL*C+216LL*E+108LL*F+57060LL; cs={{2,-88LL*A-44LL*C-8LL*D-4LL*F-640LL},{30,165LL*A-165LL*B+15LL*D-15LL*E},{5,220LL*B+110LL*C-20LL*E-10LL*F-26000LL}}; }
 else { R=-1089LL*A+1243LL*B+77LL*C+184LL*E+92LL*F-6660LL; cs={{3,-132LL*A-66LL*C-12LL*D-6LL*F-1440LL},{34,187LL*A-187LL*B+17LL*D-17LL*E}}; }
 __int128 out=(__int128)R*DEN; for(auto [rad,c]:cs){auto &x=rt(rad);out+=(__int128)c*(c>=0?x.lo:x.hi);} return out;
}
static string i128str(__int128 x){ if(x==0)return"0"; bool neg=x<0;if(neg)x=-x;string s;while(x){s.push_back('0'+x%10);x/=10;}if(neg)s.push_back('-');reverse(s.begin(),s.end());return s;}
int main(int argc,char**argv){
 if(argc<3){cerr<<"usage: prog k reps.csv\n";return 2;} int k=atoi(argv[1]); if(k<0||k>3)return 2; verify_roots(); Mom mm=mom_for_k(k);
 vector<array<Slot,11>> tils;
 if(k<=1) for(int v=0;v<11;v++){ vector<int> rv; for(int q=0;q<11;q++) if(q!=v) rv.push_back(q); auto ff=factorization10(rv); for(int lr=0;lr<9;lr++) for(int hr=0;hr<9;hr++){ array<Slot,11> sl; int c=0; for(auto [aa,bb]:ff[lr])sl[c++]={'L',aa+bb-10}; for(auto [aa,bb]:ff[hr])sl[c++]={'H',aa+bb-10}; sl[c++]={'V',2*v-10}; tils.push_back(sl); }}
 array<int,11> sig; iota(sig.begin(),sig.end(),0); long long total=0,unipass=0,unifail=0,fixedpass=0,adaptpass=0,remain=0; long long min_unipass=1e18,max_unifail=-1e18; vector<long long> uses(891,0); unordered_set<string> reps; const int N=18; const long long rhs=8LL*N*N*N*N; __int128 minfix=0,minadapt=0; bool hfix=false,hadapt=false;
 do{
  ++total; int gp[N]; iota(gp,gp+N,0); for(int i=0;i<11;i++)gp[k+i]=k+sig[i];
  long long half=0; for(int i=0;i<N;i++) for(int j=i+1;j<N;j++){int dd=i-j,ee=gp[i]-gp[j]; half+=(long long)abs(dd-ee)*psi12(dd+ee);} long long margin=10*half-rhs;
  if(margin>=0){++unipass;min_unipass=min(min_unipass,margin);continue;} ++unifail;max_unifail=max(max_unifail,margin);
  struct Br{int j,s,d;}; vector<Br> br; for(int j=0;j<11;j++)br.push_back({j,j+sig[j],j-sig[j]}); sort(br.begin(),br.end(),[](auto&x,auto&y){if(x.s!=y.s)return x.s<y.s;if(x.d!=y.d)return x.d<y.d;return x.j<y.j;}); vector<Br> low(br.begin(),br.begin()+5),high(br.begin()+6,br.end()); Br vert=br[5]; sort(low.begin(),low.end(),[](auto&x,auto&y){return x.d<y.d;}); sort(high.begin(),high.end(),[](auto&x,auto&y){return x.d<y.d;}); int nums[5]={-9,-5,0,5,9}; int CSL=0,CSH=0,ZL=0,ZH=0; for(int i=0;i<5;i++){CSL+=low[i].s;ZL+=low[i].d*nums[i];CSH+=high[i].s-2;ZH+=high[i].d*nums[i];} int sV=vert.s,ZV=0; auto lb=lb_num(k,CSL,CSH,sV,ZL,ZH,ZV);
  if(lb>0){++fixedpass;if(!hfix||lb<minfix){minfix=lb;hfix=true;}continue;}
  bool ok=false; int s[11],dd[11]; for(int j=0;j<11;j++){s[j]=j+sig[j];dd[j]=j-sig[j];}
  if(k<=1){ for(int ti=0;ti<(int)tils.size()&&!ok;ti++){ double Cst[11][11]; auto&sl=tils[ti]; for(int j=0;j<11;j++)for(int cc=0;cc<11;cc++){double z=sl[cc].z/11.0,score; if(sl[cc].typ=='L')score=s[j]*mm.ELQ+dd[j]*z*mm.ELA; else if(sl[cc].typ=='H')score=(s[j]-2)*mm.EHQ+dd[j]*z*mm.EHA; else score=s[j]*mm.EQ+dd[j]*z*mm.EA; Cst[j][cc]=-score;} int asg[11];hungarian11(Cst,asg); CSL=CSH=sV=ZL=ZH=ZV=0; for(int j=0;j<11;j++){auto slot=sl[asg[j]]; if(slot.typ=='L'){CSL+=s[j];ZL+=dd[j]*slot.z;} else if(slot.typ=='H'){CSH+=s[j]-2;ZH+=dd[j]*slot.z;} else{sV=s[j];ZV=dd[j]*slot.z;}} auto lb2=lb_num(k,CSL,CSH,sV,ZL,ZH,ZV); if(lb2>0){ok=true;++adaptpass;++uses[ti];if(!hadapt||lb2<minadapt){minadapt=lb2;hadapt=true;}}} }
  if(ok)continue; ++remain; P18 p;for(int i=0;i<N;i++)p[i]=gp[i];P18 aa=invp(p),bb=revc(p),cc=invp(bb);P18 best=min(min(p,aa),min(bb,cc));reps.insert(enc(best));
 }while(next_permutation(sig.begin(),sig.end()));
 ofstream ff(argv[2]); for(auto&s0:reps){for(int i=0;i<N;i++){if(i)ff<<",";ff<<(int)(unsigned char)s0[i];}ff<<"\n";}
 cout<<"k="<<k<<" total="<<total<<"\n"; cout<<"universal_pass="<<unipass<<" universal_fail="<<unifail<<" min_pass="<<min_unipass<<" max_fail="<<max_unifail<<"\n"; cout<<"fixed_exact_pass="<<fixedpass<<" minfix_num="<<(hfix?i128str(minfix):string("NA"))<<"\n"; cout<<"adaptive_exact_pass="<<adaptpass<<" nonzero_tilings="<<count_if(uses.begin(),uses.end(),[](long long x){return x>0;})<<" minadapt_num="<<(hadapt?i128str(minadapt):string("NA"))<<"\n"; cout<<"remain="<<remain<<" canonical_reps="<<reps.size()<<"\n";
 bool chk=false;
 if(k==0) chk=(total==39916800LL&&unipass==12737163LL&&unifail==27179637LL&&min_unipass==2&&max_unifail==-8&&fixedpass==27106578LL&&adaptpass==70795LL&&remain==2264LL&&reps.size()==1422);
 if(k==1) chk=(total==39916800LL&&unipass==5247759LL&&unifail==34669041LL&&min_unipass==2&&max_unifail==-8&&fixedpass==34656467LL&&adaptpass==12091LL&&remain==483LL&&reps.size()==326);
 if(k==2) chk=(total==39916800LL&&unipass==1502488LL&&unifail==38414312LL&&min_unipass==2&&max_unifail==-8&&fixedpass==38408954LL&&adaptpass==0LL&&remain==5358LL&&reps.size()==3778);
 if(k==3) chk=(total==39916800LL&&unipass==475572LL&&unifail==39441228LL&&min_unipass==2&&max_unifail==-8&&fixedpass==39437505LL&&adaptpass==0LL&&remain==3723LL&&reps.size()==2458);
 if(!chk){cerr<<"ASSERTION FAILURE\n";return 3;} cout<<"S11 N18 EXACT PHASE1 PASSED\n";
}
