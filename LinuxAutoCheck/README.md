# 使用方法
1、配置ansible配置文件，使其能够批量操作远程（被巡检）主机<br>
2、配置sEmail.py 里面的邮件帐号、收发件人等信息（如需要发送邮件）<br>
3、修改inspection.sh默认的巡检项内容（如需要）<br>
4、保持wxlsx.py的title内容与巡检结果中巡检内容一致，否刚EXCEL中无法正常生成<br>
5、运行run.sh（可以配置在crontab中）<br>
