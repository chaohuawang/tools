

# 服务器端启动服务
```bash
systemctl start  rsyncd
systemctl enable rsyncd
```

# 客户端同步方式，服务端要开启 tcp:873 端口

> firewall-cmd --zone=public --add-port=873/tcp --permanent

## 完全与本地目录`/var/lib/s/upload/`同步,本地增加删除都会同步到目标服务器上，需要--delete 参数
> /usr/bin/rsync -rltDvz --delete   --password-file=/etc/rsync.pass  /var/lib/s/upload/   wch@IP::dir_voice

## 只有本地目录`/var/lib/s/upload/`新增才会同步，本地目录删除的不会同步,不需要--delete 参数
> /usr/bin/rsync -rltDvz   --password-file=/etc/rsync.pass  /var/lib/s/upload/   wch@IP::dir_voice

## 本地密码文件`/etc/rsync.pass`,只需要填写密码即可，不需要用户名，密码与服务端一致
