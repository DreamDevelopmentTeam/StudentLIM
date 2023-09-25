# Windows10 局域网 MSG 命令通信无法使用解决方案

修改注册表：

```text
HKEY_LOCALMACHINE->System->CurrentControlSet->Control->TerminalServer

AllowRemoteRPC == 0 -> 1
```

---

凭据管理器：

**添加windows凭据 => 对方电脑IP地址,对方电脑用户名,对方电脑密码**

然后使用MSG命令发送消息即可：

```bat
msg /SERVER:目标IP地址 * "消息内容"
```

