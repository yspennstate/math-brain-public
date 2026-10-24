#include <bits/stdc++.h>
using namespace std;
struct DSU{int p[8]; DSU(){iota(p,p+8,0);} int f(int x){while(p[x]!=x){p[x]=p[p[x]];x=p[x];}return x;} bool un(int a,int b){a=f(a);b=f(b);if(a==b)return false;p[a]=b;return true;}};
int main(){
 vector<pair<int,int>> E;
 E.push_back({0,1});E.push_back({0,2});E.push_back({1,2});
 for(int t=0;t<3;t++)for(int x=3;x<8;x++)E.push_back({t,x});
 E.push_back({3,4}); E.push_back({3,5}); E.push_back({3,6}); E.push_back({6,7});
 int m=E.size(); if(m!=22){cerr<<m<<"\n";return 2;}
 unsigned long long Z=0; vector<unsigned long long>A(m), B(m*m);
 uint32_t M=1u<<m;
 for(uint32_t mask=0;mask<M;mask++){
   if(__builtin_popcount(mask)>7) continue;
   DSU d; bool ok=true; int bits[8],k=0;
   uint32_t z=mask;
   while(z){int i=__builtin_ctz(z);z&=z-1; auto [a,b]=E[i]; if(!d.un(a,b)){ok=false;break;} bits[k++]=i;}
   if(!ok) continue;
   Z++;
   for(int a=0;a<k;a++) A[bits[a]]++;
   for(int a=0;a<k;a++)for(int b=a+1;b<k;b++){int i=bits[a],j=bits[b];B[i*m+j]++;B[j*m+i]++;}
 }
 __int128 ming=-1,maxg=0; int mi=-1,mj=-1;
 auto print128=[](__int128 x){ if(x==0){cout<<0;return;} string s; while(x){s.push_back('0'+x%10);x/=10;} reverse(s.begin(),s.end()); cout<<s;};
 for(int i=0;i<m;i++)for(int j=i+1;j<m;j++){
   __int128 g=(__int128)A[i]*A[j]-(__int128)Z*B[i*m+j];
   if(ming<0||g<ming){ming=g;mi=i;mj=j;} if(g>maxg)maxg=g;
 }
 cout<<"GRAPH=K3_vee_D_2_1 vertices=8 edges="<<m<<"\n";
 cout<<"FORESTS="<<Z<<"\nMIN_GAP=";print128(ming);cout<<" pair="<<mi<<","<<mj<<"\nMAX_GAP=";print128(maxg);cout<<"\n";
 if(ming<=0){cout<<"FAIL\n";return 1;} cout<<"BRUTE_FORCE_PASS\n";
}
