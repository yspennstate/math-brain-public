#include <bits/stdc++.h>
#include <sys/mman.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
#include <omp.h>
using namespace std;
int main(int argc,char**argv){if(argc<3)return 2;string tf=argv[1],vf=argv[2];int iters=argc>3?atoi(argv[3]):85;uint64_t XN=513434,YN=513434,D0=1600000;const uint64_t SCALE=5000000000000000000ULL;const int deg=30;omp_set_num_threads(min(8,omp_get_max_threads()));int fd=open(tf.c_str(),O_RDONLY);struct stat st;fstat(fd,&st);size_t N=st.st_size/(deg*4);auto*tr=(const uint32_t*)mmap(nullptr,st.st_size,PROT_READ,MAP_SHARED,fd,0);long double x=(long double)XN/D0,y=x;float W[30];int jj=0;for(int c=0;c<2;c++)for(int l=-7;l<=7;l++){long double w;if(abs(l)<=6)w=l>=0?powl(x,l+1)*y:x*powl(y,-l+1);else w=l>0?powl(x,8)*y/(1-x):x*powl(y,8)/(1-y);W[jj++]=(float)w;}vector<float>v(N,1.0f),u(N),prev(N);float lastmn=0,lastmx=0;for(int it=0;it<iters;it++){float mx=0,mn=FLT_MAX;
#pragma omp parallel for reduction(max:mx) reduction(min:mn) schedule(static)
for(long long ii=0;ii<(long long)N;ii++){auto*r=tr+(size_t)ii*deg;float s=0;for(int j=0;j<deg;j++){uint32_t q=r[j];if(q)s+=W[j]*v[q-1];}u[ii]=s;float rr=s/v[ii];mx=max(mx,rr);mn=min(mn,rr);}float umax=*max_element(u.begin(),u.end());
#pragma omp parallel for schedule(static)
for(long long ii=0;ii<(long long)N;ii++)u[ii]/=umax;prev.swap(v);v.swap(u);if((it+1)==50 || (it+1)==70){float vmax=0;
#pragma omp parallel for reduction(max:vmax) schedule(static)
for(long long ii=0;ii<(long long)N;ii++){float q=v[ii]+4.0f*(v[ii]-prev[ii]);if(q<=0)q=FLT_MIN;v[ii]=q;vmax=max(vmax,q);}
#pragma omp parallel for schedule(static)
for(long long ii=0;ii<(long long)N;ii++)v[ii]/=vmax;}lastmn=mn;lastmx=mx;if((it+1)%5==0)cerr<<"it="<<it+1<<" mn="<<setprecision(10)<<mn<<" mx="<<mx<<" gap="<<mx-mn<<"\n";}float vm=*max_element(v.begin(),v.end());vector<uint64_t>V(N);uint64_t vmin=ULLONG_MAX,vmax=0;for(size_t i=0;i<N;i++){long double q=floorl((long double)v[i]/vm*SCALE);if(q<1)q=1;V[i]=(uint64_t)q;vmin=min(vmin,V[i]);vmax=max(vmax,V[i]);}FILE*fp=fopen(vf.c_str(),"wb");fwrite(V.data(),8,V.size(),fp);fclose(fp);cout<<"R17 C045 floating float32 witness search only\nproduct_states="<<N<<" iterations="<<iters<<"\n"<<setprecision(12)<<"last_mn="<<lastmn<<" last_mx="<<lastmx<<" gap="<<lastmx-lastmn<<"\nvmin="<<vmin<<" vmax="<<vmax<<"\nFLOATING_SEARCH_ONLY_NO_CERTIFICATE\n";}
