sudo nmcli con add type ethernet ifname enx6c6e071538f5 con-name lucid_gige
sudo nmcli con mod lucid_gige ipv4.method manual
sudo nmcli con mod lucid_gige ipv4.addresses 169.254.245.10/16
sudo nmcli con mod lucid_gige ipv6.method ignore
sudo nmcli con mod lucid_gige connection.autoconnect yes
sudo nmcli con mod lucid_gige connection.interface-name enx6c6e071538f5
sudo nmcli con up lucid_gige