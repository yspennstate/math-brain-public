#include <bits/stdc++.h>
using namespace std;

static int discrepancy(const vector<string>& rows){
    int m=(int)rows.size(), n=(int)rows[0].size();
    vector<vector<int>> A(m, vector<int>(n));
    for(int i=0;i<m;i++) for(int j=0;j<n;j++) A[i][j]=(rows[i][j]=='+')?1:-1;
    vector<int> x(n,1), sums(m,0);
    for(int i=0;i<m;i++) for(int j=0;j<n;j++) sums[i]+=A[i][j];
    auto infnorm=[&](){int z=0; for(int v:sums) z=max(z,abs(v)); return z;};
    int best=infnorm();
    uint32_t prev=0, lim=1u<<(n-1); // global sign: fix last coordinate +1
    for(uint32_t t=1;t<lim;t++){
        uint32_t g=t^(t>>1), diff=g^prev;
        int j=__builtin_ctz(diff), old=x[j];
        x[j]=-old;
        for(int i=0;i<m;i++) sums[i]-=2*old*A[i][j];
        best=min(best,infnorm());
        prev=g;
    }
    return best;
}

int main(){
    // Orrick--Solomon--Dowdeswell--Smith (2003), printed order-22 record matrix.
    vector<string> M={
      "++-----++++++++++-----",
      "++-----+++++-----+++++",
      "--+----+----++-----+-+",
      "---+----+----++--+--+-",
      "----+----+--+---+-+-+-",
      "-----+----+---++--+--+",
      "------+----+---+++-+--",
      "+++----+------+-+++---",
      "++-+----+---+--+--++--",
      "++--+----+---+-+-+---+",
      "++---+----+--+--+--++-",
      "++----+----++-+-----++",
      "+---+++++-+-+----+----",
      "+-+--++-++-+-+----+---",
      "+--+++-+-+-+--+----+--",
      "+-++--++-++----+----+-",
      "+-+++---+-++----+----+",
      "-+++-+---++++----+----",
      "-+-++-++--++-+----+---",
      "-++-+-+-+++---+----+--",
      "-++-++-++--+---+----+-",
      "-+-+-+++++------+----+"
    };
    for(auto&s:M) if(s.size()!=22){cerr<<"bad matrix row length\n"; return 2;}
    int dm=discrepancy(M);
    cout<<"Orrick2003_order22_record_discrepancy="<<dm<<"\n";
    if(dm!=6) return 3;

    // Exact verification of the best complement-quotient n=22,r=7 search state found this run.
    const int n=22,r=7,d=21,N=1<<d;
    vector<int> centers={
      1287219,712289,650751,343937,1660710,68218,1465810,1086453,
      1972399,1018132,311563,214685,1140805,140652,1934536,553136,
      2061177,516838,1375804,796247,1747850,241742
    };
    vector<int> S; S.reserve(300000);
    for(int x=0;x<N;x++){
        int w=__builtin_popcount((unsigned)x);
        if(w<=r || w>=n-r) S.push_back(x);
    }
    vector<unsigned char> covered(N,0);
    for(int c:centers) for(int s:S) covered[c^s]=1;
    int uncovered=0; for(auto z:covered) if(!z) uncovered++;
    cout<<"n22_r7_folded_ball_size="<<S.size()<<"\n";
    cout<<"n22_22center_uncovered="<<uncovered<<"\n";
    if((int)S.size()!=280600 || uncovered!=1257) return 4;

    // Exact comparison: a zero-residual (22,44,7) antipodal cover would imply disc >=8.
    // 8/sqrt(22) > 7/sqrt(17) iff 64*17 > 49*22.
    long long lhs=64LL*17, rhs=49LL*22;
    cout<<"ratio_crosscheck_64x17="<<lhs<<"_49x22="<<rhs<<"\n";
    if(!(lhs>rhs)) return 5;

    cout<<"ALL EXACT CHECKS PASS\n";
    cout<<"NOTE: residual 1257 is search diagnostic only; nonzero residual is NOT a nonexistence proof.\n";
}
