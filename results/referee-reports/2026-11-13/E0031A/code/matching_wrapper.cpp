// Private research driver for Kolmogorov's Blossom V (2009), v2.05.
// Complete graph; integer weights and a complementary-slackness check.
#include <cmath>
#include <vector>
#include <cstdint>
#include <exception>
#include "PerfectMatching.h"
extern "C" int solve_matching(int n,int d,const double* x,long long scale,int* partner,long long* quantized,double* length) {
 try {
  if(n<2 || (n&1) || n>4096 || d<1 || d>8 || scale<1 || scale>1000000000000LL) return 10;
  const int ecount=n*(n-1)/2;
  std::vector<int> edges(2*ecount);
  std::vector<PerfectMatching::REAL> weights(ecount);
  PerfectMatching pm(n,ecount); pm.options.verbose=false;
  int e=0;
  for(int i=0;i<n;i++) for(int j=i+1;j<n;j++,e++) {
   long double ds=0;
   for(int k=0;k<d;k++){long double dx=(long double)x[i*d+k]-x[j*d+k]; ds+=dx*dx;}
   long long w=llroundl(sqrtl(ds)*scale);
   edges[2*e]=i;edges[2*e+1]=j;weights[e]=w;
   if(pm.AddEdge(i,j,w)!=e) return 11;
  }
  pm.Solve();
  int status=CheckPerfectMatchingOptimality(n,ecount,edges.data(),weights.data(),&pm,0);
  if(status) return 20+status;
  *quantized=0; long double total=0;
  for(int i=0;i<n;i++) {
   int j=pm.GetMatch(i);partner[i]=j;
   if(j<0 || j>=n || j==i || pm.GetMatch(j)!=i) return 12;
   if(i<j){
    long double ds=0;
    for(int k=0;k<d;k++){long double dx=(long double)x[i*d+k]-x[j*d+k];ds+=dx*dx;}
    total+=sqrtl(ds);
    // Index into lexicographically enumerated upper triangular edges.
    int idx=i*(2*n-i-1)/2+j-i-1;
    *quantized+=weights[idx];
   }
  }
  *length=(double)total;
  return 0;
 } catch(...) {return 99;}
}
