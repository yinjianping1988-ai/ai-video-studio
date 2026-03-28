# 🚀 Seedance Prompt Skill 安装指南

## 自动安装（推荐）

在终端执行以下命令：

```bash
# 1. 克隆仓库
git clone https://github.com/songguoxs/seedance-prompt-skill.git

# 2. 创建技能目录
mkdir -p ~/.claude/skills/seedance

# 3. 复制技能文件
cp seedance-prompt-skill/.claude/skills/seedance/SKILL.md ~/.claude/skills/seedance/SKILL.md

# 4. 验证安装
cd ~/.claude/skills/seedance
ls -la
```

## 手动安装

### 步骤 1：创建目录
```bash
mkdir -p ~/.claude/skills/seedance
```

### 步骤 2：下载 SKILL.md
访问以下任一链接下载文件：
- GitHub: https://github.com/songguoxs/seedance-prompt-skill/blob/master/.claude/skills/seedance/SKILL.md
- Raw: https://raw.githubusercontent.com/songguoxs/seedance-prompt-skill/master/.claude/skills/seedance/SKILL.md

### 步骤 3：保存文件
将下载的 `SKILL.md` 保存到 `~/.claude/skills/seedance/SKILL.md`

---

## 验证安装

1. 打开终端，进入任意项目目录
2. 运行 `claude` 启动 Claude Code
3. 输入 `/seedance` 或直接说 "帮我生成一段仙侠战斗视频提示词"
4. 如果 Claude 开始询问视频参数，说明安装成功！

---

## 使用方法

### 快速启动
```
/seedance
```

### 直接描述需求
```
帮我生成一段赛博朋克风格的城市夜景视频提示词
```

### 完整示例
```
帮我写一段仙侠战斗的视频提示词，15 秒，横屏
```

---

## 核心功能

| 功能 | 说明 |
|------|------|
| 纯文本生成 | 无需素材，文字描述生成视频 |
| 一致性控制 | 保持角色/产品/场景统一 |
| 运镜复刻 | 复刻参考视频的镜头语言 |
| 特效复刻 | 模仿创意转场/特效 |
| 剧情补全 | 从图片/脚本自动生成剧情 |
| 视频延长 | 向前/向后延长视频 |
| 声音控制 | 音色克隆/对白/音效 |
| 一镜到底 | 连贯长镜头生成 |
| 视频编辑 | 换角色/改剧情/增减元素 |
| 音乐卡点 | 画面节奏与音乐节拍同步 |

---

## 注意事项

⚠️ **平台限制**：
- 不支持上传含有写实真人脸部的素材（会被拦截）
- 单次生成时长：4-15 秒
- 超长视频需要分段生成 + 延长拼接

✅ **最佳实践**：
- 使用自然流畅的中文描述
- 15 秒视频推荐用时间戳分镜法
- @引用使用官方命名（@图片 1、@视频 1）
- 图片风格与视频主题匹配

---

## 文件位置

- **技能文件**: `~/.claude/skills/seedance/SKILL.md`
- **GitHub 仓库**: https://github.com/songguoxs/seedance-prompt-skill
- **即梦平台**: https://jimeng.jianying.com

---

**安装完成后，就可以在我们的 AI 短视频制作工作室网页中配合使用这个 Skill 了！** 🎬
