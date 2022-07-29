# show wifi profiles on the local PC
netsh wlan show profiles
# show a specific wifi profile
netsh wlan show profile <SSID>
# show wifi password of a profile
netsh wlan show profile <SSID> key=clear
