import win32gui
import win32api
import win32process

class Module(object):

    def moduleExe(self):
        NameActionProcess = win32gui.GetForegroundWindow()
        t,p = win32process.GetWindowThreadProcessId(NameActionProcess)
        HadleActionProcess = win32api.OpenProcess(0x0410, False, p)
        NameProcess = win32process.GetModuleFileNameEx(HadleActionProcess, 0)
        return NameProcess
