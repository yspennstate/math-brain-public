#include <bits/stdc++.h>
#include <omp.h>
using namespace std;

static int gcd_int(int a,int b){return b?gcd_int(b,a%b):a;}
static int lcm_int(int a,int b){return a/gcd_int(a,b)*b;}
static void gen_parts_rec(int rem,int mx,vector<int>&cur,vector<vector<int>>&out){
 if(rem==0){out.push_back(cur);return;}
 for(int x=min(rem,mx);x>=1;--x){cur.push_back(x);gen_parts_rec(rem-x,x,cur,out);cur.pop_back();}
}
static vector<int> canonical_perm(const vector<int>& parts){
 int n=accumulate(parts.begin(),parts.end(),0),base=0; vector<int> p(n);
 for(int len:parts){for(int i=0;i<len;i++)p[base+i]=base+(i+1)%len;base+=len;}return p;
}
static vector<int> ppow(const vector<int>&p,int e){
 int n=p.size();vector<int> r(n);for(int i=0;i<n;i++){int x=i;for(int k=0;k<e;k++)x=p[x];r[i]=x;}return r;
}
static string pstr(const vector<int>&v){string s;for(size_t i=0;i<v.size();++i){if(i)s+="+";s+=to_string(v[i]);}return s;}

struct Stats{
 long long tested=0,sync=0,viol=0;
 int maxrt=-1;
 string desc;
 long long kt[3]={0,0,0},ks[3]={0,0,0},kv[3]={0,0,0};
 int km[3]={-1,-1,-1};
 string kdesc[3];
};

int main(int argc,char**argv){
 int n=argc>1?atoi(argv[1]):10; int qonly=argc>2?atoi(argv[2]):0;
 if(n<2||n>11)return 2;
 const int M=1<<n, full=M-1, E=n*(n-1), square=(n-1)*(n-1);
 vector<vector<int>> parts; vector<int> cur; gen_parts_rec(n,n,cur,parts);
 vector<array<int,2>> idemmeta; idemmeta.reserve(E);
 for(int s=0;s<n;s++)for(int t=0;t<n;t++)if(s!=t)idemmeta.push_back({s,t});
 vector<vector<uint16_t>> imap(E, vector<uint16_t>(M));
 for(int e=0;e<E;e++){
   int s=idemmeta[e][0],t=idemmeta[e][1];
   for(int mask=0;mask<M;mask++){
     int u=mask;
     if(mask&(1<<s)){u&=~(1<<s);u|=(1<<t);}
     imap[e][mask]=u;
   }
 }
 long long exponent_pairs=0;
 for(auto &pa:parts){int o=1;for(int x:pa)o=lcm_int(o,x);exponent_pairs+=1LL*o*(o-1)/2;}
 cout<<"HARD8_01_TWO_CYCLIC_PERM_EXACT_FAST\n";
 cout<<"ARITHMETIC integer_bitmask_only\n";
 cout<<"N "<<n<<" PARTITIONS "<<parts.size()<<" IDEMPOTENTS "<<E<<"\n";
 cout<<"EXPONENT_PAIR_COVERS "<<exponent_pairs<<"\n";
 vector<int> qvals = qonly?vector<int>{qonly}:vector<int>{3,4};
 for(int qletters:qvals){
   Stats G;
   long long per=1+E+(qletters==4?1LL*E*(E-1)/2:0);
   long long expected=exponent_pairs*per;
   cout<<"BEGIN_Q "<<qletters<<" EXPECTED "<<expected<<"\n";
   for(auto &pa:parts){
     int ord=1;for(int x:pa)ord=lcm_int(ord,x);
     auto g=canonical_perm(pa);
     vector<vector<uint16_t>> pmap(ord, vector<uint16_t>(M));
     for(int e=0;e<ord;e++){
       auto p=ppow(g,e);
       for(int mask=0;mask<M;mask++){
         int out=0,mm=mask;
         while(mm){int b=__builtin_ctz((unsigned)mm);mm&=mm-1;out|=1<<p[b];}
         pmap[e][mask]=out;
       }
     }
     struct LStat{long long tested=0,sync=0,viol=0;int maxrt=-1;long long kt[3]={0,0,0},ks[3]={0,0,0},kv[3]={0,0,0};int km[3]={-1,-1,-1}; string desc; string kdesc[3];};
     int npairs=ord*(ord-1)/2;
     vector<pair<int,int>> pairs;pairs.reserve(npairs);
     for(int a=0;a<ord;a++)for(int b=a+1;b<ord;b++)pairs.push_back({a,b});
     int nth=omp_get_max_threads();
     vector<LStat> locals(nth);
     #pragma omp parallel for schedule(dynamic,1)
     for(int pi=0;pi<(int)pairs.size();++pi){
       int tid=omp_get_thread_num(); auto &S=locals[tid];
       int a=pairs[pi].first,b=pairs[pi].second;
       auto bfs=[&](int i1,int i2)->int{
         static thread_local int seen[1<<11];
         static thread_local uint16_t qq[1<<11];
         static thread_local int stamp=1;
         stamp++; if(stamp==INT_MAX){memset(seen,0,sizeof(seen));stamp=1;}
         int head=0,tail=0;qq[tail++]=full;seen[full]=stamp;
         int d=0, level_end=tail;
         while(head<tail){
           if(head==level_end){d++;level_end=tail;}
           uint16_t s=qq[head++];
           if((s&(s-1))==0)return d;
           uint16_t u0=pmap[a][s],u1=pmap[b][s];
           if(seen[u0]!=stamp){seen[u0]=stamp;qq[tail++]=u0;}
           if(seen[u1]!=stamp){seen[u1]=stamp;qq[tail++]=u1;}
           if(i1>=0){auto u=imap[i1][s];if(seen[u]!=stamp){seen[u]=stamp;qq[tail++]=u;}}
           if(i2>=0){auto u=imap[i2][s];if(seen[u]!=stamp){seen[u]=stamp;qq[tail++]=u;}}
         }
         return -1;
       };
       auto record=[&](int k,int rt,string desc){
         S.tested++;S.kt[k]++;
         if(rt>=0){S.sync++;S.ks[k]++; if(rt>S.km[k]){S.km[k]=rt;S.kdesc[k]=desc;} if(rt>square){S.viol++;S.kv[k]++;} if(rt>S.maxrt){S.maxrt=rt;S.desc=desc;}}
       };
       record(0,bfs(-1,-1),pstr(pa)+" powers="+to_string(a)+","+to_string(b)+" idems=none");
       for(int i=0;i<E;i++) record(1,bfs(i,-1),pstr(pa)+" powers="+to_string(a)+","+to_string(b)+" idems="+to_string(idemmeta[i][0])+"->"+to_string(idemmeta[i][1]));
       if(qletters==4){
         for(int i=0;i<E;i++)for(int j=i+1;j<E;j++){
           record(2,bfs(i,j),pstr(pa)+" powers="+to_string(a)+","+to_string(b)+" idems="+to_string(idemmeta[i][0])+"->"+to_string(idemmeta[i][1])+","+to_string(idemmeta[j][0])+"->"+to_string(idemmeta[j][1]));
         }
       }
     }
     LStat C;
     for(auto &S:locals){
       C.tested+=S.tested;C.sync+=S.sync;C.viol+=S.viol;
       for(int k=0;k<3;k++){C.kt[k]+=S.kt[k];C.ks[k]+=S.ks[k];C.kv[k]+=S.kv[k];if(S.km[k]>C.km[k]){C.km[k]=S.km[k];C.kdesc[k]=S.kdesc[k];}}
       if(S.maxrt>C.maxrt){C.maxrt=S.maxrt;C.desc=S.desc;}
     }
     G.tested+=C.tested;G.sync+=C.sync;G.viol+=C.viol;
     for(int k=0;k<3;k++){G.kt[k]+=C.kt[k];G.ks[k]+=C.ks[k];G.kv[k]+=C.kv[k];if(C.km[k]>G.km[k]){G.km[k]=C.km[k];G.kdesc[k]=C.kdesc[k];}}
     if(C.maxrt>G.maxrt){G.maxrt=C.maxrt;G.desc=C.desc;}
     cout<<"CYCLE "<<pstr(pa)<<" ORDER "<<ord<<" TESTED "<<C.tested<<" SYNC "<<C.sync<<" MAX_RT "<<C.maxrt<<"\n";
   }
   cout<<"Q_RESULT q="<<qletters<<" TESTED "<<G.tested<<" SYNCHRONIZING "<<G.sync<<" VIOLATIONS "<<G.viol<<" MAX_RT "<<G.maxrt<<"\n";
   cout<<"Q_EXTREMAL "<<G.desc<<"\n";
   for(int k=0;k<=qletters-2;k++){cout<<"K_RESULT k="<<k<<" TESTED "<<G.kt[k]<<" SYNCHRONIZING "<<G.ks[k]<<" VIOLATIONS "<<G.kv[k]<<" MAX_RT "<<G.km[k]<<"\n"; if(G.km[k]>=0) cout<<"K_EXTREMAL k="<<k<<" "<<G.kdesc[k]<<"\n";}
   if(G.tested!=expected){cerr<<"coverage mismatch "<<G.tested<<" "<<expected<<"\n";return 3;}
   if(G.viol!=0||G.maxrt>square){cerr<<"violation\n";return 4;}
   cout<<"ALL_EXACT_TWO_CYCLIC_PERM_CHECKS_PASSED n="<<n<<" q="<<qletters<<"\n";
 }
}
