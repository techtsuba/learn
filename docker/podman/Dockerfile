# UBIベースのイメージを使用
FROM registry.access.redhat.com/ubi8/ubi:8.9-1

# 必要なパッケージをインストール
RUN dnf -y install curl policycoreutils openssh-server openssh-clients && \
    dnf clean all

# GitLabのリポジトリを追加
RUN curl -sS https://packages.gitlab.com/install/repositories/gitlab/gitlab-ce/script.rpm.sh | bash

# GitLabをインストール
RUN dnf -y install gitlab-ce && \
    dnf clean all

# デフォルトのポートを変更（例：80を8080に、22を2222に）
RUN sed -i 's/external_url 'http:\/\/gitlab.example.com'/external_url 'http:\/\/localhost:8080'/g' /etc/gitlab/gitlab.rb && \
    sed -i 's/# gitlab_rails\['gitlab_shell_ssh_port'\] = 22/gitlab_rails\['gitlab_shell_ssh_port'\] = 2222/g' /etc/gitlab/gitlab.rb

# gitlab.rbをコンテナにコピー
COPY gitlab.rb /etc/gitlab/

# ユーザーを作成してrootでないユーザーで実行
RUN useradd gitlab && chown -R gitlab:gitlab /var/opt/gitlab
USER gitlab

# ポートを公開
EXPOSE 8080 2222

# GitLabサービスを起動
CMD (/opt/gitlab/embedded/bin/runsvdir-start &) && gitlab-ctl reconfigure