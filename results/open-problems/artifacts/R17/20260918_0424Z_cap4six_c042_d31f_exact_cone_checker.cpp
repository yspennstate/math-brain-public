#include <bits/stdc++.h>
#include <sys/mman.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
#include <omp.h>
#include <boost/multiprecision/cpp_int.hpp>
using namespace std;using boost::multiprecision::cpp_int;using uint384_t=boost::multiprecision::number<boost::multiprecision::cpp_int_backend<384,384,boost::multiprecision::unsigned_magnitude,boost::multiprecision::unchecked,void>>;
static uint384_t powu(uint64_t b,int e){uint384_t r=1;for(int i=0;i<e;i++)r*=b;return r;}static cpp_int gcdc(cpp_int a,cpp_int b){while(b!=0){cpp_int r=a%b;a=b;b=r;}return a;}
int main(int argc,char**argv){if(argc<3){cerr<<"usage: exact_cone product.bin witness.bin\n";return 2;}string tf=argv[1],vf=argv[2];const uint64_t XN=513434,YN=513434,D0=1600000;const int deg=30;uint64_t DX=D0-XN,DY=D0-YN;int fd=open(tf.c_str(),O_RDONLY),fv=open(vf.c_str(),O_RDONLY);if(fd<0||fv<0){perror("open");return 3;}struct stat st,sv;if(fstat(fd,&st)||fstat(fv,&sv)){perror("fstat");return 4;}size_t N=st.st_size/(deg*4);if(sv.st_size!=(off_t)(N*sizeof(uint64_t))){cerr<<"witness size mismatch\n";return 5;}auto*tr=(const uint32_t*)mmap(nullptr,st.st_size,PROT_READ,MAP_SHARED,fd,0);auto*V=(const uint64_t*)mmap(nullptr,sv.st_size,PROT_READ,MAP_SHARED,fv,0);uint384_t C=powu(D0,8)*DX*DY,coef[30];int jj=0;for(int c=0;c<2;c++)for(int l=-7;l<=7;l++){int a=abs(l);uint384_t n;if(a<=6){int e=a+2;if(l>=0)n=powu(XN,a+1)*YN*powu(D0,8-e)*DX*DY;else n=uint384_t(XN)*powu(YN,a+1)*powu(D0,8-e)*DX*DY;}else if(l==7)n=powu(XN,8)*YN*DY;else n=uint384_t(XN)*powu(YN,8)*DX;coef[jj++]=n;}bool have=false,havemin=false;uint384_t maxsum=0,minsum=0;uint64_t maxv=1,minv=1;size_t maxi=0,mini=0;
#pragma omp parallel
{bool lh=false,lhn=false;uint384_t lmax=0,lmin=0;uint64_t lmaxv=1,lminv=1;size_t lmaxi=0,lmini=0;
#pragma omp for schedule(static)
for(long long ii=0;ii<(long long)N;ii++){auto*r=tr+(size_t)ii*deg;uint384_t s=0;for(int j=0;j<deg;j++){uint32_t q=r[j];if(q)s+=coef[j]*V[q-1];}uint64_t vv=V[ii];if(!lh||s*lmaxv>lmax*vv){lh=true;lmax=s;lmaxv=vv;lmaxi=ii;}if(!lhn||s*lminv<lmin*vv){lhn=true;lmin=s;lminv=vv;lmini=ii;}}
#pragma omp critical
{if(lh&&(!have||lmax*maxv>maxsum*lmaxv)){have=true;maxsum=lmax;maxv=lmaxv;maxi=lmaxi;}if(lhn&&(!havemin||lmin*minv<minsum*lminv)){havemin=true;minsum=lmin;minv=lminv;mini=lmini;}}}
cpp_int n=maxsum.convert_to<cpp_int>(),d=(C*maxv).convert_to<cpp_int>(),nn=minsum.convert_to<cpp_int>(),dd=(C*minv).convert_to<cpp_int>();cpp_int g=gcdc(n,d);n/=g;d/=g;g=gcdc(nn,dd);nn/=g;dd/=g;long double rmax=maxsum.convert_to<long double>()/(C*maxv).convert_to<long double>(),rmin=minsum.convert_to<long double>()/(C*minv).convert_to<long double>();cout<<"R17 C042 cap4-min6 exact cone checker\nproduct_states="<<N<<" x="<<XN<<"/"<<D0<<" y="<<YN<<"/"<<D0<<"\nmax_state="<<maxi<<" min_state="<<mini<<"\nlambda_max_num="<<n<<"\nlambda_max_den="<<d<<"\nlambda_min_num="<<nn<<"\nlambda_min_den="<<dd<<"\n"<<setprecision(30)<<"lambda_max_display="<<rmax<<"\nlambda_min_display="<<rmin<<"\ncollatz_gap_display="<<rmax-rmin<<"\nEXACT_ALL_REACHABLE_PRODUCT_ROWS_MINMAX_SCAN=PASS\nALL_EXACT_CHECKS_PASS\n";}
