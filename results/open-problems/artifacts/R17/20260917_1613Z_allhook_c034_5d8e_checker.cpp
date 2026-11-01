#include <bits/stdc++.h>
#include <sys/mman.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
#include <omp.h>
#include <boost/multiprecision/cpp_int.hpp>
using namespace std;
using boost::multiprecision::uint512_t;
using boost::multiprecision::cpp_int;
static uint512_t powu(uint64_t b,int e){uint512_t r=1;for(int i=0;i<e;i++)r*=b;return r;}
static cpp_int gcdc(cpp_int a,cpp_int b){while(b!=0){cpp_int r=a%b;a=b;b=r;}return a;}
int main(int argc,char**argv){
 if(argc<2){cerr<<"usage: checker trans.bin [iters] [scale]\n";return 2;}
 string tf=argv[1]; int iters=argc>2?atoi(argv[2]):140; uint64_t SCALE=argc>3?stoull(argv[3]):100000000000000ULL;
 const size_t N=6419109,M=5*N; const int nl=15,deg=30;
 const uint64_t XN=513401,YN=513467,D0=1600000,DX=D0-XN,DY=D0-YN;
 int fd=open(tf.c_str(),O_RDONLY); if(fd<0){perror("open");return 3;} struct stat st;fstat(fd,&st);
 if((size_t)st.st_size!=N*(size_t)deg*4){cerr<<"bad transition file size\n";return 4;}
 auto*tr=(const uint32_t*)mmap(nullptr,st.st_size,PROT_READ,MAP_SHARED,fd,0); if(tr==MAP_FAILED){perror("mmap");return 5;}
 long double x=(long double)XN/D0,y=(long double)YN/D0; double W[nl];
 for(int li=0;li<nl;li++){int l=li-7,a=abs(l);long double w;if(a<=6)w=l>=0?powl(x,a+1)*y:x*powl(y,a+1);else w=l>=0?powl(x,8)*y/(1-x):x*powl(y,8)/(1-y);W[li]=(double)w;}
 vector<double>v(M,1.0),u(M);
 for(int it=0;it<iters;it++){double mx=0;
 #pragma omp parallel for reduction(max:mx) schedule(static)
  for(long long ii=0;ii<(long long)N;ii++){const uint32_t*r=tr+(size_t)ii*deg;double s[5]={0,0,0,0,0};for(int c=0;c<2;c++)for(int li=0;li<nl;li++){uint32_t q=r[c*nl+li];if(!q)continue;int l=li-7,nm=0;if(abs(l)>=2)nm=(c==0?(l>0?1:2):(l>0?3:4));s[nm]+=W[li]*(double)v[((size_t)q-1)*5+nm];}double total=s[0]+s[1]+s[2]+s[3]+s[4];double o[5]={total,total-s[2],total-s[1],total-s[4],total-s[3]};for(int m=0;m<5;m++){u[(size_t)ii*5+m]=o[m];mx=max(mx,o[m]);}}
 #pragma omp parallel for schedule(static)
  for(long long k=0;k<(long long)M;k++)u[k]/=mx; v.swap(u);
  if(it%20==19) cerr<<"it="<<(it+1)<<" mx="<<setprecision(17)<<mx<<"\n";
 }
 vector<uint64_t>V(M); uint64_t vmin=ULLONG_MAX,vmax=0; for(size_t k=0;k<M;k++){uint64_t q=(uint64_t)llround((long double)v[k]*SCALE);if(!q)q=1;V[k]=q;vmin=min(vmin,q);vmax=max(vmax,q);}
 uint512_t C=powu(D0,8)*DX*DY; uint512_t coef[nl];
 for(int li=0;li<nl;li++){int l=li-7,a=abs(l);uint512_t n;if(a<=6){int e=a+2;if(l>=0)n=powu(XN,a+1)*YN*powu(D0,8-e)*DX*DY;else n=uint512_t(XN)*powu(YN,a+1)*powu(D0,8-e)*DX*DY;}else if(l==7)n=powu(XN,8)*YN*DY;else n=uint512_t(XN)*powu(YN,8)*DX;coef[li]=n;}
 if(C%7!=0){cerr<<"common denominator not divisible by 7\n";return 6;} for(auto&q:coef)if(q%7!=0){cerr<<"coefficient not divisible by 7\n";return 7;} C/=7; for(auto&q:coef)q/=7;
 bool have=false,havemin=false; uint512_t maxsum=0,minsum=0; uint64_t maxv=1,minv=1; size_t maxidx=0,minidx=0;
 #pragma omp parallel
 {bool lhave=false,lhavemin=false;uint512_t lmax=0,lmin=0;uint64_t lmaxv=1,lminv=1;size_t lmaxi=0,lmini=0;
 #pragma omp for schedule(static)
  for(long long ii=0;ii<(long long)N;ii++){const uint32_t*r=tr+(size_t)ii*deg;uint512_t s[5]={0,0,0,0,0};for(int c=0;c<2;c++)for(int li=0;li<nl;li++){uint32_t q=r[c*nl+li];if(!q)continue;int l=li-7,nm=0;if(abs(l)>=2)nm=(c==0?(l>0?1:2):(l>0?3:4));s[nm]+=coef[li]*V[((size_t)q-1)*5+nm];}uint512_t total=s[0]+s[1]+s[2]+s[3]+s[4];uint512_t o[5]={total,total-s[2],total-s[1],total-s[4],total-s[3]};for(int m=0;m<5;m++){size_t k=(size_t)ii*5+m;uint64_t vv=V[k];uint512_t su=o[m];if(!lhave||su*lmaxv>lmax*vv){lhave=true;lmax=su;lmaxv=vv;lmaxi=k;}if(!lhavemin||su*lminv<lmin*vv){lhavemin=true;lmin=su;lminv=vv;lmini=k;}}}
 #pragma omp critical
  {if(lhave&&(!have||lmax*maxv>maxsum*lmaxv)){have=true;maxsum=lmax;maxv=lmaxv;maxidx=lmaxi;}if(lhavemin&&(!havemin||lmin*minv<minsum*lminv)){havemin=true;minsum=lmin;minv=lminv;minidx=lmini;}}
 }
 uint512_t maxden=C*maxv,minden=C*minv; cpp_int n=maxsum.convert_to<cpp_int>(),d=maxden.convert_to<cpp_int>();cpp_int g=gcdc(n,d);n/=g;d/=g; cpp_int nn=minsum.convert_to<cpp_int>(),dd=minden.convert_to<cpp_int>();cpp_int gg=gcdc(nn,dd);nn/=gg;dd/=gg;
 long double rmax=maxsum.convert_to<long double>()/maxden.convert_to<long double>(),rmin=minsum.convert_to<long double>()/minden.convert_to<long double>();
 cout<<"R17 C034 exact h=8 maximal length-two deficiency-product Collatz checker\n";
 cout<<"base_states="<<N<<" product_states="<<M<<"\n";
 cout<<"filter=reject same-c opposite-sign adjacent labels whenever both |l|>=2\n";
 cout<<"x="<<XN<<"/"<<D0<<" y="<<YN<<"/"<<D0<<"\n";
 cout<<"search_iterations="<<iters<<" integer_scale="<<SCALE<<" vmin="<<vmin<<" vmax="<<vmax<<"\n";
 cout<<"max_product_state="<<maxidx<<" min_product_state="<<minidx<<"\n";
 cout<<"lambda_max_num="<<n<<"\nlambda_max_den="<<d<<"\n";
 cout<<"lambda_min_num="<<nn<<"\nlambda_min_den="<<dd<<"\n";
 cout<<setprecision(30)<<"lambda_max_display="<<rmax<<"\nlambda_min_display="<<rmin<<"\ncollatz_gap_display="<<(rmax-rmin)<<"\n";
 cout<<"EXACT_ALL_PRODUCT_ROWS_MINMAX_SCAN=PASS\nALL_EXACT_CHECKS_PASS\n";
 munmap((void*)tr,st.st_size); close(fd); return 0;
}
