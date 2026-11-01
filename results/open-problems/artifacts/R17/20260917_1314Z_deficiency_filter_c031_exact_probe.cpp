#include <bits/stdc++.h>
using namespace std;
static inline uint32_t pack4(uint8_t x,uint8_t y,uint8_t dx,uint8_t dy){return (uint32_t)x|((uint32_t)y<<8)|((uint32_t)dx<<16)|((uint32_t)dy<<24);} 
static inline void unpack4(uint32_t s,uint8_t &x,uint8_t &y,uint8_t &dx,uint8_t &dy){x=s&255;y=(s>>8)&255;dx=(s>>16)&255;dy=(s>>24)&255;}
struct TC{int h;uint8_t mask;TC(int H):h(H),mask((1u<<H)-1){}
 uint32_t reduce(uint32_t s)const{uint8_t x,y,dx,dy;unpack4(s,x,y,dx,dy);if(x&(1u<<(h-1))){x^=mask;y^=mask;}return pack4(x,y,dx,dy);} 
 uint32_t trans(uint32_t s,int c,int l)const{uint8_t x,y,dx,dy;unpack4(s,x,y,dx,dy);int ta=l>=0?l+1:1,tb=l<0?-l+1:1,na=h+ta,nb=h+tb;int16_t L[17][17];L[h][h]=h;int cur=h;for(int k=h-1;k>=0;--k){cur-=(dx>>(h-1-k))&1;L[k][h]=cur;}cur=h;for(int k=h-1;k>=0;--k){cur-=(dy>>(h-1-k))&1;L[h][k]=cur;}
 auto ac=[&](int i){if(i<=h)return int((x>>(h-i))&1);int q=i-h-1;if(l>=0)return q<l?1-c:c;return c;}; auto bc=[&](int j){if(j<=h)return int((y>>(h-j))&1);int q=j-h-1;if(l<0)return q<(-l)?1-c:c;return c;};
 for(int i=0;i<=na;i++)for(int j=0;j<=nb;j++)if(i>h||j>h){if(i==0)L[i][j]=L[i][j-1];else if(j==0)L[i][j]=L[i-1][j];else if(ac(i)==bc(j))L[i][j]=L[i-1][j-1]+1;else L[i][j]=max(L[i][j-1],L[i-1][j]);}
 int i=na,j=nb;while(i>=h&&j>=h){if(L[i][j]==L[i-1][j])--i;else if(L[i][j]==L[i][j-1])--j;else{--i;--j;}if(i==h&&j==h){uint8_t xs=x,ys=y;if(l>=0){for(int q=0;q<l;q++)xs=((xs<<1)|(1-c))&mask;xs=((xs<<1)|c)&mask;ys=((ys<<1)|c)&mask;}else{xs=((xs<<1)|c)&mask;for(int q=0;q<-l;q++)ys=((ys<<1)|(1-c))&mask;ys=((ys<<1)|c)&mask;}uint8_t ndx=0,ndy=0;for(int k=na-h+1;k<=na;k++)ndx=(ndx<<1)|(L[k][nb]-L[k-1][nb]);for(int k=nb-h+1;k<=nb;k++)ndy=(ndy<<1)|(L[na][k]-L[na][k-1]);return reduce(pack4(xs,ys,ndx,ndy));}}
 return UINT32_MAX;}
};
struct Par{int p,c,l;};
int main(){const int h=8;TC tc(h);uint32_t start=tc.reduce(pack4(0,0,255,255));unordered_map<uint32_t,int> idx;idx.reserve(10000);vector<uint32_t> st{start};vector<Par> par{{-1,-1,0}};idx[start]=0;size_t head=0;
 while(head<st.size() && head<10000){int si=head;uint32_t s=st[head++];for(int c=0;c<2;c++)for(int l=-7;l<=7;l++){uint32_t t=tc.trans(s,c,l);if(t==UINT32_MAX)continue;int ti;auto it=idx.find(t);if(it==idx.end()){ti=st.size();idx[t]=ti;st.push_back(t);par.push_back({si,c,l});}else ti=it->second;
   if(abs(l)==2){uint32_t u=tc.trans(t,c,-l);if(u!=UINT32_MAX){vector<pair<int,int>> path;int q=si;while(q>0){path.push_back({par[q].c,par[q].l});q=par[q].p;}reverse(path.begin(),path.end());path.push_back({c,l});path.push_back({c,-l});
      cout<<"R17-C031 exact finite recovery probe\n";
      cout<<"base_history=8\n";
      cout<<"processed_base_states_before_witness="<<head<<"\n";
      cout<<"discovered_base_states_at_witness="<<st.size()<<"\n";
      cout<<"witness_source_state="<<s<<"\n";
      cout<<"witness_mid_state="<<t<<"\n";
      cout<<"witness_dest_state="<<u<<"\n";
      cout<<"deficient_block=(c="<<c<<",l="<<l<<") then (c="<<c<<",l="<<-l<<")\n";
      cout<<"prefix_path_labels=";for(size_t z=0;z<path.size();z++){if(z)cout<<" ";cout<<"("<<path[z].first<<","<<path[z].second<<")";}cout<<"\n";
      auto mk=[&](int cc,int ll){string A,B; if(ll>=0){A=string(ll, char('0'+(1-cc)))+char('0'+cc);B=string(1,char('0'+cc));}else{A=string(1,char('0'+cc));B=string(-ll,char('0'+(1-cc)))+char('0'+cc);}return pair<string,string>{A,B};};
      auto a=mk(c,l),b=mk(c,-l);string X=a.first+b.first,Y=a.second+b.second;
      auto lcs=[&](const string&A,const string&B){vector<int>d(B.size()+1);for(char x:A){int prev=0;for(size_t j=1;j<=B.size();j++){int old=d[j];if(x==B[j-1])d[j]=prev+1;else d[j]=max(d[j],d[j-1]);prev=old;}}return d.back();};
      cout<<"block_top="<<X<<" block_bottom="<<Y<<" block_order=2 block_lcs="<<lcs(X,Y)<<"\n";
      if(lcs(X,Y)!=3){cerr<<"deficiency verification failed\n";return 4;}
      cout<<"CANONICAL_MACHINE_ACCEPTS_DEFICIENT_LENGTH2_BLOCK=PASS\n";
      cout<<"EXACT_FINITE_RECOVERY_CHECK_PASS\n";
      return 0;
   }}
 }
 }
 cerr<<"no witness found in first 10000 base states\n";return 5;
}
