/*
P16 exact finite self-check for claim P16-KKS-T23-PARENT-SIEVE-N4-54.
Scope: n=4, all distinct nonsynchronizing ternary transformation supports,
and every distinct fourth-letter extension. The program computes the
Kisielewicz-Szykula Theorem-2/Theorem-3 extension bound exactly and checks
it against exact reset thresholds. This validates the ported parent-safe
sieve architecture only; it does NOT advance the n=8 three/four-letter metric.
All computations are integer/exact; no floating point.
*/
#include <bits/stdc++.h>
using namespace std;

int main(){
    const int n=4, FULL=(1<<n)-1, M=256, TH=9;
    vector<array<unsigned char,16>> act(M);
    vector<array<unsigned char,4>> tr(M);
    for(int code=0;code<M;code++){
        int x=code;
        for(int i=0;i<n;i++){ tr[code][i]=x&3; x>>=2; }
        for(int s=0;s<(1<<n);s++){
            int y=0;
            for(int i=0;i<n;i++) if(s>>i&1) y |= 1<<tr[code][i];
            act[code][s]=y;
        }
    }
    auto sync_rt = [&](const int *gens,int k)->int{
        int dist[16]; fill(begin(dist),end(dist),-1);
        int q[16],h=0,t=0; q[t++]=FULL; dist[FULL]=0;
        while(h<t){
            int s=q[h++];
            if((s&(s-1))==0) return dist[s];
            for(int j=0;j<k;j++){
                int z=act[gens[j]][s];
                if(dist[z]<0){dist[z]=dist[s]+1;q[t++]=z;}
            }
        }
        return -1;
    };
    auto parent_stats = [&](const int *gens,int k){
        // BFS all reachable subsets from Q: minimal rank and shortest word of that rank.
        int dist[16]; fill(begin(dist),end(dist),-1);
        int q[16],h=0,t=0; q[t++]=FULL; dist[FULL]=0;
        while(h<t){int s=q[h++]; for(int j=0;j<k;j++){int z=act[gens[j]][s]; if(dist[z]<0){dist[z]=dist[s]+1;q[t++]=z;}}}
        int m=n, L=0;
        for(int s=1;s<=FULL;s++) if(dist[s]>=0){int r=__builtin_popcount((unsigned)s); if(r<m){m=r;L=dist[s];} else if(r==m) L=min(L,dist[s]);}
        // Compressible pair set P and exact shortest merge heights.
        vector<int> pair_masks; int H=0;
        for(int i=0;i<n;i++) for(int j=i+1;j<n;j++){
            int st=(1<<i)|(1<<j); int d[16]; fill(begin(d),end(d),-1); int qq[16],hh=0,tt=0; qq[tt++]=st; d[st]=0; int md=-1;
            while(hh<tt){int s=qq[hh++]; if((s&(s-1))==0){md=d[s];break;} for(int g=0;g<k;g++){int z=act[gens[g]][s];if(d[z]<0){d[z]=d[s]+1;qq[tt++]=z;}}}
            if(md>=0){pair_masks.push_back(st);H=max(H,md);}    
        }
        return tuple<int,int,vector<int>,int>{m,L,pair_masks,H};
    };
    auto p_exact = [&](const vector<int>& P,int r)->int{
        int s=P.size(); if(s==0) return 0;
        // DP over available pairs. Choosing (R,M) deletes all pairs contained in M from future availability.
        vector<int> memo(1<<s,-1);
        function<int(int)> dfs=[&](int mask)->int{
            if(mask==0) return 0; int &res=memo[mask]; if(res>=0) return res; res=0;
            for(int i=0;i<s;i++) if(mask>>i&1){
                int R=P[i];
                for(int U=1;U<=FULL;U++) if(__builtin_popcount((unsigned)U)==r && (R&U)==R){
                    int next=mask;
                    for(int j=0;j<s;j++) if((next>>j&1) && (P[j]&U)==P[j]) next &= ~(1<<j);
                    res=max(res,1+dfs(next));
                }
            }
            return res;
        };
        return dfs((1<<s)-1);
    };
    auto kks_bound = [&](const int *gens,int k){
        auto [m,L,P,H]=parent_stats(gens,k);
        int cur=L;
        for(int r=m;r>=2;r--){
            int b3=2*cur+n-r+1;
            int best=b3;
            if(!P.empty()){
                int p=p_exact(P,r);
                int N=n-r+2; int comb=N*(N-1)/2;
                int b2=cur+comb-p+H;
                best=min(best,b2);
            }
            cur=best;
        }
        return tuple<int,int,int,int,int>{cur,m,L,(int)P.size(),H};
    };

    auto key3=[](int a,int b,int c)->uint32_t{int v[3]={a,b,c};sort(v,v+3);return (uint32_t(v[0])<<16)|(uint32_t(v[1])<<8)|v[2];};
    auto key4=[](int a,int b,int c,int d)->uint32_t{int v[4]={a,b,c,d};sort(v,v+4);return uint32_t(v[0])|(uint32_t(v[1])<<8)|(uint32_t(v[2])<<16)|(uint32_t(v[3])<<24);};

    unordered_set<uint32_t> nons3; nons3.reserve(100000);
    long long nons_parents=0, sieve_safe=0, child_tests=0, sync_children_instances=0, violations=0;
    map<int,long long> bound_hist, rank_hist;
    struct Sig{int m,L,p,H,b; bool operator<(Sig const&o)const{return tie(m,L,p,H,b)<tie(o.m,o.L,o.p,o.H,o.b);} };
    map<Sig,long long> sig_hist;
    for(int a=0;a<M;a++) for(int b=a+1;b<M;b++) for(int c=b+1;c<M;c++){
        int g[3]={a,b,c}; if(sync_rt(g,3)>=0) continue;
        nons3.insert(key3(a,b,c)); nons_parents++;
        auto [B,m,L,p,H]=kks_bound(g,3);
        bound_hist[B]++; rank_hist[m]++; sig_hist[{m,L,p,H,B}]++;
        if(B<=TH) sieve_safe++;
    }

    unordered_set<uint32_t> irreducible_sync4; irreducible_sync4.reserve(2000);
    int max_rt=0, max_gap=INT_MIN;
    long long safe_parent_sync_instances=0, unsafe_parent_sync_instances=0;
    for(uint32_t kk: nons3){
        int a=(kk>>16)&255,b=(kk>>8)&255,c=kk&255; int g[3]={a,b,c};
        auto [B,m,L,p,H]=kks_bound(g,3);
        bool in[256]{}; in[a]=in[b]=in[c]=true;
        for(int d=0;d<M;d++) if(!in[d]){
            child_tests++;
            int q[4]={a,b,c,d}; int rt=sync_rt(q,4); if(rt<0) continue;
            sync_children_instances++; max_rt=max(max_rt,rt); max_gap=max(max_gap,rt-B);
            if(rt>B){violations++; if(violations<10) cerr<<"VIOLATION parent "<<a<<","<<b<<","<<c<<" d="<<d<<" rt="<<rt<<" B="<<B<<"\n";}
            if(B<=TH) safe_parent_sync_instances++; else unsafe_parent_sync_instances++;
            int s[4]={a,b,c,d}; sort(s,s+4); bool all_nons=true;
            for(int omit=0;omit<4;omit++){
                int w[3],z=0; for(int i=0;i<4;i++) if(i!=omit) w[z++]=s[i];
                if(!nons3.count(key3(w[0],w[1],w[2]))){all_nons=false;break;}
            }
            if(all_nons) irreducible_sync4.insert(key4(s[0],s[1],s[2],s[3]));
        }
    }

    cout<<"N 4\n";
    cout<<"THRESHOLD "<<TH<<"\n";
    cout<<"NONSYNC_DISTINCT_TERNARY_PARENTS "<<nons_parents<<"\n";
    cout<<"KKS_BOUND_LE_THRESHOLD_PARENTS "<<sieve_safe<<"\n";
    cout<<"KKS_BOUND_GT_THRESHOLD_PARENTS "<<(nons_parents-sieve_safe)<<"\n";
    cout<<"PARENT_RANK_HIST"; for(auto [x,c]:rank_hist) cout<<" "<<x<<":"<<c; cout<<"\n";
    cout<<"BOUND_HIST"; for(auto [x,c]:bound_hist) cout<<" "<<x<<":"<<c; cout<<"\n";
    cout<<"DISTINCT_FOURTH_LETTER_CHILD_TESTS "<<child_tests<<"\n";
    cout<<"SYNCHRONIZING_EXTENSION_INSTANCES "<<sync_children_instances<<"\n";
    cout<<"SYNC_INSTANCES_FROM_SAFE_PARENTS "<<safe_parent_sync_instances<<"\n";
    cout<<"SYNC_INSTANCES_FROM_UNSAFE_PARENTS "<<unsafe_parent_sync_instances<<"\n";
    cout<<"IRREDUCIBLY_SYNC_DISTINCT_4SUPPORTS "<<irreducible_sync4.size()<<"\n";
    cout<<"MAX_CHILD_RESET_THRESHOLD "<<max_rt<<"\n";
    cout<<"MAX_RT_MINUS_PARENT_BOUND "<<max_gap<<"\n";
    cout<<"BOUND_VIOLATIONS "<<violations<<"\n";
    bool pass=(nons_parents==83392 && irreducible_sync4.size()==492 && max_rt<=9 && violations==0);
    cout<<"KNOWN_N4_COUNTS_CHECK "<<((nons_parents==83392 && irreducible_sync4.size()==492)?"PASS":"FAIL")<<"\n";
    cout<<"KKS_PARENT_BOUND_SAFETY_CHECK "<<(violations==0?"PASS":"FAIL")<<"\n";
    cout<<"CLAIM P16-KKS-T23-PARENT-SIEVE-N4-54 "<<(pass?"PASS":"FAIL")<<"\n";
    cout<<(pass?"ALL_EXACT_CHECKS_PASSED":"CHECK_FAILED")<<"\n";
}
