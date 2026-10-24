#include <boost/multiprecision/cpp_int.hpp>
#include <algorithm>
#include <iostream>
#include <map>
#include <queue>
#include <string>
#include <unordered_map>
#include <vector>
using namespace std; using boost::multiprecision::cpp_int;

static string canon_new(const vector<int>& comp, const vector<char>& src, int w){
  map<int,unsigned char> lab; unsigned char next=1; string s(w,'\0');
  for(int j=0;j<w;j++){
    int c=comp[w+j]; if(src[c]) s[j]=0;
    else { auto it=lab.find(c); if(it==lab.end()) it=lab.emplace(c,next++).first; s[j]=char(it->second); }
  }
  return s;
}
static map<string,uint64_t> trans(const string& st){
  int w=st.size(), N=2*w, E=2*w-1; map<string,uint64_t> out;
  for(uint64_t mask=0; mask<(1ULL<<E); ++mask){
    vector<vector<int>> g(N);
    auto add=[&](int a,int b){g[a].push_back(b);g[b].push_back(a);};
    for(int i=0;i<w;i++)for(int j=i+1;j<w;j++) if((unsigned char)st[i]==(unsigned char)st[j]) add(i,j);
    for(int j=0;j<w;j++) if(mask>>j&1ULL) add(j,w+j);
    for(int j=0;j<w-1;j++) if(mask>>(w+j)&1ULL) add(w+j,w+j+1);
    vector<int> comp(N,-1); int nc=0;
    for(int z=0;z<N;z++) if(comp[z]<0){ queue<int>q;q.push(z);comp[z]=nc; while(!q.empty()){int u=q.front();q.pop();for(int v:g[u])if(comp[v]<0){comp[v]=nc;q.push(v);}} nc++; }
    vector<char> src(nc,0); for(int i=0;i<w;i++) if((unsigned char)st[i]==0) src[comp[i]]=1;
    bool alive=false; for(int j=0;j<w;j++) if(src[comp[w+j]]) alive=true;
    if(!alive) continue;
    out[canon_new(comp,src,w)]++;
  }
  return out;
}
static pair<cpp_int,cpp_int> solve(int n){
  int w=n+1; string init(w,'\0'); map<string,cpp_int> dp; dp[init]=1; map<string,map<string,uint64_t>> cache;
  for(int col=0;col<2*n;col++){
    map<string,cpp_int> nd;
    for(auto &kv:dp){ auto it=cache.find(kv.first); if(it==cache.end()) it=cache.emplace(kv.first,trans(kv.first)).first; for(auto&t:it->second) nd[t.first]+=kv.second*t.second; }
    dp.swap(nd);
  }
  cpp_int fav=0; for(auto&kv:dp)fav+=kv.second; cpp_int den=cpp_int(1)<<(2*n*(2*n+1)); return {fav,den};
}
static cpp_int gcdx(cpp_int a,cpp_int b){while(b!=0){cpp_int r=a%b;a=b;b=r;}return a;}
int main(){
  vector<string> expected={
    "1/2",
    "48449/131072",
    "5363328171/17179869184",
    "20696232901811649907/73786976294838206464",
    "1321126882225579491309717801203/5070602400912917605986812821504",
    "176191897998719099783873632323748134346583099/713623846352979940529142984724747568191373312"};
  for(int n=1;n<=6;n++){
    auto [a,b]=solve(n); cpp_int g=gcdx(a,b); a/=g;b/=g; string got=a.convert_to<string>()+"/"+b.convert_to<string>();
    if(got!=expected[n-1]){cerr<<"FAIL n="<<n<<" got="<<got<<" exp="<<expected[n-1]<<"\n";return 2;}
    cout<<"n="<<n<<" "<<got<<" PASS\n";
  }
  cout<<"R10-AUDIT-C001 exact independent frontier enumeration: PASS\n";
}
