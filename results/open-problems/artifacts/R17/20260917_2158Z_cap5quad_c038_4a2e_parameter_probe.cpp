#include <bits/stdc++.h>
#include <sys/mman.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
#include <omp.h>
using namespace std;
int main(int argc,char**argv){if(argc<2){cerr<<"table\n";return 2;}const int deg=30;string tf=argv[1];int fd=open(tf.c_str(),O_RDONLY);struct stat st;fstat(fd,&st);size_t N=st.st_size/(deg*4);auto*tr=(const uint32_t*)mmap(nullptr,st.st_size,PROT_READ,MAP_SHARED,fd,0);const long long D0=1600000,X0=513401,Y0=513467;vector<double>v(N,1.0),u(N),prev(N);auto eval=[&](long long XN,long long YN,int iters){long double x=(long double)XN/D0,y=(long double)YN/D0;double W[30];int jj=0;for(int c=0;c<2;c++)for(int l=-7;l<=7;l++){long double w;if(abs(l)<=6)w=l>=0?powl(x,l+1)*y:x*powl(y,-l+1);else w=l>0?powl(x,8)*y/(1-x):x*powl(y,8)/(1-y);W[jj++]=(double)w;}double mx=0,mn=0;for(int it=0;it<iters;it++){mx=0;mn=DBL_MAX;
#pragma omp parallel for reduction(max:mx) reduction(min:mn) schedule(static)
for(long long ii=0;ii<(long long)N;ii++){const uint32_t*r=tr+(size_t)ii*deg;double s=0;for(int j=0;j<deg;j++){uint32_t q=r[j];if(q)s+=W[j]*v[q-1];}u[ii]=s;double rr=s/v[ii];mx=max(mx,rr);mn=min(mn,rr);}double umax=*max_element(u.begin(),u.end());
#pragma omp parallel for schedule(static)
for(long long ii=0;ii<(long long)N;ii++)u[ii]/=umax;prev.swap(v);v.swap(u);}long double B=logl(4*x*y)/logl((long double)mx);cout<<XN<<" "<<YN<<" "<<setprecision(18)<<mx<<" "<<mn<<" "<<(mx-mn)<<" "<<setprecision(20)<<B<<"\n";};
// converge at center
 eval(X0,Y0,240);
 const int s=16;
 vector<pair<int,int>> ds={{s,0},{-s,0},{0,s},{0,-s},{s,s},{s,-s},{-s,s},{-s,-s},{2*s,0},{-2*s,0},{0,2*s},{0,-2*s}};
 for(auto [dx,dy]:ds)eval(X0+dx,Y0+dy,60);
 munmap((void*)tr,st.st_size);close(fd);
}
