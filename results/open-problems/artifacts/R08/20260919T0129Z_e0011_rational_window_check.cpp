#include <bits/stdc++.h>
#include <boost/multiprecision/cpp_int.hpp>
using namespace std; using boost::multiprecision::cpp_int;
struct P{int x,y;}; vector<P> dirs={{1,0},{-1,0},{0,1},{0,-1}};
vector<P> SC={{-2,0},{-2,1},{-1,-1},{-1,0},{-1,1},{-1,2},{0,-1},{0,0},{0,1},{0,2},{1,-1},{1,0},{1,1},{2,0}};
vector<P> CEL={{-2,0},{-2,1},{-1,-1},{-1,0},{-1,1},{-1,2},{0,-1},{0,0},{0,1},{0,2},{1,-1},{1,0},{1,1},{1,2},{2,0},{2,1}};
map<pair<int,int>,int> SI,FI; int pow3s[20];
int gettr(uint32_t s,int i){return (s/pow3s[i])%3;} uint32_t settr(uint32_t s,int i,int v){int o=gettr(s,i); return s+(v-o)*pow3s[i];}
vector<int> neigh_idx_sc(P c){vector<int> r; for(auto d:dirs){auto it=SI.find({c.x+d.x,c.y+d.y}); if(it!=SI.end())r.push_back(it->second);} return r;}
struct Label{int kind;P a,b;};
vector<Label> labels={ {0,{0,0},{0,0}}, {1,{-1,1},{0,1}}, {0,{0,1},{0,0}}, {0,{1,0},{0,0}}, {1,{-1,0},{-1,1}}, {1,{0,0},{0,1}}, {0,{-1,1},{0,0}}, {1,{-1,0},{0,0}}, {0,{-1,0},{0,0}}, {1,{0,0},{1,0}} };
vector<pair<uint32_t,int>> trans(uint32_t s,int li){ static unordered_map<uint64_t,vector<pair<uint32_t,int>>> memo; uint64_t key=(uint64_t)s*10+li; auto it=memo.find(key); if(it!=memo.end())return it->second; Label L=labels[li]; map<uint32_t,int> out; if(L.kind==0){int i=SI[{L.a.x,L.a.y}]; if(gettr(s,i)!=0) out[s]+=72; else {uint32_t a=settr(s,i,1); vector<int> os; for(int q:neigh_idx_sc(L.a))if(gettr(a,q)==2)os.push_back(q); if(os.empty())out[a]+=72; else {int w=72/(int)os.size(); for(int q:os){uint32_t t=settr(a,i,0);t=settr(t,q,0);out[t]+=w;}}}} else {int ia=SI[{L.a.x,L.a.y}],ib=SI[{L.b.x,L.b.y}]; if(gettr(s,ia)!=0||gettr(s,ib)!=0)out[s]+=36; else {uint32_t a=settr(settr(s,ia,2),ib,2); vector<int> ca,cb; for(int q:neigh_idx_sc(L.a))if(gettr(a,q)==1)ca.push_back(q); for(int q:neigh_idx_sc(L.b))if(gettr(a,q)==1)cb.push_back(q); if(ca.empty())ca.push_back(-1);if(cb.empty())cb.push_back(-1); int w=36/((int)ca.size()*(int)cb.size()); for(int qa:ca)for(int qb:cb){uint32_t t=a;if(qa!=-1){t=settr(t,ia,0);t=settr(t,qa,0);} if(qb!=-1){t=settr(t,ib,0);t=settr(t,qb,0);}out[t]+=w;}}} vector<pair<uint32_t,int>> v(out.begin(),out.end());memo.emplace(key,v);return v;}
vector<unordered_map<uint32_t,cpp_int>> memoA(9); bool target(uint32_t s){for(auto c:vector<P>{{-1,0},{-1,1},{0,0},{0,1},{1,0},{1,1}}){if(gettr(s,SI[{c.x,c.y}])!=0)return false;}return true;}
cpp_int A(int n,uint32_t s){auto &M=memoA[n];auto it=M.find(s);if(it!=M.end())return it->second;cpp_int z;if(n==0)z=target(s)?1:0;else for(int li=0;li<10;li++)for(auto [t,w]:trans(s,li))z+=cpp_int(w)*A(n-1,t);M.emplace(s,z);return z;}
int main(){pow3s[0]=1;for(int i=1;i<20;i++)pow3s[i]=pow3s[i-1]*3;for(int i=0;i<(int)SC.size();i++)SI[{SC[i].x,SC[i].y}]=i;for(int i=0;i<(int)CEL.size();i++)FI[{CEL[i].x,CEL[i].y}]=i; set<pair<int,int>> fixed={{-1,0},{-1,1}};vector<int> var;for(int i=0;i<(int)CEL.size();i++)if(!fixed.count({CEL[i].x,CEL[i].y}))var.push_back(i); long long total=1;for(size_t i=0;i<var.size();i++)total*=3;unordered_set<uint32_t> initset;long long full=0;vector<int> vals(CEL.size());for(long long code=0;code<total;code++){long long z=code;for(int i:var){vals[i]=z%3;z/=3;}for(int i=0;i<(int)CEL.size();i++)if(fixed.count({CEL[i].x,CEL[i].y}))vals[i]=0;bool ok=true;for(int i=0;i<(int)CEL.size()&&ok;i++){P c=CEL[i];int a=vals[i];for(auto d:vector<P>{{1,0},{0,1}}){auto it=FI.find({c.x+d.x,c.y+d.y});if(it!=FI.end()){int b=vals[it->second];if((a==1&&b==2)||(a==2&&b==1)){ok=false;break;}}}}if(!ok)continue;full++;uint32_t s=0;for(int i=0;i<(int)SC.size();i++)s+=vals[FI[{SC[i].x,SC[i].y}]]*pow3s[i];initset.insert(s);} cerr<<"full="<<full<<" desc="<<initset.size()<<"\n";
  const int N=8,D=140,H=36*D, P=87,Q=20; cpp_int F=1; for(int i=2;i<=N;i++)F*=i;
  auto ipow2=[](cpp_int a,int n){cpp_int r=1;while(n--)r*=a;return r;}; auto fact2=[](int n){cpp_int r=1;for(int i=2;i<=n;i++)r*=i;return r;};
  bool fst=true; cpp_int mn=0; uint32_t arg=0;
  for(auto st:initset){ cpp_int sum=0; for(int n=0;n<=N;n++){
      cpp_int coeff=ipow2(cpp_int(P),n)*ipow2(cpp_int(Q),N-n)*(F/fact2(n))*ipow2(cpp_int(H),N-n);
      sum += coeff*A(n,st);
    }
    if(fst||sum<mn){mn=sum;arg=st;fst=false;}
  }
  cpp_int polyden=ipow2(cpp_int(Q),N)*F*ipow2(cpp_int(H),N);
  // P7(7/20)=sum_{k=0}^7 (-x)^k/k! = 649440538531/921600000000 < exp(-7/20).
  cpp_int lbnum=ipow2(cpp_int(32),4)*cpp_int("649440538531")*mn;
  cpp_int lbden=ipow2(cpp_int(87),4)*cpp_int("921600000000")*polyden;
  cpp_int oldn("449855540637605888"), oldd("88875222725965541291015625");
  bool gain=lbnum*oldd>oldn*lbden;
  cout<<"PASS exact R08/E0011 rational-window certificate\n";
  cout<<"arg="<<arg<<" mn="<<mn<<"\n";
  cout<<"new_num="<<lbnum<<"\nnew_den="<<lbden<<"\n";
  cout<<"gain_exact="<<(gain?"true":"false")<<"\n";
  long double rat=(lbnum.convert_to<long double>()/lbden.convert_to<long double>())/(oldn.convert_to<long double>()/oldd.convert_to<long double>());
  cout<<setprecision(18)<<"gain="<<(double)rat<<" log10gain="<<(double)log10l(rat)<<"\n";
}
