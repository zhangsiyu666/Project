#创建Vcenter的虚拟机(centos)

param
(
[string]$vcenter_user=$(throw "Parameter missing: -vcenter_user") ,
[string]$vcenter_password=$(throw "Parameter missing: -vcenter_password") ,
#[string]$vcenter_mip=$(throw "Parameter missing: -vcenter_mip") ,
[string]$work_order=$(throw "Parameter missing: -work_order") ,
#[string]$os_type=$(throw "Parameter missing: -vm_type") ,
[string]$ipt_ip=$(throw "Parameter missing: -ipt_ip") ,
[string]$gateway=$(throw "Parameter missing: -gateway") ,
[string]$ipt_speed=$(throw "Parameter missing: -ipt_speed") ,
[string]$password=$(throw "Parameter missing: -password") ,
[string]$exsi_host=$(throw "Parameter missing: -exsi_host")
)
$os_type="ipt_centos7"
$data_store=$exsi_host #定义磁盘信息
"VCSA User = $vcenter_user"
"VCSA Passwd = $vcenter_password"
"Work Order = $work_order"
"OS = $os_type"
"IP address = $ipt_ip"
"Gateway = $gateway"
"Speed = $ipt_speed"
"Passworf = $password"
"EXSI host = $exsi_host"
"Datastore = $data_store"

#定义vCenter地址
$vcenter_eu_mip = "107.155.16.229"
$vcenter_ap_mip = "107.155.24.55"
$vcenter_cn_mip = "192.254.95.4"
$vcenter_us_mip = "23.236.115.178"


#################以下是固定值不要更改#################

#连接vCenter
Connect-VIServer -Server $vcenter_eu_mip -Port 21859 -Protocol https -Username $vcenter_user -Password $vcenter_password  -force
Connect-VIServer -Server $vcenter_ap_mip -Port 21859 -Protocol https -Username $vcenter_user -Password $vcenter_password  -force
Connect-VIServer -Server $vcenter_cn_mip -Port 21859 -Protocol https -Username $vcenter_user -Password $vcenter_password  -force
Connect-VIServer -Server $vcenter_us_mip -Port 21859 -Protocol https -Username $vcenter_user -Password $vcenter_password  -force

#定义系统用户名和密码
$defaule_username = "root"
$default_password = "TGQKF@123"

#SSH端口
$ssh_port = "21859"

#获取当前日期
$time=get-date

#定义虚拟机名称
$vm_name="$work_order - $os_type - $ipt_ip - $time"


#创建虚拟机
New-vm -VMHost $exsi_host -Name $vm_name -Template $os_type -Datastore $data_store

#开启虚拟机
Start-vm $vm_name
Start-Sleep -Seconds 60

#更改接口速率
Get-VM $vm_name | Get-NetworkAdapter | Where-Object NetworkName -eq "1Gbps" | Set-NetworkAdapter -confirm:$false -Portgroup (Get-VirtualPortGroup -Name $ipt_speed -Standard -VMHost $exsi_host)

#linux脚本序列
$change_ipt_ipv4="nmcli connection modify ens192 ipv4.method manual ipv4.addresses $ipt_ip"
$change_gw="nmcli connection modify ens192 ipv4.gateway $gateway"
$change_password="echo $password | passwd root --stdin > /dev/null 2>&1"
$reboot_system="reboot"


Invoke-VMScript -VM $vm_name -ScriptText $change_ipt_ipv4 -GuestUser $defaule_username -GuestPassword $default_password
Invoke-VMScript -VM $vm_name -ScriptText $change_gw -GuestUser $defaule_username -GuestPassword $default_password
Invoke-VMScript -VM $vm_name -ScriptText $change_password -GuestUser $defaule_username -GuestPassword $default_password
Invoke-VMScript -VM $vm_name -ScriptText $reboot_system -GuestUser $defaule_username -GuestPassword $password
Write-Output "虚拟机名称：$vm_name`n虚拟机IP：$ipt_ip`n虚拟机网速：$ipt_speed`n虚拟机SSH端口：$ssh_port`n虚拟机登录用户名：$defaule_username`n虚拟机登录密码：$password"
Disconnect-VIServer -Server $vcenter_eu_mip -Confirm:$false
Disconnect-VIServer -Server $vcenter_ap_mip -Confirm:$false
Disconnect-VIServer -Server $vcenter_cn_mip -Confirm:$false
Disconnect-VIServer -Server $vcenter_us_mip -Confirm:$false
