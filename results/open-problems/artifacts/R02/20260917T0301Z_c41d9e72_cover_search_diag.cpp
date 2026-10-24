#include <bits/stdc++.h>
using namespace std; using ll=long long;
static void fwht(vector<ll>&a,bool inv=false){
 int n=a.size();
 for(int len=1;2*len<=n;len<<=1)
  for(int i=0;i<n;i+=2*len)
   for(int j=0;j<len;j++){ll u=a[i+j],v=a[i+j+len];a[i+j]=u+v;a[i+j+len]=u-v;}
 if(inv) for(auto &x:a)x/=n;
}
static void run(int n,int r){
 int d=n-1,N=1<<d,m=n;
 vector<int>S; vector<ll> shat(N);
 for(int x=0;x<N;x++){int w=__builtin_popcount((unsigned)x);if(w<=r||w>=n-r){S.push_back(x);shat[x]=1;}}
 fwht(shat);
 vector<unsigned short> cnt(N,0); vector<int> centers;
 auto add=[&](int c,int delta){for(int s:S)cnt[c^s]+=delta;};
 auto rem=[&](){int q=0;for(auto z:cnt)if(!z)q++;return q;};
 for(int step=0;step<m;step++){
   vector<ll> u(N);for(int x=0;x<N;x++)if(!cnt[x])u[x]=1;
   fwht(u);for(int x=0;x<N;x++)u[x]*=shat[x];fwht(u,true);
   int c=max_element(u.begin(),u.end())-u.begin();
   centers.push_back(c);add(c,1);
 }
 int greedy=rem(),last=greedy,sweeps=0;
 for(;sweeps<10;sweeps++){
   int before=rem();
   for(int i=0;i<m;i++){
     add(centers[i],-1);
     vector<ll> u(N);for(int x=0;x<N;x++)if(!cnt[x])u[x]=1;
     fwht(u);for(int x=0;x<N;x++)u[x]*=shat[x];fwht(u,true);
     int c=max_element(u.begin(),u.end())-u.begin();
     centers[i]=c;add(c,1);
   }
   int after=rem();
   last=after;
   if(after>=before){sweeps++;break;}
 }
 cout<<"n="<<n<<" r="<<r<<" |S|="<<S.size()
     <<" greedy_uncovered="<<greedy<<" coordinate_uncovered="<<last
     <<" sweeps="<<sweeps<<"\n";
 cout<<"centers";
 for(int c:centers)cout<<" "<<c;
 cout<<"\n";
}
int main(){
 run(18,5);
 run(20,6);
 run(22,7);
 cout<<"DIAGNOSTIC COMPLETE -- nonzero residual is NOT an impossibility proof\n";
}
