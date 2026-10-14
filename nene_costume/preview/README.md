# nene_costume 预览与检查

本目录由最终清理后的图集裁格生成，不修改角色比例或动作。

- `animation-overview.gif`：九种状态总览，576×678，总时长1680毫秒。
- `idle.gif`、`running-right.gif`、`running-left.gif`、`waving.gif`、`jumping.gif`、`failed.gif`、`waiting.gif`、`running.gif`、`review.gif`：192×208 单状态预览。
- `look-directions.gif`：16方向顺时针循环，000向上、090向右、180向下、270向左，每步22.5°。
- `contact-sheet.png`、`look-directions.png`：全帧及中性帧与方向对比图。
- `preview-files-check.json`：所有 GIF 帧解码、数量、时长、尺寸及生成时哈希。
- `visual-qa.json`、`direction-semantics.json`、`direction-blind-validation.json`、`blind-review-resolution.json`：独立检查及保留的轻微告警。
- `app-loader-validation.json`：只读重放本机实际图片、版本与路径校验函数，未安装宠物或控制应用界面。

GIF用于预览，最终安装文件为宠物目录顶层的 `pet.json` 和 `spritesheet.webp`。应用设置列表及浮动显示尚未实测。
