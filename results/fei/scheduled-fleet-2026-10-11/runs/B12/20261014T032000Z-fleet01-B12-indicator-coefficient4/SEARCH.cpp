#include <algorithm>
#include <cmath>
#include <cstdint>
#include <iostream>
#include <iomanip>
#include <limits>
#include <random>
#include <vector>

struct State {
  int n, N, m;
  std::vector<unsigned char> q;
  std::vector<int> w;
  std::vector<int> deg;
  double score;
};

static double score(State const& s) {
  if (s.m == 0 || s.m == s.N) return -1e100;
  long double denom = 0.0L, sumzlogz = 0.0L;
  for (int a = 0; a < s.N; ++a) {
    long double z2 = (long double)s.w[a] * s.w[a];
    denom += s.deg[a] * z2;
    if (z2 > 0) sumzlogz += z2 * std::log2((double)z2);
  }
  if (denom == 0) return -1e100;
  long double nm = (long double)s.N * s.m;
  long double numer = nm * std::log2((double)nm) - sumzlogz;
  return (double)(numer / denom);
}

static State random_state(int n, std::mt19937_64& rng) {
  State s; s.n=n; s.N=1<<n; s.m=0; s.q.resize(s.N); s.w.resize(s.N); s.deg.resize(s.N);
  std::uniform_real_distribution<double> U(0.0,1.0);
  double p=0.5+0.45*U(rng);
  for(int x=0;x<s.N;++x){s.q[x]=U(rng)<p;s.m+=s.q[x];}
  if(s.m==0){s.q[0]=1;s.m=1;} if(s.m==s.N){s.q[0]=0;--s.m;}
  for(int a=0;a<s.N;++a){
    s.deg[a]=__builtin_popcount((unsigned)a);
    int z=0; for(int x=0;x<s.N;++x) z += s.q[x]*((__builtin_parity((unsigned)(a&x)))?-1:1);
    s.w[a]=z;
  }
  s.score=score(s); return s;
}

static void flip(State& s,int x){
  int delta=s.q[x]?-1:1; s.q[x]^=1; s.m+=delta;
  for(int a=0;a<s.N;++a) s.w[a]+=delta*((__builtin_parity((unsigned)(a&x)))?-1:1);
  s.score=score(s);
}

int main(){
  std::mt19937_64 rng(20261014032000ULL);
  State global; global.score=-1e100;
  for(int n=5;n<=9;++n){
    int N=1<<n;
    for(int restart=0;restart<40;++restart){
      State s=random_state(n,rng); double temp=0.03;
      for(int it=0;it<20000;++it){
        int x=(int)(rng()%N); double old=s.score; flip(s,x); double neu=s.score;
        double accept=std::exp(std::min(0.0,(neu-old)/temp));
        double u=(double)(rng()>>11)*(1.0/9007199254740992.0);
        if(u>accept) flip(s,x); else if(s.score>global.score){
          global=s;
          uint64_t mask=0; if(N<=64) for(int j=0;j<N;++j) if(s.q[j]) mask|=uint64_t(1)<<j;
          std::cout<<"best n="<<n<<" K="<<std::setprecision(16)<<s.score<<" m="<<s.m;
          if(N<=64) std::cout<<" mask="<<mask;
          std::cout<<"\n"<<std::flush;
        }
        temp*=0.9998; if(temp<1e-5) temp=1e-5;
      }
    }
  }
  std::cout<<"FINAL n="<<global.n<<" K="<<std::setprecision(17)<<global.score<<" m="<<global.m<<"\n";
  std::cout<<"values"; for(int x=0;x<global.N;++x) std::cout<<" "<<(int)global.q[x]; std::cout<<"\n";
  std::cout<<"walsh"; for(int z:global.w) std::cout<<" "<<z; std::cout<<"\n";
}
