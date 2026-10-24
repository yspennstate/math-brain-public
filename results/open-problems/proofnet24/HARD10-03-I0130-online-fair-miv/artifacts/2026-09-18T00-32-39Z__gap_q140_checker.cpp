#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <set>
#include <tuple>
#include <utility>
#include <vector>
using namespace std;

static constexpr int Q=140;
static constexpr int H=43;
static constexpr int START_D=2*Q;

struct Act{short a,b;};

int main(){
    const int maxD = START_D + 2*Q*H;
    vector<pair<int,int>> actions;
    for(int a=0;a<=Q;a++) for(int b=0;b<=Q;b++) actions.push_back({a,b});

    vector<vector<int>> G(H+1);
    vector<vector<Act>> P(H+1);
    G[0].assign(maxD+1,0);
    P[0].assign(maxD+1,Act{0,0});
    vector<int> root(H+1,0);

    for(int h=1;h<=H;h++){
        int lim=maxD-2*Q*h;
        G[h].assign(lim+1,0);
        P[h].assign(lim+1,Act{0,0});
        for(int D=0;D<=lim;D++){
            // The (0,0) action is a legal zero-valued padding good, so G_h is monotone in h.
            int best=INT32_MIN;
            int besta=0,bestb=0;
            for(auto [a,b]:actions){
                int c=a+b;
                int DH=D+c;
                int valH=a + G[h-1][DH];
                int DL,costL;
                if(D>=c){ DL=D-c; costL=-a; }
                else { DL=c-D; costL=b-D; }
                int valL=costL + G[h-1][DL];
                int w=min(valH,valL);
                if(w>best){best=w;besta=a;bestb=b;}
            }
            G[h][D]=best;
            P[h][D]=Act{(short)besta,(short)bestb};
        }
        root[h]=G[h][START_D];
        assert(root[h]>=root[h-1]);
    }

    assert(G[H][START_D]==427);
    // 427/140 = 61/20 guaranteed decrease from starting lower safety 1.
    assert(427*20==61*140);
    // Final lower safety <= 1 - 61/20 = -41/20.
    assert(20-61==-41);
    // Total goods <= 3+43=46, so factor <= 1-(41/20)/46 = 879/920.
    assert(3+H==46);
    assert(41*920 == 41*20*46);
    assert(920-41==879);
    // Current width: 879/920 - 19/30.
    long long numW=879LL*30-19LL*920;
    long long denW=920LL*30;
    // Reduce the metric width exactly.
    long long a=numW,b=denW; while(b){long long t=a%b;a=b;b=t;} long long g=a;
    // Improvement over 101/105 is exactly 25/3864.
    assert(101LL*920 > 879LL*105);
    assert((101LL*920-879LL*105)*3864 == 25LL*105*920);

    // Verify reachable policy DAG in the exact-H recursion (zero-valued goods may pad).
    set<pair<int,int>> seen;
    vector<pair<int,int>> st{{H,START_D}};
    long long stop_nodes=0, action_nodes=0;
    set<pair<int,int>> used;
    while(!st.empty()){
        auto [h,D]=st.back(); st.pop_back();
        if(!seen.insert({h,D}).second) continue;
        if(h==0){stop_nodes++; continue;}
        Act ac=P[h][D];
        int a0=ac.a,b0=ac.b;
        if(a0==0 && b0==0){
            assert(G[h][D]==G[h-1][D]);
            st.push_back({h-1,D});
            stop_nodes++;
            continue;
        }
        action_nodes++; used.insert({a0,b0});
        int c=a0+b0;
        int DH=D+c;
        int valH=a0+G[h-1][DH];
        int DL,costL;
        if(D>=c){DL=D-c;costL=-a0;}
        else{DL=c-D;costL=b0-D;}
        int valL=costL+G[h-1][DL];
        assert(min(valH,valL)==G[h][D]);
        st.push_back({h-1,DH});
        st.push_back({h-1,DL});
    }

    cout << "I0130_GAP_Q140_CERTIFICATE_PASS\n";
    cout << "grid_denominator="<<Q<<"\n";
    cout << "post_unit_horizon="<<H<<"\n";
    cout << "balanced_start_gap=2\n";
    cout << "guaranteed_lower_safety_decrease=427/140=61/20\n";
    cout << "terminal_lower_safety_at_most=-41/20\n";
    cout << "max_total_goods=46\n";
    cout << "source_valid_upper_bound=879/920\n";
    cout << "current_lower_bound=19/30\n";
    cout << "metric_width_raw="<<numW<<"/"<<denW<<"\n";
    cout << "metric_width_reduced="<<(numW/g)<<"/"<<(denW/g)<<"\n";
    cout << "improvement_over_101_105=25/3864\n";
    cout << "root_action="<<P[H][START_D].a<<"/140,"<<P[H][START_D].b<<"/140\n";
    cout << "reachable_gap_policy_nodes="<<seen.size()<<"\n";
    cout << "reachable_action_nodes="<<action_nodes<<"\n";
    cout << "reachable_stop_or_zero_nodes="<<stop_nodes<<"\n";
    cout << "distinct_actions_used="<<used.size()<<"\n";
    cout << "root_values=";
    for(int h=0;h<=H;h++){ if(h) cout<<","; cout<<root[h]; }
    cout << "\n";
    return 0;
}
