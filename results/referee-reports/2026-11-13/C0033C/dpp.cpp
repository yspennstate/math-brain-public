#include <algorithm>
#include <cmath>
#include <complex>
#include <cstdint>
#include <vector>
using Z=std::complex<double>;
// Exhaustive atom probabilities and analytic directional derivatives.
// Inputs are interleaved real/imaginary, row major. No BLAS or worker threads.
extern "C" int dpp_stats(int n,const double* qr,const double* ar,double* out){
 if(n<1 || n>18) return 1;
 std::vector<Z> q(n*n),a(n*n),b(n*n),v(n*n),c(n*n);
 for(int j=0;j<n*n;++j){q[j]=Z(qr[2*j],qr[2*j+1]);a[j]=Z(ar[2*j],ar[2*j+1]);}
 long double h=0,h2=0,mass=0,d1=0,d2=0;
 double minp=1;
 for(uint64_t s=0;s<(1ULL<<n);++s){
  b=q; std::fill(v.begin(),v.end(),Z(0));
  for(int i=0;i<n;++i){b[i*n+i]-=((s>>i)&1)?0.:1.;v[i*n+i]=1.;}
  Z det=1.;
  for(int k=0;k<n;++k){
   int piv=k; for(int i=k+1;i<n;++i) if(std::abs(b[i*n+k])>std::abs(b[piv*n+k]))piv=i;
   if(std::abs(b[piv*n+k])<1e-300)return 2;
   if(piv!=k){for(int j=0;j<n;++j){std::swap(b[k*n+j],b[piv*n+j]);std::swap(v[k*n+j],v[piv*n+j]);}det=-det;}
   Z f=b[k*n+k];det*=f;
   for(int j=0;j<n;++j){b[k*n+j]/=f;v[k*n+j]/=f;}
   for(int i=0;i<n;++i)if(i!=k){f=b[i*n+k];for(int j=0;j<n;++j){b[i*n+j]-=f*b[k*n+j];v[i*n+j]-=f*v[k*n+j];}}
  }
  double p=det.real()*((n-__builtin_popcountll(s))%2?-1.:1.);
  if(!std::isfinite(p) || p<=0 || std::abs(det.imag())>1e-8*std::abs(det.real()))return 3;
  for(int i=0;i<n;++i)for(int j=0;j<n;++j){Z z=0.;for(int k=0;k<n;++k)z+=v[i*n+k]*a[k*n+j];c[i*n+j]=z;}
  Z tr=0.,tr2=0.;for(int i=0;i<n;++i){tr+=c[i*n+i];for(int j=0;j<n;++j)tr2+=c[i*n+j]*c[j*n+i];}
  double r=tr.real(),r2=(tr*tr-tr2).real(),lp=std::log(p);
  h-=(long double)p*lp;
  h2-=(long double)p*(r*r+lp*r2);
  mass+=p;d1+=p*r;d2+=p*r2;minp=std::min(minp,p);
 }
 out[0]=h;out[1]=h2;out[2]=mass;out[3]=minp;out[4]=d1;out[5]=d2;
 for(int i=0;i<6;++i)if(!std::isfinite(out[i]))return 4;
 return 0;
}
