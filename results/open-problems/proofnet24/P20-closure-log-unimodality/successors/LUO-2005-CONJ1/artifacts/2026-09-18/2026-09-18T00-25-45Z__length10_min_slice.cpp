#include <bits/stdc++.h>
using namespace std;
static const int N=10, U=1<<N;
struct QMeta{vector<int> q; int m,d,v,c0,c1,card; array<uint64_t,16> bits; vector<int> prof;};

void genPatternsRec(int n,int pos,int maxv,vector<int>&pat,const function<void(const vector<int>&)>& f){
    if(pos==n){f(pat);return;}
    pat.push_back(-1); genPatternsRec(n,pos+1,maxv,pat,f); pat.pop_back();
    pat.push_back(-2); genPatternsRec(n,pos+1,maxv,pat,f); pat.pop_back();
    for(int v=0;v<=maxv+1;v++){pat.push_back(v); genPatternsRec(n,pos+1,max(maxv,v),pat,f); pat.pop_back();}
}
void genPatterns(int n,const function<void(const vector<int>&)>& f){vector<int> p; p.reserve(n); genPatternsRec(n,0,-1,p,f);} 

struct Stats{int v,c0,c1; vector<int> occ,prof;};
Stats stats(const vector<int>& p){
    int maxv=-1,c0=0,c1=0; for(int s:p){if(s>=0) maxv=max(maxv,s); else if(s==-1)c0++; else c1++;}
    vector<int> occ(maxv+1,0); for(int s:p) if(s>=0) occ[s]++;
    vector<int> prof=occ; sort(prof.begin(),prof.end());
    return {(int)occ.size(),c0,c1,occ,prof};
}
long long Fcoeff(const vector<int>& a,int d){
    if(a.empty()) return 0;
    long long tot=0;
    function<void(int,int,int)> rec=[&](int i,int rem,int se){
        if(i==(int)a.size()){if(rem==0) tot += 1LL<<se; return;}
        for(int e=0;e*a[i]<=rem;e++) rec(i+1,rem-e*a[i],se+e);
    }; rec(0,d,0); return tot;
}

void setbit(array<uint64_t,16>& b,int w){b[w>>6] |= 1ULL<<(w&63);} 
int popbits(const array<uint64_t,16>&b){int s=0;for(auto x:b)s+=__builtin_popcountll(x);return s;}

array<uint64_t,16> sliceBits(const vector<int>& q,const Stats& st){
    int m=q.size(),d=N-m,v=st.v; array<uint64_t,16> bits{};
    vector<int> e(v,0);
    function<void(int,int)> exrec=[&](int i,int rem){
        if(i==v){
            if(rem) return;
            vector<int> L(v); for(int x=0;x<v;x++) L[x]=1+e[x];
            int base=0,pos=0; vector<int> masks; vector<vector<int>> vm(v); for(int x=0;x<v;x++) vm[x].assign(L[x],0);
            for(int s:q){
                if(s==-1){pos++;}
                else if(s==-2){base |= 1<<(N-1-pos); pos++;}
                else {for(int j=0;j<L[s];j++){vm[s][j] |= 1<<(N-1-(pos+j));} pos+=L[s];}
            }
            if(pos!=N){cerr<<"badpos"; exit(9);} for(int x=0;x<v;x++) for(int mm:vm[x]) masks.push_back(mm);
            vector<int> words; words.reserve(1<<masks.size()); words.push_back(base);
            for(int mm:masks){int sz=words.size(); for(int k=0;k<sz;k++) words.push_back(words[k]|mm);} 
            for(int w:words) setbit(bits,w);
            return;
        }
        int a=st.occ[i]; for(int z=0;z*a<=rem;z++){e[i]=z; exrec(i+1,rem-z*a);} e[i]=0;
    };
    exrec(0,d); return bits;
}

vector<int> minWords(const vector<int>&p,const Stats&st){
    int base=0; vector<int> vm(st.v,0); for(int pos=0;pos<N;pos++){int s=p[pos],b=1<<(N-1-pos); if(s==-2)base|=b; else if(s>=0)vm[s]|=b;}
    vector<int> ws; ws.reserve(1<<st.v); ws.push_back(base); for(int mm:vm){int sz=ws.size();for(int i=0;i<sz;i++)ws.push_back(ws[i]|mm);} return ws;
}

string ps(const vector<int>&p){ostringstream o;o<<"[";for(size_t i=0;i<p.size();i++){if(i)o<<",";o<<p[i];}o<<"]";return o.str();}

int main(){
    // Independent generator sanity check against the canonical-count formula
    // sum_{k=0}^n binom(n,k) 2^{n-k} Bell(k), n=1,...,10.
    const long long expected[11] = {0,3,10,37,151,674,3263,17007,94828,562595,3535027};
    cout << "CANONICAL_COUNTS";
    for(int n=1;n<=N;n++){
        long long cnt=0; genPatterns(n,[&](const vector<int>&){cnt++;});
        if(cnt!=expected[n]){cerr<<"canonical count mismatch n="<<n<<" got="<<cnt<<" expected="<<expected[n]<<"\n"; return 8;}
        cout << " " << n << ":" << cnt;
    }
    cout << "\n";

    vector<QMeta> qm; map<pair<int,int>,int> bydv;
    for(int m:{8,9}){int d=N-m; genPatterns(m,[&](const vector<int>&q){
        auto st=stats(q); if(st.v>N-2*d) return; int rho=0;for(int a:st.prof)rho+=a-1; if(rho<d)return; if(Fcoeff(st.prof,d)< (1LL<<(2*d))) return;
        auto bits=sliceBits(q,st); int card=popbits(bits); qm.push_back({q,m,d,st.v,st.c0,st.c1,card,bits,st.prof}); bydv[{d,st.v}]++;
    });}
    cout<<"QMETA "<<qm.size()<<" ";for(auto [k,v]:bydv)cout<<"d"<<k.first<<"v"<<k.second<<":"<<v<<" ";cout<<"\n";
    long long totalp=0;
    for(int vp=0;vp<=10;vp++){
        vector<int> ids; int need=1<<vp; for(int i=0;i<(int)qm.size();i++) if(vp-qm[i].v>=2*qm[i].d && qm[i].card>=need) ids.push_back(i);
        cout<<"VP_START "<<vp<<" QARR="<<ids.size()<<"\n"; if(ids.empty())continue;
        int Q=ids.size(), W=(Q+63)/64; vector<uint64_t> incidence((size_t)U*W,0);
        vector<int> freq(U,0);
        for(int j=0;j<Q;j++){
            auto &b=qm[ids[j]].bits; for(int w=0;w<U;w++) if((b[w>>6]>>(w&63))&1ULL){incidence[(size_t)w*W+(j>>6)] |= 1ULL<<(j&63);freq[w]++;}
        }
        vector<uint64_t> cmask((size_t)(N+1)*(N+1)*W,0);
        auto cmoff=[&](int a,int b){return ((size_t)a*(N+1)+b)*W;};
        for(int j=0;j<Q;j++){auto &qq=qm[ids[j]];for(int a=qq.c0;a<=N;a++)for(int b=qq.c1;b<=N;b++)cmask[cmoff(a,b)+(j>>6)] |= 1ULL<<(j&63);}
        vector<uint64_t> cand(W); long long pc=0; bool found=false;
        genPatterns(N,[&](const vector<int>&p){if(found)return; auto st=stats(p); if(st.v!=vp)return; size_t off=cmoff(st.c0,st.c1); bool any=false; for(int z=0;z<W;z++){cand[z]=cmask[off+z];any|=cand[z];} if(!any)return; pc++;
            auto ws=minWords(p,st); sort(ws.begin(),ws.end(),[&](int a,int b){return freq[a]<freq[b];});
            for(int w:ws){any=false; size_t io=(size_t)w*W; for(int z=0;z<W;z++){cand[z]&=incidence[io+z]; any|=cand[z];} if(!any)break;}
            if(any){int j=-1;for(int z=0;z<W;z++)if(cand[z]){j=z*64+__builtin_ctzll(cand[z]);break;} auto &qq=qm[ids[j]]; cout<<"SURVIVOR vp="<<vp<<" p="<<ps(p)<<" pc="<<st.c0<<","<<st.c1<<" q="<<ps(qq.q)<<" m="<<qq.m<<" d="<<qq.d<<" vq="<<qq.v<<" qc="<<qq.c0<<","<<qq.c1<<" card="<<qq.card<<"\n"; found=true;}
        });
        if(found) return 2; totalp+=pc; cout<<"VP_DONE "<<vp<<" P_CHECKED="<<pc<<" NO_SURVIVOR\n";
    }
    cout<<"NO_BAD_MINSLICE_SURVIVOR_D1_D2_N10\n";
    cout<<"TOTAL_P_CHECKED "<<totalp<<"\n";
    cout<<"ALL_EXACT_CHECKS_PASS\n";
}
