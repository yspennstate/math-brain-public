#include <bits/stdc++.h>
#include <sys/mman.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
#include <boost/multiprecision/cpp_int.hpp>
#ifdef _OPENMP
#include <omp.h>
#endif
using namespace std;
using boost::multiprecision::cpp_int;
using boost::multiprecision::uint512_t;
uint512_t powu(uint64_t b,int e){uint512_t r=1;for(int i=0;i<e;i++)r*=b;return r;}
cpp_int gcdc(cpp_int a,cpp_int b){while(b!=0){cpp_int r=a%b;a=b;b=r;}return a;}
int main(int argc,char**argv){
 if(argc<6){cerr<<"usage: exact trans ZN ZD iter scale\n"; return 2;}
 string tf=argv[1]; uint64_t ZN=stoull(argv[2]), ZD=stoull(argv[3]); int niter=stoi(argv[4]); uint64_t SCALE=stoull(argv[5]);
 const size_t N=6419109; const int deg=30; int fd=open(tf.c_str(),O_RDONLY); if(fd<0){perror("open");return 3;} struct stat st;fstat(fd,&st); if((size_t)st.st_size!=N*(size_t)deg*4){cerr<<"bad size\n";return 4;} auto*tr=(const uint32_t*)mmap(nullptr,st.st_size,PROT_READ,MAP_SHARED,fd,0); if(tr==MAP_FAILED)return 5;
 long double z=(long double)ZN/(long double)ZD; vector<double>w(deg);int jj=0;for(int c=0;c<2;c++)for(int l=-7;l<=7;l++){int a=abs(l);w[jj++]=(a<7)?powl(z,a+2):powl(z,9)/(1-z);} vector<double>v(N,1.0),av(N);double mn=0,mx=0;
 for(int it=0;it<niter;it++){mn=DBL_MAX;mx=-DBL_MAX;double vmax=0;
  #pragma omp parallel for reduction(min:mn) reduction(max:mx,vmax) schedule(static)
  for(long long ii=0;ii<(long long)N;ii++){const uint32_t*row=tr+(size_t)ii*deg;double s=0;for(int j=0;j<deg;j++){uint32_t q=row[j];if(q)s+=w[j]*v[q-1];}av[ii]=s;double r=s/v[ii];if(r<mn)mn=r;if(r>mx)mx=r;if(s>vmax)vmax=s;}
  #pragma omp parallel for schedule(static)
  for(long long ii=0;ii<(long long)N;ii++)av[ii]/=vmax; v.swap(av);
 }
 vector<uint64_t>V(N); uint64_t vmin=ULLONG_MAX,vmaxv=0; for(size_t i=0;i<N;i++){ long double y=(long double)v[i]*(long double)SCALE; uint64_t q=(uint64_t)floor(y+0.5L); if(!q)q=1; V[i]=q;vmin=min(vmin,q);vmaxv=max(vmaxv,q); }
 uint64_t om=ZD-ZN; uint512_t D=uint512_t(om)*powu(ZD,8), coeff[8]; for(int a=0;a<=6;a++){int e=a+2; coeff[a]=uint512_t(om)*powu(ZN,e)*powu(ZD,8-e);} coeff[7]=powu(ZN,9);
 bool have=false; uint512_t maxsum=0; uint64_t maxv=1; size_t maxidx=0;
 #pragma omp parallel
 {bool lhave=false;uint512_t lsum=0;uint64_t lv=1;size_t li=0;
  #pragma omp for schedule(static)
  for(long long ii=0;ii<(long long)N;ii++){uint512_t sum=0;const uint32_t*row=tr+(size_t)ii*deg;int j=0;for(int c=0;c<2;c++)for(int l=-7;l<=7;l++,j++){uint32_t q=row[j];if(q)sum+=coeff[abs(l)]*V[q-1];}if(!lhave||sum*lv>lsum*V[ii]){lhave=true;lsum=sum;lv=V[ii];li=ii;}}
  #pragma omp critical
  {if(lhave&&(!have||lsum*maxv>maxsum*lv)){have=true;maxsum=lsum;maxv=lv;maxidx=li;}}
 }
 uint512_t den=D*maxv; if(!(maxsum<den)){cerr<<"lambda>=1\n";return 6;} cpp_int n=maxsum.convert_to<cpp_int>(), d=den.convert_to<cpp_int>(); cpp_int g=gcdc(n,d);n/=g;d/=g;
 long double lam=maxsum.convert_to<long double>()/den.convert_to<long double>(); long double bound=2*logl(2*z)/logl(lam);
 cout<<"states="<<N<<"\n"<<"z="<<ZN<<"/"<<ZD<<"\n"<<"iterations="<<niter<<" scale="<<SCALE<<" vmin="<<vmin<<" vmax="<<vmaxv<<"\n";cout<<setprecision(18)<<"search_min="<<mn<<" search_max="<<mx<<"\n";cout<<"worst_state="<<maxidx<<"\n";cout<<"lambda_num="<<n<<"\n"<<"lambda_den="<<d<<"\n";cout<<setprecision(30)<<"lambda_display="<<lam<<"\ncontinuous_bound_display="<<bound<<"\nEXACT_ALL_STATE_CONE_SCAN=PASS\nALL_EXACT_CHECKS_PASS\n";
 munmap((void*)tr,st.st_size);close(fd);
}
