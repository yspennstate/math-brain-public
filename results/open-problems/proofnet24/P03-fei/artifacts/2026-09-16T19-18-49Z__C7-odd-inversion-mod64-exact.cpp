#include <boost/multiprecision/cpp_int.hpp>
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <future>
#include <iostream>
#include <limits>
#include <map>
#include <unordered_map>
#include <utility>
#include <vector>
using namespace std;
using boost::multiprecision::cpp_int;
using i64 = long long;

static constexpr int QLOG = (1<<20);
static constexpr i64 INF = numeric_limits<i64>::max()/4;
static const vector<int> PR = {2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61};

struct H {
  size_t operator()(uint64_t x) const {
    x ^= x >> 33; x *= 0xff51afd7ed558ccdULL;
    x ^= x >> 33; x *= 0xc4ceb9fe1a85ec53ULL;
    x ^= x >> 33; return x;
  }
};

static map<int,int> lf;
static cpp_int ipow(int b,int e){cpp_int r=1,x=b;while(e){if(e&1)r*=x;e>>=1;if(e)x*=x;}return r;}
static void init_logs(){for(int p:PR)lf[p]=(p==2?QLOG:boost::multiprecision::msb(ipow(p,QLOG)));}
static map<int,int> factor_int(int x){map<int,int> f;for(int p:PR)while(x%p==0){f[p]++;x/=p;}assert(x==1);return f;}
static i64 log_lo(int a){if(a<=1)return 0;i64 s=0;for(auto [p,e]:factor_int(a))s+=(i64)e*lf[p];return s;}
static i64 log_hi(int a){if(a<=1)return 0;i64 s=0;for(auto [p,e]:factor_int(a))s+=(i64)e*(p==2?lf[p]:lf[p]+1);return s;}
static i64 t_lo(int a){return a<=1?0:(i64)a*a*log_lo(a);}
static int C(int n,int k){if(k<0||k>n)return 0;int r=1;for(int i=1;i<=k;i++)r=r*(n-k+i)/i;return r;}

// state = (sum a^2, sum d a^2, signed-sum residue mod 64)
static inline uint64_t pack(int q,int w,int r){return (uint64_t)q | ((uint64_t)w<<12) | ((uint64_t)r<<25);}
static inline void unpack(uint64_t k,int &q,int &w,int &r){q=k&4095; w=(k>>12)&8191; r=(k>>25)&63;}

using Side = unordered_map<uint64_t,i64,H>;

static Side side_dp(int m,int parity,int target_residue,int WMAX){
  const int Q=m*(128-m);
  vector<int> degs;
  for(int d=1;d<=7;d++) if((d&1)==parity)
    for(int j=0;j<C(7,d);j++) degs.push_back(d);

  // For odd m after translating XOR(M) to zero, every signed Walsh coefficient
  // is congruent to m (mod 4). Thus the possible signed values are m,m-4,...,-m+2.
  vector<int> vals;
  for(int v=m;v>=-m;v-=4) vals.push_back(v);

  Side dp,nd; dp.reserve(300000); dp[pack(0,0,0)]=0;
  for(int d:degs){
    nd.clear(); nd.reserve(dp.size()*2+1000);
    for(auto &kv:dp){
      int q,w,r; unpack(kv.first,q,w,r);
      for(int v:vals){
        int a=abs(v), nq=q+a*a, nw=w+d*a*a;
        if(nq>Q || nw>WMAX) continue;
        int nr=(r+v)%64; if(nr<0) nr+=64;
        uint64_t key=pack(nq,nw,nr);
        i64 nv=kv.second+t_lo(a);
        auto it=nd.find(key);
        if(it==nd.end() || nv<it->second) nd[key]=nv;
      }
    }
    dp.swap(nd);
  }

  // Compress to (q,w) among states with the required side residue.
  const uint64_t BASE=(uint64_t)WMAX+1;
  Side out; out.reserve(dp.size()/8+1000);
  int tr=((target_residue%64)+64)%64;
  for(auto &kv:dp){
    int q,w,r; unpack(kv.first,q,w,r);
    if(r!=tr) continue;
    uint64_t key=(uint64_t)q*BASE+w;
    auto it=out.find(key);
    if(it==out.end() || kv.second<it->second) out[key]=kv.second;
  }
  return out;
}

static i64 min_T_nonempty(int m,int B){
  int Q=m*(128-m), W=64*B, WMAX=W;
  // Fourier inversion at 0 and at all-ones gives the necessary congruences
  // odd-degree signed sum == 0 (mod64), even-degree nonempty signed sum == -m (mod64).
  auto fo=async(launch::async,[&](){return side_dp(m,1,0,WMAX);});
  auto fe=async(launch::async,[&](){return side_dp(m,0,-m,WMAX);});
  Side odd=fo.get(), even=fe.get();
  const uint64_t BASE=(uint64_t)WMAX+1;
  i64 best=INF;
  for(auto &kv:odd){
    int q=kv.first/BASE, w=kv.first%BASE;
    int eq=Q-q, ew=W-w;
    if(eq<0||ew<0||ew>WMAX) continue;
    auto it=even.find((uint64_t)eq*BASE+ew);
    if(it!=even.end()) best=min(best,kv.second+it->second);
  }
  return best;
}

static i64 L_lower_num(int m,int B,i64 Tnon){
  int a0=64-m;
  return 24576LL*(B-7)*QLOG + 7*(t_lo(a0)+Tnon) - 3969LL*B*log_hi(63);
}

int main(int argc,char**argv){
  if(argc!=4){cerr << "usage: cert m B expected_Lnum\n"; return 1;}
  int m=atoi(argv[1]), B=atoi(argv[2]); i64 expected=stoll(argv[3]);
  init_logs();
  cout << "P03_C7_ODD_INVERSION_MOD64_EXACT_CERTIFICATE m="<<m<<" B="<<B<<"\n";
  i64 T=min_T_nonempty(m,B);
  assert(T<INF);
  i64 L=L_lower_num(m,B,T);
  cout << "CERT m="<<m<<" B="<<B<<" Tnon_lower_num="<<T<<" L_lower_num="<<L<<"\n";
  if(L!=expected){cerr<<"unexpected exact lower numerator\n"; return 2;}
  if(L<=0){cerr<<"nonpositive certificate\n"; return 3;}
  cout << "P03-C7-ODD-INVERSION-MOD64-CELL=PASS\n";
  return 0;
}
