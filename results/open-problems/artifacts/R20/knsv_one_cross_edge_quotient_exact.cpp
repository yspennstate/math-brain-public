#include <bits/stdc++.h>
using namespace std;
using ll=long long; using u64=uint64_t; using u16=uint16_t;
static const pair<int,int> BASE[6]={{0,2},{2,4},{4,1},{1,3},{3,0},{0,4}};
static const int SLOT[2][4]={{1,2,3,3},{1,3,4,4}};
using Key=array<ll,12>;

struct LocalClass { int r; uint32_t mask; };
vector<uint32_t> unrep[5], ptrep[5];
vector<vector<pair<int,int>>> allowedE(5);

int root(int *p,int x){while(p[x]!=x){p[x]=p[p[x]]; x=p[x];}return x;}
bool connected_mask(int r,uint32_t mask){int n=r+2,p[6];iota(p,p+n,0);auto &A=allowedE[r];for(int i=0;i<(int)A.size();++i)if(mask>>i&1){int a=root(p,A[i].first),b=root(p,A[i].second);if(a!=b)p[b]=a;}int z=root(p,0);for(int i=1;i<n;++i)if(root(p,i)!=z)return false;return true;}
uint32_t transform_mask(int r,uint32_t mask,const vector<int>&pm){auto &A=allowedE[r]; map<pair<int,int>,int> idx; for(int i=0;i<(int)A.size();++i)idx[A[i]]=i; uint32_t out=0;for(int i=0;i<(int)A.size();++i)if(mask>>i&1){int a=pm[A[i].first],b=pm[A[i].second];if(a>b)swap(a,b);out|=1u<<idx[{a,b}];}return out;}
uint32_t canon_un(int r,uint32_t mask){int n=r+2;vector<int> q(r);iota(q.begin(),q.end(),2);uint32_t best=UINT32_MAX;do{vector<int> pm(n);pm[0]=0;pm[1]=1;for(int j=0;j<r;++j)pm[2+j]=q[j];best=min(best,transform_mask(r,mask,pm));}while(next_permutation(q.begin(),q.end()));return best;}
uint32_t canon_pt(int r,uint32_t mask,int markj){int n=r+2,mark=2+markj;vector<int> rest;for(int v=2;v<n;++v)if(v!=mark)rest.push_back(v);vector<int>dests;for(int v=3;v<n;++v)dests.push_back(v);uint32_t best=UINT32_MAX;sort(dests.begin(),dests.end());do{vector<int>pm(n,-1);pm[0]=0;pm[1]=1;pm[mark]=2;for(int i=0;i<(int)rest.size();++i)pm[rest[i]]=dests[i];best=min(best,transform_mask(r,mask,pm));}while(next_permutation(dests.begin(),dests.end()));return best;}
void enum_classes(){for(int r=1;r<=4;++r){int n=r+2;for(int i=0;i<n;++i)for(int j=i+1;j<n;++j)if(!(i==0&&j==1))allowedE[r].push_back({i,j});set<uint32_t> U,P;int T=1<<(int)allowedE[r].size();int conn=0;for(int m=0;m<T;++m)if(connected_mask(r,m)){++conn;U.insert(canon_un(r,m));for(int j=0;j<r;++j)P.insert(canon_pt(r,m,j));}unrep[r]=vector<uint32_t>(U.begin(),U.end());ptrep[r]=vector<uint32_t>(P.begin(),P.end());cerr<<"r="<<r<<" connected="<<conn<<" un="<<U.size()<<" pt="<<P.size()<<"\n";}}

struct Graph{array<u16,12> adj{};};
void addE(Graph&g,int a,int b){if(a>b)swap(a,b); if((g.adj[a]>>b)&1) {cerr<<"dup edge "<<a<<","<<b<<"\n"; abort();} g.adj[a]|=u16(1u<<b); g.adj[b]|=u16(1u<<a);}
Graph build_graph(int side,const array<int,4>&r,int cs,int ct,const array<int,4>&choice){Graph g;for(auto e:BASE)addE(g,e.first,e.second);int nxt=5;array<int,4> markGlobal{};for(int s=0;s<4;++s){int rr=r[s];bool pointed=(s==cs||s==ct);uint32_t mask=pointed?ptrep[rr][choice[s]]:unrep[rr][choice[s]];auto [a,b]=BASE[SLOT[side][s]];vector<int>mp(rr+2);mp[0]=a;mp[1]=b;for(int j=0;j<rr;++j){mp[2+j]=nxt+j;}if(pointed)markGlobal[s]=mp[2];auto &A=allowedE[rr];for(int i=0;i<(int)A.size();++i)if(mask>>i&1)addE(g,mp[A[i].first],mp[A[i].second]);nxt+=rr;}if(nxt!=12)abort();addE(g,markGlobal[cs],markGlobal[ct]);return g;}

Key traces(const Graph&g){ll L[12][12]{};for(int i=0;i<12;++i){int d=__builtin_popcount((unsigned)g.adj[i]);L[i][i]=d;for(int j=0;j<12;++j)if((g.adj[i]>>j)&1)L[i][j]=-1;}ll P[12][12]{},Q[12][12]{};for(int i=0;i<12;++i)for(int j=0;j<12;++j)P[i][j]=L[i][j];Key out{};for(int e=1;e<=12;++e){__int128 tr=0;for(int i=0;i<12;++i)tr+=P[i][i];if(tr>LLONG_MAX||tr<LLONG_MIN)abort();out[e-1]=(ll)tr;if(e<12){for(int i=0;i<12;++i)for(int j=0;j<12;++j){__int128 z=0;for(int k=0;k<12;++k)z+=(__int128)P[i][k]*L[k][j];if(z>LLONG_MAX||z<LLONG_MIN)abort();Q[i][j]=(ll)z;}for(int i=0;i<12;++i)for(int j=0;j<12;++j)P[i][j]=Q[i][j];}}
return out;}
struct Rec{Key k; Graph g;};

void gen_comps_rec(int pos,int rem,array<int,4>&a,vector<array<int,4>>&out){if(pos==3){a[3]=rem;if(rem>0)out.push_back(a);return;}for(int x=1;x<=rem-(3-pos);++x){a[pos]=x;gen_comps_rec(pos+1,rem-x,a,out);}}
vector<array<int,4>> comps(){vector<array<int,4>>o;array<int,4>a{};gen_comps_rec(0,7,a,o);return o;}

template<class F> void choices_rec(const array<int,4>&r,int cs,int ct,int pos,array<int,4>&ch,F &f){if(pos==4){f(ch);return;}int n=(pos==cs||pos==ct)?ptrep[r[pos]].size():unrep[r[pos]].size();for(int i=0;i<n;++i){ch[pos]=i;choices_rec(r,cs,ct,pos+1,ch,f);}}

vector<Rec> generate_side(int side){vector<Rec> out;out.reserve(160000);auto C=comps();for(auto &r:C)for(int cs=0;cs<4;++cs)for(int ct=cs+1;ct<4;++ct){array<int,4>ch{};auto f=[&](const array<int,4>&cc){Graph g=build_graph(side,r,cs,ct,cc);out.push_back({traces(g),g});};choices_rec(r,cs,ct,0,ch,f);}return out;}

u64 part_start(){u64 z=0;for(int i=0;i<12;++i)z|=(u64)i<<(4*i);return z;}
inline int lab(u64 st,int v){return (st>>(4*v))&15;}
u64 merge_part(u64 st,int a,int b){int x=lab(st,a),y=lab(st,b);if(x==y)return st;int lo=min(x,y),hi=max(x,y);for(int v=0;v<12;++v)if(lab(st,v)==hi){st &= ~(u64(15)<<(4*v)); st |= (u64)lo<<(4*v);}return st;}

uint32_t evalU(const Graph&g,uint32_t MOD,uint32_t q,const array<uint32_t,13>&x){vector<pair<int,int>> E;for(int i=0;i<12;++i)for(int j=i+1;j<12;++j)if((g.adj[i]>>j)&1)E.push_back({i,j});unordered_map<u64,uint32_t> dp,nd;dp.reserve(4096);dp[part_start()]=1;for(auto [a,b]:E){nd.clear();nd.reserve(dp.size()*2+16);for(auto &kv:dp){u64 st=kv.first;uint32_t w=kv.second;int ra=lab(st,a),rb=lab(st,b);if(ra==rb){uint64_t val=(uint64_t)w*(1+q)%MOD;auto it=nd.find(st);if(it==nd.end())nd.emplace(st,(uint32_t)val);else it->second=(it->second+val)%MOD;}else{auto it=nd.find(st);if(it==nd.end())nd.emplace(st,w);else {uint32_t z=it->second+w;if(z>=MOD)z-=MOD;it->second=z;}u64 mt=merge_part(st,a,b);auto jt=nd.find(mt);if(jt==nd.end())nd.emplace(mt,w);else {uint32_t z=jt->second+w;if(z>=MOD)z-=MOD;jt->second=z;}}}dp.swap(nd);}uint64_t ans=0;for(auto &kv:dp){int cnt[12]{};for(int v=0;v<12;++v){int r=lab(kv.first,v);cnt[r]++;}uint64_t w=kv.second;for(int r=0;r<12;++r)if(cnt[r])w=w*x[cnt[r]]%MOD;ans+=w;if(ans>=(uint64_t)MOD*MOD)ans%=MOD;}return ans%MOD;}

uint32_t brute_evalU(const Graph&g,uint32_t MOD,uint32_t q,const array<uint32_t,13>&x){
    vector<pair<int,int>> E;
    for(int i=0;i<12;++i)for(int j=i+1;j<12;++j)if((g.adj[i]>>j)&1)E.push_back({i,j});
    if(E.size()>24){ cerr<<"brute selfcheck graph too large\n"; abort(); }
    uint64_t total=1ull<<E.size(), ans=0;
    for(uint64_t mask=0;mask<total;++mask){
        int p[12],sz[12]; iota(p,p+12,0); fill(sz,sz+12,1);
        auto f=[&](int a){while(p[a]!=a){p[a]=p[p[a]];a=p[a];}return a;};
        int ecount=0;
        for(int e=0;e<(int)E.size();++e) if(mask>>e&1){
            ++ecount; int a=f(E[e].first),b=f(E[e].second);
            if(a!=b){ if(sz[a]<sz[b]) swap(a,b); p[b]=a; sz[a]+=sz[b]; }
        }
        int comps=0; uint64_t w=1;
        for(int v=0;v<12;++v) if(f(v)==v){ ++comps; w=w*x[sz[v]]%MOD; }
        int cyc=ecount-12+comps;
        for(int k=0;k<cyc;++k) w=w*q%MOD;
        ans += w; if(ans>=(uint64_t)MOD*MOD) ans%=MOD;
    }
    return ans%MOD;
}

array<int,12> vertex_signature(const Graph&g,int v){
    array<int,12> z{}; z.fill(-1);
    z[0]=__builtin_popcount((unsigned)g.adj[v]);
    vector<int>d;
    for(int w=0;w<12;++w) if((g.adj[v]>>w)&1) d.push_back(__builtin_popcount((unsigned)g.adj[w]));
    sort(d.begin(),d.end());
    for(int i=0;i<(int)d.size();++i) z[1+i]=d[i];
    return z;
}

bool isomorphic_exact(const Graph&A,const Graph&B){
    array<array<int,12>,12> sa,sb;
    for(int v=0;v<12;++v){sa[v]=vertex_signature(A,v); sb[v]=vertex_signature(B,v);}
    multiset<array<int,12>> ma(sa.begin(),sa.end()),mb(sb.begin(),sb.end());
    if(ma!=mb) return false;
    vector<int> ord(12); iota(ord.begin(),ord.end(),0);
    auto count_sig=[&](auto const&sigs,auto sig){int c=0;for(auto const&x:sigs)c+=x==sig;return c;};
    sort(ord.begin(),ord.end(),[&](int u,int v){
        int cu=count_sig(sa,sa[u]), cv=count_sig(sa,sa[v]);
        if(cu!=cv) return cu<cv;
        return sa[u]>sa[v];
    });
    int mp[12],inv[12]; fill(mp,mp+12,-1); fill(inv,inv+12,-1);
    function<bool(int)> dfs=[&](int dep){
        if(dep==12) return true;
        int u=ord[dep];
        for(int v=0;v<12;++v) if(inv[v]<0 && sa[u]==sb[v]){
            bool ok=true;
            for(int d=0;d<dep && ok;++d){int u2=ord[d],v2=mp[u2];
                bool ea=(A.adj[u]>>u2)&1, eb=(B.adj[v]>>v2)&1;
                if(ea!=eb) ok=false;
            }
            if(!ok) continue;
            mp[u]=v; inv[v]=u;
            if(dfs(dep+1)) return true;
            mp[u]=-1; inv[v]=-1;
        }
        return false;
    };
    return dfs(0);
}

int main(){
    ios::sync_with_stdio(false);
    enum_classes();
    const int EU[5]={0,1,8,67,701};
    const int EP[5]={0,1,14,171,2394};
    for(int r=1;r<=4;++r){
        cout<<"r="<<r<<" unpointed_rooted_iso_types="<<unrep[r].size()
            <<" pointed_rooted_iso_types="<<ptrep[r].size()<<"\n";
        if((int)unrep[r].size()!=EU[r] || (int)ptrep[r].size()!=EP[r]) abort();
    }
    auto C=comps();
    cout<<"R20 exact rooted-isomorphism quotient: KNSV n=12 one-cross-edge family\n";
    cout<<"positive_compositions="<<C.size()<<"\n";
    long long formula=0;
    for(auto&r:C)for(int s=0;s<4;++s)for(int t=s+1;t<4;++t){
        long long z=1;
        for(int j=0;j<4;++j) z*=(j==s||j==t)?(long long)ptrep[r[j]].size():(long long)unrep[r[j]].size();
        formula+=z;
    }
    cout<<"quotient_instances_per_side="<<formula<<"\n";
    if(formula!=157212) abort();

    vector<Rec>A=generate_side(0),B=generate_side(1);
    cout<<"generated="<<A.size()<<","<<B.size()<<"\n";
    if(A.size()!=157212 || B.size()!=157212) abort();
    sort(A.begin(),A.end(),[](auto&a,auto&b){return a.k<b.k;});
    sort(B.begin(),B.end(),[](auto&a,auto&b){return a.k<b.k;});

    vector<Rec> SA,SB; size_t i=0,j=0; long long trace_pairs=0; int common=0;
    while(i<A.size()&&j<B.size()){
        if(A[i].k<B[j].k){++i;continue;} if(B[j].k<A[i].k){++j;continue;}
        Key k=A[i].k; size_t ii=i,jj=j;
        while(ii<A.size()&&A[ii].k==k)++ii; while(jj<B.size()&&B[jj].k==k)++jj;
        ++common; trace_pairs+=(long long)(ii-i)*(jj-j);
        for(size_t z=i;z<ii;++z)SA.push_back(A[z]); for(size_t z=j;z<jj;++z)SB.push_back(B[z]);
        i=ii;j=jj;
    }
    cout<<"common_trace12="<<common<<"\n";
    cout<<"trace_survivor_instances="<<SA.size()<<","<<SB.size()<<"\n";
    cout<<"trace_cross_pairs="<<trace_pairs<<"\n";
    if(common!=47 || SA.size()!=117 || SB.size()!=122 || trace_pairs!=322) abort();

    const uint32_t MOD=1000000007u, q=7;
    array<uint32_t,13>x{}; for(int s=1;s<=12;++s)x[s]=(uint32_t)((uint64_t)s*s+22ull*s+68ull);
    vector<uint32_t> ua(SA.size()),ub(SB.size());
    for(size_t a=0;a<SA.size();++a) ua[a]=evalU(SA[a].g,MOD,q,x);
    for(size_t b=0;b<SB.size();++b) ub[b]=evalU(SB[b].g,MOD,q,x);

    int m=0; for(int u=0;u<12;++u)for(int v=u+1;v<12;++v)m+=((SA[0].g.adj[u]>>v)&1);
    uint32_t dpv=ua[0], brv=brute_evalU(SA[0].g,MOD,q,x);
    cout<<"modular_U_selfcheck_edges="<<m<<" dp="<<dpv<<" brute="<<brv<<"\n";
    if(dpv!=brv) abort();
    cout<<"modular_U_dp_vs_bruteforce_selfcheck=PASS\n";

    long long unequal=0,equal=0,iso=0,noniso=0;
    for(size_t a=0;a<SA.size();++a) for(size_t b=0;b<SB.size();++b) if(SA[a].k==SB[b].k){
        if(ua[a]!=ub[b]){ ++unequal; continue; }
        ++equal;
        if(isomorphic_exact(SA[a].g,SB[b].g)) ++iso; else ++noniso;
    }
    cout<<"specialization_unequal_pairs="<<unequal<<"\n";
    cout<<"specialization_equal_pairs="<<equal<<"\n";
    cout<<"specialization_equal_isomorphic_pairs="<<iso<<"\n";
    cout<<"specialization_equal_nonisomorphic_pairs="<<noniso<<"\n";
    if(unequal+equal!=trace_pairs || unequal!=108 || equal!=214 || iso!=214 || noniso!=0) abort();
    cout<<"VERDICT=PASS_NO_NONISOMORPHIC_U_COLLISION_IN_FULL_ROOTED_ISO_QUOTIENT_ONE_CROSS_EDGE_FAMILY\n";
}
