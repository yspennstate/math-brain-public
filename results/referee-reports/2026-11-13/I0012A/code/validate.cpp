#define SIMULATOR_NO_MAIN
#include "simulate.cpp"
#include <map>
#include <iomanip>

using State=std::pair<int,int>;
int tooth(int x) { return ((x%4)+4)%4; }
std::vector<State> adjacent(State a) {
    std::vector<State> v;
    int x=a.first,h=a.second,H=tooth(x);
    if(h==0) { v.push_back({x-1,0}); v.push_back({x+1,0}); }
    if(h>0) v.push_back({x,h-1});
    if(h<H) v.push_back({x,h+1});
    return v;
}
int main() {
    constexpr int T=12,M=50000;
    std::map<State,double> dist={{{0,0},1.0}};
    double exactTotal=0,exactBase=0;
    for(int t=1;t<=T;++t) {
        std::map<State,double> nxt;
        for(auto [s,p]:dist) {
            auto v=adjacent(s);
            for(auto q:v) nxt[q]+=p/v.size();
        }
        dist.swap(nxt);
        for(auto [s,p]:dist) {
            exactTotal+=p*p;
            if(s.second==0) exactBase+=p*p;
        }
    }
    Comb c(1.0/3,100,1);
    for(int x=-T;x<=T;++x) c.heights[x]=tooth(x);
    double sum=0,sum2=0,sumb=0,sumb2=0;
    for(int i=0;i<M;++i) {
        std::mt19937_64 r(34567ULL+i*8191ULL),r2(76543ULL+i*65537ULL);
        Pos a,b; int z=0,zb=0;
        for(int t=1;t<=T;++t) {
            step(a,c,r);step(b,c,r2);
            if(a.h<0 || a.h>tooth(a.x) || b.h<0 || b.h>tooth(b.x)) return 2;
            if(((a.x+a.h-t)%2)!=0 || ((b.x+b.h-t)%2)!=0) return 3;
            if(a.x==b.x && a.h==b.h) {++z;if(a.h==0)++zb;}
        }
        sum+=z;sum2+=z*z;sumb+=zb;sumb2+=zb*zb;
    }
    double mean=sum/M,mb=sumb/M;
    double se=std::sqrt((sum2/M-mean*mean)/(M-1));
    double seb=std::sqrt((sumb2/M-mb*mb)/(M-1));
    std::cout<<std::setprecision(12)<<"exact propagation vs shared step simulator, T="<<T<<", pairs="<<M<<"\n"
             <<"total exact="<<exactTotal<<" sample="<<mean<<" se="<<se<<" z="<<(mean-exactTotal)/se<<"\n"
             <<"base exact="<<exactBase<<" sample="<<mb<<" se="<<seb<<" z="<<(mb-exactBase)/seb<<"\n";
    if(std::abs(mean-exactTotal)>5*se || std::abs(mb-exactBase)>5*seb) return 4;
    // Independent finite-matrix audit of the squared-degree identity used in the proof.
    const int N=7;
    std::vector<State> vertices;
    for(int x=0;x<N;++x) for(int h=0;h<=tooth(x);++h) vertices.push_back({x,h});
    const int V=vertices.size();
    std::map<State,int> index;
    for(int i=0;i<V;++i)index[vertices[i]]=i;
    std::vector<std::vector<double>> P(V,std::vector<double>(V)),K(V,std::vector<double>(V));
    std::vector<int> deg(V);
    for(int i=0;i<V;++i) {
        auto [x,h]=vertices[i]; std::vector<State> v;
        if(h==0) {v.push_back({(x+N-1)%N,0});v.push_back({(x+1)%N,0});}
        if(h>0)v.push_back({x,h-1});
        if(h<tooth(x))v.push_back({x,h+1});
        deg[i]=v.size();K[i][i]=1;
        for(auto q:v)P[i][index[q]]=1.0/v.size();
    }
    double residual=0;
    for(int t=0;t<=12;++t) {
        for(int i=0;i<V;++i)for(int j=0;j<V;++j)
            residual=std::max(residual,std::abs(deg[i]*K[i][j]-deg[j]*K[j][i]));
        double outgoing=0,incoming=0;
        for(int x=0;x<N;++x)for(int y=0;y<N;++y) {
            int i=index[{x,0}],j=index[{y,0}];double q=(y+1.0)/(N+1.0);
            outgoing+=deg[i]*deg[i]*K[i][j]*K[i][j]*q;
            incoming+=deg[j]*deg[j]*K[j][i]*K[j][i]*q;
        }
        residual=std::max(residual,std::abs(outgoing-incoming));
        std::vector<std::vector<double>> nxt(V,std::vector<double>(V));
        for(int i=0;i<V;++i)for(int j=0;j<V;++j)for(int k=0;k<V;++k)nxt[i][j]+=K[i][k]*P[k][j];
        K.swap(nxt);
    }
    std::cout<<"finite-matrix detailed balance / backbone transport maximum residual="<<residual<<"\n";
    if(residual>1e-11)return 5;
    std::cout<<"PASS\n";
}
