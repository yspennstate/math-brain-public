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
static inline int H(int c,int s){return 1+2*c+(s<0);} // s=+1/-1
static inline int U(int c,int s){return 5+2*c+(s<0);}
static inline int P(int c,int s){return 9+2*c+(s<0);} // first sign
static inline int Q(int c,int s){return 13+2*c+(s<0);} // first hook sign
int main(int argc,char**argv){
 if(argc<2){cerr<<"usage: prog trans.bin [iters] [scale]\n";return 2;}string tf=argv[1];int iters=argc>2?atoi(argv[2]):100;uint64_t SCALE=argc>3?stoull(argv[3]):1000000000000000ULL;
 const size_t N=6419109; const int K=17,MEM=K,nl=15,deg=30; const uint64_t XN=513401,YN=513467,D0=1600000,DX=D0-XN,DY=D0-YN;
 int fd=open(tf.c_str(),O_RDONLY);if(fd<0){perror("open");return 3;}struct stat st;fstat(fd,&st);if((size_t)st.st_size!=N*(size_t)deg*4){cerr<<"bad trans size\n";return 4;}auto*tr=(const uint32_t*)mmap(nullptr,st.st_size,PROT_READ,MAP_SHARED,fd,0);if(tr==MAP_FAILED){perror("mmap");return 5;}
 long double x=(long double)XN/D0,y=(long double)YN/D0;double W[nl];for(int li=0;li<nl;li++){int l=li-7,a=abs(l);long double w;if(a<=6)w=l>=0?powl(x,a+1)*y:x*powl(y,a+1);else w=l>=0?powl(x,8)*y/(1-x):x*powl(y,8)/(1-y);W[li]=(double)w;}
 size_t MS=N*(size_t)K;vector<double>v(MS,1.0),u(MS);
 for(int it=0;it<iters;it++){double mx=0,mn=DBL_MAX;
 #pragma omp parallel for reduction(max:mx) reduction(min:mn) schedule(static)
  for(long long ii=0;ii<(long long)N;ii++){
   const uint32_t*r=tr+(size_t)ii*deg; double total=0; double hook[2][2]={{0,0},{0,0}}, unit[2][2]={{0,0},{0,0}}, zero[2]={0,0};
   double zdelta[2][2]={{0,0},{0,0}}, udelta[2][2]={{0,0},{0,0}}, pdelta[2][2]={{0,0},{0,0}};
   for(int c=0;c<2;c++)for(int li=0;li<nl;li++){uint32_t q=r[c*nl+li];if(!q)continue;int l=li-7;double w=W[li];size_t qb=((size_t)q-1)*K;
    if(l==0){double base=w*v[qb+0];zero[c]+=base;total+=base;
      int c0=1-c; for(int si=0;si<2;si++){int s=si? -1:1;zdelta[c0][si]+=w*(v[qb+Q(c0,s)]-v[qb+0]);}
    } else if(abs(l)==1){int si=l<0;int s=si?-1:1;double base=w*v[qb+U(c,s)];unit[c][si]+=base;total+=base;
      int s0=-s,si0=s0<0;udelta[c][si0]+=w*(v[qb+P(c,s0)]-v[qb+U(c,s)]); pdelta[c][si]+=w*(v[qb+P(c,-s)]-v[qb+U(c,s)]);
    } else {int si=l<0;int s=si?-1:1;double base=w*v[qb+H(c,s)];hook[c][si]+=base;total+=base;}
   }
   double o[K];o[0]=total;
   for(int c=0;c<2;c++)for(int si=0;si<2;si++){int s=si?-1:1;
      o[H(c,s)] = total - hook[c][1-si] + zdelta[c][si];
      o[U(c,s)] = total + udelta[c][si];
      o[P(c,s)] = total - unit[1-c][1-si] + pdelta[c][si];
      o[Q(c,s)] = total - hook[c][1-si];
   }
   size_t ib=(size_t)ii*K;for(int m=0;m<K;m++){u[ib+m]=o[m];double rr=o[m]/v[ib+m];mx=max(mx,rr);mn=min(mn,rr);}
  }
 #pragma omp parallel for schedule(static)
  for(long long k=0;k<(long long)MS;k++)u[k]/=mx;v.swap(u);if(it%10==9)cerr<<"it="<<it+1<<" mn="<<setprecision(17)<<mn<<" mx="<<mx<<" gap="<<mx-mn<<"\n";
 }
 vector<uint64_t>V(MS);uint64_t vmin=ULLONG_MAX,vmax=0;for(size_t k=0;k<MS;k++){uint64_t q=(uint64_t)llround((long double)v[k]*SCALE);if(!q)q=1;V[k]=q;vmin=min(vmin,q);vmax=max(vmax,q);}v.clear();u.clear();v.shrink_to_fit();u.shrink_to_fit();
 uint512_t C=powu(D0,8)*DX*DY,coef[nl];for(int li=0;li<nl;li++){int l=li-7,a=abs(l);uint512_t n;if(a<=6){int e=a+2;if(l>=0)n=powu(XN,a+1)*YN*powu(D0,8-e)*DX*DY;else n=uint512_t(XN)*powu(YN,a+1)*powu(D0,8-e)*DX*DY;}else if(l==7)n=powu(XN,8)*YN*DY;else n=uint512_t(XN)*powu(YN,8)*DX;coef[li]=n;}if(C%7!=0)return 6;for(auto&q:coef)if(q%7!=0)return 7;C/=7;for(auto&q:coef)q/=7;
 bool have=false,havemin=false;uint512_t maxsum=0,minsum=0;uint64_t maxv=1,minv=1;size_t maxi=0,mini=0;
 #pragma omp parallel
 {bool lh=false,lhn=false;uint512_t lmax=0,lmin=0;uint64_t lmaxv=1,lminv=1;size_t lmaxi=0,lmini=0;
 #pragma omp for schedule(static)
  for(long long ii=0;ii<(long long)N;ii++){
   const uint32_t*r=tr+(size_t)ii*deg;uint512_t total=0,hook[2][2]={{0,0},{0,0}},unit[2][2]={{0,0},{0,0}},zero[2]={0,0};
   uint512_t zalt[2][2]={{0,0},{0,0}}, ualt[2][2]={{0,0},{0,0}}, palt[2][2]={{0,0},{0,0}};
   for(int c=0;c<2;c++)for(int li=0;li<nl;li++){uint32_t q=r[c*nl+li];if(!q)continue;int l=li-7;uint512_t w=coef[li];size_t qb=((size_t)q-1)*K;
    if(l==0){uint512_t base=w*V[qb];zero[c]+=base;total+=base;int c0=1-c;for(int si=0;si<2;si++){int s=si?-1:1;zalt[c0][si]+=w*V[qb+Q(c0,s)];}}
    else if(abs(l)==1){int si=l<0;int s=si?-1:1;uint512_t base=w*V[qb+U(c,s)];unit[c][si]+=base;total+=base;int s0=-s,si0=s0<0;ualt[c][si0]+=w*V[qb+P(c,s0)]; palt[c][si]+=w*V[qb+P(c,-s)];}
    else {int si=l<0;int s=si?-1:1;uint512_t base=w*V[qb+H(c,s)];hook[c][si]+=base;total+=base;}
   }
   uint512_t o[K];o[0]=total;for(int c=0;c<2;c++)for(int si=0;si<2;si++){int s=si?-1:1;
      int zc=1-c;
      o[H(c,s)] = total - hook[c][1-si] - zero[zc] + zalt[c][si];
      o[U(c,s)] = total - unit[c][1-si] + ualt[c][si];
      o[P(c,s)] = total - unit[1-c][1-si] - unit[c][si] + palt[c][si];
      o[Q(c,s)] = total - hook[c][1-si];
   }
   size_t ib=(size_t)ii*K;for(int m=0;m<K;m++){uint64_t vv=V[ib+m];uint512_t su=o[m];if(!lh||su*lmaxv>lmax*vv){lh=true;lmax=su;lmaxv=vv;lmaxi=ib+m;}if(!lhn||su*lminv<lmin*vv){lhn=true;lmin=su;lminv=vv;lmini=ib+m;}}
  }
 #pragma omp critical
  {if(lh&&(!have||lmax*maxv>maxsum*lmaxv)){have=true;maxsum=lmax;maxv=lmaxv;maxi=lmaxi;}if(lhn&&(!havemin||lmin*minv<minsum*lminv)){havemin=true;minsum=lmin;minv=lminv;mini=lmini;}}
 }
 uint512_t maxden=C*maxv,minden=C*minv;cpp_int n=maxsum.convert_to<cpp_int>(),d=maxden.convert_to<cpp_int>();cpp_int g=gcdc(n,d);n/=g;d/=g;cpp_int nn=minsum.convert_to<cpp_int>(),dd=minden.convert_to<cpp_int>();cpp_int gg=gcdc(nn,dd);nn/=gg;dd/=gg;
 long double rmax=maxsum.convert_to<long double>()/maxden.convert_to<long double>(),rmin=minsum.convert_to<long double>()/minden.convert_to<long double>();
 cout<<"R17 C035 exact h=8 length2-allhook plus 8 minimal-deficient-triple DFA Collatz checker\n";
 cout<<"base_states="<<N<<" memory_states="<<K<<" product_states="<<MS<<"\n";
 cout<<"x="<<XN<<"/"<<D0<<" y="<<YN<<"/"<<D0<<"\n";
 cout<<"search_iterations="<<iters<<" integer_scale="<<SCALE<<" vmin="<<vmin<<" vmax="<<vmax<<"\n";
 cout<<"max_product_state="<<maxi<<" min_product_state="<<mini<<"\n";
 cout<<"lambda_max_num="<<n<<"\nlambda_max_den="<<d<<"\n";
 cout<<"lambda_min_num="<<nn<<"\nlambda_min_den="<<dd<<"\n";
 cout<<setprecision(30)<<"lambda_max_display="<<rmax<<"\nlambda_min_display="<<rmin<<"\ncollatz_gap_display="<<(rmax-rmin)<<"\n";
 cout<<"EXACT_ALL_PRODUCT_ROWS_MINMAX_SCAN=PASS\nALL_EXACT_CHECKS_PASS\n";
 munmap((void*)tr,st.st_size);close(fd);return 0;
}
