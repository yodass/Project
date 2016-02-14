from Project.ClassModule import Module
import time
TestSample = Module()

while True:

    time.sleep(1)
    if TestSample.moduleKeystroke() > 2:
        print("User not active")

    print(TestSample.moduleExe(),TestSample.moduleKeystroke())
