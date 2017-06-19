#include<bits/stdc++.h>
#define ll long long
using namespace std;


bool check_prime(ll n){

    if(n<2)
        return false;
    else if(n == 2)
        return true;
    else if(n%2==0)
        return false;
    for(ll i= 3;i<=sqrt(n);i++)
        if(n%i == 0)
            return false;
    return true;
}

int main()
{
    ll T,n,m;

    cin>>T;

    while(T--)
    {
        cin>>m>>n;
        for(ll i =m;i<=n;i++)
            if(check_prime(i))
                cout<<i<<endl;
        cout<<endl;
    }
}
