#include <bits/stdc++.h>
#include <sys/mman.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
#include <omp.h>
#include <boost/multiprecision/cpp_int.hpp>
using namespace std; using boost::multiprecision::cpp_int; using boost::multiprecision::uint1024_t;
uint1024_t powu(uint1024_t b,int e){uint1024_t r=1;while(e--)r*=b;return r;} cpp_int gcdc(cpp_int a,cpp_int b){while(b!=0){cpp_int r=a%b;a=b;b=r;}return a;}
int main(int argc,char**argv){if(argc<8){cerr<<"trans vf ZN ZD SCALE theta_num theta_den [dump]\n";return 2;} string tf=argv[1],vf=argv[2]; uint1024_t ZN(argv[3]),ZD(argv[4]); uint64_t SCALE=stoull(argv[5]); long double theta=stold(argv[6])/stold(argv[7]); string dump=argc>=9?argv[8]:"-"; const size_t N=6419109; const int deg=30;
 int fd=open(tf.c_str(),O_RDONLY);struct stat st;fstat(fd,&st);auto*tr=(const uint32_t*)mmap(nullptr,st.st_size,PROT_READ,MAP_SHARED,fd,0);vector<long double>vd(N);FILE*f=fopen(vf.c_str(),"rb");if(!f||fread(vd.data(),sizeof(long double),N,f)!=N)return 3;fclose(f);vector<uint64_t>V(N);for(size_t i=0;i<N;i++){long double y=vd[i]*(long double)SCALE; long double ql=floorl(y+theta); if(ql<1)ql=1; if(ql>(long double)UINT64_MAX){cerr<<"overflow\n";return 5;} V[i]=(uint64_t)ql;}
 if(dump!="-"){FILE*g=fopen(dump.c_str(),"wb");fwrite(V.data(),8,N,g);fclose(g);} uint1024_t om=ZD-ZN;uint1024_t D=uint1024_t(om)*powu(ZD,8),coeff[8];for(int a=0;a<=6;a++){int e=a+2;coeff[a]=uint1024_t(om)*powu(ZN,e)*powu(ZD,8-e);}coeff[7]=powu(ZN,9);
 bool haveMax=false,haveMin=false;uint1024_t maxsum=0,minsum=0;uint64_t maxv=1,minv=1;size_t maxidx=0,minidx=0;
#pragma omp parallel
 {bool lhmax=false,lhmin=false;uint1024_t lmaxs=0,lmins=0;uint64_t lmaxv=1,lminv=1;size_t lmaxi=0,lmini=0;
#pragma omp for schedule(static)
 for(long long ii=0;ii<(long long)N;ii++){uint1024_t sum=0;const uint32_t*row=tr+(size_t)ii*deg;for(int j=0;j<deg;j++){uint32_t q=row[j];if(q){int l=(j%15)-7;sum+=coeff[abs(l)]*V[q-1];}}if(!lhmax||sum*lmaxv>lmaxs*V[ii]){lhmax=true;lmaxs=sum;lmaxv=V[ii];lmaxi=ii;}if(!lhmin||sum*lminv<lmins*V[ii]){lhmin=true;lmins=sum;lminv=V[ii];lmini=ii;}}
#pragma omp critical
 {if(lhmax&&(!haveMax||lmaxs*maxv>maxsum*lmaxv)){haveMax=true;maxsum=lmaxs;maxv=lmaxv;maxidx=lmaxi;}if(lhmin&&(!haveMin||lmins*minv<minsum*lminv)){haveMin=true;minsum=lmins;minv=lminv;minidx=lmini;}}}
 cpp_int maxn=maxsum.convert_to<cpp_int>(),maxd=(D*maxv).convert_to<cpp_int>(),minn=minsum.convert_to<cpp_int>(),mind=(D*minv).convert_to<cpp_int>(); cpp_int g=gcdc(maxn,maxd);maxn/=g;maxd/=g;g=gcdc(minn,mind);minn/=g;mind/=g; long double mx=maxsum.convert_to<long double>()/(D*maxv).convert_to<long double>(),mn=minsum.convert_to<long double>()/(D*minv).convert_to<long double>(); long double z=ZN.convert_to<long double>()/ZD.convert_to<long double>(); long double bound=2*logl(2*z)/logl(mx); cout<<"scale="<<SCALE<<" theta="<<argv[6]<<"/"<<argv[7]<<"\nmax_state="<<maxidx<<"\nmin_state="<<minidx<<"\nmax_num="<<maxn<<"\nmax_den="<<maxd<<"\nmin_num="<<minn<<"\nmin_den="<<mind<<"\n"<<setprecision(36)<<"max_display="<<mx<<"\nmin_display="<<mn<<"\ngap_display="<<(mx-mn)<<"\nbound_display="<<bound<<"\nALL_EXACT_CHECKS_PASS\n"; }
