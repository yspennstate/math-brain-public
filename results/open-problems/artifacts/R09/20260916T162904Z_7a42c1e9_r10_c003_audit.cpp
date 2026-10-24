#include <boost/multiprecision/cpp_int.hpp>
#include <unordered_map>
#include <vector>
#include <iostream>
#include <string>
using namespace std; using boost::multiprecision::cpp_int;
static inline vector<int> decode(uint64_t code,int w){vector<int>a(w);for(int i=0;i<w;i++)a[i]=(code>>(4*i))&15;return a;}
static inline uint64_t encode(const vector<int>&a){uint64_t c=0;for(int i=0;i<(int)a.size();i++)c|=(uint64_t)a[i]<<(4*i);return c;}
static inline uint64_t canon(vector<int>a){int mp[16]={0},next=1;for(int &z:a){if(z==0)continue;if(!mp[z])mp[z]=next++;z=mp[z];}return encode(a);}
static inline bool replace_closed(uint64_t code,int w,int j,uint64_t &out){auto a=decode(code,w);int old=a[j],mx=0;for(int z:a)mx=max(mx,z);a[j]=mx+1;if(old==0){bool any=false;for(int z:a)if(z==0){any=true;break;}if(!any)return false;}out=canon(a);return true;}
static inline uint64_t merge_slots(uint64_t code,int w,int i,int j){auto a=decode(code,w);int x=a[i],y=a[j];if(x==y)return code;int keep,kill;if(x==0||y==0){keep=0;kill=(x==0?y:x);}else{keep=min(x,y);kill=max(x,y);}for(int &z:a)if(z==kill)z=keep;return canon(a);}
pair<cpp_int,int> calc(int n){int w=n+1;unordered_map<uint64_t,cpp_int>D,E;vector<int> init(w,0);D[encode(init)]=1;int edges=0;for(int col=1;col<=2*n;col++){for(int j=0;j<w;j++){E.clear();E.reserve(D.size()*2+8);for(auto &kv:D){E[kv.first]+=kv.second;uint64_t t;if(replace_closed(kv.first,w,j,t))E[t]+=kv.second;}D.swap(E);edges++;if(j>0){E.clear();E.reserve(D.size()*2+8);for(auto &kv:D){E[kv.first]+=kv.second;uint64_t t=merge_slots(kv.first,w,j-1,j);E[t]+=kv.second;}D.swap(E);edges++;}}}cpp_int num=0;for(auto &kv:D)num+=kv.second;cerr<<"n="<<n<<" states="<<D.size()<<" edges="<<edges<<"\n";return {num,edges};}
cpp_int parse(const string&s){cpp_int x=0;for(char c:s)if(isdigit(c)){x*=10;x+=c-'0';}return x;}
int main(){struct E{int n;const char*num;const char*den;};E ex[]={{7,"190412956947279112493363607761924047154705129959550148139281","803469022129495137770981046170581301261101496891396417650688"},{8,"3401168741170800499782725821825429379121670909466793138845105826881363208183761","14821387422376473014217086081112052205218558037201992197050570753012880593911808"},{9,"489050884538050680474242020538103107795573977403288337801839028539008251265699201462979829980308697","2187250724783011924372502227117621365353169430893212436425770606409952999199375923223513177023053824"}};for(auto z:ex){auto [num,e]=calc(z.n);cpp_int den=cpp_int(1)<<e;cpp_int en=parse(z.num),ed=parse(z.den);if(num*ed!=en*den){cerr<<"MISMATCH n="<<z.n<<"\n";return 2;}cout<<"n="<<z.n<<" exact_fraction_match=TRUE edges="<<e<<"\n";}cout<<"PASS\n";}
