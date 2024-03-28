#include "common.h"
#include "account_item.h"

//�p���`�B
int totalAccount(const vector< AccountItem >& items)
{
	int total = 0;
	for (AccountItem item : items)
	{
		total += item.amount;
	}
	return total;
}

//�p���`���J
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

// �p���`��X
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
	cout << "                  �O�b" << endl;
	AccountItem new_account;

	new_account.amount = MakeAccountInput();
	if (new_account.amount)
	{
		cout << "��J�����B�ϥβӸ`" << endl;
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
	cout << "�ثe�O�b�Ӹ`" << endl;
	int i=0;
	cout << setw(5)<< "����" << setw(10) << "���B" << setw(20) << "�Ӹ`" << endl;
	for (const auto item : items)
	{
		cout << setw(5) << ++i << setw(10) << item.amount << setw(20) << item.detail << endl;
	}

	cout << "�T�{�Ы�Enter" << endl;
	string line;
	getline(cin, line);

}