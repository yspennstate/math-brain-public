// R17 exact checker for the 240-step h=8 Perron witness refinement.
// Search floating point is non-proof; all finite inequalities below are exact.
#include <bits/stdc++.h>
#include <sys/mman.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
#include <boost/multiprecision/cpp_int.hpp>
using namespace std;
using boost::multiprecision::uint256_t;
using boost::multiprecision::cpp_int;
uint256_t powu(uint64_t b,int e){uint256_t r=1;for(int i=0;i<e;i++)r*=b;return r;}
cpp_int ipow(cpp_int b,unsigned long long e){cpp_int r=1;while(e){if(e&1)r*=b;e>>=1;if(e)b*=b;}return r;}
cpp_int gcd_cpp(cpp_int a,cpp_int b){while(b!=0){cpp_int r=a%b;a=b;b=r;}return a;}
int main(int argc,char**argv){
 if(argc<3){cerr<<"usage: exact_checker transition.bin search_vector_double.bin\n";return 2;}
 string tf=argv[1],df=argv[2]; const size_t N=6419109; const int deg=30;
 vector<double> v(N); FILE*f=fopen(df.c_str(),"rb"); if(!f||fread(v.data(),sizeof(double),N,f)!=N){cerr<<"bad search vector\n";return 3;} fclose(f);
 const uint64_t SCALE=1000000000000000ULL;
 vector<uint64_t> V(N); uint64_t vmin=ULLONG_MAX,vmax=0;
 for(size_t i=0;i<N;i++){uint64_t q=(uint64_t)floor((long double)v[i]*(long double)SCALE+0.5L);if(q==0)q=1;V[i]=q;vmin=min(vmin,q);vmax=max(vmax,q);}
 int fd=open(tf.c_str(),O_RDONLY); if(fd<0){perror("transition");return 4;} struct stat st;fstat(fd,&st); if((size_t)st.st_size!=N*(size_t)deg*4){cerr<<"transition size mismatch\n";return 5;} auto*tr=(const uint32_t*)mmap(nullptr,st.st_size,PROT_READ,MAP_SHARED,fd,0);if(tr==MAP_FAILED)return 6;
 // z=3209/10000. Common denominator for Lueker h=8 weights.
 uint256_t D=uint256_t(6791)*powu(10000,8), coeff[8];
 for(int a=0;a<=6;a++){int e=a+2;coeff[a]=uint256_t(6791)*powu(3209,e)*powu(10000,8-e);} coeff[7]=powu(3209,9);
 bool have=false;uint256_t maxsum=0;uint64_t maxv=1;size_t maxidx=0;
 for(size_t i=0;i<N;i++){
   uint256_t sum=0;const uint32_t*row=tr+i*deg;int j=0;
   for(int c=0;c<2;c++)for(int l=-7;l<=7;l++,j++){uint32_t q=row[j];if(q)sum+=coeff[abs(l)]*V[q-1];}
   if(!have||sum*maxv>maxsum*V[i]){have=true;maxsum=sum;maxv=V[i];maxidx=i;}
 }
 uint256_t maxden=D*maxv; if(!(maxsum<maxden)){cerr<<"lambda>=1\n";return 7;}
 cpp_int n=maxsum.convert_to<cpp_int>(),d=maxden.convert_to<cpp_int>();cpp_int g=gcd_cpp(n,d);n/=g;d/=g;
 const cpp_int expect_n("1205756908493739750118272911119587569742420049311");
 const cpp_int expect_d("3527335053202052628125000000000000000000000000000");
 if(n!=expect_n||d!=expect_d){cerr<<"lambda fraction mismatch\n";return 8;}
 // Exact endpoint: U*=2 log(3209/5000)/log(lambda) < p/q iff
 // (3209/5000)^(2q) > lambda^p because both logarithms are negative.
 const unsigned long long p=287817,q=348329;
 cpp_int lhs=ipow(cpp_int(3209),2*q)*ipow(d,p);
 cpp_int rhs=ipow(cpp_int(5000),2*q)*ipow(n,p);
 if(!(lhs>rhs)){cerr<<"endpoint power comparison FAIL\n";return 9;}
 // Exact arithmetic for the public rational endpoint and width.
 if((__int128)34945*348329-(__int128)287817*42292 != 341){cerr<<"upper decrease numerator FAIL\n";return 10;}
 if((unsigned long long)((__int128)42292*348329)!=14731530068ULL){cerr<<"upper decrease denominator FAIL\n";return 11;}
 // L=0.792665992=99083249/125000000.
 __int128 wn=(__int128)287817*125000000-(__int128)99083249*348329;
 __int128 wd=(__int128)348329*125000000;
 unsigned long long wn64=(unsigned long long)wn,wd64=(unsigned long long)wd;auto gg=std::gcd(wn64,wd64);wn64/=gg;wd64/=gg;
 if(wn64!=1463555959079ULL||wd64!=43541125000000ULL){cerr<<"width FAIL\n";return 12;}
 cout<<"R17-C020 exact h=8 witness refinement\n";
 cout<<"states="<<N<<"\n";
 cout<<"integer_scale="<<SCALE<<" vmin="<<vmin<<" vmax="<<vmax<<"\n";
 cout<<"worst_state_zero_based="<<maxidx<<"\n";
 cout<<"lambda_num="<<n<<"\n";
 cout<<"lambda_den="<<d<<"\n";
 cout<<"EXACT_ALL_STATE_CONE_SCAN=PASS\n";
 cout<<"EXACT_ENDPOINT_POWER_COMPARISON=PASS\n";
 cout<<"CERTIFIED_NEW_UPPER=287817/348329\n";
 cout<<"PREVIOUS_UPPER=34945/42292\n";
 cout<<"UPPER_DECREASE=341/14731530068\n";
 cout<<"CERTIFIED_NEW_WIDTH=1463555959079/43541125000000\n";
 cout<<"ALL_EXACT_CHECKS_PASS\n";
 munmap((void*)tr,st.st_size);close(fd);return 0;
}
