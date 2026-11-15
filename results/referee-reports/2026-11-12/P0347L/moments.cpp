// Exact conditional central-moment recursion, evaluated in floating arithmetic.
#include <array>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <sys/resource.h>
#include <vector>
using R = long double;
constexpr int K=6;
using Row=std::array<R,K+1>;
int main(int argc,char**argv){
 const int N=argc>1?std::atoi(argv[1]):8000;
 if(N<2 || N>50000) return 2;
 // Two indices: means/n, central moments/n^k. No quadratic storage.
 const size_t estimate=2*(N+1)*(sizeof(Row)+sizeof(R))+size_t(1<<20);
 std::cerr<<"Planned array+workspace bytes "<<estimate<<"; limit 4000000000\n";
 if(estimate>3500000000ULL) return 3;
 R bin[K+1][K+1]{};
 for(int k=0;k<=K;k++){bin[k][0]=bin[k][k]=1;for(int j=1;j<k;j++)bin[k][j]=bin[k-1][j-1]+bin[k-1][j];}
 std::array<std::vector<Row>,2> m{std::vector<Row>(N+1),std::vector<Row>(N+1)};
 std::array<std::vector<R>,2> mean{std::vector<R>(N+1),std::vector<R>(N+1)};
 for(auto &v:m)v[1][0]=1;
 std::ofstream out("finite_moments.csv");
 out<<"index,n,mean_per_n,m2,m3,m4,m5,m6,t2,t3,t4,t5,t6,mean_B,max_B_error\n"<<std::setprecision(19);
 R h=0, maxmass=0, maxcenter=0;
 const R z=acosl(-1.L)*acosl(-1.L)/6;
 for(int n=2;n<=N;n++){
  h+=1/R(n-1);
  for(int s=0;s<2;s++){
   R avg=0,mass=0;
   for(int i=1;i<=n/2;i++){
    int j=n-i; R x=R(i)/n,y=R(j)/n;
    R q=R(n)/(2*h*i*j)*(i==j?1:2);
    R toll=s==0?1:fabsl(x-y);
    avg+=q*(x*mean[s][i]+y*mean[s][j]+toll); mass+=q;
   }
   mean[s][n]=avg;
   Row sum{}, tollsum{};
   R eb=0,berror=0;
   for(int i=1;i<=n/2;i++){
    int j=n-i; R x=R(i)/n,y=R(j)/n;
    R q=R(n)/(2*h*i*j)*(i==j?1:2);
    R toll=s==0?1:fabsl(x-y);
    R B=toll+x*mean[s][i]+y*mean[s][j]-avg;
    R xp[K+1],yp[K+1],bp[K+1]; xp[0]=yp[0]=bp[0]=1;
    for(int r=1;r<=K;r++){xp[r]=xp[r-1]*x;yp[r]=yp[r-1]*y;bp[r]=bp[r-1]*B;}
    Row zm{};zm[0]=1;
    for(int r=2;r<=K;r++){
     zm[r]=xp[r]*m[s][i][r]+yp[r]*m[s][j][r];
     for(int a=2;a<=r-2;a++)zm[r]+=bin[r][a]*xp[a]*yp[r-a]*m[s][i][a]*m[s][j][r-a];
    }
    for(int k=2;k<=K;k++){
     R t=bp[k];
     for(int r=2;r<k;r++)t+=bin[k][r]*bp[k-r]*zm[r];
     // The r=k cross terms are nonrecursive tolls as well.
     for(int a=2;a<=k-2;a++)t+=bin[k][a]*xp[a]*yp[k-a]*m[s][i][a]*m[s][j][k-a];
     tollsum[k]+=q*t;
     sum[k]+=q*(xp[k]*m[s][i][k]+yp[k]*m[s][j][k]+t);
    }
    eb+=q*B;
    R H=-x*logl(x)-y*logl(y);
    berror=std::max(berror,fabsl(B+logl(R(n))*H/z));
   }
   m[s][n]=sum;m[s][n][0]=1;
   maxmass=std::max(maxmass,fabsl(mass-1));maxcenter=std::max(maxcenter,fabsl(eb));
   out<<(s==0?"S":"C")<<','<<n<<','<<mean[s][n];
   R L=logl(R(n));
   for(int k=2;k<=K;k++)out<<','<<m[s][n][k]/powl(L,k);
   for(int k=2;k<=K;k++)out<<','<<h*tollsum[k]/powl(L,k);
   out<<','<<eb<<','<<berror<<'\n';
  }
  if(n%1000==0)std::cerr<<"n="<<n<<'\n';
 }
 rusage ru{};getrusage(RUSAGE_SELF,&ru);
 std::ofstream audit("finite_audit.json");
 audit<<std::setprecision(19)<<"{\"n\":"<<N<<",\"orders\":6,\"planned_bytes\":"<<estimate<<",\"peak_rss_bytes\":"<<ru.ru_maxrss<<",\"sizeof_long_double\":"<<sizeof(R)<<",\"max_split_mass_error\":"<<maxmass<<",\"max_centering_error_per_n\":"<<maxcenter<<"}\n";
}
