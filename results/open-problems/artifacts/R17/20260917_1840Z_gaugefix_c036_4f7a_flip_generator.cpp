#include <bits/stdc++.h>
using namespace std;
static inline uint32_t pack4(uint8_t x,uint8_t y,uint8_t dx,uint8_t dy){return (uint32_t)x|((uint32_t)y<<8)|((uint32_t)dx<<16)|((uint32_t)dy<<24);} 
static inline void unpack4(uint32_t s,uint8_t &x,uint8_t &y,uint8_t &dx,uint8_t &dy){x=s&255;y=(s>>8)&255;dx=(s>>16)&255;dy=(s>>24)&255;}
struct FastMap{
    static constexpr uint32_t LG=24, SZ=1u<<LG, MASK=SZ-1;
    vector<uint64_t> tab; FastMap():tab(SZ,0){}
    static inline uint32_t hs(uint32_t x){x^=x>>16;x*=0x7feb352dU;x^=x>>15;x*=0x846ca68bU;x^=x>>16;return x;}
    inline uint32_t get(uint32_t key) const {uint32_t p=hs(key)&MASK;uint64_t tag=(uint64_t(key)+1)<<32;for(;;){uint64_t z=tab[p];if(!z)return 0;if((z&0xffffffff00000000ULL)==tag)return uint32_t(z);p=(p+1)&MASK;}}
    inline uint32_t put_if_absent(uint32_t key,uint32_t val,bool &inserted){uint32_t p=hs(key)&MASK;uint64_t tag=(uint64_t(key)+1)<<32;for(;;){uint64_t &z=tab[p];if(!z){z=tag|val;inserted=true;return val;}if((z&0xffffffff00000000ULL)==tag){inserted=false;return uint32_t(z);}p=(p+1)&MASK;}}
};
struct TC{int h;uint8_t mask;TC(int H):h(H),mask((1u<<H)-1){}
 pair<uint32_t,int> reduce(uint32_t s) const {uint8_t x,y,dx,dy;unpack4(s,x,y,dx,dy);int flip=!!(x&(1u<<(h-1)));if(flip){x^=mask;y^=mask;}return {pack4(x,y,dx,dy),flip};}
 bool trans(uint32_t s,int c,int l,uint32_t &out,int &flip) const {uint8_t x,y,dx,dy;unpack4(s,x,y,dx,dy);int ta=l>=0?l+1:1,tb=l<0?-l+1:1,na=h+ta,nb=h+tb;int16_t L[17][17]; L[h][h]=h;int cur=h;for(int k=h-1;k>=0;--k){cur-=(dx>>(h-1-k))&1;L[k][h]=cur;}cur=h;for(int k=h-1;k>=0;--k){cur-=(dy>>(h-1-k))&1;L[h][k]=cur;}
 auto achar=[&](int i){if(i<=h)return int((x>>(h-i))&1);int q=i-h-1;if(l>=0)return q<l?1-c:c;return c;};auto bchar=[&](int j){if(j<=h)return int((y>>(h-j))&1);int q=j-h-1;if(l<0)return q<(-l)?1-c:c;return c;};
 for(int i=0;i<=na;i++)for(int j=0;j<=nb;j++)if(i>h||j>h){if(i==0)L[i][j]=L[i][j-1];else if(j==0)L[i][j]=L[i-1][j];else if(achar(i)==bchar(j))L[i][j]=L[i-1][j-1]+1;else L[i][j]=max(L[i][j-1],L[i-1][j]);}
 int i=na,j=nb;while(i>=h&&j>=h){if(L[i][j]==L[i-1][j])--i;else if(L[i][j]==L[i][j-1])--j;else{--i;--j;}if(i==h&&j==h){uint8_t xs=x,ys=y;if(l>=0){for(int q=0;q<l;q++)xs=((xs<<1)|(1-c))&mask;xs=((xs<<1)|c)&mask;ys=((ys<<1)|c)&mask;}else{xs=((xs<<1)|c)&mask;for(int q=0;q<-l;q++)ys=((ys<<1)|(1-c))&mask;ys=((ys<<1)|c)&mask;}uint8_t ndx=0,ndy=0;for(int k=na-h+1;k<=na;k++)ndx=(ndx<<1)|(L[k][nb]-L[k-1][nb]);for(int k=nb-h+1;k<=nb;k++)ndy=(ndy<<1)|(L[na][k]-L[na][k-1]);auto r=reduce(pack4(xs,ys,ndx,ndy));out=r.first;flip=r.second;return true;}}return false;}
};
int main(int argc,char**argv){int h=argc>1?atoi(argv[1]):8;string out=argc>2?argv[2]:"/mnt/data/r17_h8_flip.bin";TC tc(h);uint8_t mask=(1u<<h)-1;auto sr=tc.reduce(pack4(0,0,mask,mask));uint32_t start=sr.first;FastMap idx;vector<uint32_t>states;states.reserve(7000000);states.push_back(start);bool ins;idx.put_if_absent(start,1,ins);FILE*fp=fopen(out.c_str(),"wb");if(!fp){perror("fopen");return 2;}size_t head=0;while(head<states.size()){uint32_t s=states[head++];for(int c=0;c<2;c++)for(int l=-(h-1);l<=h-1;l++){uint32_t t=0,ti=0;int fl=0;if(tc.trans(s,c,l,t,fl)){uint32_t newidx=(uint32_t)states.size()+1;ti=idx.put_if_absent(t,newidx,ins);if(ins)states.push_back(t);if(fl)ti|=0x80000000u;}fwrite(&ti,4,1,fp);}if(head%1000000==0)cerr<<"head="<<head<<" states="<<states.size()<<"\n";}fclose(fp);cout<<"h="<<h<<" states="<<states.size()<<"\n";return 0;}
