# 华东理工大学电量统计

本项目受 [ecust-electricity-statistics](https://github.com/lxl66566/ecust-electricity-statistics) 启发而编写，用于统计华东理工大学的宿舍电量，并绘制折线图。

## 使用方法

1. fork 本仓库

2. 删除仓库里的 `data.js`。

3. 华理信息办 - 微门户 - 电费充值 - 查询您的宿舍电量 - 复制链接

4. 设置 Secrets 里的 `URL` 为您复制的链接

5. (可选) 设置 Secrets 里的 `PUSH_PLUS_TOKEN` 为您的[推送加](https://www.pushplus.plus/) token。（仅用于推送低电量提醒）

6. 部署 Github Pages

## 许可协议
基于 MIT 协议开源。