#include <bits/stdc++.h>
#include <sys/mman.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
#include <omp.h>
using namespace std;
int main(int argc,char**argv){if(argc<4)return 2;string tf=argv[1],inw=argv[2],outw=argv[3];int iters=argc>4?atoi(argv[4]):30;const uint64_t SCALE=5000000000000000000ULL;const int deg=30;omp_set_num_threads(min(12,omp_get_max_threads()));int fd=open(tf.c_str(),O_RDONLY),fw=open(inw.c_str(),O_RDONLY);struct stat st,sw;fstat(fd,&st);fstat(fw,&sw);size_t N=st.st_size/(deg*4);auto*tr=(const uint32_t*)mmap(nullptr,st.st_size,PROT_READ,MAP_SHARED,fd,0);auto*Vin=(const uint64_t*)mmap(nullptr,sw.st_size,PROT_READ,MAP_SHARED,fw,0);long double x=(long double)513434/1600000,y=x;double W[30];int jj=0;for(int c=0;c<2;c++)for(int l=-7;l<=7;l++){long double w;if(abs(l)<=6)w=l>=0?powl(x,l+1)*y:x*powl(y,-l+1);else w=l>0?powl(x,8)*y/(1-x):x*powl(y,8)/(1-y);W[jj++]=(double)w;}vector<double>v(N),u(N);double vm0=0;for(size_t i=0;i<N;i++){v[i]=(double)((long double)Vin[i]/SCALE);vm0=max(vm0,v[i]);}for(auto&z:v)z/=vm0;double mn=0,mx=0;for(int it=0;it<iters;it++){mx=0;mn=DBL_MAX;double umax=0;
#pragma omp parallel for reduction(max:mx,umax) reduction(min:mn) schedule(static)
for(long long ii=0;ii<(long long)N;ii++){auto*r=tr+(size_t)ii*deg;double s=0;for(int j=0;j<deg;j++){uint32_t q=r[j];if(q)s+=W[j]*v[q-1];}u[ii]=s;double rr=s/v[ii];mx=max(mx,rr);mn=min(mn,rr);umax=max(umax,s);}
#pragma omp parallel for schedule(static)
for(long long ii=0;ii<(long long)N;ii++)u[ii]/=umax;v.swap(u);}double vm=*max_element(v.begin(),v.end());vector<uint64_t>V(N);for(size_t i=0;i<N;i++){long double q=floorl((long double)v[i]/vm*SCALE);if(q<1)q=1;V[i]=(uint64_t)q;}FILE*fp=fopen(outw.c_str(),"wb");fwrite(V.data(),8,V.size(),fp);fclose(fp);cout<<"R17 C044 double witness refinement search only\nstates="<<N<<" iters="<<iters<<" mn="<<setprecision(17)<<mn<<" mx="<<mx<<" gap="<<mx-mn<<"\nFLOATING_SEARCH_ONLY_NO_CERTIFICATE\n";}
