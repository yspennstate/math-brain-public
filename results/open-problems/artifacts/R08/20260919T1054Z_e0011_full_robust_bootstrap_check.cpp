#include <bits/stdc++.h>
#include <boost/multiprecision/cpp_int.hpp>
using namespace std; using boost::multiprecision::cpp_int; using u128=unsigned __int128;
struct Pt{int x,y; bool operator<(Pt const&o)const{return tie(x,y)<tie(o.x,o.y);} bool operator==(Pt const&o)const{return x==o.x&&y==o.y;}};
struct Lab{int k; Pt a,b;};
vector<Pt>P,Core; map<pair<int,int>,int> PI,CI; vector<unsigned long long>P3; vector<Lab>Old,New; int TI[6]; vector<int> corePI; vector<pair<int,int>> pedges;
int gv(uint64_t s,int i){return (s/P3[i])%3;} uint64_t sv(uint64_t s,int i,int v){return s+(long long)(v-gv(s,i))*P3[i];}
set<Pt> nb(Pt p){return {{p.x+1,p.y},{p.x-1,p.y},{p.x,p.y+1},{p.x,p.y-1}};}
vector<int> niP(Pt p){vector<int>r;for(auto q:nb(p)){auto it=PI.find({q.x,q.y});if(it!=PI.end())r.push_back(it->second);}return r;}
bool adj(Pt a,Pt b){return abs(a.x-b.x)+abs(a.y-b.y)==1;}
bool insideP(Pt p){return PI.count({p.x,p.y});}
bool suppcoP(Pt p){if(!insideP(p))return false;for(auto q:nb(p))if(!insideP(q))return false;return true;}
bool suppoP(Pt a,Pt b){if(!insideP(a)||!insideP(b)||!adj(a,b))return false;for(auto q:nb(a))if(!insideP(q))return false;for(auto q:nb(b))if(!insideP(q))return false;return true;}
uint64_t embedCore(uint64_t cs, const array<int,4>& bv){uint64_t s=0; for(int i=0;i<(int)Core.size();i++){int v=(cs/P3[i])%3; s+=P3[corePI[i]]*v;} int ei[4]={PI[{0,-2}],PI[{0,3}],PI[{1,2}],PI[{2,1}]}; for(int j=0;j<4;j++)s+=P3[ei[j]]*bv[j]; return s;}
uint64_t projCore(uint64_t ps){uint64_t c=0;for(int i=0;i<(int)Core.size();i++)c+=P3[i]*gv(ps,corePI[i]);return c;}
bool stableFast(uint64_t s){for(auto [i,j]:pedges){int a=gv(s,i),b=gv(s,j);if((a==1&&b==2)||(a==2&&b==1))return false;}return true;}
bool targetC(uint64_t cs){for(int i:TI)if((cs/P3[i])%3)return false;return true;}
u128 labelSum(uint64_t s, const Lab& l, const function<u128(uint64_t)>& F){
 if(!l.k){int i=PI[{l.a.x,l.a.y}]; if(gv(s,i))return (u128)72*F(projCore(s)); auto a=sv(s,i,1); int os[4],k=0;for(int q:niP(l.a))if(gv(a,q)==2)os[k++]=q; if(!k)return (u128)72*F(projCore(a)); int w=72/k;u128 z=0;for(int t=0;t<k;t++)z+=(u128)w*F(projCore(sv(sv(a,i,0),os[t],0)));return z;
 } else {int u=PI[{l.a.x,l.a.y}],v=PI[{l.b.x,l.b.y}]; if(gv(s,u)||gv(s,v))return (u128)36*F(projCore(s)); auto a=sv(sv(s,u,2),v,2); int cu[5],cv[5],ku=0,kv=0;for(int q:niP(l.a))if(gv(a,q)==1)cu[ku++]=q;for(int q:niP(l.b))if(gv(a,q)==1)cv[kv++]=q;if(!ku)cu[ku++]=-1;if(!kv)cv[kv++]=-1;int d=ku*kv,w=36/d;u128 z=0;for(int iu=0;iu<ku;iu++)for(int iv=0;iv<kv;iv++){auto t=a;if(cu[iu]>=0)t=sv(sv(t,u,0),cu[iu],0);if(cv[iv]>=0)t=sv(sv(t,v,0),cv[iv],0);z+=(u128)w*F(projCore(t));}return z; }
}
unordered_map<uint64_t,u128> OM[9], RM[9];
u128 O(int n,uint64_t cs){auto &m=OM[n];auto it=m.find(cs);if(it!=m.end())return it->second;if(!n){u128 z=targetC(cs);m.emplace(cs,z);return z;}array<int,4>b={0,0,0,0};uint64_t ps=embedCore(cs,b);u128 z=0;auto f=[&](uint64_t t){return O(n-1,t);};for(auto &l:Old)z+=labelSum(ps,l,f);m.emplace(cs,z);return z;}
u128 R(int n,uint64_t cs){auto &m=RM[n];auto it=m.find(cs);if(it!=m.end())return it->second;if(!n){u128 z=targetC(cs);m.emplace(cs,z);return z;}array<int,4>b0={0,0,0,0};uint64_t ps0=embedCore(cs,b0);u128 oldsum=0;auto fr=[&](uint64_t t){return R(n-1,t);};for(auto &l:Old)oldsum+=labelSum(ps0,l,fr);u128 best=~(u128)0;bool any=false;for(int code=0;code<81;code++){int q=code;array<int,4>b;for(int j=0;j<4;j++){b[j]=q%3;q/=3;}uint64_t ps=embedCore(cs,b);if(!stableFast(ps))continue;any=true;u128 z=0;for(auto &l:New)z+=labelSum(ps,l,fr);if(z<best)best=z;}if(!any){cerr<<"no ext\n";exit(8);}u128 z=oldsum+best;m.emplace(cs,z);return z;}
string s128(u128 x){if(!x)return"0";string s;while(x){s.push_back('0'+x%10);x/=10;}reverse(s.begin(),s.end());return s;}
int main(){vector<pair<int,int>> core={{-2,0},{-2,1},{-1,-1},{-1,0},{-1,1},{-1,2},{0,-1},{0,0},{0,1},{0,2},{1,-1},{1,0},{1,1},{2,0}};vector<pair<int,int>> extras={{0,-2},{0,3},{1,2},{2,1}};for(auto[x,y]:core)Core.push_back({x,y});sort(Core.begin(),Core.end());vector<pair<int,int>> pp=core;for(auto e:extras)pp.push_back(e);sort(pp.begin(),pp.end());pp.erase(unique(pp.begin(),pp.end()),pp.end());for(auto[x,y]:pp)P.push_back({x,y});for(int i=0;i<(int)P.size();i++)PI[{P[i].x,P[i].y}]=i;for(int i=0;i<(int)Core.size();i++)CI[{Core[i].x,Core[i].y}]=i;P3.resize(30);P3[0]=1;for(int i=1;i<30;i++)P3[i]=P3[i-1]*3ULL;for(auto p:Core)corePI.push_back(PI[{p.x,p.y}]);for(int i=0;i<(int)P.size();i++)for(int j=i+1;j<(int)P.size();j++)if(adj(P[i],P[j]))pedges.push_back({i,j});
 set<pair<int,int>> BC(core.begin(),core.end()); auto inC=[&](Pt p){return BC.count({p.x,p.y});}; auto sco=[&](Pt p){if(!inC(p))return false;for(auto q:nb(p))if(!inC(q))return false;return true;}; auto so2=[&](Pt a,Pt b){if(!inC(a)||!inC(b)||!adj(a,b))return false;for(auto q:nb(a))if(!inC(q))return false;for(auto q:nb(b))if(!inC(q))return false;return true;};for(auto p:P)if(sco(p))Old.push_back({0,p,{0,0}});set<pair<Pt,Pt>>seen;for(auto p:P)for(auto q:nb(p)){Pt a=p,b=q;if(b<a)swap(a,b);if(seen.insert({a,b}).second&&so2(a,b))Old.push_back({1,a,b});}vector<Lab>All;for(auto p:P)if(suppcoP(p))All.push_back({0,p,{0,0}});seen.clear();for(auto p:P)for(auto q:nb(p)){Pt a=p,b=q;if(b<a)swap(a,b);if(seen.insert({a,b}).second&&suppoP(a,b))All.push_back({1,a,b});}auto same=[](Lab u,Lab v){return u.k==v.k&&u.a==v.a&&(u.k==0||u.b==v.b);};for(auto a:All){bool old=false;for(auto b:Old)if(same(a,b)){old=true;break;}if(!old)New.push_back(a);}cerr<<"labels "<<Old.size()<<" "<<New.size()<<" edges "<<pedges.size()<<"\n";
 vector<pair<int,int>> targ={{-1,0},{-1,1},{0,0},{0,1},{1,0},{1,1}};for(int j=0;j<6;j++)TI[j]=CI[targ[j]];
 set<pair<int,int>> fixed={{-1,0},{-1,1}};vector<int>var;for(int i=0;i<(int)Core.size();i++)if(!fixed.count({Core[i].x,Core[i].y}))var.push_back(i);vector<uint64_t> init; long long tot=1;for(int _:var)tot*=3;for(long long code=0;code<tot;code++){long long q=code;uint64_t cs=0;for(int i:var){int v=q%3;q/=3;cs+=P3[i]*v;}bool ok=true;for(int i=0;i<(int)Core.size()&&ok;i++){int a=(cs/P3[i])%3;if(!a)continue;for(int j=i+1;j<(int)Core.size();j++)if(adj(Core[i],Core[j])){int b=(cs/P3[j])%3;if((a==1&&b==2)||(a==2&&b==1)){ok=false;break;}}}if(ok)init.push_back(cs);}cerr<<"init projected "<<init.size()<<"\n";
 if(init.size()!=48027||Old.size()!=10||New.size()!=7){cerr<<"frozen counts fail\n";return 10;}
 int N=8,D=140,H=36*D,lam=4;auto ip=[](cpp_int a,int n){cpp_int r=1;while(n--)r*=a;return r;};cpp_int fact[9];fact[0]=1;for(int n=1;n<=N;n++)fact[n]=fact[n-1]*n;cpp_int FF=fact[N];vector<cpp_int>coef(N+1);for(int n=0;n<=N;n++)coef[n]=ip(cpp_int(lam),n)*(FF/fact[n])*ip(cpp_int(H),N-n);
 auto polyO=[&](uint64_t cs){cpp_int z=0;for(int n=0;n<=N;n++)z+=cpp_int(s128(O(n,cs)))*coef[n];return z;};
 auto polyR=[&](uint64_t cs){cpp_int z=0;for(int n=0;n<=N;n++)z+=cpp_int(s128(R(n,cs)))*coef[n];return z;};
 vector<pair<cpp_int,uint64_t>> rank;rank.reserve(init.size());for(auto cs:init)rank.push_back({polyO(cs),cs});sort(rank.begin(),rank.end(),[](auto const&a,auto const&b){return a.first<b.first;});
 if(rank[0].second!=4782752ULL || rank[0].first!=cpp_int("4642311559640512826443825152")){cerr<<"old min changed\n";return 11;}
 cpp_int firstCut=polyR(rank[0].second); vector<pair<cpp_int,uint64_t>> cand; for(auto const&r:rank){ if(r.first>=firstCut) break; cand.push_back(r);} cerr<<"firstCut "<<firstCut<<" candidates "<<cand.size()<<"\n";
 cpp_int rMin;uint64_t rArg=0;bool first=true;for(size_t idx=0;idx<cand.size();idx++){cpp_int z=polyR(cand[idx].second);if(first||z<rMin){first=false;rMin=z;rArg=cand[idx].second;} if((idx+1)%10==0) cerr<<"done "<<idx+1<<"/"<<cand.size()<<"\n";}
 if(rMin>firstCut){cerr<<"impossible min>cut\n";return 12;} if(cand.size()<rank.size() && rank[cand.size()].first<rMin){cerr<<"branch-bound failure\n";return 13;}
 cpp_int f1Min("7492177630527378997219688448"); if(!(rMin>f1Min)){cerr<<"no strict gain over F1\n";return 14;}
 cout<<"PASS exact R08/E0011 unrestricted robust-bootstrap certificate\n";
 cout<<"projected_descriptors="<<init.size()<<" old_labels="<<Old.size()<<" halo_labels="<<New.size()<<" D="<<D<<" lambda="<<lam<<"\n";
 cout<<"old_poly_min="<<rank[0].first<<" old_arg="<<rank[0].second<<"\n";
 cout<<"unrestricted_at_old_arg="<<firstCut<<" candidates_below_cutoff="<<cand.size(); if(cand.size()<rank.size()) cout<<" next_old_poly="<<rank[cand.size()].first; cout<<"\n";
 cout<<"unrestricted_poly_min="<<rMin<<" unrestricted_arg="<<rArg<<"\n";
 cout<<"unrestricted_arg_Rn="; for(int n=0;n<=N;n++) cout<<s128(R(n,rArg))<<(n<N?",":"\n");
 cout<<"previous_F1_poly_min="<<f1Min<<"\n";
 cout<<"gain_over_F1_num="<<rMin<<" gain_over_F1_den="<<f1Min<<"\n";
 cout<<"RM_cache_sizes="; for(int n=0;n<=8;n++)cout<<RM[n].size()<<(n<8?",":"\n");
}
