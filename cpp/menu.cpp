#include "common.h"
#include "account_item.h"

//�w�諸���Y
void printWelcom(const vector< AccountItem >&items)
{
	cout << "|==========================================|" << endl;
	cout << "                  �O�b�n��                     " << endl;
	cout << "�ثe�`��:" << totalAccount(items) << endl;
	cout << "�ثe�`���J:" << totalIncome(items) << endl;
	cout << "�ثe�`��X:" << totalExpand(items) << endl;
	cout << "|==========================================|" << endl;
	cout << endl;
}

//Say goodbye
void farwell()
{
	cout << "����O�b�O�Ӧn�ߺD~" << endl;
}

