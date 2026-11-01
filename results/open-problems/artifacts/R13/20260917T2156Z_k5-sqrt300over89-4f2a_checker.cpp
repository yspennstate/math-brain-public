#include <bits/stdc++.h>
using namespace std;
using A5 = array<int,5>;
using A4 = array<int,4>;
struct St { uint16_t mask; A5 v; int norm2; vector<double> score10; };

static const int CP=89, CQ=300; // c = 89/300; T^2 = 300/89
static const int M[17]={0,5,16,29,48,61,80,101,128,133,144,157,176,189,208,229,256};
vector<A5> S(16), W10, W20;
vector<St> states;
unordered_map<int,vector<int>> by_key;
set<int> observed[13], needed[13];
vector<vector<uint16_t>> mask_cache(17);

__int128 gcd128(__int128 a,__int128 b){
    if(a<0)a=-a; if(b<0)b=-b;
    while(b){ __int128 r=a%b; a=b; b=r; }
    return a;
}
long long lcmll(long long a,long long b){ return a/std::gcd(a,b)*b; }

pair<long long,long long> cert_term(const A5& v,int k,const A5& w,int D){
    long long L=1,N=0;
    for(int x:w) L=lcmll(L,x);
    for(int j=0;j<5;j++) N += 1LL*v[j]*v[j]*(L/w[j]);
    if(!N) return {LLONG_MAX/4,1};
    long long a=1LL*k*k*L, b=1LL*D*N;
    long long g=std::gcd(a,b); return {a/g,b/g};
}

bool exact_certificate(const vector<int>& idx,const A4& k,const vector<A5>& W,int wi,int D){
    __int128 a=0,b=1;
    for(int r=0;r<4;r++){
        auto [p,q]=cert_term(states[idx[r]].v,k[r],W[wi],D);
        if(p>=LLONG_MAX/8) return true;
        a=a*q+(__int128)p*b; b*=q;
        __int128 g=gcd128(a,b); a/=g; b/=g;
    }
    return a*CQ >= (__int128)CP*b;
}

double float_term(const A5& v,int k,const A5& w,int D){
    double z=0;
    for(int j=0;j<5;j++) z += (double)D*v[j]*v[j]/w[j];
    return (double)k*k/z;
}

void add_state(int k,uint16_t mask,const A5& v,int norm2){
    St x{mask,v,norm2,{}};
    x.score10.resize(W10.size());
    for(int i=0;i<(int)W10.size();i++) x.score10[i]=float_term(v,k,W10[i],10);
    int id=(int)states.size(); states.push_back(move(x));
    by_key[k*65536+(int)mask].push_back(id);
}

void generate_oriented_states(int k){
    vector<int> c(k);
    function<void(int,int)> rec=[&](int p,int z){
        if(p==k){
            uint16_t mask=0; for(int x:c) mask|=(uint16_t)(1u<<x);
            for(int sb=0; sb<(1<<(k-1)); sb++){
                A5 v=S[c[0]];
                for(int t=1;t<k;t++){
                    int sg=((sb>>(t-1))&1)?1:-1;
                    for(int j=0;j<5;j++) v[j]+=sg*S[c[t]][j];
                }
                int n2=0; for(int x:v)n2+=x*x;
                observed[k].insert(n2);
                if(needed[k].count(n2)) add_state(k,mask,v,n2);
            }
            return;
        }
        for(int x=z;x<=16-(k-p);x++){ c[p]=x; rec(p+1,x+1); }
    };
    rec(0,0);
}

int main(){
    for(int m=0;m<16;m++){
        S[m][0]=1;
        for(int j=0;j<4;j++) S[m][j+1]=((m>>j)&1)?1:-1;
    }
    for(int k=1;k<=16;k++) for(unsigned m=1;m<65536;m++)
        if(__builtin_popcount(m)==k) mask_cache[k].push_back((uint16_t)m);

    for(int a=1;a<=6;a++) for(int b=1;b<=10-a-2;b++)
      for(int c=1;c<=10-a-b-1;c++) for(int d=1;d<=10-a-b-c;d++){
        int e=10-a-b-c-d; if(e>=1) W10.push_back({a,b,c,d,e});
      }
    for(int a=1;a<=16;a++) for(int b=1;b<=20-a-2;b++)
      for(int c=1;c<=20-a-b-1;c++) for(int d=1;d<=20-a-b-c;d++){
        int e=20-a-b-c-d; if(e>=1) W20.push_back({a,b,c,d,e});
      }
    assert(W10.size()==126 && W20.size()==3876);

    vector<set<int>> E(13);
    E[1]={5};
    E[2]={4,8,12,16};
    E[3]={5,13,21,29};
    E[4]={0,4,8,12,16,20,24,28,32,36,40,44,48};
    E[5]={5,13,21,29,37,45,53,61};
    E[6]={0,4,8,12,16,20,24,28,32,36,40,44,48,52,56,60,64,68,72,76,80};
    E[7]={5,13,21,29,37,45,53,61,69,77,85,93,101};
    E[8]={0,4,8,12,16,20,24,28,32,36,40,44,48,52,56,60,64,68,72,76,80,84,88,92,96,100,104,108,112,128};
    E[9]={5,13,21,29,37,45,53,61,69,77,85,93,101,109,117,125,133};
    E[10]={0,4,8,12,16,20,24,28,32,36,40,44,48,52,56,60,64,68,72,76,80,84,88,92,96,100,104,108,112,116,120,124,128,132,136,140,144};
    for(int n=5;n<=157;n+=8) E[11].insert(n);
    for(int n=0;n<=176;n+=4) E[12].insert(n);

    vector<A4> profiles;
    for(int a=1;a<=16;a++) for(int b=a;b<=16;b++) for(int c=b;c<=16;c++){
        int d=16-a-b-c; if(d<c||d<1) continue;
        int K[4]={a,b,c,d};
        __int128 x=0,y=1;
        for(int r=0;r<4;r++){
            x=x*M[K[r]]+(__int128)K[r]*K[r]*y;
            y*=M[K[r]];
            __int128 g=gcd128(x,y); x/=g; y/=g;
        }
        if(x*CQ < (__int128)5*CP*y) profiles.push_back({a,b,c,d});
    }
    assert(profiles.size()==33);
    int max_block=0; for(auto p:profiles) max_block=max(max_block,p[3]);
    assert(max_block==12);

    // Only generate oriented states that can survive profile-wise total-energy pruning.
    for(auto p:profiles) for(int r=0;r<4;r++){
        int k=p[r]; __int128 x=0,y=1;
        for(int i=0;i<4;i++) if(i!=r){
            x=x*M[p[i]]+(__int128)p[i]*p[i]*y;
            y*=M[p[i]];
            __int128 g=gcd128(x,y); x/=g; y/=g;
        }
        for(int n2:E[k]) if(n2>0)
            if((x*n2+(__int128)k*k*y)*CQ < (__int128)5*CP*y*n2)
                needed[k].insert(n2);
    }
    for(int k=1;k<=12;k++){
        generate_oriented_states(k);
        assert(observed[k]==E[k]);
        assert(*observed[k].rbegin()==M[k]);
    }

    // Independently recompute the exact many-row DP barrier over nondecreasing
    // block-size profiles k_1+...+k_q=16, q>=5.
    __int128 best_num=0,best_den=1; vector<int> best_profile; bool have_best=false;
    for(int q=5;q<=16;q++){
        vector<int> ks(q);
        function<void(int,int,int)> part=[&](int pos,int lo,int rem){
            if(pos==q){
                if(rem!=0) return;
                __int128 a=0,b=1;
                for(int k:ks){ a=a*M[k]+(__int128)k*k*b; b*=M[k]; __int128 g=gcd128(a,b); a/=g; b/=g; }
                if(!have_best || a*best_den<best_num*b){ have_best=true; best_num=a; best_den=b; best_profile=ks; }
                return;
            }
            int slots=q-pos;
            for(int k=lo;k<=rem/slots;k++){ ks[pos]=k; part(pos+1,k,rem-k); }
        };
        part(0,1,16);
    }
    assert(have_best && best_num==89 && best_den==60);
    assert((best_profile==vector<int>{1,1,2,4,8}));

    // q <= 3: partial rounding gives sqrt(3) < T.
    assert(3*CP < CQ);
    // q >= 5: strict witness inequalities give total energy > 89/60,
    // while 5c = 5*(89/300) = 89/60. Equality of caps is therefore excluded.
    assert((__int128)5*CP*60 <= (__int128)89*CQ);

    long long N=0, fail10=0, use20=0, full20=0, unique_patterns=0, unique_D20=0;
    unordered_map<string,unsigned char> cert_cache;
    for(auto K:profiles){
        vector<set<int>> allowed(4);
        for(int r=0;r<4;r++){
            __int128 x=0,y=1;
            for(int i=0;i<4;i++) if(i!=r){
                x=x*M[K[i]]+(__int128)K[i]*K[i]*y;
                y*=M[K[i]];
                __int128 g=gcd128(x,y); x/=g; y/=g;
            }
            for(int n2:E[K[r]]) if(n2>0)
                if((x*n2+(__int128)K[r]*K[r]*y)*CQ < (__int128)5*CP*y*n2)
                    allowed[r].insert(n2);
        }
        const auto &m0=mask_cache[K[0]], &m1=mask_cache[K[1]], &m2=mask_cache[K[2]];
        for(uint16_t a:m0){
            auto p0=by_key.find(K[0]*65536+(int)a); if(p0==by_key.end()) continue;
            for(uint16_t b:m1){
                if((a&b) || (K[1]==K[0] && b<=a)) continue;
                auto p1=by_key.find(K[1]*65536+(int)b); if(p1==by_key.end()) continue;
                for(uint16_t c:m2){
                    if(((a|b)&c) || (K[2]==K[1] && c<=b)) continue;
                    uint16_t d=(uint16_t)(0xFFFFu^(a|b|c));
                    if(__builtin_popcount((unsigned)d)!=K[3] || (K[3]==K[2] && d<=c)) continue;
                    auto p2=by_key.find(K[2]*65536+(int)c), p3=by_key.find(K[3]*65536+(int)d);
                    if(p2==by_key.end()||p3==by_key.end()) continue;
                    for(int i0:p0->second) if(allowed[0].count(states[i0].norm2))
                    for(int i1:p1->second) if(allowed[1].count(states[i1].norm2))
                    for(int i2:p2->second) if(allowed[2].count(states[i2].norm2))
                    for(int i3:p3->second) if(allowed[3].count(states[i3].norm2)){
                        N++; vector<int> idx={i0,i1,i2,i3};
                        string key; key.reserve(24);
                        for(int r=0;r<4;r++) key.push_back((char)K[r]);
                        int ids[4]={i0,i1,i2,i3};
                        for(int r=0;r<4;r++) for(int j=0;j<5;j++){ int z=states[ids[r]].v[j]; key.push_back((char)(z*z)); }
                        auto itc=cert_cache.find(key); unsigned char level=0;
                        if(itc!=cert_cache.end()) level=itc->second;
                        else {
                            unique_patterns++; double best=-1; int wi=-1;
                            for(int z=0;z<(int)W10.size();z++){
                                double q=states[i0].score10[z]+states[i1].score10[z]+states[i2].score10[z]+states[i3].score10[z];
                                if(q>best){best=q;wi=z;}
                            }
                            bool ok=exact_certificate(idx,K,W10,wi,10);
                            if(!ok){ for(int z=0;z<(int)W10.size()&&!ok;z++) ok=exact_certificate(idx,K,W10,z,10); }
                            if(ok) level=10;
                            else {
                                unique_D20++; best=-1; wi=-1;
                                for(int z=0;z<(int)W20.size();z++){
                                    double q=float_term(states[i0].v,K[0],W20[z],20)+float_term(states[i1].v,K[1],W20[z],20)
                                           +float_term(states[i2].v,K[2],W20[z],20)+float_term(states[i3].v,K[3],W20[z],20);
                                    if(q>best){best=q;wi=z;}
                                }
                                ok=exact_certificate(idx,K,W20,wi,20);
                                if(!ok){ full20++; for(int z=0;z<(int)W20.size()&&!ok;z++) ok=exact_certificate(idx,K,W20,z,20); }
                                if(!ok) return 2; level=20;
                            }
                            cert_cache.emplace(key,level);
                        }
                        if(level==20){ fail10++; use20++; }
                    }
                }
            }
        }
    }
    assert(N==15234630);
    assert(fail10==20920 && use20==20920 && full20==0);
    cout << "R13 K5 <= sqrt(300/89) exact checker\n"
         << "target_c=89/300\n"
         << "target_T_squared=300/89\n"
         << "four_row_profiles=" << profiles.size() << "\n"
         << "max_block_size=" << max_block << "\n"
         << "oriented_four_row_configurations=" << N << "\n"
         << "weights_D10=" << W10.size() << "\n"
         << "weights_D20=" << W20.size() << "\n"
         << "unique_squared_certificate_patterns=" << unique_patterns << "\n"
         << "unique_patterns_requiring_D20=" << unique_D20 << "\n"
         << "configs_requiring_D20=" << use20 << "\n"
         << "full_D20_fallbacks=" << full20 << "\n"
         << "q_le_3_condition=3c<1\n"
         << "q_ge_5_exact_lower=" << (long long)best_num << "/" << (long long)best_den << "\n"
         << "q_ge_5_minimizing_profile=1,1,2,4,8\n"
         << "q_ge_5_target_total_cap=89/60\n"
         << "R13_K5_SQRT300OVER89_EXACT_PASS\n";
    return 0;
}
