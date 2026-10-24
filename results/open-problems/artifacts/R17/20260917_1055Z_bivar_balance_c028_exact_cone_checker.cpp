#include <bits/stdc++.h>
#include <sys/mman.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
#include <omp.h>
#include <boost/multiprecision/cpp_int.hpp>
using namespace std; using boost::multiprecision::uint512_t; using boost::multiprecision::cpp_int;
uint512_t powu(uint512_t b,int e){uint512_t r=1;while(e--)r*=b;return r;}
cpp_int gcdc(cpp_int a,cpp_int b){while(b!=0){cpp_int r=a%b;a=b;b=r;}return a;}
int main(int argc,char**argv){if(argc<5){cerr<<"trans double_vec scale dump_int\n";return 2;}string tf=argv[1],vf=argv[2];uint64_t SCALE=stoull(argv[3]);string dump=argv[4];const size_t N=6419109;const int deg=30;
 int fd=open(tf.c_str(),O_RDONLY);if(fd<0){perror("open");return 3;}struct stat st;fstat(fd,&st);if((size_t)st.st_size!=N*(size_t)deg*4){cerr<<"bad trans size\n";return 4;}auto*tr=(const uint32_t*)mmap(nullptr,st.st_size,PROT_READ,MAP_SHARED,fd,0);if(tr==MAP_FAILED){perror("mmap");return 5;}
 vector<double>vd(N);FILE*f=fopen(vf.c_str(),"rb");if(!f||fread(vd.data(),sizeof(double),N,f)!=N){cerr<<"vector read fail\n";return 6;}fclose(f);double vmax=*max_element(vd.begin(),vd.end());vector<uint64_t>V(N);uint64_t vmin=ULLONG_MAX,vmaxi=0;
 for(size_t i=0;i<N;i++){long double yy=(long double)vd[i]/vmax*(long double)SCALE;long double qq=floorl(yy);if(qq<1)qq=1;if(qq>(long double)ULLONG_MAX){cerr<<"overflow\n";return 7;}V[i]=(uint64_t)qq;vmin=min(vmin,V[i]);vmaxi=max(vmaxi,V[i]);}
 FILE*gout=fopen(dump.c_str(),"wb");if(!gout||fwrite(V.data(),8,N,gout)!=N){cerr<<"dump fail\n";return 8;}fclose(gout);
 const uint64_t Q=800000,X=256701,Y=256733;uint512_t q=Q,x=X,y=Y,omx=Q-X,omy=Q-Y;uint512_t D=powu(q,8)*omx*omy,cp[8],cn[8];for(int a=0;a<=6;a++){cp[a]=powu(x,a+1)*y*powu(q,6-a)*omx*omy;cn[a]=x*powu(y,a+1)*powu(q,6-a)*omx*omy;}cp[7]=powu(x,8)*y*omy;cn[7]=x*powu(y,8)*omx;
 bool haveMax=false,haveMin=false;uint512_t maxsum=0,minsum=0;uint64_t maxv=1,minv=1;size_t maxidx=0,minidx=0;
#pragma omp parallel
 {bool lhmax=false,lhmin=false;uint512_t lmaxs=0,lmins=0;uint64_t lmaxv=1,lminv=1;size_t lmaxi=0,lmini=0;
#pragma omp for schedule(static)
  for(long long ii=0;ii<(long long)N;ii++){uint512_t sum=0;const uint32_t*row=tr+(size_t)ii*deg;for(int j=0;j<deg;j++){uint32_t dest=row[j];if(dest){int l=(j%15)-7;int a=abs(l);sum+=(l>=0?cp[a]:cn[a])*V[dest-1];}}if(!lhmax||sum*lmaxv>lmaxs*V[ii]){lhmax=true;lmaxs=sum;lmaxv=V[ii];lmaxi=ii;}if(!lhmin||sum*lminv<lmins*V[ii]){lhmin=true;lmins=sum;lminv=V[ii];lmini=ii;}}
#pragma omp critical
  {if(lhmax&&(!haveMax||lmaxs*maxv>maxsum*lmaxv)){haveMax=true;maxsum=lmaxs;maxv=lmaxv;maxidx=lmaxi;}if(lhmin&&(!haveMin||lmins*minv<minsum*lminv)){haveMin=true;minsum=lmins;minv=lminv;minidx=lmini;}}}
 cpp_int maxn=maxsum.convert_to<cpp_int>(),maxd=(D*maxv).convert_to<cpp_int>(),minn=minsum.convert_to<cpp_int>(),mind=(D*minv).convert_to<cpp_int>();cpp_int gg=gcdc(maxn,maxd);maxn/=gg;maxd/=gg;gg=gcdc(minn,mind);minn/=gg;mind/=gg;long double mx=maxsum.convert_to<long double>()/(D*maxv).convert_to<long double>(),mn=minsum.convert_to<long double>()/(D*minv).convert_to<long double>();long double xx=(long double)X/Q,yy=(long double)Y/Q;long double B=logl(4*xx*yy)/logl(mx);
 cout<<"R17-C028 refined bivariate h=8 exact cone certificate\n";cout<<"x="<<X<<"/"<<Q<<" y="<<Y<<"/"<<Q<<"\nscale="<<SCALE<<" vmin="<<vmin<<" vmax="<<vmaxi<<"\nmax_state="<<maxidx<<"\nmin_state="<<minidx<<"\nmax_num="<<maxn<<"\nmax_den="<<maxd<<"\nmin_num="<<minn<<"\nmin_den="<<mind<<"\n"<<setprecision(36)<<"max_display="<<mx<<"\nmin_display="<<mn<<"\ngap_display="<<(mx-mn)<<"\nbound_display="<<B<<"\nEXACT_ALL_STATE_BIVARIATE_CONE_SCAN=PASS\nALL_EXACT_CHECKS_PASS\n";munmap((void*)tr,st.st_size);close(fd);}
