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
using P16=array<unsigned char,16>;
P16 invp(const P16&p){P16 q;for(int i=0;i<16;i++)q[p[i]]=i;return q;}
P16 revc(const P16&p){P16 q;for(int i=0;i<16;i++)q[i]=15-p[15-i];return q;}
string enc(const P16&p){string s(16,'\0');for(int i=0;i<16;i++)s[i]=char(p[i]);return s;}
struct Mom { double ELQ,ELA,EHQ,EHA,EQ,EA,ETQ; };
Mom mom_for_k(int k){
 if(k==0) return {-0.44722920160743335,0.5527707983925666,0.017271271329915076,0.907490162187982,-0.21497896513875914,0.7301304802902743,-0.027895250811370995};
 if(k==1) return {-0.332670614298702,0.6673293857012981,0.08720076389299485,0.8863699457727063,-0.12273492520285356,0.7768496657370022,0.010080458005726198};
 return {-0.2409886334377083,0.7590113665622917,0.1606392161149669,0.8364895659119648,-0.04017470866137069,0.7977504662371283,0.04828006141303625};
}
int main(int argc,char**argv){
 if(argc<5){cerr<<"usage: prog k fixed.csv adapt.csv reps.csv\n";return 2;} int k=atoi(argv[1]); if(k<0||k>2)return 2; Mom mm=mom_for_k(k);
 vector<array<Slot,11>> tils;
 for(int v=0;v<11;v++){ vector<int> rv; for(int q=0;q<11;q++) if(q!=v) rv.push_back(q); auto ff=factorization10(rv); for(int lr=0;lr<9;lr++) for(int hr=0;hr<9;hr++){ array<Slot,11> sl; int c=0; for(auto [a,b]:ff[lr])sl[c++]={'L',a+b-10}; for(auto [a,b]:ff[hr])sl[c++]={'H',a+b-10}; sl[c++]={'V',2*v-10}; tils.push_back(sl); }}
 array<int,11> sig; iota(sig.begin(),sig.end(),0); long long total=0,unipass=0,unifail=0,fixedpass=0,adaptpass=0,remain=0; long long min_unipass=1e18,max_unifail=-1e18; vector<long long> uses(tils.size(),0); unordered_set<Tup,TupHash> fixedtuples,adapttuples; unordered_set<string> reps; const int N=16; const long long rhs=8LL*N*N*N*N;
 do{
  ++total; int gp[N]; iota(gp,gp+N,0); for(int i=0;i<11;i++)gp[k+i]=k+sig[i];
  long long half=0; for(int i=0;i<N;i++) for(int j=i+1;j<N;j++){int d=i-j,e=gp[i]-gp[j]; half+=(long long)abs(d-e)*psi12(d+e);} long long margin=10*half-rhs;
  if(margin>=0){++unipass;min_unipass=min(min_unipass,margin);continue;} ++unifail;max_unifail=max(max_unifail,margin);
  struct Br{int j,s,d;}; vector<Br> br; for(int j=0;j<11;j++)br.push_back({j,j+sig[j],j-sig[j]}); sort(br.begin(),br.end(),[](auto&x,auto&y){if(x.s!=y.s)return x.s<y.s;if(x.d!=y.d)return x.d<y.d;return x.j<y.j;}); vector<Br> low(br.begin(),br.begin()+5),high(br.begin()+6,br.end()); Br vert=br[5]; sort(low.begin(),low.end(),[](auto&x,auto&y){return x.d<y.d;}); sort(high.begin(),high.end(),[](auto&x,auto&y){return x.d<y.d;}); int nums[5]={-9,-5,0,5,9}; int CSL=0,CSH=0,ZL=0,ZH=0; for(int i=0;i<5;i++){CSL+=low[i].s;ZL+=low[i].d*nums[i];CSH+=high[i].s-2;ZH+=high[i].d*nums[i];} int sV=vert.s,ZV=0;
  double T=CSL*mm.ELQ+CSH*mm.EHQ+sV*mm.EQ+(ZL/11.0)*mm.ELA+(ZH/11.0)*mm.EHA-200*mm.ETQ;
  if(T>1e-9){++fixedpass;fixedtuples.insert({CSL,CSH,sV,ZL,ZH,ZV});continue;}
  int s[11],d[11]; for(int j=0;j<11;j++){s[j]=j+sig[j];d[j]=j-sig[j];} bool ok=false;
  for(int ti=0;ti<(int)tils.size()&&!ok;ti++){ double C[11][11]; auto&sl=tils[ti]; for(int j=0;j<11;j++)for(int c=0;c<11;c++){double z=sl[c].z/11.0,score; if(sl[c].typ=='L')score=s[j]*mm.ELQ+d[j]*z*mm.ELA; else if(sl[c].typ=='H')score=(s[j]-2)*mm.EHQ+d[j]*z*mm.EHA; else score=s[j]*mm.EQ+d[j]*z*mm.EA; C[j][c]=-score;} int asg[11];hungarian11(C,asg); CSL=CSH=sV=ZL=ZH=ZV=0; for(int j=0;j<11;j++){auto slot=sl[asg[j]]; if(slot.typ=='L'){CSL+=s[j];ZL+=d[j]*slot.z;} else if(slot.typ=='H'){CSH+=s[j]-2;ZH+=d[j]*slot.z;} else{sV=s[j];ZV=d[j]*slot.z;}} T=CSL*mm.ELQ+CSH*mm.EHQ+sV*mm.EQ+(ZL/11.0)*mm.ELA+(ZH/11.0)*mm.EHA+(ZV/11.0)*mm.EA-200*mm.ETQ; if(T>1e-8){ok=true;++adaptpass;++uses[ti];adapttuples.insert({CSL,CSH,sV,ZL,ZH,ZV});}}
  if(ok)continue; ++remain; P16 p;for(int i=0;i<N;i++)p[i]=gp[i];P16 a=invp(p),b=revc(p),c=invp(b);P16 best=min(min(p,a),min(b,c));reps.insert(enc(best));
 }while(next_permutation(sig.begin(),sig.end()));
 ofstream f1(argv[2]),f2(argv[3]),f3(argv[4]); for(auto &x:fixedtuples)f1<<x.a<<","<<x.b<<","<<x.c<<","<<x.d<<","<<x.e<<","<<x.f<<"\n"; for(auto&x:adapttuples)f2<<x.a<<","<<x.b<<","<<x.c<<","<<x.d<<","<<x.e<<","<<x.f<<"\n"; for(auto&s0:reps){for(int i=0;i<N;i++){if(i)f3<<",";f3<<(int)(unsigned char)s0[i];}f3<<"\n";}
 cout<<"k="<<k<<" total="<<total<<"\n"; cout<<"universal_pass="<<unipass<<" universal_fail="<<unifail<<" min_pass="<<min_unipass<<" max_fail="<<max_unifail<<"\n"; cout<<"fixed_pass="<<fixedpass<<" fixed_unique_tuples="<<fixedtuples.size()<<"\n"; cout<<"adaptive_pass="<<adaptpass<<" nonzero_tilings="<<count_if(uses.begin(),uses.end(),[](long long x){return x>0;})<<" adaptive_unique_tuples="<<adapttuples.size()<<"\n"; cout<<"remain="<<remain<<" canonical_reps="<<reps.size()<<"\n";
 bool chk=false;
 if(k==0) chk=(total==39916800LL && unipass==25769333LL && unifail==14147467LL && min_unipass==2 && max_unifail==-8 && fixedpass==14040832LL && fixedtuples.size()==468848 && adaptpass==103157LL && adapttuples.size()==7004 && remain==3478LL && reps.size()==2115);
 if(k==1) chk=(total==39916800LL && unipass==18836094LL && unifail==21080706LL && min_unipass==2 && max_unifail==-8 && fixedpass==21058170LL && fixedtuples.size()==610209 && adaptpass==21723LL && adapttuples.size()==1845 && remain==813LL && reps.size()==506);
 if(k==2) chk=(total==39916800LL && unipass==14283783LL && unifail==25633017LL && min_unipass==2 && max_unifail==-8 && fixedpass==25620447LL && fixedtuples.size()==686413 && adaptpass==12130LL && adapttuples.size()==1288 && remain==440LL && reps.size()==247);
 if(!chk){cerr<<"ASSERTION FAILURE\n";return 3;}
 cout<<"S11 N16 PHASE1 + ALL-891-DOMINO CENSUS PASSED\n";
}
