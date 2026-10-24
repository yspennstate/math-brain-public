#include <bits/stdc++.h>
using namespace std;
using i128=__int128_t;
static const long long SCALE=1000000000000000LL;
static const long long U32[33]={
0,0,31250000000000LL,0,93750000000000LL,0,169807324168044LL,0,250000000000000LL,0,327748418967313LL,0,397979296672175LL,0,456559443899824LL,0,500000000000000LL,0,525281835024787LL,0,529743675869249LL,0,511006048006930LL,0,466917186688700LL,0,395513184641840LL,0,294987775599294LL,0,163668874906902LL,0,0};
static const long long U64[65]={
0,0,9765625000000LL,0,31250000000000LL,0,60029956042011LL,0,93750000000000LL,0,130765229741829LL,0,169807324168044LL,0,209842985974956LL,0,250000000000000LL,0,289523583756197LL,0,327748418967313LL,0,364079637001733LL,0,397979296672175LL,0,428956421160460LL,0,456559443899824LL,0,480370343726726LL,0,500000000000000LL,0,515084450934868LL,0,525281835024787LL,0,530269858685285LL,0,529743675869249LL,0,523414094833139LL,0,511006048006930LL,0,492257275870782LL,0,466917186688700LL,0,434745862091401LL,0,395513184641840LL,0,348998068208656LL,0,294987775599294LL,0,233277310737719LL,0,163668874906902LL,0,85971378355885LL,0,0};

vector<uint64_t> gen_monotone(int n){
    vector<uint64_t> fs={0,1}; int N=1;
    for(int k=1;k<=n;k++){
        vector<uint64_t> nw;
        if(k==5) nw.reserve(7581); if(k==6) nw.reserve(7828354);
        uint64_t mask=(N==64?~0ULL:((1ULL<<N)-1));
        for(uint64_t a:fs) for(uint64_t b:fs)
            if((a & (~b & mask))==0) nw.push_back(a | (b<<N));
        fs.swap(nw); N*=2;
        cerr<<"M("<<k<<")="<<fs.size()<<"\n";
    }
    return fs;
}

struct Scan { size_t balanced=0, rigorous_bad=0, pzero=0; long double best=-1, second=-1; size_t ties=0; uint64_t besttt=0; long double bestH=0,bestI=0; };
Scan scan(const vector<uint64_t>& fs,int n){
    int N=1<<n; long long den2=1LL*N*N; const long long *U=(N==32?U32:U64); int pc[64]; for(int s=0;s<N;s++)pc[s]=__builtin_popcount((unsigned)s);
    Scan R;
    for(uint64_t tt:fs){
        if(__builtin_popcountll(tt)!=N/2) continue; R.balanced++;
        long long W[64]; for(int x=0;x<N;x++) W[x]=((tt>>x)&1ULL)?-1:1;
        for(int h=1;h<N;h<<=1) for(int i=0;i<N;i+=2*h) for(int j=0;j<h;j++){ long long u=W[i+j],v=W[i+j+h]; W[i+j]=u+v; W[i+j+h]=u-v; }
        long long Inum=0; long long Hup=0; long double H=0,I=0;
        for(int s=0;s<N;s++) if(W[s]){
            int w=abs((int)W[s]); long long w2=1LL*w*w; Inum += (long long)pc[s]*w2; Hup += U[w];
            long double p=(long double)w2/den2; H-=p*log2l(p); I+=(long double)pc[s]*p;
        }
        if(Inum==den2){R.pzero++; continue;}
        i128 lhs=(i128)Hup*den2*5; i128 rhs=(i128)32*SCALE*(Inum-den2);
        if(!(lhs<rhs)) R.rigorous_bad++;
        long double sc=H/(I-1);
        if(sc>R.best+1e-16L){R.second=R.best;R.best=sc;R.besttt=tt;R.bestH=H;R.bestI=I;R.ties=1;}
        else if(fabsl(sc-R.best)<=1e-16L)R.ties++;
        else if(sc>R.second)R.second=sc;
    }
    return R;
}
int main(){
    auto f5=gen_monotone(5); auto s5=scan(f5,5);
    auto f6=gen_monotone(6); auto s6=scan(f6,6);
    cout<<setprecision(20);
    auto out=[](int n,const vector<uint64_t>&fs,const Scan&s){
        cout<<"n="<<n<<" monotone="<<fs.size()<<" balanced="<<s.balanced<<" pzero="<<s.pzero<<" rigorous_ratio_ge_6.4="<<s.rigorous_bad<<"\n";
        cout<<"best="<<s.best<<" second="<<s.second<<" ties="<<s.ties<<" H="<<s.bestH<<" I="<<s.bestI<<" tt=0x"<<hex<<s.besttt<<dec<<"\n";
    };
    out(5,f5,s5); out(6,f6,s6);
    return (s5.rigorous_bad||s6.rigorous_bad)?2:0;
}
