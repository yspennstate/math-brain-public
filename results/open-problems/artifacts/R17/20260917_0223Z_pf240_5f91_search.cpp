// R17 search-only helper for h=8 Perron-vector refinement.
// Floating point is used only to locate a positive direction; no theorem claim
// relies on these ratios. The resulting vector is rounded and independently
// checked by the exact checker in the same run.
#include <bits/stdc++.h>
#include <sys/mman.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
#ifdef _OPENMP
#include <omp.h>
#endif
using namespace std;
int main(int argc,char**argv){if(argc<5){cerr<<"trans vec niter z\n";return 2;}string tf=argv[1],vf=argv[2];int niter=atoi(argv[3]);double z=atof(argv[4]);const size_t N=6419109;const int deg=30;int fd=open(tf.c_str(),O_RDONLY);if(fd<0){perror("open");return 3;}struct stat st;fstat(fd,&st);if((size_t)st.st_size!=N*deg*4){cerr<<"bad trans size "<<st.st_size<<"\n";return 4;}auto*tr=(const uint32_t*)mmap(nullptr,st.st_size,PROT_READ,MAP_SHARED,fd,0);if(tr==MAP_FAILED)return 5;vector<double>v(N),av(N);FILE*f=fopen(vf.c_str(),"rb");if(f){size_t r=fread(v.data(),sizeof(double),N,f);fclose(f);if(r!=N){cerr<<"bad vec\n";return 6;}}else fill(v.begin(),v.end(),1.0);vector<double>w(deg);int jj=0;for(int c=0;c<2;c++)for(int l=-7;l<=7;l++){int a=abs(l);w[jj++]=(a<7)?pow(z,a+2):pow(z,9)/(1-z);}double mn=0,mx=0;
for(int it=0;it<niter;it++){
 mn=DBL_MAX;mx=-DBL_MAX;double vmax=0;
 #pragma omp parallel for reduction(min:mn) reduction(max:mx,vmax) schedule(static)
 for(long long ii=0;ii<(long long)N;ii++){const uint32_t*row=tr+(size_t)ii*deg;double s=0;for(int j=0;j<deg;j++){uint32_t q=row[j];if(q)s+=w[j]*v[q-1];}av[ii]=s;double r=s/v[ii];if(r<mn)mn=r;if(r>mx)mx=r;if(s>vmax)vmax=s;}
 #pragma omp parallel for schedule(static)
 for(long long ii=0;ii<(long long)N;ii++)av[ii]/=vmax;
 v.swap(av);
}
f=fopen(vf.c_str(),"wb");fwrite(v.data(),sizeof(double),N,f);fclose(f);cout<<setprecision(17)<<"z="<<z<<" niter="<<niter<<" min="<<mn<<" max="<<mx<<" bound_display="<<2*log(2*z)/log(mx)<<"\n";munmap((void*)tr,st.st_size);close(fd);return 0;}
