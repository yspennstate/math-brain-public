#include <bits/stdc++.h>
using namespace std;

struct PermInfo {
    vector<int> parts;
    vector<int> p;
    int ord;
};

static int gcd_int(int a,int b){return b?gcd_int(b,a%b):a;}
static int lcm_int(int a,int b){return a/gcd_int(a,b)*b;}

static void gen_parts_rec(int rem, int mx, vector<int>& cur, vector<vector<int>>& out){
    if(rem==0){out.push_back(cur); return;}
    for(int x=min(rem,mx); x>=1; --x){
        cur.push_back(x); gen_parts_rec(rem-x,x,cur,out); cur.pop_back();
    }
}

static vector<int> canonical_perm_from_parts(const vector<int>& parts){
    int n=0; for(int x:parts)n+=x;
    vector<int> p(n); int base=0;
    for(int len:parts){
        for(int i=0;i<len;i++) p[base+i]=base+(i+1)%len;
        base+=len;
    }
    return p;
}

static vector<int> perm_power(const vector<int>& p, int e){
    int n=p.size(); vector<int> r(n);
    for(int i=0;i<n;i++){
        int x=i; for(int k=0;k<e;k++) x=p[x];
        r[i]=x;
    }
    return r;
}

static inline uint16_t image_mask(uint16_t mask, const vector<uint8_t>& t){
    uint16_t out=0;
    while(mask){
        int b=__builtin_ctz(mask); mask &= mask-1;
        out |= uint16_t(1u<<t[b]);
    }
    return out;
}

static int reset_threshold_exact(const vector<vector<uint8_t>>& letters, int n){
    int M=1<<n, full=M-1;
    static int dist[1<<12];
    for(int i=0;i<M;i++) dist[i]=-1;
    static uint16_t q[1<<12]; int head=0,tail=0;
    dist[full]=0; q[tail++]=full;
    while(head<tail){
        uint16_t s=q[head++]; int d=dist[s];
        if((s & (s-1))==0) return d;
        for(auto &t: letters){
            uint16_t u=image_mask(s,t);
            if(dist[u]<0){dist[u]=d+1; q[tail++]=u;}
        }
    }
    return -1;
}

static string parts_str(const vector<int>& parts){
    string s; for(size_t i=0;i<parts.size();i++){ if(i)s+='+'; s+=to_string(parts[i]); } return s;
}
static string trans_str(const vector<uint8_t>& t){
    string s="["; for(size_t i=0;i<t.size();i++){ if(i)s+=","; s+=to_string(int(t[i])); } return s+"]";
}

int main(int argc,char**argv){
    int n=(argc>1?atoi(argv[1]):8); if(n<2||n>11){cerr<<"n out of supported range\n";return 1;} const int E=n*(n-1), square=(n-1)*(n-1);
    vector<vector<int>> parts; vector<int> cur; gen_parts_rec(n,n,cur,parts);
    vector<PermInfo> infos;
    long long exponent_pairs_total=0;
    for(auto pa:parts){
        vector<int> p=canonical_perm_from_parts(pa);
        int ord=1; for(int x:pa) ord=lcm_int(ord,x);
        infos.push_back({pa,p,ord});
        exponent_pairs_total += 1LL*ord*(ord-1)/2;
    }

    vector<vector<uint8_t>> idems;
    vector<pair<int,int>> idem_meta;
    for(int s=0;s<n;s++) for(int t=0;t<n;t++) if(s!=t){
        vector<uint8_t> f(n); for(int i=0;i<n;i++) f[i]=i; f[s]=t;
        idems.push_back(f); idem_meta.push_back({s,t});
    }

    cout << "HARD8_01_TWO_CYCLIC_PERM_EXACT\n";
    cout << "ARITHMETIC integer_only\n";
    cout << "N "<<n<<" PARTITIONS "<<parts.size()<<" IDEMPOTENTS "<<E<<"\n";
    cout << "EXPONENT_PAIR_COVERS "<<exponent_pairs_total<<"\n";

    for(int qletters: {3,4}){
        long long tested=0,sync=0,viol=0;
        int maxrt=-1;
        string maxdesc;
        map<int,long long> rtdist;
        long long ktested[3]={0,0,0}, ksync[3]={0,0,0}, kviol[3]={0,0,0}; int kmax[3]={-1,-1,-1};
        long long expected_per_pair=1 + E;
        if(qletters==4) expected_per_pair += 1LL*E*(E-1)/2;
        long long expected=exponent_pairs_total*expected_per_pair;
        long long by_cycle_sum=0;
        cout << "BEGIN_Q "<<qletters<<" EXPECTED "<<expected<<"\n";
        for(auto &info:infos){
            vector<vector<uint8_t>> powers(info.ord, vector<uint8_t>(n));
            for(int e=0;e<info.ord;e++){
                auto pp=perm_power(info.p,e);
                for(int i=0;i<n;i++) powers[e][i]=pp[i];
            }
            long long cyc_tested=0,cyc_sync=0; int cyc_max=-1;
            for(int a=0;a<info.ord;a++) for(int b=a+1;b<info.ord;b++){
                // k=0 simple idempotents
                {
                    vector<vector<uint8_t>> letters={powers[a],powers[b]};
                    int rt=reset_threshold_exact(letters,n); tested++;cyc_tested++; ktested[0]++;
                    if(rt>=0){sync++;cyc_sync++;ksync[0]++;rtdist[rt]++; kmax[0]=max(kmax[0],rt); if(rt>maxrt){maxrt=rt;maxdesc=parts_str(info.parts)+" powers="+to_string(a)+","+to_string(b)+" idems=none";} cyc_max=max(cyc_max,rt); if(rt>square){viol++;kviol[0]++;}}
                }
                // k=1
                for(int i=0;i<E;i++){
                    vector<vector<uint8_t>> letters={powers[a],powers[b],idems[i]};
                    int rt=reset_threshold_exact(letters,n); tested++;cyc_tested++; ktested[1]++;
                    if(rt>=0){sync++;cyc_sync++;ksync[1]++;rtdist[rt]++; kmax[1]=max(kmax[1],rt); if(rt>maxrt){maxrt=rt;maxdesc=parts_str(info.parts)+" powers="+to_string(a)+","+to_string(b)+" idems="+to_string(idem_meta[i].first)+"->"+to_string(idem_meta[i].second);} cyc_max=max(cyc_max,rt); if(rt>square){viol++;kviol[1]++;}}
                }
                if(qletters==4){
                    for(int i=0;i<E;i++) for(int j=i+1;j<E;j++){
                        vector<vector<uint8_t>> letters={powers[a],powers[b],idems[i],idems[j]};
                        int rt=reset_threshold_exact(letters,n); tested++;cyc_tested++; ktested[2]++;
                        if(rt>=0){sync++;cyc_sync++;ksync[2]++;rtdist[rt]++; kmax[2]=max(kmax[2],rt); if(rt>maxrt){maxrt=rt;maxdesc=parts_str(info.parts)+" powers="+to_string(a)+","+to_string(b)+" idems="+to_string(idem_meta[i].first)+"->"+to_string(idem_meta[i].second)+","+to_string(idem_meta[j].first)+"->"+to_string(idem_meta[j].second);} cyc_max=max(cyc_max,rt); if(rt>square){viol++;kviol[2]++;}}
                    }
                }
            }
            by_cycle_sum += cyc_tested;
            cout << "CYCLE "<<parts_str(info.parts)<<" ORDER "<<info.ord<<" TESTED "<<cyc_tested<<" SYNC "<<cyc_sync<<" MAX_RT "<<cyc_max<<"\n";
        }
        if(tested!=expected || by_cycle_sum!=expected){ cerr<<"coverage mismatch\n"; return 2; }
        cout << "Q_RESULT q="<<qletters<<" TESTED "<<tested<<" SYNCHRONIZING "<<sync<<" VIOLATIONS "<<viol<<" MAX_RT "<<maxrt<<"\n";
        cout << "Q_EXTREMAL "<<maxdesc<<"\n";
        for(int k=0;k<=qletters-2;k++) cout << "K_RESULT k="<<k<<" TESTED "<<ktested[k]<<" SYNCHRONIZING "<<ksync[k]<<" VIOLATIONS "<<kviol[k]<<" MAX_RT "<<kmax[k]<<"\n";
        cout << "Q_RT_DISTRIBUTION"; for(auto [r,c]:rtdist) cout << " "<<r<<":"<<c; cout << "\n";
        if(viol!=0 || maxrt>square){ cerr<<"square violation\n"; return 3; }
    }
    cout << "ALL_EXACT_TWO_CYCLIC_PERM_CHECKS_PASSED n="<<n<<"\n";
}
