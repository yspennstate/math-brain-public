// R17-C028 SEARCH-ONLY recipe.  No floating inequality produced here is part
// of the theorem.  Input is the already validated h=8 transition table.
// Actual C028 path:
//   ./search trans.bin x y 140 v140.bin
//   ./search trans.bin x y 60 v200.bin v140.bin
// with x=0.32087625, y=0.32091625.  The exact checker then normalizes v200,
// floors it at scale 18e18, and rechecks every one of 6,419,109 rows exactly.
#include <bits/stdc++.h>
#include <sys/mman.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
#include <omp.h>
using namespace std;
int main(int argc,char**argv){if(argc<6){cerr<<"trans x y steps outvec [invec]\n";return 2;}string tf=argv[1];double x=stod(argv[2]),y=stod(argv[3]);int steps=atoi(argv[4]);string out=argv[5];string in=argc>6?argv[6]:"";const size_t N=6419109;const int deg=30;int fd=open(tf.c_str(),O_RDONLY);struct stat st;fstat(fd,&st);auto*tr=(const uint32_t*)mmap(nullptr,st.st_size,PROT_READ,MAP_SHARED,fd,0);
double w[30];int jj=0;for(int c=0;c<2;c++)for(int l=-7;l<=7;l++){double ww;if(l==0)ww=x*y;else if(l>0&&l<7)ww=pow(x,l+1)*y;else if(l<0&&-l<7)ww=x*pow(y,-l+1);else if(l==7)ww=pow(x,8)*y/(1-x);else ww=x*pow(y,8)/(1-y);w[jj++]=ww;}
vector<double>v(N,1.0),a(N),prev(N);if(!in.empty()){FILE*f=fopen(in.c_str(),"rb");if(!f||fread(v.data(),8,N,f)!=N)return 3;fclose(f);double vm=*max_element(v.begin(),v.end());for(auto&q:v)q/=vm;}
auto step=[&](){double vmax=0;
#pragma omp parallel for reduction(max:vmax) schedule(static)
for(long long ii=0;ii<(long long)N;ii++){const uint32_t*row=tr+(size_t)ii*deg;double s=0;for(int j=0;j<deg;j++){uint32_t q=row[j];if(q)s+=w[j]*v[q-1];}a[ii]=s;vmax=max(vmax,s);}
#pragma omp parallel for schedule(static)
for(long long ii=0;ii<(long long)N;ii++)a[ii]/=vmax;v.swap(a);};
for(int it=0;it<steps;it++){prev=v;step();if((it+1)==60||(it+1)==120||(it+1)==180){
#pragma omp parallel for schedule(static)
for(long long i=0;i<(long long)N;i++){double q=v[i]+6.0*(v[i]-prev[i]);if(q<=0)q=DBL_MIN;v[i]=q;}double vm=*max_element(v.begin(),v.end());
#pragma omp parallel for schedule(static)
for(long long i=0;i<(long long)N;i++)v[i]/=vm;}}
FILE*f=fopen(out.c_str(),"wb");if(!f||fwrite(v.data(),8,N,f)!=N)return 4;fclose(f);munmap((void*)tr,st.st_size);close(fd);}
