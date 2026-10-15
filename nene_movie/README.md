[← 返回宠物合集](../README.md)

# 草薙宁宁 · Let's enjoy the movie！

二星卡1084的观影造型，采用Q版日系插画，保留黄色发结、格纹上衣、奶油色背带裙和红白爆米花桶。卡面未露出的长裙下摆与深棕圆头平底鞋由用户确认后补全，属于同人演绎。

<img src="preview/readme-portrait.png" alt="草薙宁宁观影造型静态预览" width="144">

**`nene_movie`** · Q版日系插画 · 9种动画 · 16个注视方向

## 动画与下载

[查看动画总览](preview/animation-overview.gif) · [查看注视方向](preview/look-directions.gif) · [全部预览](preview/README.md)

本套纳入本地五套合集 `nene_codex_pets-v1.4.0.zip`，位于 `release-assets/v1.4.0/`，同目录提供 `SHA256SUMS.txt`。本版尚未上传GitHub或发布线上Release。现有ZIP保留安装前快照及原校验和，后续安装记录见本页。

## 安装

解压并核对同版SHA-256后，将本套顶层 `pet.json` 和 `spritesheet.webp` 一起复制至 `~/.codex/pets/nene_movie/`。Windows默认为 `%USERPROFILE%\.codex\pets\nene_movie\`；自定义 `CODEX_HOME` 时使用其下的 `pets/nene_movie/`。在Codex设置 > Pets中刷新并选择「nene_movie」，必要时重启应用。本套已于2026-10-15安装至 `C:\Users\tieha\.codex\pets\nene_movie\`，两个导入文件与工作区成品逐字节一致，未切换当前宠物；记录见 [安装校验](installed-validation.json)。

<details>
<summary>规格与验收</summary>

- 2026-10-15重新只读核实本机 `OpenAI.Codex_26.1007.9446.0` 的加载器与渲染器，证据及模块SHA-256见 [app-contract-verification.json](source/references/app-contract-verification.json)。
- v2图集为1536×2288、8列11行、单格192×208，无损RGBA WebP，`spriteVersionNumber: 2`。九状态依次为idle、running-right、running-left、waving、jumping、failed、waiting、running、review，帧数6/8/8/4/5/8/6/6/6。后两行以向上为000°，顺时针16方向，每步22.5°；空白格全透明。
- 应用读取 `CODEX_HOME/pets/<pet-id>/pet.json`，清单与图集位于同一目录顶层；下划线ID符合当前加载器规则。依据是本机实际应用，未借用ChatGPT Work Pets规格。
- 当前导入入口为 [pet.json](pet.json) 与 [spritesheet.webp](spritesheet.webp)，[结构校验](validation.json)通过；图集尺寸、透明度、空白格与隐藏RGB检查无错误或警告。仅执行一次最终边缘处理，alpha字节保持不变。
- 九组动画分别生成并经过逐帧复核；为保留原图中的起跳高度，跳跃采用共享取景框分格，确认未裁切或出现明显缩放跳变。左右移动分别绘制，爆米花桶始终由同一只手握持。
- 四个正方向先通过检查，再分别整行生成前、后八个方向。后八方向严格复用前八格的注册结果和尺度。三名隔离盲测的四个正方向全部通过；067.5°、112.5°的纵向分量，135°、157.5°、202.5°、225°的横向分量在盲测中较难分辨，292.5°、315°、337.5°的左向分量也较细微。独立带标签循环复核确认没有错误象限或方向倒转，作为细微说明保留。
- 270°→292.5°及337.5°→000°差异指标较高；独立复核未见明显跳变，后者中心位移约4.1像素。检查未发现内部透明破洞。
- 最终GIF已逐帧解码，帧数与时长核对通过。独立视觉验收使用实际解码帧按顺序复核；其图像查看器不能播放GIF，因此不将该项写成独立播放实测。记录见 `source/qa/preview-files-check.json` 与 `source/qa/final-visual-qa.json`。
- [本机加载算法检查](preview/app-loader-validation.json)通过，仅重放实际图片、版本与路径验证函数；应用设置识别、选用和桌面浮动显示尚未实测。其他四套宠物的八个导入文件保持原样。
- 本地HTML预览已生成，但浏览器连接本地服务超时，宽窄屏展示及折叠交互尚未实测；链接、图片路径和静态图像素一致性另行核对。
- 当前制作和验收记录位于本套 `source/qa/`，方向说明见 `direction-semantics.json`，盲测接受依据见 `blind-review-resolution.json`。首屏静态图是最终图集待机首帧的原始RGBA像素裁切。

</details>

<details>
<summary>参考与制作记录</summary>

- [所选卡面公开镜像](https://anihonetwallpaper.com/post/56898)是服装、发型及道具参考；[游戏数据镜像](https://github.com/Sekai-World/sekai-master-db-diff/blob/main/cards.json)核实卡1084、角色15、二星、pure、`res015_no040`。两者均不是官方来源，快照、URL与下载哈希保存在 `source/references/`。
- [官方游戏角色资料](https://pjsekai.sega.jp/character/unite04/nene/index.html)及[官方电影角色资料](https://sh-anime.shochiku.co.jp/pjsekai-movie/character/kusanagi-nene/)用于性格依据：喜欢游戏、音乐剧和电影，擅长歌唱与机器操作。官方电影页全身图属于另一套舞台服，已明确排除为本套服装参考。
- 安静眨眼、拘谨招手、期待回应、认真思考和审视是根据性格设计的创作演绎。爆米花桶固定同一只手握持，桶身文字简化为无字条纹。
- 详细依据见 [design-brief.md](source/references/design-brief.md)，进度见 [progress.json](source/qa/progress.json)。

</details>
