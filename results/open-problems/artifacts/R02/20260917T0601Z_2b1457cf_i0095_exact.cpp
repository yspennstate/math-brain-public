#include <bits/stdc++.h>
using namespace std;

long long C(int n,int k){ if(k<0||k>n)return 0; long long r=1; for(int i=1;i<=k;i++) r=r*(n-k+i)/i; return r; }
long long I(int n,int r,int d){ long long s=0; for(int a=0;a<=d;a++) for(int b=0;b<=n-d;b++) if(a+b<=r && d-a+b<=r) s += C(d,a)*C(n-d,b); return s; }

int main(){
  // Lin--Phoa Example 4, order-22 Type-I near-Hadamard design.
  const int v=10,n=22;
  int aa[v]={-1,-1,1,-1,1,-1,1,-1,1,1};
  int bb[v]={-1,-1,-1,-1,1,1,-1,1,1,1};
  int A[v][v],B[v][v];
  for(int i=0;i<v;i++)for(int j=0;j<v;j++){ A[i][j]=aa[(j-i+v)%v]; B[i][j]=bb[(j-i+v)%v]; }
  int M[n][n]{};
  M[0][0]=1;M[0][1]=1; for(int j=0;j<v;j++){M[0][2+j]=1;M[0][12+j]=1;}
  M[1][0]=1;M[1][1]=-1;for(int j=0;j<v;j++){M[1][2+j]=1;M[1][12+j]=-1;}
  for(int i=0;i<v;i++){
    int r=2+i; M[r][0]=1;M[r][1]=1;
    for(int j=0;j<v;j++){M[r][2+j]=A[i][j];M[r][12+j]=B[i][j];}
  }
  for(int i=0;i<v;i++){
    int r=12+i; M[r][0]=1;M[r][1]=-1;
    for(int j=0;j<v;j++){M[r][2+j]=B[j][i];M[r][12+j]=-A[j][i];}
  }
  int disc=99; uint32_t bestmask=0; vector<int>bestsums;
  for(uint32_t mask=0;mask<(1u<<21);mask++){
    int mx=0; vector<int>s(n);
    for(int i=0;i<n;i++){
      int z=M[i][0];
      for(int j=1;j<n;j++){int x=((mask>>(j-1))&1)?-1:1; z += M[i][j]*x;}
      s[i]=z; mx=max(mx,abs(z)); if(mx>=disc) break;
    }
    if(mx<disc){disc=mx;bestmask=mask;bestsums=s;}
  }
  if(disc!=6){cerr<<"Example4 discrepancy mismatch: "<<disc<<"\n";return 1;}
  cout<<"lin_phoa_example4_order22_discrepancy="<<disc<<" witness_mask="<<bestmask<<"\n";
  cout<<"witness_row_sums="; for(int z:bestsums)cout<<z<<' '; cout<<"\n";

  // Best 22-center folded-radius-7 quotient code found in this run.
  const uint32_t C22[22]={1398112,892963,323539,1948110,1215594,948297,464538,1124633,1053255,130733,1595570,1893916,1466799,1750401,533480,2043637,245972,1831803,432948,749318,529791,2083721};
  long long uncovered=0;
  const uint32_t QN=1u<<21;
  for(uint32_t x=0;x<QN;x++){
    bool ok=false;
    for(uint32_t c:C22){int w=__builtin_popcount(x^c); if(w<=7||w>=15){ok=true;break;}}
    if(!ok) uncovered++;
  }
  if(uncovered!=1231){cerr<<"residual mismatch "<<uncovered<<"\n";return 2;}
  cout<<"n22_folded_radius7_residual="<<uncovered<<"\n";

  // Exact pair-overlap necessary condition for any 22-center cover.
  long long V=0;for(int k=0;k<=7;k++)V+=C(22,k);
  if(V!=280600){cerr<<"V mismatch\n";return 3;}
  long long threshold=2LL*22*V-3LL*QN; // N(2 lambda -3)
  if(threshold!=6054944){cerr<<"threshold mismatch "<<threshold<<"\n";return 4;}
  cout<<"folded_ball_size="<<V<<" pair_overlap_cover_threshold="<<threshold<<"\n";
  long long J[12];
  for(int d=0;d<=11;d++){J[d]=I(22,7,d)+I(22,7,22-d); cout<<"J["<<d<<"]="<<J[d]<<"\n";}
  long long expected[12]={280600,164320,164320,110056,110056,72928,72928,45628,49060,29040,37356,23496};
  for(int d=0;d<=11;d++)if(J[d]!=expected[d]){cerr<<"J mismatch d="<<d<<"\n";return 5;}
  map<int,int> hist; long long pairSum=0;
  for(int i=0;i<22;i++)for(int j=i+1;j<22;j++){int d=__builtin_popcount(C22[i]^C22[j]);d=min(d,22-d);hist[d]++;pairSum+=J[d];}
  if(pairSum!=7061052){cerr<<"pairSum mismatch "<<pairSum<<"\n";return 6;}
  cout<<"best_code_distance_hist="; for(auto [d,c]:hist)cout<<d<<":"<<c<<" ";cout<<"\n";
  cout<<"best_code_pair_overlap_sum="<<pairSum<<"\n";

  // Exact normalized comparisons.
  // 8/sqrt(22) > 7/sqrt(17) iff 64*17 > 49*22.
  long long lhs=64LL*17,rhs=49LL*22;
  if(!(lhs>rhs)){cerr<<"ratio comparison failed\n";return 7;}
  cout<<"ratio_compare_8_over_sqrt22_vs_7_over_sqrt17="<<lhs<<">"<<rhs<<"\n";
  cout<<"ALL_EXACT_CHECKS_PASS\n";
}
