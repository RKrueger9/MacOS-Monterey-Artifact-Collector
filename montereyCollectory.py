"""
MacOS Monterey Artifact Collector
@author Ryne Krueger
CSEC-791
"""
import subprocess
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import os



def browse_button():
    global folderPath
    filename = filedialog.askdirectory()
    folderPath = filename
    Label(win, text=folderPath, bg='light gray').grid(row=1, column=3)
    print("browse button: " + folderPath)

def checkCheckboxes():
    global folderPath
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
        if (installHist.get() == 1):
            print("install")
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
                cmd = "cp -rp /Library/Logs/DiagnositcReports " + str(folderPath) + "/DiagnosticReports/"
                print(cmd)
                subprocess.check_output(cmd, shell=True)
            except:
                print("Diagnositc Report Error")
        if (crashReport.get() == 1):
            print("crash")
            try:
                cmd = "cp -rp /Library/Application\ Support/CrashReporter/ " + str(folderPath) + "/"
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
        if (configPref.get() == 1):
            print("config")
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
        if (safariHist.get() == 1):
            print("safari hist")
        if (bootupTime.get() == 1):
            print("boot time")
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

        messagebox.showinfo("", "Done!")
        print("Done")

def main():
    #Creates GUI window
    global win
    win=Tk() #creating the main window and storing the window object in 'win'
    win.title('macOS Monterey Artifact Collector') #setting title of the window
    win.configure(bg='light gray')



    Label(win, text='Enter Administrator Password', bg='light gray').grid(row=0)
    Entry(win).grid(row=0, column=1)

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


    #checkmarks for artifacts to find
    sysInfo = IntVar()
    Checkbutton(win, text='System Info', variable=sysInfo,onvalue=1,offvalue=0,height=5,width=20, bg='light gray').grid(row=4, column = 0, sticky=W)
    unifiedLogs = IntVar()
    Checkbutton(win, text='Unified Logs', variable=unifiedLogs,onvalue=1,offvalue=0,height=5,width=20, bg='light gray').grid(row=4,column = 1, sticky=W)
    installHist = IntVar()
    Checkbutton(win, text='Installation History', variable=installHist,onvalue=1,offvalue=0,height=5,width=20, bg='light gray').grid(row=4, column = 2, sticky=W)
    sysStartup = IntVar()
    Checkbutton(win, text='System Startup Items', variable=sysStartup, onvalue=1, offvalue=0, height=5, width=20, bg='light gray').grid(row=5, column=0, sticky=W)
    diagReport = IntVar()
    Checkbutton(win, text='Diagnostic Report', variable=diagReport, onvalue=1, offvalue=0, height=5, width=20, bg='light gray').grid(row=5, column=1, sticky=W)
    crashReport = IntVar()
    Checkbutton(win, text='Crash Reporter', variable=crashReport, onvalue=1, offvalue=0, height=5, width=20, bg='light gray').grid(row=5, column=2, sticky=W)
    launchDaemon = IntVar()
    Checkbutton(win, text='Launch Daemons', variable=launchDaemon, onvalue=1, offvalue=0, height=5, width=20, bg='light gray').grid(row=6, column=0, sticky=W)
    launchAgent = IntVar()
    Checkbutton(win, text='Launch Agents', variable=launchAgent, onvalue=1, offvalue=0, height=5, width=20, bg='light gray').grid(row=6, column=1, sticky=W)
    sleepImage = IntVar()
    Checkbutton(win, text='Sleep Image', variable=sleepImage, onvalue=1, offvalue=0, height=5, width=20, bg='light gray').grid(row=6, column=2, sticky=W)
    configPref = IntVar()
    Checkbutton(win, text='Configuration Preferences', variable=configPref, onvalue=1, offvalue=0, height=5, width=20, bg='light gray').grid(row=7, column=0, sticky=W)
    internetPlugins = IntVar()
    Checkbutton(win, text='Internet Plugins', variable=internetPlugins, onvalue=1, offvalue=0, height=5, width=20, bg='light gray').grid(row=7, column=1, sticky=W)
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

    #done button
    Button(text="Start", command=checkCheckboxes, bg='light gray').grid(row=10, column=2)

    print(folderPath)
    win.mainloop() #running the loop that works as a trigger



main()