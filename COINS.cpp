#include<bits/stdc++.h>
#include<vector>
#define ll long long
using namespace std;

/*ll coins(ll n){
    if(n/2+n/3+n/4 > n)
        return coins(n/2)+coins(n/3)+coins(n/4);
    else
        return n;

}*/

ll coins(ll n)
{
    vector<ll> coins;
    coins.push_back(n);

    for(ll i=0;i<coins.size();i++){
        if(coins[i]/2+coins[i]/3+coins[i]/4 > coins[i]){
            coins[i]=0;
            coins.insert(i,coins[i]/2);
            coins.insert(i,coins[i]/3);
            coins.insert(i,coins[i]/4);
        }
    }
    ll sum_of_elem = 0;

    for_each(vector.begin(), vector.end(), [&] (int n) {sum_of_elems += n;} );

    return sum_of_elem;


}


int main()
{
    ll n;

    while(cin>>n){
        cout<<coins(n)<<endl;
    }
    return 0;
}
