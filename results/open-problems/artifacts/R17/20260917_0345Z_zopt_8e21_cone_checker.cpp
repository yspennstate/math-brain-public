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
static inline uint32_t pack4(uint8_t x,uint8_t y,uint8_t dx,uint8_t dy){return (uint32_t)x|((uint32_t)y<<8)|((uint32_t)dx<<16)|((uint32_t)dy<<24);} 
static inline void unpack4(uint32_t s,uint8_t &x,uint8_t &y,uint8_t &dx,uint8_t &dy){x=s&255;y=(s>>8)&255;dx=(s>>16)&255;dy=(s>>24)&255;}
struct TC{
 int h; uint8_t mask; TC(int hh):h(hh),mask((1u<<hh)-1){}
 inline uint32_t reduce(uint32_t s)const{uint8_t x,y,dx,dy;unpack4(s,x,y,dx,dy);if(x&(1u<<(h-1))){x^=mask;y^=mask;}return pack4(x,y,dx,dy);} 
 uint32_t trans(uint32_t s,int c,int l)const{
  uint8_t x,y,dx,dy;unpack4(s,x,y,dx,dy);int ta=l>=0?l+1:1,tb=l<0?-l+1:1,na=h+ta,nb=h+tb;int16_t L[17][17];L[h][h]=h;int cur=h;
  for(int k=h-1;k>=0;--k){cur-=(dx>>(h-1-k))&1;L[k][h]=cur;}cur=h;for(int k=h-1;k>=0;--k){cur-=(dy>>(h-1-k))&1;L[h][k]=cur;}
  auto ac=[&](int i){if(i<=h)return int((x>>(h-i))&1);int q=i-h-1;if(l>=0)return q<l?1-c:c;return c;};
  auto bc=[&](int j){if(j<=h)return int((y>>(h-j))&1);int q=j-h-1;if(l<0)return q<(-l)?1-c:c;return c;};
  for(int i=0;i<=na;i++)for(int j=0;j<=nb;j++)if(i>h||j>h){if(i==0)L[i][j]=L[i][j-1];else if(j==0)L[i][j]=L[i-1][j];else if(ac(i)==bc(j))L[i][j]=L[i-1][j-1]+1;else L[i][j]=max(L[i][j-1],L[i-1][j]);}
  int i=na,j=nb;while(i>=h&&j>=h){if(L[i][j]==L[i-1][j])--i;else if(L[i][j]==L[i][j-1])--j;else{--i;--j;}if(i==h&&j==h){uint8_t xs=x,ys=y;if(l>=0){for(int q=0;q<l;q++)xs=((xs<<1)|(1-c))&mask;xs=((xs<<1)|c)&mask;ys=((ys<<1)|c)&mask;}else{xs=((xs<<1)|c)&mask;for(int q=0;q<-l;q++)ys=((ys<<1)|(1-c))&mask;ys=((ys<<1)|c)&mask;}uint8_t ndx=0,ndy=0;for(int k=na-h+1;k<=na;k++)ndx=(ndx<<1)|(L[k][nb]-L[k-1][nb]);for(int k=nb-h+1;k<=nb;k++)ndy=(ndy<<1)|(L[na][k]-L[na][k-1]);return reduce(pack4(xs,ys,ndx,ndy));}}
  return UINT32_MAX;
 }
};
uint512_t powu(uint64_t b,int e){uint512_t r=1;for(int i=0;i<e;i++)r*=b;return r;}
cpp_int gcdc(cpp_int a,cpp_int b){while(b!=0){cpp_int r=a%b;a=b;b=r;}return a;}
int main(int argc,char**argv){
 if(argc<2){cerr<<"usage: prog transfile [num den iter scale]\n";return 2;} string tf=argv[1]; uint64_t ZN=argc>2?stoull(argv[2]):320899, ZD=argc>3?stoull(argv[3]):1000000; int niter=argc>4?stoi(argv[4]):280; uint64_t SCALE=argc>5?stoull(argv[5]):1000000000000000ULL;
 const int h=8,deg=30; const size_t PUBN=6419109; TC tc(h); uint8_t mask=(1u<<h)-1; uint32_t start=tc.reduce(pack4(0,0,mask,mask));
 bool exists=false; struct stat st0;if(stat(tf.c_str(),&st0)==0 && (size_t)st0.st_size==PUBN*(size_t)deg*4)exists=true;
 if(!exists){cerr<<"enumerating transitions...\n";unordered_map<uint32_t,uint32_t> idx;idx.reserve(7000000);idx.max_load_factor(.75);vector<uint32_t>states;states.reserve(7000000);states.push_back(start);idx[start]=1;FILE*fp=fopen(tf.c_str(),"wb");if(!fp){perror("fopen");return 3;}size_t head=0;while(head<states.size()){uint32_t s=states[head++];for(int c=0;c<2;c++)for(int l=-7;l<=7;l++){uint32_t t=tc.trans(s,c,l),ti=0;if(t!=UINT32_MAX){auto it=idx.find(t);if(it==idx.end()){ti=(uint32_t)states.size()+1;idx.emplace(t,ti);states.push_back(t);}else ti=it->second;}fwrite(&ti,4,1,fp);}if((head&262143)==0)cerr<<"head="<<head<<" states="<<states.size()<<"\n";}fclose(fp);cerr<<"states="<<states.size()<<"\n";if(states.size()!=PUBN){cerr<<"bad state count\n";return 4;}}
 int fd=open(tf.c_str(),O_RDONLY);struct stat st;fstat(fd,&st);auto*tr=(const uint32_t*)mmap(nullptr,st.st_size,PROT_READ,MAP_SHARED,fd,0);if(tr==MAP_FAILED)return 5; const size_t N=PUBN;
 long double z=(long double)ZN/(long double)ZD;vector<double>w(deg);int jj=0;for(int c=0;c<2;c++)for(int l=-7;l<=7;l++){int a=abs(l);w[jj++]=(a<7)?powl(z,a+2):powl(z,9)/(1-z);} vector<double>v(N,1.0),av(N);double mn=0,mx=0;
 for(int it=0;it<niter;it++){
  mn=DBL_MAX; mx=-DBL_MAX; double vmax=0;
  #pragma omp parallel for reduction(min:mn) reduction(max:mx,vmax) schedule(static)
  for(long long ii=0;ii<(long long)N;ii++){
   const uint32_t*row=tr+(size_t)ii*deg; double ss=0;
   for(int j=0;j<deg;j++){uint32_t q=row[j];if(q)ss+=w[j]*v[q-1];}
   av[ii]=ss; double r=ss/v[ii]; if(r<mn)mn=r; if(r>mx)mx=r; if(ss>vmax)vmax=ss;
  }
  #pragma omp parallel for schedule(static)
  for(long long ii=0;ii<(long long)N;ii++) av[ii]/=vmax;
  v.swap(av);
  if((it+1)%40==0) cerr<<"it="<<it+1<<" min="<<setprecision(17)<<mn<<" max="<<mx<<"\n";
 }
 vector<uint64_t>V(N);uint64_t vmin=ULLONG_MAX,vmax=0;for(size_t i=0;i<N;i++){uint64_t q=(uint64_t)floor((long double)v[i]*(long double)SCALE+0.5L);if(!q)q=1;V[i]=q;vmin=min(vmin,q);vmax=max(vmax,q);} uint64_t oneMinus=ZD-ZN;uint512_t D=uint512_t(oneMinus)*powu(ZD,8), coeff[8];for(int a=0;a<=6;a++){int e=a+2;coeff[a]=uint512_t(oneMinus)*powu(ZN,e)*powu(ZD,8-e);}coeff[7]=powu(ZN,9);
 bool have=false;uint512_t maxsum=0;uint64_t maxv=1;size_t maxidx=0;
 #pragma omp parallel
 {bool lhave=false;uint512_t lsum=0;uint64_t lv=1;size_t li=0;
 #pragma omp for schedule(static)
  for(long long ii=0;ii<(long long)N;ii++){uint512_t sum=0;const uint32_t*row=tr+(size_t)ii*deg;int j=0;for(int c=0;c<2;c++)for(int l=-7;l<=7;l++,j++){uint32_t q=row[j];if(q)sum+=coeff[abs(l)]*V[q-1];}if(!lhave||sum*lv>lsum*V[ii]){lhave=true;lsum=sum;lv=V[ii];li=ii;}}
 #pragma omp critical
  {if(lhave&&(!have||lsum*maxv>maxsum*lv)){have=true;maxsum=lsum;maxv=lv;maxidx=li;}}
 }
 uint512_t den=D*maxv;if(!(maxsum<den)){cerr<<"lambda >=1\n";return 6;}cpp_int n=maxsum.convert_to<cpp_int>(),d=den.convert_to<cpp_int>();cpp_int g=gcdc(n,d);n/=g;d/=g;
 long double lam=maxsum.convert_to<long double>()/den.convert_to<long double>(); long double bound=2*logl(2*z)/logl(lam);
 cout<<"states="<<N<<"\n";cout<<"z="<<ZN<<"/"<<ZD<<"\n";cout<<"iterations="<<niter<<" scale="<<SCALE<<" vmin="<<vmin<<" vmax="<<vmax<<"\n";cout<<"search_min="<<setprecision(18)<<mn<<" search_max="<<mx<<"\n";cout<<"worst_state="<<maxidx<<"\n";cout<<"lambda_num="<<n<<"\n";cout<<"lambda_den="<<d<<"\n";cout<<setprecision(24)<<"lambda_display="<<lam<<"\ncontinuous_bound_display="<<bound<<"\n";cout<<"EXACT_ALL_STATE_CONE_SCAN=PASS\n";cout<<"ALL_EXACT_CHECKS_PASS\n";munmap((void*)tr,st.st_size);close(fd);}
