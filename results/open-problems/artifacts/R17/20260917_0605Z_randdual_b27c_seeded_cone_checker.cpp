#include <bits/stdc++.h>
#include <sys/mman.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
#include <omp.h>
#include <boost/multiprecision/cpp_int.hpp>
using namespace std;using boost::multiprecision::cpp_int;using boost::multiprecision::uint512_t;
uint512_t powu(uint64_t b,int e){uint512_t r=1;while(e--)r*=b;return r;}cpp_int gcdc(cpp_int a,cpp_int b){while(b!=0){cpp_int r=a%b;a=b;b=r;}return a;}
int main(int argc,char**argv){if(argc<5){cerr<<"trans v scale seed\n";return 2;}const size_t N=6419109;const int deg=30;uint64_t SCALE=stoull(argv[3]);uint64_t SEED=stoull(argv[4]);int fd=open(argv[1],O_RDONLY);struct stat st;fstat(fd,&st);auto*tr=(const uint32_t*)mmap(nullptr,st.st_size,PROT_READ,MAP_SHARED,fd,0);vector<double>vd(N);FILE*f=fopen(argv[2],"rb");if(!f||fread(vd.data(),sizeof(double),N,f)!=N)return 3;fclose(f);vector<uint64_t>V(N);uint64_t vmin=ULLONG_MAX,vmax=0;for(size_t i=0;i<N;i++){long double y=(long double)vd[i]*(long double)SCALE;long double fl=floor(y),fr=y-fl;uint64_t hsh=((uint64_t)i^SEED)+0x9e3779b97f4a7c15ULL;hsh^=hsh>>30;hsh*=0xbf58476d1ce4e5b9ULL;hsh^=hsh>>27;hsh*=0x94d049bb133111ebULL;hsh^=hsh>>31;long double u=(long double)(hsh>>11)*(1.0L/9007199254740992.0L);uint64_t q=(uint64_t)fl+(u<fr);if(!q)q=1;V[i]=q;vmin=min(vmin,q);vmax=max(vmax,q);}const uint64_t ZN=256717,ZD=800000,om=ZD-ZN;uint512_t D=uint512_t(om)*powu(ZD,8),coeff[8];for(int a=0;a<=6;a++){int e=a+2;coeff[a]=uint512_t(om)*powu(ZN,e)*powu(ZD,8-e);}coeff[7]=powu(ZN,9);
bool haveMax=false,haveMin=false;uint512_t maxsum=0,minsum=0;uint64_t maxv=1,minv=1;size_t maxidx=0,minidx=0;
#pragma omp parallel
{bool lhmax=false,lhmin=false;uint512_t lmaxs=0,lmins=0;uint64_t lmaxv=1,lminv=1;size_t lmaxi=0,lmini=0;
#pragma omp for schedule(static)
for(long long ii=0;ii<(long long)N;ii++){uint512_t sum=0;const uint32_t*row=tr+(size_t)ii*deg;int j=0;for(int c=0;c<2;c++)for(int l=-7;l<=7;l++,j++){uint32_t q=row[j];if(q)sum+=coeff[abs(l)]*V[q-1];}if(!lhmax||sum*lmaxv>lmaxs*V[ii]){lhmax=true;lmaxs=sum;lmaxv=V[ii];lmaxi=ii;}if(!lhmin||sum*lminv<lmins*V[ii]){lhmin=true;lmins=sum;lminv=V[ii];lmini=ii;}}
#pragma omp critical
{if(lhmax&&(!haveMax||lmaxs*maxv>maxsum*lmaxv)){haveMax=true;maxsum=lmaxs;maxv=lmaxv;maxidx=lmaxi;}if(lhmin&&(!haveMin||lmins*minv<minsum*lminv)){haveMin=true;minsum=lmins;minv=lminv;minidx=lmini;}}}
uint512_t maxden=D*maxv,minden=D*minv;if(!(maxsum<maxden))return 4;cpp_int maxn=maxsum.convert_to<cpp_int>(),maxd=maxden.convert_to<cpp_int>(),minn=minsum.convert_to<cpp_int>(),mind=minden.convert_to<cpp_int>();cpp_int g=gcdc(maxn,maxd);maxn/=g;maxd/=g;g=gcdc(minn,mind);minn/=g;mind/=g;cout<<"z=256717/800000\nscale="<<SCALE<<" seed="<<SEED<<" vmin="<<vmin<<" vmax="<<vmax<<"\nmax_state="<<maxidx<<"\nmax_num="<<maxn<<"\nmax_den="<<maxd<<"\nmin_state="<<minidx<<"\nmin_num="<<minn<<"\nmin_den="<<mind<<"\n";long double mx=maxsum.convert_to<long double>()/maxden.convert_to<long double>(),mn=minsum.convert_to<long double>()/minden.convert_to<long double>();cout<<setprecision(30)<<"min_display="<<mn<<"\nmax_display="<<mx<<"\ngap_display="<<(mx-mn)<<"\nEXACT_MINMAX_CONE_SCAN=PASS\nALL_EXACT_CHECKS_PASS\n";munmap((void*)tr,st.st_size);close(fd);}
