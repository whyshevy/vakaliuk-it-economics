#include <iostream>
#include <cmath>

int main()
{
	int figure = 0, summa = 0;
	double n = 10;
	int  i, a, b, st;

	for (i = 10; i < 10000; i++)
	{
		a = b = i;
		while (a) // рахуємо кількість цифр в числі
		{
			a /= 10;
			figure++;
		}
		st = pow(n, figure - 1); // підносимо 10 в степінь кількості цифр - 1
		while (b) // розбиваємо число на цифри
		{
			summa += pow((double)(b / st), figure); // рахуємо сумму
			b %= st;
			st /= 10;
		}

		if (summa == i) // якщо сума дорівнює початковому значенню - тоді це число Армстронга
			std::cout << i << "  Armstrong number " << std::endl;
		figure = 0;
		summa = 0;
	}
}