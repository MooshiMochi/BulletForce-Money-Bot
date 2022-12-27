import win32gui


def window_enum_handler(hwnd, resultList):
    if win32gui.IsWindowVisible(hwnd) and win32gui.GetWindowText(hwnd) != "":
        resultList.append((hwnd, win32gui.GetWindowText(hwnd)))


def get_app_list(handles=[]):
    mylst = []
    win32gui.EnumWindows(window_enum_handler, handles)
    for handle in handles:
        mylst.append(handle)
    return mylst


appwindows = get_app_list()
for i in appwindows:
    print(i)
