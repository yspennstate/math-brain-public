// Independent finite conditional-central-moment recursion. No author code used.
#include <array>
#include <algorithm>
#include <cmath>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <vector>
using Row = std::array<double,7>;
int choose[7][7];
int main(int argc,char**argv){
  int N=argc>1?std::stoi(argv[1]):4000;
  for(int k=0;k<=6;k++){choose[k][0]=choose[k][k]=1;for(int a=1;a<k;a++)choose[k][a]=choose[k-1][a-1]+choose[k-1][a];}
  std::ofstream out("referee_finite.csv"), diag("referee_diagnostics.csv"), cats("referee_categories.csv");
  out<<std::setprecision(17)<<"index,n,mean_over_n,m2,m3,m4,m5,m6\n";
  diag<<std::setprecision(17)<<"index,n,prob_error,centering_over_n,max_toll_remainder,endpoint_remainder,root_abs_B_over_n\n";
  cats<<std::setprecision(17)<<"index,n,k,linear_canceled,linear_uncanceled,c0,c1_cross,cge2,toll_direct,toll_from_defect,linear_entropy_only,linear_remainder,leading_cge2\n";
  for(int kind=0;kind<3;kind++){
    const char* name=kind==0?"S":kind==1?"C":"D";
    std::vector<Row> m(N+1);std::vector<double> mean(N+1);
    m[1][0]=1.;double h=0.;
    for(int n=2;n<=N;n++){
      h+=1./(n-1);double L=std::log(n), ps=0.,mu=0.;
      for(int i=1;i<n;i++){
        int j=n-i;double x=double(i)/n,y=double(j)/n,q=double(n)/(2*h*i*j);
        double t=kind==0?1.:kind==1?std::abs(1.-2*x):2*std::min(x,y);
        ps+=q;mu+=q*(x*mean[i]+y*mean[j]+t);
      }
      mean[n]=mu;m[n][0]=1.;Row sums{};double ctr=0.,absB=0.,maxerr=0.,enderr=0.;
      for(int i=1;i<n;i++){
        int j=n-i;double x=double(i)/n,y=double(j)/n,q=double(n)/(2*h*i*j);
        double t=kind==0?1.:kind==1?std::abs(1.-2*x):2*std::min(x,y);
        double B=t+x*mean[i]+y*mean[j]-mu;
        double g=(x*std::log(x)+y*std::log(y))/(std::acos(-1.)*std::acos(-1.)/6);
        ctr+=q*B;absB+=q*std::abs(B);maxerr=std::max(maxerr,std::abs(B-(kind==2?0.:L*g)));
        if(i==1)enderr=B-(kind==2?0.:L*g);
        Row left{},right{},bp{},daughter{};left[0]=right[0]=bp[0]=1.;double xp=1.,yp=1.;
        for(int k=1;k<=6;k++){xp*=x;yp*=y;left[k]=xp*m[i][k];right[k]=yp*m[j][k];bp[k]=bp[k-1]*B;}
        for(int k=0;k<=6;k++)for(int a=0;a<=k;a++)daughter[k]+=choose[k][a]*left[a]*right[k-a];
        for(int k=2;k<=6;k++)for(int d=0;d<=k;d++)sums[k]+=q*choose[k][d]*daughter[d]*bp[k-d];
      }
      for(int k=2;k<=6;k++)m[n][k]=sums[k];
      if(n<=20 || n==100 || n==500 || n%1000==0 || n==N){
        out<<name<<','<<n<<','<<mu;for(int k=2;k<=6;k++)out<<','<<m[n][k]/std::pow(L,k);out<<'\n';
        diag<<name<<','<<n<<','<<ps-1<<','<<ctr<<','<<maxerr<<','<<enderr<<','<<absB<<'\n';
      }
      if(n%1000==0 || n==N){
        for(int k=2;k<=6;k++){
          double lin=0.,unc=0.,zero=0.,one=0.,many=0.,def=0.,ent=0.,rem=0.,lead=0.;
          for(int i=1;i<n;i++){
            int j=n-i;double x=double(i)/n,y=double(j)/n,q=double(n)/(2*h*i*j);
            double t=kind==0?1.:kind==1?std::abs(1.-2*x):2*std::min(x,y),B=t+x*mean[i]+y*mean[j]-mu;
            double g=(x*std::log(x)+y*std::log(y))/(std::acos(-1.)*std::acos(-1.)/6);
            int r=k-1;double daughters=std::pow(x,r)*m[i][r]+std::pow(y,r)*m[j][r];
            lin+=q*k*B*(daughters-m[n][r]);unc+=q*k*B*daughters;
            ent+=q*k*L*g*daughters;rem+=q*k*(B-L*g)*daughters;
            def+=q*(std::pow(x,k)*m[i][k]+std::pow(y,k)*m[j][k]);
            for(int a=0;a<k;a++)for(int b=0;b<k;b++){
              int c=k-a-b;if(c<0 || (c==1 && (a==0||b==0)))continue;
              double fac=choose[k][a]*choose[k-a][b],base=q*fac*std::pow(x,a)*m[i][a]*std::pow(y,b)*m[j][b];
              double v=base*std::pow(B,c);
              if(c==0)zero+=v;else if(c==1)one+=v;else{many+=v;lead+=base*std::pow(L*g,c);}
            }
          }
          double scale=h/std::pow(L,k);
          cats<<name<<','<<n<<','<<k;for(double v:{lin,unc,zero,one,many,lin+zero+one+many,m[n][k]-def,ent,rem,lead})cats<<','<<v*scale;cats<<'\n';
        }
        std::cerr<<name<<" n="<<n<<" completed\n";
      }
    }
  }
}
