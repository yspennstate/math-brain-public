#include <bits/stdc++.h>
#include <boost/multiprecision/cpp_int.hpp>
using namespace std; using boost::multiprecision::cpp_int;

struct C{int x,y; bool operator<(C const&o)const{return tie(x,y)<tie(o.x,o.y);} bool operator==(C const&o)const{return x==o.x&&y==o.y;}};
vector<C> dirs={{1,0},{-1,0},{0,1},{0,-1}};
vector<C> STATE={{-2,0},{-2,1},{-1,-1},{-1,0},{-1,1},{-1,2},{0,-1},{0,0},{0,1},{0,2},{1,-1},{1,0},{1,1},{2,0}};
vector<C> FULL={{-2,0},{-2,1},{-1,-1},{-1,0},{-1,1},{-1,2},{0,-1},{0,0},{0,1},{0,2},{1,-1},{1,0},{1,1},{1,2},{2,0},{2,1}};
map<pair<int,int>,int> si,fi;
int p3[15];
int getd(int code,int i){return (code/p3[i])%3;}
int setd(int code,int i,int v){int old=getd(code,i); return code+(v-old)*p3[i];}
int enc(const vector<int>&a){int z=0;for(int i=0;i<(int)a.size();++i)z+=a[i]*p3[i];return z;}

bool target(int code){
    static int id[]={3,4,7,8,11,12};
    for(int i:id) if(getd(code,i)!=0) return false; return true;
}

struct Label { int kind; C a,b; };
vector<Label> labv;

vector<pair<int,int>> trans(int code,int li){
    auto L=labv[li]; map<int,int> out;
    if(L.kind==0){
        auto it=si.find(make_pair(L.a.x,L.a.y)); if(it==si.end()) throw runtime_error("CO root not state"); int i=it->second;
        if(getd(code,i)!=0){out[code]+=72; goto done;}
        {
            int c2=setd(code,i,1); vector<int> os;
            for(auto d:dirs){ auto jt=si.find(make_pair(L.a.x+d.x,L.a.y+d.y)); if(jt!=si.end() && getd(c2,jt->second)==2) os.push_back(jt->second); }
            if(os.empty()){out[c2]+=72; goto done;}
            int w=72/(int)os.size();
            for(int j:os){int t=setd(c2,i,0); t=setd(t,j,0); out[t]+=w;}
        }
    } else {
        int ia=si.at(make_pair(L.a.x,L.a.y)), ib=si.at(make_pair(L.b.x,L.b.y));
        if(getd(code,ia)!=0 || getd(code,ib)!=0){out[code]+=36; goto done;}
        {
            int c2=setd(setd(code,ia,2),ib,2);
            vector<int> ca,cb;
            for(auto d:dirs){ auto jt=si.find(make_pair(L.a.x+d.x,L.a.y+d.y)); if(jt!=si.end() && getd(c2,jt->second)==1) ca.push_back(jt->second); }
            for(auto d:dirs){ auto jt=si.find(make_pair(L.b.x+d.x,L.b.y+d.y)); if(jt!=si.end() && getd(c2,jt->second)==1) cb.push_back(jt->second); }
            vector<int> A=ca.empty()?vector<int>{-1}:ca, B=cb.empty()?vector<int>{-1}:cb;
            int den=A.size()*B.size(); int w=36/den;
            for(int qa:A)for(int qb:B){
                int t=c2;
                if(qa!=-1){ t=setd(t,ia,0); t=setd(t,qa,0); }
                if(qb!=-1){ t=setd(t,ib,0); t=setd(t,qb,0); }
                out[t]+=w;
            }
        }
    }
done:
    return vector<pair<int,int>>(out.begin(),out.end());
}

bool stable_full(const vector<int>&a){
    for(int i=0;i<(int)FULL.size();++i){
        C c=FULL[i]; int av=a[i];
        for(C d: vector<C>{{1,0},{0,1}}){ auto jt=fi.find({c.x+d.x,c.y+d.y}); if(jt!=fi.end()){int b=a[jt->second]; if((av==1&&b==2)||(av==2&&b==1)) return false;}}
    }
    return true;
}

vector<int> enumerate_inits(set<pair<int,int>> fixed){
    vector<int> vars; for(int i=0;i<(int)FULL.size();++i) if(!fixed.count({FULL[i].x,FULL[i].y})) vars.push_back(i);
    long long total=1; for(size_t i=0;i<vars.size();++i) total*=3;
    unordered_set<int> S; vector<int>a(FULL.size());
    for(long long mask=0;mask<total;++mask){
        fill(a.begin(),a.end(),0); long long q=mask;
        for(int idx:vars){a[idx]=q%3;q/=3;}
        if(!stable_full(a)) continue;
        vector<int>s(STATE.size()); for(int i=0;i<(int)STATE.size();++i)s[i]=a[fi.at({STATE[i].x,STATE[i].y})];
        S.insert(enc(s));
    }
    vector<int> v(S.begin(),S.end()); sort(v.begin(),v.end()); return v;
}

vector<int> closure(const vector<int>&inits,const vector<int>&allowed){
    unordered_set<int>S(inits.begin(),inits.end()); vector<int> front=inits;
    for(int depth=0; depth<20 && !front.empty(); ++depth){ vector<int> nf; for(int s:front){ for(int li:allowed) for(auto [t,w]:trans(s,li)) if(S.insert(t).second) nf.push_back(t);} front.swap(nf); }
    vector<int> v(S.begin(),S.end()); sort(v.begin(),v.end()); return v;
}

struct Stage {string name; int D; vector<int>* inits; vector<int> allowed;};

vector<cpp_int> solve_stage(const Stage& st, int N, int H, const vector<cpp_int>* nextm){
    vector<int> states=closure(*st.inits, st.allowed);
    unordered_map<int,int> pos; pos.reserve(states.size()*2); for(int i=0;i<(int)states.size();++i)pos[states[i]]=i;
    vector<vector<pair<int,int>>> edges(states.size());
    for(int i=0;i<(int)states.size();++i){
        map<int,int> acc; for(int li:st.allowed) for(auto [t,w]:trans(states[i],li)) acc[t]+=w;
        for(auto [t,w]:acc) edges[i].push_back({pos.at(t),w});
    }
    vector<int> init_idx; init_idx.reserve(st.inits->size()); for(int s:*st.inits) init_idx.push_back(pos.at(s));
    int nullw=36*(222-st.D);
    vector<cpp_int> prev(states.size()),cur(states.size()),m(N+1);
    if(nextm==nullptr){ for(int i=0;i<(int)states.size();++i) prev[i]=target(states[i])?1:0; }
    else { for(int i=0;i<(int)states.size();++i) prev[i]=target(states[i])?(*nextm)[0]:0; }
    bool first=true; for(int i:init_idx){ if(first||prev[i]<m[0]){m[0]=prev[i];first=false;} }
    cerr<<st.name<<" states="<<states.size()<<" m0="<<m[0]<<"\n";
    for(int n=1;n<=N;++n){
        for(int i=0;i<(int)states.size();++i){
            if(nextm && target(states[i])) { cur[i]=(*nextm)[n]; continue; }
            cpp_int z=0;
            if(nullw) z += cpp_int(nullw)*prev[i];
            for(auto [j,w]:edges[i]) z += cpp_int(w)*prev[j];
            cur[i]=z;
        }
        first=true; for(int i:init_idx){ if(first||cur[i]<m[n]){m[n]=cur[i];first=false;} }
        prev.swap(cur);
        if(n%10==0) cerr<<"  n="<<n<<" m_digits~"<<m[n].backend().size()<<"\n";
    }
    return m;
}

vector<cpp_int> firsthit_min_kernel(const Stage& st, int N, int H){
    vector<int> states=closure(*st.inits, st.allowed);
    unordered_map<int,int> pos; pos.reserve(states.size()*2); for(int i=0;i<(int)states.size();++i)pos[states[i]]=i;
    vector<vector<pair<int,int>>> edges(states.size());
    for(int i=0;i<(int)states.size();++i){ map<int,int> acc; for(int li:st.allowed) for(auto [t,w]:trans(states[i],li)) acc[t]+=w; for(auto [t,w]:acc) edges[i].push_back({pos.at(t),w}); }
    vector<int> init_idx; for(int s:*st.inits) init_idx.push_back(pos.at(s));
    int nullw=36*(222-st.D);
    vector<cpp_int> prev(states.size()),cur(states.size()),a(N+1);
    for(int i=0;i<(int)states.size();++i) prev[i]=target(states[i])?1:0;
    bool first=true; for(int i:init_idx){ cpp_int z=prev[i]; if(first||z<a[0]){a[0]=z;first=false;} }
    for(int n=1;n<=N;++n){
        for(int i=0;i<(int)states.size();++i){
            if(target(states[i])) { cur[i]=1; for(int k=0;k<n;k++) cur[i]*=H; continue; }
            cpp_int z=0; if(nullw) z+=cpp_int(nullw)*prev[i]; for(auto [j,w]:edges[i]) z+=cpp_int(w)*prev[j]; cur[i]=z;
        }
        first=true; for(int i:init_idx){ cpp_int d=cur[i]-cpp_int(H)*prev[i]; if(d<0){cerr<<"negative firsthit\n"; exit(3);} if(first||d<a[n]){a[n]=d;first=false;} }
        prev.swap(cur);
    }
    return a;
}

int main(int argc,char**argv){
    int N=120; if(argc>1)N=atoi(argv[1]);
    p3[0]=1;for(int i=1;i<15;++i)p3[i]=p3[i-1]*3;
    for(int i=0;i<(int)STATE.size();++i)si[{STATE[i].x,STATE[i].y}]=i;
    for(int i=0;i<(int)FULL.size();++i)fi[{FULL[i].x,FULL[i].y}]=i;
    labv={
      {0,{0,0},{}}, {1,{-1,1},{0,1}}, {0,{0,1},{}}, {0,{1,0},{}},
      {1,{-1,0},{-1,1}}, {1,{0,0},{0,1}}, {0,{-1,1},{}},
      {1,{-1,0},{0,0}}, {0,{-1,0},{}}, {1,{0,0},{1,0}}
    };
    set<pair<int,int>> fixedbase={{-1,0},{-1,1},{0,0},{0,1}};
    auto fixedbeh=fixedbase; fixedbeh.insert({-2,0}); fixedbeh.insert({-2,1});
    auto base=enumerate_inits(fixedbase), beh=enumerate_inits(fixedbeh);
    cerr<<"inits base="<<base.size()<<" beh="<<beh.size()<<"\n";
    if(base.size()!=12201 || beh.size()!=1743){ cerr<<"entrance-count mismatch\n"; return 2; }
    vector<int> all={0,1,2,3,4,5,6,7,8,9}; vector<int> term={0,1,2,4,5,6,7,8};
    vector<Stage> stages={
      {"h3",150,&beh,all},{"h4",167,&beh,all},{"h5",178,&beh,all},{"h6",187,&beh,all},
      {"h7",197,&beh,all},{"h8term",201,&beh,term},{"gdown",218,&base,all},{"gup",222,&base,all}
    };
    int H=36*222;
    vector<cpp_int> next, finalm;
    for(int j=7;j>=0;--j){ auto m=solve_stage(stages[j],N,H, j==7?nullptr:&next); if(j==7) finalm=m; next.swap(m); }
    vector<vector<cpp_int>> kernels;
    for(int j=0;j<7;++j) kernels.push_back(firsthit_min_kernel(stages[j],N,H));
    vector<cpp_int> conv(N+1); conv[0]=1;
    for(int j=0;j<7;++j){ vector<cpp_int> nc(N+1); for(int n=0;n<=N;++n) if(conv[n]!=0) for(int k=0;n+k<=N;++k) if(kernels[j][k]!=0) nc[n+k]+=conv[n]*kernels[j][k]; conv.swap(nc); }
    vector<cpp_int> forward(N+1); for(int n=0;n<=N;++n) for(int k=0;k<=n;++k) if(conv[k]!=0 && finalm[n-k]!=0) forward[n]+=conv[k]*finalm[n-k];
    if(N==40){
      if(next[18] != cpp_int("1335241765123705160600345389301760")) return 4;
      if(next[22] != cpp_int("21594360744990667130171544797248513823121711562752")) return 5;
      if(next[30] != cpp_int("3430163092891565906095118909235211804747824182107317023868347474414853817368576")) return 6;
      if(next[40] != cpp_int("3238122226406033110010001541728022258844508450664395979649766319648774405894871547125803946961701103992832")) return 7;
      for(int n=0;n<=40;++n) if(forward[n]!=0) return 8;
    }
    cout<<"H "<<H<<" N "<<N<<"\n";
    for(int n=0;n<=N;++n){ if(next[n]!=0 || forward[n]!=0) cout<<n<<" "<<next[n]<<" "<<forward[n]<<"\n"; }
    cout<<"PASS exact R08/E0011 global fixed-top backward uniformization; naive forward pointwise-min envelope is zero through N="<<N<<"\n";
}
