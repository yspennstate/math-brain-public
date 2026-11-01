#include <bits/stdc++.h>
using namespace std;

static inline uint32_t pack4(uint8_t x,uint8_t y,uint8_t dx,uint8_t dy){
    return (uint32_t)x | ((uint32_t)y<<8) | ((uint32_t)dx<<16) | ((uint32_t)dy<<24);
}
static inline void unpack4(uint32_t s,uint8_t &x,uint8_t &y,uint8_t &dx,uint8_t &dy){
    x=s&255; y=(s>>8)&255; dx=(s>>16)&255; dy=(s>>24)&255;
}
struct TC {
    static constexpr int h=8; static constexpr uint8_t mask=255;
    pair<uint32_t,int> reduce_with_flip(uint32_t s) const {
        uint8_t x,y,dx,dy; unpack4(s,x,y,dx,dy); int f=0;
        if(x&128){x^=mask;y^=mask;f=1;} return {pack4(x,y,dx,dy),f};
    }
    tuple<bool,uint32_t,int> trans(uint32_t s,int c,int l) const {
        uint8_t x,y,dx,dy;unpack4(s,x,y,dx,dy);
        int ta=l>=0?l+1:1,tb=l<0?-l+1:1,na=h+ta,nb=h+tb;
        int16_t L[17][17]{}; L[h][h]=h; int cur=h;
        for(int k=h-1;k>=0;--k){cur-=(dx>>(h-1-k))&1;L[k][h]=cur;}
        cur=h;for(int k=h-1;k>=0;--k){cur-=(dy>>(h-1-k))&1;L[h][k]=cur;}
        auto A=[&](int i){if(i<=h)return int((x>>(h-i))&1);int q=i-h-1;return l>=0?(q<l?1-c:c):c;};
        auto B=[&](int j){if(j<=h)return int((y>>(h-j))&1);int q=j-h-1;return l<0?(q<-l?1-c:c):c;};
        for(int i=0;i<=na;i++)for(int j=0;j<=nb;j++)if(i>h||j>h){
            if(i==0)L[i][j]=L[i][j-1]; else if(j==0)L[i][j]=L[i-1][j];
            else if(A(i)==B(j))L[i][j]=L[i-1][j-1]+1; else L[i][j]=max(L[i][j-1],L[i-1][j]);
        }
        int i=na,j=nb;while(i>=h&&j>=h){
            if(L[i][j]==L[i-1][j])--i; else if(L[i][j]==L[i][j-1])--j; else {--i;--j;}
            if(i==h&&j==h){
                uint8_t xs=x,ys=y;if(l>=0){for(int q=0;q<l;q++)xs=((xs<<1)|(1-c))&mask;xs=((xs<<1)|c)&mask;ys=((ys<<1)|c)&mask;}
                else {xs=((xs<<1)|c)&mask;for(int q=0;q<-l;q++)ys=((ys<<1)|(1-c))&mask;ys=((ys<<1)|c)&mask;}
                uint8_t ndx=0,ndy=0;for(int k=na-h+1;k<=na;k++)ndx=(ndx<<1)|(L[k][nb]-L[k-1][nb]);
                for(int k=nb-h+1;k<=nb;k++)ndy=(ndy<<1)|(L[na][k]-L[na][k-1]);
                auto [t,f]=reduce_with_flip(pack4(xs,ys,ndx,ndy)); return {true,t,f};
            }
        }
        return {false,0,0};
    }
};

static int lcs(const vector<int>&a,const vector<int>&b){
    vector<int>d(b.size()+1);for(int x:a){int prev=0;for(size_t j=1;j<=b.size();j++){int old=d[j];d[j]=(x==b[j-1])?prev+1:max(d[j],d[j-1]);prev=old;}}return d.back();
}
static pair<vector<int>,vector<int>> build(const vector<pair<int,int>>&w){
    vector<int>a,b;for(auto [c,l]:w){int d=1-c;if(l>=0){for(int q=0;q<l;q++)a.push_back(d);a.push_back(c);b.push_back(c);}else{a.push_back(c);for(int q=0;q<-l;q++)b.push_back(d);b.push_back(c);}}return {a,b};
}

int main(){
    TC tc; auto [start,ff]=tc.reduce_with_flip(pack4(0,0,255,255)); if(ff) return 1;
    vector<pair<int,int>> first={{1,-1},{1,1}};
    vector<int> z={1,0,0,0,0,0,0,0};
    vector<uint32_t> finals;
    for(auto f:first){
        auto [ok,s,g]=tc.trans(start,f.first,f.second); if(!ok){cerr<<"first transition invalid\n";return 2;}
        uint32_t after_first=s;
        for(int c:z){auto [ok2,t,fl]=tc.trans(s,c,0); if(!ok2){cerr<<"zero hook invalid\n";return 3;} s=t;}
        finals.push_back(s);
        uint8_t x,y,dx,dy;unpack4(s,x,y,dx,dy);
        cout<<"first=("<<f.first<<","<<f.second<<") after_first=0x"<<hex<<setw(8)<<setfill('0')<<after_first
            <<" final=0x"<<setw(8)<<s<<dec<<setfill(' ')<<" unpack=("<<int(x)<<","<<int(y)<<","<<int(dx)<<","<<int(dy)<<")\n";
    }
    if(finals[0]==finals[1]){cerr<<"unexpected synchronization\n";return 4;}
    cout<<"EXACT_EIGHT_ZERO_HOOK_FIXED_WORD_NOT_SYNCHRONIZING_PASS\n";

    // Verify the simple seven-factor deficient word used in the attempted universal completion.
    vector<pair<int,int>> W={{0,-1},{0,1},{0,0},{0,0},{0,0},{0,0},{1,1}};
    auto [A,B]=build(W); int L=lcs(A,B); auto [Ap,Bp]=build(vector<pair<int,int>>(W.begin(),W.begin()+6));
    auto [As,Bs]=build(vector<pair<int,int>>(W.begin()+1,W.end())); int Lp=lcs(Ap,Bp),Ls=lcs(As,Bs);
    cout<<"candidate_W_lcs="<<L<<" prefix6_lcs="<<Lp<<" suffix6_lcs="<<Ls<<"\n";
    if(!(L==8&&Lp==6&&Ls==6)){cerr<<"candidate deficiency check failed\n";return 5;}
    cout<<"EXACT_MINIMAL_SEVEN_DEFICIENCY_WITNESS_PASS\n";
    cout<<"ALL_EXACT_CHECKS_PASS\n";
}
