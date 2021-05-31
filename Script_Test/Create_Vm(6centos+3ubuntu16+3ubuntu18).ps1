param
(
[string]$ipt_ip1=$(throw "Parameter missing: -ipt_ip1") ,
[string]$ipt_ip2=$(throw "Parameter missing: -ipt_ip2") ,
[string]$ipt_ip3=$(throw "Parameter missing: -ipt_ip3") ,
[string]$ipt_ip4=$(throw "Parameter missing: -ipt_ip4") ,
[string]$ipt_ip5=$(throw "Parameter missing: -ipt_ip5") ,
[string]$ipt_ip6=$(throw "Parameter missing: -ipt_ip6") ,
[string]$ipt_ip7=$(throw "Parameter missing: -ipt_ip7") ,
[string]$ipt_ip8=$(throw "Parameter missing: -ipt_ip8") ,
[string]$ipt_ip9=$(throw "Parameter missing: -ipt_ip9") ,
[string]$ipt_ip10=$(throw "Parameter missing: -ipt_ip10") ,
[string]$ipt_ip11=$(throw "Parameter missing: -ipt_ip11") ,
[string]$ipt_ip12=$(throw "Parameter missing: -ipt_ip12") ,
[string]$gateway=$(throw "Parameter missing: -gateway") ,
[string]$os_password1=$(throw "Parameter missing: -os_password1") ,
[string]$os_password2=$(throw "Parameter missing: -os_password2") ,
[string]$os_password3=$(throw "Parameter missing: -os_password3") ,
[string]$os_password4=$(throw "Parameter missing: -os_password4") ,
[string]$os_password5=$(throw "Parameter missing: -os_password5") ,
[string]$os_password6=$(throw "Parameter missing: -os_password6") ,
[string]$os_password7=$(throw "Parameter missing: -os_password7") ,
[string]$os_password8=$(throw "Parameter missing: -os_password8") ,
[string]$os_password9=$(throw "Parameter missing: -os_password9") ,
[string]$os_password10=$(throw "Parameter missing: -os_password10") ,
[string]$os_password11=$(throw "Parameter missing: -os_password11") ,
[string]$os_password12=$(throw "Parameter missing: -os_password12") ,
[string]$exsi_host=$(throw "Parameter missing: -exsi_host") ,
[string]$model=$(throw "Parameter missing: -model")
)
$os_type1= $model+"_"+"centos7.8"
$os_type2= $model+"_"+"ubuntu16.04"
$os_type3= $model+"_"+"ubuntu18.04"
$data_store = $exsi_host

#定义vCenter账号密码
$vcenter_user = "casey.zhang@zenlayer.com"
$vcenter_password  = "kypjU3#kiHKEQh0n"

#定义vCenter地址

$vcenter_eu_mip = "107.155.16.235"
$vcenter_ap_mip = "107.155.24.41"
$vcenter_cn_mip = "103.239.205.157"
$vcenter_us_mip = "23.236.115.180"
$vcenter_india_mip = "209.177.87.57"

#################以下是固定值不要更改#################

#连接vCenter

Connect-VIServer -Server $vcenter_eu_mip -Port 443 -Protocol https -Username $vcenter_user -Password $vcenter_password  -force
Connect-VIServer -Server $vcenter_ap_mip -Port 443 -Protocol https -Username $vcenter_user -Password $vcenter_password  -force
Connect-VIServer -Server $vcenter_cn_mip -Port 443 -Protocol https -Username $vcenter_user -Password $vcenter_password  -force
Connect-VIServer -Server $vcenter_us_mip -Port 443 -Protocol https -Username $vcenter_user -Password $vcenter_password  -force
Connect-VIServer -Server $vcenter_india_mip -Port 443 -Protocol https -Username $vcenter_user -Password $vcenter_password  -force

#定义系统用户名和密码
$defaule_username = "root"
$default_password = "SalesQKF@123"

#定义系统密码

#SSH端口
$ssh_port = "4229"

#定义虚拟机名称
$vm_name1="$os_type1-login:$ipt_ip1-ssh:$ssh_port-root/$os_password1"
$vm_name2="$os_type1-login:$ipt_ip2-ssh:$ssh_port-root/$os_password2"
$vm_name3="$os_type1-login:$ipt_ip3-ssh:$ssh_port-root/$os_password3"
$vm_name4="$os_type1-login:$ipt_ip4-ssh:$ssh_port-root/$os_password4"
$vm_name5="$os_type1-login:$ipt_ip5-ssh:$ssh_port-root/$os_password5"
$vm_name6="$os_type1-login:$ipt_ip6-ssh:$ssh_port-root/$os_password6"
$vm_name7="$os_type2-login:$ipt_ip7-ssh:$ssh_port-root/$os_password7"
$vm_name8="$os_type2-login:$ipt_ip8-ssh:$ssh_port-root/$os_password8"
$vm_name9="$os_type2-login:$ipt_ip9-ssh:$ssh_port-root/$os_password9"
$vm_name10="$os_type3-login:$ipt_ip10-ssh:$ssh_port-root/$os_password10"
$vm_name11="$os_type3-login:$ipt_ip11-ssh:$ssh_port-root/$os_password11"
$vm_name12="$os_type3-login:$ipt_ip12-ssh:$ssh_port-root/$os_password12"

#创建虚拟机
New-vm -VMHost $exsi_host -Name $vm_name1 -Template $os_type1 -Datastore $data_store
New-vm -VMHost $exsi_host -Name $vm_name2 -Template $os_type1 -Datastore $data_store
New-vm -VMHost $exsi_host -Name $vm_name3 -Template $os_type1 -Datastore $data_store
New-vm -VMHost $exsi_host -Name $vm_name4 -Template $os_type1 -Datastore $data_store
New-vm -VMHost $exsi_host -Name $vm_name5 -Template $os_type1 -Datastore $data_store
New-vm -VMHost $exsi_host -Name $vm_name6 -Template $os_type1 -Datastore $data_store
New-vm -VMHost $exsi_host -Name $vm_name7 -Template $os_type2 -Datastore $data_store
New-vm -VMHost $exsi_host -Name $vm_name8 -Template $os_type2 -Datastore $data_store
New-vm -VMHost $exsi_host -Name $vm_name9 -Template $os_type2 -Datastore $data_store
New-vm -VMHost $exsi_host -Name $vm_name10 -Template $os_type3 -Datastore $data_store
New-vm -VMHost $exsi_host -Name $vm_name11 -Template $os_type3 -Datastore $data_store
New-vm -VMHost $exsi_host -Name $vm_name12 -Template $os_type3 -Datastore $data_store

#开启虚拟机
Start-vm $vm_name1
Start-vm $vm_name2
Start-vm $vm_name3
Start-vm $vm_name4
Start-vm $vm_name5
Start-vm $vm_name6
Start-vm $vm_name7
Start-vm $vm_name8
Start-vm $vm_name9
Start-vm $vm_name10
Start-vm $vm_name11
Start-vm $vm_name12
Start-Sleep -Seconds 60

#linux脚本序列
$change_ipt_ipv4_1="nmcli connection modify ens192 ipv4.method manual ipv4.addresses $ipt_ip1"
$change_gw1="nmcli connection modify ens192 ipv4.gateway $gateway"
$change_password_1="echo $os_password1 | passwd root --stdin > /dev/null 2>&1"
$reboot_system="reboot"

$change_ipt_ipv4_2="nmcli connection modify ens192 ipv4.method manual ipv4.addresses $ipt_ip2"
$change_gw2="nmcli connection modify ens192 ipv4.gateway $gateway"
$change_password_2="echo $os_password2 | passwd root --stdin > /dev/null 2>&1"
$reboot_system="reboot"

$change_ipt_ipv4_3="nmcli connection modify ens192 ipv4.method manual ipv4.addresses $ipt_ip3"
$change_gw3="nmcli connection modify ens192 ipv4.gateway $gateway"
$change_password_3="echo $os_password3 | passwd root --stdin > /dev/null 2>&1"
$reboot_system="reboot"

$change_ipt_ipv4_4="nmcli connection modify ens192 ipv4.method manual ipv4.addresses $ipt_ip4"
$change_gw4="nmcli connection modify ens192 ipv4.gateway $gateway"
$change_password_4="echo $os_password4 | passwd root --stdin > /dev/null 2>&1"
$reboot_system="reboot"

$change_ipt_ipv4_5="nmcli connection modify ens192 ipv4.method manual ipv4.addresses $ipt_ip5"
$change_gw5="nmcli connection modify ens192 ipv4.gateway $gateway"
$change_password_5="echo $os_password5 | passwd root --stdin > /dev/null 2>&1"
$reboot_system="reboot"

$change_ipt_ipv4_6="nmcli connection modify ens192 ipv4.method manual ipv4.addresses $ipt_ip6"
$change_gw6="nmcli connection modify ens192 ipv4.gateway $gateway"
$change_password_6="echo $os_password6 | passwd root --stdin > /dev/null 2>&1"
$reboot_system="reboot"

$change_ipt_ipv4_7="nmcli connection modify ens160 ipv4.method manual ipv4.addresses $ipt_ip7"
$change_gw7="nmcli connection modify ens160 ipv4.gateway $gateway"
$change_password_7="echo root:$os_password7 | chpasswd"
$reboot_system="reboot"

$change_ipt_ipv4_8="nmcli connection modify ens160 ipv4.method manual ipv4.addresses $ipt_ip8"
$change_gw8="nmcli connection modify ens160 ipv4.gateway $gateway"
$change_password_8="echo root:$os_password8 | chpasswd"
$reboot_system="reboot"

$change_ipt_ipv4_9="nmcli connection modify ens160 ipv4.method manual ipv4.addresses $ipt_ip9"
$change_gw9="nmcli connection modify ens160 ipv4.gateway $gateway"
$change_password_9="echo root:$os_password9 | chpasswd"
$reboot_system="reboot"

$change_ipt_ipv4_10="nmcli connection modify ens160 ipv4.method manual ipv4.addresses $ipt_ip10"
$change_gw10="nmcli connection modify ens160 ipv4.gateway $gateway"
$change_password_10="echo root:$os_password10 | chpasswd"
$reboot_system="reboot"

$change_ipt_ipv4_11="nmcli connection modify ens160 ipv4.method manual ipv4.addresses $ipt_ip11"
$change_gw11="nmcli connection modify ens160 ipv4.gateway $gateway"
$change_password_11="echo root:$os_password11 | chpasswd"
$reboot_system="reboot"

$change_ipt_ipv4_12="nmcli connection modify ens160 ipv4.method manual ipv4.addresses $ipt_ip12"
$change_gw12="nmcli connection modify ens160 ipv4.gateway $gateway"
$change_password_12="echo root:$os_password12 | chpasswd"
$reboot_system="reboot"

Invoke-VMScript -VM $vm_name1 -ScriptText $change_ipt_ipv4_1 -GuestUser $defaule_username -GuestPassword $default_password
Invoke-VMScript -VM $vm_name1 -ScriptText $change_gw1 -GuestUser $defaule_username -GuestPassword $default_password
Invoke-VMScript -VM $vm_name1 -ScriptText $change_password_1 -GuestUser $defaule_username -GuestPassword $default_password
Invoke-VMScript -VM $vm_name1 -ScriptText $reboot_system -GuestUser $defaule_username -GuestPassword $os_password1

Invoke-VMScript -VM $vm_name2 -ScriptText $change_ipt_ipv4_2 -GuestUser $defaule_username -GuestPassword $default_password
Invoke-VMScript -VM $vm_name2 -ScriptText $change_gw2 -GuestUser $defaule_username -GuestPassword $default_password
Invoke-VMScript -VM $vm_name2 -ScriptText $change_password_2 -GuestUser $defaule_username -GuestPassword $default_password
Invoke-VMScript -VM $vm_name2 -ScriptText $reboot_system -GuestUser $defaule_username -GuestPassword $os_password2

Invoke-VMScript -VM $vm_name3 -ScriptText $change_ipt_ipv4_3 -GuestUser $defaule_username -GuestPassword $default_password
Invoke-VMScript -VM $vm_name3 -ScriptText $change_gw3 -GuestUser $defaule_username -GuestPassword $default_password
Invoke-VMScript -VM $vm_name3 -ScriptText $change_password_3 -GuestUser $defaule_username -GuestPassword $default_password
Invoke-VMScript -VM $vm_name3 -ScriptText $reboot_system -GuestUser $defaule_username -GuestPassword $os_password3

Invoke-VMScript -VM $vm_name4 -ScriptText $change_ipt_ipv4_4 -GuestUser $defaule_username -GuestPassword $default_password
Invoke-VMScript -VM $vm_name4 -ScriptText $change_gw4 -GuestUser $defaule_username -GuestPassword $default_password
Invoke-VMScript -VM $vm_name4 -ScriptText $change_password_4 -GuestUser $defaule_username -GuestPassword $default_password
Invoke-VMScript -VM $vm_name4 -ScriptText $reboot_system -GuestUser $defaule_username -GuestPassword $os_password4

Invoke-VMScript -VM $vm_name5 -ScriptText $change_ipt_ipv4_5 -GuestUser $defaule_username -GuestPassword $default_password
Invoke-VMScript -VM $vm_name5 -ScriptText $change_gw5 -GuestUser $defaule_username -GuestPassword $default_password
Invoke-VMScript -VM $vm_name5 -ScriptText $change_password_5 -GuestUser $defaule_username -GuestPassword $default_password
Invoke-VMScript -VM $vm_name5 -ScriptText $reboot_system -GuestUser $defaule_username -GuestPassword $os_password5

Invoke-VMScript -VM $vm_name6 -ScriptText $change_ipt_ipv4_6 -GuestUser $defaule_username -GuestPassword $default_password
Invoke-VMScript -VM $vm_name6 -ScriptText $change_gw6 -GuestUser $defaule_username -GuestPassword $default_password
Invoke-VMScript -VM $vm_name6 -ScriptText $change_password_6 -GuestUser $defaule_username -GuestPassword $default_password
Invoke-VMScript -VM $vm_name6 -ScriptText $reboot_system -GuestUser $defaule_username -GuestPassword $os_password6

Invoke-VMScript -VM $vm_name7 -ScriptText $change_ipt_ipv4_7 -GuestUser $defaule_username -GuestPassword $default_password
Invoke-VMScript -VM $vm_name7 -ScriptText $change_gw7 -GuestUser $defaule_username -GuestPassword $default_password
Invoke-VMScript -VM $vm_name7 -ScriptText $change_password_7 -GuestUser $defaule_username -GuestPassword $default_password
Invoke-VMScript -VM $vm_name7 -ScriptText $reboot_system -GuestUser $defaule_username -GuestPassword $os_password7

Invoke-VMScript -VM $vm_name8 -ScriptText $change_ipt_ipv4_8 -GuestUser $defaule_username -GuestPassword $default_password
Invoke-VMScript -VM $vm_name8 -ScriptText $change_gw8 -GuestUser $defaule_username -GuestPassword $default_password
Invoke-VMScript -VM $vm_name8 -ScriptText $change_password_8 -GuestUser $defaule_username -GuestPassword $default_password
Invoke-VMScript -VM $vm_name8 -ScriptText $reboot_system -GuestUser $defaule_username -GuestPassword $os_password8

Invoke-VMScript -VM $vm_name9 -ScriptText $change_ipt_ipv4_9 -GuestUser $defaule_username -GuestPassword $default_password
Invoke-VMScript -VM $vm_name9 -ScriptText $change_gw9 -GuestUser $defaule_username -GuestPassword $default_password
Invoke-VMScript -VM $vm_name9 -ScriptText $change_password_9 -GuestUser $defaule_username -GuestPassword $default_password
Invoke-VMScript -VM $vm_name9 -ScriptText $reboot_system -GuestUser $defaule_username -GuestPassword $os_password9

Invoke-VMScript -VM $vm_name10 -ScriptText $change_ipt_ipv4_10 -GuestUser $defaule_username -GuestPassword $default_password
Invoke-VMScript -VM $vm_name10 -ScriptText $change_gw10 -GuestUser $defaule_username -GuestPassword $default_password
Invoke-VMScript -VM $vm_name10 -ScriptText $change_password_10 -GuestUser $defaule_username -GuestPassword $default_password
Invoke-VMScript -VM $vm_name10 -ScriptText $reboot_system -GuestUser $defaule_username -GuestPassword $os_password10

Invoke-VMScript -VM $vm_name11 -ScriptText $change_ipt_ipv4_11 -GuestUser $defaule_username -GuestPassword $default_password
Invoke-VMScript -VM $vm_name11 -ScriptText $change_gw11 -GuestUser $defaule_username -GuestPassword $default_password
Invoke-VMScript -VM $vm_name11 -ScriptText $change_password_11 -GuestUser $defaule_username -GuestPassword $default_password
Invoke-VMScript -VM $vm_name11 -ScriptText $reboot_system -GuestUser $defaule_username -GuestPassword $os_password11

Invoke-VMScript -VM $vm_name12 -ScriptText $change_ipt_ipv4_12 -GuestUser $defaule_username -GuestPassword $default_password
Invoke-VMScript -VM $vm_name12 -ScriptText $change_gw12 -GuestUser $defaule_username -GuestPassword $default_password
Invoke-VMScript -VM $vm_name12 -ScriptText $change_password_12 -GuestUser $defaule_username -GuestPassword $default_password
Invoke-VMScript -VM $vm_name12 -ScriptText $reboot_system -GuestUser $defaule_username -GuestPassword $os_password12

Write-Output $vm_name1
Write-Output $vm_name2
Write-Output $vm_name3
Write-Output $vm_name4
Write-Output $vm_name5
Write-Output $vm_name6
Write-Output $vm_name7
Write-Output $vm_name8
Write-Output $vm_name9
Write-Output $vm_name10
Write-Output $vm_name11
Write-Output $vm_name12`

Disconnect-VIServer -Server $vcenter_eu_mip -Confirm:$false
Disconnect-VIServer -Server $vcenter_ap_mip -Confirm:$false
Disconnect-VIServer -Server $vcenter_cn_mip -Confirm:$false
Disconnect-VIServer -Server $vcenter_us_mip -Confirm:$false
Disconnect-VIServer -Server $vcenter_india_mip -Confirm:$false
