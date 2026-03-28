#!/bin/bash

# Seedance Prompt Skill 一键安装脚本
# 自动下载并安装到 ~/.claude/skills/seedance/

set -e

echo "🚀 开始安装 Seedance Prompt Skill..."

# 创建目录
echo "📁 创建技能目录..."
mkdir -p ~/.claude/skills/seedance

# 下载 SKILL.md
echo "📥 下载 SKILL.md..."
curl -o ~/.claude/skills/seedance/SKILL.md \
  https://raw.githubusercontent.com/songguoxs/seedance-prompt-skill/master/.claude/skills/seedance/SKILL.md

# 验证文件
if [ -f ~/.claude/skills/seedance/SKILL.md ]; then
    echo "✅ 安装成功！"
    echo ""
    echo "📍 文件位置：~/.claude/skills/seedance/SKILL.md"
    echo ""
    echo "🎯 使用方法："
    echo "   1. 打开终端，运行 claude"
    echo "   2. 输入 /seedance 或直接描述视频需求"
    echo ""
    echo "📚 即梦平台：https://jimeng.jianying.com"
else
    echo "❌ 安装失败！请检查网络连接或手动安装"
    exit 1
fi
