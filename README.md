# Order Coach

## 项目简介

本项目用于自动预约应县金土地驾校的科目二课程，旨在帮助学员更加快速便捷地练习。

* 程序运行的原理为发送http请求，与网页点击的效果一致。
* 本项目基于Github的Action功能运作。

## 免责声明

* 作者对项目的最终效果**不作任何保证**，即**不能保证预约一定成功**。作者**不承担由于使用该项目引起的任何损失**。
* 作者不对任何**经他人（包括但不限于非作者本人的个人、团体、组织等）修改后**的代码负责。

## 版权声明

本项目遵循AGPL 3.0开源协议，您在使用和传播时应当遵循该协议。<br></br>
Order_Coach © 2021 by [ZXY ](https://github.com/zhao0349)is licensed under AGPL 3.0

## 使用教程

由于众所周知的科学原因，GitHub上readme文件中的图片无法显示，故以下教程均为纯文字。

### 步骤 0  声明

**请确保您已阅读并理解免责声明与版权声明！**<br></br>
**继续进行后续步骤，即代表您同意上述各条款；如不同意，请立即退出本项目。**

### 步骤 1  fork代码

1. 登录你的GitHub账号（如果没有，请先注册一个）。
2. 点击项目右上角的“fork”，将项目复制到你的仓库中。
   成功后，你的账号下将出现一个完全相同的项目。
3. 接下来的**所有步骤**将在该项目（**你的账号中的同名项目**）下执行。

### 步骤 2  部署代码

首先，确保你已转到**你的仓库**，即地址栏显示内容为：

> https://github.com/**(你的用户名)**/Order_Coach

#### 2.1 获取coachID

1. 使用电脑端chromium内核浏览器（如Chrome，新Edge，国产浏览器的“极速模式”等），转到[驾校约车网址](http://yyyxjtdjx.ay001.net/Login.htm)并登录。
2. 找到你要预约的教练，右击其头像，选择“检查元素”。
3. 在开发人员工具的“元素”选项卡（一般情况下，默认就是”元素“选项卡）中，找到所选行上方以”ygd+数字“开头的教练编号(即CoachID)，复制备用。*（如`ygd201807070002`）*

#### 2.2 修改代码

1. 在Github的“code”选项卡下，点击“main.py”，然后点击代码预览框右上角的铅笔图标，进入编辑状态。
   ps. 如果会的话，也可以连接到VS Code，使用VS Code编辑。
2. 将这一行代码中的教练代码替换为你想预约的教练的代码。

```
cid = str("ygd201706050003") #此处为康教练的coachID，届时请自行修改
```

3. 将下方的代码也按照注释进行修改

#### 2.3 设置secret

1. 点击本项目的“settings”，然后选择左边栏中的“secret”，点击右上角的“New repository secret”。
2. 在“Name”栏中输入“USERNAME”，Value栏中输入你的身份证号，然后点击下方的“Add Secret”。
3. 重复一遍上述步骤，再新建一个Secret，Name为“PASSWORD”，Value为你的手机号。

<br/>

**至此，代码部署已基本完成，可以正常使用。但是GitHub的定时器经常不准，可能导致5:50以后脚本才启动，为此可以额外使用腾讯云函数来充当触发器。**

### 步骤 3 设置额外触发器（可选）

1. 点击GitHub页面右上角你的头像，点击“Settings”，进入个人账户的设置页面（不是项目设置）。
2. 选择 Developer settings -> Personal access tokens -> Generate new token。
3. 设置名字为 **ORDER** , 然后勾选repo，点击 Generate token ，最后**立刻复制保存**生成的github密钥（一旦离开或刷新页面就看不到了）。
4. 按照这个网页的方法，部署腾讯云函数：[GithubAction的Schedule运行不准时的解决办法_白描描描描描描描描描-CSDN博客](https://blog.csdn.net/l1937gzjlzy/article/details/117753465)
5. 代码按照这样的格式输入即可：

```
import requests
import json

def run():
        payload = json.dumps({"ref": "main"})
        header = {'Authorization': 'token （刚才复制的密钥）',   #例如{'Authorization': 'token 123456'
                  "Accept": "application/vnd.github.v3+json"}
        response_decoded_json = requests.post(
            f'https://api.github.com/repos/（你的用户名）/Order_Coach/actions/workflows/main.yml/dispatches',
            data=payload, headers=header)
def main_handler(event, context):
    return run()
```

**至此，部署工作全部结束。如果运行出现异常，你的GitHub绑定的邮箱会收到邮件。但这里仍然建议每天早上去看看约到了没，至少前几天去看看，万一出现异常了呢(｀・ω・´)**

## 关闭脚本

* 若想要关闭脚本，请转到“**Actions**”选项卡，在左侧列表中找到“**Order**”并点击，在运行记录框的右上角有一个“**…**”按钮（三个点），点击后选择弹出菜单中的“**Disable workflow**”即可。看到运行记录上方有一个橙色叹号框，显示“**⚠️  This workflow was disabled manually.**”即表示已关闭脚本。
* 若要重新开启，点击橙色叹号框右边的“**Enable workflow**”按钮即可。

## 联系作者

### 如遇到问题，可以按如下方式联系作者：

* **QQ号：2932123724**（小号，不一定经常在线）
* **微信号：star223333**（当然也是小号）
* **邮箱**（听说国际友人喜欢用电子邮件？🤔）：**zxy0349@vip.qq.com（这个是大号，拒绝垃圾邮件轰炸）**（不会吧不会吧，不会真的有国际友人吧？）
* **此外，遇到bug也可以通过提交Issues来反馈。**
