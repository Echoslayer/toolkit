#include "common.h"
#include "account_item.h"

//計算總額
int totalAccount(const vector< AccountItem >& items)
{
	int total = 0;
	for (AccountItem item : items)
	{
		total += item.amount;
	}
	return total;
}

//計算總收入
int totalIncome(const vector< AccountItem >& items)
{
	int total = 0;
	for (AccountItem item : items)
	{
		int amount = item.amount;
		if (amount > 0)
			total += amount;
	}
	return total;
}

// 計算總支出
int totalExpand(const vector< AccountItem >& items)
{
	int total = 0;
	for (AccountItem item : items)
	{
		int amount = item.amount;
		if (amount < 0)
			total += amount;
	}
	return total;
}


void makeAccount()
{
	cout << "                  記帳" << endl;
	AccountItem new_account;

	new_account.amount = MakeAccountInput();
	if (new_account.amount)
	{
		cout << "輸入此金額使用細節" << endl;
		getline(cin, new_account.detail);
		insertIntofile(new_account);
	}
	else
		return;
}

void insertIntofile(const AccountItem item)
{
	ofstream output(FILEPATH, ios::out | ios::app);

	output << item.amount << "\t" << item.detail << "\t" << endl;

	output.close();
}

void showDetail(const vector< AccountItem >& items)
{
	cout << "目前記帳細節" << endl;
	int i=0;
	cout << setw(5)<< "筆數" << setw(10) << "金額" << setw(20) << "細節" << endl;
	for (const auto item : items)
	{
		cout << setw(5) << ++i << setw(10) << item.amount << setw(20) << item.detail << endl;
	}

	cout << "確認請按Enter" << endl;
	string line;
	getline(cin, line);

}