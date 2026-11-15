// Independent exhaustive algorithm for n<=6: permutation expansion and Walsh transform.
// No finite fields, inverses, Gaussian elimination, or recursive Schur complements.
#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <numeric>
#include <sys/resource.h>
#include <vector>
using U=uint64_t;
struct Term{U negative_entries;int fixed,sign;};
int main(int argc,char**argv){
 if(argc!=2||getpriority(PRIO_PROCESS,0)<10)return 1;
 int n=std::stoi(argv[1]);if(n<1||n>6)return 1;
 std::vector<int>p(n);std::iota(p.begin(),p.end(),0);std::vector<Term>terms;
 do{
  Term t{0,0,1};int inversions=0;
  for(int i=0;i<n;i++){
   if(i==p[i])t.fixed|=1<<i;else t.negative_entries|=U(1)<<(i*n+p[i]);
   for(int j=i+1;j<n;j++)inversions+=p[i]>p[j];
  }
  if(inversions&1)t.sign=-1;terms.push_back(t);
 }while(std::next_permutation(p.begin(),p.end()));
 std::vector<int>free;
 for(int i=0;i<n;i++)for(int j=0;j<n;j++)if(i!=j&&!(n==2||i==0||j==0||(i==1&&j==2)))free.push_back(i*n+j);
 U total=U(1)<<free.size();std::map<int,U>hist;std::vector<int>a(1<<n);
 for(U b=0;b<total;b++){
  U neg=0;for(size_t j=0;j<free.size();j++)if(!(b>>j&1))neg|=U(1)<<free[j];
  std::fill(a.begin(),a.end(),0);
  for(const auto&t:terms)a[t.fixed]+=t.sign*((__builtin_popcountll(neg&t.negative_entries)&1)?-1:1);
  for(int step=1;step<(1<<n);step<<=1)for(int base=0;base<(1<<n);base+=2*step)for(int k=0;k<step;k++){
   int x=a[base+k],y=a[base+k+step];a[base+k]=x+y;a[base+k+step]=x-y;
  }
  int z=std::count(a.begin(),a.end(),0);hist[z]++;
 }
 std::cout<<"{\"n\":"<<n<<",\"representatives\":"<<total<<",\"histogram\":{";bool first=true;
 for(auto[z,c]:hist){std::cout<<(first?"":",")<<"\""<<z<<"\":"<<c;first=false;}
 std::cout<<"}}\n";
}
