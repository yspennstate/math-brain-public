#include <boost/multiprecision/cpp_int.hpp>
#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <numeric>
#include <iomanip>
using boost::multiprecision::cpp_int;
using namespace std;

cpp_int fact(int n){ cpp_int z=1; for(int i=2;i<=n;i++) z*=i; return z; }
cpp_int binom_int(int n,int k){ if(k<0||k>n) return 0; k=min(k,n-k); cpp_int z=1; for(int i=1;i<=k;i++){ z*=n-k+i; z/=i;} return z; }
cpp_int falling(cpp_int x,int r){ cpp_int z=1; for(int i=0;i<r;i++) z*=x-i; return z; }
cpp_int ipow(cpp_int a,int e){ cpp_int r=1; while(e){ if(e&1) r*=a; a*=a; e>>=1;} return r; }
long long stirling1ll(int n,int k){ vector<vector<long long>> d(n+1,vector<long long>(n+1)); d[0][0]=1; for(int i=1;i<=n;i++) for(int j=1;j<=i;j++) d[i][j]=d[i-1][j-1]-(i-1)*d[i-1][j]; return d[n][k]; }

void comps_rec(int pos,int left,vector<int>&nu,int p,const function<void(const vector<int>&)>&f){
 if(pos==p-1){nu[pos]=left; f(nu); return;} for(int x=0;x<=left;x++){nu[pos]=x; comps_rec(pos+1,left-x,nu,p,f);} }

cpp_int Hmult(const vector<int>&nu,int p){
 vector<cpp_int> dp(p),ndp(p); dp[0]=1;
 for(int j=0;j<p;j++){
   int n=nu[j]; if(n==0) continue;
   fill(ndp.begin(),ndp.end(),cpp_int(0));
   for(int t=0;t<=n;t++){
     cpp_int c=binom_int(n,t); int sh=(j*t)%p;
     for(int r=0;r<p;r++) if(dp[r]!=0) ndp[(r+sh)%p]+=dp[r]*c;
   }
   dp.swap(ndp);
 }
 return dp[0];
}

cpp_int G(int p,int b,int m){
 cpp_int total=0, fb=fact(b); vector<int> nu(p);
 comps_rec(0,b,nu,p,[&](const vector<int>&v){
   cpp_int mult=fb; for(int z:v) mult/=fact(z);
   cpp_int H=Hmult(v,p);
   total += mult*falling(H-1,m);
 });
 return total;
}

cpp_int Sformula(int p,int m){
 cpp_int total=0;
 for(int b=0;b<=m;b++){
   long long s=stirling1ll(m+1,b+1);
   cpp_int term=ipow(cpp_int(p),m-b)*G(p,b,m)-falling(ipow(cpp_int(2),b)-1,m);
   total += cpp_int(s)*term;
 }
 if(total%(p-1)!=0){ cerr<<"div error\n"; exit(2); }
 return total/(p-1);
}

int rankmod(vector<vector<int>> A,int p){
 int nr=A.size(),nc=nr?A[0].size():0,r=0;
 auto inv=[&](int x){ for(int y=1;y<p;y++) if((x*y)%p==1)return y; return 0;};
 for(int c=0;c<nc;c++){
   int piv=-1; for(int i=r;i<nr;i++) if(A[i][c]%p){piv=i;break;} if(piv<0)continue;
   swap(A[r],A[piv]); int iv=inv((A[r][c]%p+p)%p); for(int j=c;j<nc;j++)A[r][j]=(A[r][j]*iv)%p;
   for(int i=0;i<nr;i++) if(i!=r && A[i][c]%p){ int f=A[i][c]%p; for(int j=c;j<nc;j++){A[i][j]=(A[i][j]-f*A[r][j])%p; if(A[i][j]<0)A[i][j]+=p;}}
   r++; if(r==nr)break;
 }
 return r;
}

bool collision_free(const vector<vector<int>>&A){
 int m=A.size(); set<vector<int>> rs,cs;
 for(auto&r:A){ bool nz=false;for(int x:r)nz|=x; if(!nz)return false; rs.insert(r);} if((int)rs.size()<m)return false;
 for(int j=0;j<m;j++){ vector<int> c(m);bool nz=false;for(int i=0;i<m;i++){c[i]=A[i][j];nz|=c[i];}if(!nz)return false;cs.insert(c);}return (int)cs.size()==m;
}

cpp_int Sbrute(int p,int m,long long &good){
 cpp_int S=0; good=0; unsigned long long total=1ULL<<(m*m);
 for(unsigned long long mask=0;mask<total;mask++){
   vector<vector<int>> A(m,vector<int>(m)); for(int i=0;i<m;i++)for(int j=0;j<m;j++)A[i][j]=(mask>>(i*m+j))&1ULL;
   if(!collision_free(A))continue; good++; int d=m-rankmod(A,p); if(d){ cpp_int num=ipow(cpp_int(p),d)-1; S+=num/(p-1); }
 }
 return S;
}

string fracstr(cpp_int num,cpp_int den){ return num.convert_to<string>()+"/"+den.convert_to<string>(); }
long double told(const cpp_int&x){ return x.convert_to<long double>(); }
pair<cpp_int,cpp_int> Rbound(int p,int m){ cpp_int S=Sformula(p,m); int e=m*m-(m+1); if(e>=0)return {S,ipow(cpp_int(2),e)}; return {S*ipow(cpp_int(2),-e),1}; }

int main(){
 cout<<"R03 projective-null incidence exact checker\n";
 cout<<"formula S_p,m partition-Mobius incidence\n";
 for(int m=1;m<=4;m++) for(int p: {3,7}){ long long good; cpp_int sb=Sbrute(p,m,good),sf=Sformula(p,m); if(sb!=sf){cerr<<"FAIL brute "<<m<<" "<<p<<"\n";return 3;} cout<<"brute-formula m="<<m<<" p="<<p<<" good="<<good<<" S="<<sf<<" PASS\n"; }
 cpp_int prior_num("4039481031913758122055"), prior_den("9223372036854775808");
 vector<int> ps10={2,3,5,7,11,13}; map<int,pair<cpp_int,cpp_int>> v10;
 cout<<"n=10 prime table\n";
 for(int p:ps10){auto f=Rbound(p,9);v10[p]=f;cout<<"p="<<p<<" S="<<Sformula(p,9)<<" r="<<fracstr(f.first,f.second)<<" decimal="<<setprecision(18)<<(told(f.first)/told(f.second))<<"\n";}
 auto r7=v10[7]; if(r7.first*prior_den>=prior_num*r7.second){cerr<<"FAIL improve\n";return 4;}
 cout<<"best-tested-n10 p=7 r="<<fracstr(r7.first,r7.second)<<" PASS\n";
 cpp_int imp_num=prior_num*r7.second-r7.first*prior_den, imp_den=prior_den*r7.second;
 cout<<"strict-improvement decimal="<<setprecision(18)<<(told(imp_num)/told(imp_den))<<"\n";
 cout<<"n=11 prime comparison\n"; map<int,pair<cpp_int,cpp_int>>v11; for(int p:{7,11,13}){auto f=Rbound(p,10);v11[p]=f;cout<<"p="<<p<<" S="<<Sformula(p,10)<<" r="<<fracstr(f.first,f.second)<<" decimal="<<setprecision(18)<<(told(f.first)/told(f.second))<<"\n";}
 auto lt=[](auto a,auto b){return a.first*b.second<b.first*a.second;}; if(!lt(v11[11],v11[7])||!lt(v11[11],v11[13])){cerr<<"FAIL p11\n";return 5;} cout<<"p7-not-universally-optimal PASS\n";
 cout<<"SELF-CHECK PASS\n"; return 0;
}
