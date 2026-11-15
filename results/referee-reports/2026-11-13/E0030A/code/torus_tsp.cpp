// Candidate 2-opt, Or-opt(1,2,3), and double-bridge iterated local search.
// No external tour solver; no optimality claim. Distances are never rounded.
#include <algorithm>
#include <array>
#include <cassert>
#include <chrono>
#include <cmath>
#include <cstdint>
#include <deque>
#include <iomanip>
#include <iostream>
#include <numeric>
#include <random>
#include <stdexcept>
#include <vector>
using namespace std;
struct Solver {
    int n, k; bool audit; vector<array<double,2>> xy; vector<vector<int>> nn;
    vector<int> t, pos, order; mt19937_64 rng;
    deque<int> active;vector<char> queued;bool fast_mode=false;
    Solver(int n_, int k_, uint64_t seed, bool audit_): n(n_), k(k_), audit(audit_),
      xy(n), nn(n,vector<int>(k)),t(n),pos(n),order(n),rng(seed),queued(n) {
        iota(order.begin(),order.end(),0);
    }
    double d(int a,int b) const {
        double x=abs(xy[a][0]-xy[b][0]), y=abs(xy[a][1]-xy[b][1]);
        x=min(x,1-x); y=min(y,1-y); return sqrt(x*x+y*y);
    }
    void positions(){ for(int i=0;i<n;i++)pos[t[i]]=i; }
    void enqueue(int a){if(!queued[a]){queued[a]=1;active.push_back(a);}}
    void touch(int a){
        if(!fast_mode)return;
        enqueue(a);
        for(int c:nn[a])enqueue(c);
        for(int j=-3;j<=3;j++)enqueue(t[(pos[a]+n+j)%n]);
    }
    double length() const { double s=0; for(int i=0;i<n;i++)s+=d(t[i],t[(i+1)%n]);return s; }
    void check() const {
        vector<int> cnt(n); for(int i=0;i<n;i++){
            if(t[i]<0||t[i]>=n||++cnt[t[i]]!=1||pos[t[i]]!=i)
                throw runtime_error("invalid tour or inverse permutation");
        }
    }
    void initialize(){
        vector<char> used(n); int a=int(rng()%n);
        for(int i=0;i<n;i++){
            t[i]=a; used[a]=1; if(i==n-1)break;
            int b=-1; for(int c:nn[a]) if(!used[c]){b=c;break;}
            if(b<0){double best=1e9;for(int c=0;c<n;c++)if(!used[c]){
                double z=d(a,c);if(z<best){best=z;b=c;}
            }}
            a=b;
        }
        positions();check();
    }
    bool two(int i,int j){
        if(i>j)swap(i,j);
        if(j-i<=1||(i==0&&j==n-1))return false;
        int a=t[i],b=t[i+1],c=t[j],e=t[(j+1)%n];
        double delta=d(a,c)+d(b,e)-d(a,b)-d(c,e);
        if(delta>=-1e-12)return false;
        double before=audit?length():0;
        reverse(t.begin()+i+1,t.begin()+j+1);
        for(int l=i+1;l<=j;l++)pos[t[l]]=l;
        touch(a);touch(b);touch(c);touch(e);
        if(audit){check(); if(abs(length()-before-delta)>1e-9)throw runtime_error("2opt delta");}
        return true;
    }
    bool two_pass(){
        bool changed=false;shuffle(order.begin(),order.end(),rng);
        for(int a:order){
            for(int c:nn[a]){
                int i=pos[a],j=pos[c];
                if(two(i,j)||two((i+n-1)%n,(j+n-1)%n)){changed=true;break;}
            }
        }
        return changed;
    }
    bool or_move(int a,int c,int count){
        int i=pos[a],j=pos[c];
        if(i+count>n||(j>=i&&j<i+count)||j==(i+n-1)%n)return false;
        int u=t[(i+n-1)%n],tail=t[i+count-1],v=t[(i+count)%n],b=t[(j+1)%n];
        double delta=d(u,v)+d(c,a)+d(tail,b)-d(u,a)-d(tail,v)-d(c,b);
        if(delta>=-1e-12)return false;
        double before=audit?length():0;
        int lo,hi;
        if(j<i){rotate(t.begin()+j+1,t.begin()+i,t.begin()+i+count);lo=j+1;hi=i+count;}
        else {rotate(t.begin()+i,t.begin()+i+count,t.begin()+j+1);lo=i;hi=j+1;}
        for(int l=lo;l<hi;l++)pos[t[l]]=l;
        touch(u);touch(a);touch(tail);touch(v);touch(c);touch(b);
        if(audit){check();if(abs(length()-before-delta)>1e-9)throw runtime_error("Or-opt delta");}
        return true;
    }
    bool or_pass(){
        bool changed=false;shuffle(order.begin(),order.end(),rng);
        for(int a:order){bool moved=false;
            for(int count=1;count<=3&&!moved;count++)
                for(int z=0;z<min(k,16);z++) if(or_move(a,nn[a][z],count)){
                    changed=true;moved=true;break;
                }
        }
        return changed;
    }
    void optimize(){
        double before=length();
        // Finite safeguards are reported in output through cap_hits.
        bool settled=false;
        for(int outer=0;outer<80;outer++){
            bool change=false;
            for(int p=0;p<100;p++){
                bool z=two_pass();change|=z;if(!z)break;if(p==99)cap_hits++;
            }
            bool z=or_pass();change|=z;
            if(!change){settled=true;break;}
        }
        if(!settled)cap_hits++;
        check();if(length()>before+1e-8)throw runtime_error("local search increased cost");
    }
    int cap_hits=0;
    void fast_optimize(bool all=false){
        fast_mode=true;
        if(all){shuffle(order.begin(),order.end(),rng);for(int a:order)enqueue(a);}
        int processed=0;
        while(!active.empty()){
            int a=active.front();active.pop_front();queued[a]=0;
            bool changed=false;
            for(int c:nn[a]){
                int i=pos[a],j=pos[c];
                if(two(i,j)||two((i+n-1)%n,(j+n-1)%n)){changed=true;break;}
            }
            if(!changed){
                for(int count=1;count<=3&&!changed;count++)
                    for(int z=0;z<min(k,16);z++)if(or_move(a,nn[a][z],count)){
                        changed=true;break;
                    }
            }
            if(++processed>1000*n){cap_hits++;break;}
        }
        while(!active.empty()){queued[active.front()]=0;active.pop_front();}
        fast_mode=false;
        if(audit)check();
    }
    void kick(){
        if(n<8){shuffle(t.begin(),t.end(),rng);positions();return;}
        array<int,4> cut;
        for(int i=0;i<4;i++){
            do {cut[i]=1+int(rng()%(n-1));}while(find(cut.begin(),cut.begin()+i,cut[i])!=cut.begin()+i);
        }
        sort(cut.begin(),cut.end());int a=cut[0],b=cut[1],c=cut[2],e=cut[3];
        vector<int> v;v.reserve(n);
        auto add=[&](int lo,int hi){v.insert(v.end(),t.begin()+lo,t.begin()+hi);};
        add(0,a);add(c,e);add(b,c);add(a,b);add(e,n);t.swap(v);positions();
        if(audit)check();
    }
    void short_kick(){
        if(n<12){kick();return;}
        int span=min(n-1,12+int(rng()%37));
        int start=int(rng()%(n-span));array<int,4> cut;
        for(int i=0;i<4;i++){
            do{cut[i]=start+int(rng()%(span+1));}
            while(find(cut.begin(),cut.begin()+i,cut[i])!=cut.begin()+i);
        }
        sort(cut.begin(),cut.end());int a=cut[0],b=cut[1],c=cut[2],e=cut[3];
        vector<int> v;v.reserve(e-a);
        v.insert(v.end(),t.begin()+c,t.begin()+e);
        v.insert(v.end(),t.begin()+b,t.begin()+c);
        v.insert(v.end(),t.begin()+a,t.begin()+b);
        copy(v.begin(),v.end(),t.begin()+a);
        for(int i=a;i<e;i++)pos[t[i]]=i;
        if(fast_mode){
            touch(t[(a+n-1)%n]);touch(t[a]);touch(t[e-1]);touch(t[e%n]);
            // All vertices in the short segment cover every changed edge.
            for(int i=a;i<e;i++)enqueue(t[i]);
        }
        if(audit)check();
    }
    struct Result{double initial,base,best;vector<int> tour;};
    Result run(int kicks){
        initialize();fast_optimize(true);optimize();double initial=length(),best=initial,base=initial;
        vector<int> incumbent=t;
        int total=kicks*max(1,n/50);
        for(int i=0;i<total;i++){
            t=incumbent;positions();
            if(i%max(1,n/50)==0){
                rotate(t.begin(),t.begin()+int(rng()%n),t.end());positions();
                incumbent=t;
            }
            fast_mode=true;short_kick();fast_optimize();
            double cost=length();
            if(cost<best-1e-11){best=cost;incumbent=t;}
            if(i+1==max(1,total/4))base=best;
        }
        t=incumbent;positions();optimize();
        if(length()<best){best=length();incumbent=t;}
        return {initial,base,best,incumbent};
    }
};
int main(){
    ios::sync_with_stdio(false);cin.tie(nullptr);
    int n,k,kicks,audit;uint64_t seed;
    if(!(cin>>n>>k>>kicks>>seed>>audit))return 2;
    if(n<3||n>10000||k<2||k>=n||kicks<0)return 3;
    Solver s(n,k,seed,audit);
    for(auto &p:s.xy)cin>>p[0]>>p[1];
    for(auto &v:s.nn)for(auto &a:v)cin>>a;
    if(!cin)return 4;
    auto begin=chrono::steady_clock::now();
    auto x=s.run(kicks);
    s.rng.seed(seed^uint64_t(0x9e3779b97f4a7c15ULL));
    auto y=s.run(kicks);
    auto &best=x.best<=y.best?x:y;
    double seconds=chrono::duration<double>(chrono::steady_clock::now()-begin).count();
    cout<<setprecision(17)<<"{\"initial1\":"<<x.initial<<",\"base1\":"<<x.base
        <<",\"best1\":"<<x.best<<",\"initial2\":"<<y.initial<<",\"base2\":"<<y.base
        <<",\"best2\":"<<y.best<<",\"best\":"<<best.best<<",\"cap_hits\":"<<s.cap_hits
        <<",\"seconds\":"<<seconds<<",\"tour\":[";
    for(int i=0;i<n;i++){if(i)cout<<',';cout<<best.tour[i];}cout<<"]}\n";
}
