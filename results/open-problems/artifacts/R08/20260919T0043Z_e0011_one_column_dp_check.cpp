#include <bits/stdc++.h>
#include <boost/multiprecision/cpp_int.hpp>
using namespace std;
using boost::multiprecision::cpp_int;
struct P{int x,y;};
struct PLess{bool operator()(P const&a,P const&b) const{return tie(a.x,a.y)<tie(b.x,b.y);}};
bool eq(P a,P b){return a.x==b.x&&a.y==b.y;}
vector<P> dirs={{1,0},{-1,0},{0,1},{0,-1}};
vector<P> SC={{-2,0},{-2,1},{-1,-1},{-1,0},{-1,1},{-1,2},{0,-1},{0,0},{0,1},{0,2},{1,-1},{1,0},{1,1},{2,0}};
vector<P> CEL={{-2,0},{-2,1},{-1,-1},{-1,0},{-1,1},{-1,2},{0,-1},{0,0},{0,1},{0,2},{1,-1},{1,0},{1,1},{1,2},{2,0},{2,1}};
map<pair<int,int>,int> SI,FI;
int pow3s[20];
int gettr(uint32_t s,int i){return (s/pow3s[i])%3;}
uint32_t settr(uint32_t s,int i,int v){int o=gettr(s,i); return s+(v-o)*pow3s[i];}
vector<int> neigh_idx_sc(P c){vector<int> r;for(auto d:dirs){auto it=SI.find({c.x+d.x,c.y+d.y});if(it!=SI.end())r.push_back(it->second);}return r;}
struct Label{int kind; P a,b;}; // kind 0 CO,1 O2
vector<Label> labels={
{0,{0,0},{0,0}}, {1,{-1,1},{0,1}}, {0,{0,1},{0,0}}, {0,{1,0},{0,0}},
{1,{-1,0},{-1,1}}, {1,{0,0},{0,1}}, {0,{-1,1},{0,0}}, {1,{-1,0},{0,0}},
{0,{-1,0},{0,0}}, {1,{0,0},{1,0}}
};
vector<vector<pair<uint32_t,int>>> trans_cache; vector<char> trans_done;
vector<pair<uint32_t,int>> trans(uint32_t s,int li){
  uint64_t key=(uint64_t)s*10+li;
  static unordered_map<uint64_t, vector<pair<uint32_t,int>>> memo;
  auto it=memo.find(key); if(it!=memo.end()) return it->second;
  Label L=labels[li]; map<uint32_t,int> out;
  if(L.kind==0){
    int i=SI[{L.a.x,L.a.y}];
    if(gettr(s,i)!=0){out[s]+=72;}
    else{
      uint32_t a=settr(s,i,1); vector<int> os;
      for(int q:neigh_idx_sc(L.a)) if(gettr(a,q)==2) os.push_back(q);
      if(os.empty()) out[a]+=72;
      else {int w=72/(int)os.size(); for(int q:os){uint32_t t=settr(a,i,0);t=settr(t,q,0);out[t]+=w;}}
    }
  }else{
    int ia=SI[{L.a.x,L.a.y}], ib=SI[{L.b.x,L.b.y}];
    if(gettr(s,ia)!=0||gettr(s,ib)!=0) out[s]+=36;
    else{
      uint32_t a=settr(settr(s,ia,2),ib,2); vector<int> ca,cb;
      for(int q:neigh_idx_sc(L.a)) if(gettr(a,q)==1) ca.push_back(q);
      for(int q:neigh_idx_sc(L.b)) if(gettr(a,q)==1) cb.push_back(q);
      if(ca.empty()) ca.push_back(-1); if(cb.empty()) cb.push_back(-1);
      int w=36/((int)ca.size()*(int)cb.size());
      for(int qa:ca)for(int qb:cb){uint32_t t=a; if(qa!=-1){t=settr(t,ia,0);t=settr(t,qa,0);} if(qb!=-1){t=settr(t,ib,0);t=settr(t,qb,0);} out[t]+=w;}
    }
  }
  vector<pair<uint32_t,int>> v(out.begin(),out.end()); memo.emplace(key,v); return v;
}
vector<unordered_map<uint32_t,cpp_int>> memoA(9);
bool target(uint32_t s){
  for(auto c: vector<P>{{-1,0},{-1,1},{0,0},{0,1},{1,0},{1,1}}){auto it=SI.find({c.x,c.y}); if(it==SI.end()||gettr(s,it->second)!=0)return false;} return true;
}
cpp_int A(int n,uint32_t s){
  auto &M=memoA[n]; auto it=M.find(s); if(it!=M.end())return it->second;
  cpp_int z;
  if(n==0) z=target(s)?1:0;
  else for(int li=0;li<10;li++) for(auto [t,w]:trans(s,li)) z += cpp_int(w)*A(n-1,t);
  M.emplace(s,z); return z;
}
cpp_int ipow(cpp_int a,int n){cpp_int r=1;while(n--)r*=a;return r;}
cpp_int fact(int n){cpp_int r=1;for(int i=2;i<=n;i++)r*=i;return r;}
string sstr(cpp_int x){return x.convert_to<string>();}
int main(){
  pow3s[0]=1;for(int i=1;i<20;i++)pow3s[i]=pow3s[i-1]*3;
  for(int i=0;i<(int)SC.size();i++)SI[{SC[i].x,SC[i].y}]=i;
  for(int i=0;i<(int)CEL.size();i++)FI[{CEL[i].x,CEL[i].y}]=i;
  vector<int> var; set<pair<int,int>> fixed={{-1,0},{-1,1}};
  for(int i=0;i<(int)CEL.size();i++) if(!fixed.count({CEL[i].x,CEL[i].y})) var.push_back(i);
  long long total=1;for(size_t i=0;i<var.size();i++)total*=3;
  unordered_set<uint32_t> initset; long long full=0;
  vector<int> vals(CEL.size(),0);
  for(long long code=0;code<total;code++){
    long long z=code; for(int i:var){vals[i]=z%3;z/=3;} for(int i=0;i<(int)CEL.size();i++) if(fixed.count({CEL[i].x,CEL[i].y})) vals[i]=0;
    bool ok=true; for(int i=0;i<(int)CEL.size()&&ok;i++){
      P c=CEL[i]; int a=vals[i];
      for(auto d: vector<P>{{1,0},{0,1}}){auto it=FI.find({c.x+d.x,c.y+d.y}); if(it!=FI.end()){int b=vals[it->second]; if((a==1&&b==2)||(a==2&&b==1)){ok=false;break;}}}
    }
    if(!ok)continue; full++;
    uint32_t s=0; for(int i=0;i<(int)SC.size();i++){int v=vals[FI[{SC[i].x,SC[i].y}]];s+=v*pow3s[i];} initset.insert(s);
  }
  cerr<<"full "<<full<<" desc "<<initset.size()<<"\n";
  if(full!=215383||initset.size()!=48027) return 2;
  vector<cpp_int> mins(5); bool first=true;
  for(int n=0;n<=4;n++){
    first=true; for(auto s:initset){cpp_int v=A(n,s); if(first||v<mins[n]){mins[n]=v;first=false;}}
  }
  if(mins[0]!=0||mins[1]!=0||mins[2]!=0||mins[3]!=0||mins[4]!=12109824) return 3;
  int N=8,D=140,H=36*D; cpp_int F=fact(N), den=F*ipow(cpp_int(H),N);
  int best=0; cpp_int best_num=0,best_den=1;
  for(int lam=1;lam<=8;lam++){
    bool fst=true; cpp_int mn=0;
    for(auto s:initset){
      cpp_int sum=0;
      for(int n=0;n<=N;n++){
        cpp_int coeff=ipow(cpp_int(lam),n)*(F/fact(n))*ipow(cpp_int(H),N-n);
        sum += coeff*A(n,s);
      }
      if(fst||sum<mn){mn=sum;fst=false;}
    }
    cpp_int num=ipow(cpp_int(32),lam)*mn;
    cpp_int de=ipow(cpp_int(87),lam)*den;
    if(best==0 || num*best_den>best_num*de){best=lam;best_num=num;best_den=de;}
    cerr<<"lam "<<lam<<" done\n";
  }
  if(best!=4) return 4;
  cpp_int en=cpp_int("449855540637605888"), ed=cpp_int("88875222725965541291015625");
  if(best_num*ed!=en*best_den) return 5;
  cout<<"PASS exact one-column DP\n";
  cout<<"full="<<full<<" descriptors="<<initset.size()<<" minA4="<<mins[4]<<" best_lambda="<<best<<"\n";
  cout<<"p_exact=449855540637605888/88875222725965541291015625\n";
  return 0;
}
