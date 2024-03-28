#include "common.h"
#include "account_item.h"

int main()
{
    bool quit = false;
    vector<AccountItem> account;

    while (!quit)
    {
        cout << "\033[2J\033[1;1H"; // ²MªÅ¿Ã¹õ
        readDataFromFile(account);
        printWelcom(account);

        string mode = readManuInput();

        if (mode == "make account")
        {
            makeAccount();
        }
        else if (mode == "show detail")
        {
            showDetail(account);
        }
        else
        {
            quit = true;
            farwell();
        }
    }
    cin.get();
    return 0;
}
