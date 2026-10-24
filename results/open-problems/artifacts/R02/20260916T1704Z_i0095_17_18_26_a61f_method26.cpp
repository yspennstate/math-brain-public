#include <bits/stdc++.h>
using namespace std;
static mt19937_64 rng(202609162003ULL);
uint32_t foldx(uint32_t x,uint32_t mask){uint32_t y=x^mask; return min(x,y);} 
int main(int argc,char**argv){int n=22,R=7,restarts=5,steps=500,samps=30; if(argc>1)n=atoi(argv[1]); if(argc>2)R=atoi(argv[2]); if(argc>3)restarts=atoi(argv[3]); if(argc>4)steps=atoi(argv[4]); if(argc>5)samps=atoi(argv[5]);
 uint32_t mask=(1u<<n)-1, half=1u<<(n-1); vector<uint32_t> flips; flips.reserve(300000);
 for(uint32_t x=0;x<(1u<<n);x++) if(__builtin_popcount(x)<=R) flips.push_back(x);
 cerr<<"n "<<n<<" R "<<R<<" half "<<half<<" flips "<<flips.size()<<"\n";
 vector<unsigned char> cnt(half); vector<uint32_t> centers(n); long long global=half; vector<uint32_t> gb;
 auto update=[&](uint32_t c,int delta){for(uint32_t f:flips){uint32_t y=foldx(c^f,mask); cnt[y]+=delta;}};
 auto gain=[&](uint32_t c){int g=0; for(uint32_t f:flips){uint32_t y=foldx(c^f,mask); if(cnt[y]==0) g++;} return g;};
 auto unique=[&](uint32_t c){int g=0; for(uint32_t f:flips){uint32_t y=foldx(c^f,mask); if(cnt[y]==1) g++;} return g;};
 uniform_int_distribution<uint32_t> U(0,half-1); uniform_int_distribution<size_t> UF(0,flips.size()-1);
 for(int rr=0;rr<restarts;rr++){
   fill(cnt.begin(),cnt.end(),0); centers[0]=0; for(int i=1;i<n;i++) centers[i]=U(rng); for(auto c:centers) update(c,+1);
   long long unc=0; for(auto z:cnt) unc+=(z==0); if(unc<global){global=unc;gb=centers;cerr<<"BEST "<<global<<" init r"<<rr<<"\n";}
   for(int st=0;st<steps && unc;st++){
      vector<pair<int,int>> us; for(int i=1;i<n;i++) us.push_back({unique(centers[i]),i}); nth_element(us.begin(),us.begin()+min<int>(5,us.size())-1,us.end()); int lim=min<int>(5,us.size()); sort(us.begin(),us.begin()+lim); int idx=us[rng()%lim].second;
      uint32_t old=centers[idx]; int olduniq=unique(old); update(old,-1); long long base=unc+olduniq;
      int bestg=-1; uint32_t bestc=old;
      for(int s=0;s<samps;s++){
        uint32_t x; do{x=U(rng);}while(cnt[x]!=0);
        uint32_t c=foldx(x^flips[UF(rng)],mask);
        int g=gain(c); if(g>bestg){bestg=g;bestc=c; if(base-g==0) break;}
      }
      long long nu=base-bestg;
      bool accept=nu<=unc;
      if(!accept){ double T=max(1.0, 100.0*(1.0-(double)st/steps)); double prob=exp((double)(unc-nu)/T); accept=generate_canonical<double,53>(rng)<prob;}
      if(accept){centers[idx]=bestc;update(bestc,+1);unc=nu;} else {update(old,+1);} 
      if(unc<global){global=unc;gb=centers;cerr<<"BEST "<<global<<" rr "<<rr<<" st "<<st<<"\n"; if(!global)break;}
   }
   cerr<<"end rr "<<rr<<" unc "<<unc<<" global "<<global<<"\n";
   if(global==0)break;
 }
 cout<<"FINAL unc="<<global<<" centers"; for(auto c:gb) cout<<" "<<c; cout<<"\n";
}
