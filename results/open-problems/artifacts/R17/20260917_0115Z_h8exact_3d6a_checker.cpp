// R17 exact checker: independent reconstruction and exact certification of
// Lueker's h=8 upper automaton for the binary Chvatal--Sankoff constant.
//
// Mathematical source interface reproduced from Lueker 2009, Figure 7 and
// the author's code overview. Floating point is used ONLY to search for a
// positive vector.  The final finite certificate uses an integer vector and
// exact rational arithmetic (boost::multiprecision::uint256_t/cpp_int).
//
// Compile: g++ -O3 -march=native -fopenmp -std=c++17 checker.cpp -o checker
// Run:     OMP_NUM_THREADS=8 ./checker /tmp/r17_h8_trans.bin /tmp/r17_h8_V.bin

#include <bits/stdc++.h>
#include <sys/mman.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
#include <boost/multiprecision/cpp_int.hpp>
#ifdef _OPENMP
#include <omp.h>
#endif
using namespace std;
using boost::multiprecision::cpp_int;
using boost::multiprecision::uint256_t;

static inline uint32_t pack4(uint8_t x,uint8_t y,uint8_t dx,uint8_t dy){
    return (uint32_t)x | ((uint32_t)y<<8) | ((uint32_t)dx<<16) | ((uint32_t)dy<<24);
}
static inline void unpack4(uint32_t s,uint8_t &x,uint8_t &y,uint8_t &dx,uint8_t &dy){
    x=s&255; y=(s>>8)&255; dx=(s>>16)&255; dy=(s>>24)&255;
}

struct TransComputer {
    int h; uint8_t mask;
    explicit TransComputer(int hh):h(hh),mask((1u<<hh)-1){}
    inline uint32_t reduce(uint32_t s) const {
        uint8_t x,y,dx,dy; unpack4(s,x,y,dx,dy);
        if(x & (1u<<(h-1))){ x^=mask; y^=mask; }
        return pack4(x,y,dx,dy);
    }
    uint32_t trans(uint32_t s,int c,int l) const {
        uint8_t x,y,dx,dy; unpack4(s,x,y,dx,dy);
        int ta = l>=0 ? l+1 : 1;
        int tb = l<0 ? -l+1 : 1;
        int na=h+ta, nb=h+tb;
        int16_t L[17][17];
        L[h][h]=h;
        int cur=h;
        for(int k=h-1;k>=0;--k){ cur -= (dx>>(h-1-k))&1; L[k][h]=cur; }
        cur=h;
        for(int k=h-1;k>=0;--k){ cur -= (dy>>(h-1-k))&1; L[h][k]=cur; }
        auto achar=[&](int i)->int {
            if(i<=h) return (x>>(h-i))&1;
            int q=i-h-1;
            if(l>=0) return q<l ? 1-c : c;
            return c;
        };
        auto bchar=[&](int j)->int {
            if(j<=h) return (y>>(h-j))&1;
            int q=j-h-1;
            if(l<0) return q<(-l) ? 1-c : c;
            return c;
        };
        for(int i=0;i<=na;i++) for(int j=0;j<=nb;j++) if(i>h || j>h){
            if(i==0) L[i][j]=L[i][j-1];
            else if(j==0) L[i][j]=L[i-1][j];
            else if(achar(i)==bchar(j)) L[i][j]=L[i-1][j-1]+1;
            else L[i][j]=max(L[i][j-1],L[i-1][j]);
        }
        int i=na,j=nb;
        while(i>=h && j>=h){
            if(L[i][j]==L[i-1][j]) --i;
            else if(L[i][j]==L[i][j-1]) --j;
            else { --i; --j; }
            if(i==h && j==h){
                uint8_t xs=x,ys=y;
                if(l>=0){
                    for(int q=0;q<l;q++) xs=((xs<<1)|(1-c))&mask;
                    xs=((xs<<1)|c)&mask; ys=((ys<<1)|c)&mask;
                } else {
                    xs=((xs<<1)|c)&mask;
                    for(int q=0;q<-l;q++) ys=((ys<<1)|(1-c))&mask;
                    ys=((ys<<1)|c)&mask;
                }
                uint8_t ndx=0,ndy=0;
                for(int k=na-h+1;k<=na;k++) ndx=(ndx<<1)|(L[k][nb]-L[k-1][nb]);
                for(int k=nb-h+1;k<=nb;k++) ndy=(ndy<<1)|(L[na][k]-L[na][k-1]);
                return reduce(pack4(xs,ys,ndx,ndy));
            }
        }
        return UINT32_MAX;
    }
};

struct EnumResult { size_t n; vector<uint32_t> h2rows; };

EnumResult enumerate_machine(int h, const string &out){
    TransComputer tc(h); uint8_t mask=(1u<<h)-1;
    uint32_t start=tc.reduce(pack4(0,0,mask,mask));
    unordered_map<uint32_t,uint32_t> idx;
    size_t reserveN = h==8 ? 7000000 : (h==7?900000:150000);
    idx.reserve(reserveN); idx.max_load_factor(0.75);
    vector<uint32_t> states; states.reserve(reserveN); states.push_back(start); idx[start]=1;
    FILE* fp=nullptr; if(!out.empty()){ fp=fopen(out.c_str(),"wb"); if(!fp){perror("fopen trans");exit(3);} }
    vector<uint32_t> h2rows;
    size_t head=0;
    while(head<states.size()){
        uint32_t s=states[head++];
        for(int c=0;c<2;c++) for(int l=-(h-1);l<=h-1;l++){
            uint32_t t=tc.trans(s,c,l), ti=0;
            if(t!=UINT32_MAX){
                auto it=idx.find(t);
                if(it==idx.end()){
                    ti=(uint32_t)states.size()+1; idx.emplace(t,ti); states.push_back(t);
                } else ti=it->second;
            }
            if(fp && fwrite(&ti,4,1,fp)!=1){perror("write trans");exit(4);}
            if(h==2) h2rows.push_back(ti);
        }
    }
    if(fp) fclose(fp);
    return {states.size(),h2rows};
}

uint256_t powu(uint64_t b,int e){ uint256_t r=1; for(int i=0;i<e;i++) r*=b; return r; }
cpp_int ipow(cpp_int b, uint64_t e){ cpp_int r=1; while(e){ if(e&1)r*=b; e>>=1; if(e)b*=b; } return r; }

int main(int argc,char**argv){
    if(argc<3){ cerr<<"usage: checker transition_tmp.bin integer_vector_tmp.bin\n"; return 2; }
    string transfile=argv[1], vfile=argv[2];
    cout<<"R17 h=8 independent exact reconstruction/certificate\n";
    cout<<"FLOATING POINT IS SEARCH-ONLY; FINAL COMPONENT AND ENDPOINT CHECKS ARE EXACT.\n";

    const uint32_t pub_h2[42]={
      2,1,3,4,5,6,
      2,1,0,4,4,7,
      7,6,6,0,1,3,
      4,4,7,2,1,0,
      4,5,6,2,1,3,
      7,6,6,0,1,3,
      7,7,7,0,1,0
    };
    const size_t pubN[9]={0,0,7,98,1020,10160,89960,780368,6419109};
    for(int h=2;h<=7;h++){
        auto er=enumerate_machine(h,"");
        if(er.n!=pubN[h]){ cerr<<"state-count FAIL h="<<h<<" got="<<er.n<<" expected="<<pubN[h]<<"\n"; return 10+h; }
        if(h==2){
            if(er.h2rows.size()!=42) return 20;
            for(size_t i=0;i<42;i++) if(er.h2rows[i]!=pub_h2[i]){ cerr<<"h2 table FAIL at "<<i<<"\n"; return 21; }
            cout<<"h=2 exact transition table: PASS\n";
        }
        cout<<"h="<<h<<" accepting states="<<er.n<<" (published count PASS)\n";
    }

    auto t0=chrono::steady_clock::now();
    auto er8=enumerate_machine(8,transfile);
    if(er8.n!=pubN[8]){ cerr<<"h8 count FAIL got="<<er8.n<<"\n"; return 30; }
    const size_t N=er8.n; const int deg=30;
    cout<<"h=8 accepting states="<<N<<" (published count PASS)\n";

    int fd=open(transfile.c_str(),O_RDONLY); if(fd<0){perror("open");return 31;}
    struct stat st; fstat(fd,&st); size_t expected=N*(size_t)deg*4;
    if((size_t)st.st_size!=expected){cerr<<"transition size FAIL\n";return 32;}
    auto *tr=(const uint32_t*)mmap(nullptr,st.st_size,PROT_READ,MAP_SHARED,fd,0);
    if(tr==MAP_FAILED){perror("mmap");return 33;}

    const double zsearch=0.3209; vector<double>w(deg); int jj=0;
    for(int c=0;c<2;c++) for(int l=-7;l<=7;l++){
        int a=abs(l); w[jj++]=(a<7)?pow(zsearch,a+2):pow(zsearch,9)/(1-zsearch);
    }
    vector<double> v(N,1.0), av(N);
    double lastMin=0,lastMax=0;
    for(int it=0;it<120;it++){
        double mn=DBL_MAX,mx=-DBL_MAX,vmax=0;
        #pragma omp parallel for reduction(min:mn) reduction(max:mx,vmax) schedule(static)
        for(long long ii=0;ii<(long long)N;ii++){
            const uint32_t*row=tr+(size_t)ii*deg; double s=0;
            for(int j=0;j<deg;j++){uint32_t q=row[j]; if(q) s+=w[j]*v[q-1];}
            av[ii]=s; double r=s/v[ii]; mn=min(mn,r);mx=max(mx,r);vmax=max(vmax,s);
        }
        #pragma omp parallel for schedule(static)
        for(long long ii=0;ii<(long long)N;ii++) av[ii]/=vmax;
        v.swap(av); lastMin=mn;lastMax=mx;
    }
    cout<<setprecision(17)<<"search-only iteration 120: minRatio="<<lastMin<<" maxRatio="<<lastMax<<"\n";

    const uint64_t SCALE=1000000000000ULL;
    vector<uint64_t> V(N); uint64_t vmin=UINT64_MAX,vmax=0;
    FILE* vf=fopen(vfile.c_str(),"wb"); if(!vf){perror("vfile");return 34;}
    for(size_t i=0;i<N;i++){
        uint64_t q=(uint64_t)floor((long double)v[i]*(long double)SCALE+0.5L); if(q==0)q=1;
        V[i]=q; vmin=min(vmin,q);vmax=max(vmax,q); fwrite(&q,sizeof(q),1,vf);
    }
    fclose(vf);
    cout<<"integer witness scale="<<SCALE<<" min="<<vmin<<" max="<<vmax<<"\n";

    uint256_t D=uint256_t(6791)*powu(10000,8), coeff[8];
    for(int a=0;a<=6;a++){int e=a+2; coeff[a]=uint256_t(6791)*powu(3209,e)*powu(10000,8-e);}
    coeff[7]=powu(3209,9);

    bool have=false; uint256_t maxsum=0; uint64_t maxv=1; size_t maxidx=0;
    for(size_t i=0;i<N;i++){
        uint256_t sum=0; const uint32_t*row=tr+i*deg; int j=0;
        for(int c=0;c<2;c++) for(int l=-7;l<=7;l++,j++){
            uint32_t q=row[j]; if(q) sum += coeff[abs(l)]*V[q-1];
        }
        if(!have || sum*maxv > maxsum*V[i]){have=true;maxsum=sum;maxv=V[i];maxidx=i;}
    }
    uint256_t maxden=D*maxv;
    if(!(maxsum<maxden)){cerr<<"lambda not <1\n";return 35;}
    cout<<"EXACT Collatz-Wielandt certificate: PASS for every one of "<<N<<" states\n";
    cout<<"exact worst state zero-based="<<maxidx<<"\n";
    cout<<"lambda_num="<<maxsum<<"\n";
    cout<<"lambda_den="<<maxden<<"\n";
    long double lr=maxsum.convert_to<long double>()/maxden.convert_to<long double>();
    cout<<setprecision(20)<<"lambda_exact_decimal_for_display="<<lr<<"\n";

    const uint64_t p=34945, q=42292;
    cpp_int lhs=ipow(cpp_int(3209),2*q)*ipow(cpp_int(maxden),p);
    cpp_int rhs=ipow(cpp_int(5000),2*q)*ipow(cpp_int(maxsum),p);
    if(!(lhs>rhs)){cerr<<"endpoint exact power comparison FAIL\n";return 36;}
    cout<<"EXACT endpoint power comparison: (3209/5000)^(2*42292) > lambda^(34945): PASS\n";
    cout<<"CERTIFIED_NEW_UPPER=34945/42292\n";
    cout<<"CERTIFIED_NEW_UPPER_DECIMAL=0.82627920174028184999527097323370850279012579211198...\n";
    cout<<"CERTIFIED_NEW_WIDTH=44424058323/1321625000000\n";
    cout<<"CERTIFIED_NEW_WIDTH_DECIMAL=0.033613209740281849995270973233708502790125792111983...\n";
    cout<<"OLD_UPPER=173228576586520/209648759000007\n";
    cout<<"UPPER_DECREASE=7077741859225/8866465315628296044\n";
    cout<<"UPPER_DECREASE_DECIMAL=0.00000079825969056119367386661207220791811684306156919891...\n";

    auto t1=chrono::steady_clock::now();
    cout<<"elapsed_seconds="<<chrono::duration<double>(t1-t0).count()<<"\n";
    cout<<"ALL_EXACT_CHECKS_PASS\n";
    munmap((void*)tr,st.st_size); close(fd);
    return 0;
}
