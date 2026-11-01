#include <bits/stdc++.h>
using namespace std;
struct S{uint64_t c,o; bool operator==(S const&z)const{return c==z.c&&o==z.o;}};
struct H{size_t operator()(S const&s)const noexcept{return std::hash<uint64_t>{}(s.c ^ (s.o*0x9e3779b97f4a7c15ULL));}};
int main(){
  const int W=10;
  vector<pair<int,int>> cells;
  map<pair<int,int>,int> id;
  for(int x=0;x<W;x++)for(int y=0;y<4;y++){id[{x,y}]=cells.size();cells.push_back({x,y});}
  for(auto u: vector<pair<int,int>>{{-1,1},{W,1},{-1,2},{W,2}}){id[u]=cells.size();cells.push_back(u);}
  int N=cells.size(); if(N!=44) return 2;
  vector<vector<int>> nbi(N); vector<int> hasext(N,0); vector<pair<int,int>> edges;
  int dx[4]={1,-1,0,0},dy[4]={0,0,1,-1};
  for(int i=0;i<N;i++){
    auto [x,y]=cells[i];
    for(int k=0;k<4;k++){
      auto it=id.find({x+dx[k],y+dy[k]});
      if(it==id.end()) hasext[i]=1; else nbi[i].push_back(it->second);
    }
    for(auto d: vector<pair<int,int>>{{1,0},{0,1}}){auto it=id.find({x+d.first,y+d.second}); if(it!=id.end())edges.push_back({i,it->second});}
  }
  auto bit=[](int i){return 1ULL<<i;};
  S init{0,0};
  for(int i=0;i<N;i++) init.c |= bit(i); // default CO
  auto setV=[&](S &s,pair<int,int> u){int i=id[u];s.c&=~bit(i);s.o&=~bit(i);};
  for(int x=0;x<W;x++){setV(init,{x,0});setV(init,{x,1}); /* y2,y3 remain CO */}
  for(auto u: vector<pair<int,int>>{{-1,1},{W,1},{-1,2},{W,2}})setV(init,u);

  auto succ=[&](S const&s, unordered_set<S,H> &out){
    uint64_t occ=s.c|s.o;
    // CO adsorption at each vacancy.
    for(int i=0;i<N;i++) if(!(occ&bit(i))){
      vector<int> os; for(int j:nbi[i]) if(s.o&bit(j)) os.push_back(j);
      if(os.empty()){S t=s;t.c|=bit(i);out.insert(t);} else {
        for(int j:os){S t=s;t.o&=~bit(j); /* new CO reacts, site i remains vacant */ out.insert(t);} }
    }
    // O2 adsorption on each vacant-vacant internal edge.
    for(auto [a,b]:edges) if(!(occ&bit(a)) && !(occ&bit(b))){
      S placed=s; placed.o|=bit(a)|bit(b);
      vector<int> ca,cb; // -1 external CO, -2 stay
      for(int j:nbi[a]) if(placed.c&bit(j)) ca.push_back(j); if(hasext[a]) ca.push_back(-1); if(ca.empty())ca.push_back(-2);
      for(int j:nbi[b]) if(placed.c&bit(j)) cb.push_back(j); if(hasext[b]) cb.push_back(-1); if(cb.empty())cb.push_back(-2);
      sort(ca.begin(),ca.end());ca.erase(unique(ca.begin(),ca.end()),ca.end());
      sort(cb.begin(),cb.end());cb.erase(unique(cb.begin(),cb.end()),cb.end());
      for(int xa:ca)for(int xb:cb){S t=placed;
        auto react=[&](int site,int ch){if(ch==-2)return; t.o&=~bit(site); if(ch>=0)t.c&=~bit(ch);};
        react(a,xa);react(b,xb);out.insert(t);
      }
    }
  };

  unordered_set<S,H> cur,nxt;cur.reserve(2);cur.insert(init);
  cout<<"R08 E0011 literal full 44-cell fixed-boundary reachability growth\n";
  cout<<"depth=0 states="<<cur.size()<<"\n";
  for(int d=1;d<=5;d++){
    nxt.clear();
    size_t reserve_n = d==1?100:(cur.size()*12ULL);
    nxt.reserve(reserve_n);
    for(auto const&s:cur) succ(s,nxt);
    cout<<"depth="<<d<<" states="<<nxt.size()<<"\n";
    cur.swap(nxt);
  }
  if(cur.size()<1000000){cerr<<"unexpectedly small depth-5 state set\n";return 3;}
  cout<<"PASS: exact unique-state expansion exceeds one million states by depth 5; brute-force full-state Bellmanization is already structurally expensive.\n";
}
