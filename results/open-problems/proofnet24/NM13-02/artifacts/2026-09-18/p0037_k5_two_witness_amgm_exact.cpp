#include <bits/stdc++.h>
using namespace std;

static const int N=5;
static vector<pair<int,int>> EDGES;
static int edge_index[5][5];

int pc(int x){ return __builtin_popcount((unsigned)x); }

bool is_tree_mask(int mask){
    if(pc(mask)!=N-1) return false;
    int p[N]; iota(p,p+N,0);
    function<int(int)> find=[&](int a){ while(p[a]!=a){ p[a]=p[p[a]]; a=p[a]; } return a; };
    auto unite=[&](int a,int b){ a=find(a); b=find(b); if(a==b) return false; p[b]=a; return true; };
    for(int e=0;e<(int)EDGES.size();++e) if(mask>>e&1){
        if(!unite(EDGES[e].first,EDGES[e].second)) return false;
    }
    int r=find(0); for(int i=1;i<N;i++) if(find(i)!=r) return false;
    return true;
}

int permute_mask(int mask, const array<int,5>& perm){
    int out=0;
    for(int e=0;e<10;e++) if(mask>>e&1){
        auto [u,v]=EDGES[e]; int a=perm[u],b=perm[v]; if(a>b) swap(a,b);
        out |= 1<<edge_index[a][b];
    }
    return out;
}

struct Event {
    vector<int> wit;
    bitset<125> mem;
    uint64_t key=0;
};

uint64_t event_key(vector<int> w){
    sort(w.begin(),w.end());
    if(w.size()==1) return (uint64_t)w[0]+1;
    return (1ULL<<20) | ((uint64_t)w[0]<<10) | (uint64_t)w[1];
}

uint64_t permute_event_key(const Event& E, const array<int,5>& p){
    vector<int> w; for(int x:E.wit) w.push_back(permute_mask(x,p));
    return event_key(w);
}

int main(){
    memset(edge_index,-1,sizeof(edge_index));
    for(int i=0;i<N;i++) for(int j=i+1;j<N;j++){
        edge_index[i][j]=edge_index[j][i]=EDGES.size(); EDGES.push_back({i,j});
    }
    assert(EDGES.size()==10);

    vector<int> trees;
    for(int m=0;m<(1<<10);m++) if(is_tree_mask(m)) trees.push_back(m);
    assert(trees.size()==125);

    vector<array<int,5>> perms;
    array<int,5> a={0,1,2,3,4};
    do{ perms.push_back(a); }while(next_permutation(a.begin(),a.end()));
    assert(perms.size()==120);

    vector<int> w2;
    for(int m=0;m<(1<<10);m++) if(pc(m)==2) w2.push_back(m);
    assert(w2.size()==45);

    vector<Event> events;
    auto make_event=[&](vector<int> ws){
        Event E; sort(ws.begin(),ws.end()); E.wit=ws; E.key=event_key(ws);
        for(int ti=0;ti<125;ti++){
            int t=trees[ti]; bool hit=false;
            for(int w:ws) if((t&w)==w){ hit=true; break; }
            if(hit) E.mem.set(ti);
        }
        return E;
    };
    for(int w:w2) events.push_back(make_event({w}));
    for(int i=0;i<45;i++) for(int j=i+1;j<45;j++) events.push_back(make_event({w2[i],w2[j]}));
    assert(events.size()==1035);
    unordered_set<uint64_t> event_keys; unordered_set<string> event_memberships;
    for(auto &E:events){
        assert(event_keys.insert(E.key).second);
        string s; s.reserve(125); for(int i=0;i<125;i++) s.push_back(E.mem[i]?'1':'0');
        assert(event_memberships.insert(s).second);
    }

    unordered_map<uint64_t,int> key_to_event; for(int i=0;i<(int)events.size();i++) key_to_event[events[i].key]=i;

    vector<int> event_canon(events.size());
    map<uint64_t,int> canon_to_rep;
    for(int i=0;i<(int)events.size();i++){
        uint64_t best=ULLONG_MAX;
        for(auto &p:perms) best=min(best,permute_event_key(events[i],p));
        event_canon[i]=key_to_event.at(best);
        canon_to_rep.emplace(best,key_to_event.at(best));
    }
    assert(canon_to_rep.size()==19);
    vector<int> A_reps; for(auto &kv:canon_to_rep) A_reps.push_back(kv.second);

    vector<pair<int,int>> pair_reps;
    long long covered_ordered_pairs=0;
    for(int ai:A_reps){
        vector<array<int,5>> stab;
        for(auto &p:perms) if(permute_event_key(events[ai],p)==events[ai].key) stab.push_back(p);
        assert(120%(int)stab.size()==0);
        set<uint64_t> seenB;
        for(int bi=0;bi<(int)events.size();bi++){
            uint64_t best=ULLONG_MAX;
            for(auto &p:stab) best=min(best,permute_event_key(events[bi],p));
            if(!seenB.insert(best).second) continue;
            int brep=key_to_event.at(best);
            pair_reps.push_back({ai,brep});
            int pair_stab=0;
            for(auto &p:perms){
                if(permute_event_key(events[ai],p)==events[ai].key && permute_event_key(events[brep],p)==events[brep].key) pair_stab++;
            }
            assert(pair_stab>0 && 120%pair_stab==0);
            covered_ordered_pairs += 120/pair_stab;
        }
    }
    assert(pair_reps.size()==9413);
    assert(covered_ordered_pairs==1035LL*1035LL);

    struct Fibre { int inter, uni; int expcode; vector<pair<int,int>> pairs; };
    unordered_map<int,int> fibre_by_key;
    unordered_map<int,int> fibre_by_exp;
    vector<Fibre> fibres;
    auto exp_code=[&](int t1,int t2){
        int code=0,mul=1;
        for(int e=0;e<10;e++){
            int d=((t1>>e)&1)+((t2>>e)&1); code += d*mul; mul*=3;
        }
        return code;
    };
    for(int i=0;i<125;i++) for(int j=0;j<125;j++){
        int inter=trees[i]&trees[j], uni=trees[i]|trees[j];
        int key=inter | (uni<<10);
        int fid;
        auto it=fibre_by_key.find(key);
        if(it==fibre_by_key.end()){
            fid=fibres.size(); int ec=exp_code(trees[i],trees[j]);
            fibres.push_back({inter,uni,ec,{}}); fibre_by_key[key]=fid;
            auto ins=fibre_by_exp.emplace(ec,fid); assert(ins.second);
        } else fid=it->second;
        fibres[fid].pairs.push_back({i,j});
    }
    assert(fibres.size()==3425);

    vector<vector<pair<int,int>>> comp(fibres.size());
    auto digits=[&](int code){ array<int,10>d{}; for(int e=0;e<10;e++){d[e]=code%3;code/=3;} return d;};
    vector<array<int,10>> dig(fibres.size()); for(int i=0;i<(int)fibres.size();i++) dig[i]=digits(fibres[i].expcode);
    for(int m=0;m<(int)fibres.size();m++){
        for(int b=0;b<(int)fibres.size();b++){
            int gcode=0,mul=1; bool ok=true;
            for(int e=0;e<10;e++){
                int gd=2*dig[m][e]-dig[b][e]; if(gd<0||gd>2){ok=false;break;} gcode += gd*mul; mul*=3;
            }
            if(!ok) continue;
            auto it=fibre_by_exp.find(gcode); if(it==fibre_by_exp.end()) continue;
            int g=it->second; if(b<g) comp[m].push_back({b,g});
        }
        sort(comp[m].begin(),comp[m].end()); comp[m].erase(unique(comp[m].begin(),comp[m].end()),comp[m].end());
    }

    long long nonneg_orbits=0, amgm_orbits=0,total_neg_terms=0;
    int global_min_coeff=0,max_neg_terms=0;
    map<pair<int,int>,long long> mincoeff_nneg_hist;
    int max_dfs_nodes=0;

    vector<int> coeff(fibres.size());
    vector<int> cap(fibres.size());
    vector<int> use(fibres.size());

    for(auto [ai,bi]:pair_reps){
        fill(coeff.begin(),coeff.end(),0);
        const Event &A=events[ai], &B=events[bi];
        bitset<125> D;
        for(int ti=0;ti<125;ti++){
            int t=trees[ti]; bool hit=false;
            for(int fw:A.wit){
                for(int hw:B.wit){
                    if((fw & hw)==0 && (t & (fw|hw))==(fw|hw)){ hit=true; break; }
                }
                if(hit) break;
            }
            if(hit) D.set(ti);
        }
        for(int fid=0;fid<(int)fibres.size();fid++){
            int c=0;
            for(auto [i,j]:fibres[fid].pairs){
                if(A.mem[i] && B.mem[j]) c++;
                if(D[i]) c--;
            }
            coeff[fid]=c;
        }
        vector<int> neg;
        int minc=0;
        for(int i=0;i<(int)fibres.size();i++) if(coeff[i]<0){neg.push_back(i); minc=min(minc,coeff[i]);}
        global_min_coeff=min(global_min_coeff,minc);
        max_neg_terms=max(max_neg_terms,(int)neg.size());
        total_neg_terms += neg.size();
        mincoeff_nneg_hist[{minc,(int)neg.size()}]++;
        if(neg.empty()){ nonneg_orbits++; continue; }

        vector<vector<pair<int,int>>> opts(neg.size());
        for(int r=0;r<(int)neg.size();r++){
            int m=neg[r];
            for(auto [b,g]:comp[m]) if(coeff[b]>0 && coeff[g]>0) opts[r].push_back({b,g});
            assert(!opts[r].empty());
        }
        for(int i=0;i<(int)fibres.size();i++) cap[i]=max(0,2*coeff[i]);
        fill(use.begin(),use.end(),0);
        vector<char> done(neg.size(),0);
        int dfs_nodes=0;
        function<bool(int)> dfs=[&](int depth)->bool{
            dfs_nodes++;
            if(depth==(int)neg.size()) return true;
            int best=-1, best_count=INT_MAX;
            for(int r=0;r<(int)neg.size();r++) if(!done[r]){
                int d=-coeff[neg[r]], cnt=0;
                for(auto [b,g]:opts[r]) if(use[b]+d<=cap[b] && use[g]+d<=cap[g]) cnt++;
                if(cnt<best_count){best_count=cnt;best=r; if(cnt==0) break;}
            }
            if(best<0||best_count==0) return false;
            done[best]=1; int d=-coeff[neg[best]];
            for(auto [b,g]:opts[best]){
                if(use[b]+d>cap[b] || use[g]+d>cap[g]) continue;
                use[b]+=d; use[g]+=d;
                if(dfs(depth+1)){done[best]=0; return true;}
                use[b]-=d; use[g]-=d;
            }
            done[best]=0; return false;
        };
        bool ok=dfs(0); assert(ok);
        max_dfs_nodes=max(max_dfs_nodes,dfs_nodes);
        amgm_orbits++;
    }
    assert(nonneg_orbits+amgm_orbits==(long long)pair_reps.size());
    assert(nonneg_orbits==9118);
    assert(amgm_orbits==295);
    assert(global_min_coeff==-2);

    cout << "K5_SPANNING_TREES=" << trees.size() << "\n";
    cout << "PRODUCT_MULTIPLICITY_CELLS=" << fibres.size() << "\n";
    cout << "TWO_EDGE_WITNESSES=" << w2.size() << "\n";
    cout << "EVENTS_ONE_OR_TWO_TWOEDGE_WITNESSES=" << events.size() << "\n";
    cout << "S5_EVENT_ORBITS=" << canon_to_rep.size() << "\n";
    cout << "ORDERED_EVENT_PAIR_ORBITS=" << pair_reps.size() << "\n";
    cout << "ORDERED_EVENT_PAIRS_COVERED=" << covered_ordered_pairs << "\n";
    cout << "PAIR_ORBITS_COEFFICIENTWISE_NONNEGATIVE=" << nonneg_orbits << "\n";
    cout << "PAIR_ORBITS_REQUIRING_AMGM=" << amgm_orbits << "\n";
    cout << "GLOBAL_MIN_COEFFICIENT=" << global_min_coeff << "\n";
    cout << "TOTAL_NEGATIVE_MONOMIAL_OCCURRENCES=" << total_neg_terms << "\n";
    cout << "MAX_NEGATIVE_TERMS_IN_ONE_PAIR_ORBIT=" << max_neg_terms << "\n";
    cout << "AMGM_CAPACITY_CERTIFIED_ORBITS=" << amgm_orbits << "\n";
    cout << "TROPICAL_EXPOSED_NEGATIVE_TERMS=0\n";
    cout << "MAX_DFS_NODES_FOR_CAPACITY_ASSIGNMENT=" << max_dfs_nodes << "\n";
    cout << "MINCOEFF_NEGCOUNT_HISTOGRAM_BEGIN\n";
    for(auto &kv:mincoeff_nneg_hist) if(kv.first.second>0)
        cout << "min=" << kv.first.first << ",neg=" << kv.first.second << ",orbits=" << kv.second << "\n";
    cout << "MINCOEFF_NEGCOUNT_HISTOGRAM_END\n";
    cout << "ALL_EXACT_CHECKS_PASS\n";
}
