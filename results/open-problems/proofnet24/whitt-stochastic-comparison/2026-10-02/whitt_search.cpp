#include <algorithm>
#include <array>
#include <cmath>
#include <cstdint>
#include <cstdio>
#include <random>
#include <vector>

struct Model { double a,b,p,delta,lambda; int split; };
int main(){
 std::mt19937_64 rng(70122026); std::uniform_real_distribution<double> unif(0,1);
 constexpr long n=1000000,burn=10000; const int m=10;
 const std::array<double,m> xs={0,.001,.01,.05,.1,.25,.5,1,2,5};
 double best=0;
 for(int z=0;z<320;z++){
  double a=std::exp(-5+5*unif(rng)), b=std::exp(.05+4.95*unif(rng));
  double p=(b-1)/(b-a), load=.03+.92*unif(rng), lam=2*load;
  int split=z%2; double center=split?a:b; double delta=center*(.1+.9*unif(rng));
  double x0=0,y0=0,x1=0,y1=0;
  std::array<long,m> hits0={},hits1={};
  for(long k=0;k<n+burn;k++){
   double dt=-std::log(unif(rng))/lam;
   x0=std::max(0.,x0-dt);y0=std::max(0.,y0-dt);
   x1=std::max(0.,x1-dt);y1=std::max(0.,y1-dt);
   bool low=unif(rng)<p; double s0=low?a:b; double s1=s0;
   if(low==bool(split)) s1+=unif(rng)<.5?-delta:delta;
   if(k>=burn) for(int j=0;j<m;j++){hits0[j]+=x0>xs[j];hits1[j]+=x1>xs[j];}
   x0+=s0;if(x0>y0)std::swap(x0,y0);
   x1+=s1;if(x1>y1)std::swap(x1,y1);
  }
  for(int j=0;j<m;j++){
   double diff=double(hits1[j]-hits0[j])/n;
   if(diff<best){best=diff;std::printf("best %.8f z%d a%.12g b%.12g p%.12g split%d delta%.12g lambda%.12g threshold%.12g p0%.8f p1%.8f\n",diff,z,a,b,p,split,delta,lam,xs[j],double(hits0[j])/n,double(hits1[j])/n);std::fflush(stdout);}
  }
 }
}
