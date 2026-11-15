// Exact degree-six coefficients, computed by polarization without a dense polynomial.
#include <algorithm>
#include <array>
#include <cassert>
#include <chrono>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <unistd.h>
using I=__int128_t;
using L=int64_t;
std::string dec(I x) {
  if(x==0) return "0";
  bool neg=x<0; if(neg) x=-x;
  std::string s;
  while(x) {s.push_back('0'+x%10);x/=10;}
  if(neg) s.push_back('-');
  std::reverse(s.begin(),s.end());return s;
}
int main(int argc,char**argv) {
  alarm(270);
  auto start=std::chrono::steady_clock::now();
  assert(argc==2);std::ifstream in(argv[1]);
  int n,r,cone;in>>n>>r>>cone;assert(in && n>=5 && r>0);
  std::vector<std::vector<L>> v(r,std::vector<L>(n));
  L K=0; for(auto &a:v) for(auto &x:a) {in>>x;K=std::max(K,std::abs(x));}
  // n<=13 and K<=100 imply every intermediate is far below signed 128 bits.
  // The input generator saves an explicit bound using unbounded integers too.
  assert(n<=13 && K<=100 && r<=50);
  auto i2=[&](int a,int b){return a*r+b;};
  auto i3=[&](int a,int b,int c){return (a*r+b)*r+c;};
  auto i4=[&](int a,int b,int c,int d){return ((a*r+b)*r+c)*r+d;};
  std::vector<L> D2(r*r),D3(r*r*r),D4(r*r*r*r),M(r*r);
  int u=cone==1?0:n-1,w=cone==1?1:n-2;
  for(int a=0;a<r;a++) for(int b=0;b<r;b++) {
    for(int j=0;j<n;j++) D2[i2(a,b)]+=v[a][j]*v[b][j];
    M[i2(a,b)]=v[a][u]*v[b][w]+v[b][u]*v[a][w];
  }
  for(int a=0;a<r;a++) for(int b=a;b<r;b++) for(int c=b;c<r;c++) {
    for(int j=0;j<n;j++) D3[i3(a,b,c)]+=v[a][j]*v[b][j]*v[c][j];
    for(int d=c;d<r;d++) for(int j=0;j<n;j++) D4[i4(a,b,c,d)]+=v[a][j]*v[b][j]*v[c][j]*v[d][j];
  }
  struct Pair {int a,b;std::array<int,4> rest;};
  std::vector<Pair> pp;
  for(int a=0;a<6;a++) for(int b=a+1;b<6;b++) {
    Pair p;p.a=a;p.b=b;int k=0;for(int j=0;j<6;j++) if(j!=a&&j!=b)p.rest[k++]=j;pp.push_back(p);
  }
  std::vector<std::array<int,6>> triples;
  for(int b=1;b<6;b++) for(int c=b+1;c<6;c++) {
    std::array<int,6> t={0,b,c,0,0,0};int k=3;for(int j=1;j<6;j++)if(j!=b&&j!=c)t[k++]=j;triples.push_back(t);
  }
  long long total=0,neg=0,zero=0;I sum=0,minval=0,maxval=0;bool first=true;
  const int factorial[]={1,1,2,6,24,120,720};
  std::ofstream dump;if(n<=7)dump.open(std::string(argv[1])+".coefficients");
  for(int a=0;a<r;a++) for(int b=a;b<r;b++) for(int c=b;c<r;c++)
  for(int d=c;d<r;d++) for(int e=d;e<r;e++) for(int f=e;f<r;f++) {
    std::array<int,6> z={a,b,c,d,e,f};
    I qt=0,ttt=0,ttm=0,qm=0,p2=0;
    for(const auto &p:pp) {
      int a0=z[p.a],b0=z[p.b],c0=z[p.rest[0]],d0=z[p.rest[1]],e0=z[p.rest[2]],f0=z[p.rest[3]];
      L pair=D2[i2(a0,b0)], m=M[i2(a0,b0)], q=D4[i4(c0,d0,e0,f0)];
      I t2=I(D2[i2(c0,d0)])*D2[i2(e0,f0)]+I(D2[i2(c0,e0)])*D2[i2(d0,f0)]+I(D2[i2(c0,f0)])*D2[i2(d0,e0)];
      qt+=I(q)*pair;ttt+=I(pair)*t2;ttm+=I(m)*t2;qm+=I(m)*q;
    }
    for(const auto &t:triples) p2+=I(D3[i3(z[t[0]],z[t[1]],z[t[2]])])*D3[i3(z[t[3]],z[t[4]],z[t[5]])];
    I numerator=(n-4)*(96*qt-16*ttt)-144*(n-3)*p2+8*(n-1)*(n*n-6*n+6)*ttm+48*n*(n-1)*qm;
    int denom=1,run=1;for(int k=1;k<=6;k++) {if(k<6&&z[k]==z[k-1])run++;else{denom*=factorial[run];run=1;}}
    assert(numerator%denom==0);I value=numerator/denom;
    if(dump && value!=0) {
      dump<<dec(value)<<" ";for(int j=0;j<r;j++){if(j)dump<<",";dump<<std::count(z.begin(),z.end(),j);}dump<<"\n";
    }
    total++;sum+=value;
    if(value<0) {neg++; if(neg<=3)std::cerr<<"negative coefficient "<<dec(value)<<"\n";}
    if(value==0)zero++;
    else {if(first||value<minval)minval=value;if(first||value>maxval)maxval=value;first=false;}
  }
  std::vector<I> x(n);for(int j=0;j<n;j++) for(int a=0;a<r;a++)x[j]+=v[a][j];
  I T=0,P=0,Q=0;for(I a:x){T+=a*a;P+=a*a*a;Q+=a*a*a*a;}
  I direct=(n-4)*(2*Q-T*T)*T-2*(n-3)*P*P+(n-1)*((n*n-6*n+6)*T*T+2*n*Q)*x[u]*x[w];
  assert(sum==direct);
  auto seconds=std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count();
  std::ostringstream out;
  out<<"{\"n\":"<<n<<",\"cone\":"<<cone<<",\"rays\":"<<r<<",\"monomials\":"<<total<<",\"negative\":"<<neg<<",\"zero\":"<<zero<<",\"min_nonzero\":\""<<dec(minval)<<"\",\"max\":\""<<dec(maxval)<<"\",\"sum_coefficients\":\""<<dec(sum)<<"\",\"sum_check\":true,\"seconds\":"<<seconds<<"}\n";
  std::cout<<out.str();std::ofstream(std::string(argv[1])+".json")<<out.str();
  std::ofstream log("LOG.md",std::ios::app);log<<"\nStep 7 exact extension: "<<out.str();
}
