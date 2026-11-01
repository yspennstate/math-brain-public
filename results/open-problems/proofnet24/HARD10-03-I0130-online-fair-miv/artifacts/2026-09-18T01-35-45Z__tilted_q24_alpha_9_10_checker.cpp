#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <set>
#include <tuple>
#include <utility>
#include <vector>
using namespace std;

// Exact target-aware Bellman certificate for alpha = 9/10.
// After three common unit goods split 2--1, tilted safety
//   z_i = 2(B_i+R_i) - (9/10)V_i
// starts at (13/10, 33/10), hence lower level 13/10 and gap 2.
// Later action values lie on {0,1/24,...,1} for the current lower/higher z-agent.
// Scale all z/gaps by q*Q = 10*24 = 240.
static constexpr int p=1;      // delta = p/q = 1/10, alpha=1-delta=9/10
static constexpr int q=10;
static constexpr int Q=24;
static constexpr int H=100;
static constexpr int SCALE=q*Q; // 240
static constexpr int START_D=2*SCALE; // gap 2 -> 480
static constexpr int START_X=(q+3*p)*Q; // 13/10 -> 312
static constexpr int STEP=2*q*Q; // max gap increment = 480

struct Act { uint8_t i,j; };

int main(){
    static_assert(SCALE==240);
    static_assert(START_D==480);
    static_assert(START_X==312);

    vector<pair<int,int>> actions;
    actions.reserve((Q+1)*(Q+1));
    for(int i=0;i<=Q;i++) for(int j=0;j<=Q;j++) actions.push_back({i,j});

    const int maxD = START_D + STEP*H;
    vector<vector<int>> G(H+1);
    vector<vector<Act>> P(H+1);
    G[0].assign(maxD+1,0);
    P[0].assign(maxD+1,Act{0,0});
    vector<int> root(H+1,0);
    long long total_states = (long long)G[0].size();

    // Recurrence. If the high-z agent receives (i/Q,j/Q), the current lower z
    // misses value i/Q and decreases by (1-delta)i/Q, i.e. (q-p)i scaled units;
    // the gap increases by (q-p)i+(q+p)j.
    // If the low-z agent receives, the gap threshold is C=(q+p)i+(q-p)j.
    // Outside reflection lower z rises by (1+delta)i/Q (negative decrease);
    // inside reflection the old high agent becomes the lower one and decrease is
    // (1-delta)j/Q - D.
    for(int h=1; h<=H; ++h){
        int lim=maxD-STEP*h;
        G[h].assign(lim+1,0);
        P[h].assign(lim+1,Act{0,0});
        total_states += (long long)G[h].size();
        for(int D=0; D<=lim; ++D){
            int best=INT32_MIN, besti=0,bestj=0;
            for(auto [i,j]: actions){
                int incH=(q-p)*i+(q+p)*j;
                int valH=(q-p)*i + G[h-1][D+incH];

                int C=(q+p)*i+(q-p)*j;
                int DL,costL;
                if(D>=C){
                    DL=D-C;
                    costL=-(q+p)*i;
                } else {
                    DL=C-D;
                    costL=(q-p)*j-D;
                }
                int valL=costL+G[h-1][DL];
                int w=min(valH,valL);
                if(w>best){ best=w; besti=i; bestj=j; }
            }
            G[h][D]=best;
            P[h][D]=Act{(uint8_t)besti,(uint8_t)bestj};
        }
        root[h]=G[h][START_D];
        assert(root[h]>=root[h-1]); // zero good pads a shorter policy
    }

    // Exact target hit and first-hit horizon on this grid.
    assert(G[H][START_D]==START_X);
    assert(G[H-1][START_D] < START_X);
    assert(root[99]==311);
    assert(root[100]==312);

    // Root action: (15/24,24/24)=(5/8,1).
    assert(P[H][START_D].i==15 && P[H][START_D].j==24);

    // Independently traverse the reachable policy DAG and verify every Bellman equality.
    set<pair<int,int>> seen;
    vector<pair<int,int>> st{{H,START_D}};
    long long action_nodes=0, zero_nodes=0, leaf_nodes=0;
    set<pair<int,int>> used_actions;
    int max_seen_gap=0;
    while(!st.empty()){
        auto [h,D]=st.back(); st.pop_back();
        if(!seen.insert({h,D}).second) continue;
        max_seen_gap=max(max_seen_gap,D);
        if(h==0){ ++leaf_nodes; continue; }
        Act ac=P[h][D];
        int i=ac.i,j=ac.j;
        if(i==0 && j==0){
            assert(G[h][D]==G[h-1][D]);
            st.push_back({h-1,D});
            ++zero_nodes;
            continue;
        }
        ++action_nodes;
        used_actions.insert({i,j});
        int incH=(q-p)*i+(q+p)*j;
        int DH=D+incH;
        int valH=(q-p)*i+G[h-1][DH];
        int C=(q+p)*i+(q-p)*j;
        int DL,costL;
        if(D>=C){DL=D-C;costL=-(q+p)*i;}
        else{DL=C-D;costL=(q-p)*j-D;}
        int valL=costL+G[h-1][DL];
        assert(min(valH,valL)==G[h][D]);
        st.push_back({h-1,DH});
        st.push_back({h-1,DL});
    }

    // Source-model conversion.
    // If the first three unit goods split 2--1, lower tilted safety is 13/10.
    // The grid policy guarantees a decrease 312/240 = 13/10, hence z<=0.
    // z<=0 is exactly factor <= 9/10.
    assert(START_X*q == 13*SCALE); // 312*10 = 13*240
    // New width 9/10 - 19/30 = 4/15.
    long long wnum=9LL*30-19LL*10, wden=10LL*30;
    long long A=wnum,B=wden; while(B){ long long t=A%B; A=B; B=t; }
    assert(wnum/A==4 && wden/A==15);
    // Improvement over previous upper 879/920 is 51/920.
    assert(879LL*10 - 9LL*920 == 510);
    assert(510/10==51);

    cout << "I0130_TILTED_Q24_ALPHA_9_10_CERTIFICATE_PASS\n";
    cout << "delta=1/10\n";
    cout << "target_alpha=9/10\n";
    cout << "action_grid_denominator=24\n";
    cout << "scaled_unit=1/240\n";
    cout << "post_unit_start_lower_tilted_safety=13/10\n";
    cout << "post_unit_start_gap=2\n";
    cout << "first_winning_additional_horizon=100\n";
    cout << "root_value_h99=311/240\n";
    cout << "root_value_h100=312/240=13/10\n";
    cout << "root_action=15/24,24/24=5/8,1\n";
    cout << "source_valid_upper_bound=9/10\n";
    cout << "current_lower_bound=19/30\n";
    cout << "metric_width=4/15\n";
    cout << "improvement_over_879_920=51/920\n";
    cout << "total_dp_states="<<total_states<<"\n";
    cout << "reachable_policy_nodes="<<seen.size()<<"\n";
    cout << "reachable_action_nodes="<<action_nodes<<"\n";
    cout << "reachable_zero_nodes="<<zero_nodes<<"\n";
    cout << "reachable_leaf_nodes="<<leaf_nodes<<"\n";
    cout << "distinct_actions_used="<<used_actions.size()<<"\n";
    cout << "max_reachable_scaled_gap="<<max_seen_gap<<"\n";
    cout << "root_values_last_12=";
    for(int h=89;h<=100;h++){ if(h>89) cout<<","; cout<<h<<":"<<root[h]; }
    cout << "\n";
    return 0;
}
