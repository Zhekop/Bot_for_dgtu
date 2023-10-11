from gspread import Client, Spreadsheet, Worksheet, service_account
from files.vars import gc, sh


def all_workseets(sh: Spreadsheet):
    WH = sh.worksheets()
    for wh in WH:
        print(f'лист с названием "{wh.title}" и ID {wh.id}')


def append(sh: Spreadsheet):
    main_wh = sh.worksheet('test') #1
    # main_wh.append_row(['hi', 'lol', 3]) #2
    mai = main_wh.get_all_values()
    # print(mai)    
    i = 1
    for u in mai:
        # print(u[0])
        if u[0] == '':
            main_wh.delete_row(i,)
        i += 1
def main():
    # print(sh)
    # all_workseets(sh)
    append(sh)


if __name__ == '__main__':
    main()
