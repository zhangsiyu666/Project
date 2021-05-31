param
(
[string]$ipt_ip=$(throw "Parameter missing: -ipt_ip") ,
[string]$gateway=$(throw "Parameter missing: -gateway") ,
[string]$os_password=$(throw "Parameter missing: -password") ,
[string]$exsi_host=$(throw "Parameter missing: -exsi_host") , 
[string]$model=$(throw "Parameter missing: -model")
)
$os_type = $model+"_"+"ubuntu16.04"
$data_store = $exsi_host
$ipt_speed = "100Mbps"

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

#SSH端口
$ssh_port = "4229"

#定义虚拟机名称
$vm_name="$os_type-login:$ipt_ip-ssh_port:$ssh_port-root/$os_password"

#创建虚拟机
New-vm -VMHost $exsi_host -Name $vm_name -Template $os_type -Datastore $data_store

#开启虚拟机
Start-vm $vm_name
Start-Sleep -Seconds 60

#linux脚本序列
$change_ipt_ipv4 = "nmcli connection modify ens160 ipv4.method manual ipv4.addresses $ipt_ip"
$change_gw = "nmcli connection modify ens160 ipv4.gateway $gateway"
$change_password = "echo root:$os_password | chpasswd"
$reboot_system = "reboot"

Invoke-VMScript -VM $vm_name -ScriptText $change_ipt_ipv4 -GuestUser $defaule_username -GuestPassword $default_password
Invoke-VMScript -VM $vm_name -ScriptText $change_gw -GuestUser $defaule_username -GuestPassword $default_password
Invoke-VMScript -VM $vm_name -ScriptText $change_password -GuestUser $defaule_username -GuestPassword $default_password
Invoke-VMScript -VM $vm_name -ScriptText $reboot_system -GuestUser $defaule_username -GuestPassword $os_password
Write-Output "虚拟机名称：$vm_name`n虚拟机IP：$ipt_ip`n虚拟机网速：$ipt_speed`n虚拟机SSH端口：$ssh_port`n虚拟机登录用户名：$defaule_username`n虚拟机登录密码：$os_password"
Disconnect-VIServer -Server $vcenter_eu_mip -Confirm:$false
Disconnect-VIServer -Server $vcenter_ap_mip -Confirm:$false
Disconnect-VIServer -Server $vcenter_cn_mip -Confirm:$false
Disconnect-VIServer -Server $vcenter_us_mip -Confirm:$false
Disconnect-VIServer -Server $vcenter_india_mip -Confirm:$false
