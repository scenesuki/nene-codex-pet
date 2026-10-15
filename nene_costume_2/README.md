[← 返回宠物合集](../README.md)

# 草薙宁宁 · ワンダーランズ×ショウタイム

以二星卡「ワンダーランズ×ショウタイム」的初始舞台服为参考，采用Q版日系插画，整体采用紧凑的Q版比例。保留青绿无袖马甲、浅黄百褶裙、粉色蝴蝶结与蝶叶头饰。

<img src="preview/readme-portrait.png" alt="草薙宁宁初始舞台服静态预览" width="144">

**`nene_costume_2`** · Q版日系插画 · 9种动画 · 16个注视方向

## 动画与下载

[查看动画总览](preview/animation-overview.gif) · [查看注视方向](preview/look-directions.gif) · [全部预览](preview/README.md)

本套包含于 **[五套完整合集 · v1.4.0](https://github.com/scenesuki/nene_codex_pets/releases/download/v1.4.0/nene_codex_pets-v1.4.0.zip)**，下载后使用同版 [SHA256SUMS.txt](https://github.com/scenesuki/nene_codex_pets/releases/download/v1.4.0/SHA256SUMS.txt) 核对校验和。本地副本位于 `release-assets/v1.4.0/`。

## 安装

1. 解压本地五套合集，使用同版 `SHA256SUMS.txt` 核对校验和；也可直接使用仓库中的本套目录。
2. 将 `nene_costume_2/` 复制到 `~/.codex/pets/`，确保 `pet.json` 与 `spritesheet.webp` 同时位于该目录顶层。
3. 在Codex设置 > Pets中刷新并选择「nene_costume_2」；必要时重启应用。

Windows默认位置为 `%USERPROFILE%\.codex\pets\nene_costume_2\`；自定义 `CODEX_HOME` 时使用其下的 `pets/nene_costume_2/`。

本套已于2026-10-14安装到 `%USERPROFILE%\.codex\pets\nene_costume_2\`，两个导入文件与本目录成品逐字节一致；[安装校验](installed-validation.json)已通过本机应用的图片、版本与路径验证函数。尚未切换当前宠物，应用设置识别、选用及实际浮动显示仍未实测。

<details>
<summary>规格与验收 · 展开查看</summary>

### 目标规格与来源

2026-10-14只读检查本机 `OpenAI.Codex_26.1007.9446.0` 的实际加载器与渲染器。v2图集为1536×2288，8列11行，每格192×208；`spriteVersionNumber: 2`。来源摘录与模块SHA-256见 [app-contract-verification.json](source/references/app-contract-verification.json)。

0–8行为idle、running-right、running-left、waving、jumping、failed、waiting、running、review，帧数分别为6、8、8、4、5、8、6、6、6。9–10行为顺时针16个注视方向，以向上为0°，每步22.5°；空白格完全透明。采用无损RGBA WebP。

应用从 `CODEX_HOME/pets/<pet-id>/pet.json` 加载，默认Windows目录为 `%USERPROFILE%\.codex\pets\`；清单与 `spritesheet.webp` 同处宠物目录顶层。下划线ID符合当前加载器规则。ChatGPT Work Pets的规格不作为本项目依据。

### 验收记录（2026-10-14）

- 导入入口为顶层 `pet.json` 与 `spritesheet.webp`。结构、透明度、全部GIF帧与独立视觉检查通过；图集仅进行一次边缘处理，alpha保持不变。
- 九种状态保持统一的紧凑Q版比例；左右移动分别绘制，跳跃使用共享取景框分格，保留起落轨迹。
- 最终GIF按顺序检查全部实际解码帧，并核对帧数与时长；实时播放尚未实测。
- 四个正方向通过三名隔离盲测。022.5°、337.5°的视线差异较含蓄，带标签循环复核未见错误象限或方向倒转；157.5°→180°和337.5°→000°差异指标较高，独立复核未见明显跳变。
- [方向语义](source/qa/direction-semantics.json)、[独立视觉验收](source/qa/final-visual-qa.json)、[动画文件检查](source/qa/preview-files-check.json)和[交付检查](source/qa/delivery-check.json)均对应当前成品。
- [安装校验](installed-validation.json)确认两个本机导入文件与成品逐字节一致，并通过本机应用的图片、版本与路径验证函数。应用设置识别、选用及实际浮动显示尚未实测，未切换当前宠物。


</details>

<details>
<summary>参考与制作记录 · 展开查看</summary>

- [官方草薙宁宁角色资料与PAST立绘](https://pjsekai.sega.jp/character/unite04/nene/index.html)：人物性格、初始舞台服与配色依据。[原始立绘](https://pjsekai.sega.jp/assets/data/webp/character/unite04/nene/past/img.png.webp)中的绿色偏移图形不属于服装，宠物不保留该图形投影。
- [游戏数据镜像](https://github.com/Sekai-World/sekai-master-db-diff/blob/main/cards.json)：卡片58、角色15、二星、`res015_no002`，标题「ワンダーランズ×ショウタイム」。本套[数据快照](source/references/card-58-game-data.json)及[来源哈希](source/references/sources.json)已保留；该镜像不是官方站点。
- 官方设定：怕生、说话直率，喜欢对战游戏、音乐剧和电影，擅长唱歌与机器操作。创作演绎：安静眨眼、拘谨招手、小幅舞台跳跃、等待询问、专注思考与认真审视。
- 与 `nene_costume` 的Brand New Style新舞台服分别存放；本套不使用羽毛白花、长手套、泡泡袖、白色上身和青绿主裙。
- 素材使用内置imagegen生成，hatch-pet脚本负责分格、组装和检查；当前设计规格、原始生成图、分帧和有效验收资料保存在本套 `source/`。不更改其他套宠物的成品。
- 详细设计依据见[design-brief.md](source/references/design-brief.md)，制作进度见[progress.json](source/qa/progress.json)，源素材索引见[source/README.md](source/README.md)。

</details>
