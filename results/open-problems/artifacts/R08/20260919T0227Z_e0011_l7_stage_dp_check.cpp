#include <bits/stdc++.h>
#include <boost/multiprecision/cpp_int.hpp>
using namespace std;
using boost::multiprecision::cpp_int;

struct P { int x,y; };
struct PLess { bool operator()(P const&a,P const&b) const { return tie(a.x,a.y)<tie(b.x,b.y); } };
bool operator==(P a,P b){ return a.x==b.x && a.y==b.y; }
vector<P> dirs={{1,0},{-1,0},{0,1},{0,-1}};

vector<P> SC={{-2,0},{-2,1},{-1,-1},{-1,0},{-1,1},{-1,2},{0,-1},{0,0},{0,1},{0,2},{1,-1},{1,0},{1,1},{2,0}};
vector<P> CEL={{-2,0},{-2,1},{-1,-1},{-1,0},{-1,1},{-1,2},{0,-1},{0,0},{0,1},{0,2},{1,-1},{1,0},{1,1},{1,2},{2,0},{2,1}};
map<pair<int,int>,int> SI, FI;
int p3[20];

int gettr(uint32_t s,int i){ return (s/p3[i])%3; }
uint32_t settr(uint32_t s,int i,int v){ int o=gettr(s,i); return s+(v-o)*p3[i]; }
vector<int> nidx(P c){
    vector<int> r;
    for(auto d:dirs){
        auto it=SI.find({c.x+d.x,c.y+d.y});
        if(it!=SI.end()) r.push_back(it->second);
    }
    return r;
}
struct Label { int kind; P a,b; };
vector<Label> labels={
 {0,{0,0},{0,0}},
 {1,{-1,1},{0,1}},
 {0,{0,1},{0,0}},
 {0,{1,0},{0,0}},
 {1,{-1,0},{-1,1}},
 {1,{0,0},{0,1}},
 {0,{-1,1},{0,0}},
 {1,{-1,0},{0,0}},
 {0,{-1,0},{0,0}},
 {1,{0,0},{1,0}}
};
unordered_map<uint64_t, vector<pair<uint32_t,int>>> tcache;
vector<pair<uint32_t,int>> trans(uint32_t s,int li){
    uint64_t key=(uint64_t)s*10+li;
    auto hit=tcache.find(key); if(hit!=tcache.end()) return hit->second;
    Label L=labels[li]; map<uint32_t,int> out;
    if(L.kind==0){
        int i=SI[{L.a.x,L.a.y}];
        if(gettr(s,i)!=0) out[s]+=72;
        else {
            uint32_t a=settr(s,i,1); vector<int> os;
            for(int q:nidx(L.a)) if(gettr(a,q)==2) os.push_back(q);
            if(os.empty()) out[a]+=72;
            else {
                int w=72/(int)os.size();
                for(int q:os){
                    uint32_t t=settr(a,i,0); t=settr(t,q,0); out[t]+=w;
                }
            }
        }
    } else {
        int ia=SI[{L.a.x,L.a.y}], ib=SI[{L.b.x,L.b.y}];
        if(gettr(s,ia)!=0 || gettr(s,ib)!=0) out[s]+=36;
        else {
            uint32_t a=settr(settr(s,ia,2),ib,2);
            vector<int> ca,cb;
            for(int q:nidx(L.a)) if(gettr(a,q)==1) ca.push_back(q);
            for(int q:nidx(L.b)) if(gettr(a,q)==1) cb.push_back(q);
            if(ca.empty()) ca.push_back(-1);
            if(cb.empty()) cb.push_back(-1);
            int den=(int)ca.size()*(int)cb.size();
            assert(36%den==0);
            int w=36/den;
            for(int qa:ca) for(int qb:cb){
                uint32_t t=a;
                if(qa!=-1){ t=settr(t,ia,0); t=settr(t,qa,0); }
                if(qb!=-1){ t=settr(t,ib,0); t=settr(t,qb,0); }
                out[t]+=w;
            }
        }
    }
    vector<pair<uint32_t,int>> v(out.begin(),out.end());
    tcache.emplace(key,v);
    return v;
}
bool target(uint32_t s){
    vector<P> T={{-1,0},{-1,1},{0,0},{0,1},{1,0},{1,1}};
    for(auto c:T){
        auto it=SI.find({c.x,c.y});
        if(it==SI.end() || gettr(s,it->second)!=0) return false;
    }
    return true;
}

struct KeyHash {
  size_t operator()(uint64_t x) const noexcept { return std::hash<uint64_t>{}(x); }
};
unordered_map<uint64_t, cpp_int, KeyHash> memo10, memo8;
cpp_int Arec(int n,uint32_t s,bool terminal){
    uint64_t key=((uint64_t)n<<33) | ((uint64_t)terminal<<32) | s;
    auto &M = terminal?memo8:memo10;
    auto it=M.find(key); if(it!=M.end()) return it->second;
    cpp_int z=0;
    if(n==0) z=target(s)?1:0;
    else {
        for(int li=0;li<10;li++){
            if(terminal && (li==3 || li==9)) continue;
            for(auto [t,w]:trans(s,li)) z += cpp_int(w)*Arec(n-1,t,terminal);
        }
    }
    M.emplace(key,z); return z;
}
cpp_int ipow(cpp_int a,int n){ cpp_int r=1; while(n--) r*=a; return r; }
cpp_int fact(int n){ cpp_int r=1; for(int i=2;i<=n;i++) r*=i; return r; }

vector<uint32_t> enum_inits(set<pair<int,int>> fixed_zero, long long &full){
    vector<int> var;
    for(int i=0;i<(int)CEL.size();i++) if(!fixed_zero.count({CEL[i].x,CEL[i].y})) var.push_back(i);
    long long total=1; for(size_t i=0;i<var.size();i++) total*=3;
    vector<int> vals(CEL.size(),0);
    unordered_set<uint32_t> desc;
    full=0;
    for(long long code=0;code<total;code++){
        long long z=code;
        for(int i:var){ vals[i]=z%3; z/=3; }
        for(int i=0;i<(int)CEL.size();i++) if(fixed_zero.count({CEL[i].x,CEL[i].y})) vals[i]=0;
        bool ok=true;
        for(int i=0;i<(int)CEL.size() && ok;i++){
            P c=CEL[i]; int a=vals[i];
            for(P d:vector<P>{{1,0},{0,1}}){
                auto it=FI.find({c.x+d.x,c.y+d.y});
                if(it!=FI.end()){
                    int b=vals[it->second];
                    if((a==1&&b==2)||(a==2&&b==1)){ ok=false; break; }
                }
            }
        }
        if(!ok) continue;
        full++;
        uint32_t s=0;
        for(int i=0;i<(int)SC.size();i++){
            int v=vals[FI[{SC[i].x,SC[i].y}]];
            s += v*p3[i];
        }
        desc.insert(s);
    }
    vector<uint32_t> v(desc.begin(),desc.end());
    sort(v.begin(),v.end());
    return v;
}

struct Rat { cpp_int num, den; };
bool rat_gt(Rat const&a,Rat const&b){ return a.num*b.den > b.num*a.den; }

Rat best_stage(int D, vector<uint32_t> const& inits, bool terminal, int &bestlam){
    const int N=8; cpp_int F=fact(N), H=36*D, den=F*ipow(H,N);
    Rat best{0,1}; bestlam=0;
    for(int lam=1;lam<=8;lam++){
        bool first=true; cpp_int mn=0;
        vector<cpp_int> coeff(N+1);
        for(int n=0;n<=N;n++) coeff[n]=ipow(cpp_int(lam),n)*(F/fact(n))*ipow(H,N-n);
        for(uint32_t s:inits){
            cpp_int sum=0;
            for(int n=0;n<=N;n++) sum += coeff[n]*Arec(n,s,terminal);
            if(first || sum<mn){ mn=sum; first=false; }
        }
        Rat r{ipow(cpp_int(32),lam)*mn, ipow(cpp_int(87),lam)*den};
        if(bestlam==0 || rat_gt(r,best)){ best=r; bestlam=lam; }
    }
    return best;
}
string ss(cpp_int x){ return x.convert_to<string>(); }

int main(){
    p3[0]=1; for(int i=1;i<20;i++) p3[i]=p3[i-1]*3;
    for(int i=0;i<(int)SC.size();i++) SI[{SC[i].x,SC[i].y}]=i;
    for(int i=0;i<(int)CEL.size();i++) FI[{CEL[i].x,CEL[i].y}]=i;
    long long fb,fh;
    auto base=enum_inits({{-1,0},{-1,1},{0,0},{0,1}},fb);
    auto behind=enum_inits({{-2,0},{-2,1},{-1,0},{-1,1},{0,0},{0,1}},fh);
    if(fb!=50785 || base.size()!=12201 || fh!=7255 || behind.size()!=1743){
        cerr<<"bad counts "<<fb<<" "<<base.size()<<" "<<fh<<" "<<behind.size()<<"\n"; return 2;
    }
    vector<tuple<string,int,vector<uint32_t>*,bool>> req={
      {"h_generated_D191",191,&behind,false},
      {"h_terminal_D194",194,&behind,true},
      {"guard_D211",211,&base,false}
    };
    cout<<"PASS exact R08/E0011 L7 stage-DP certificate\n";
    cout<<"base_full="<<fb<<" base_desc="<<base.size()<<" behind_full="<<fh<<" behind_desc="<<behind.size()<<"\n";
    for(auto &[name,D,iv,term]:req){
        int bl=0; Rat r=best_stage(D,*iv,term,bl);
        cout<<name<<" best_lambda="<<bl<<" p_exact="<<ss(r.num)<<"/"<<ss(r.den)<<"\n";
    }
    return 0;
}
