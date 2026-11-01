#include <bits/stdc++.h>
using namespace std;
struct P{int x,y;};
static const P dirs[4]={{1,0},{-1,0},{0,1},{0,-1}};
vector<P> SC={{-2,0},{-2,1},{-1,-1},{-1,0},{-1,1},{-1,2},{0,-1},{0,0},{0,1},{0,2},{1,-1},{1,0},{1,1},{2,0}};
vector<P> CEL={{-2,0},{-2,1},{-1,-1},{-1,0},{-1,1},{-1,2},{0,-1},{0,0},{0,1},{0,2},{1,-1},{1,0},{1,1},{1,2},{2,0},{2,1}};
map<pair<int,int>,int> SI,FI; int p3[20];
int gettr(uint32_t s,int i){return (s/p3[i])%3;}
uint32_t settr(uint32_t s,int i,int v){int o=gettr(s,i);return s+(v-o)*p3[i];}
vector<int> nidx(P c){vector<int> r;for(auto d:dirs){auto it=SI.find({c.x+d.x,c.y+d.y});if(it!=SI.end())r.push_back(it->second);}return r;}
struct Label{int kind;P a,b;};
vector<Label> lab={
 {0,{0,0},{0,0}},
 {1,{-1,1},{0,1}},
 {0,{0,1},{0,0}},
 {1,{-1,0},{-1,1}},
 {1,{0,0},{0,1}},
 {0,{-1,1},{0,0}},
 {1,{-1,0},{0,0}},
 {0,{-1,0},{0,0}}
};
using Bel=vector<uint32_t>;
unordered_map<uint64_t,Bel> tcache;
Bel trans_state(uint32_t s,int li){
    uint64_t key=(uint64_t)s*8+li;
    auto hit=tcache.find(key); if(hit!=tcache.end()) return hit->second;
    auto L=lab[li]; Bel out;
    if(L.kind==0){
        int i=SI[{L.a.x,L.a.y}];
        if(gettr(s,i)!=0) out.push_back(s);
        else{
            uint32_t a=settr(s,i,1); vector<int> os;
            for(int q:nidx(L.a)) if(gettr(a,q)==2) os.push_back(q);
            if(os.empty()) out.push_back(a);
            else for(int q:os){uint32_t t=settr(settr(a,i,0),q,0);out.push_back(t);}
        }
    }else{
        int ia=SI[{L.a.x,L.a.y}],ib=SI[{L.b.x,L.b.y}];
        if(gettr(s,ia)!=0||gettr(s,ib)!=0) out.push_back(s);
        else{
            uint32_t a=settr(settr(s,ia,2),ib,2); vector<int> ca,cb;
            for(int q:nidx(L.a)) if(gettr(a,q)==1) ca.push_back(q);
            for(int q:nidx(L.b)) if(gettr(a,q)==1) cb.push_back(q);
            if(ca.empty()) ca.push_back(-1); if(cb.empty()) cb.push_back(-1);
            for(int qa:ca) for(int qb:cb){
                uint32_t t=a;
                if(qa!=-1){t=settr(t,ia,0);t=settr(t,qa,0);}
                if(qb!=-1){t=settr(t,ib,0);t=settr(t,qb,0);}
                out.push_back(t);
            }
        }
    }
    sort(out.begin(),out.end());out.erase(unique(out.begin(),out.end()),out.end());
    return tcache[key]=out;
}
int DEL;
Bel edge_closure(Bel b){
    size_t n=b.size();
    for(size_t k=0;k<n;k++) if(gettr(b[k],DEL)==1) b.push_back(settr(b[k],DEL,0));
    sort(b.begin(),b.end());b.erase(unique(b.begin(),b.end()),b.end());return b;
}
Bel step(Bel const&B,int li){Bel o;for(auto s:B){auto t=trans_state(s,li);o.insert(o.end(),t.begin(),t.end());}return edge_closure(move(o));}
vector<int> TIDX;
bool target(Bel const&B){for(auto s:B)for(int i:TIDX)if(gettr(s,i)!=0)return false;return true;}
vector<uint32_t> enum_inits(){
    set<pair<int,int>> fixed={{-2,0},{-2,1},{-1,0},{-1,1},{0,0},{0,1}};
    vector<int> var;for(int i=0;i<(int)CEL.size();i++)if(!fixed.count({CEL[i].x,CEL[i].y}))var.push_back(i);
    long long total=1;for(size_t i=0;i<var.size();i++)total*=3;vector<int> vals(CEL.size());unordered_set<uint32_t> desc;
    for(long long code=0;code<total;code++){
        long long z=code;for(int i:var){vals[i]=z%3;z/=3;}for(int i=0;i<(int)CEL.size();i++)if(fixed.count({CEL[i].x,CEL[i].y}))vals[i]=0;
        bool ok=true;
        for(int i=0;i<(int)CEL.size()&&ok;i++){
            P c=CEL[i];int a=vals[i];
            for(P d:vector<P>{{1,0},{0,1}}){auto it=FI.find({c.x+d.x,c.y+d.y});if(it!=FI.end()){int b=vals[it->second];if((a==1&&b==2)||(a==2&&b==1)){ok=false;break;}}}
        }
        if(!ok)continue;uint32_t s=0;for(int i=0;i<(int)SC.size();i++)s+=vals[FI[{SC[i].x,SC[i].y}]]*p3[i];desc.insert(s);
    }
    vector<uint32_t> v(desc.begin(),desc.end());sort(v.begin(),v.end());return v;
}
const int MAXD=7;uint64_t pw[9],offv[9],TOTAL;
void mark_success(uint32_t s,vector<uint64_t>&bits){
    Bel b=edge_closure(Bel{s});
    function<void(Bel const&,int,uint64_t)> dfs=[&](Bel const&B,int d,uint64_t code){
        uint64_t id=offv[d]+code;
        if(target(B)) bits[id>>6]|=1ull<<(id&63);
        if(d==MAXD)return;
        for(int li=0;li<8;li++) dfs(step(B,li),d+1,code*8+li);
    };
    dfs(b,0,0);
}
int main(){
    p3[0]=1;for(int i=1;i<20;i++)p3[i]=p3[i-1]*3;
    for(int i=0;i<(int)SC.size();i++)SI[{SC[i].x,SC[i].y}]=i;
    for(int i=0;i<(int)CEL.size();i++)FI[{CEL[i].x,CEL[i].y}]=i;
    DEL=SI[{1,1}];
    for(P c:vector<P>{{-1,0},{-1,1},{0,0},{0,1},{1,0},{1,1}})TIDX.push_back(SI[{c.x,c.y}]);
    pw[0]=1;for(int d=1;d<=8;d++)pw[d]=pw[d-1]*8;offv[0]=0;for(int d=1;d<=8;d++)offv[d]=offv[d-1]+pw[d-1];TOTAL=offv[8];
    auto inits=enum_inits();assert(inits.size()==1743);
    unordered_set<uint32_t> initset(inits.begin(),inits.end());
    vector<uint32_t> W={177147,0,18,486,9,243,1458,1215,39366};
    for(auto s:W)assert(initset.count(s));
    vector<uint64_t> inter((TOTAL+63)/64,~0ull);if(TOTAL%64)inter.back()&=(1ull<<(TOTAL%64))-1;
    vector<size_t> remain;
    for(auto s:W){
        vector<uint64_t> good(inter.size());mark_success(s,good);
        size_t c=0;for(size_t k=0;k<inter.size();k++){inter[k]&=good[k];c+=__builtin_popcountll(inter[k]);}
        remain.push_back(c);
    }
    assert(remain.back()==0);
    vector<Bel> joint;for(auto s:W)joint.push_back(edge_closure(Bel{s}));
    unsigned long long count_by_depth[MAXD+1]={0};
    function<void(vector<Bel> const&,int)> rec=[&](vector<Bel> const&cur,int d){
        bool ok=true;for(auto const&B:cur)if(!target(B)){ok=false;break;}if(ok)count_by_depth[d]++;
        if(d==MAXD)return;
        for(int li=0;li<8;li++){vector<Bel> nx;nx.reserve(cur.size());for(auto const&B:cur)nx.push_back(step(B,li));rec(nx,d+1);}
    };
    rec(joint,0);
    for(int d=0;d<=MAXD;d++)assert(count_by_depth[d]==0);
    cout<<"PASS exact R08/E0011 L7 eight-label minimum-length obstruction\n";
    cout<<"generated_shield_descriptors="<<inits.size()<<" witness_count="<<W.size()<<" total_words_le7="<<TOTAL<<"\n";
    cout<<"witness_states=";for(auto s:W)cout<<s<<",";cout<<"\n";
    cout<<"intersection_remaining_after_each_witness=";for(auto x:remain)cout<<x<<",";cout<<"\n";
    cout<<"joint_success_counts_depth_0_to_7=";for(int d=0;d<=MAXD;d++)cout<<count_by_depth[d]<<",";cout<<"\n";
    cout<<"conclusion=min_universal_robust_word_length_at_least_8\n";
}
