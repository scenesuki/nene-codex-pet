# nene_codex_pets

草薙宁宁的 Codex 桌面宠物合集。工作区现有八套造型，各有9种状态动画与16个注视方向。本次新增「きらびやかな夢の舞台」特训后蓬裙与展开花边伞造型 `nene_victorian_lolita`。

**[下载八套完整合集 · v1.7.2](https://github.com/scenesuki/nene_codex_pets/releases/download/v1.7.2/nene_codex_pets-v1.7.2.zip)** · [校验和](https://github.com/scenesuki/nene_codex_pets/releases/download/v1.7.2/SHA256SUMS.txt) · [更新记录](https://github.com/scenesuki/nene_codex_pets/releases)

本版合集包含下列全部八套宠物、完整预览和最终校验记录；选用的制作原素材保留在仓库各套 `source/`。

## 选一位宁宁

| 初始校服 | 宁宁机器人 |
| :---: | :---: |
| <a href="nene-initial-uniform/README.md"><img src="nene-initial-uniform/preview/readme-portrait.png" alt="草薙宁宁初始校服" width="144"></a> | <a href="nene-robo/README.md"><img src="nene-robo/preview/readme-portrait.png" alt="宁宁机器人原始造型" width="144"></a> |
| 神山高校校服 · Q版日系插画 | 原始演出服 · 贴近游戏原画 |
| [造型与说明](nene-initial-uniform/README.md) · [查看动画](nene-initial-uniform/preview/animation-overview.gif) | [造型与说明](nene-robo/README.md) · [查看动画](nene-robo/preview/animation-overview.gif) |

| Brand New Style | 初始舞台服 · 新增 |
| :---: | :---: |
| <a href="nene_costume/README.md"><img src="nene_costume/preview/readme-portrait.png" alt="草薙宁宁 Brand New Style 舞台服" width="144"></a> | <a href="nene_costume_2/README.md"><img src="nene_costume_2/preview/readme-portrait.png" alt="草薙宁宁ワンダーランズ×ショウタイム初始舞台服" width="144"></a> |
| 新舞台服 · Q版日系插画 | ワンダーランズ×ショウタイム · Q版日系插画 |
| [造型与说明](nene_costume/README.md) · [查看动画](nene_costume/preview/animation-overview.gif) | [造型与说明](nene_costume_2/README.md) · [查看动画](nene_costume_2/preview/animation-overview.gif) |

| Let's enjoy the movie！ | 江戸の町並みに飲まれて · 新增 |
| :---: | :---: |
| <a href="nene_movie/README.md"><img src="nene_movie/preview/readme-portrait.png" alt="草薙宁宁观影造型" width="144"></a> | <a href="nene_edo/README.md"><img src="nene_edo/preview/readme-portrait.png" alt="草薙宁宁黑绿复古洋装" width="144"></a> |
| 格纹背带长裙与爆米花桶 · Q版日系插画 | 黑绿洋装、小礼帽与金边折扇 · Q版日系插画 |
| [造型与说明](nene_movie/README.md) · [查看动画](nene_movie/preview/animation-overview.gif) | [造型与说明](nene_edo/README.md) · [查看动画](nene_edo/preview/animation-overview.gif) |

| ワンダーステッキ | Victorian Lolita · 新增 |
| :---: | :---: |
| <a href="nene_wand/README.md"><img src="nene_wand/preview/readme-portrait.png" alt="草薙宁宁膝上条纹短裙、红色小腿袜与手杖" width="144"></a> | <a href="nene_victorian_lolita/README.md"><img src="nene_victorian_lolita/preview/readme-portrait.png" alt="Victorian Lolita宁宁与展开花边伞" width="144"></a> |
| 红色短外套、膝上条纹短裙与红色小腿袜 · Q版日系插画 | 青绿蓬裙、藏蓝帽与展开花边伞 · Q版日系插画 |
| [造型与说明](nene_wand/README.md) · [查看动画](nene_wand/preview/animation-overview.gif) | [造型与说明](nene_victorian_lolita/README.md) · [查看动画](nene_victorian_lolita/preview/animation-overview.gif) |

## 三步安装

1. 下载上方合集 ZIP，使用同版 `SHA256SUMS.txt` 核对校验和，再解压。
2. 将想使用的宠物目录复制到 `~/.codex/pets/`，确保目录内同时有 `pet.json` 和 `spritesheet.webp`。
3. 打开 Codex 设置 > Pets，刷新并选择对应造型；必要时重启应用。

Windows 默认目录为 `%USERPROFILE%\.codex\pets\`；自定义 `CODEX_HOME` 时，使用其下的 `pets/`。各套宠物可同时安装，由你选择当前使用的一套。v1.7.2包含上方全部八套及完整预览。

<details>
<summary>规格与验证范围</summary>

- Codex桌面v2格式：无损RGBA WebP，1536×2288；8×11格，单格192×208。
- 已核对动画帧数、透明边缘、方向语义和循环预览；五套安装文件均已核对哈希，并重放本机实际图片、版本及路径验证函数。
- 初始舞台服已安装并核对成品一致性；新增观影造型已于2026-10-15安装，两个导入文件与成品一致，未切换当前宠物。两套均已按 `OpenAI.Codex_26.1007.9446.0` 复核图集格式及加载算法；原有三套依据为 `26.1007.2314.0`。**应用设置识别、选用及桌面浮动显示尚未实测。** 详细记录与已接受的细微问题见各套README。
- 新增 `nene_edo` 的规格、文件与视觉验收记录见其子页；已于2026-10-15安装并核对两个成品文件，未切换当前宠物，已纳入v1.6.2完整合集。
- 新增 `nene_wand` 已依据完整参考重制为膝上短裙与红色小腿袜，九状态、十六方向及本机实际加载校验函数均通过；少数中间视线分量和跨段姿态差异记录为细微限制。已纳入v1.6.2完整合集；尚未安装，应用内显示尚未实测，详见其子页。
- 新增 `nene_victorian_lolita`（显示名称 `nene_victorian lolita`）已通过原生v2校验、视觉复核与本机加载算法检查；跳跃已改为8px离地的小跳，其余八状态和十六方向逐像素保留。原方向盲审仍适用，五个低头斜向的横向提示较细微，详见子页；尚未安装，应用UI与实际动态播放尚未实测。
- 首屏静态图直接提取自各套最终交付图集。完整动画通过上方链接查看，所有预览也保存在发布包中。

</details>

<details>
<summary>版本与历史下载</summary>

| 版本 | 实际内容 | 附件 |
| --- | --- | --- |
| [v1.7.2](https://github.com/scenesuki/nene_codex_pets/releases/tag/v1.7.2) | 新增Victorian Lolita蓬裙与花边伞，八套完整合集；整理有效原素材与最终验收 | `nene_codex_pets-v1.7.2.zip` |
| [v1.6.2](https://github.com/scenesuki/nene_codex_pets/releases/tag/v1.6.2) | 新增江户风洋装与手杖造型，七套完整合集 | `nene_codex_pets-v1.6.2.zip` |
| [v1.4.0](https://github.com/scenesuki/nene_codex_pets/releases/tag/v1.4.0) | 新增初始舞台服与观影造型，五套完整合集 | `nene_codex_pets-v1.4.0.zip` |
| [v1.2.1](https://github.com/scenesuki/nene_codex_pets/releases/tag/v1.2.1) | 校服、机器人、新舞台服三套合集；项目更名为 `nene_codex_pets` | `nene_codex_pets-v1.2.1.zip` |
| [v1.1.1](https://github.com/scenesuki/nene_codex_pets/releases/tag/v1.1.1) | 校服与机器人两套合集 | `nene-codex-pet-v1.1.1.zip` |
| [v1.1.0](https://github.com/scenesuki/nene_codex_pets/releases/tag/v1.1.0) | 机器人单套包 | `nene-robo-v1.0.0.zip` |
| [v1.0.0](https://github.com/scenesuki/nene_codex_pets/releases/tag/v1.0.0) | 初始校服单套包 | `nene-codex-pet-v1.0.0.zip` |

从v1.1.1起，新Release采用全量合集。v1.7.2包含全部八套及当前说明、预览和最终验收；历史版本内容以对应Release为准。

本地保留当前全量合集ZIP；未采用废案、旧分发快照、重复制作缓存及旧本地包按授权清理。当前成果对应的有效制作原素材保留在各套 `source/`，由 `materials-index.json` 记录路径与哈希。已发布版本的说明、校验和与回执保留，历史附件仍从对应GitHub Release下载。

</details>

<details>
<summary>项目结构与全量打包</summary>

每套宠物在根目录独立存放，顶层为当前导入文件、说明与校验；`preview/`保留正式预览、应用规格依据和最终验收。各套 `source/` 保留选用的原始生成图、有效参考图、实际输入和提示词，并提供 `materials-index.json` 索引。参考来源与创作补全写在各套README。共用打包、验证脚本在`scripts/`；本地发布资源在`release-assets/<tag>/`，不提交Git。

从项目根目录运行，`vX.Y.Z`替换为尚未存在的新版本：

```powershell
python scripts/build_release.py --tag vX.Y.Z
python scripts/verify_release.py release-assets/vX.Y.Z/nene_codex_pets-vX.Y.Z.zip
```

脚本自动清点根目录全部`*/pet.json`，核对成品、全部GIF与ZIP文件一致性；缺少资源时停止，已有版本不会覆盖。发布时上传合集ZIP及同目录的`SHA256SUMS.txt`，核对下载哈希。工作区保留最终成果及有效制作原素材；废案、重复缓存和本地历史包按用户授权清理。

工作约定见[AGENTS.md](AGENTS.md)，机器人预览索引见[preview/README.md](nene-robo/preview/README.md)。本地发布目录索引位于`release-assets/README.md`。辅助验证脚本依赖对应Windows应用安装包；预览与打包使用Python及Pillow。

</details>

---

《Project SEKAI》非官方同人项目。角色及参考素材权利归原权利人所有，详见[NOTICE.md](NOTICE.md)。
