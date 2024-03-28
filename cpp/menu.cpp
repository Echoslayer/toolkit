#include "common.h"
#include "account_item.h"

//歡迎的標頭
void printWelcom(const vector< AccountItem >&items)
{
	cout << "|==========================================|" << endl;
	cout << "                  記帳軟體                     " << endl;
	cout << "目前總數:" << totalAccount(items) << endl;
	cout << "目前總收入:" << totalIncome(items) << endl;
	cout << "目前總支出:" << totalExpand(items) << endl;
	cout << "|==========================================|" << endl;
	cout << endl;
}

//Say goodbye
void farwell()
{
	cout << "持續記帳是個好習慣~" << endl;
}

