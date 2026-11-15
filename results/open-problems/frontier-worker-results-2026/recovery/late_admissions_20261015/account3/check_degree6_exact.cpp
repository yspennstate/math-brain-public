#define NOMINMAX
#include <windows.h>
#include <intrin.h>
#include <algorithm>
#include <array>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <map>
#include <numeric>
#include <stdexcept>
#include <string>
#include <vector>
using U=unsigned long long;
using Tri=std::array<int,3>;
void need(bool b,const char* s){if(!b)throw std::runtime_error(s);}
struct Wide{
 U lo=0,hi=0;
 void add(U a,U b,U c){
  U ph,pl=_umul128(a,b,&ph),carry;
  U ql=_umul128(pl,c,&carry),qh;
  need(ph==0||c<=~U(0)/ph,"mul overflow");
  qh=ph*c;need(qh<=~U(0)-carry,"high overflow");qh+=carry;
  unsigned char cy=_addcarry_u64(0,lo,ql,&lo);
  need(!_addcarry_u64(cy,hi,qh,&hi),"add overflow");
 }
 U div(U d)const{need(hi<d,"quotient overflow");U rem;return _udiv128(hi,lo,d,&rem);}
};
struct Term{uint16_t index;uint32_t coeff;};
struct Engine{
 int N,A,B;U S,D;std::vector<Tri> ks;std::vector<int> lookup;
 std::vector<size_t> starts;std::vector<Term> terms;std::vector<std::vector<Term>> edges;
 Engine(int n,int a,int b,int bits):N(n),A(a),B(b),S(U(1)<<bits),D(108ULL*n*n){
  need(n>0&&n%3==0&&n<=96&&a>=0&&a<=b&&b>0&&bits<=40,"parameters");
  lookup.assign((N+1)*(N+1)*(N+1),-1);
  for(int x=0;x<=N/3;x++)for(int y=x;y<=(N-x)/2;y++){
   Tri k{x,y,N-x-y};lookup[key(k)]=(int)ks.size();ks.push_back(k);
  }
 }
 int key(Tri k)const{return (k[0]*(N+1)+k[1])*(N+1)+k[2];}
 int id(Tri k)const{std::sort(k.begin(),k.end());int i=lookup[key(k)];need(i>=0,"unknown vertex");return i;}
 std::map<int,U> split(Tri nums,int den,U multiplier)const{
  Tri low{},rem{};int total=0;for(int i=0;i<3;i++){low[i]=nums[i]/den;rem[i]=nums[i]%den;total+=rem[i];}
  need(total%den==0,"noninteger fractional sum");std::map<int,U> out;
  int s=total/den;
  if(s==0)out[id(low)]+=multiplier*den;
  else if(s==1){for(int i=0;i<3;i++)if(rem[i]){auto k=low;k[i]++;out[id(k)]+=multiplier*rem[i];}}
  else if(s==2){for(int i=0;i<3;i++)if(rem[i]!=den){auto k=low;for(int j=0;j<3;j++)if(j!=i)k[j]++;out[id(k)]+=multiplier*(den-rem[i]);}}
  else need(false,"fractional sum range");return out;
 }
 void build(const std::string& prefix,bool dump){
  std::ofstream f;if(dump)f.open(prefix+".rows.txt");
  starts.push_back(0);size_t zeros=0;
  for(size_t i=0;i<ks.size();i++){
   for(size_t j=0;j<ks.size();j++){
    Tri h=ks[j];int v=0;do{v++;}while(std::next_permutation(h.begin(),h.end()));
    h=ks[j];std::map<int,U> row;
    do{
     int t=0;Tri nums{};for(int c=0;c<3;c++){t+=ks[i][c]*h[c];nums[c]=N*ks[i][c]*h[c];}
     if(!t){zeros++;continue;}
     for(auto [dest,coef]:split(nums,t,324/v))row[dest]+=coef;
    }while(std::next_permutation(h.begin(),h.end()));
    U sum=0;for(auto [dest,coef]:row){sum+=coef;need(coef<=UINT32_MAX,"coefficient overflow");terms.push_back({(uint16_t)dest,(uint32_t)coef});}
    need(sum==D,"fusion row normalization");starts.push_back(terms.size());
    if(dump){f<<i<<' '<<j;for(auto [dest,coef]:row)f<<' '<<dest<<':'<<coef;f<<'\n';}
   }
   if(i%100==0)std::cout<<"{\"phase\":\"build\",\"row\":"<<i<<"}"<<std::endl;
  }
  std::ofstream ef;if(dump)ef.open(prefix+".edges.txt");
  for(size_t i=0;i<ks.size();i++){
   Tri nums;for(int c=0;c<3;c++)nums[c]=(B-A)*N+3*A*ks[i][c];
   auto r=split(nums,3*B,1);std::vector<Term> row;U sum=0;
   if(dump)ef<<i;
   for(auto [d,c]:r){need(c<=UINT32_MAX,"edge coefficient overflow");row.push_back({(uint16_t)d,(uint32_t)c});sum+=c;if(dump)ef<<' '<<d<<':'<<c;}
   need(sum==3ULL*B,"edge normalization");edges.push_back(row);if(dump)ef<<'\n';
  }
  std::cout<<"{\"phase\":\"built\",\"orbits\":"<<ks.size()<<",\"rows\":"<<ks.size()*ks.size()<<",\"terms\":"<<terms.size()<<",\"null_orientations\":"<<zeros<<"}"<<std::endl;
 }
 std::vector<U> round(const std::vector<Wide>& raw,U den,U& loss){
  std::vector<U> out(ks.size());U total=0;
  for(size_t i=0;i<out.size();i++){out[i]=raw[i].div(den);need(out[i]<=S&&total<=S-out[i],"rounded mass exceeds one");total+=out[i];}
  loss=S-total;out[0]+=loss;return out;
 }
 std::vector<U> edge(const std::vector<U>& m,U& loss){
  std::vector<Wide> raw(ks.size());for(size_t i=0;i<m.size();i++)if(m[i])for(auto t:edges[i])raw[t.index].add(m[i],1,t.coeff);
  return round(raw,3ULL*B,loss);
 }
 std::vector<U> fuse(const std::vector<U>& a,const std::vector<U>& b,U& loss){
  std::vector<Wide> raw(ks.size());size_t n=ks.size();
  for(size_t i=0;i<n;i++)if(a[i])for(size_t j=0;j<n;j++)if(b[j]){
   size_t row=i*n+j;for(size_t z=starts[row];z<starts[row+1];z++){auto t=terms[z];raw[t.index].add(a[i],b[j],t.coeff);}
  }
  return round(raw,S*D,loss);
 }
 void run(const std::string& prefix,int depth,int degree){
  std::vector<U> m(ks.size());m[0]=S;std::ofstream masses(prefix+".masses.txt"),meta(prefix+".stages.txt");
  for(int t=0;t<=depth;t++){
   masses<<t;for(auto x:m)masses<<' '<<x;masses<<'\n';masses.flush();
   Wide signal;for(size_t i=0;i<m.size();i++){auto k=ks[i];U v=3ULL*(k[0]*k[0]+k[1]*k[1]+k[2]*k[2])-N*N;signal.add(m[i],v,1);}
   need(signal.hi==0,"signal unexpectedly wide");
   std::cout<<"{\"phase\":\"depth\",\"depth\":"<<t<<",\"signal_numerator\":"<<signal.lo<<",\"signal_denominator\":"<<S*3*N*N<<"}"<<std::endl;
   if(t==depth)break;
   U loss;auto e=edge(m,loss);meta<<t+1<<" edge "<<loss<<'\n';
   std::vector<U> acc;auto power=e;int remaining=degree;
   while(remaining){if(remaining&1){if(acc.empty())acc=power;else{acc=fuse(acc,power,loss);meta<<t+1<<" combine "<<loss<<'\n';}}remaining>>=1;if(remaining){power=fuse(power,power,loss);meta<<t+1<<" square "<<loss<<'\n';}}
   m=acc;meta.flush();
  }
 }
};
int main(int argc,char** argv){try{
 SetPriorityClass(GetCurrentProcess(),BELOW_NORMAL_PRIORITY_CLASS);
 need(argc==9,"N A B bits depth degree prefix dump");
 Engine e(std::stoi(argv[1]),std::stoi(argv[2]),std::stoi(argv[3]),std::stoi(argv[4]));
 e.build(argv[7],std::stoi(argv[8])!=0);e.run(argv[7],std::stoi(argv[5]),std::stoi(argv[6]));
 std::cout<<"{\"complete\":true}"<<std::endl;return 0;
 }catch(const std::exception& e){std::cerr<<e.what()<<std::endl;return 1;}}
