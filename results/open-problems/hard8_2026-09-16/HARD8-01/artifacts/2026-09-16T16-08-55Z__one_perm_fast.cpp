#include <bits/stdc++.h>
#include <omp.h>
using namespace std;
static int gcd_int(int a,int b){return b?gcd_int(b,a%b):a;}
static void gen_parts_rec(int rem,int mx,vector<int>&cur,vector<vector<int>>&out){if(!rem){out.push_back(cur);return;}for(int x=min(rem,mx);x>=1;--x){cur.push_back(x);gen_parts_rec(rem-x,x,cur,out);cur.pop_back();}}
static vector<int> canon(const vector<int>&parts){int n=accumulate(parts.begin(),parts.end(),0),base=0;vector<int>p(n);for(int l:parts){for(int i=0;i<l;i++)p[base+i]=base+(i+1)%l;base+=l;}return p;}
static string pstr(const vector<int>&v){string s;for(size_t i=0;i<v.size();++i){if(i)s+="+";s+=to_string(v[i]);}return s;}
static long long C(int n,int k){if(k<0||k>n)return 0;if(k>n-k)k=n-k;long long r=1;for(int i=1;i<=k;i++)r=r*(n-k+i)/i;return r;}

int main(int argc,char**argv){
 int n=argc>1?atoi(argv[1]):11; int q=argc>2?atoi(argv[2]):4;
 if(n<2||n>12||q<2||q>4)return 2;
 int M=1<<n, full=M-1,E=n*(n-1),sq=(n-1)*(n-1);
 vector<vector<int>> parts; vector<int>cur;gen_parts_rec(n,n,cur,parts);
 vector<array<int,2>> meta; for(int s=0;s<n;s++)for(int t=0;t<n;t++)if(s!=t)meta.push_back({s,t});
 vector<vector<uint16_t>> imap(E,vector<uint16_t>(M));
 for(int e=0;e<E;e++){int s=meta[e][0],t=meta[e][1];for(int m=0;m<M;m++){int u=m;if(m&(1<<s)){u&=~(1<<s);u|=1<<t;}imap[e][m]=u;}}
 struct GStat{long long tested=0,sync=0,viol=0,kt[4]={0,0,0,0},ks[4]={0,0,0,0},kv[4]={0,0,0,0};int maxrt=-1,km[4]={-1,-1,-1,-1};string desc,kdesc[4];} G;
 long long no_perm_count=0; for(int k=1;k<=q;k++)no_perm_count+=C(E,k);
 long long one_expected=(long long)parts.size()*([&](){long long z=0;for(int k=0;k<=q-1;k++)z+=C(E,k);return z;})();
 cout<<"HARD8_01_AT_MOST_ONE_PERM_FAST\nN "<<n<<" Q "<<q<<" PARTITIONS "<<parts.size()<<" IDEMPOTENTS "<<E<<"\n";
 cout<<"NO_PERM_SUPPORTS_THEOREM_COUNT "<<no_perm_count<<" SYNCHRONIZING 0 REASON q<n-1\n";
 cout<<"ONE_PERM_EXPECTED "<<one_expected<<"\n";
 for(auto &pa:parts){
   auto p=canon(pa);
   vector<uint16_t> pmap(M);
   for(int m=0;m<M;m++){int out=0,mm=m;while(mm){int b=__builtin_ctz((unsigned)mm);mm&=mm-1;out|=1<<p[b];}pmap[m]=out;}
   struct S{long long t=0,s=0,v=0,kt[4]={0},ks[4]={0},kv[4]={0};int mx=-1,km[4]={-1,-1,-1,-1};string d,kd[4];};
   int nth=omp_get_max_threads(); vector<S> ls(nth);
   auto bfs=[&](int i,int j,int h)->int{
     static thread_local vector<int> seen;
     static thread_local vector<uint16_t> qq;
     static thread_local int stamp=1;
     if((int)seen.size()!=M){seen.assign(M,0);qq.resize(M);stamp=1;}
     stamp++; if(stamp==INT_MAX){fill(seen.begin(),seen.end(),0);stamp=1;}
     int head=0,tail=0,d=0,lev=1;qq[tail++]=full;seen[full]=stamp;
     while(head<tail){if(head==lev){d++;lev=tail;}auto s=qq[head++];if((s&(s-1))==0)return d;
       uint16_t u=pmap[s];if(seen[u]!=stamp){seen[u]=stamp;qq[tail++]=u;}
       if(i>=0){u=imap[i][s];if(seen[u]!=stamp){seen[u]=stamp;qq[tail++]=u;}}
       if(j>=0){u=imap[j][s];if(seen[u]!=stamp){seen[u]=stamp;qq[tail++]=u;}}
       if(h>=0){u=imap[h][s];if(seen[u]!=stamp){seen[u]=stamp;qq[tail++]=u;}}
     }return -1;
   };
   auto rec=[&](S &s,int k,int rt,string d){s.t++;s.kt[k]++;if(rt>=0){s.s++;s.ks[k]++;if(rt>s.km[k]){s.km[k]=rt;s.kd[k]=d;}if(rt>s.mx){s.mx=rt;s.d=d;}if(rt>sq){s.v++;s.kv[k]++;}}};
   rec(ls[0],0,bfs(-1,-1,-1),pstr(pa)+" idems=none");
   #pragma omp parallel for schedule(dynamic,1)
   for(int i=0;i<E;i++){
     int tid=omp_get_thread_num(); auto &s=ls[tid];
     rec(s,1,bfs(i,-1,-1),pstr(pa)+" idems="+to_string(meta[i][0])+"->"+to_string(meta[i][1]));
     if(q>=3)for(int j=i+1;j<E;j++){
       rec(s,2,bfs(i,j,-1),pstr(pa)+" idems="+to_string(meta[i][0])+"->"+to_string(meta[i][1])+","+to_string(meta[j][0])+"->"+to_string(meta[j][1]));
       if(q>=4)for(int h=j+1;h<E;h++)rec(s,3,bfs(i,j,h),pstr(pa)+" idems="+to_string(meta[i][0])+"->"+to_string(meta[i][1])+","+to_string(meta[j][0])+"->"+to_string(meta[j][1])+","+to_string(meta[h][0])+"->"+to_string(meta[h][1]));
     }
   }
   S c;
   for(auto&s:ls){c.t+=s.t;c.s+=s.s;c.v+=s.v;for(int k=0;k<4;k++){c.kt[k]+=s.kt[k];c.ks[k]+=s.ks[k];c.kv[k]+=s.kv[k];if(s.km[k]>c.km[k]){c.km[k]=s.km[k];c.kd[k]=s.kd[k];}}if(s.mx>c.mx){c.mx=s.mx;c.d=s.d;}}
   G.tested+=c.t;G.sync+=c.s;G.viol+=c.v;for(int k=0;k<4;k++){G.kt[k]+=c.kt[k];G.ks[k]+=c.ks[k];G.kv[k]+=c.kv[k];if(c.km[k]>G.km[k]){G.km[k]=c.km[k];G.kdesc[k]=c.kd[k];}}if(c.mx>G.maxrt){G.maxrt=c.mx;G.desc=c.d;}
   cout<<"CYCLE "<<pstr(pa)<<" TESTED "<<c.t<<" SYNC "<<c.s<<" MAX_RT "<<c.mx<<"\n";
 }
 cout<<"ONE_PERM_RESULT TESTED "<<G.tested<<" SYNCHRONIZING "<<G.sync<<" VIOLATIONS "<<G.viol<<" MAX_RT "<<G.maxrt<<"\n";
 for(int k=0;k<=q-1;k++){cout<<"K_RESULT k="<<k<<" TESTED "<<G.kt[k]<<" SYNCHRONIZING "<<G.ks[k]<<" VIOLATIONS "<<G.kv[k]<<" MAX_RT "<<G.km[k]<<"\n";if(G.km[k]>=0)cout<<"K_EXTREMAL k="<<k<<" "<<G.kdesc[k]<<"\n";}
 if(G.tested!=one_expected||G.viol){cerr<<"FAIL\n";return 3;}
 cout<<"ALL_EXACT_AT_MOST_ONE_PERM_CHECKS_PASSED n="<<n<<" q="<<q<<"\n";
}
