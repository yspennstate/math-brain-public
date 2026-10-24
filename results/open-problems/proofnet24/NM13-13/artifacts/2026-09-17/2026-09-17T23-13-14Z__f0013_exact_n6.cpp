#include <bits/stdc++.h>
#include <omp.h>
using namespace std;

static inline int bit_at(uint64_t A, int n, int i, int j){ return (A >> (i*n+j)) & 1ULL; }
static inline void set_bitv(uint64_t &A, int n, int i, int j, int b){ if(b) A |= (1ULL<<(i*n+j)); }

struct CanonMaps {
    int m, bits;
    vector<vector<uint32_t>> pack; // [k][B] = canon | (stab<<bits)
    vector<vector<array<int,5>>> perms; // only first m values used
    vector<vector<array<uint8_t,32>>> colmaps; // [k]? not used globally
};

static vector<array<int,5>> block_perms(int m,int k){
    vector<int> a(k), b(m-k);
    iota(a.begin(),a.end(),0); iota(b.begin(),b.end(),k);
    vector<array<int,5>> out;
    do {
        do {
            array<int,5> p{}; int z=0;
            for(int x:a) p[z++]=x;
            for(int x:b) p[z++]=x;
            out.push_back(p);
        } while(next_permutation(b.begin(),b.end()));
        sort(b.begin(),b.end());
    } while(next_permutation(a.begin(),a.end()));
    return out;
}

static inline uint32_t transform_B(uint32_t B,int m,const array<int,5>& p, const array<uint8_t,32>& cmap){
    uint32_t out=0;
    uint32_t mask=(1u<<m)-1;
    for(int i=0;i<m;i++){
        uint32_t row=(B>>(m*p[i])) & mask;
        out |= uint32_t(cmap[row]) << (m*i);
    }
    return out;
}

static CanonMaps build_maps(int m){
    CanonMaps cm; cm.m=m; cm.bits=m*m; cm.pack.resize(m+1); cm.perms.resize(m+1); cm.colmaps.resize(m+1);
    uint32_t states=1u<<cm.bits;
    #pragma omp parallel for schedule(dynamic,1)
    for(int k=0;k<=m;k++){
        auto ps=block_perms(m,k); cm.perms[k]=ps;
        vector<array<uint8_t,32>> cmapv(ps.size());
        for(size_t pi=0;pi<ps.size();++pi){
            for(int row=0;row<(1<<m);++row){
                int nr=0;
                for(int j=0;j<m;j++) nr |= ((row>>ps[pi][j])&1)<<j;
                cmapv[pi][row]=uint8_t(nr);
            }
        }
        vector<uint32_t> arr(states, 0xffffffffu);
        vector<uint32_t> vals; vals.reserve(ps.size());
        uint64_t norb=0;
        for(uint32_t B=0;B<states;B++) if(arr[B]==0xffffffffu){
            vals.clear();
            for(size_t pi=0;pi<ps.size();++pi) vals.push_back(transform_B(B,m,ps[pi],cmapv[pi]));
            sort(vals.begin(),vals.end()); vals.erase(unique(vals.begin(),vals.end()),vals.end());
            uint32_t canon=vals[0];
            uint32_t stab=uint32_t(ps.size()/vals.size());
            uint32_t packed = canon | (stab<<cm.bits);
            for(uint32_t x: vals) arr[x]=packed;
            norb++;
        }
        for(uint32_t x:arr) if(x==0xffffffffu){ cerr<<"unfilled map\n"; exit(2);}
        cm.pack[k]=move(arr);
        #pragma omp critical
        cerr << "built maps m="<<m<<" k="<<k<<" group="<<ps.size()<<" orbits="<<norb<<"\n";
    }
    return cm;
}

struct RootInfo { uint32_t key; int root_count; int root_stab; uint64_t orbit_weight; };

static RootInfo root_info(uint64_t A,int n,const CanonMaps& cm){
    int m=n-1; int Bbits=m*m;
    uint32_t best=0xffffffffu; int count=0; int beststab=-1;
    for(int r=0;r<n;r++){
        vector<int> one,zero; one.reserve(m); zero.reserve(m);
        for(int v=0;v<n;v++) if(v!=r){
            int c = bit_at(A,n,v,r) ^ bit_at(A,n,r,v);
            (c?one:zero).push_back(v);
        }
        int k=one.size(); vector<int> ord; ord.reserve(m); ord.insert(ord.end(),one.begin(),one.end()); ord.insert(ord.end(),zero.begin(),zero.end());
        uint32_t B=0;
        for(int i=0;i<m;i++) for(int j=0;j<m;j++){
            int vi=ord[i], vj=ord[j];
            int b = bit_at(A,n,vi,vj) ^ bit_at(A,n,r,vi) ^ bit_at(A,n,r,vj);
            if(b) B |= 1u<<(i*m+j);
        }
        uint32_t packed=cm.pack[k][B];
        uint32_t canon = packed & ((1u<<Bbits)-1);
        int stab = packed >> Bbits;
        int diag=bit_at(A,n,r,r);
        uint32_t key=(canon<<4) | (uint32_t(k)<<1) | uint32_t(diag);
        if(key<best){ best=key; count=1; beststab=stab; }
        else if(key==best){ count++; if(stab!=beststab){ cerr<<"stab mismatch\n"; exit(3);} }
    }
    uint64_t group=(1ULL<<(n-1));
    for(int i=2;i<=n;i++) group*=i;
    uint64_t aut=uint64_t(count)*uint64_t(beststab);
    if(group%aut){ cerr<<"bad aut group n="<<n<<" group="<<group<<" aut="<<aut<<"\n"; exit(4);}    
    return {best,count,beststab,group/aut};
}

static uint64_t reconstruct_from_key(uint32_t key,int n){
    int m=n-1; int Bbits=m*m;
    int diag=key&1u; int k=(key>>1)&7u; uint32_t B=key>>4;
    if(k>m || (Bbits<32 && B >= (1u<<Bbits))){ cerr<<"bad key decode\n"; exit(5);}    
    uint64_t A=0;
    set_bitv(A,n,0,0,diag);
    for(int j=1;j<n;j++){
        // row 0 outgoing fixed +1 => bit 0
        int c = ((j-1)<k)?1:0;
        set_bitv(A,n,j,0,c);
    }
    for(int i=0;i<m;i++) for(int j=0;j<m;j++) if((B>>(i*m+j))&1u) set_bitv(A,n,i+1,j+1,1);
    return A;
}

static vector<uint32_t> generate_classes_from_raw(int n,const CanonMaps& cm){
    uint64_t total=1ULL<<(n*n);
    vector<uint8_t> seen(1u<<24,0); // enough for n<=4 key; waste 16MB
    vector<uint32_t> keys;
    for(uint64_t A=0;A<total;A++){
        auto ri=root_info(A,n,cm); uint32_t k=ri.key;
        if(k>=seen.size()){ cerr<<"seen overflow key="<<k<<"\n"; exit(6);}        
        if(!seen[k]){seen[k]=1; keys.push_back(k);}    
    }
    sort(keys.begin(),keys.end());
    return keys;
}

static vector<uint32_t> extend_classes(const vector<uint32_t>& parentKeys,int parentN,const CanonMaps& childMaps){
    int n=parentN+1; int freebits=2*parentN;
    uint64_t per=1ULL<<freebits;
    int T=omp_get_max_threads();
    vector<vector<uint32_t>> locals(T);
    for(int t=0;t<T;t++) locals[t].reserve((parentKeys.size()*per)/T + 1024);
    #pragma omp parallel
    {
        int tid=omp_get_thread_num(); auto &loc=locals[tid];
        #pragma omp for schedule(dynamic,16)
        for(long long idx=0; idx<(long long)parentKeys.size(); ++idx){
            uint64_t P=reconstruct_from_key(parentKeys[idx],parentN);
            uint64_t base=0;
            for(int i=0;i<parentN;i++) for(int j=0;j<parentN;j++) if(bit_at(P,parentN,i,j)) set_bitv(base,n,i,j,1);
            int nv=parentN;
            for(uint64_t mask=0;mask<per;mask++){
                uint64_t A=base; int z=0;
                for(int i=1;i<parentN;i++) set_bitv(A,n,i,nv,(mask>>z++)&1ULL);
                for(int j=0;j<parentN;j++) set_bitv(A,n,nv,j,(mask>>z++)&1ULL);
                set_bitv(A,n,nv,nv,(mask>>z++)&1ULL);
                if(z!=freebits){ cerr<<"z mismatch\n"; exit(7);}
                loc.push_back(root_info(A,n,childMaps).key);
            }
        }
    }
    size_t total=0; for(auto &v:locals) total+=v.size();
    vector<uint32_t> all; all.reserve(total);
    for(auto &v:locals){ all.insert(all.end(),v.begin(),v.end()); vector<uint32_t>().swap(v); }
    sort(all.begin(),all.end()); all.erase(unique(all.begin(),all.end()),all.end());
    return all;
}

struct PolyKey { array<int,6> c; bool operator==(PolyKey const&o)const{return c==o.c;} };
struct PolyHash { size_t operator()(PolyKey const&p)const noexcept { uint64_t h=1469598103934665603ULL; for(int x:p.c){ uint64_t y=uint64_t(int64_t(x)+1000003); h^=y; h*=1099511628211ULL;} return size_t(h);} };

struct BData { int q[6]; int P[5][25]; }; // P[m][i,j]=B^m m=0..4; P0=I

static BData compute_Bdata(uint32_t Bbits){
    int B[25]; for(int i=0;i<25;i++) B[i]=((Bbits>>i)&1u)?-1:1;
    BData d{};
    for(int i=0;i<25;i++) d.P[0][i]=((i/5)==(i%5));
    for(int i=0;i<25;i++) d.P[1][i]=B[i];
    for(int pow=2;pow<=4;pow++){
        for(int i=0;i<5;i++) for(int j=0;j<5;j++){
            int s=0; for(int t=0;t<5;t++) s += d.P[pow-1][i*5+t] * B[t*5+j];
            d.P[pow][i*5+j]=s;
        }
    }
    int P5[25];
    for(int i=0;i<5;i++) for(int j=0;j<5;j++){
        int s=0; for(int t=0;t<5;t++) s += d.P[4][i*5+t]*B[t*5+j]; P5[i*5+j]=s;
    }
    long long tr[6]{};
    for(int p=1;p<=4;p++){ long long s=0; for(int i=0;i<5;i++) s+=d.P[p][i*5+i]; tr[p]=s; }
    { long long s=0; for(int i=0;i<5;i++) s+=P5[i*5+i]; tr[5]=s; }
    d.q[0]=1;
    for(int k=1;k<=5;k++){
        long long s=0; for(int i=1;i<=k;i++) s += (long long)d.q[k-i]*tr[i];
        if((-s)%k!=0){ cerr<<"Newton nondiv\n"; exit(8);} d.q[k]=int((-s)/k);
    }
    return d;
}

static PolyKey charpoly_from_Bdata(const BData& d,int k,int diagbit){
    int cvec[5]; for(int j=0;j<5;j++) cvec[j]=(j<k)?-1:1;
    long long s[5]{};
    for(int p=0;p<=4;p++){
        long long v=0; for(int i=0;i<5;i++) for(int j=0;j<5;j++) v += (long long)d.P[p][i*5+j]*cvec[j];
        s[p]=v;
    }
    long long r[5]{};
    for(int j=0;j<=4;j++){
        long long v=0; for(int h=0;h<=j;h++) v += (long long)d.q[h]*s[j-h]; r[j]=v;
    }
    int a=diagbit?-1:1;
    PolyKey pk{};
    pk.c[0]=d.q[1]-a;
    pk.c[1]=d.q[2]-a*d.q[1]-int(r[0]);
    pk.c[2]=d.q[3]-a*d.q[2]-int(r[1]);
    pk.c[3]=d.q[4]-a*d.q[3]-int(r[2]);
    pk.c[4]=d.q[5]-a*d.q[4]-int(r[3]);
    pk.c[5]=-a*d.q[5]-int(r[4]);
    return pk;
}

static array<int,6> direct_charpoly6(uint64_t A){
    int n=6; int M[36]; for(int i=0;i<36;i++) M[i]=((A>>i)&1ULL)?-1:1;
    long long P[36],N[36]; for(int i=0;i<36;i++) P[i]=M[i];
    long long tr[7]{}; for(int i=0;i<n;i++) tr[1]+=P[i*n+i];
    for(int pw=2;pw<=6;pw++){
        for(int i=0;i<n;i++) for(int j=0;j<n;j++){ long long s=0; for(int t=0;t<n;t++) s+=P[i*n+t]*M[t*n+j]; N[i*n+j]=s; }
        memcpy(P,N,sizeof(P)); for(int i=0;i<n;i++) tr[pw]+=P[i*n+i];
    }
    long long c[7]{}; c[0]=1;
    for(int k=1;k<=6;k++){ long long s=0; for(int i=1;i<=k;i++) s+=c[k-i]*tr[i]; c[k]=-s/k; }
    array<int,6> out{}; for(int i=1;i<=6;i++) out[i-1]=int(c[i]); return out;
}

int main(){
    ios::sync_with_stdio(false);
    cerr<<"BUILD_MAPS_3\n"; auto cm3=build_maps(3);
    cerr<<"RAW_N4\n"; auto k4=generate_classes_from_raw(4,cm3); cerr<<"n4_classes="<<k4.size()<<"\n";
    uint64_t sum4=0; for(auto key:k4){ auto A=reconstruct_from_key(key,4); auto ri=root_info(A,4,cm3); if(ri.key!=key){cerr<<"n4 key mismatch\n";return 9;} sum4+=ri.orbit_weight; }
    cerr<<"n4_orbit_sum="<<sum4<<" expected="<<(1ULL<<16)<<"\n";

    cerr<<"BUILD_MAPS_4\n"; auto cm4=build_maps(4);
    cerr<<"EXTEND_N5\n"; auto k5=extend_classes(k4,4,cm4); cerr<<"n5_classes="<<k5.size()<<"\n";
    uint64_t sum5=0; for(auto key:k5){ auto A=reconstruct_from_key(key,5); auto ri=root_info(A,5,cm4); if(ri.key!=key){cerr<<"n5 key mismatch\n";return 10;} sum5+=ri.orbit_weight; }
    cerr<<"n5_orbit_sum="<<sum5<<" expected="<<(1ULL<<25)<<"\n";

    cerr<<"BUILD_MAPS_5\n"; auto cm5=build_maps(5);
    cerr<<"EXTEND_N6\n"; auto k6=extend_classes(k5,5,cm5); cerr<<"n6_classes="<<k6.size()<<"\n";
    vector<uint64_t> classw(k6.size());
    unsigned long long sum6=0; int bad6=0;
    #pragma omp parallel for reduction(+:sum6,bad6) schedule(static)
    for(long long ii=0;ii<(long long)k6.size();++ii){
        auto A=reconstruct_from_key(k6[ii],6); auto ri=root_info(A,6,cm5);
        if(ri.key!=k6[ii]) bad6++; classw[ii]=ri.orbit_weight; sum6+=ri.orbit_weight;
    }
    if(bad6){ cerr<<"n6 key mismatches="<<bad6<<"\n"; return 11;}
    cerr<<"n6_orbit_sum="<<sum6<<" expected="<<(1ULL<<36)<<"\n";

    int T=omp_get_max_threads();
    vector<unordered_map<PolyKey,uint64_t,PolyHash>> wm(T);
    #pragma omp parallel
    {
        int tid=omp_get_thread_num(); auto &mp=wm[tid]; mp.reserve(k6.size()/(T*4));
        uint32_t lastB=0xffffffffu; BData bd{};
        #pragma omp for schedule(static)
        for(long long ii=0;ii<(long long)k6.size();++ii){
            uint32_t key=k6[ii]; uint32_t B=key>>4; int k=(key>>1)&7; int diag=key&1;
            if(B!=lastB){ bd=compute_Bdata(B); lastB=B; }
            PolyKey pk=charpoly_from_Bdata(bd,k,diag);
            mp[pk]+=classw[ii];
        }
    }
    unordered_map<PolyKey,uint64_t,PolyHash> weights; weights.reserve(200000);
    for(auto &mp:wm) for(auto &kv:mp) weights[kv.first]+=kv.second;
    unsigned long long direct_checks=k6.size(); int char_mismatches=0;
    #pragma omp parallel for reduction(+:char_mismatches) schedule(static)
    for(long long ii=0;ii<(long long)k6.size();++ii){
        uint32_t key=k6[ii], B=key>>4; int k=(key>>1)&7, diag=key&1; auto bd=compute_Bdata(B); auto pk=charpoly_from_Bdata(bd,k,diag);
        auto dc=direct_charpoly6(reconstruct_from_key(key,6)); if(dc!=pk.c) char_mismatches++;
    }
    if(char_mismatches){ cerr<<"direct charpoly mismatches="<<char_mismatches<<"\n"; return 12;}
    uint64_t wsum=0; for(auto &kv:weights) wsum+=kv.second;
    cerr<<"distinct_polynomials="<<weights.size()<<" weight_sum="<<wsum<<" direct_checks="<<direct_checks<<"\n";

    cout<<"META\tn4_classes\t"<<k4.size()<<"\tn4_sum\t"<<sum4<<"\tn5_classes\t"<<k5.size()<<"\tn5_sum\t"<<sum5<<"\tn6_classes\t"<<k6.size()<<"\tn6_sum\t"<<sum6<<"\tdistinct\t"<<weights.size()<<"\tdirect_checks\t"<<direct_checks<<"\n";
    vector<pair<PolyKey,uint64_t>> rows; rows.reserve(weights.size()); for(auto &kv:weights) rows.push_back(kv);
    sort(rows.begin(),rows.end(),[](auto const&a,auto const&b){return a.first.c<b.first.c;});
    for(auto &rw:rows){ cout<<"P"; for(int x:rw.first.c) cout<<"\t"<<x; cout<<"\t"<<rw.second<<"\n"; }
    return 0;
}
