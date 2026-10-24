#include <array>
#include <algorithm>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <numeric>
#include <tuple>
#include <vector>

static int sign_y_plus_x_sqrt2(long long X, long long Y){
    if(X==0) return (Y>0)-(Y<0);
    if(Y==0) return (X>0)-(X<0);
    if(X>0 && Y>0) return 1;
    if(X<0 && Y<0) return -1;
    __int128 xx=(__int128)X*X, yy=(__int128)Y*Y;
    if(X>0 && Y<0){ __int128 d=2*xx-yy; return (d>0)-(d<0); }
    __int128 d=yy-2*xx; return (d>0)-(d<0);
}

struct Br{int s,d,j;};
int main(int argc,char**argv){
    const char* outpath = argc>1 ? argv[1] : "s11_endpoint_phase1_residual.csv";
    std::ofstream fout(outpath);
    if(!fout){std::cerr<<"cannot open output\n"; return 10;}
    constexpr int m=11;
    std::array<int,m> p{}; std::iota(p.begin(),p.end(),0);
    long long total=0, inde=0, slab_pass=0, slab_res=0, heuristic_pass=0, residual=0;
    const int znum[5]={-9,-5,0,5,9};
    long double minval=1e100L; long long minX=0,minY=0; std::array<int,m> minp{};
    do{
        ++total;
        int mx=-1; bool dec=false;
        for(int i=0;i<m-1;++i){mx=std::max(mx,p[i]); if(mx==i){dec=true;break;}}
        if(dec) continue;
        ++inde;
        int hist[21]={0};
        for(int i=0;i<m;++i) ++hist[i-p[i]+10];
        int SD=0;
        for(int a=0;a<21;++a) if(hist[a]) for(int b=a+1;b<21;++b) if(hist[b]) SD += hist[a]*hist[b]*(b-a);
        if(SD>=242){++slab_pass; continue;}
        ++slab_res;
        std::array<Br,m> br{};
        for(int j=0;j<m;++j) br[j]={j+p[j],j-p[j],j};
        std::sort(br.begin(),br.end(),[](const Br&a,const Br&b){if(a.s!=b.s)return a.s<b.s; if(a.d!=b.d)return a.d<b.d; return a.j<b.j;});
        int CSL=0, CSH=0, sV=br[5].s; std::array<int,5> dl{},dh{};
        for(int q=0;q<5;++q){ CSL += br[q].s; dl[q]=br[q].d; CSH += br[q+6].s-2; dh[q]=br[q+6].d; }
        std::sort(dl.begin(),dl.end()); std::sort(dh.begin(),dh.end());
        int ZL=0,ZH=0;
        for(int q=0;q<5;++q){ZL += dl[q]*znum[q]; ZH += dh[q]*znum[q];}
        long long A=11LL*CSL+ZL, B=11LL*CSH+ZH, C=11LL*sV;
        long long X=A-B, Y=4*B+2*C-2640;
        int sg=sign_y_plus_x_sqrt2(X,Y);
        if(sg>0){
            ++heuristic_pass;
            long double val=(long double)Y+(long double)X*1.414213562373095048801688724209698L;
            if(val<minval){minval=val;minX=X;minY=Y;minp=p;}
            continue;
        }
        ++residual;
        for(int i=0;i<m;++i){if(i)fout<<','; fout<<p[i];} fout<<'\n';
    }while(std::next_permutation(p.begin(),p.end()));
    fout.close();
    std::cout<<"total="<<total<<"\n";
    std::cout<<"indecomposable="<<inde<<"\n";
    std::cout<<"equal_slab_pass="<<slab_pass<<"\n";
    std::cout<<"equal_slab_residual="<<slab_res<<"\n";
    std::cout<<"deterministic_domino_pass="<<heuristic_pass<<"\n";
    std::cout<<"phase2_residual="<<residual<<"\n";
    std::cout<<"smallest_phase1_positive_expression="<<minY<<" + ("<<minX<<")*sqrt(2) approx "<<(double)minval<<"\n";
    std::cout<<"smallest_phase1_perm="; for(int x:minp)std::cout<<x<<' '; std::cout<<"\n";
    if(total!=39916800LL) return 1;
    if(inde!=31998903LL) return 2;
    if(slab_res!=2970828LL) return 3;
    if(heuristic_pass!=2949943LL) return 4;
    if(residual!=20885LL) return 5;
    std::cout<<"EXACT S11 ENDPOINT PHASE1 PASSED\n";
    return 0;
}
