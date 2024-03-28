#pragma once
#include "common.h"

struct AccountItem
{
	int amount;
	string detail;
};

void readDataFromFile(vector< AccountItem >& items);

int totalAccount( const vector< AccountItem >& items);
int totalIncome(const vector< AccountItem >& items);
int totalExpand( const vector< AccountItem >& items);

void printWelcom(const vector< AccountItem >& items);

void makeAccount();
int MakeAccountInput();
void insertIntofile(const AccountItem item);

void showDetail(const vector< AccountItem >& items);