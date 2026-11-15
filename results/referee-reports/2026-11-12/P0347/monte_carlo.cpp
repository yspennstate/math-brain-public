// Symmetric tree statistics: K with P(K=k)=1/(H_{m-1} k) gives the
// same unordered split as q(m,k). Two independent samplers are provided.
#include <algorithm>
#include <array>
#include <chrono>
#include <cmath>
#include <cstdint>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <random>
#include <string>
#include <vector>
#include <sys/resource.h>
struct Alias {std::vector<double> p;std::vector<int> a;};
int main(int argc,char**argv){
 if(argc!=6){std::cerr<<"n repetitions seed alias|cdf output.csv\n";return 1;}
 int n=std::stoi(argv[1]),R=std::stoi(argv[2]);uint64_t seed=std::stoull(argv[3]);
 bool use_alias=std::string(argv[4])=="alias";
 if(n>1000000||R<1)return 2;
 std::mt19937_64 rng(seed);
 auto uniform=[&](){return (rng()>>11)*0x1.0p-53;};
 std::vector<double> h(n+1);for(int k=1;k<=n;k++)h[k]=h[k-1]+1./k;
 std::array<Alias,257> table;
 if(use_alias)for(int m=2;m<=256;m++){
  int l=m-1;auto &t=table[m];t.p.resize(l);t.a.resize(l);
  std::vector<int>small,large;
  for(int k=0;k<l;k++){t.p[k]=l/(h[l]*(k+1));(t.p[k]<1?small:large).push_back(k);}
  while(!small.empty()&&!large.empty()){
   int s=small.back();small.pop_back();int b=large.back();large.pop_back();
   t.a[s]=b;t.p[b]-=1-t.p[s];(t.p[b]<1?small:large).push_back(b);
  }
  for(int k:small)t.p[k]=1;for(int k:large)t.p[k]=1;
 }
 auto draw=[&](int m){
  if(!use_alias){double u=uniform()*h[m-1];return int(std::upper_bound(h.begin()+1,h.begin()+m,u)-h.begin());}
  if(m<=256){auto&t=table[m];double u=uniform()*(m-1);int k=int(u);return (u-k<t.p[k]?k:t.a[k])+1;}
  const double log2=std::log(2.);double lm=std::log(double(m));
  while(true){int k=std::min(m-1,int(std::exp(uniform()*lm)));if(uniform()<=log2/(k*std::log1p(1./k)))return k;}
 };
 std::ofstream out(argv[5]);out<<"rep,n,S,C,QC\n";
 std::ofstream lg("LOG.md",std::ios::app);
 auto stamp=[](){auto t=std::time(nullptr);std::tm tm=*std::localtime(&t);char b[64];std::strftime(b,sizeof b,"%Y-%m-%d %H:%M:%S %z",&tm);return std::string(b);};
 std::vector<int> stack;stack.reserve(2048);
 for(int r=0;r<R;r++){
  uint64_t S=0,C=0,Q=0;stack.clear();stack.push_back(n);
  while(!stack.empty()){
   int m=stack.back();stack.pop_back();
   if(m==1)continue;
   if(m==2){S+=2;continue;}
   if(m==3){S+=5;C++;Q++;continue;}
   int i=draw(m),j=m-i;int64_t d=int64_t(m)-2*i;
   S+=m;C+=std::abs(d);Q+=uint64_t(d*d);
   // Put smaller child on top: live stack is O(log n).
   stack.push_back(std::max(i,j));stack.push_back(std::min(i,j));
  }
  out<<r<<','<<n<<','<<S<<','<<C<<','<<Q<<'\n';
  if((r+1)%250==0||r+1==R){
   struct rusage ru;getrusage(RUSAGE_SELF,&ru);if(ru.ru_maxrss>3700000000LL)return 3;
   std::string s=stamp()+" — Monte Carlo n="+std::to_string(n)+", "+std::to_string(r+1)+"/"+std::to_string(R)+", sampler="+argv[4]+", RSS bytes="+std::to_string(ru.ru_maxrss);
   lg<<'\n'<<s<<'\n';lg.flush();std::cout<<s<<std::endl;out.flush();
  }
 }
}
