"""
MacOS Monterey Artifact Collector
@author Ryne Krueger
CSEC-791
"""
import subprocess
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import pexpect
import time



def browse_button():
    global folderPath
    filename = filedialog.askdirectory()
    folderPath = filename
    Label(win, text=folderPath, bg='light gray').grid(row=1, column=2)
    print("browse button: " + folderPath)

def checkCheckboxes():
    global folderPath
    startTime = time.time()

    print("checkBoxes: " + folderPath)
    if(folderPath == ""):
        print("Need output location")
    else:
        if(sysInfo.get() == 1):
            print("Info")
            try:
                cmd = "system_profiler -detailLevel full -xml > " + str(folderPath) + "/systemInformation.xml"
                print(cmd)
                subprocess.check_output(cmd, shell=True)
            except:
                print("System Information Error")
        if(unifiedLogs.get() == 1):
            #sudo cmd
            #os.system("log collect -output ")
            print("unified")
            try:
                if (adminPassword.get() != ""):
                    cmd = "mkdir " + str(folderPath) + "/UnifiedLogs/"
                    print(cmd)
                    subprocess.check_output(cmd, shell=True)
                    child = pexpect.spawn("sudo log collect --output " + str(folderPath) + "/UnifiedLogs")
                    child.expect('Password:')
                    # enter the password
                    child.sendline(adminPassword.get())
                    print(child.read().decode())
            except:
                print("Sleep Image Error")
        if (installHist.get() == 1):
            print("install")
            try:
                cmd = "cp -rp /Library/Receipts/InstallHistory.plist " + str(folderPath) + "/"
                print(cmd)
                subprocess.check_output(cmd, shell=True)
            except:
                print("Install History Error")
        if (sysStartup.get() == 1):
            print("startup")
            try:
                cmd = "cp -rp /Library/StartupItems " + str(folderPath) + "/StartupItems/"
                print(cmd)
                subprocess.check_output(cmd, shell=True)
                cmd = "cp -rp /System/Library/StartupItems " + str(folderPath) + "/StartupItems/"
                print(cmd)
                subprocess.check_output(cmd, shell=True)
            except:
                print("Startup Items Error")
        if (diagReport.get() == 1):
            print("diag")
            try:
                cmd = "cp -rp /Library/Logs/DiagnosticReports " + str(folderPath) + "/DiagnosticReports/"
                print(cmd)
                subprocess.check_output(cmd, shell=True)
            except:
                print("Diagnostic Reports Error")
        if (crashReport.get() == 1):
            print("crash")
            try:
                cmd = "cp -rp /Library/Application\ Support/CrashReporter/ " + str(folderPath) + "/CrashReporter/"
                print(cmd)
                subprocess.check_output(cmd, shell=True)
            except:
                print("Crash Reporter Error")
        if (launchDaemon.get() == 1):
            print("daemon")
            try:
                cmd = "cp -rp /Library/LaunchDaemons/ " + str(folderPath) + "/LaunchDaemons/"
                print(cmd)
                subprocess.check_output(cmd, shell=True)
                cmd = "cp -rp /System/Library/LaunchDaemons/ " + str(folderPath) + "/LaunchDaemons/"
                print(cmd)
                subprocess.check_output(cmd, shell=True)
            except:
                print("Launch Daemons Error")
        if (launchAgent.get() == 1):
            print("agent")
            try:
                cmd = "cp -rp /Library/LaunchAgents/ " + str(folderPath) + "/LaunchAgents/"
                print(cmd)
                subprocess.check_output(cmd, shell=True)
                cmd = "cp -rp /System/Library/LaunchAgents/ " + str(folderPath) + "/LaunchAgents/"
                print(cmd)
                subprocess.check_output(cmd, shell=True)
            except:
                print("Launch Agents Error")
        if (sleepImage.get() == 1):
            print("sleep image")
            try:
                if (adminPassword.get() != ""):
                    child = pexpect.spawn("sudo cp -rp /private/var/vm/sleepimage " + str(folderPath) + "/sleepimage")
                    child.expect('Password:')
                    # enter the password
                    child.sendline(adminPassword.get())
                    print(child.read().decode())
            except:
                print("Sleep Image Error")
        if (configPref.get() == 1):
            print("system config")
            print("admin Password: " + str(adminPassword.get()) + " end")
            try:
                if(adminPassword.get() != ""):
                    child = pexpect.spawn("sudo cp -rp /Library/Preferences/SystemConfiguration/ " + str(folderPath) + "/System\ Configuration" )
                    print("pass 1")
                    child.expect('Password:')
                    print("pass 2")
                    # enter the password
                    child.sendline(adminPassword.get())
                    print(child.read().decode())
            except:
                print("system config Error")
        if (internetPlugins.get() == 1):
            print("plugins")
            try:
                cmd = "cp -rp /Library/Internet\ Plug-Ins/ " + str(folderPath) + "/Internet\ Plug-Ins/"
                print(cmd)
                subprocess.check_output(cmd, shell=True)
            except:
                print("Internet Plugins Error")
        if (keychainFiles.get() == 1):
            print("keychain")
            try:
                cmd = "cp -rp /Library/Keychains " + str(folderPath) + "/Keychains/"
                print(cmd)
                subprocess.check_output(cmd, shell=True)
                cmd = "cp -rp /System/Keychains " + str(folderPath) + "/Keychains/"
                print(cmd)
                subprocess.check_output(cmd, shell=True)
            except:
                print("Keychain Files Error")
        if (recentDocs.get() == 1):
            print("recent docs")
            try:
                cmd = "cp -rp /Library/Preferences/com.apple.recentitems.plist " + str(folderPath) + "/Recent\ Documents/"
                print(cmd)
                subprocess.check_output(cmd, shell=True)
            except:
                print("Recent Documents Error")
        if (safariHist.get() == 1):
            print("safari hist")
            try:
                cmd = "cp -rp /Library/Safari/History.plist " + str(folderPath) + "/Safari/"
                print(cmd)
                subprocess.check_output(cmd, shell=True)
                cmd = "cp -rp /System/Library/StartupItems " + str(folderPath) + "/StartupItems/"
                print(cmd)
                subprocess.check_output(cmd, shell=True)
            except:
                print("Startup Items Error")
        if (bootupTime.get() == 1):
            print("boot time")
            try:
                cmd = "cp -rp /private/var/log/System.log (find 'BOOT_Time') " + str(folderPath) + "/Bootup \Time/"
                print(cmd)
                subprocess.check_output(cmd, shell=True)
            except:
                print("Bootup Time Error")
        if (filesystemLogs.get() == 1):
            print("file logs")
            try:
                cmd = "cp -p ~/Library/Logs/fsck_hfs.log " + str(folderPath) + "/fsck_hfs.log"
                print(cmd)
                subprocess.check_output(cmd, shell=True)
            except:
                print("File System Logs Error")
        if (netInfo.get() == 1):
            print("netinfo")
            try:
                cmd = "cp -p /private/var/log/daily.out " + str(folderPath) + "/daily.out"
                print(cmd)
                subprocess.check_output(cmd, shell=True)
            except:
                print("Network Information Error")
        if (timezone.get() == 1):
            print("timezone")
            try:
                cmd = "cp -p /Library/Preferences/.GlobalPreferences.plist " + str(folderPath) + "/GlobalPreferences.plist"
                print(cmd)
                subprocess.check_output(cmd, shell=True)
            except:
                print("Timezone Information Error")
        if (diskPartition.get() == 1):
            print("disk")
            try:
                cmd = "diskutil list > " + str(folderPath) + "/diskutil.txt"
                print(cmd)
                subprocess.check_output(cmd, shell=True)
            except:
                print("Disk Partition Information Error")
        if (firewallLogs.get() == 1):
            print("firewall")
            try:
                cmd = "cp -p /private/var/log/appfirewall.log " + str(folderPath) + "/appfirewall.log"
                print(cmd)
                subprocess.check_output(cmd, shell=True)
            except:
                print("Firewall Log Error")

        endTime = time.time()
        timeSpent = endTime - startTime
        messagebox.showinfo("", "Done! \n" +  str(round(timeSpent, 2)) + " seconds")
        print("Done")

def main():
    #Creates GUI window
    global win
    win=Tk() #creating the main window and storing the window object in 'win'
    win.title('macOS Monterey Artifact Collector') #setting title of the window
    win.configure(bg='light gray')


    global adminPassword
    adminPassword = StringVar()
    Label(win, text='Enter Administrator Password', bg='light gray').grid(row=0, column=0)
    Entry(win, textvariable=adminPassword, show="*").grid(row=0, column=1)

    global folderPath
    folderPath = ""
    Label(win, text='Select Output Location', bg='light gray').grid(row=1, column=0)
    Button(text="Browse", command=browse_button, bg='light gray').grid(row=1, column=1)



    global sysInfo
    global unifiedLogs
    global installHist
    global sysStartup
    global diagReport
    global crashReport
    global launchDaemon
    global launchAgent
    global sleepImage
    global configPref
    global internetPlugins
    global keychainFiles
    global recentDocs
    global safariHist
    global bootupTime
    global filesystemLogs
    global netInfo
    global timezone
    global diskPartition
    global firewallLogs


    #checkmarks for artifacts to find
    sysInfo = IntVar()
    Checkbutton(win, text='System Info', variable=sysInfo,onvalue=1,offvalue=0,height=5,width=20, bg='light gray').grid(row=4, column = 0, sticky=W)
    installHist = IntVar()
    Checkbutton(win, text='Installation History', variable=installHist,onvalue=1,offvalue=0,height=5,width=20, bg='light gray').grid(row=4, column = 1, sticky=W)
    sysStartup = IntVar()
    Checkbutton(win, text='System Startup Items', variable=sysStartup, onvalue=1, offvalue=0, height=5, width=20, bg='light gray').grid(row=4, column=2, sticky=W)
    unifiedLogs = IntVar()
    Checkbutton(win, text='Unified Logs', variable=unifiedLogs, onvalue=1, offvalue=0, height=5, width=20, bg='yellow').grid(row=5, column=0, sticky=W)
    sleepImage = IntVar()
    Checkbutton(win, text='Sleep Image', variable=sleepImage, onvalue=1, offvalue=0, height=5, width=20, bg='yellow').grid(row=5, column=1, sticky=W)
    configPref = IntVar()
    Checkbutton(win, text='Configuration Preferences', variable=configPref, onvalue=1, offvalue=0, height=5, width=20, bg='yellow').grid(row=5, column=2, sticky=W)
    diagReport = IntVar()
    Checkbutton(win, text='Diagnostic Report', variable=diagReport, onvalue=1, offvalue=0, height=5, width=20, bg='light gray').grid(row=6, column=0, sticky=W)
    crashReport = IntVar()
    Checkbutton(win, text='Crash Reporter', variable=crashReport, onvalue=1, offvalue=0, height=5, width=20, bg='light gray').grid(row=6, column=1, sticky=W)
    internetPlugins = IntVar()
    Checkbutton(win, text='Internet Plugins', variable=internetPlugins, onvalue=1, offvalue=0, height=5, width=20, bg='light gray').grid(row=6, column=2, sticky=W)
    launchDaemon = IntVar()
    Checkbutton(win, text='Launch Daemons', variable=launchDaemon, onvalue=1, offvalue=0, height=5, width=20, bg='light gray').grid(row=7, column=0, sticky=W)
    launchAgent = IntVar()
    Checkbutton(win, text='Launch Agents', variable=launchAgent, onvalue=1, offvalue=0, height=5, width=20, bg='light gray').grid(row=7, column=1, sticky=W)
    keychainFiles = IntVar()
    Checkbutton(win, text='Keychain Files', variable=keychainFiles, onvalue=1, offvalue=0, height=5, width=20, bg='light gray').grid(row=7, column=2, sticky=W)
    recentDocs = IntVar()
    Checkbutton(win, text='Recent Documents', variable=recentDocs, onvalue=1, offvalue=0, height=5, width=20, bg='light gray').grid(row=8, column=0, sticky=W)
    safariHist = IntVar()
    Checkbutton(win, text='Safari Browsing History', variable=safariHist, onvalue=1, offvalue=0, height=5, width=20, bg='light gray').grid(row=8, column=1, sticky=W)
    bootupTime = IntVar()
    Checkbutton(win, text='Bootup Time', variable=bootupTime, onvalue=1, offvalue=0, height=5, width=20, bg='light gray').grid(row=8, column=2, sticky=W)
    filesystemLogs = IntVar()
    Checkbutton(win, text='Filesystem Logs', variable=filesystemLogs, onvalue=1, offvalue=0, height=5, width=20, bg='light gray').grid(row=9, column=0, sticky=W)
    netInfo = IntVar()
    Checkbutton(win, text='Network Information', variable=netInfo, onvalue=1, offvalue=0, height=5, width=20, bg='light gray').grid(row=9, column=1, sticky=W)
    timezone = IntVar()
    Checkbutton(win, text='Timezone', variable=timezone, onvalue=1, offvalue=0, height=5, width=20, bg='light gray').grid(row=9, column=2, sticky=W)
    diskPartition = IntVar()
    Checkbutton(win, text='Disk Partition Info', variable=diskPartition, onvalue=1, offvalue=0, height=5, width=20, bg='light gray').grid(row=10, column=0, sticky=W)
    firewallLogs = IntVar()
    Checkbutton(win, text='Firewall', variable=firewallLogs, onvalue=1, offvalue=0, height=5, width=20,bg='light gray').grid(row=10, column=1, sticky=W)

    #done button
    Button(text="Start", command=checkCheckboxes, bg='light gray').grid(row=10, column=2)

    # displays message explaining application
    messagebox.showinfo("", "This application does not require the administrator password for the system. "
                               "However, Unified Logs, Sleep Image, and System Configurations will not be collected. "
                               "These options are highlighted in yellow.")

    print(folderPath)
    win.mainloop() #running the loop that works as a trigger





main()