#include <algorithm>
#include <chrono>
#include <cmath>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <cassert>
int main(int argc,char**argv){
 assert(argc==4);int d=std::stoi(argv[1]),C=std::stoi(argv[2]);assert(d>=3&&d<=35&&C>=1&&C<=256);
 std::vector<int> f(C+1),s(C+1);for(int n=1;n<=C;n++){int j=n-1,bits=0;while(j){bits+=j&1;j>>=1;}f[n]=f[n-1]+bits;s[n]=2*(d-1)*n-2*f[n];assert(s[n]>0);}
 auto pos=[&](int a,int b,int c){return(size_t(a-1)*C+b-1)*C+c-1;};auto base=[&](int a,int b){return size_t(a-1)*C+b-1;};
 std::vector<double> h(C*C),next(C*C),v(size_t(C)*C*C);double gain=0,change=0;int sweeps=0;
 auto start=std::chrono::steady_clock::now();
 for(int it=0;it<1000;it++){
  for(int a=C;a>=1;a--)for(int b=C;b>=1;b--)for(int c=C;c>=1;c--){
   int ra=a<C?s[a]:0,rb=b<C?s[b]+std::max(a-b,0):0,rc=c<C?s[c]+std::max(b-c,0):0,total=ra+rb+rc+c;
   double z=1+c*h[base(b,c)];if(ra)z+=ra*v[pos(a+1,b,c)];if(rb)z+=rb*v[pos(a,b+1,c)];if(rc)z+=rc*v[pos(a,b,c+1)];v[pos(a,b,c)]=z/total;
  }
  gain=v[pos(C,C,1)];change=0;
  for(int a=1;a<=C;a++)for(int b=1;b<=C;b++){auto k=base(a,b);next[k]=v[pos(a,b,1)]-gain;change=std::max(change,std::abs(next[k]-h[k]));}
  h.swap(next);sweeps=it+1;
  if(change<2e-14)break;
  if(std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count()>50)break;
 }
 const long long scale=1099511627776LL;
 long long alpha0=std::min(scale,(long long)std::ceil(gain*scale)+1024);
 std::ofstream out(argv[3]);assert(out);out.precision(17);out<<"{\"dimension\":"<<d<<",\"cap\":"<<C<<",\"width\":3,\"scale\":"<<scale<<",\"alpha0_units\":"<<alpha0<<",\"gain_estimate\":"<<gain<<",\"last_change\":"<<change<<",\"sweeps\":"<<sweeps<<",\"base_bias\":[";
 bool first=true;for(double z:h){if(!first)out<<",";first=false;out<<(long long)std::llround(z*scale);}out<<"]}\n";
 std::cout<<"Discovery compressed base ONLY, d="<<d<<" C="<<C<<" gain="<<gain<<" sweeps="<<sweeps<<" change="<<change<<std::endl;
}
