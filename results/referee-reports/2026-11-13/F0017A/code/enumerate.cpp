// Exact diagonal-completion enumeration, single threaded.
// Compile: clang++ -O3 -std=c++17 code/enumerate.cpp -o code/enumerate
// The field modulus exceeds twice Hadamard's determinant bound for n<=24.
// Consequently centered residues recover the actual integer determinants.
#include <algorithm>
#include <array>
#include <cassert>
#include <chrono>
#include <cmath>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <map>
#include <random>
#include <string>
#include <sys/resource.h>
#include <vector>
using U=uint64_t; using I=int64_t; using W=__uint128_t; using S=__int128_t;
constexpr U P=(U(1)<<61)-1;
inline U add(U a,U b){U s=a+b;return s>=P?s-P:s;}
inline U sub(U a,U b){return a>=b?a-b:a+P-b;}
inline U mul(U a,U b){W z=W(a)*b;U s=U(z&P)+U(z>>61);s=(s&P)+(s>>61);return s>=P?s-P:s;}
U inv(U a){assert(a);U r=1;for(U e=P-2;e;e>>=1,a=mul(a,a))if(e&1)r=mul(r,a);return r;}
I center(U a){return a>P/2?I(a)-I(P):I(a);}
std::string dec(S v){if(!v)return "0";bool neg=v<0;if(neg)v=-v;std::string s;while(v){s+=char('0'+v%10);v/=10;}if(neg)s+='-';std::reverse(s.begin(),s.end());return s;}
using Mat=std::array<U,24*24>;
using IDs=std::array<int,24>;

U det(Mat a,int m){
 U d=1;
 for(int k=0;k<m;k++){
  int j=k;while(j<m&&!a[j*m+k])j++;
  if(j==m)return 0;
  if(j!=k){for(int c=k;c<m;c++)std::swap(a[k*m+c],a[j*m+c]);d=sub(0,d);}
  U p=a[k*m+k];d=mul(d,p);U ip=inv(p);
  for(int r=k+1;r<m;r++){U t=mul(a[r*m+k],ip);for(int c=k+1;c<m;c++)a[r*m+c]=sub(a[r*m+c],mul(t,a[k*m+c]));}
 }
 return d;
}
struct Result{
 int n; U zeros=0,seen=0,fallbacks=0;int max_fallback=0;
 U first_zero=UINT64_MAX,first_nonzero=UINT64_MAX;I first_nonzero_det=0;
 I lo=INT64_MAX,hi=INT64_MIN;S sum=0,parity_sum=0;std::vector<I> values;
 explicit Result(int n_,bool save=false):n(n_){if(save)values.resize(U(1)<<n);}
 void emit(U d,U mask){
  I v=center(d);zeros+=v==0;seen++;lo=std::min(lo,v);hi=std::max(hi,v);sum+=v;
  if(!v&&first_zero==UINT64_MAX)first_zero=mask;
  if(v&&first_nonzero==UINT64_MAX){first_nonzero=mask;first_nonzero_det=v;}
  // A mask bit denotes a +1 diagonal, so the product is (-1)^(n-popcount).
  parity_sum+=((n-__builtin_popcountll(mask))&1)?-S(v):S(v);
  if(!values.empty())values[mask]=v;
 }
};

void walk(const Mat&a,int m,const IDs&ids,U factor,U mask,Result&r){
 if(m<=3){
  for(int bits=0;bits<(1<<m);bits++){
   U d[3],ms=mask;for(int i=0;i<m;i++){bool plus=bits>>i&1;d[i]=add(a[i*m+i],plus?1:P-1);if(plus)ms|=U(1)<<ids[i];}
   U v;
   if(m==0)v=1;
   else if(m==1)v=d[0];
   else if(m==2)v=sub(mul(d[0],d[1]),mul(a[1],a[2]));
   else{
    v=mul(mul(d[0],d[1]),d[2]);
    v=sub(v,mul(mul(a[1],a[3]),d[2]));
    v=sub(v,mul(mul(a[2],a[6]),d[1]));
    v=sub(v,mul(mul(a[5],a[7]),d[0]));
    v=add(v,mul(mul(a[1],a[5]),a[6]));
    v=add(v,mul(mul(a[2],a[3]),a[7]));
   }
   r.emit(mul(factor,v),ms);
  }return;
 }
 for(int plus=0;plus<2;plus++){
  U p=add(a[0],plus?1:P-1),ms=mask|(plus?(U(1)<<ids[0]):0);
  if(p){
   Mat b;IDs js;U ip=inv(p);
   for(int i=1;i<m;i++){
    js[i-1]=ids[i];U t=mul(a[i*m],ip);
    for(int j=1;j<m;j++)b[(i-1)*(m-1)+j-1]=sub(a[i*m+j],mul(t,a[j]));
   }
   walk(b,m-1,js,mul(factor,p),ms,r);
  }else{
   int j=1;while(j<m&&(!a[j]||!a[j*m]))j++;
   if(j<m){
    // An invertible principal 2x2 block handles the zero pivot.
    U u=a[j],v=a[j*m],bd=sub(0,mul(u,v)),q=inv(bd);
    std::array<int,24> keep;IDs js;int k=0;
    for(int i=1;i<m;i++)if(i!=j){keep[k]=i;js[k++]=ids[i];}
    for(int pos=0;pos<2;pos++){
     U w=add(a[j*m+j],pos?1:P-1);Mat b;
     for(int x=0;x<m-2;x++){
      int i=keep[x];U t0=mul(sub(mul(a[i*m],w),mul(a[i*m+j],v)),q);
      U t1=sub(0,mul(mul(a[i*m],u),q));
      for(int y=0;y<m-2;y++){
       int c=keep[y];b[x*(m-2)+y]=sub(a[i*m+c],add(mul(t0,a[c]),mul(t1,a[j*m+c])));
      }
     }
     walk(b,m-2,js,mul(factor,bd),ms|(pos?(U(1)<<ids[j]):0),r);
    }
   }else{
    // Rare degenerate pivot pattern: enumerate the remainder using row pivoting.
    r.fallbacks++;r.max_fallback=std::max(r.max_fallback,m);
    for(U bits=0;bits<(U(1)<<(m-1));bits++){
     Mat b=a;b[0]=0;U mm=ms;
     for(int i=1;i<m;i++){bool pos=bits>>(i-1)&1;b[i*m+i]=add(b[i*m+i],pos?1:P-1);if(pos)mm|=U(1)<<ids[i];}
     r.emit(mul(factor,det(b,m)),mm);
    }
   }
  }
 }
}

Result evaluate(const std::vector<U>&rows,int n,bool values=false){
 assert(n>=1&&n<=24);assert(powl((long double)n,(long double)n/2)<(long double)P/2);
 Mat a{};IDs ids;for(int i=0;i<n;i++){ids[i]=i;for(int j=0;j<n;j++)if(i!=j)a[i*n+j]=(rows[i]>>j&1)?1:P-1;}
 Result r(n,values);walk(a,n,ids,1,0,r);
 if(r.seen!=(U(1)<<n)||r.parity_sum!=(S(1)<<n)||r.sum!=S(center(det(a,n)))*(S(1)<<n)){
  std::cerr<<"determinant/Fourier identity audit failed\n";std::exit(2);
 }
 return r;
}
int pairs(const std::vector<U>&a,int n){
 if(n<3)return 0;int out=0;
 for(int i=0;i<n;i++)for(int j=i+1;j<n;j++){
  U mask=((U(1)<<n)-1)^(U(1)<<i)^(U(1)<<j),x=(a[i]^a[j])&mask;
  out+=(x==0||x==mask);
  int s=0;bool ok=true;for(int k=0;k<n;k++)if(k!=i&&k!=j){int t=((a[k]>>i)^(a[k]>>j))&1;if(!s)s=t?2:1;else if(s!=(t?2:1))ok=false;}out+=ok;
 }return out;
}
void output(const Result&r,const std::vector<U>&a,U index,U seed){
 std::cout<<"{\"n\":"<<r.n<<",\"sample\":"<<index<<",\"seed\":"<<seed<<",\"row_bits\":[";
 for(int i=0;i<r.n;i++)std::cout<<(i?",":"")<<a[i];
 std::cout<<"],\"singular_switchings\":"<<r.zeros<<",\"visited\":"<<r.seen<<",\"min_det\":"<<r.lo<<",\"max_det\":"<<r.hi
 <<",\"sum_det\":\""<<dec(r.sum)<<"\",\"parity_sum\":\""<<dec(r.parity_sum)<<"\",\"pair_events\":"<<pairs(a,r.n)
 <<",\"fallbacks\":"<<r.fallbacks<<",\"max_fallback\":"<<r.max_fallback;
 std::cout<<",\"first_zero_mask\":"<<(r.first_zero==UINT64_MAX?"null":std::to_string(r.first_zero))
 <<",\"first_nonzero_mask\":"<<(r.first_nonzero==UINT64_MAX?"null":std::to_string(r.first_nonzero))
 <<",\"first_nonzero_det\":"<<r.first_nonzero_det;
 if(!r.values.empty()){std::cout<<",\"determinants\":[";for(size_t i=0;i<r.values.size();i++)std::cout<<(i?",":"")<<r.values[i];std::cout<<"]";}
 std::cout<<"}"<<std::endl;
}
int main(int argc,char**argv){
 // The macOS sandbox rejects setrlimit. Matrices are fixed arrays and n<=24;
 // no 2^n table is allocated except the n<=10 validation output.
 if(getpriority(PRIO_PROCESS,0)<10){std::cerr<<"Requires inherited nice >=10\n";return 3;}
 if(argc<3){std::cerr<<"exhaustive n | monte n count seed | values n row_bits...\n";return 1;}
 std::string mode=argv[1];int n=std::stoi(argv[2]);if(n<1||n>24)return 1;
 auto start=std::chrono::steady_clock::now();
 if(mode=="monte"){
  if(argc!=5)return 1;int count=std::stoi(argv[3]);U seed=std::stoull(argv[4]);std::mt19937_64 gen(seed);
  for(int t=0;t<count;t++){std::vector<U>a(n,0);for(int i=0;i<n;i++)for(int j=0;j<n;j++)if(i!=j)a[i]|=(gen()&1)<<j;output(evaluate(a,n),a,t,seed);}
 }else if(mode=="values"||mode=="audit"){
  if((mode=="values"&&n>10)||argc!=n+3)return 1;std::vector<U>a;for(int i=0;i<n;i++)a.push_back(std::stoull(argv[3+i]));output(evaluate(a,n,mode=="values"),a,0,0);
 }else if(mode=="exhaustive"){
  if(n>6)return 1;
  // Fixed spanning tree of K_(n,n) minus the diagonal matching, for n>=3.
  std::vector<std::pair<int,int>>free;std::vector<U>base(n,0);
  for(int i=0;i<n;i++)for(int j=0;j<n;j++)if(i!=j){bool tree=(n==2||i==0||j==0||(i==1&&j==2));if(tree)base[i]|=U(1)<<j;else free.push_back({i,j});}
  U total=U(1)<<free.size();std::map<U,U>hist;U pair_failure=0,other_failure=0;
  for(U bits=0;bits<total;bits++){
   auto a=base;for(size_t k=0;k<free.size();k++)if(bits>>k&1)a[free[k].first]|=U(1)<<free[k].second;
   auto r=evaluate(a,n);hist[r.zeros]++;if(r.zeros){if(pairs(a,n))pair_failure++;else other_failure++;}
  }
  std::cout<<"{\"n\":"<<n<<",\"representatives\":"<<total<<",\"free_offdiagonal_bits\":"<<free.size()<<",\"pair_failures\":"<<pair_failure<<",\"other_failures\":"<<other_failure<<",\"histogram\":{";
  bool first=true;for(auto [z,c]:hist){std::cout<<(first?"":",")<<"\""<<z<<"\":"<<c;first=false;}std::cout<<"}}"<<std::endl;
 }else return 1;
 std::cerr<<"seconds="<<std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count()<<" nice="<<getpriority(PRIO_PROCESS,0)<<"\n";
}
