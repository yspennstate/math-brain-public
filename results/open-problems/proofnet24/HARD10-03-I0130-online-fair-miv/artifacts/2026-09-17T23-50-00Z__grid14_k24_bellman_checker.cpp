#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <tuple>
#include <utility>
#include <vector>
using namespace std;

static const int Q=14;
static const int TARGET=-24;
static const pair<int,int> START={Q,3*Q};
static const int DEPTH=42;

struct ActionRec {int a,b; pair<int,int> c1,c2;};
map<tuple<int,int,int>, uint8_t> memo; // 1 lose, 2 win
map<tuple<int,int,int>, ActionRec> policy;
vector<pair<int,int>> actions;

static pair<int,int> srt(int u,int v){ if(u<=v) return {u,v}; return {v,u}; }

bool win(int x,int y,int d){
    assert(x<=y);
    if(x<=TARGET || y<=TARGET) return true;
    if(d==0) return false;
    auto key=make_tuple(x,y,d);
    auto it=memo.find(key); if(it!=memo.end()) return it->second==2;
    for(auto [a,b]:actions){
        auto c1=srt(x+a,y-b);
        auto c2=srt(x-a,y+b);
        if(win(c1.first,c1.second,d-1) && win(c2.first,c2.second,d-1)){
            memo[key]=2; policy[key]={a,b,c1,c2}; return true;
        }
    }
    memo[key]=1; return false;
}

int main(){
    for(int a=0;a<=Q;a++) for(int b=0;b<=Q;b++) if(a||b) actions.push_back({a,b});
    sort(actions.begin(),actions.end(),[](auto p, auto q){
        int sp=p.first+p.second, sq=q.first+q.second;
        if(sp!=sq) return sp>sq;
        int dp=abs(p.first-p.second), dq=abs(q.first-q.second);
        if(dp!=dq) return dp>dq;
        if(p.first!=q.first) return p.first>q.first;
        return p.second>q.second;
    });
    for(int d=0; d<DEPTH; ++d){
        bool w=win(START.first,START.second,d);
        if(w){ cerr<<"unexpected winning depth "<<d<<"\n"; return 2; }
    }
    if(!win(START.first,START.second,DEPTH)){ cerr<<"root not winning\n"; return 3; }

    set<tuple<int,int,int>> seen;
    vector<tuple<int,int,int>> stack{{START.first,START.second,DEPTH}};
    long long terminals=0;
    map<pair<int,int>,long long> action_counts;
    while(!stack.empty()){
        auto key=stack.back(); stack.pop_back();
        if(seen.count(key)) continue;
        seen.insert(key);
        auto [x,y,d]=key;
        assert(x<=y);
        if(x<=TARGET || y<=TARGET){ terminals++; continue; }
        assert(d>0);
        auto it=policy.find(key); assert(it!=policy.end());
        auto r=it->second;
        assert(0<=r.a && r.a<=Q && 0<=r.b && r.b<=Q && (r.a||r.b));
        assert(r.c1==srt(x+r.a,y-r.b));
        assert(r.c2==srt(x-r.a,y+r.b));
        action_counts[{r.a,r.b}]++;
        stack.push_back({r.c1.first,r.c1.second,d-1});
        stack.push_back({r.c2.first,r.c2.second,d-1});
    }
    assert(terminals>0);

    // Exact source arithmetic by integer cross-multiplication.
    // U_new = 101/105 = 1 - (24/14)/45.
    assert(105-101==4);
    assert(24*105 == 4*14*45); // 24/(14*45)=4/105
    assert(3+DEPTH==45);
    assert(2*105 < 3*101);     // 2/3 < 101/105
    // Width: 101/105 - 19/30 = 23/70.
    assert(101*30 - 19*105 == 23*45); // denominator 3150; 3150/70=45
    // Improvement over 445/462 is exactly 1/770.
    assert(445*105 - 101*462 == 63); // denominator 48510; 48510/770=63

    cout<<"I0130_GRID14_K24_BELLMAN_CERTIFICATE_PASS\n";
    cout<<"grid_denominator=14\n";
    cout<<"target_safety=-24/14=-12/7\n";
    cout<<"balanced_start_safety=(1,3)\n";
    cout<<"first_winning_additional_horizon=42\n";
    cout<<"max_total_goods=45\n";
    cout<<"source_valid_upper_bound=101/105\n";
    cout<<"current_lower_bound=19/30\n";
    cout<<"new_metric_width=23/70\n";
    cout<<"upper_bound_improvement=1/770\n";
    cout<<"memoized_nonterminal_states="<<memo.size()<<"\n";
    cout<<"reachable_policy_dag_nodes="<<seen.size()<<"\n";
    cout<<"reachable_terminal_nodes="<<terminals<<"\n";
    cout<<"distinct_actions_used="<<action_counts.size()<<"\n";
    cout<<"action_counts=";
    bool first=true;
    for(auto const& [ab,c]:action_counts){
        if(!first) cout<<";"; first=false;
        cout<<"("<<ab.first<<"/14,"<<ab.second<<"/14):"<<c;
    }
    cout<<"\n";
    return 0;
}
