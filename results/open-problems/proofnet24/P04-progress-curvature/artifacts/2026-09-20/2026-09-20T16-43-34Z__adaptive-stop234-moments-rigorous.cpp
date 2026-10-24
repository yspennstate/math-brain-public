#include <bits/stdc++.h>
using namespace std;

static constexpr int L=4,W=7;
static constexpr uint64_t Q=1000000000000000ULL;
static constexpr uint64_t A_NUM=16139ULL, A_DEN=31250ULL;
static constexpr uint64_t aQ=A_NUM*(Q/A_DEN);
static vector<vector<int>> adjv;
static uint64_t colmask[5];

struct V {
  uint64_t w;       // upward-rounded E[C+a(4-D)] from this state
  uint64_t cost_up; // upward-rounded remaining physical-time cost
  uint64_t cost_lo; // downward-rounded remaining physical-time cost
  uint64_t m2;      // upward-rounded endpoint transverse second moment
  uint64_t eta_lo;  // downward-rounded E[4-D]
  uint64_t eta_hi;  // upward-rounded E[4-D]
};

struct KeyHash {
  size_t operator()(const pair<uint64_t,uint8_t>&p) const noexcept {
    return hash<uint64_t>()(p.first ^ ((uint64_t)p.second<<61));
  }
};

static unordered_map<pair<uint64_t,uint8_t>,V,KeyHash> memo;
static unsigned long long cnt[5]={},stops[5]={},conts[5]={};
static inline uint64_t cdiv(__int128 x,uint64_t y){return (uint64_t)((x+y-1)/y);}
static inline uint64_t fdiv(__int128 x,uint64_t y){return (uint64_t)(x/y);}

V adv(uint64_t mask,int k){
  auto key=make_pair(mask,(uint8_t)k);
  auto it=memo.find(key);
  if(it!=memo.end()) return it->second;
  ++cnt[k];

  if(mask&colmask[k]){
    int rr=-1,ct=0;
    for(int r=0;r<W;++r) if((mask>>(k*W+r))&1ULL){rr=r;++ct;}
    assert(rr>=0 && ct==1); // first hit of column k
    long long d=rr-W/2;
    if(k==4){
      V v{0,0,0,(uint64_t)(d*d)*Q,0,0};
      memo.emplace(key,v); return v;
    }
    uint64_t stop=(uint64_t)(4-k)*aQ;
    V cv=adv(mask,k+1);
    V v;
    if(stop<=cv.w){
      ++stops[k];
      uint64_t eta=(uint64_t)(4-k)*Q;
      v={stop,0,0,(uint64_t)(d*d)*Q,eta,eta};
    } else {
      ++conts[k];
      v=cv;
    }
    memo.emplace(key,v); return v;
  }

  int rates[64]={0},tot=0;
  uint64_t mm=mask;
  while(mm){
    int i=__builtin_ctzll(mm); mm&=mm-1;
    for(int j:adjv[i]) if(!((mask>>j)&1ULL)){++rates[j];++tot;}
  }
  assert(tot>0);

  __int128 sw=Q, scu=Q, scl=Q, sm=0, seLo=0, seHi=0;
  for(int j=0;j<(L+1)*W;++j) if(rates[j]){
    V c=adv(mask|(1ULL<<j),k);
    sw   += (__int128)rates[j]*c.w;
    scu  += (__int128)rates[j]*c.cost_up;
    scl  += (__int128)rates[j]*c.cost_lo;
    sm   += (__int128)rates[j]*c.m2;
    seLo += (__int128)rates[j]*c.eta_lo;
    seHi += (__int128)rates[j]*c.eta_hi;
  }
  V v{cdiv(sw,tot),cdiv(scu,tot),fdiv(scl,tot),cdiv(sm,tot),fdiv(seLo,tot),cdiv(seHi,tot)};
  memo.emplace(key,v); return v;
}

int main(){
  int n=(L+1)*W;
  auto id=[](int x,int r){return x*W+r;};
  adjv.assign(n,{});
  for(int x=0;x<L;++x) for(int r=0;r<W;++r){
    int p=id(x,r),q=id(x+1,r); adjv[p].push_back(q); adjv[q].push_back(p);
  }
  for(int x=0;x<L;++x) for(int r=0;r<W-1;++r){
    int p=id(x,r),q=id(x,r+1); adjv[p].push_back(q); adjv[q].push_back(p);
  }
  for(int x=0;x<=L;++x) for(int r=0;r<W;++r) colmask[x]|=1ULL<<id(x,r);

  memo.reserve(40000000);
  uint64_t start=1ULL<<id(0,W/2);
  V root=adv(start,1);

  assert(cnt[1]==80ULL && cnt[2]==5896ULL && cnt[3]==462615ULL && cnt[4]==35095016ULL);
  assert(stops[1]==0ULL);
  assert(root.w < 4*aQ);
  assert(root.eta_lo<=root.eta_hi);
  assert(root.cost_lo<=root.cost_up);

  cout<<"P04 T10 adaptive-stop 2/3/4 rigorous moment certificate\n";
  cout<<"ALL_RIGOROUS_CHECKS_PASS = True\n";
  cout<<"Q = "<<Q<<"\n";
  cout<<"root_transformed_upper = "<<root.w<<"\n";
  cout<<"cost_lo = "<<root.cost_lo<<"\n";
  cout<<"cost_up = "<<root.cost_up<<"\n";
  cout<<"eta_lo = "<<root.eta_lo<<"\n";
  cout<<"eta_hi = "<<root.eta_hi<<"\n";
  cout<<"D_lo = "<<(4*Q-root.eta_hi)<<"\n";
  cout<<"D_hi = "<<(4*Q-root.eta_lo)<<"\n";
  cout<<"xi2_policy_upper = "<<root.m2<<"\n";
  cout<<"stage_states = "<<cnt[1]<<","<<cnt[2]<<","<<cnt[3]<<","<<cnt[4]<<"\n";
  cout<<"stop_state_evals = "<<stops[1]<<","<<stops[2]<<","<<stops[3]<<"\n";
  cout<<"continue_state_evals = "<<conts[1]<<","<<conts[2]<<","<<conts[3]<<"\n";
  cout<<setprecision(18);
  cout<<"cost_up_decimal = "<<(long double)root.cost_up/Q<<"\n";
  cout<<"eta_lo_decimal = "<<(long double)root.eta_lo/Q<<"\n";
  cout<<"eta_hi_decimal = "<<(long double)root.eta_hi/Q<<"\n";
  cout<<"D_lo_decimal = "<<(long double)(4*Q-root.eta_hi)/Q<<"\n";
  cout<<"xi2_policy_upper_decimal = "<<(long double)root.m2/Q<<"\n";
  cout.flush();
  _Exit(0);
}
