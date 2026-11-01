#include <bits/stdc++.h>
using namespace std; using i64=long long;
static long long C(int n,int k){if(k<0||k>n)return 0; long long r=1;for(int i=1;i<=k;i++)r=r*(n-k+i)/i;return r;}
static inline void fwt(vector<i64>&a){for(size_t l=1;l<a.size();l<<=1)for(size_t i=0;i<a.size();i+=2*l)for(size_t j=0;j<l;j++){i64 u=a[i+j],v=a[i+j+l];a[i+j]=u+v;a[i+j+l]=u-v;}}
static inline bool cv22(uint32_t x,uint32_t c){int w=__builtin_popcount(x^c);return w<=7||w>=15;}

static vector<array<uint32_t,24>> load_h24(){
  vector<string> tok; string s;
  ifstream in("artifacts/R02/20260917T0443Z_5c7a9d31_i0095_exact.cpp");
  if(in){
    string all((istreambuf_iterator<char>(in)),{}); size_t p=all.find("HAD24[60]");
    if(p==string::npos) throw runtime_error("canonical HAD24 array not found");
    p=all.find('{',p); size_t q=all.find("};",p); string sub=all.substr(p,q-p);
    regex re("\\\"([0-9A-F ]+)\\\""); smatch m; string::const_iterator it=sub.begin();
    while(regex_search(it,sub.cend(),m,re)){istringstream z(m[1].str());while(z>>s)tok.push_back(s);it=m.suffix().first;}
  } else {
    ifstream f("/mnt/data/had24.txt"); while(f>>s)tok.push_back(s); // execution fallback only
  }
  if(tok.size()!=1440) throw runtime_error("expected 1440 Hadamard row tokens");
  vector<array<uint32_t,24>> M(60); size_t z=0;for(int h=0;h<60;h++)for(int r=0;r<24;r++)M[h][r]=strtoul(tok[z++].c_str(),nullptr,16);
  return M;
}
int main(){
  auto M=load_h24();
  for(int h=0;h<60;h++)for(int r=0;r<24;r++)for(int s=r;s<24;s++){
    int dot=24-2*__builtin_popcount(M[h][r]^M[h][s]); if(dot!=(r==s?24:0)) return 1;
  }
  long long tested=0,full=0; uint64_t checksum=0; const uint32_t N23=1u<<22;
  for(int h=0;h<60;h++)for(int dc=0;dc<24;dc++){
    int keep[23],k=0;for(int c=0;c<24;c++)if(c!=dc)keep[k++]=c;int anchor=keep[0];uint32_t cen[24];
    for(int r=0;r<24;r++){int a=(M[h][r]>>(23-anchor))&1;uint32_t q=0;for(int j=1;j<23;j++){int b=((M[h][r]>>(23-keep[j]))&1)^a;if(b)q|=1u<<(j-1);}cen[r]=q;}
    tested++; bool all=true; uint32_t u=0;
    for(uint32_t x=0;x<N23;x++){bool ok=false;for(auto c:cen){int w=__builtin_popcount(x^c);if(w<=7||w>=16){ok=true;break;}}if(!ok){all=false;u=x;break;}}
    if(all)full++; else checksum=checksum*1315423911ULL+u+1ULL+257ULL*h+dc;
  }
  if(tested!=1440||full) return 2;
  cout<<"had24_classes_verified=60 orthogonality_exact=1\n";
  cout<<"length23_one_column_punctures_tested="<<tested<<" full_24row_folded_radius7_covers="<<full<<" uncovered_checksum="<<checksum<<"\n";

  for(int n=21;n<=26;n++){
    long long V=0;for(int k=0;k<=7;k++)V+=C(n,k); unsigned long long nV=(unsigned long long)n*V,Q=1ULL<<(n-1);long long d=n-14,L=d*d*17LL,R=49LL*n;
    cout<<"radius7_n="<<n<<" V="<<V<<" nV="<<nV<<" quotient="<<Q<<" beats_A17="<<(L>R)<<" ratio_compare="<<L<<":"<<R<<"\n";
    if(n>=22&&n<=25&&!(nV>=Q&&L>R))return 3;if(n==21&&L>R)return 4;if(n==26&&!(nV<Q))return 5;
  }
  long long V26=0;for(int k=0;k<=7;k++)V26+=C(26,k);if(!(2*V26<27*C(26,7)))return 6;
  cout<<"radius7_monotonicity_base_2V26="<<2*V26<<" less_than_27C26_7="<<27*C(26,7)<<"\n";

  const uint32_t A[22]={1398112,892963,323539,1948110,1215594,948297,464538,1124633,1053255,130733,1595570,1893916,1466799,1750401,533480,2043637,245972,1831803,432948,749318,529791,2083721};
  const uint32_t N=1u<<21; vector<unsigned char> cov(N);for(uint32_t x=0;x<N;x++)for(auto c:A)if(cv22(x,c))cov[x]++;long long unc=0;for(auto z:cov)if(!z)unc++;if(unc!=1231)return 7;
  vector<i64>G(N);for(uint32_t x=0;x<N;x++){int w=__builtin_popcount(x);G[x]=(w<=7||w>=15);}fwt(G);long long mn=LLONG_MAX;int noimp=0;
  for(int i=0;i<22;i++){
    vector<i64>F(N);long long need=0;for(uint32_t x=0;x<N;x++){int z=(int)cov[x]-(cv22(x,A[i])?1:0);if(!z)F[x]=1,need++;}fwt(F);for(uint32_t k=0;k<N;k++)F[k]*=G[k];fwt(F);i64 best=-1;
    for(uint32_t k=0;k<N;k++){if(F[k]%(i64)N)return 8;best=max(best,F[k]/(i64)N);}long long r=need-best;mn=min(mn,r);if(r==1231)noimp++;if(r<1231)return 9;
  }
  if(mn!=1231||noimp!=22)return 10;
  cout<<"n22_recovered_residual="<<unc<<" exact_one_center_global_best_response_min_residual="<<mn<<" coordinates_with_no_improvement="<<noimp<<"/22\n";
  cout<<"ALL_EXACT_CHECKS_PASS\n";
}
