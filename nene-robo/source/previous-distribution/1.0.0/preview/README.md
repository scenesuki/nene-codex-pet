# 宁宁机器人动画预览

- [九种状态总览](animation-overview.gif)
- [十六方向演示](look-directions.gif)：从向上开始，顺时针每22.5°一格，每格200ms；应用中由指针位置选择方向。
- [全部帧检查表](contact-sheet.png)、[中性与方向检查表](look-directions.png)

| 状态 | 预览 | 帧数 | 表现 |
| --- | --- | --- | --- |
| idle | [待机](idle.gif) | 6 | 小幅待机与眨眼 |
| running-right | [右移](running-right.gif) | 8 | 右向交替机械步态 |
| running-left | [左移](running-left.gif) | 8 | 独立绘制左向步态 |
| waving | [招手](waving.gif) | 4 | 小手抬到脸旁并收回 |
| jumping | [弹跳](jumping.gif) | 5 | 小幅机械跳跃并落定 |
| failed | [故障反应](failed.gif) | 8 | 低头闭眼、垂手后恢复 |
| waiting | [等待输入](waiting.gif) | 6 | 胸前询问手势与期待歪头 |
| running | [工作中](running.gif) | 6 | 小幅左右拳交替运算 |
| review | [结果审视](review.gif) | 6 | 手近下巴、专注审查 |

单格192×208；这些GIF从最终清理后的图集裁出，未改变人物几何。总览把每种状态各一完整循环放入同一时间轴；单状态GIF保留基准时长。GIF颜色受格式调色板限制，实际宠物使用无损RGBA WebP。
