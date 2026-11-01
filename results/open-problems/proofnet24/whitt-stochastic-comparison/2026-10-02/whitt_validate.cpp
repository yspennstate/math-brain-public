#include <algorithm>
#include <array>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <random>
int main(int argc,char**argv){
 long n=argc>1?atol(argv[1]):50000000; long seed=argc>2?atol(argv[2]):1701;
 std::mt19937_64 rng(seed);std::uniform_real_distribution<double>U(0,1);
 const std::array<double,9>xs={0,.001,.01,.05,.1,.25,.5,1,2};
 double x0=0,y0=0,x1=0,y1=0;std::array<long,9>h0={},h1={};
 const long burn=100000; const double a=.2,b=1.6,p=3./7,delta=.2,lam=1.1;
 double sum0=0,sum1=0;
 for(long k=0;k<n+burn;k++){
  double dt=-log(U(rng))/lam;x0=std::max(0.,x0-dt);y0=std::max(0.,y0-dt);x1=std::max(0.,x1-dt);y1=std::max(0.,y1-dt);
  bool low=U(rng)<p;double s0=low?a:b,s1=s0;if(low)s1+=U(rng)<.5?-delta:delta;
  if(k>=burn){for(int j=0;j<9;j++){h0[j]+=x0>xs[j];h1[j]+=x1>xs[j];}sum0+=x0;sum1+=x1;}
  x0+=s0;if(x0>y0)std::swap(x0,y0);x1+=s1;if(x1>y1)std::swap(x1,y1);
 }
 for(int j=0;j<9;j++)printf("x%.3f base%.10f spread%.10f difference%.10f\n",xs[j],double(h0[j])/n,double(h1[j])/n,double(h1[j]-h0[j])/n);
 printf("mean_base%.10f mean_spread%.10f difference%.10f\n",sum0/n,sum1/n,(sum1-sum0)/n);
}
