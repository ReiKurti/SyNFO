import winreg, os, time
from colorama import init, Fore, Back, Style
init()
os.system('CLS')
# PRETITOLO ------------------------------------------------------------------------------------------
print()
print(Fore.WHITE+Style.BRIGHT+' SyNFO is a simple System Recovery Tool that allows you to know'+Fore.RESET)
print(Fore.WHITE+Style.BRIGHT+' the information of your PC, BIOS and Processor with a click.'+Fore.RESET)
# TITOLO ---------------------------------------------------------------------------------------------
print()
print(Fore.MAGENTA+Style.BRIGHT+' SyNFO 0.5'+Fore.RESET)

print()
# PC INFO ---------------------------------------------------------------------------------------------
print(Fore.CYAN+Style.BRIGHT+'--------------------'+Fore.RESET)
print(Fore.YELLOW+Style.BRIGHT+' PC INFO'+Fore.RESET)
print(Fore.CYAN+Style.BRIGHT+'--------------------'+Fore.RESET)

hKey = winreg.OpenKey (winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows NT\CurrentVersion")
value, type = winreg.QueryValueEx (hKey, "ProductName")
print (' Windows Version      '+Fore.GREEN+Style.BRIGHT+value+Fore.RESET)

hKey = winreg.OpenKey (winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows NT\CurrentVersion")
value, type = winreg.QueryValueEx (hKey, "ProductId")
print (' Serial Number        '+Fore.GREEN+Style.BRIGHT+value+Fore.RESET)

hKey = winreg.OpenKey (winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows NT\CurrentVersion")
value, type = winreg.QueryValueEx (hKey, "CSDVersion")
print (' Service Pack         '+Fore.GREEN+Style.BRIGHT+value+Fore.RESET)

hKey = winreg.OpenKey (winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Internet Explorer")
value, type = winreg.QueryValueEx (hKey, "svcUpdateVersion")
print (' IE Explorer Version  '+Fore.GREEN+Style.BRIGHT+value+Fore.RESET)

print(Fore.CYAN+Style.BRIGHT+'--------------------'+Fore.RESET)
# BIOS INFO --------------------------------------------------------------------------------------------
print(Fore.YELLOW+Style.BRIGHT+' BIOS INFO'+Fore.RESET)
print(Fore.CYAN+Style.BRIGHT+'--------------------'+Fore.RESET)

hKey = winreg.OpenKey (winreg.HKEY_LOCAL_MACHINE, r"HARDWARE\DESCRIPTION\System\BIOS")
value, type = winreg.QueryValueEx (hKey, "BaseBoardManufacturer")
print (' MotherBoard          '+Fore.GREEN+Style.BRIGHT+value+Fore.RESET)

hKey = winreg.OpenKey (winreg.HKEY_LOCAL_MACHINE, r"HARDWARE\DESCRIPTION\System\BIOS")
value, type = winreg.QueryValueEx (hKey, "BaseBoardProduct")
print (' Model                '+Fore.GREEN+Style.BRIGHT+value+Fore.RESET)

hKey = winreg.OpenKey (winreg.HKEY_LOCAL_MACHINE, r"HARDWARE\DESCRIPTION\System\BIOS")
value, type = winreg.QueryValueEx (hKey, "BIOSVersion")
print (' Bios Version         '+Fore.GREEN+Style.BRIGHT+value+Fore.RESET)

hKey = winreg.OpenKey (winreg.HKEY_LOCAL_MACHINE, r"HARDWARE\DESCRIPTION\System\BIOS")
value, type = winreg.QueryValueEx (hKey, "BIOSReleaseDate")
print (' Bios Release Date    '+Fore.GREEN+Style.BRIGHT+value+Fore.RESET)

hKey = winreg.OpenKey (winreg.HKEY_LOCAL_MACHINE, r"HARDWARE\DESCRIPTION\System\BIOS")
value, type = winreg.QueryValueEx (hKey, "SystemProductName")
print (' System Product name  '+Fore.GREEN+Style.BRIGHT+value+Fore.RESET)

hKey = winreg.OpenKey (winreg.HKEY_LOCAL_MACHINE, r"HARDWARE\DESCRIPTION\System\BIOS")
value, type = winreg.QueryValueEx (hKey, "SystemVersion")
print (' System Version       '+Fore.GREEN+Style.BRIGHT+value+Fore.RESET)

print(Fore.CYAN+Style.BRIGHT+'--------------------'+Fore.RESET)

# PROCESSOR INFO -----------------------------------------------------------------------------------------
print(Fore.YELLOW+Style.BRIGHT+' PROCESSOR INFO'+Fore.RESET)
print(Fore.CYAN+Style.BRIGHT+'--------------------'+Fore.RESET)

hKey = winreg.OpenKey (winreg.HKEY_LOCAL_MACHINE, r"HARDWARE\DESCRIPTION\System\CentralProcessor\0")
value, type = winreg.QueryValueEx (hKey, "ProcessorNameString")
print (' Processor Name       '+Fore.GREEN+Style.BRIGHT+value+Fore.RESET)
print(Fore.CYAN+Style.BRIGHT+'--------------------'+Fore.RESET)
# VIDEO CARD INFO -----------------------------------------------------------------------------------------
print(Fore.YELLOW+Style.BRIGHT+' VIDEO CARD INFO'+Fore.RESET)
print(Fore.CYAN+Style.BRIGHT+'--------------------'+Fore.RESET)

hKey = winreg.OpenKey (winreg.HKEY_LOCAL_MACHINE, r"SYSTEM\ControlSet001\Control\Class\{4D36E968-E325-11CE-BFC1-08002BE10318}\0000")
value, type = winreg.QueryValueEx (hKey, "Device Description")
print (' Name                 '+Fore.GREEN+Style.BRIGHT+value+Fore.RESET)

hKey = winreg.OpenKey (winreg.HKEY_LOCAL_MACHINE, r"SYSTEM\ControlSet001\Control\Class\{4D36E968-E325-11CE-BFC1-08002BE10318}\0000")
value, type = winreg.QueryValueEx (hKey, "DriverVersion")
print (' Driver Version       '+Fore.GREEN+Style.BRIGHT+value+Fore.RESET)

hKey = winreg.OpenKey (winreg.HKEY_LOCAL_MACHINE, r"SYSTEM\ControlSet001\Control\Class\{4D36E968-E325-11CE-BFC1-08002BE10318}\0000")
value, type = winreg.QueryValueEx (hKey, "DriverDate")
print (' Driver Date          '+Fore.GREEN+Style.BRIGHT+value+Fore.RESET)
print(Fore.CYAN+Style.BRIGHT+'--------------------'+Fore.RESET)
# OTHER INFO -----------------------------------------------------------------------------------------
print(Fore.YELLOW+Style.BRIGHT+' OTHER INFO'+Fore.RESET)
print(Fore.CYAN+Style.BRIGHT+'--------------------'+Fore.RESET)

hKey = winreg.OpenKey (winreg.HKEY_LOCAL_MACHINE, r"SYSTEM\ControlSet001\Control\Class\{4D36E96B-E325-11CE-BFC1-08002BE10318}\0000")
value, type = winreg.QueryValueEx (hKey, "DriverDesc")
print (' Keyboard             '+Fore.GREEN+Style.BRIGHT+value+Fore.RESET)

hKey = winreg.OpenKey (winreg.HKEY_LOCAL_MACHINE, r"SYSTEM\ControlSet001\Control\Class\{4D36E96C-E325-11CE-BFC1-08002BE10318}\0000")
value, type = winreg.QueryValueEx (hKey, "DriverDesc")
print (' Audio                '+Fore.GREEN+Style.BRIGHT+value+Fore.RESET)

hKey = winreg.OpenKey (winreg.HKEY_LOCAL_MACHINE, r"SYSTEM\ControlSet001\Control\Class\{4D36E96E-E325-11CE-BFC1-08002BE10318}\0000")
value, type = winreg.QueryValueEx (hKey, "DriverDesc")
print (' Monitor              '+Fore.GREEN+Style.BRIGHT+value+Fore.RESET)

hKey = winreg.OpenKey (winreg.HKEY_LOCAL_MACHINE, r"SYSTEM\ControlSet001\Control\Class\{4D36E96F-E325-11CE-BFC1-08002BE10318}\0000")
value, type = winreg.QueryValueEx (hKey, "DriverDesc")
print (' Mouse                '+Fore.GREEN+Style.BRIGHT+value+Fore.RESET)

# EXIT ---------------------------------------------------------------------------------------------------
print(Fore.CYAN+Style.BRIGHT+'--------------------'+Fore.RESET)
print()
print(' Press '+Fore.RED+Style.BRIGHT+'ENTER'+Fore.RESET+' to exit')
input()
exit()
#---------------------------------------------------------------------------------------------------------
