#include <boost/multiprecision/cpp_int.hpp>
#include <bits/stdc++.h>
using namespace std;
using boost::multiprecision::cpp_int;
using u128 = unsigned __int128;

struct P {
  int x,y,z;
  bool operator<(P const& o) const { return tie(x,y,z) < tie(o.x,o.y,o.z); }
};
struct M66 { uint64_t lo=0, hi=0; };
static inline M66 mor(M66 a,M66 b){ return {a.lo|b.lo,a.hi|b.hi}; }
static inline int pop66(M66 a){ return __builtin_popcountll(a.lo)+__builtin_popcountll(a.hi); }
static vector<P> shell(int r){
  vector<P> v;
  for(int x=-r;x<=r;x++) for(int y=-r;y<=r;y++) for(int z=-r;z<=r;z++)
    if(abs(x)+abs(y)+abs(z)==r) v.push_back({x,y,z});
  return v;
}
static vector<P> nbrs(P p){
  return {{p.x+1,p.y,p.z},{p.x-1,p.y,p.z},{p.x,p.y+1,p.z},
          {p.x,p.y-1,p.z},{p.x,p.y,p.z+1},{p.x,p.y,p.z-1}};
}
static string u128s(u128 x){ if(!x) return "0"; string s; while(x){s.push_back(char('0'+x%10));x/=10;} reverse(s.begin(),s.end()); return s; }
static cpp_int parse_big(const string&s){ cpp_int x=0; for(char c:s){x*=10;x+=c-'0';} return x; }
static cpp_int gcd_big(cpp_int a, cpp_int b){ while(b!=0){ cpp_int r=a%b; a=b; b=r; } return a; }

static vector<uint32_t> INM(38), PNUM(1<<18);
static vector<M66> OUTM(38);
static int K;
static u128 TOTAL;
static void dfs(int start,int depth,uint32_t Y,M66 Z){
  if(depth==K){ TOTAL += (u128)PNUM[Y] << (66-pop66(Z)); return; }
  int need=K-depth;
  for(int i=start;i<=38-need;i++) dfs(i+1,depth+1,Y|INM[i],mor(Z,OUTM[i]));
}

int main(){
  cout << "R09 exact checker: radius-4 certificate through |A|<=12 + l1 passage domain\n";
  auto S1=shell(1), S2=shell(2), S3=shell(3), S4=shell(4);
  if(S1.size()!=6 || S2.size()!=18 || S3.size()!=38 || S4.size()!=66) return 2;
  map<P,int> i1,i2,i4;
  for(int i=0;i<(int)S1.size();i++)i1[S1[i]]=i;
  for(int i=0;i<(int)S2.size();i++)i2[S2[i]]=i;
  for(int i=0;i<(int)S4.size();i++)i4[S4[i]]=i;
  for(int i=0;i<38;i++) for(P y:nbrs(S3[i])){
    int r=abs(y.x)+abs(y.y)+abs(y.z);
    if(r==2) INM[i] |= 1u<<i2[y];
    if(r==4){ int j=i4[y]; if(j<64) OUTM[i].lo |= 1ull<<j; else OUTM[i].hi |= 1ull<<(j-64); }
  }
  vector<uint32_t> reach(64);
  for(int sm=0;sm<64;sm++){
    uint32_t rm=0;
    for(P y:S2){
      bool ok=false;
      for(P z:nbrs(y)) if(abs(z.x)+abs(z.y)+abs(z.z)==1 && ((sm>>i1[z])&1)){ok=true;break;}
      if(ok) rm |= 1u<<i2[y];
    }
    reach[sm]=rm;
  }
  const int Q=18;
  for(uint32_t Y=0;Y<(1u<<18);Y++){
    uint32_t num=0;
    for(uint32_t rm:reach){ int k=__builtin_popcount(Y&rm); if(k) num += (1u<<Q)-(1u<<(Q-k)); }
    PNUM[Y]=num;
  }

  vector<string> exp_raw={
    "2720773306528480238411710464",
    "1772293628573416183761469440",
    "1062050999214371775214256128",
    "591965302916963954166071296",
    "309295578646188144967286784",
    "152348794358940594847350784",
    "71040229313639204934647808"
  };
  cpp_int sum_6_12=0;
  for(K=6;K<=12;K++){
    TOTAL=0; dfs(0,0,0,{});
    string got=u128s(TOTAL);
    if(got!=exp_raw[K-6]){ cerr<<"raw mismatch k="<<K<<" got="<<got<<"\n"; return 3; }
    sum_6_12 += parse_big(got);
    cout << "k="<<K<<" common_numerator="<<got<<" PASS\n";
  }

  // All failure contributions use common denominator 2^129.
  cpp_int den = cpp_int(1) << 129;
  cpp_int D5_common = cpp_int(263121688539LL) << 56; // old D5 denominator was 2^73.
  cpp_int D12_common = D5_common + sum_6_12;
  cpp_int exp_D12 = parse_big("25639683654869377825421918208");
  if(D12_common!=exp_D12) return 4;
  cpp_int g=gcd_big(D12_common,den);
  cpp_int D12n=D12_common/g, D12d=den/g;
  if(D12n!=parse_big("48903815564860110903591") || D12d!=parse_big("1298074214633706907132624082305024")) return 5;

  cpp_int B3_common = parse_big("4517544707082764121") << 66; // B3 denominator 2^63.
  cpp_int B4_common = B3_common-D12_common;
  cpp_int gb=gcd_big(B4_common,den);
  cpp_int B4n=B4_common/gb, B4d=den/gb;
  if(B4n!=parse_big("635787895558830340599512346683097") || B4d!=parse_big("1298074214633706907132624082305024")) return 6;

  // Strict improvement over previous |A|<=5 certificate B4_old.
  cpp_int oldn=parse_big("4625965779789628771365"), oldd=parse_big("9444732965739290427392");
  if(!(B4n*oldd < oldn*B4d)) return 7;

  // Exact l1-ball coordinate count used by the refined passage compiler.
  for(int L=0;L<=100;L++){
    long long enumN=1; for(int r=1;r<=L;r++) enumN += 4LL*r*r+2;
    long long formula=(4LL*L*L*L+6LL*L*L+8LL*L+3)/3;
    if(enumN!=formula) return 8;
  }

  cout << "D12 = "<<D12n<<"/"<<D12d<<"\n";
  cout << "B4_k12 = "<<B4n<<"/"<<B4d<<"\n";
  cout << "strictly improves prior B4: PASS\n";
  cout << "l1 ball count |{||x||_1<=L}|=(4L^3+6L^2+8L+3)/3 for L<=100: PASS\n";
  cout << "PASS\n";
  return 0;
}
