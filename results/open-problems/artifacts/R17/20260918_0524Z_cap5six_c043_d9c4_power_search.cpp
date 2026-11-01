#include <bits/stdc++.h>
#include <sys/mman.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
#include <omp.h>
using namespace std;
int main(int argc,char**argv){if(argc<3){cerr<<"usage: power_search product.bin witness.bin [iters] [XN] [YN] [D]\n";return 2;}string tf=argv[1],vf=argv[2];int iters=argc>3?atoi(argv[3]):90;uint64_t XN=argc>4?strtoull(argv[4],0,10):513434,YN=argc>5?strtoull(argv[5],0,10):513434,D0=argc>6?strtoull(argv[6],0,10):1600000;const uint64_t SCALE=5000000000000000000ULL;const int deg=30;omp_set_num_threads(min(5,omp_get_max_threads()));int fd=open(tf.c_str(),O_RDONLY);if(fd<0){perror("open");return 3;}struct stat st;if(fstat(fd,&st)){perror("fstat");return 4;}size_t N=st.st_size/(deg*4);auto*tr=(const uint32_t*)mmap(nullptr,st.st_size,PROT_READ,MAP_SHARED,fd,0);long double x=(long double)XN/D0,y=(long double)YN/D0;double W[30];int jj=0;for(int c=0;c<2;c++)for(int l=-7;l<=7;l++){long double w;if(abs(l)<=6)w=l>=0?powl(x,l+1)*y:x*powl(y,-l+1);else w=l>0?powl(x,8)*y/(1-x):x*powl(y,8)/(1-y);W[jj++]=(double)w;}vector<double>v(N,1.0),u(N),prev(N);double lastmn=0,lastmx=0;for(int it=0;it<iters;it++){double mx=0,mn=DBL_MAX;
#pragma omp parallel for reduction(max:mx) reduction(min:mn) schedule(static)
for(long long ii=0;ii<(long long)N;ii++){auto*r=tr+(size_t)ii*deg;double s=0;for(int j=0;j<deg;j++){uint32_t q=r[j];if(q)s+=W[j]*v[q-1];}u[ii]=s;double rr=s/v[ii];mx=max(mx,rr);mn=min(mn,rr);}double umax=*max_element(u.begin(),u.end());
#pragma omp parallel for schedule(static)
for(long long ii=0;ii<(long long)N;ii++)u[ii]/=umax;prev.swap(v);v.swap(u);if((it+1)%60==0&&it+1<iters){double vmax=0;
#pragma omp parallel for reduction(max:vmax) schedule(static)
for(long long ii=0;ii<(long long)N;ii++){double q=v[ii]+4*(v[ii]-prev[ii]);if(q<=0)q=DBL_MIN;v[ii]=q;vmax=max(vmax,q);}
#pragma omp parallel for schedule(static)
for(long long ii=0;ii<(long long)N;ii++)v[ii]/=vmax;}lastmn=mn;lastmx=mx;if((it+1)%10==0)cerr<<"it="<<it+1<<" mn="<<setprecision(17)<<mn<<" mx="<<mx<<" gap="<<mx-mn<<"\n";}
double vm=*max_element(v.begin(),v.end());vector<uint64_t>V(N);uint64_t vmin=ULLONG_MAX,vmax=0;for(size_t i=0;i<N;i++){long double q=floorl((long double)v[i]/vm*SCALE);if(q<1)q=1;V[i]=(uint64_t)q;vmin=min(vmin,V[i]);vmax=max(vmax,V[i]);}FILE*fp=fopen(vf.c_str(),"wb");if(!fp){perror("fopen");return 5;}fwrite(V.data(),sizeof(uint64_t),V.size(),fp);fclose(fp);cout<<"R17 C043 floating witness search only\nproduct_states="<<N<<" iterations="<<iters<<" x="<<XN<<"/"<<D0<<" y="<<YN<<"/"<<D0<<"\n"<<setprecision(17)<<"last_mn="<<lastmn<<" last_mx="<<lastmx<<" gap="<<lastmx-lastmn<<"\nvmin="<<vmin<<" vmax="<<vmax<<"\nFLOATING_SEARCH_ONLY_NO_CERTIFICATE\n";}
