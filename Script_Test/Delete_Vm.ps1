#此脚本用于删除Vcenter上的虚拟机，匹配规则为引号内的虚拟机名称
#./delete_ipt_vm.ps1 -vcenter_user 'casey.zhang@zenlayer.com' -vcenter_password 'ypjU3#kiHKEQh0' -work_order 'xxxx'

param
(
[string]$vcenter_user=$(throw "Parameter missing: -vcenter_user") ,
[string]$vcenter_password=$(throw "Parameter missing: -vcenter_password") ,
[string]$work_order=$(throw "Parameter missing: -work_order") 
)
"VCSA User = $vcenter_user"
"VCSA Passwd = $vcenter_password"
"Work Order = $work_order"

$vcenter_eu_mip = "107.155.16.229"
$vcenter_ap_mip = "107.155.24.55"
$vcenter_cn_mip = "192.254.95.4"
$vcenter_us_mip = "23.236.115.178"

##写死遍历后统一断开
Connect-VIServer -Server $vcenter_eu_mip -Port 21859 -Protocol https -Username $vcenter_user -Password $vcenter_password  -force
Connect-VIServer -Server $vcenter_ap_mip -Port 21859 -Protocol https -Username $vcenter_user -Password $vcenter_password  -force
Connect-VIServer -Server $vcenter_cn_mip -Port 21859 -Protocol https -Username $vcenter_user -Password $vcenter_password  -force
Connect-VIServer -Server $vcenter_us_mip -Port 21859 -Protocol https -Username $vcenter_user -Password $vcenter_password  -force
$vm_name = (Get-VM | where {$_.Name -match $work_order}).Name
"Delete VM name = $vm_name"
Stop-VM $vm_name -Confirm:$false
Start-Sleep -Seconds 10
Remove-VM $vm_name -Confirm:$false

$?

Disconnect-VIServer -Server $vcenter_eu_mip -Confirm:$false
Disconnect-VIServer -Server $vcenter_ap_mip -Confirm:$false
Disconnect-VIServer -Server $vcenter_cn_mip -Confirm:$false
Disconnect-VIServer -Server $vcenter_us_mip -Confirm:$false