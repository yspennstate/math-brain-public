#include <bits/stdc++.h>
#include <boost/multiprecision/cpp_int.hpp>
using namespace std; using boost::multiprecision::cpp_int;
struct C{int x,y; bool operator<(C const&o)const{return tie(x,y)<tie(o.x,o.y);} bool operator==(C const&o)const{return x==o.x&&y==o.y;}};
vector<C> dirs={{1,0},{-1,0},{0,1},{0,-1}};
vector<C> STATE={{-2,0},{-2,1},{-1,-1},{-1,0},{-1,1},{-1,2},{0,-1},{0,0},{0,1},{0,2},{1,-1},{1,0},{1,1},{2,0}};
vector<C> FULL={{-2,0},{-2,1},{-1,-1},{-1,0},{-1,1},{-1,2},{0,-1},{0,0},{0,1},{0,2},{1,-1},{1,0},{1,1},{1,2},{2,0},{2,1}};
map<pair<int,int>,int> si,fi; int p3[15];
int getd(int code,int i){return (code/p3[i])%3;} int setd(int code,int i,int v){return code+(v-getd(code,i))*p3[i];}
int enc(const vector<int>&a){int z=0;for(int i=0;i<(int)a.size();++i)z+=a[i]*p3[i];return z;}
bool target(int code){ static int id[]={3,4,7,8,11,12}; for(int i:id) if(getd(code,i)!=0)return false; return true; }
struct Label{int kind; C a,b;}; vector<Label> labv;
vector<pair<int,int>> trans(int code,int li){
 auto L=labv[li]; map<int,int> out;
 if(L.kind==0){int i=si.at({L.a.x,L.a.y}); if(getd(code,i)!=0){out[code]+=72; goto done;} {int c2=setd(code,i,1);vector<int>os;for(auto d:dirs){auto jt=si.find({L.a.x+d.x,L.a.y+d.y});if(jt!=si.end()&&getd(c2,jt->second)==2)os.push_back(jt->second);}if(os.empty()){out[c2]+=72;goto done;}int w=72/(int)os.size();for(int j:os){int t=setd(c2,i,0);t=setd(t,j,0);out[t]+=w;}}}
 else {int ia=si.at({L.a.x,L.a.y}),ib=si.at({L.b.x,L.b.y}); if(getd(code,ia)!=0||getd(code,ib)!=0){out[code]+=36;goto done;} {int c2=setd(setd(code,ia,2),ib,2);vector<int>ca,cb;for(auto d:dirs){auto jt=si.find({L.a.x+d.x,L.a.y+d.y});if(jt!=si.end()&&getd(c2,jt->second)==1)ca.push_back(jt->second);}for(auto d:dirs){auto jt=si.find({L.b.x+d.x,L.b.y+d.y});if(jt!=si.end()&&getd(c2,jt->second)==1)cb.push_back(jt->second);}vector<int>A=ca.empty()?vector<int>{-1}:ca,B=cb.empty()?vector<int>{-1}:cb;int den=A.size()*B.size(),w=36/den;for(int qa:A)for(int qb:B){int t=c2;if(qa!=-1){t=setd(t,ia,0);t=setd(t,qa,0);}if(qb!=-1){t=setd(t,ib,0);t=setd(t,qb,0);}out[t]+=w;}}}
 done:return vector<pair<int,int>>(out.begin(),out.end());
}
bool stable_full(const vector<int>&a){for(int i=0;i<(int)FULL.size();++i){auto c=FULL[i];int av=a[i];for(C d:vector<C>{{1,0},{0,1}}){auto jt=fi.find({c.x+d.x,c.y+d.y});if(jt!=fi.end()){int b=a[jt->second];if((av==1&&b==2)||(av==2&&b==1))return false;}}}return true;}
vector<int> enumerate_inits(set<pair<int,int>> fixed){vector<int>vars;for(int i=0;i<(int)FULL.size();++i)if(!fixed.count({FULL[i].x,FULL[i].y}))vars.push_back(i); long long total=1;for(size_t i=0;i<vars.size();++i)total*=3;unordered_set<int>S;vector<int>a(FULL.size());for(long long mask=0;mask<total;++mask){fill(a.begin(),a.end(),0);long long q=mask;for(int idx:vars){a[idx]=q%3;q/=3;}if(!stable_full(a))continue;vector<int>s(STATE.size());for(int i=0;i<(int)STATE.size();++i)s[i]=a[fi.at({STATE[i].x,STATE[i].y})];S.insert(enc(s));}vector<int>v(S.begin(),S.end());sort(v.begin(),v.end());return v;}
vector<int> closure(const vector<int>&inits,const vector<int>&allowed){unordered_set<int>S(inits.begin(),inits.end());vector<int>front=inits;for(int depth=0;depth<20&&!front.empty();++depth){vector<int>nf;for(int s:front)for(int li:allowed)for(auto [t,w]:trans(s,li))if(S.insert(t).second)nf.push_back(t);front.swap(nf);}vector<int>v(S.begin(),S.end());sort(v.begin(),v.end());return v;}

// Overlap signature for a literal +1 horizontal shift: next coordinate c sees current coordinate c+(1,0).
// Coordinates that land only in the two untracked FULL halo cells are intentionally left unconstrained.
vector<pair<int,int>> overlap_pairs; // (next_state_index,current_state_index)
int sig_next(int t){int k=0,m=1;for(auto [ni,ci]:overlap_pairs){k+=m*getd(t,ni);m*=3;}return k;}
int sig_current(int s){int k=0,m=1;for(auto [ni,ci]:overlap_pairs){k+=m*getd(s,ci);m*=3;}return k;}

struct Stage{string name;int D;vector<int>*inits;vector<int>allowed;};
struct Result{vector<cpp_int> m; vector<vector<cpp_int>> entry; vector<int> inits;};

Result solve_stage(const Stage&st,int N,int H,const Result*next,bool use_relation,bool save_entry){
 vector<int> states=closure(*st.inits,st.allowed);unordered_map<int,int>pos;pos.reserve(states.size()*2);for(int i=0;i<(int)states.size();++i)pos[states[i]]=i;
 vector<vector<pair<int,int>>>edges(states.size());for(int i=0;i<(int)states.size();++i){map<int,int>acc;for(int li:st.allowed)for(auto [t,w]:trans(states[i],li))acc[t]+=w;for(auto [t,w]:acc)edges[i].push_back({pos.at(t),w});}
 vector<int> init_idx;for(int s:*st.inits)init_idx.push_back(pos.at(s)); int nullw=36*(222-st.D);
 vector<unordered_map<int,cpp_int>> relmin; if(next&&use_relation){relmin.resize(N+1);for(int n=0;n<=N;++n){auto &M=relmin[n];M.reserve(next->inits.size()*2);for(size_t k=0;k<next->inits.size();++k){int sg=sig_next(next->inits[k]);const cpp_int&v=next->entry[n][k];auto it=M.find(sg);if(it==M.end()||v<it->second)M[sg]=v;}}}
 auto boundary=[&](int n,int s)->cpp_int{if(!next)return target(s)?cpp_int(1):cpp_int(0); if(!target(s))return cpp_int(0); if(!use_relation)return next->m[n]; int sg=sig_current(s);auto it=relmin[n].find(sg);if(it==relmin[n].end()){cerr<<"EMPTY_RELATION stage="<<st.name<<" n="<<n<<" state="<<s<<" sig="<<sg<<"\n";exit(21);}return it->second;};
 vector<cpp_int>prev(states.size()),cur(states.size());Result R;R.m.resize(N+1);R.inits=*st.inits;if(save_entry)R.entry.assign(N+1,vector<cpp_int>(st.inits->size()));
 for(int i=0;i<(int)states.size();++i)prev[i]=boundary(0,states[i]);
 bool first=true;for(size_t k=0;k<init_idx.size();++k){int i=init_idx[k];if(first||prev[i]<R.m[0]){R.m[0]=prev[i];first=false;}if(save_entry)R.entry[0][k]=prev[i];}
 cerr<<st.name<<" states="<<states.size()<<" rel="<<use_relation<<" entries="<<st.inits->size()<<"\n";
 for(int n=1;n<=N;++n){for(int i=0;i<(int)states.size();++i){if(next&&target(states[i])){cur[i]=boundary(n,states[i]);continue;}cpp_int z=0;if(nullw)z+=cpp_int(nullw)*prev[i];for(auto [j,w]:edges[i])z+=cpp_int(w)*prev[j];cur[i]=z;}first=true;for(size_t k=0;k<init_idx.size();++k){int i=init_idx[k];if(first||cur[i]<R.m[n]){R.m[n]=cur[i];first=false;}if(save_entry)R.entry[n][k]=cur[i];}prev.swap(cur);}
 return R;
}

int main(){int N=40;p3[0]=1;for(int i=1;i<15;++i)p3[i]=p3[i-1]*3;for(int i=0;i<(int)STATE.size();++i)si[{STATE[i].x,STATE[i].y}]=i;for(int i=0;i<(int)FULL.size();++i)fi[{FULL[i].x,FULL[i].y}]=i;
 for(int ni=0;ni<(int)STATE.size();++ni){auto c=STATE[ni];auto it=si.find({c.x+1,c.y});if(it!=si.end())overlap_pairs.push_back({ni,it->second});}
 if(overlap_pairs.size()!=10){cerr<<"bad overlap count\n";return 2;}
 cerr<<"overlap_pairs="<<overlap_pairs.size()<<"\n";for(auto [ni,ci]:overlap_pairs)cerr<<" next("<<STATE[ni].x<<","<<STATE[ni].y<<") <- cur("<<STATE[ci].x<<","<<STATE[ci].y<<")\n";
 labv={{0,{0,0},{}},{1,{-1,1},{0,1}},{0,{0,1},{}},{0,{1,0},{}},{1,{-1,0},{-1,1}},{1,{0,0},{0,1}},{0,{-1,1},{}},{1,{-1,0},{0,0}},{0,{-1,0},{}},{1,{0,0},{1,0}}};
 set<pair<int,int>>fixedbase={{-1,0},{-1,1},{0,0},{0,1}};auto fixedbeh=fixedbase;fixedbeh.insert({-2,0});fixedbeh.insert({-2,1});auto base=enumerate_inits(fixedbase),beh=enumerate_inits(fixedbeh);if(base.size()!=12201||beh.size()!=1743){cerr<<"bad inits\n";return 3;}vector<int>all={0,1,2,3,4,5,6,7,8,9},term={0,1,2,4,5,6,7,8};vector<Stage>st={{"h3",150,&beh,all},{"h4",167,&beh,all},{"h5",178,&beh,all},{"h6",187,&beh,all},{"h7",197,&beh,all},{"h8",201,&beh,term},{"gdown",218,&base,all},{"gup",222,&base,all}};int H=7992;
 // Baseline scalar-reset recursion, exactly the b20_global stage glue.
 Result s7=solve_stage(st[7],N,H,nullptr,false,false); Result s6=solve_stage(st[6],N,H,&s7,false,false); Result s5=solve_stage(st[5],N,H,&s6,false,false); Result s4=solve_stage(st[4],N,H,&s5,false,false); Result s3=solve_stage(st[3],N,H,&s4,false,false); Result s2=solve_stage(st[2],N,H,&s3,false,false); Result s1=solve_stage(st[1],N,H,&s2,false,false); Result s0=solve_stage(st[0],N,H,&s1,false,false);
 if(s0.m[18]!=cpp_int("1335241765123705160600345389301760")) return 4;
 if(s0.m[22]!=cpp_int("21594360744990667130171544797248513823121711562752")) return 5;
 if(s0.m[30]!=cpp_int("3430163092891565906095118909235211804747824182107317023868347474414853817368576")) return 6;
 if(s0.m[40]!=cpp_int("3238122226406033110010001541728022258844508450664395979649766319648774405894871547125803946961701103992832")) return 7;
 // Relation-aware recursion only on the five literal +1 horizontal translations.
 Result r7=solve_stage(st[7],N,H,nullptr,false,false); Result r6=solve_stage(st[6],N,H,&r7,false,false); Result r5=solve_stage(st[5],N,H,&r6,false,true); Result r4=solve_stage(st[4],N,H,&r5,true,true); Result r3=solve_stage(st[3],N,H,&r4,true,true); Result r2=solve_stage(st[2],N,H,&r3,true,true); Result r1=solve_stage(st[1],N,H,&r2,true,true); Result r0=solve_stage(st[0],N,H,&r1,true,false);
 int strict=0; for(int n=0;n<=N;++n){if(r0.m[n]<s0.m[n]){cerr<<"relation decreased at n="<<n<<"\n";return 8;}if(r0.m[n]>s0.m[n])strict++;}
 if(strict==0){cerr<<"no strict coefficient gain\n";return 9;}
 cout<<"H "<<H<<" N "<<N<<" overlap "<<overlap_pairs.size()<<" strict_coefficients "<<strict<<"\n";
 for(int n=0;n<=N;++n) if(r0.m[n]!=0 || s0.m[n]!=0) cout<<"DATA "<<n<<" "<<s0.m[n]<<" "<<r0.m[n]<<"\n";
 cout<<"PASS exact R08/E0011 horizontal descriptor relation dominates scalar-reset recursion\n";
}
