#include <boost/multiprecision/cpp_int.hpp>
#include <array>
#include <iostream>
using boost::multiprecision::cpp_int;
using namespace std;
static unsigned long long cnt[13];
static int px[13],py[13],pz[13];
static const int dx[6]={1,-1,0,0,0,0};
static const int dy[6]={0,0,1,-1,0,0};
static const int dz[6]={0,0,0,0,1,-1};
inline bool used(int x,int y,int z,int depth){
 for(int i=0;i<=depth;i++) if(px[i]==x&&py[i]==y&&pz[i]==z) return true;
 return false;
}
void dfs(int depth){
 if(depth>0) ++cnt[depth];
 if(depth==12) return;
 int x=px[depth],y=py[depth],z=pz[depth];
 for(int k=0;k<6;k++){
   int a=x+dx[k],b=y+dy[k],c=z+dz[k];
   if(!used(a,b,c,depth)){px[depth+1]=a;py[depth+1]=b;pz[depth+1]=c;dfs(depth+1);}
 }
}
cpp_int ipow(cpp_int a,int n){cpp_int r=1; while(n--){r*=a;} return r;}
int main(){
 px[0]=py[0]=pz[0]=0; dfs(0);
 unsigned long long expected[13]={0,6,30,150,726,3534,16926,81390,387966,1853886,8809878,41934150,198842742};
 for(int n=1;n<=12;n++){cout<<"c_"<<n<<"="<<cnt[n]<<"\n"; if(cnt[n]!=expected[n]){cerr<<"count mismatch\n";return 2;}}
 cpp_int num=203449919, den=1000000000;
 cpp_int lhs=cpp_int(cnt[12])*ipow(num,12);
 cpp_int rhs=ipow(den,12);
 cout<<"pstar=203449919/1000000000\n";
 cout<<"certificate c12*pstar^12 < 1: "<<(lhs<rhs?"TRUE":"FALSE")<<"\n";
 if(!(lhs<rhs)) return 3;
 cout<<"lhs="<<lhs<<"\n";
 cout<<"rhs="<<rhs<<"\n";
 cout<<"PASS\n";
}
