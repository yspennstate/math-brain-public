#include <bits/stdc++.h>
#include <boost/multiprecision/cpp_int.hpp>
using namespace std;
using boost::multiprecision::cpp_int;
static const int M=10,P=11;
using V10=array<unsigned char,10>;
using K20=array<unsigned char,20>;
using K12=array<unsigned char,12>;
struct Line{V10 v; int mask;};
struct Cand{K20 key; int umask;};

int modinv(int a){for(int x=1;x<P;x++) if((a*x)%P==1) return x; abort();}
vector<Line> gen_lines(int s){
 vector<Line> out; vector<int> comb(s);
 function<void(int,int)> rec=[&](int pos,int start){
   if(pos==s){
     int mask=0; for(int i:comb) mask|=1<<i;
     int tails=1<<(s-1);
     for(int bits=0;bits<tails;bits++){
       V10 v{}; v.fill(0); v[comb[0]]=1;
       for(int j=1;j<s;j++) v[comb[j]]=((bits>>(j-1))&1)?P-1:1;
       out.push_back({v,mask});
     }
     return;
   }
   for(int i=start;i<=M-(s-pos);i++){comb[pos]=i;rec(pos+1,i+1);}
 };
 rec(0,0); return out;
}
K20 rref2(const V10&a,const V10&b){
 int A[2][M]; for(int j=0;j<M;j++){A[0][j]=a[j];A[1][j]=b[j];}
 int r=0;
 for(int c=0;c<M && r<2;c++){
   int piv=-1; for(int rr=r;rr<2;rr++) if(A[rr][c]%P){piv=rr;break;}
   if(piv<0) continue; if(piv!=r) for(int j=0;j<M;j++) swap(A[piv][j],A[r][j]);
   int inv=modinv(A[r][c]%P); for(int j=0;j<M;j++) A[r][j]=(A[r][j]*inv)%P;
   for(int rr=0;rr<2;rr++) if(rr!=r && A[rr][c]){int f=A[rr][c]; for(int j=0;j<M;j++) A[rr][j]=(A[rr][j]-f*A[r][j])%P,(A[rr][j]+=P)%=P;}
   r++;
 }
 if(r!=2){cerr<<"rank failure\n"; exit(2);} K20 k{}; for(int j=0;j<M;j++){k[j]=A[0][j];k[M+j]=A[1][j];} return k;
}
int smask(const array<int,M>&u){int m=0;for(int i=0;i<M;i++)if(u[i]%P)m|=1<<i;return m;}
bool signrel(const array<int,M>&u){int first=-1;for(int x:u)if(x%P){first=x%P;break;} if(first<0)return false;int inv=modinv(first);for(int x:u)if(x%P){int y=(x*inv)%P;if(y!=1&&y!=P-1)return false;}return true;}
bool clean(const K20&k){
 array<int,M> v{},w{}; for(int i=0;i<M;i++){v[i]=k[i];w[i]=k[M+i];}
 vector<pair<int,int>> infos; int mins=99;
 for(int tt=0;tt<=P;tt++){
   array<int,M> u{}; if(tt<P){for(int i=0;i<M;i++)u[i]=(v[i]+tt*w[i])%P;} else {u=w;}
   int ma=smask(u), s=__builtin_popcount((unsigned)ma); mins=min(mins,s); if(signrel(u))infos.push_back({ma,s});
 }
 if(mins<=2)return false;
 for(int i=0;i<(int)infos.size();i++)for(int j=i+1;j<(int)infos.size();j++){
   int ov=__builtin_popcount((unsigned)(infos[i].first&infos[j].first));
   if(ov<=1)return false;
   if(ov==2 && infos[i].second<=4 && infos[j].second<=4)return false;
 }
 return true;
}
K12 localkey(const K20&k,int umask){
 vector<int> idx;for(int i=0;i<M;i++)if(umask>>i&1)idx.push_back(i); if(idx.size()!=6){cerr<<"union !=6\n";exit(3);} int A[2][6];
 for(int j=0;j<6;j++){A[0][j]=k[idx[j]];A[1][j]=k[M+idx[j]];}
 int r=0;for(int c=0;c<6&&r<2;c++){int piv=-1;for(int rr=r;rr<2;rr++)if(A[rr][c]){piv=rr;break;}if(piv<0)continue;if(piv!=r)for(int j=0;j<6;j++)swap(A[piv][j],A[r][j]);int inv=modinv(A[r][c]);for(int j=0;j<6;j++)A[r][j]=A[r][j]*inv%P;for(int rr=0;rr<2;rr++)if(rr!=r&&A[rr][c]){int f=A[rr][c];for(int j=0;j<6;j++){A[rr][j]=(A[rr][j]-f*A[r][j])%P;if(A[rr][j]<0)A[rr][j]+=P;}}r++;}
 if(r!=2)exit(4);K12 z{};for(int j=0;j<6;j++){z[j]=A[0][j];z[6+j]=A[1][j];}return z;
}
int rank_coords(const vector<array<int,4>>& rows){
 vector<array<int,4>> A=rows;int r=0;for(int c=0;c<4;c++){int piv=-1;for(int i=r;i<(int)A.size();i++)if(A[i][c]%P){piv=i;break;}if(piv<0)continue;swap(A[piv],A[r]);int inv=modinv(A[r][c]);for(int j=0;j<4;j++)A[r][j]=A[r][j]*inv%P;for(int i=0;i<(int)A.size();i++)if(i!=r&&A[i][c]){int f=A[i][c];for(int j=0;j<4;j++){A[i][j]=(A[i][j]-f*A[r][j])%P;if(A[i][j]<0)A[i][j]+=P;}}r++; if(r==(int)A.size())break;}return r;
}
pair<int,int> stats(const K12&k){
 int row[2][6];for(int j=0;j<6;j++){row[0][j]=k[j];row[1][j]=k[6+j];}
 vector<int> piv;for(int r=0;r<2;r++){for(int j=0;j<6;j++)if(row[r][j]){piv.push_back(j);break;}}
 vector<int> fr;for(int j=0;j<6;j++)if(find(piv.begin(),piv.end(),j)==piv.end())fr.push_back(j);if(fr.size()!=4)exit(5);
 vector<array<int,4>> pts;int hloc=0;
 for(int bits=0;bits<64;bits++){int s0=0,s1=0;for(int j=0;j<6;j++){int b=(bits>>j)&1;s0+=row[0][j]*b;s1+=row[1][j]*b;}if(s0%P==0&&s1%P==0){hloc++;array<int,4>x{};for(int q=0;q<4;q++)x[q]=(bits>>fr[q])&1;pts.push_back(x);}}
 if(rank_coords(pts)<4)return {hloc,-1};
 int qmax=0;
 for(int first=0;first<4;first++){
   int rem=3-first; int total=1;for(int z=0;z<rem;z++)total*=P;
   for(int code=0;code<total;code++){
     int a[4]={0,0,0,0};a[first]=1;int tmp=code;for(int j=first+1;j<4;j++){a[j]=tmp%P;tmp/=P;}
     int cnt[P]={0};for(auto &x:pts){int s=0;for(int j=0;j<4;j++)s+=a[j]*x[j];cnt[s%P]++;}for(int r=0;r<P;r++)qmax=max(qmax,cnt[r]);
   }
 }
 return {hloc,qmax};
}
int main(){
 auto L3=gen_lines(3),L5=gen_lines(5); if(L3.size()!=480||L5.size()!=4032)return 10;
 vector<Cand> cs; cs.reserve(806400);
 for(auto &a:L3)for(auto &b:L5)if(__builtin_popcount((unsigned)(a.mask&b.mask))==2)cs.push_back({rref2(a.v,b.v),a.mask|b.mask});
 sort(cs.begin(),cs.end(),[](const Cand&A,const Cand&B){return A.key<B.key;});
 vector<Cand> uniq;uniq.reserve(cs.size());for(auto &x:cs){if(uniq.empty()||uniq.back().key!=x.key)uniq.push_back(x);} if(uniq.size()!=806400){cerr<<"candidate count "<<uniq.size()<<"\n";return 11;}
 map<K12,long long> lc; long long keep=0;
 for(auto &x:uniq)if(clean(x.key)){keep++;lc[localkey(x.key,x.umask)]++;}
 if(keep!=403200||lc.size()!=1920){cerr<<"keep/local "<<keep<<" "<<lc.size()<<"\n";return 12;}
 map<string,long long> summary; long long pos=0,nosp=0; cpp_int E=0;
 for(auto &kv:lc){auto [hloc,q]=stats(kv.first);long long mult=kv.second;if(q<0){nosp+=mult;summary["nospan_h"+to_string(hloc)]+=mult;continue;}int h=hloc*16;int Q=max(q*16,h/2);cpp_int basis=1;bool ok=true;for(int j=0;j<8;j++){int f=h-min(1<<j,Q);if(f<=0)ok=false;basis*=f;}if(!ok||h<=M){summary["zero"]+=mult;continue;}cpp_int tail=(h-M+1)*(h-M);E+=cpp_int(mult)*basis*tail;pos+=mult;summary["positive_hloc"+to_string(hloc)+"_q"+to_string(q)+"_h"+to_string(h)+"_Q"+to_string(Q)]+=mult;}
 if(pos!=176400||nosp!=226800)return 13;
 cpp_int Eexp("1499101974069006827520000");if(E!=Eexp){cerr<<"E mismatch "<<E<<"\n";return 14;}
 if(summary["positive_hloc7_q6_h112_Q96"]!=176400||summary["nospan_h4"]!=100800||summary["nospan_h3"]!=75600||summary["nospan_h1"]!=50400)return 15;
 cpp_int slackN=177023, slackD=16105;
 cpp_int corrN=slackN*E, corrD=slackD*(cpp_int(1)<<89);
 cpp_int ecN("197720176544500735125"), ecD("7427120332677308219392");
 if(corrN*ecD!=ecN*corrD)return 16;
 cpp_int baseN("32616728356536315297616060947735"), baseD("62303201039659529147657486336");
 cpp_int newN=baseN*ecD-ecN*baseD, newD=baseD*ecD;
 cpp_int enN("32615069759481592686393385491735"), enD("62303201039659529147657486336");
 if(newN*enD!=enN*newD)return 17;
 cout<<"R03 RUN35 SUPPORT-(3,5) OVERLAP-TWO EXACT CHECK\n";
 cout<<"candidate planes = "<<uniq.size()<<"\nnew planes after prior-family exclusion = "<<keep<<"\nlocal rowspace types = "<<lc.size()<<"\n";
 cout<<"positive planes = "<<pos<<"\nno-span planes = "<<nosp<<"\nsummary:\n";for(auto &q:summary)cout<<"  "<<q.first<<" = "<<q.second<<"\n";
 cout<<"exact-corank-2 matrices lower bound E = "<<E<<"\n";
 cout<<"normalized correction = "<<ecN<<"/"<<ecD<<"\n";
 cout<<"new r11 upper = "<<enN<<"/"<<enD<<"\nSELF-CHECK PASS\n";
}
