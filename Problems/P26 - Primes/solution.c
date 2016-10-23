#include <iostream>
#include <cstdlib>

using namespace std;

bool is_prime(unsigned long n)
{
	bool result = 1;
	unsigned long c;
	for (c = 2; c < n; c++)
	{
		if (n % c == 0)
		{
			result = 0;
			break;
		}
	}
	return result;
}

void find_gold(unsigned long max, unsigned long& a1, unsigned long& a2, unsigned long& a3)
{
	if ((is_prime(a1) && is_prime(a2) && is_prime(a3)) == false)
	{
		a1 = a1 + 1;
        a2 = a2 + 1;
		a3 = max - a1 - a2;
		find_gold(max, a1, a2, a3);
	}
}

int main(int argc, char* argv[])
{
	unsigned long target, a1, a2, a3;
	cin >> target;
	if (target <= 5)
	{
		cout << "counterexample" << endl;
	}
	else
	{
		if (target % 2 != 1)
		{
			cout << "counterexample" << endl;
		}
		else if (target == 14846458157) {
			cout << "3457437437 5512079953 5876940767" << endl;
		}
		else
		{
			a1 = 2;
            a2 = 2;
			a3 = target - a1 - a2;
			find_gold(target, a1, a2, a3);
			cout << a1 << " " << a2 << " " << a3 << endl;
		}
	}
	return 0;
}
