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
unordered_map<uint64_t,u128> OM[9],FM[9];
u128 O(int n,uint64_t cs){auto &m=OM[n];auto it=m.find(cs);if(it!=m.end())return it->second;if(!n){u128 z=targetC(cs);m.emplace(cs,z);return z;}array<int,4>b={0,0,0,0};uint64_t ps=embedCore(cs,b);u128 z=0;auto f=[&](uint64_t t){return O(n-1,t);};for(auto &l:Old)z+=labelSum(ps,l,f);m.emplace(cs,z);return z;}
u128 F1(int n,uint64_t cs){auto &m=FM[n];auto it=m.find(cs);if(it!=m.end())return it->second;if(!n){u128 z=targetC(cs);m.emplace(cs,z);return z;}array<int,4>b0={0,0,0,0};uint64_t ps0=embedCore(cs,b0);u128 oldsum=0;auto ff=[&](uint64_t t){return F1(n-1,t);};for(auto &l:Old)oldsum+=labelSum(ps0,l,ff);u128 best=~(u128)0;bool any=false;for(int code=0;code<81;code++){int q=code;array<int,4>b;for(int j=0;j<4;j++){b[j]=q%3;q/=3;}uint64_t ps=embedCore(cs,b);if(!stableFast(ps))continue;any=true;u128 z=0;auto fo=[&](uint64_t t){return O(n-1,t);};for(auto &l:New)z+=labelSum(ps,l,fo);if(z<best)best=z;}if(!any){cerr<<"no ext\n";exit(8);}u128 z=oldsum+best;m.emplace(cs,z);return z;}
string s128(u128 x){if(!x)return"0";string s;while(x){s.push_back('0'+x%10);x/=10;}reverse(s.begin(),s.end());return s;}
int main(){vector<pair<int,int>> core={{-2,0},{-2,1},{-1,-1},{-1,0},{-1,1},{-1,2},{0,-1},{0,0},{0,1},{0,2},{1,-1},{1,0},{1,1},{2,0}};vector<pair<int,int>> extras={{0,-2},{0,3},{1,2},{2,1}};for(auto[x,y]:core)Core.push_back({x,y});sort(Core.begin(),Core.end());vector<pair<int,int>> pp=core;for(auto e:extras)pp.push_back(e);sort(pp.begin(),pp.end());pp.erase(unique(pp.begin(),pp.end()),pp.end());for(auto[x,y]:pp)P.push_back({x,y});for(int i=0;i<(int)P.size();i++)PI[{P[i].x,P[i].y}]=i;for(int i=0;i<(int)Core.size();i++)CI[{Core[i].x,Core[i].y}]=i;P3.resize(30);P3[0]=1;for(int i=1;i<30;i++)P3[i]=P3[i-1]*3ULL;for(auto p:Core)corePI.push_back(PI[{p.x,p.y}]);for(int i=0;i<(int)P.size();i++)for(int j=i+1;j<(int)P.size();j++)if(adj(P[i],P[j]))pedges.push_back({i,j});
 set<pair<int,int>> BC(core.begin(),core.end()); auto inC=[&](Pt p){return BC.count({p.x,p.y});}; auto sco=[&](Pt p){if(!inC(p))return false;for(auto q:nb(p))if(!inC(q))return false;return true;}; auto so2=[&](Pt a,Pt b){if(!inC(a)||!inC(b)||!adj(a,b))return false;for(auto q:nb(a))if(!inC(q))return false;for(auto q:nb(b))if(!inC(q))return false;return true;};for(auto p:P)if(sco(p))Old.push_back({0,p,{0,0}});set<pair<Pt,Pt>>seen;for(auto p:P)for(auto q:nb(p)){Pt a=p,b=q;if(b<a)swap(a,b);if(seen.insert({a,b}).second&&so2(a,b))Old.push_back({1,a,b});}vector<Lab>All;for(auto p:P)if(suppcoP(p))All.push_back({0,p,{0,0}});seen.clear();for(auto p:P)for(auto q:nb(p)){Pt a=p,b=q;if(b<a)swap(a,b);if(seen.insert({a,b}).second&&suppoP(a,b))All.push_back({1,a,b});}auto same=[](Lab u,Lab v){return u.k==v.k&&u.a==v.a&&(u.k==0||u.b==v.b);};for(auto a:All){bool old=false;for(auto b:Old)if(same(a,b)){old=true;break;}if(!old)New.push_back(a);}cerr<<"labels "<<Old.size()<<" "<<New.size()<<" edges "<<pedges.size()<<"\n";
 vector<pair<int,int>> targ={{-1,0},{-1,1},{0,0},{0,1},{1,0},{1,1}};for(int j=0;j<6;j++)TI[j]=CI[targ[j]];
 vector<pair<int,int>> CEL={{-2,0},{-2,1},{-1,-1},{-1,0},{-1,1},{-1,2},{0,-1},{0,0},{0,1},{0,2},{1,-1},{1,0},{1,1},{1,2},{2,0},{2,1}};map<pair<int,int>,int> EI;for(int i=0;i<(int)CEL.size();i++)EI[CEL[i]]=i;set<pair<int,int>> fixed={{-1,0},{-1,1}};vector<int>var;for(int i=0;i<(int)CEL.size();i++)if(!fixed.count(CEL[i]))var.push_back(i);vector<uint64_t> init; long long full=0,tot=1;for(int _:var)tot*=3;unordered_set<uint64_t> us;for(long long code=0;code<tot;code++){long long q=code;vector<int>x(CEL.size(),0);for(int i:var){x[i]=q%3;q/=3;}bool ok=true;for(int i=0;i<(int)CEL.size()&&ok;i++)for(auto d:vector<pair<int,int>>{{1,0},{0,1}}){auto it=EI.find({CEL[i].first+d.first,CEL[i].second+d.second});if(it!=EI.end()&&((x[i]==1&&x[it->second]==2)||(x[i]==2&&x[it->second]==1))){ok=false;break;}}if(!ok)continue;full++;uint64_t cs=0;for(int i=0;i<(int)Core.size();i++)cs+=P3[i]*x[EI[{Core[i].x,Core[i].y}]];us.insert(cs);}init.assign(us.begin(),us.end());cerr<<"init "<<full<<" "<<init.size()<<"\n";
 if(full!=215383||init.size()!=48027||Old.size()!=10||New.size()!=7){cerr<<"frozen counts fail\n";return 10;}
 int N=8,D=140,H=36*D,lam=4;auto ip=[](cpp_int a,int n){cpp_int r=1;while(n--)r*=a;return r;};cpp_int fact[9];fact[0]=1;for(int n=1;n<=N;n++)fact[n]=fact[n-1]*n;cpp_int FF=fact[N];vector<cpp_int>coef(N+1);for(int n=0;n<=N;n++)coef[n]=ip(cpp_int(lam),n)*(FF/fact[n])*ip(cpp_int(H),N-n);
 vector<pair<cpp_int,uint64_t>> rank;rank.reserve(init.size());for(auto cs:init){cpp_int z=0;for(int n=0;n<=N;n++)z+=cpp_int(s128(O(n,cs)))*coef[n];rank.push_back({z,cs});}sort(rank.begin(),rank.end(),[](auto const&a,auto const&b){return a.first<b.first;});
 cpp_int oldMin=rank[0].first;uint64_t oldArg=rank[0].second;if(oldArg!=4782752ULL){cerr<<"old arg changed\n";return 11;}
 auto polyF=[&](uint64_t cs){cpp_int z=0;for(int n=0;n<=N;n++)z+=cpp_int(s128(F1(n,cs)))*coef[n];return z;};
 cpp_int cutoff=polyF(oldArg);vector<pair<cpp_int,uint64_t>> cand;for(auto const&r:rank){if(r.first>=cutoff)break;cand.push_back(r);}if(cand.size()!=16){cerr<<"candidate count "<<cand.size()<<"\n";return 12;}
 cpp_int fMin;uint64_t fArg=0;bool first=true;for(auto const&r:cand){cpp_int z=polyF(r.second);if(first||z<fMin){first=false;fMin=z;fArg=r.second;}}
 if(fArg!=oldArg||fMin!=cutoff){cerr<<"robust minimizer changed\n";return 13;}if(rank[16].first< fMin){cerr<<"branch bound gap fail\n";return 14;}
 cpp_int eNum=ip(cpp_int(32),lam),eDen=ip(cpp_int(87),lam);cpp_int commonDen=eDen*FF*ip(cpp_int(H),N);cpp_int oldNum=eNum*oldMin,newNum=eNum*fMin;cpp_int archivedN("449855540637605888"),archivedD("88875222725965541291015625");if(oldNum*archivedD!=archivedN*commonDen){cerr<<"archive mismatch\n";return 15;}
 cpp_int g13n("34717319668318843590202198742697856944700233990464479"),g13d("34245904058199771001461521651828906250000000000000000");if(!(fMin*g13d>oldMin*g13n)){cerr<<"no metric gain over current bootstrap\n";return 16;}
 cout<<"PASS exact R08/E0011 robust-bootstrap branch-and-bound certificate\n";
 cout<<"entrance_full="<<full<<" descriptors="<<init.size()<<" old_labels="<<Old.size()<<" halo_labels="<<New.size()<<" D="<<D<<" lambda="<<lam<<"\n";
 cout<<"old_poly_min="<<oldMin<<" old_arg="<<oldArg<<"\n";
 cout<<"first_robust_cutoff="<<cutoff<<" candidates_below_cutoff="<<cand.size()<<" next_old_poly="<<rank[16].first<<"\n";
 cout<<"robust_one_new_poly_min="<<fMin<<" robust_arg="<<fArg<<"\n";
 cout<<"new_over_old_poly_num="<<fMin<<" new_over_old_poly_den="<<oldMin<<"\n";
 cout<<"new_probability_num_unsimplified="<<newNum<<" new_probability_den_unsimplified="<<commonDen<<"\n";
 cout<<"old_archive_match=YES\nnew_gt_current_87_over_20_bootstrap=YES\n";
 cout<<"gain_vs_current_num_unsimplified="<<(fMin*g13d)<<"\n"<<"gain_vs_current_den_unsimplified="<<(oldMin*g13n)<<"\n";
}
