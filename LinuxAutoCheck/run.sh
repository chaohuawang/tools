#!/bin/bash
#功能：Linux自动批量巡检
#作者：王超华
kworkdir=$(cd $(dirname $0); pwd)
cd ${kworkdir}
ansible all -m copy -a "src=./inspection.sh dest=/tmp"
ansible all -m command -a 'bash /tmp/inspection.sh'
ansible all -m fetch -a "src=/home/monitor.txt dest=./"
find ./ -name "monitor.txt"|xargs cat > monitor_hebing.txt
python wxlsx.py 
#配置邮件推送结果
#dt=`date +'%F %T'`
#python sEmail.py "巡检报告-${dt}" Monitor.xlsx 
