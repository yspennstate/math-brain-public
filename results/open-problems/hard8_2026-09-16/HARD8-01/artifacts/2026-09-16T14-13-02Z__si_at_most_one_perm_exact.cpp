#include <bits/stdc++.h>
using namespace std;

struct Letter { vector<uint16_t> img; string name; int s=-1,t=-1; bool is_perm=false; };
struct BFSResult { int dist; vector<int> word; int finalmask; };

static vector<vector<int>> partitions_n(int n){
    vector<vector<int>> out; vector<int> cur;
    function<void(int,int)> rec=[&](int rem,int lo){ if(rem==0){out.push_back(cur);return;} for(int x=lo;x<=rem;x++){cur.push_back(x);rec(rem-x,x);cur.pop_back();}};
    rec(n,1); return out;
}
static vector<int> perm_from_partition(const vector<int>& part,int n){ vector<int> p(n);int b=0;for(int len:part){for(int j=0;j<len;j++)p[b+j]=b+(j+1)%len;b+=len;}return p; }
static vector<int> orbit_id_from_partition(const vector<int>& part,int n){ vector<int> o(n);int b=0;for(int c=0;c<(int)part.size();c++){for(int j=0;j<part[c];j++)o[b+j]=c;b+=part[c];}return o; }
static Letter make_perm(const vector<int>& p,int n,string nm){int N=1<<n;Letter L;L.img.resize(N);L.name=move(nm);L.is_perm=true;for(int m=0;m<N;m++){int z=0;for(int i=0;i<n;i++)if(m&(1<<i))z|=1<<p[i];L.img[m]=z;}return L;}
static Letter make_idem(int s,int t,int n){int N=1<<n;Letter L;L.img.resize(N);L.s=s;L.t=t;L.name="e"+to_string(s)+"->"+to_string(t);for(int m=0;m<N;m++){int z=m;if(m&(1<<s)){z&=~(1<<s);z|=1<<t;}L.img[m]=z;}return L;}

static BFSResult reset_bfs(const vector<const Letter*>& ls,int n,bool want=false){
    int N=1<<n,full=N-1; static uint32_t seen[1<<12]; static uint16_t dd[1<<12], par[1<<12],qq[1<<12]; static int16_t pl[1<<12]; static uint32_t st=0; ++st;if(!st){memset(seen,0,sizeof(seen));st=1;}int h=0,zq=0;qq[zq++]=full;seen[full]=st;dd[full]=0;par[full]=full;pl[full]=-1;
    auto one=[](int m){return m && !(m&(m-1));};
    while(h<zq){int m=qq[h++],d=dd[m];for(int li=0;li<(int)ls.size();li++){int z=ls[li]->img[m];if(seen[z]==st)continue;seen[z]=st;dd[z]=d+1;par[z]=m;pl[z]=li;qq[zq++]=z;if(one(z)){vector<int>w;if(want){int c=z;while(c!=full){w.push_back(pl[c]);c=par[c];}reverse(w.begin(),w.end());}return{d+1,w,z};}}}
    return{-1,{},0};
}
static long long C(int n,int k){if(k<0||k>n)return 0;if(k>n-k)k=n-k;long long r=1;for(int i=1;i<=k;i++)r=r*(n-k+i)/i;return r;}
static void comb_iter(int N,int k,const function<void(const vector<int>&)>&f){if(k==0){f({});return;}vector<int>a(k);iota(a.begin(),a.end(),0);while(1){f(a);int i=k-1;while(i>=0&&a[i]==N-k+i)--i;if(i<0)break;++a[i];for(int j=i+1;j<k;j++)a[j]=a[j-1]+1;}}

struct Rec { long long tested=0,sync=0,viol=0; int maxrt=-1; long long maxcount=0; vector<string> letters; vector<int> ptype; vector<int> word; };
static void update_rec(Rec &R,const vector<const Letter*>&ls,int n,const vector<int>&pt,int dist){R.tested++; if(dist<0)return;R.sync++; if(dist>(n-1)*(n-1))R.viol++; if(dist>R.maxrt){R.maxrt=dist;R.maxcount=1;R.letters.clear();for(auto L:ls)R.letters.push_back(L->name);R.ptype=pt;R.word=reset_bfs(ls,n,true).word;}else if(dist==R.maxrt)R.maxcount++;}

static bool strongly_connected_orbits(const vector<int>& oid,int r,const vector<const Letter*>&ls){
    if(r<=1) return true;
    bool a[12][12] = {};
    for(int i=0;i<r;i++) a[i][i]=true;
    for(auto L:ls) if(!L->is_perm){ int u=oid[L->s], v=oid[L->t]; if(u!=v) a[u][v]=true; }
    for(int k=0;k<r;k++) for(int i=0;i<r;i++) if(a[i][k]) for(int j=0;j<r;j++) a[i][j]=a[i][j] || a[k][j];
    for(int i=0;i<r;i++) for(int j=0;j<r;j++) if(!a[i][j]) return false;
    return true;
}
static bool all_cross(const vector<int>&oid,const vector<const Letter*>&ls){for(auto L:ls)if(!L->is_perm&&oid[L->s]==oid[L->t])return false;return true;}

int main(int argc,char**argv){int n=8;if(argc>1)n=stoi(argv[1]);if(n>12)return 2;int E=n*(n-1);vector<Letter>ids;for(int s=0;s<n;s++)for(int t=0;t<n;t++)if(s!=t)ids.push_back(make_idem(s,t,n));auto parts=partitions_n(n);vector<Letter>ps;vector<vector<int>>oids;for(auto &pt:parts){auto p=perm_from_partition(pt,n);string nm="p[";for(int i=0;i<(int)pt.size();i++){if(i)nm+=",";nm+=to_string(pt[i]);}nm+="]";ps.push_back(make_perm(p,n,nm));oids.push_back(orbit_id_from_partition(pt,n));}
    Rec q3,q4, q3_trans,q4_trans,q3_multi_sc,q4_multi_sc,q3_multi_sc_cross,q4_multi_sc_cross,q3_no_perm,q4_no_perm;
    long long np3=0,np4=0,op3=0,op4=0;
    for(int k=1;k<=4;k++)comb_iter(E,k,[&](const vector<int>&a){vector<const Letter*>ls;for(int x:a)ls.push_back(&ids[x]);int d=reset_bfs(ls,n,false).dist;if(k<=3){update_rec(q3,ls,n,{},d);update_rec(q3_no_perm,ls,n,{},d);np3++;}update_rec(q4,ls,n,{},d);update_rec(q4_no_perm,ls,n,{},d);np4++;});
    for(int pi=0;pi<(int)ps.size();pi++){int r=parts[pi].size();for(int k=0;k<=3;k++)comb_iter(E,k,[&](const vector<int>&a){vector<const Letter*>ls{&ps[pi]};for(int x:a)ls.push_back(&ids[x]);int d=reset_bfs(ls,n,false).dist;bool sc=strongly_connected_orbits(oids[pi],r,ls);bool cr=all_cross(oids[pi],ls);if(k+1<=3){update_rec(q3,ls,n,parts[pi],d);op3++;if(r==1)update_rec(q3_trans,ls,n,parts[pi],d);else if(sc){update_rec(q3_multi_sc,ls,n,parts[pi],d);if(cr)update_rec(q3_multi_sc_cross,ls,n,parts[pi],d);}}update_rec(q4,ls,n,parts[pi],d);op4++;if(r==1)update_rec(q4_trans,ls,n,parts[pi],d);else if(sc){update_rec(q4_multi_sc,ls,n,parts[pi],d);if(cr)update_rec(q4_multi_sc_cross,ls,n,parts[pi],d);}});}
    long long pN=parts.size();long long exnp3=C(E,1)+C(E,2)+C(E,3), exnp4=exnp3+C(E,4), exop3=pN*(C(E,0)+C(E,1)+C(E,2)), exop4=pN*(C(E,0)+C(E,1)+C(E,2)+C(E,3));
    auto show=[&](const char*name,const Rec&R){cout<<name<<" tested "<<R.tested<<" synchronizing "<<R.sync<<" violations "<<R.viol<<" max_rt "<<R.maxrt<<" max_count "<<R.maxcount<<"\n";if(R.maxrt>=0){cout<<name<<" extremal_cycle_type";if(R.ptype.empty())cout<<" NONE";else for(int x:R.ptype)cout<<" "<<x;cout<<"\n";cout<<name<<" extremal_letters";for(auto&s:R.letters)cout<<" "<<s;cout<<"\n";cout<<name<<" extremal_word_indices";for(int x:R.word)cout<<" "<<x;cout<<"\n";}};
    cout<<"HARD8_01_SI_AT_MOST_ONE_PERM_EXACT_V2\n";cout<<"n "<<n<<" square_bound "<<(n-1)*(n-1)<<" simple_idempotents "<<E<<" permutation_cycle_types "<<pN<<"\n";
    cout<<"coverage_formula_q3 no_perm "<<exnp3<<" one_perm "<<exop3<<" total "<<exnp3+exop3<<"\n";cout<<"coverage_loop_q3 no_perm "<<np3<<" one_perm "<<op3<<" total "<<np3+op3<<"\n";cout<<"coverage_formula_q4 no_perm "<<exnp4<<" one_perm "<<exop4<<" total "<<exnp4+exop4<<"\n";cout<<"coverage_loop_q4 no_perm "<<np4<<" one_perm "<<op4<<" total "<<np4+op4<<"\n";
    show("q3_all",q3);show("q4_all",q4);show("q3_no_perm",q3_no_perm);show("q4_no_perm",q4_no_perm);show("q3_transitive_perm",q3_trans);show("q4_transitive_perm",q4_trans);show("q3_multi_orbit_transfer_SC",q3_multi_sc);show("q4_multi_orbit_transfer_SC",q4_multi_sc);show("q3_multi_orbit_transfer_SC_cross_only",q3_multi_sc_cross);show("q4_multi_orbit_transfer_SC_cross_only",q4_multi_sc_cross);
    bool ok=np3==exnp3&&np4==exnp4&&op3==exop3&&op4==exop4&&q3.viol==0&&q4.viol==0;cout<<(ok?"ALL_CHECKS_PASSED":"CHECK_FAILURE")<<"\n";return ok?0:1;
}
