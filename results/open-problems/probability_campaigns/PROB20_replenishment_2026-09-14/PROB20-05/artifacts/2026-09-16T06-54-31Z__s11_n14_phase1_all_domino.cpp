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
struct Tup { int a,b,c,d,e,f; bool operator==(Tup const&o) const {return tie(a,b,c,d,e,f)==tie(o.a,o.b,o.c,o.d,o.e,o.f);} };
struct TupHash { size_t operator()(Tup const&k) const { size_t h=0; int v[6]={k.a,k.b,k.c,k.d,k.e,k.f}; for(int x:v) h=h*1009+(x+500); return h; } };
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
using P14=array<unsigned char,14>;
P14 invp(const P14&p){P14 q;for(int i=0;i<14;i++)q[p[i]]=i;return q;}
P14 revc(const P14&p){P14 q;for(int i=0;i<14;i++)q[i]=13-p[13-i];return q;}
string enc(const P14&p){string s(14,'\0');for(int i=0;i<14;i++)s[i]=char(p[i]);return s;}
struct Mom { double ELQ,ELA,EHQ,EHA,EQ,EA,ETQ; };
Mom mom_for_k(int k){
 if(k==0) return {-0.40906315971472111447,0.59093684028527888553,0.10166449455102395096,0.86797684638322960682,-0.15369933244247312579,0.72945648538448529203,0.011076167305232733337};
 return {-0.28659487845126330437,0.71340512154873669563,0.18854402931947397145,0.80816955816669826716,-0.04902542482830911447,0.76078758489310129802,0.056837004857659858117};
}
int main(int argc,char**argv){
 if(argc<5){cerr<<"usage: prog k fixed.csv adapt.csv reps.csv\n";return 2;} int k=atoi(argv[1]); if(k<0||k>1)return 2; Mom mm=mom_for_k(k);
 vector<int> rem; for(int q=1;q<11;q++) rem.push_back(q); auto fac=factorization10(rem); vector<array<Slot,11>> tils;
 for(int v=0;v<11;v++){ vector<int> rv; for(int q=0;q<11;q++) if(q!=v) rv.push_back(q); auto ff=factorization10(rv); for(int lr=0;lr<9;lr++) for(int hr=0;hr<9;hr++){ array<Slot,11> sl; int c=0; for(auto [a,b]:ff[lr])sl[c++]={'L',a+b-10}; for(auto [a,b]:ff[hr])sl[c++]={'H',a+b-10}; sl[c++]={'V',2*v-10}; tils.push_back(sl); }}
 array<int,11> sig; iota(sig.begin(),sig.end(),0); long long total=0,unipass=0,unifail=0,fixedpass=0,adaptpass=0,remain=0; long long min_unipass=1e18,max_unifail=-1e18; vector<long long> uses(tils.size(),0); unordered_set<Tup,TupHash> fixedtuples,adapttuples; unordered_set<string> reps; const int N=14; const long long rhs=8LL*N*N*N*N;
 do{
  ++total; int gp[N]; iota(gp,gp+N,0); for(int i=0;i<11;i++)gp[k+i]=k+sig[i];
  long long half=0; for(int i=0;i<N;i++) for(int j=i+1;j<N;j++){int d=i-j,e=gp[i]-gp[j]; half+=(long long)abs(d-e)*psi12(d+e);} long long margin=10*half-rhs;
  if(margin>=0){++unipass;min_unipass=min(min_unipass,margin);continue;} ++unifail;max_unifail=max(max_unifail,margin);
  struct Br{int j,s,d;}; vector<Br> br; for(int j=0;j<11;j++)br.push_back({j,j+sig[j],j-sig[j]}); sort(br.begin(),br.end(),[](auto&x,auto&y){if(x.s!=y.s)return x.s<y.s;if(x.d!=y.d)return x.d<y.d;return x.j<y.j;}); vector<Br> low(br.begin(),br.begin()+5),high(br.begin()+6,br.end()); Br vert=br[5]; sort(low.begin(),low.end(),[](auto&x,auto&y){return x.d<y.d;}); sort(high.begin(),high.end(),[](auto&x,auto&y){return x.d<y.d;}); int nums[5]={-9,-5,0,5,9}; int CSL=0,CSH=0,ZL=0,ZH=0; for(int i=0;i<5;i++){CSL+=low[i].s;ZL+=low[i].d*nums[i];CSH+=high[i].s-2;ZH+=high[i].d*nums[i];} int sV=vert.s,ZV=0;
  double T=CSL*mm.ELQ+CSH*mm.EHQ+sV*mm.EQ+(ZL/11.0)*mm.ELA+(ZH/11.0)*mm.EHA-200*mm.ETQ;
  if(T>1e-9){++fixedpass;fixedtuples.insert({CSL,CSH,sV,ZL,ZH,ZV});continue;}
  int s[11],d[11]; for(int j=0;j<11;j++){s[j]=j+sig[j];d[j]=j-sig[j];} bool ok=false;
  for(int ti=0;ti<(int)tils.size()&&!ok;ti++){ double C[11][11]; auto&sl=tils[ti]; for(int j=0;j<11;j++)for(int c=0;c<11;c++){double z=sl[c].z/11.0,score; if(sl[c].typ=='L')score=s[j]*mm.ELQ+d[j]*z*mm.ELA; else if(sl[c].typ=='H')score=(s[j]-2)*mm.EHQ+d[j]*z*mm.EHA; else score=s[j]*mm.EQ+d[j]*z*mm.EA; C[j][c]=-score;} int asg[11];hungarian11(C,asg); CSL=CSH=sV=ZL=ZH=ZV=0; for(int j=0;j<11;j++){auto slot=sl[asg[j]]; if(slot.typ=='L'){CSL+=s[j];ZL+=d[j]*slot.z;} else if(slot.typ=='H'){CSH+=s[j]-2;ZH+=d[j]*slot.z;} else{sV=s[j];ZV=d[j]*slot.z;}} T=CSL*mm.ELQ+CSH*mm.EHQ+sV*mm.EQ+(ZL/11.0)*mm.ELA+(ZH/11.0)*mm.EHA+(ZV/11.0)*mm.EA-200*mm.ETQ; if(T>1e-8){ok=true;++adaptpass;++uses[ti];adapttuples.insert({CSL,CSH,sV,ZL,ZH,ZV});}}
  if(ok)continue; ++remain; P14 p;for(int i=0;i<N;i++)p[i]=gp[i];P14 a=invp(p),b=revc(p),c=invp(b);P14 best=min(min(p,a),min(b,c));reps.insert(enc(best));
 }while(next_permutation(sig.begin(),sig.end()));
 ofstream f1(argv[2]),f2(argv[3]),f3(argv[4]); for(auto &x:fixedtuples)f1<<x.a<<","<<x.b<<","<<x.c<<","<<x.d<<","<<x.e<<","<<x.f<<"\n"; for(auto&x:adapttuples)f2<<x.a<<","<<x.b<<","<<x.c<<","<<x.d<<","<<x.e<<","<<x.f<<"\n"; for(auto&s0:reps){for(int i=0;i<N;i++){if(i)f3<<",";f3<<(int)(unsigned char)s0[i];}f3<<"\n";}
 cout<<"k="<<k<<" total="<<total<<"\n"; cout<<"universal_pass="<<unipass<<" universal_fail="<<unifail<<" min_pass="<<min_unipass<<" max_fail="<<max_unifail<<"\n"; cout<<"fixed_pass="<<fixedpass<<" fixed_unique_tuples="<<fixedtuples.size()<<"\n"; cout<<"adaptive_pass="<<adaptpass<<" nonzero_tilings="<<count_if(uses.begin(),uses.end(),[](long long x){return x>0;})<<" adaptive_unique_tuples="<<adapttuples.size()<<"\n"; cout<<"remain="<<remain<<" canonical_reps="<<reps.size()<<"\n";
 bool ok=false;
 if(k==0) ok=(total==39916800LL && unipass==35107045LL && unifail==4809755LL && min_unipass==2 && max_unifail==-8 && fixedpass==4604655LL && fixedtuples.size()==233615 && adaptpass==196558LL && adapttuples.size()==15594 && remain==8542LL && reps.size()==4941);
 if(k==1) ok=(total==39916800LL && unipass==33008145LL && unifail==6908655LL && min_unipass==2 && max_unifail==-8 && fixedpass==6839065LL && fixedtuples.size()==319843 && adaptpass==67062LL && adapttuples.size()==6205 && remain==2528LL && reps.size()==1254);
 if(!ok){cerr<<"ASSERTION FAILURE\n";return 3;}
 cout<<"S11 N14 PHASE1 + ALL-891-DOMINO CENSUS PASSED\n";
}
