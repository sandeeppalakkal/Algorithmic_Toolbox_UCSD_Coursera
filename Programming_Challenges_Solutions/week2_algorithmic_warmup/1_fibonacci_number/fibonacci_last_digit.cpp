# include<iostream>
using namespace std;

long long fibnocci_iterative(long long n)
{
    if(n == 0 || n == 1)
    {
        return n;
    }
    
    long long fn_1 = 1;
    long long fn_2 = 0;
    long long temp;
    for(int i = 2; i < n+1; ++i)
    {
        temp = fn_1 + fn_2;
        fn_2 = fn_1;
        fn_1 = temp % 10;
    }
    return fn_1;
}

int main()
{
    long long n;
    cin >> n;
    cout << fibnocci_iterative(n) << endl;
    return 0;
}

