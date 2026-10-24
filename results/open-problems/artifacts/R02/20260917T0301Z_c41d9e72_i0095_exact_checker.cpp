#include <bits/stdc++.h>
using namespace std;

static vector<vector<int>> parseH(const string& line){
    stringstream ss(line); string tok; vector<vector<int>> H;
    while(ss>>tok){
        unsigned x=stoul(tok,nullptr,16);
        vector<int> r(20);
        for(int j=0;j<20;j++) r[j]=((x>>(19-j))&1)?1:-1;
        H.push_back(r);
    }
    if(H.size()!=20) throw runtime_error("bad row count");
    return H;
}
static bool hadamard20(const vector<vector<int>>& H){
    for(int i=0;i<20;i++)for(int j=0;j<20;j++){
        int s=0;for(int k=0;k<20;k++)s+=H[i][k]*H[j][k];
        if(s!=(i==j?20:0))return false;
    } return true;
}

// Exact discrepancy of an m x n sign matrix.
// Global signing symmetry fixes the last signing coordinate to +1.
// Gray code changes one of the first n-1 coordinates each step.
static int discrepancy(const vector<vector<int>>& A){
    int m=A.size(), n=A[0].size();
    if(n>25) throw runtime_error("too many cols");
    vector<int> sums(m,0);
    vector<int> x(n,1);
    for(int i=0;i<m;i++)for(int j=0;j<n;j++)sums[i]+=A[i][j];
    auto norm=[&](){int z=0;for(int v:sums)z=max(z,abs(v));return z;};
    int best=norm();
    unsigned prev=0, lim=1u<<(n-1);
    for(unsigned t=1;t<lim;t++){
        unsigned g=t^(t>>1), diff=g^prev;
        int j=__builtin_ctz(diff);
        int old=x[j]; x[j]=-old;
        for(int i=0;i<m;i++) sums[i]-=2*old*A[i][j];
        best=min(best,norm());
        prev=g;
    }
    return best;
}

static long long C(int n,int k){
    if(k<0||k>n)return 0;
    long long z=1;
    for(int i=1;i<=k;i++) z=z*(n-k+i)/i;
    return z;
}

int main(){
    // C002: exact order-17 sphere obstruction to discrepancy >= 9.
    long long V17_4=0;
    for(int k=0;k<=4;k++) V17_4+=C(17,k);
    long long cap=34*V17_4;
    long long cube=1LL<<17;
    cout<<"C002 V(17,4)="<<V17_4
        <<" 34*V="<<cap<<" 2^17="<<cube<<"\n";
    if(!(cap<cube)) return 2;

    vector<string> lines={
      "FFFFF FFC00 F83E0 F421E E3199 D3067 CC987 CC479 C2F54 C1EAA B0D4B AAA33 A94D6 A68EC A5725 9A68D 9993C 965B2 95AD1 8F34A",
      "FFFFF FFC00 F83E0 F421E E3199 D3067 CC987 CC479 C2F54 C1EAA B0D33 AAA4B A94D6 A66A5 A596C 9A8BC 9970D 965CA 95AD1 8F332",
      "FFFFF FFC00 F83E0 F421E E3199 D2947 CD0A7 CA47C C4F31 C1ECA B1473 AAA2B A8D96 A66C5 A596C 9C8D9 9970D 965AA 93AB4 8F352"
    };

    for(int cls=0;cls<3;cls++){
        auto H=parseH(lines[cls]);
        bool ok=hadamard20(H);
        cout<<"class "<<cls<<" hadamard="<<(ok?1:0);
        if(!ok)return 3;
        int dfull=discrepancy(H);
        cout<<" full_disc="<<dfull<<"\n";
        if(dfull!=6)return 4;

        int mn=99,mx=-1;
        for(int del=0;del<20;del++){
            vector<vector<int>> A(20, vector<int>(21));
            for(int i=0;i<20;i++){
                int q=0;
                for(int j=0;j<20;j++)if(j!=del)A[i][q++]=H[i][j];
                A[i][q++]=1;
                A[i][q++]=1;
            }
            int d=discrepancy(A);
            mn=min(mn,d);mx=max(mx,d);
            if(d!=7){
                cerr<<"unexpected puncture class "<<cls<<" del "<<del<<" disc "<<d<<"\n";
                return 5;
            }
        }
        cout<<"class "<<cls<<" 20/20 puncture+two-ones rectangular_disc=7"
            <<" min="<<mn<<" max="<<mx<<"\n";
    }
    cout<<"ALL EXACT CHECKS PASS\n";
}
