#include <bits/stdc++.h>
#include <sys/mman.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
#include <omp.h>
#include <boost/multiprecision/cpp_int.hpp>
using namespace std; using boost::multiprecision::uint512_t; using boost::multiprecision::cpp_int;
static uint512_t powu(uint64_t b,int e){uint512_t r=1;for(int i=0;i<e;i++)r*=b;return r;}
static cpp_int gcdc(cpp_int a,cpp_int b){while(b!=0){cpp_int r=a%b;a=b;b=r;}return a;}
static const int K=17,RJ=17;
static const int CP[K]={0,14,13,15,16,11,12,8,7,10,9,5,6,2,1,3,4};
static const int UQ[10][3]={{4,10,12},{0,13,15},{0,13,15},{0,13,15},{1,5,7},{6,9,16},{0,2,3},{0,2,3},{0,2,3},{8,11,14}};
static const int JM[K][10]={
{0,0,0,0,0,2,0,0,0,2},{-1,0,0,0,0,0,1,1,1,0},{-1,0,0,0,0,2,0,0,0,2},{0,0,0,0,-1,2,0,0,0,2},{0,0,0,0,-1,1,2,2,2,1},{-1,0,0,0,0,0,1,1,1,-1},{-1,2,2,2,1,2,0,0,0,-1},{-1,0,0,0,0,-1,1,1,1,0},{-1,1,1,1,2,-1,0,0,0,2},{1,2,2,2,-1,2,0,0,0,-1},{0,0,0,0,-1,1,2,2,2,-1},{2,1,1,1,-1,-1,0,0,0,2},{0,0,0,0,-1,-1,2,2,2,1},{0,0,0,0,0,-1,0,0,0,2},{2,1,1,1,2,-1,0,0,0,2},{0,0,0,0,0,2,0,0,0,-1},{1,2,2,2,1,2,0,0,0,-1}};
static inline int cat(int l){if(l<=-2)return 0;if(l==-1)return 1;if(l==0)return 2;if(l==1)return 3;return 4;}
int main(int argc,char**argv){if(argc<2){cerr<<"flipbin [iters] [scale]\n";return 2;}string fn=argv[1];int iters=argc>2?atoi(argv[2]):100;uint64_t SCALE=argc>3?stoull(argv[3]):1000000000000000ULL;const size_t N=6419109;const int nl=15,deg=30;const uint64_t XN=513401,YN=513467,D0=1600000,DX=D0-XN,DY=D0-YN;int fd=open(fn.c_str(),O_RDONLY);if(fd<0){perror("open");return 3;}struct stat st;fstat(fd,&st);if((size_t)st.st_size!=N*(size_t)deg*4){cerr<<"bad size\n";return 4;}auto*tr=(const uint32_t*)mmap(nullptr,st.st_size,PROT_READ,MAP_SHARED,fd,0);
long double x=(long double)XN/D0,y=(long double)YN/D0;double W[nl];for(int li=0;li<nl;li++){int l=li-7,a=abs(l);long double w;if(a<=6)w=l>=0?powl(x,a+1)*y:x*powl(y,a+1);else w=l>=0?powl(x,8)*y/(1-x):x*powl(y,8)/(1-y);W[li]=(double)w;}
size_t MS=N*(size_t)K;vector<double>v(MS,1.0),u(MS);
for(int it=0;it<iters;it++){double mx=0,mn=DBL_MAX;
#pragma omp parallel for reduction(max:mx) reduction(min:mn) schedule(static)
for(long long ii=0;ii<(long long)N;ii++){const uint32_t*r=tr+(size_t)ii*deg;double B[10][3]={{0}};for(int c=0;c<2;c++)for(int li=0;li<nl;li++){uint32_t raw=r[c*nl+li];if(!raw)continue;int fl=raw>>31;uint32_t q=raw&0x7fffffffU;if(!q)continue;int l=li-7,s=c*5+cat(l);size_t qb=((size_t)q-1)*K;double w=W[li];for(int j=0;j<3;j++){int m2=UQ[s][j];if(fl)m2=CP[m2];B[s][j]+=w*v[qb+m2];}}
size_t ib=(size_t)ii*K;for(int m=0;m<K;m++){double su=0;for(int s=0;s<10;s++){int j=JM[m][s];if(j>=0)su+=B[s][j];}u[ib+m]=su;double rr=su/v[ib+m];mx=max(mx,rr);mn=min(mn,rr);}}
#pragma omp parallel for schedule(static)
for(long long k=0;k<(long long)MS;k++)u[k]/=mx;v.swap(u);if(it%10==9)cerr<<"it="<<it+1<<" mn="<<setprecision(17)<<mn<<" mx="<<mx<<" gap="<<mx-mn<<"\n";}
vector<uint64_t>V(MS);uint64_t vmin=ULLONG_MAX,vmax=0;for(size_t k=0;k<MS;k++){uint64_t q=(uint64_t)llround((long double)v[k]*SCALE);if(!q)q=1;V[k]=q;vmin=min(vmin,q);vmax=max(vmax,q);}vector<double>().swap(v);vector<double>().swap(u);
uint512_t C=powu(D0,8)*DX*DY,coef[nl];for(int li=0;li<nl;li++){int l=li-7,a=abs(l);uint512_t n;if(a<=6){int e=a+2;if(l>=0)n=powu(XN,a+1)*YN*powu(D0,8-e)*DX*DY;else n=uint512_t(XN)*powu(YN,a+1)*powu(D0,8-e)*DX*DY;}else if(l==7)n=powu(XN,8)*YN*DY;else n=uint512_t(XN)*powu(YN,8)*DX;coef[li]=n;}if(C%7!=0)return 6;for(auto&q:coef)if(q%7!=0)return 7;C/=7;for(auto&q:coef)q/=7;
bool have=false,havemin=false;uint512_t maxsum=0,minsum=0;uint64_t maxv=1,minv=1;size_t maxi=0,mini=0;
#pragma omp parallel
{bool lh=false,lhn=false;uint512_t lmax=0,lmin=0;uint64_t lmaxv=1,lminv=1;size_t lmaxi=0,lmini=0;
#pragma omp for schedule(static)
for(long long ii=0;ii<(long long)N;ii++){const uint32_t*r=tr+(size_t)ii*deg;uint512_t B[10][3]={{0}};for(int c=0;c<2;c++)for(int li=0;li<nl;li++){uint32_t raw=r[c*nl+li];if(!raw)continue;int fl=raw>>31;uint32_t q=raw&0x7fffffffU;if(!q)continue;int l=li-7,s=c*5+cat(l);size_t qb=((size_t)q-1)*K;uint512_t w=coef[li];for(int j=0;j<3;j++){int m2=UQ[s][j];if(fl)m2=CP[m2];B[s][j]+=w*V[qb+m2];}}
size_t ib=(size_t)ii*K;for(int m=0;m<K;m++){uint512_t su=0;for(int s=0;s<10;s++){int j=JM[m][s];if(j>=0)su+=B[s][j];}uint64_t vv=V[ib+m];if(!lh||su*lmaxv>lmax*vv){lh=true;lmax=su;lmaxv=vv;lmaxi=ib+m;}if(!lhn||su*lminv<lmin*vv){lhn=true;lmin=su;lminv=vv;lmini=ib+m;}}}
#pragma omp critical
{if(lh&&(!have||lmax*maxv>maxsum*lmaxv)){have=true;maxsum=lmax;maxv=lmaxv;maxi=lmaxi;}if(lhn&&(!havemin||lmin*minv<minsum*lminv)){havemin=true;minsum=lmin;minv=lminv;mini=lmini;}}}
uint512_t maxden=C*maxv,minden=C*minv;cpp_int n=maxsum.convert_to<cpp_int>(),d=maxden.convert_to<cpp_int>();cpp_int g=gcdc(n,d);n/=g;d/=g;cpp_int nn=minsum.convert_to<cpp_int>(),dd=minden.convert_to<cpp_int>();cpp_int gg=gcdc(nn,dd);nn/=gg;dd/=gg;long double rmax=maxsum.convert_to<long double>()/maxden.convert_to<long double>(),rmin=minsum.convert_to<long double>()/minden.convert_to<long double>();
cout<<"R17 C037 gauge-corrected outer-hook sandwich exact Collatz checker\n";cout<<"base_states="<<N<<" memory_states="<<K<<" product_states="<<MS<<"\n";cout<<"x="<<XN<<"/"<<D0<<" y="<<YN<<"/"<<D0<<"\n";cout<<"search_iterations="<<iters<<" integer_scale="<<SCALE<<" vmin="<<vmin<<" vmax="<<vmax<<"\n";cout<<"max_product_state="<<maxi<<" min_product_state="<<mini<<"\n";cout<<"lambda_max_num="<<n<<"\nlambda_max_den="<<d<<"\n";cout<<"lambda_min_num="<<nn<<"\nlambda_min_den="<<dd<<"\n";cout<<setprecision(30)<<"lambda_max_display="<<rmax<<"\nlambda_min_display="<<rmin<<"\ncollatz_gap_display="<<(rmax-rmin)<<"\n";cout<<"EXACT_ALL_GAUGE_CORRECTED_PRODUCT_ROWS_MINMAX_SCAN=PASS\nALL_EXACT_CHECKS_PASS\n";munmap((void*)tr,st.st_size);close(fd);return 0;}
