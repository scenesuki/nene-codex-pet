# 初始校服宁宁 · 动画预览

所有 GIF 从清理后的最终图集直接裁出单格，未再次缩放或改变人物几何。

- [9 种动作总览](animation-overview.gif)：3 × 3 排列，每个状态完成一个循环；总览统一循环时间，单状态 GIF 保留制作合同的基准时长。
- [16 个注视方向演示](look-directions.gif)：从向上开始，每格 200ms，顺时针排列。应用中由指针位置选择方向。
- [全部帧检查表](contact-sheet.png)；[中性姿态与方向检查表](look-directions.png)。

| 状态 | 预览 | 帧数 | 表现 |
| --- | --- | --- | --- |
| idle | [待机](idle.gif) | 6 | 安静呼吸与眨眼 |
| running-right | [向右移动](running-right.gif) | 8 | 向右的交替步态 |
| running-left | [向左移动](running-left.gif) | 8 | 独立生成的向左步态 |
| waving | [招手](waving.gif) | 4 | 同一侧手臂拘谨招手 |
| jumping | [跳跃](jumping.gif) | 5 | 蓄力、起跳、腾空、下降、落定 |
| failed | [失败](failed.gif) | 8 | 收眉、低落、叹气后恢复 |
| waiting | [等待输入](waiting.gif) | 6 | 轻微举手和询问式歪头 |
| running | [工作中](running.gif) | 6 | 站立托腮思考 |
| review | [检查结果](review.gif) | 6 | 专注审视、歪头和轻微点头 |

单格均为 192 × 208。GIF 持续循环用于检查，应用内播放由 Codex 控制。技术文件记录在 `preview-files-check.json`，完整验收、导入步骤和未验证项见上一层 README。
