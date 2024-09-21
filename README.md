# 华东理工大学电量统计

本项目受 [ecust-electricity-statistics](https://github.com/lxl66566/ecust-electricity-statistics) 启发而编写，用于统计华东理工大学的宿舍电量，并绘制折线图。

## 使用方法

1. fork 本仓库
   ![](https://user-images.githubusercontent.com/88281489/205480982-a221a67c-c789-4298-9a45-34a35c820b71.png)

2. 删除仓库里的 `data.js`。

3. 华理信息办 - 微门户 - 电费充值 - 查询您的宿舍电量 - 复制链接
   ![](https://user-images.githubusercontent.com/88281489/205481212-aaca1699-79ef-4c17-b3e3-a7e477ad55db.png)

4. 设置 Secrets 里的 `URL` 为您复制的链接
    ![](https://user-images.githubusercontent.com/88281489/205481390-292a3fc3-fa69-4c2f-886c-b0bc573f5470.png)

5. 部署 Github Pages
   ![](https://user-images.githubusercontent.com/88281489/205528351-399f221b-96e8-4ca5-86d0-32eb6cdb9286.png)

## 许可协议
基于 MIT 协议开源。