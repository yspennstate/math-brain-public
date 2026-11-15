#include <algorithm>
#include <cassert>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <vector>
using I=long long;
int main(int argc,char**argv){assert(argc==2);std::ifstream in(argv[1]);int d,C;I A0;in>>d>>C>>A0;assert(in&&3<=d&&d<=35&&1<=C&&C<=256);const I S=I(1)<<40;assert(A0>0&&A0<=S);
 std::vector<I> H(C*C),prev(C*C),cur(C*C);for(auto &x:H){in>>x;assert(in&&x>=-S&&x<=S);}I extra;assert(!(in>>extra));
 std::vector<int> f(C+1),sigma(C+1);for(int n=1;n<=C;n++){int j=n-1,bits=0;while(j){bits+=j&1;j>>=1;}f[n]=f[n-1]+bits;sigma[n]=2*(d-1)*n-2*f[n];assert(sigma[n]>0);}
 auto idx=[&](int b,int c){return(b-1)*C+c-1;};I A=A0,minSlack=9223372036854775807LL;int wx=0,wy=0;unsigned long long states=0;
 for(int a=C;a>=1;a--){for(int b=C;b>=1;b--)for(int c=C;c>=1;c--){
  I ra=a<C?sigma[a]:0,rb=b<C?sigma[b]+std::max(a-b,0):0,rc=c<C?sigma[c]+std::max(b-c,0):0,total=ra+rb+rc+c;assert(total<=100000);
  I ha=a<C?prev[idx(b,c)]:0,hb=b<C?cur[idx(b+1,c)]:0,hc=c<C?cur[idx(b,c+1)]:0;
  I hdrop=H[idx(b,c)],h;
  if(c==1){h=H[idx(a,b)];I need=S+ra*(ha-h)+rb*(hb-h)+rc*(hc-h)+(hdrop-h);if(need>A){A=need;wx=a;wy=b;}}
  else {I num=S+ra*ha+rb*hb+rc*hc+c*(hdrop-A0);h=num>=0?(num+total-1)/total:num/total;I slack=total*h-num;assert(slack>=0&&slack<total);minSlack=std::min(minSlack,slack);}
  assert(h>=-S&&h<=S);cur[idx(b,c)]=h;states++;
 }prev.swap(cur);}
 assert(A<=S&&states==(unsigned long long)C*C*C);
 std::cout<<"{\"status\":\"PASS integer constructive finite bias only, physical extension unaudited\",\"dimension\":"<<d<<",\"cap\":"<<C<<",\"states\":"<<states<<",\"alpha0_units\":"<<A0<<",\"alpha_units\":"<<A<<",\"scale\":"<<S<<",\"minimum_interior_slack\":"<<minSlack<<",\"worst_base\":["<<wx<<","<<wy<<",1]}"<<std::endl;
}
