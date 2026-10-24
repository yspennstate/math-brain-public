#include <bits/stdc++.h>
using namespace std;

static const char* H16_HEX[5] = {
"FFFF FF00 F0F0 F00F CCCC CC33 C3C3 C33C AAAA AA55 A5A5 A55A 9999 9966 9696 9669",
"FFFF FF00 F0F0 F00F CCCC CC33 C3C3 C33C AAAA AA55 A5A5 A55A 9996 9969 9699 9666",
"FFFF FF00 F0F0 F00F CCCC CC33 C3C3 C33C AAAA AA55 A599 A566 9996 9969 96A5 965A",
"FFFF FF00 F0F0 F00F CCCC CC33 C3C3 C33C AAAA A995 A659 A566 9A56 9969 96A5 959A",
"FFFF FF00 F0F0 F00F CCCC CC33 C3AA C355 AAC3 AA3C A599 A566 9996 9969 96A5 965A"
};

vector<vector<int>> parse_hex(const string& line, int n){
    stringstream ss(line); string h; vector<vector<int>> A;
    while(ss>>h){
        unsigned long long x=stoull(h,nullptr,16);
        vector<int> r(n);
        for(int j=0;j<n;j++) r[j]=((x>>(n-1-j))&1ULL)?1:-1;
        A.push_back(r);
    }
    return A;
}

int discrepancy(const vector<vector<int>>& A, unsigned long long* arg=nullptr){
    int m=A.size(), n=A[0].size();
    if(n>=63) throw runtime_error("too many columns");
    vector<int> s(m,0);
    for(int i=0;i<m;i++) for(int j=0;j<n;j++) s[i]+=A[i][j];
    // disc(Ax)=disc(A(-x)), so fix the final sign to +1 and enumerate the
    // other n-1 signs exactly in Gray-code order.
    unsigned long long total=1ULL<<(n-1), prevg=0, bestg=0;
    int best=INT_MAX;
    for(unsigned long long k=0;k<total;k++){
        unsigned long long g=k^(k>>1);
        if(k){
            unsigned long long diff=g^prevg;
            int j=__builtin_ctzll(diff);
            int delta=((g>>j)&1ULL)?-2:+2;
            for(int i=0;i<m;i++) s[i]+=delta*A[i][j];
        }
        prevg=g;
        int mx=0;
        for(int v:s) mx=max(mx,abs(v));
        if(mx<best){best=mx;bestg=g;}
    }
    if(arg) *arg=bestg;
    return best;
}

bool is_hadamard(const vector<vector<int>>& H){
    int n=H.size(); if((int)H[0].size()!=n) return false;
    for(int i=0;i<n;i++) for(int j=0;j<n;j++){
        int s=0; for(int k=0;k<n;k++) s+=H[i][k]*H[j][k];
        if(s!=(i==j?n:0)) return false;
    }
    return true;
}

vector<vector<int>> puncture(const vector<vector<int>>& H,int del){
    int m=H.size(), n=H[0].size(); vector<vector<int>> P(m);
    for(int i=0;i<m;i++) for(int j=0;j<n;j++) if(j!=del) P[i].push_back(H[i][j]);
    return P;
}

vector<vector<int>> pad_ones(const vector<vector<int>>& P,int t){
    auto A=P; for(auto& r:A) for(int z=0;z<t;z++) r.push_back(1); return A;
}

vector<vector<int>> square_by_duplicate_rows(vector<vector<int>> A){
    int n=A[0].size();
    while((int)A.size()<n) A.push_back(A[(A.size()-1)%A.size()]);
    if((int)A.size()!=n) throw runtime_error("cannot square by row duplication");
    return A;
}

int main(){
    cout << "R02 I0095 order-16 Hadamard class scan\n";
    vector<vector<vector<int>>> Hs;
    for(int c=0;c<5;c++){
        auto H=parse_hex(H16_HEX[c],16);
        if(H.size()!=16 || !is_hadamard(H)){cerr<<"bad H16 class "<<c<<"\n";return 2;}
        Hs.push_back(H);
        int dfull=discrepancy(H);
        map<int,int> punct_hist, pad_hist;
        for(int del=0;del<16;del++){
            auto P=puncture(H,del);
            int dp=discrepancy(P); punct_hist[dp]++;
            auto A17=square_by_duplicate_rows(pad_ones(P,2));
            int d17=discrepancy(A17); pad_hist[d17]++;
        }
        cout<<"class="<<c<<" full="<<dfull<<" puncture_hist=";
        for(auto [d,k]:punct_hist) cout<<d<<":"<<k<<",";
        cout<<" padded17_hist=";
        for(auto [d,k]:pad_hist) cout<<d<<":"<<k<<",";
        cout<<"\n";
    }
    // The fourth public equivalence-class representative (index 3), any puncture.
    auto P=puncture(Hs[3],0);
    auto A17=square_by_duplicate_rows(pad_ones(P,2));
    unsigned long long arg=0;
    int d17=discrepancy(A17,&arg);
    if(d17!=7){cerr<<"certificate failed: d17="<<d17<<"\n";return 3;}
    if(49*9<=25*17){cerr<<"ratio comparison failed\n";return 4;}
    cout<<"CERT class=3 delete_col=0 n=17 discrepancy="<<d17
        <<" argmask="<<arg<<" ratio^2=49/17 old_ratio^2=25/9 cross=441>425\n";

    // Method #6: deform the same puncture by t identical all-one columns.
    // For n>=16 duplicate existing rows until square; row duplication leaves discrepancy unchanged.
    cout<<"deformation t:n:disc\n";
    for(int t=1;t<=6;t++){
        auto A=square_by_duplicate_rows(pad_ones(P,t));
        int d=discrepancy(A);
        cout<<t<<":"<<A.size()<<":"<<d<<"\n";
    }
    cout<<"ALL EXACT CHECKS PASS\n";
}
