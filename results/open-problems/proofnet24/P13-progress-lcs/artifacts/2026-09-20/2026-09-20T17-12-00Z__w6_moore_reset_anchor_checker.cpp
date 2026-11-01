#include <bits/stdc++.h>
#include <boost/multiprecision/cpp_int.hpp>
using namespace std; using u128=unsigned __int128; using boost::multiprecision::cpp_int;
static string S(u128 x){if(!x)return"0";string s;while(x){s.push_back(char('0'+x%10));x/=10;}reverse(s.begin(),s.end());return s;}
static cpp_int CI(u128 x){cpp_int z=(uint64_t)(x>>64);z<<=64;z+=(uint64_t)x;return z;}
static inline uint32_t step_state(uint32_t state,int uv,int w){int m=2*w;uint32_t mask=(1u<<m)-1,x=state&mask,g=(state>>m)&mask;int u=(uv>>1)&1,v=uv&1,c[32];c[0]=0;for(int i=1;i<=m;i++){int gi=(g>>(i-1))&1,xi=(x>>(i-1))&1;c[i]=(1-gi)*(c[i-1]||(xi==v));}uint32_t gp=0;for(int i=1;i<m;i++){int z=((g>>i)&1)+c[i+1]-c[i];if(z)gp|=1u<<(i-1);}if((1-c[m])*(u==v))gp|=1u<<(m-1);uint32_t xp=(x>>1)|(uint32_t(u)<<(m-1));return xp|(gp<<m);}
static inline uint32_t canon(uint32_t s,int w){int m=2*w;uint32_t mask=(1u<<m)-1,x=s&mask,g=(s>>m)&mask;int l=0;while(l<m&&((g>>l)&1u))l++;if(l)x&=~((1u<<l)-1u);return x|(g<<m);}
struct QNode{uint32_t n[4];uint8_t gm;};
struct Rec{uint32_t a,b,c,d,id;};
static bool cmpRec(const Rec&x,const Rec&y){if(x.a!=y.a)return x.a<y.a;if(x.b!=y.b)return x.b<y.b;if(x.c!=y.c)return x.c<y.c;if(x.d!=y.d)return x.d<y.d;return x.id<y.id;}
static string compw(string s){for(char&c:s){if(c=='A')c='B';else if(c=='B')c='A';else if(c=='C')c='D';else c='C';}return s;}
static vector<string> reset_patterns(int m){set<string> p;p.insert(string(m,'A'));p.insert(string(m,'B'));for(int r=1;r<m;r++){for(char z:string("BCD"))p.insert(string(r,'A')+z+string(m-r,'A'));for(char z:string("ACD"))p.insert(string(r,'B')+z+string(m-r,'B'));}set<string> add;for(int r=1;r<m;r++)for(int s=0;s<m-r;s++){int t=m-r-s;if(t<1)continue;for(char z1:string("BCD"))for(char z2:string("BCD")){bool good=(z1=='C'||z2=='D')||(z1=='D'&&z2=='C')||(z1=='B'&&z2=='C'&&r>=2);if(good)add.insert(string(r,'A')+z1+string(s,'A')+z2+string(t,'A'));}}for(auto&w:add)p.insert(w);for(auto&w:add)p.insert(compw(w));vector<string> v;for(auto&w:p){bool bad=false;for(auto&u:p)if(u!=w&&w.find(u)!=string::npos){bad=true;break;}if(!bad)v.push_back(w);}return v;}
static int code(char c){if(c=='A')return 1;if(c=='B')return 2;if(c=='C')return 0;return 3;}
static uint32_t apply0(const string&w,int half){uint32_t s=0;for(char c:w)s=step_state(s,code(c),half);return s;}
int main(){constexpr int w=6,m=12;const uint32_t BAD=0xffffffffu;size_t total=1ull<<(2*m);vector<uint32_t> seen(total,BAD),states;seen[0]=0;states.push_back(0);states.reserve(5800000);for(size_t h=0;h<states.size();h++)for(int a=0;a<4;a++){auto t=step_state(states[h],a,w);if(seen[t]==BAD){seen[t]=states.size();states.push_back(t);}}
vector<uint32_t> qid(total,BAD),reps;reps.reserve(4500000);for(auto s:states){auto c=canon(s,w);if(qid[c]==BAD){qid[c]=reps.size();reps.push_back(c);}}vector<QNode> Q(reps.size());for(uint32_t i=0;i<reps.size();i++){auto s=reps[i];Q[i].gm=(s>>(2*m-1))&1;for(int a=0;a<4;a++)Q[i].n[a]=qid[canon(step_state(s,a,w),w)];}
auto pats=reset_patterns(m);map<int,int> cnt;for(auto&p:pats)cnt[p.size()]++;
set<string> sync14; const string AL="ABCD";
for(auto &p:pats){int e=14-(int)p.size();for(int left=0;left<=e;left++){int right=e-left;uint64_t np=1ull<<(2*left), ns=1ull<<(2*right);for(uint64_t ip=0;ip<np;ip++)for(uint64_t is=0;is<ns;is++){string pre(left,'A'),suf(right,'A');uint64_t z=ip;for(int j=0;j<left;j++){pre[j]=AL[z&3];z>>=2;}z=is;for(int j=0;j<right;j++){suf[j]=AL[z&3];z>>=2;}sync14.insert(pre+p+suf);}}}
vector<uint32_t> sync14targets;sync14targets.reserve(sync14.size());for(auto &word:sync14)sync14targets.push_back(qid[canon(apply0(word,w),w)]);
cout<<"patterns="<<pats.size();for(auto kv:cnt)cout<<" len"<<kv.first<<"="<<kv.second;cout<<" sync14="<<sync14.size()<<"\n";
seen.clear();seen.shrink_to_fit();states.clear();states.shrink_to_fit();reps.clear();reps.shrink_to_fit();qid.clear();qid.shrink_to_fit();
// Exact output-preserving Moore refinement; stabilization gives the minimal terminal-output automaton.
vector<uint32_t> cls(Q.size()),ncls(Q.size());for(size_t i=0;i<Q.size();i++)cls[i]=Q[i].gm;uint32_t ncprev=2;vector<Rec> rec(Q.size());cout<<"moore_round_0=2\n";int stable=-1;
for(int r=1;r<=30;r++){for(uint32_t i=0;i<Q.size();i++){auto&q=Q[i];rec[i]={cls[q.n[0]],cls[q.n[1]],cls[q.n[2]],cls[q.n[3]],i};}sort(rec.begin(),rec.end(),cmpRec);uint32_t nc=0;for(size_t j=0;j<rec.size();j++){if(j==0||rec[j].a!=rec[j-1].a||rec[j].b!=rec[j-1].b||rec[j].c!=rec[j-1].c||rec[j].d!=rec[j-1].d)nc++;ncls[rec[j].id]=nc-1;}cout<<"moore_round_"<<r<<"="<<nc<<"\n";if(nc==ncprev){stable=r;break;}ncprev=nc;cls.swap(ncls);}
if(stable<0||ncprev!=Q.size()){cerr<<"Moore minimality failure\n";return 2;}cout<<"MOORE_MINIMAL_SHIELD_QUOTIENT_PASS stable_round="<<stable<<" classes="<<ncprev<<"\n";rec.clear();rec.shrink_to_fit();cls.clear();cls.shrink_to_fit();ncls.clear();ncls.shrink_to_fit();
vector<u128> cur(Q.size()),nxt(Q.size());for(size_t i=0;i<Q.size();i++)cur[i]=Q[i].gm;u128 mn=0,mx=0;for(int k=0;k<=64;k++){mn=cur[0];mx=cur[0];for(size_t i=1;i<cur.size();i++){mn=min(mn,cur[i]);mx=max(mx,cur[i]);}if(k==64)break;for(size_t i=0;i<Q.size();i++){auto&q=Q[i];nxt[i]=cur[q.n[0]]+cur[q.n[1]]+cur[q.n[2]]+cur[q.n[3]];}cur.swap(nxt);} 
cpp_int A=0;uint64_t R=sync14targets.size();for(uint32_t qi:sync14targets)A+=CI(cur[qi]);
uint64_t total14=1ull<<28, non=total14-R;cpp_int low=A+cpp_int(non)*CI(mn),up=A+cpp_int(non)*CI(mx),den=(cpp_int(1)<<156);cpp_int width=up-low,oldscaled=CI(mx-mn)*cpp_int(total14),improve=oldscaled-width;
cout<<"mn64="<<S(mn)<<"\nmx64="<<S(mx)<<"\nspread64="<<S(mx-mn)<<"\n";
cout<<"reset_superwords14="<<R<<" nonreset_count14="<<non<<"\n";
cout<<"anchor_A64="<<A<<"\nJ78_event_lower_num="<<low<<"\nJ78_event_upper_num="<<up<<"\nJ78_denom_2pow156="<<den<<"\nJ78_width_num="<<width<<"\nI64_width_scaled="<<oldscaled<<"\nstrict_improvement_num="<<improve<<"\n";
if(R!=1438||width!=cpp_int(non)*CI(mx-mn)||improve!=cpp_int(R)*CI(mx-mn)||improve<=0)return 3;cout<<"RESET_SUPERWORD_ANCHOR_PASS\nALL_EXACT_CHECKS_PASS\n";
}
