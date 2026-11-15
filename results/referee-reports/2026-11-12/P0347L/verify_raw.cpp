// Independent uncentered recursion to N; center only after computing raw moments.
#include <array>
#include <cmath>
#include <cstdlib>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <sstream>
#include <string>
#include <sys/resource.h>
#include <vector>
using R=long double;
using Row=std::array<R,7>;
int main(int argc,char**argv){
 int N=argc>1?std::atoi(argv[1]):8000;
 size_t bytes=4*(N+1)*sizeof(Row)+1000000;
 std::cerr<<"Preflight bytes "<<bytes<<'\n';if(bytes>3500000000ULL)return 3;
 R B[7][7]{};for(int k=0;k<=6;k++){B[k][0]=B[k][k]=1;for(int j=1;j<k;j++)B[k][j]=B[k-1][j-1]+B[k-1][j];}
 std::array<std::vector<Row>,2> target{std::vector<Row>(N+1),std::vector<Row>(N+1)};
 std::ifstream in("finite_moments.csv");std::string line;getline(in,line);
 while(getline(in,line)){std::stringstream ss(line);std::string v;getline(ss,v,',');int s=v=="S"?0:1;getline(ss,v,',');int n=std::stoi(v);if(n>N)continue;getline(ss,v,',');target[s][n][1]=std::stold(v);for(int k=2;k<=6;k++){getline(ss,v,',');target[s][n][k]=std::stold(v);}}
 std::array<std::vector<Row>,2> raw{std::vector<Row>(N+1),std::vector<Row>(N+1)};
 for(auto &v:raw)v[1][0]=1;
 std::array<Row,2>worst{};R h=0;
 std::ofstream csv("raw_verification.csv");csv<<"index,n,k,raw_centered,central_recursion,relative_error\n"<<std::setprecision(18);
 for(int n=2;n<=N;n++){
  h+=1/R(n-1);
  for(int s=0;s<2;s++){
   Row sum{};
   for(int i=1;i<n;i++){
    int j=n-i;R x=R(i)/n,y=R(j)/n,q=R(n)/(2*h*i*j),t=s==0?1:fabsl(x-y);
    Row xp{},yp{},tp{},conv{};xp[0]=yp[0]=tp[0]=1;
    for(int k=1;k<=6;k++){xp[k]=xp[k-1]*x;yp[k]=yp[k-1]*y;tp[k]=tp[k-1]*t;}
    for(int k=0;k<=6;k++)for(int a=0;a<=k;a++)conv[k]+=B[k][a]*xp[a]*yp[k-a]*raw[s][i][a]*raw[s][j][k-a];
    for(int k=1;k<=6;k++)for(int r=0;r<=k;r++)sum[k]+=q*B[k][r]*tp[k-r]*conv[r];
   }
   sum[0]=1;raw[s][n]=sum;
   worst[s][1]=std::max(worst[s][1],fabsl(sum[1]-target[s][n][1])/std::max(R(1),fabsl(sum[1])));
   for(int k=2;k<=6;k++){
    // Compensated summation of alternating raw-to-central terms.
    R val=0,comp=0;
    for(int r=0;r<=k;r++){R term=B[k][r]*powl(-sum[1],k-r)*sum[r];R next=val+term;comp+=(fabsl(val)>=fabsl(term))?(val-next)+term:(term-next)+val;val=next;}
    val=(val+comp)/powl(logl(R(n)),k);
    R expected=target[s][n][k],err=fabsl(val-expected)/std::max(R(1e-14L),fabsl(expected));
    if(n>=4)worst[s][k]=std::max(worst[s][k],err);
    if(n==N)csv<<(s==0?'S':'C')<<','<<n<<','<<k<<','<<val<<','<<expected<<','<<err<<'\n';
   }
  }
 }
 rusage ru{};getrusage(RUSAGE_SELF,&ru);
 std::ofstream out("raw_audit.json");out<<std::setprecision(18)<<"{\"n\":"<<N<<",\"planned_bytes\":"<<bytes<<",\"peak_rss_bytes\":"<<ru.ru_maxrss;
 for(int s=0;s<2;s++){out<<",\""<<(s==0?'S':'C')<<"_max_relative_errors\":[";for(int k=1;k<=6;k++)out<<(k==1?"":",")<<worst[s][k];out<<']';}out<<"}\n";
}
