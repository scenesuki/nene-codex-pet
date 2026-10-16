[← 返回宠物合集](../README.md)

# 草薙宁宁 · 江戸の町並みに飲まれて

二星卡960的黑绿复古洋装，采用Q版日系插画。保留平顶小礼帽、灰绿长发、紫色眼睛、黑色手套和金边青绿色折扇。卡面未露出的下半身按用户确认补全为及踝黑绿长裙与黑色圆头系带短靴，属于同人演绎。

<img src="preview/readme-portrait.png" alt="草薙宁宁黑绿复古洋装静态预览" width="144">

**`nene_edo`** · 江户风宁宁 · Q版日系插画 · 9种动画 · 16个注视方向

## 动画与下载

[查看动画总览](preview/animation-overview.gif) · [查看注视方向](preview/look-directions.gif) · [全部预览](preview/README.md)

本套已纳入 [v1.6.2七套完整合集](https://github.com/scenesuki/nene_codex_pets/releases/tag/v1.6.2)，包含全部预览与校验和。本地发布附件位于 `release-assets/v1.6.2/`；此前v1.5.0为未发布的制作快照。最终导入文件为本目录顶层的 [pet.json](pet.json) 和 [spritesheet.webp](spritesheet.webp)。

## 安装

将本套顶层的 `pet.json` 和 `spritesheet.webp` 一起复制到 `~/.codex/pets/nene_edo/`。Windows默认为 `%USERPROFILE%\.codex\pets\nene_edo\`；自定义 `CODEX_HOME` 时使用其下的 `pets/nene_edo/`。在Codex设置 > Pets中刷新并选择「nene_edo」，必要时重启应用。本套已于2026-10-15安装至 `C:\Users\tieha\.codex\pets\nene_edo\`，两个导入文件与项目成品逐字节一致，未切换当前宠物；见 [安装校验](installed-validation.json)。

<details>
<summary>规格与验收</summary>

- 2026-10-15只读核实本机 `OpenAI.Codex_26.1007.9446.0` 的加载器与渲染器，证据及模块SHA-256见 [app-contract-verification.json](source/references/app-contract-verification.json)。
- v2图集1536×2288，8列11行，单格192×208，无损RGBA WebP，`spriteVersionNumber: 2`。九状态为idle、running-right、running-left、waving、jumping、failed、waiting、running、review，帧数6/8/8/4/5/8/6/6/6；后两行为从正上方000°开始、顺时针每22.5°一格的16方向。
- 应用读取 `CODEX_HOME/pets/<pet-id>/pet.json`，两个导入文件在同一目录顶层；依据是本机实际Codex应用。文件检查、视觉检查和应用内导入分别记录。
- [图集结构校验](validation.json)通过，无错误或警告，隐藏RGB残留为0。完整8×11图集只执行一次最终边缘处理，alpha保持逐字节一致，未进行后续叠加清理。
- 九状态经过独立逐帧检查；左右移动分别绘制，保留折扇与帽饰侧别；跳跃使用共享取景框，保留源图中实际的起落高度。`failed`与`review`动作幅度克制但可辨，`running`是双脚站定、右手近下巴的思考状态。
- 四个正方向先通过检查，再整行生成两组八方向；后八方向严格复用前八方向的注册结果与尺度。三名隔离盲测均正确辨认000°上、090°右、180°下、270°左。
- 已接受的细微说明：022.5°、067.5°、112.5°的纵向分量，以及135°、157.5°的横向分量在隔离盲测中较难辨认。带标签的原尺寸顺序复核确认象限正确、没有方向倒转。
- 157.5°→180°、337.5°→000°的头部与帽子换姿比相邻帧明显。最初独立复核将其判为跳变，追加的原尺寸相邻帧复核与项目主验收确认脚底、裙摆及身体锚点稳定，没有整体缩放跳变或身份变化，按细微限制接受。原始不同意见与依据均保留在 `source/qa/final-visual-qa-initial-worker.json`、`boundary-severity-review.json`及`blind-review-resolution.json`。
- 全部GIF已逐帧解码并核对帧数、时长，独立视觉复核查看实际解码帧；尚未验证GIF播放器实际播放。连续性检查未发现内部透明破洞。记录见 `source/qa/preview-files-check.json`与`final-visual-qa.json`。
- [本机加载算法校验](preview/app-loader-validation.json)通过：重放实际应用的图片、版本和路径验证函数。已安装并通过 [安装文件校验](installed-validation.json)，未切换当前宠物；应用设置识别、选用及桌面浮动显示尚未实测。
- 其他五套宠物的十个导入文件保持原样。静态展示图是最终图集待机首帧原始RGBA像素的192×208裁切；本地链接和像素一致性另有检查。本次未进行README桌面/窄屏实屏及折叠交互验证。
- 当前验收见 `source/qa/delivery-check.json`，制作进度见 [progress.json](source/qa/progress.json)。

</details>

<details>
<summary>参考与制作记录</summary>

- [SEGA官方活动公告](https://prtimes.jp/main/html/rd/p/000005855.000005397.html)明确列出二星草薙宁宁及对应卡面，活动为「お縄を頂戴！？天馬捕物帳」。本套服装是黑绿复古洋装；标题中的江户街景并不代表角色穿和服。
- [卡面高清公开镜像](https://anihonetwallpaper.com/post/54207)用于衣饰细节，与官方公告卡图交叉核对。[游戏数据镜像](https://github.com/Sekai-World/sekai-master-db-diff/blob/main/cards.json)用于核对卡960、角色15、二星、cute及 `res015_no036`；镜像并非官方来源。来源URL、快照与下载SHA-256保存在本套 `source/references/`。
- [官方角色资料](https://pjsekai.sega.jp/character/unite04/nene/index.html)提供性格依据：不擅社交、说话直率，喜欢游戏、音乐剧和电影，擅长歌唱与机器操作。安静眨眼、拘谨招手、期待回应、认真思考和审视点头是据此设计的创作演绎，不作为官方剧情动作。
- 左手固定握持展开的折扇，右手用于招手、请求回应或思考；左右移动分别生成，保留帽饰和道具的侧别。未露出的鞋履及裙摆由用户确认补全。
- 制作源素材与 `source/` 验收明细留在项目目录，分发ZIP不包含源素材。
- 详细设计见 [design-brief.md](source/references/design-brief.md)，注视机制见 [look-mechanics.md](source/qa/look-mechanics.md)。制作工具代码参考既有 `nene_movie` 流程，本套使用自己的角色与动画素材。

</details>
