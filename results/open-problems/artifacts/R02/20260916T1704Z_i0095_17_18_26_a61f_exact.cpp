#include <bits/stdc++.h>
using namespace std;

static int exact_disc(const vector<uint32_t>& rows, int n){
    const uint32_t total = 1u << (n-1); // fix x_0=+1 modulo global negation
    vector<int> y(n,0);
    for(int i=0;i<n;i++) y[i] = 2*__builtin_popcount(rows[i]) - n; // all x_j=+1
    auto norm_inf=[&](){int z=0; for(int v:y) z=max(z,abs(v)); return z;};
    int best=norm_inf(); uint32_t prev=0;
    for(uint32_t t=1;t<total;t++){
        uint32_t g=t^(t>>1), diff=g^prev;
        int col=__builtin_ctz(diff)+1;
        bool to_minus=(g>>(col-1))&1u;
        for(int i=0;i<n;i++){
            int a=((rows[i]>>col)&1u)?1:-1;
            y[i]+= to_minus ? -2*a : 2*a;
        }
        best=min(best,norm_inf());
        prev=g;
    }
    return best;
}

static uint32_t rotbits(uint32_t x,int s,int n){
    uint32_t mask=(1u<<n)-1;
    if(s==0) return x&mask;
    return ((x<<s)|(x>>(n-s)))&mask;
}
static uint32_t canon(uint32_t x,int n){
    uint32_t mask=(1u<<n)-1,best=mask;
    for(int s=0;s<n;s++){
        uint32_t y=rotbits(x,s,n);
        best=min(best,y); best=min(best,(~y)&mask);
    }
    return best;
}
static tuple<int,uint32_t,uint32_t,size_t> max_circulant_disc(int n){
    const uint32_t N=1u<<n;
    vector<uint32_t> reps; reps.reserve(N/(2*n)+100);
    for(uint32_t x=0;x<N;x++) if(canon(x,n)==x) reps.push_back(x);
    int globalbest=-1; uint32_t bestr=0,bestx=0;
    for(uint32_t r:reps){
        int mind=999; uint32_t minx=0;
        for(uint32_t x:reps){
            int mx=0;
            for(int s=0;s<n;s++){
                uint32_t y=rotbits(r,s,n);
                int d=__builtin_popcount(y^x);
                mx=max(mx,abs(n-2*d));
            }
            if(mx<mind){
                mind=mx; minx=x;
                if(mind<=globalbest) break; // this r cannot improve the certified max
            }
        }
        if(mind>globalbest){globalbest=mind;bestr=r;bestx=minx;}
    }
    return {globalbest,bestr,bestx,reps.size()};
}

// GF(4)=F2[a]/(a^2+a+1), encoded 0,1,a,a+1 as 0,1,2,3.
static int g4add(int x,int y){return x^y;}
static int g4mul(int x,int y){
    int a0=x&1,a1=(x>>1)&1,b0=y&1,b1=(y>>1)&1;
    int c0=a0*b0, c1=(a0*b1)^(a1*b0), c2=a1*b1;
    c0^=c2; c1^=c2; return c0|(c1<<1);
}
static int g4inv(int x){for(int y=1;y<4;y++)if(g4mul(x,y)==1)return y;abort();}
static array<int,3> normp(array<int,3> v){
    for(int j=0;j<3;j++) if(v[j]){int z=g4inv(v[j]);for(int k=0;k<3;k++)v[k]=g4mul(z,v[k]);return v;}
    abort();
}
static int g4dot(array<int,3>a,array<int,3>b){int z=0;for(int k=0;k<3;k++)z=g4add(z,g4mul(a[k],b[k]));return z;}
static vector<uint32_t> pg24_matrix(){
    set<array<int,3>> S;
    for(int a=0;a<4;a++)for(int b=0;b<4;b++)for(int c=0;c<4;c++) if(a||b||c) S.insert(normp({a,b,c}));
    vector<array<int,3>> P(S.begin(),S.end());
    assert(P.size()==21);
    vector<uint32_t> rows;
    for(auto L:P){uint32_t r=0;for(int j=0;j<21;j++)if(g4dot(L,P[j])==0)r|=(1u<<j);rows.push_back(r);}
    for(auto r:rows) assert(__builtin_popcount(r)==5);
    return rows;
}

int main(){
    // Recovered n=9 witness from the repository baseline.
    vector<string> W={"---++++++","-+---++++","+---++-++","+++++--++","+-+----++","++--+++-+","+--+-++-+","-+-+-+--+","--+-+---+"};
    vector<uint32_t> R9;
    for(auto&s:W){uint32_t r=0;for(int j=0;j<9;j++)if(s[j]=='+')r|=1u<<j;R9.push_back(r);}
    int d9=exact_disc(R9,9); assert(d9==5);
    cout<<"BASELINE n=9 disc="<<d9<<" ratio=5/3\n";

    auto P=pg24_matrix(); int dpg=exact_disc(P,21); assert(dpg==5);
    cout<<"METHOD17 PG(2,4) incidence-sign matrix n=21 disc="<<dpg<<"\n";

    cout<<"METHOD18 exact max discrepancy among circulant sign matrices\n";
    int best_ratio_n=0,bestd=0;
    for(int n=9;n<=24;n++){
        auto [d,r,x,nrep]=max_circulant_disc(n);
        cout<<"n="<<n<<" max_circulant_disc="<<d<<" seed="<<r<<" minimizing_x_rep="<<x<<" reps="<<nrep<<"\n";
        // Exact integer comparison d/sqrt(n) <= 5/3 <=> 9d^2 <=25n.
        assert(9*d*d <= 25*n);
        if(best_ratio_n==0 || 1LL*d*d*best_ratio_n > 1LL*bestd*bestd*n){best_ratio_n=n;bestd=d;}
    }
    cout<<"CIRCULANT_BEST n="<<best_ratio_n<<" d="<<bestd<<"; exact check 9*d^2<=25*n: PASS\n";
    cout<<"ALL EXACT CHECKS PASS\n";
}
