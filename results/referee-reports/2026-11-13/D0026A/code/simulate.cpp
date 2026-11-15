// Exact continuous-time FA-1f simulation; zero is represented by infected=true.
#include <algorithm>
#include <array>
#include <cassert>
#include <cmath>
#include <cstdint>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <random>
#include <string>
#include <vector>
#include <sys/resource.h>
struct Sim {
 int H,N,L,R,everL,everR; double q,t=0; uint64_t events=0;
 std::mt19937_64 gen; std::vector<unsigned char> inf,seen;
 std::array<std::vector<int>,2> group; std::vector<int> pos,kind;
 double unif(){return std::generate_canonical<double,53>(gen);}
 Sim(int h,double qq,uint64_t seed,int mode):H(h),N(2*h+1),L(2*h+1),R(-1),everL(h),everR(h),q(qq),gen(seed),inf(N),seen(N),pos(N,-1),kind(N,-1){
  for(int i=0;i<N;i++){
   inf[i]=(mode==2 ? unif()<q : (i==H || (mode==1 && unif()<0.04/(1.+std::abs(i-H)/10.))));
   seen[i]=inf[i]; if(inf[i]){L=std::min(L,i);R=std::max(R,i);}
  }
  for(int i=0;i<N;i++) refresh(i);
  grow();
 }
 void refresh(int i){
  if(i<0 || i>=N)return;
  int k=((i>0 && inf[i-1]) || (i+1<N && inf[i+1])) ? int(inf[i]) : -1;
  if(k==kind[i])return;
  if(kind[i]>=0){auto &v=group[kind[i]];int j=pos[i];int last=v.back();v[j]=last;pos[last]=j;v.pop_back();}
  kind[i]=k;pos[i]=-1;
  if(k>=0){pos[i]=int(group[k].size());group[k].push_back(i);}
 }
 void grow(){while(everL>0 && seen[everL-1])--everL;while(everR+1<N && seen[everR+1])++everR;}
 double rate(){return q*group[0].size()+(1-q)*group[1].size();}
 void flip(){
  double r=rate();assert(r>0);
  int k=unif()*r<q*group[0].size()?0:1;
  auto &v=group[k]; std::uniform_int_distribution<int> pick(0,int(v.size())-1);int i=v[pick(gen)];
  inf[i]=!inf[i];++events;
  if(inf[i]){L=std::min(L,i);R=std::max(R,i);seen[i]=1;if(i>=everL-1 && i<=everR+1)grow();}
  else {if(i==L)++L;if(i==R)--R;}
  assert(L<=R);
  refresh(i-1);refresh(i);refresh(i+1);
 }
 void audit(){
  for(int i=0;i<N;i++){
   int k=((i>0 && inf[i-1]) || (i+1<N && inf[i+1]))?int(inf[i]):-1;
   assert(k==kind[i]);if(k>=0)assert(group[k][pos[i]]==i);
  }
  assert(inf[L] && inf[R]);for(int i=0;i<L;i++)assert(!inf[i]);for(int i=R+1;i<N;i++)assert(!inf[i]);
 }
};
int main(int argc,char**argv){
 if(argc<7){std::cerr<<"q replicas horizon halfwidth mode output.csv [seed]\n";return 2;}
 double q=std::stod(argv[1]),T=std::stod(argv[3]);int reps=std::stoi(argv[2]),H=std::stoi(argv[4]),mode=std::stoi(argv[5]);
 uint64_t seed=argc>7?std::stoull(argv[7]):260026;
 int ni=getpriority(PRIO_PROCESS,0);if(ni<10){std::cerr<<"nice must be >=10, got "<<ni<<"\n";return 3;}
 std::vector<double> ts={0};for(double t=.25;t<T;t*=2)ts.push_back(t);ts.push_back(T);
 constexpr int K=8;std::vector<std::array<double,K>> sum(ts.size()),sq(ts.size());
 uint64_t ne=0;int touches=0;
 for(int rep=0;rep<reps;rep++){
  Sim s(H,q,seed+uint64_t(rep)*0x9e3779b97f4a7c15ULL,mode);size_t j=0;
  while(j<ts.size()){
   double rt=s.rate();double next=s.t+(rt>0?-std::log(std::max(s.unif(),1e-300))/rt:INFINITY);
   while(j<ts.size() && ts[j]<next){
    double a=s.inf[H],b=s.inf[H+1];
    std::array<double,K>x={a,a*b,double(!s.inf[H-1]&&!s.inf[H]&&!s.inf[H+1]),double(s.R-H),double(H-s.L),double(s.everR-H),double(H-s.everL),double(s.R-s.L)};
    for(int k=0;k<K;k++){sum[j][k]+=x[k];sq[j][k]+=x[k]*x[k];}++j;
   }
   if(j==ts.size())break;
   s.t=next;s.flip();
   if(rep==0 && s.events%1000==0)s.audit();
  }
  ne+=s.events;touches+=(s.seen[0]||s.seen[s.N-1]);s.audit();
 }
 std::ofstream out(argv[6]);out<<"q,mode,replicas,time";
 const char*names[K]={"infect0","infect01","healthy3","right_front","minus_left_front","ever_right","ever_minus_left","diameter"};
 for(auto n:names)out<<","<<n<<","<<n<<"_se";out<<"\n"<<std::setprecision(10);
 for(size_t j=0;j<ts.size();j++){
  out<<q<<","<<mode<<","<<reps<<","<<ts[j];
  for(int k=0;k<K;k++){double m=sum[j][k]/reps;double se=std::sqrt(std::max(0.,(sq[j][k]-reps*m*m)/(reps-1)/reps));out<<","<<m<<","<<se;}out<<"\n";
 }
 struct rusage usage{}; getrusage(RUSAGE_SELF,&usage);
 std::cout<<"max_rss_bytes="<<usage.ru_maxrss<<" ";
 std::cout<<"q="<<q<<" mode="<<mode<<" reps="<<reps<<" events="<<ne<<" nice="<<ni<<" boundary_ever_seen="<<touches<<"/"<<reps<<"\n";
}
