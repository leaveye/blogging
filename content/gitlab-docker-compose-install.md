Title: 使用 Docker Compose 搭建本地 GitLab 服务器
Date: 2016-08-12 10:34
modified: 2016-08-12 14:55
Tags: server, install, gitlab, docker
Category: system
Slug: gitlab-docker-compose-install
Author: Levi G

# 软件安装

> 过程主要参考自 [Omnibus GitLab 官方文档](http://docs.gitlab.com/omnibus/)中 [install GitLab using docker-compose](http://docs.gitlab.com/omnibus/docker/#install-gitlab-using-docker-compose) 章节。

## 设置项选择

|设置项|值|备注|
|-|-|-|
|安装版本|`gitlab-ce`||
|服务器 IP|`192.168.3.12`|Docker 容器|
|工作目录|`~/docker-test`|容器(集)配置所在路径，此次安装主要工作路径|
|服务目录|`~/gitlab`|GitLab 服务使用的文件将保存在此处|
|HTTP 端口|`80`|唯一 Web 服务，可以独占端口|
|SSH 端口|`2201`|Docker 主机使用了缺省的 22 端口|
|访问地址|`http://192.168.3.12`||

## 系统准备

0.  安装 64 位 Ubuntu ([16.04 LTS](http://releases.ubuntu.com/xenial/))。

    > * docker 依赖。

    过程略。
    
    完成后设置服务器 IP 为静态 IP `192.168.3.12`。

0.  安装 `docker-compose`。

    > * 过程参考自 Docker Compose [Install Docker Compose - Ubuntu installation](https://docs.docker.com/engine/installation/linux/ubuntulinux/) 。
    
    > * 这里是全新安装。如果是升级安装请参阅[官方文档](https://docs.docker.com/engine/installation/linux/ubuntulinux/)。

        # 确保 apt 已更新
        sudo apt-get update
        sudo apt-get install apt-transport-https ca-certificates
        
        # 增加 GPG key
        sudo apt-key adv \
        --keyserver hkp://p80.pool.sks-keyservers.net:80 \
        --recv-keys 58118E89F3A912897C070ADBF76221572C52609D
        
        # 更新源列表
        echo 'deb https://apt.dockerproject.org/repo ubuntu-xenial main' > docker.list
        sudo mv -f docker.list /etc/apt/sources.list.d/docker.list
        
        # 更新软件源
        sudo apt-get update
        
        # 安装推荐包
        sudo apt-get install linux-image-extra-$(uname -r)
        
        # 安装并启动 Docker
        sudo apt-get install docker-engine
        sudo service docker start
    
0.  环境准备完成。

## 安装与配置

0.  创建并进入工作路径。

        mkdir -p ~/docker-test
        cd ~/docker-test
        sudo mkdir -p ~/gitlab
        ln -s ~/gitlab gitlab

0.  创建 `docker-compose.yml`。

        cat >docker-compose.yml <<TEXT
        web:
          image: 'gitlab/gitlab-ce:latest'
          restart: always
          hostname: '192.168.3.12'
          environment:
            GITLAB_OMNIBUS_CONFIG: |
              external_url 'http://192.168.3.12'
              # Add any other gitlab.rb configuration here, each on its own line
          ports:
            - '80:80'
            - '443:443'
            - '2201:22'
          volumes:
            - '`readlink -f gitlab`/config:/etc/gitlab'
            - '`readlink -f gitlab`/logs:/var/log/gitlab'
            - '`readlink -f gitlab`/data:/var/opt/gitlab'
        TEXT

0.  首次启动 GitLab 服务。

    > * 需要下载 image ，会耗时，但是有进度条看得到。
    > * 每次启动 GitLab 需等待约 5 分钟才可以开始访问，中间如果在后台做操作可能会使安装失败。

        sudo docker-compose up -d

0.  访问 GitLab 设置 `root` 用户的初始密码。

    浏览器打开 [http://192.168.3.12](http://192.168.3.12) ，在页面中按提示操作。

0.  停止 GitLab 服务。

        sudo docker-compose stop

0.  修改配置文件 `~/gitlab/config/gitlab.rb` 。

    > * 这里<big>不是 Shell 命令</big>，而是文件内容文本。
    > * 文件中配置的详细说明，参见[文档](https://gitlab.com/gitlab-org/omnibus-gitlab/tree/master/doc/settings)。此文件中大多段落也有该段落的文档链接。

        gitlab_rails['gitlab_shell_ssh_port'] = 2201 # default 22

0.  启动 GitLab 服务。

        sudo docker-compose up -d

0.  安装完毕，已可正常使用。

## 管理 GitLab

*   启动 GitLab 服务。

        sudo docker-compose up -d

*   停止 GitLab 服务。

        sudo docker-compose stop

*   销毁 GitLab 服务。（停止服务并删除容器）

        sudo docker-compose down

*   升级 GitLab 服务。

    参见官方文档中 [Update GitLab using Docker compose](http://docs.gitlab.com/omnibus/docker/#update-gitlab-using-docker-compose) 章节。

