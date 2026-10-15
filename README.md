# nene_codex_pets

草薙宁宁的 Codex 桌面宠物合集。五套造型，各有9种状态动画与16个注视方向。新增二星卡「Let’s enjoy the movie！」观影造型 `nene_movie`，合集版本为v1.4.0。

**[下载五套合集 · v1.4.0](https://github.com/scenesuki/nene_codex_pets/releases/download/v1.4.0/nene_codex_pets-v1.4.0.zip)** · [校验和](https://github.com/scenesuki/nene_codex_pets/releases/download/v1.4.0/SHA256SUMS.txt) · [更新记录](https://github.com/scenesuki/nene_codex_pets/releases)

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

| Let's enjoy the movie！ · 新增 |
| :---: |
| <a href="nene_movie/README.md"><img src="nene_movie/preview/readme-portrait.png" alt="草薙宁宁观影造型" width="144"></a> |
| 格纹背带长裙与爆米花桶 · Q版日系插画 |
| [造型与说明](nene_movie/README.md) · [查看动画](nene_movie/preview/animation-overview.gif) |

## 三步安装

1. 下载上方合集 ZIP，使用同版 `SHA256SUMS.txt` 核对校验和，再解压。
2. 将想使用的宠物目录复制到 `~/.codex/pets/`，确保目录内同时有 `pet.json` 和 `spritesheet.webp`。
3. 打开 Codex 设置 > Pets，刷新并选择对应造型；必要时重启应用。

Windows 默认目录为 `%USERPROFILE%\.codex\pets\`；自定义 `CODEX_HOME` 时，使用其下的 `pets/`。各套宠物可同时安装，由你选择当前使用的一套。v1.4.0合集包含上方五套造型及完整预览。

<details>
<summary>规格与验证范围</summary>

- Codex桌面v2格式：无损RGBA WebP，1536×2288；8×11格，单格192×208。
- 已核对动画帧数、透明边缘、方向语义和循环预览；五套安装文件均已核对哈希，并重放本机实际图片、版本及路径验证函数。
- 初始舞台服已安装并核对成品一致性；新增观影造型已于2026-10-15安装，两个导入文件与成品一致，未切换当前宠物。两套均已按 `OpenAI.Codex_26.1007.9446.0` 复核图集格式及加载算法；原有三套依据为 `26.1007.2314.0`。**应用设置识别、选用及桌面浮动显示尚未实测。** 详细记录与已接受的细微问题见各套README。
- 首屏静态图直接提取自各套最终交付图集。完整动画通过上方链接查看，所有预览也保存在发布包中。

</details>

<details>
<summary>版本与历史下载</summary>

| 版本 | 实际内容 | 附件 |
| --- | --- | --- |
| [v1.4.0](https://github.com/scenesuki/nene_codex_pets/releases/tag/v1.4.0) | 新增初始舞台服与观影造型，五套完整合集 | `nene_codex_pets-v1.4.0.zip` |
| [v1.2.1](https://github.com/scenesuki/nene_codex_pets/releases/tag/v1.2.1) | 校服、机器人、新舞台服三套合集；项目更名为 `nene_codex_pets` | `nene_codex_pets-v1.2.1.zip` |
| [v1.1.1](https://github.com/scenesuki/nene_codex_pets/releases/tag/v1.1.1) | 校服与机器人两套合集 | `nene-codex-pet-v1.1.1.zip` |
| [v1.1.0](https://github.com/scenesuki/nene_codex_pets/releases/tag/v1.1.0) | 机器人单套包 | `nene-robo-v1.0.0.zip` |
| [v1.0.0](https://github.com/scenesuki/nene_codex_pets/releases/tag/v1.0.0) | 初始校服单套包 | `nene-codex-pet-v1.0.0.zip` |

从v1.1.1起，新Release采用全量合集。当前v1.4.0包含五套宠物，本地副本位于 `release-assets/v1.4.0/`，线上下载见上方入口。本地历史ZIP和旧分发快照已按用户要求清理，发布说明与回执保留；线上历史附件不受影响。

</details>

<details>
<summary>项目结构与全量打包</summary>

每套宠物在根目录独立存放，顶层为导入文件，`preview/`为预览，`source/`为参考、提示词、源图、候选和验收记录。共用脚本在`scripts/`；本地发布资源在`release-assets/<tag>/`，不提交Git。

从项目根目录运行，`vX.Y.Z`替换为尚未存在的新版本：

```powershell
python scripts/build_release.py --tag vX.Y.Z
python scripts/verify_release.py release-assets/vX.Y.Z/nene_codex_pets-vX.Y.Z.zip
```

脚本自动清点根目录全部`*/pet.json`，核对成品、全部GIF与ZIP文件一致性；缺少资源时停止，已有版本不会覆盖。发布时上传合集ZIP及同目录的`SHA256SUMS.txt`，核对下载哈希。有效源素材保留在各套 `source/`，本地历史包按用户授权清理。

工作约定见[AGENTS.md](AGENTS.md)，机器人素材索引见[source/README.md](nene-robo/source/README.md)。本地发布目录索引位于`release-assets/README.md`。辅助验证脚本依赖对应Windows应用安装包；预览与打包使用Python及Pillow。

</details>

---

《Project SEKAI》非官方同人项目。角色及参考素材权利归原权利人所有，详见[NOTICE.md](NOTICE.md)。
