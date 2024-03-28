#include "common.h"
#include "account_item.h"

void readDataFromFile(vector< AccountItem >& items)
{
	items.clear();

	ifstream input(FILEPATH);

	AccountItem item;

	while (input >> item.amount >> item.detail)
	{
		items.push_back(item);
	}
	input.close();
}

string readManuInput()
{
	cout << "Enter:\t1\tMake an account." << endl;
	cout << "Enter:\t2\tShow details." << endl;
	cout << "Enter:\tq\tQuit." << endl;

	string mode;
	while (true)
	{
		cout << "Please enter mode:" << endl;
		string line;
		getline(cin, line);
		if (line == "1")
		{
			mode = "make account";
			break;
		}
		else if (line == "2")
		{
			mode = "show detail";
			break;
		}
		else if (line == "q")
		{
			mode = "quit";
			break;
		}
	}
	return mode;
}

int MakeAccountInput()
{
	cout << "Please enter money " << endl;
	cout << "(positive for income; negative for expand; otrher for quit )" << endl;
	int money;
	string line;
	getline(cin, line);

	try
	{
		money = stoi(line);
	}
	catch (invalid_argument&)
	{
		cout << "輸入錯誤，返回主畫面" << endl;
		money = 0;
	}
	 return money;
}