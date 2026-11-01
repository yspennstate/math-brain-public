#include <boost/multiprecision/cpp_int.hpp>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <set>
#include <vector>
#include <algorithm>
using namespace std;
using boost::multiprecision::cpp_int;
using i64 = long long;

static constexpr int n=7, N=128;
static constexpr i64 QLOG=(1LL<<20);

static int pc(int x){ return __builtin_popcount((unsigned)x); }
static int emax(int m){ int s=0; for(int x=0;x<m;x++) s+=pc(x); return s; }

static int edges(const set<int>& M, int dims=7){
  int e=0; for(int x:M) for(int i=0;i<dims;i++) if(M.count(x^(1<<i))) e++; return e/2;
}

static vector<int> walsh_abs(const set<int>& M){
  vector<int> a(N); for(int s=0;s<N;s++){ int z=0; for(int x:M) z += (pc(s&x)&1)?-1:1; a[s]=abs(z); } return a;
}
static map<int,int> counts_nonempty(const set<int>& M){
  auto a=walsh_abs(M); map<int,int> c; for(int s=1;s<N;s++) c[a[s]]++; return c;
}
static void require_counts(const set<int>& M,const map<int,int>& target,const string& tag){
  assert((int)M.size()==13); assert(edges(M)==21); auto c=counts_nonempty(M);
  if(c!=target){ cerr<<"bad spectrum "<<tag<<"\n"; exit(2); }
}

static cpp_int ipow(int b,int e){ cpp_int r=1,x=b; while(e){ if(e&1)r*=x; e>>=1; if(e)x*=x; } return r; }
static i64 lf(int p){ return (i64)boost::multiprecision::msb(ipow(p,(int)QLOG)); }
static i64 log_lo(int p){ return lf(p); }
static i64 log_hi(int p){ return lf(p)+1; }

int main(){
  cout<<"P03_C7_M13_B49_EXACT\n";
  cout<<"emax:"; for(int m=1;m<=13;m++) cout<<" "<<m<<":"<<emax(m); cout<<"\n";
  int dismax=0; for(int a=1;a<=12;a++) dismax=max(dismax,emax(a)+emax(13-a));
  cout<<"disconnected_upper="<<dismax<<"\n"; assert(dismax==20);

  cout<<"r_ge_6_split_table:";
  vector<int> tab3; for(int b=1;b<=6;b++){ int a=13-b; int u=emax(a)+emax(b)+min(b,3); tab3.push_back(u); cout<<" "<<b<<":"<<u; }
  cout<<"\n"; assert((tab3==vector<int>{21,20,20,20,20,19}));

  cout<<"r_5_split_table:";
  vector<int> tab4; for(int b=1;b<=6;b++){ int a=13-b; int u=emax(a)+emax(b)+min(b,4); tab4.push_back(u); cout<<" "<<b<<":"<<u; }
  cout<<"\n"; assert((tab4==vector<int>{21,20,20,21,21,20}));

  const map<int,int> R4={{1,96},{3,24},{13,7}};
  const map<int,int> R5={{1,96},{3,12},{5,12},{11,4},{13,3}};

  // r=4: representatives for the two stabilizer types of a 3-point complement with one edge.
  for(int v: {6,14}){ set<int>M; for(int x=0;x<16;x++) if(x!=0&&x!=1&&x!=v) M.insert(x); require_counts(M,R4,"r4"); }

  // r=5, b=1: A is canonical 12-extremal in Q4, B={y} subset A.
  set<int>A12; for(int x=0;x<12;x++)A12.insert(x); int b1=0;
  for(int y:A12){ set<int>M=A12; M.insert(y|16); require_counts(M,R5,"r5-b1"); b1++; }
  cout<<"r5_b1_normal_form_choices="<<b1<<"\n"; assert(b1==12);

  // r=5, b=4: A is canonical 9-extremal; B ranges over all 2-faces contained in A.
  set<int>A9; for(int x=0;x<9;x++)A9.insert(x); int b4=0;
  for(int i=0;i<4;i++)for(int j=i+1;j<4;j++){
    vector<int> fixed; for(int k=0;k<4;k++) if(k!=i&&k!=j) fixed.push_back(k);
    for(int mask=0;mask<4;mask++){
      int base=0; for(int q=0;q<2;q++) if(mask&(1<<q)) base|=1<<fixed[q];
      set<int>B={base,base^(1<<i),base^(1<<j),base^(1<<i)^(1<<j)};
      bool sub=true; for(int x:B)if(!A9.count(x))sub=false; if(!sub)continue;
      set<int>M=A9; for(int x:B)M.insert(x|16); require_counts(M,R5,"r5-b4"); b4++;
    }
  }
  cout<<"r5_b4_normal_form_choices="<<b4<<"\n"; assert(b4==6);

  // r=5, b=5: A is canonical 8-extremal; B ranges over all size-5 extremals with |A cap B|=4.
  set<int>A8; for(int x=0;x<8;x++)A8.insert(x); int b5=0;
  for(int mask=0;mask<(1<<16);mask++) if(pc(mask)==5){
    set<int>B; for(int x=0;x<16;x++) if(mask&(1<<x)) B.insert(x);
    int inter=0; for(int x:B) if(A8.count(x)) inter++;
    if(inter!=4 || edges(B,4)!=5) continue;
    set<int>M=A8; for(int x:B)M.insert(x|16); require_counts(M,R5,"r5-b5"); b5++;
  }
  cout<<"r5_b5_normal_form_choices="<<b5<<"\n"; assert(b5==24);

  // Exact logarithmic lower bounds for 1568*(C7* - R_case), scaled by QLOG.
  i64 l3=lf(3),l5=lf(5),l7=lf(7),l11=lf(11),l13=lf(13),l17=lf(17);
  auto lo=[&](i64 c,int p)->cpp_int{ i64 l=lf(p); return cpp_int(c)*(c>=0?l:l+1); };
  cpp_int N4=cpp_int(147456)*QLOG + lo(-24966,3)+lo(-27783,7)+lo(2601,17)+lo(1183,13);
  cpp_int N5=cpp_int(147456)*QLOG + lo(-25074,3)+lo(-27783,7)+lo(2601,17)+lo(300,5)+lo(484,11)+lo(507,13);
  cout<<"r4_gap_lower_num="<<N4<<"\n";
  cout<<"r5_gap_lower_num="<<N5<<"\n";
  if(N4<=0||N5<=0){ cerr<<"nonpositive exact gap\n"; return 3; }
  cout<<"P03-C7-M13-B49-CERTIFICATE=PASS\n";
  return 0;
}
