#include <bits/stdc++.h>
using namespace std;
static inline uint32_t pack4(uint8_t x,uint8_t y,uint8_t dx,uint8_t dy){return (uint32_t)x|((uint32_t)y<<8)|((uint32_t)dx<<16)|((uint32_t)dy<<24);} 
static inline void unpack4(uint32_t s,uint8_t &x,uint8_t &y,uint8_t &dx,uint8_t &dy){x=s&255;y=(s>>8)&255;dx=(s>>16)&255;dy=(s>>24)&255;}
struct TC{
  int h; uint8_t mask;
  TC(int H):h(H),mask((1u<<H)-1){}
  pair<uint32_t,int> reduce(uint32_t s)const{uint8_t x,y,dx,dy;unpack4(s,x,y,dx,dy);int flip=!!(x&(1u<<(h-1)));if(flip){x^=mask;y^=mask;}return{pack4(x,y,dx,dy),flip};}
  bool trans(uint32_t s,int c,int l,uint32_t &out,int &flip)const{
    uint8_t x,y,dx,dy;unpack4(s,x,y,dx,dy);int ta=l>=0?l+1:1,tb=l<0?-l+1:1,na=h+ta,nb=h+tb;int16_t L[17][17];
    L[h][h]=h;int cur=h;for(int k=h-1;k>=0;--k){cur-=(dx>>(h-1-k))&1;L[k][h]=cur;}cur=h;for(int k=h-1;k>=0;--k){cur-=(dy>>(h-1-k))&1;L[h][k]=cur;}
    auto achar=[&](int i){if(i<=h)return int((x>>(h-i))&1);int q=i-h-1;if(l>=0)return q<l?1-c:c;return c;};
    auto bchar=[&](int j){if(j<=h)return int((y>>(h-j))&1);int q=j-h-1;if(l<0)return q<(-l)?1-c:c;return c;};
    for(int i=0;i<=na;i++)for(int j=0;j<=nb;j++)if(i>h||j>h){if(i==0)L[i][j]=L[i][j-1];else if(j==0)L[i][j]=L[i-1][j];else if(achar(i)==bchar(j))L[i][j]=L[i-1][j-1]+1;else L[i][j]=max(L[i][j-1],L[i-1][j]);}
    int i=na,j=nb;while(i>=h&&j>=h){if(L[i][j]==L[i-1][j])--i;else if(L[i][j]==L[i][j-1])--j;else{--i;--j;}if(i==h&&j==h){uint8_t xs=x,ys=y;if(l>=0){for(int q=0;q<l;q++)xs=((xs<<1)|(1-c))&mask;xs=((xs<<1)|c)&mask;ys=((ys<<1)|c)&mask;}else{xs=((xs<<1)|c)&mask;for(int q=0;q<-l;q++)ys=((ys<<1)|(1-c))&mask;ys=((ys<<1)|c)&mask;}uint8_t ndx=0,ndy=0;for(int k=na-h+1;k<=na;k++)ndx=(ndx<<1)|(L[k][nb]-L[k-1][nb]);for(int k=nb-h+1;k<=nb;k++)ndy=(ndy<<1)|(L[na][k]-L[na][k-1]);auto r=reduce(pack4(xs,ys,ndx,ndy));out=r.first;flip=r.second;return true;}}
    return false;
  }
};
int main(){
  TC tc(8); const uint8_t mask=255; uint32_t start=tc.reduce(pack4(0,0,mask,mask)).first;
  vector<uint32_t> st{start}; vector<int> dep{0},par{-1},pc{-1},pl{0}; unordered_map<uint32_t,int> id; id[start]=0;
  size_t head=0;
  while(head<st.size() && head<1000000){
    uint32_t s=st[head]; int d=dep[head]; uint8_t x,y,dx,dy; unpack4(s,x,y,dx,dy);
    auto swr=tc.reduce(pack4(y,x,dy,dx)); uint32_t ss=swr.first; int e=swr.second;
    for(int c=0;c<2;c++) for(int l=-7;l<=7;l++){
      uint32_t t=0,t2=0; int f=0,f2=0; bool a=tc.trans(s,c,l,t,f); bool b=tc.trans(ss,c^e,-l,t2,f2);
      if(a!=b){
        vector<pair<int,int>> path; int z=(int)head; while(z>0){path.push_back({pc[z],pl[z]});z=par[z];} reverse(path.begin(),path.end());
        cout<<"R17 C040 exact swap-equivariance counterexample\n";
        cout<<"depth="<<d<<" state="<<s<<" x="<<int(x)<<" y="<<int(y)<<" dx="<<int(dx)<<" dy="<<int(dy)<<"\n";
        cout<<"label=("<<c<<","<<l<<") swap_normalization_flip="<<e<<" original_valid="<<a<<" swapped_valid="<<b<<"\n";
        cout<<"path="; for(auto [cc,ll]:path) cout<<"("<<cc<<","<<ll<<")"; cout<<"\n";
        const bool expected=(d==3 && s==100530178u && x==2 && y==248 && dx==253 && dy==5 && c==1 && l==1 && e==1 && a==true && b==false && path==vector<pair<int,int>>{{0,-7},{0,0},{0,1}});
        if(!expected){cout<<"UNEXPECTED_COUNTEREXAMPLE\n"; return 3;}
        cout<<"EXACT_SWAP_COUNTEREXAMPLE_PASS\nALL_EXACT_CHECKS_PASS\n"; return 0;
      }
      if(a && !id.count(t)){id[t]=(int)st.size();st.push_back(t);dep.push_back(d+1);par.push_back((int)head);pc.push_back(c);pl.push_back(l);}
    }
    head++;
  }
  cout<<"EXPECTED_COUNTEREXAMPLE_NOT_FOUND\n"; return 4;
}
