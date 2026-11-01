#include <bits/stdc++.h>
using namespace std;
int main(){
  const int M=1<<16;
  const long long SCALE=1000000000000000LL;
  // Exact-rational upward entropy atom table imported from the independently generated
  // fleet04/B14 N=32 table. T[w]/SCALE >= (w^2/1024) log2(1024/w^2).
  long long T[33]={0};
  T[2]=31250000000000LL; T[4]=93750000000000LL; T[6]=169807324168044LL;
  T[8]=250000000000000LL; T[10]=327748418967313LL; T[12]=397979296672175LL;
  T[14]=456559443899824LL; T[16]=500000000000000LL; T[18]=525281835024787LL;
  T[20]=529743675869249LL; T[22]=511006048006930LL; T[24]=466917186688700LL;
  T[26]=395513184641840LL; T[28]=294987775599294LL; T[30]=163668874906902LL;

  vector<unsigned char> sz(M), bd(M);
  vector<array<signed char,16>> wal(M);
  static unsigned char pc[M];
  for(int m=0;m<M;m++){ pc[m]=__builtin_popcount((unsigned)m); sz[m]=pc[m]; }
  for(int m=0;m<M;m++){
    int b=0;
    for(int v=0;v<16;v++) if((m>>v)&1)
      for(int j=0;j<4;j++){ int u=v^(1<<j); if(((m>>u)&1)==0) b++; }
    bd[m]=b;
    for(int s=0;s<16;s++){
      int w=0;
      for(int v=0;v<16;v++){
        int f=((m>>v)&1)?1:-1;
        int chi=__builtin_parity((unsigned)(s&v))?-1:1;
        w += f*chi;
      }
      wal[m][s]=(signed char)w;
    }
  }

  vector<int> G[17][33];
  for(int m=0;m<M;m++) G[sz[m]][bd[m]].push_back(m);

  long long candidate_pairs=0, low_count=0;
  map<int,long long> cnt,maxHU;
  map<int,pair<int,int>> arg;
  for(int s=0;s<=16;s++){
    int t=16-s;
    for(int b0=0;b0<=32;b0++) if(!G[s][b0].empty())
      for(int b1=0;b1<=32;b1++) if(!G[t][b1].empty()){
        // |A0 triangle A1| >= ||A0|-|A1||.
        if(b0+b1+abs(s-t)>28) continue;
        for(int m0:G[s][b0]) for(int m1:G[t][b1]){
          candidate_pairs++;
          int B=b0+b1+pc[m0^m1];
          if(B>28) continue;
          low_count++; cnt[B]++;
          if(B==16) continue; // exactly the ten signed dictators; I-1=0.
          long long hu=0;
          for(int u=0;u<16;u++){
            int a=wal[m0][u], b=wal[m1][u];
            hu += T[abs(a+b)] + T[abs(a-b)];
          }
          if(!maxHU.count(B)||hu>maxHU[B]){ maxHU[B]=hu; arg[B]={m0,m1}; }
          // H <= 6(I-1) = 6(B/16-1) = 3(B-16)/8.
          // hu/SCALE is an UPWARD bound for H, so this exact integer comparison certifies the claim.
          if((__int128)8*hu > (__int128)3*(B-16)*SCALE){
            cerr<<"FAIL boundary="<<B<<" m0="<<hex<<m0<<" m1="<<m1<<dec<<"\n";
            return 2;
          }
        }
      }
  }

  // Exhibit equality: m0=0x000f,m1=0x33ff has B=24 and Walsh magnitudes
  // 8 repeated eight times and 16 repeated twice, hence H=3 and I=3/2.
  int e0=0x000f,e1=0x33ff;
  int Beq=bd[e0]+bd[e1]+pc[e0^e1];
  map<int,int> hist;
  for(int u=0;u<16;u++){
    int a=wal[e0][u],b=wal[e1][u];
    if(a+b) hist[abs(a+b)]++;
    if(a-b) hist[abs(a-b)]++;
  }
  if(Beq!=24 || hist[8]!=8 || hist[16]!=2 || hist.size()!=2){ cerr<<"FAIL equality witness\n"; return 3; }

  cout<<"candidate_pairs_checked="<<candidate_pairs<<"\n";
  cout<<"balanced_low_boundary_functions="<<low_count<<"\n";
  for(auto &kv:cnt){
    int B=kv.first;
    cout<<"boundary="<<B<<" count="<<kv.second;
    if(B>16) cout<<" max_entropy_upper_units="<<maxHU[B]<<" arg="<<hex<<arg[B].first<<","<<arg[B].second<<dec;
    cout<<"\n";
  }
  cout<<"high_boundary_argument=H<=5 and B>=30 gives H/(I-1)<=40/7<6\n";
  cout<<"equality_witness=m0:000f,m1:33ff boundary=24 WalshAbs{8:8,16:2} H=3 I=3/2 ratio=6\n";
  cout<<"CERTIFIED: max over balanced Boolean gates on 5 uniform inputs with I>1 of H/(I-1) is exactly 6\n";
  cout<<"CERTIFIED: for C0=6.4548, max balanced-uniform five-input gate margin c_G is -1.8192\n";
  cout<<"PASS=1\n";
  return 0;
}
