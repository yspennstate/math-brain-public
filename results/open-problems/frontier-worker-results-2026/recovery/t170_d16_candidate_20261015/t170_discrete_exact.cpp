// A count-state Bellman upper bound, with exact rates and upward-rounded dyadic time values.
#include <algorithm>
#include <chrono>
#include <cstdio>
#include <cstring>
#include <array>
#include <cstdint>
#include <cstdlib>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <limits>
#include <stdexcept>
#include <sstream>
#include <vector>
using U = std::uint64_t;
static U SCALE;
static const auto DEADLINE=std::chrono::steady_clock::now()+std::chrono::seconds(500);
static int DIM;
static int MINIMUM_RATES = 0;
static std::vector<int> ISO;
static std::uint64_t CHECKSUM = 1469598103934665603ULL;
static std::uint64_t REPAIRS = 0, STATES = 0;
static U plus(U a,U b) { if (b>std::numeric_limits<U>::max()-a) throw std::overflow_error("add"); return a+b; }
static U times(U a,U b) { if (a && b>std::numeric_limits<U>::max()/a) throw std::overflow_error("multiply"); return a*b; }
struct Table {
    std::vector<int> dims, strides;
    std::vector<U> data;
    Table() {}
    explicit Table(std::vector<int> d): dims(d), strides(d.size(),1) {
        int size=1;
        for(int k=(int)d.size()-1;k>=0;--k) { strides[k]=size; size*=d[k]+1; }
        data.assign(size,0);
    }
    int index(const std::vector<int>& p) const {
        int v=0; for(int k=0;k<(int)p.size();++k) { if(p[k]>dims[k]) throw std::runtime_error("boundary out of range"); v+=p[k]*strides[k]; } return v;
    }
};
static U bellman(const std::vector<int>& counts,const std::vector<U>& child) {
    U denominator=counts.back(), numerator=SCALE;
    for(int k=0;k<(int)counts.size();++k) {
        const int prev=k?counts[k-1]:0;
        const U rate=ISO[counts[k]]+(k?std::max(prev-counts[k],0):0);
        if(rate>2*(DIM-1)*counts[k]+prev) throw std::runtime_error("rate interval");
        denominator=plus(denominator,rate);numerator=plus(numerator,times(rate,child[k]));
    }
    if(!denominator) throw std::runtime_error("zero denominator"); ++STATES;
    const U answer=numerator/denominator+(numerator%denominator!=0);
    return answer;
}
static Table stage(const std::vector<int>& box,const std::vector<int>& keep,const Table& prev,U gamma) {
    const int n=(int)box.size();
    std::vector<int> tail(box.begin()+1,box.end());
    Table layer(tail), output(keep);
    struct Point {std::vector<int> p; bool valid,border; U initial;};
    std::vector<Point> points;
    points.reserve(layer.data.size());
    for(int index=0;index<(int)layer.data.size();++index) {
        std::vector<int> p(tail.size()); int rem=index; bool zero=false,valid=true,border=false;
        for(int k=0;k<(int)tail.size();++k) {
            p[k]=rem/layer.strides[k]; rem%=layer.strides[k];
            if(p[k]==0) zero=true; else if(zero) valid=false;
            if(p[k]==tail[k]) border=true;
        }
        bool allzero=std::all_of(p.begin(),p.end(),[](int v){return v==0;});
        U initial=0;
        if(valid) initial=allzero?gamma:std::min(gamma,prev.data[prev.index(p)]);
        points.push_back({p,valid,border,initial}); layer.data[index]=initial;
    }
    auto save=[&](int i) {
        if(i>keep[0]) return;
        for(int index=0;index<(int)points.size();++index) {
            if(!points[index].valid) continue;
            auto p=points[index].p; bool inside=true;
            for(int k=0;k<(int)p.size();++k) if(p[k]>keep[k+1]) inside=false;
            if(inside) { p.insert(p.begin(),i); output.data[output.index(p)]=layer.data[index]; }
        }
    };
    save(box[0]);
    for(int i=box[0]-1;i>=1;--i) {
        if(std::chrono::steady_clock::now()>DEADLINE) throw std::runtime_error("500 second foreground guard; completed slab caches retained");
        for(int index=(int)points.size()-1;index>=0;--index) {
            const Point& point=points[index];
            if(!point.valid) continue;
            if(point.border) { layer.data[index]=prev.data[prev.index(point.p)]; continue; }
            std::vector<int> counts=point.p; counts.insert(counts.begin(),i);
            std::vector<U> child(n,0); child[0]=layer.data[index];
            for(int k=1;k<n;++k) {
                const int rate=ISO[counts[k]]+std::max(counts[k-1]-counts[k],0);
                if(rate) child[k]=layer.data[index+layer.strides[k-1]];
            }
            layer.data[index]=bellman(counts,child);
        }
        save(i);
    }
    std::vector<int> origin(n,0); origin[0]=1;
    const U value=output.data[output.index(origin)];
    std::cout << "{\"d\":"<<DIM<<",\"level\":"<<n<<",\"scale\":"<<SCALE<<",\"raw_upper_units\":"<<value
              <<",\"normalized_upper\":"<<std::setprecision(17)<<(double)value/(double)SCALE/n
              <<",\"states_so_far\":"<<STATES<<",\"rate_endpoint_changes\":"<<REPAIRS<<",\"checksum\":"<<CHECKSUM<<"}\n"<<std::flush;
    return output;
}

int main(int argc,char**argv) {
 try {
  if(argc!=2) throw std::runtime_error("usage: own-discrete-screen input");
  std::ifstream in(argv[1]);int last,maximum;
  in>>DIM>>last>>maximum;SCALE=1ULL<<40;MINIMUM_RATES=1;
  std::vector<U> g(last+1);for(int n=1;n<=last;n++)in>>g[n];
  ISO.resize(maximum+1);for(int& r:ISO)in>>r;
  if(!in || last<6 || last>11)throw std::runtime_error("bad input");
  Table empty;
  Table p=stage({1000},{1000},empty,g[1]);
  p=stage({10000,1000},{100,10},p,g[2]);
  p=stage({1000,100,10},{100,10,10},p,g[3]);
  p=stage({1000,100,10,10},{100,100,10,1},p,g[4]);
  p=stage({1000,100,100,10,1},{100,10,10,1,1},p,g[5]);
  for(int n=6;n<=last;n++){
   std::vector<int> box(n,1),keep(n,1);box[0]=1000;box[1]=100;box[2]=10;box[3]=10;
   keep[0]=100;keep[1]=10;keep[2]=10;
   if(n==last){std::fill(keep.begin(),keep.end(),0);keep[0]=1;}
   p=stage(box,keep,p,g[n]);
  }
  return 0;
 }catch(const std::exception&e){std::cerr<<e.what()<<"\n";return 2;}
}
