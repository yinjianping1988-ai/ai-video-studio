#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AI 短剧剧本分析工具 - 本地版本
直接调用阿里云 Qwen API，无 CORS 限制

使用方法：
python3 analyze_script.py
"""

import json
import requests
from datetime import datetime

# ========== 配置 ==========
API_KEY = "sk-63aaf6ddba6c4a34af223efca3f85811"  # 替换为你的 API Key
API_URL = "https://dashscope.aliyuncs.com/api/v1/services/aigc/text-generation/generation"
MODEL = "qwen-plus"

# ========== API 调用函数 ==========
def call_qwen_api(prompt, system_prompt=""):
    """调用阿里云 Qwen API"""
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }
    
    messages = []
    if system_prompt:
        messages.append({"role": "system", "content": system_prompt})
    messages.append({"role": "user", "content": prompt})
    
    payload = {
        "model": MODEL,
        "input": {
            "messages": messages
        },
        "parameters": {
            "result_format": "message",
            "temperature": 0.7,
            "max_tokens": 2000
        }
    }
    
    try:
        response = requests.post(API_URL, headers=headers, json=payload, timeout=60)
        response.raise_for_status()
        
        data = response.json()
        if data.get("output") and data["output"].get("choices"):
            return data["output"]["choices"][0]["message"]["content"]
        else:
            return f"❌ API 返回格式异常：{data}"
    
    except requests.exceptions.Timeout:
        return "❌ 请求超时，请检查网络连接"
    except requests.exceptions.ConnectionError:
        return "❌ 连接失败，请检查网络"
    except Exception as e:
        return f"❌ 错误：{str(e)}"


# ========== 剧本分析功能 ==========
def analyze_script(script_content, check_logic=True, check_structure=True, second_review=True):
    """分析剧本"""
    
    print("\n" + "="*60)
    print("📊 开始分析剧本...")
    print("="*60 + "\n")
    
    # 第一次分析
    system_prompt_1 = """你是一位专业的剧本分析师，擅长：
1. 内容合理性评估（逻辑/时间线/因果关系）
2. 故事条理性分析（结构/节奏/起承转合）
3. 二次深度审核"""

    analysis_prompt = f"""请分析以下剧本：

{script_content}

请按以下格式输出分析报告：

【📊 基础统计】
- 总字数
- 场景数
- 角色数
- 预估时长

"""
    
    if check_logic:
        analysis_prompt += """【✅ 内容合理性】
- 逻辑连贯性
- 时间线清晰度
- 因果关系

"""
    
    if check_structure:
        analysis_prompt += """【📈 故事条理性】
- 结构完整性（起承转合）
- 节奏把控
- 冲突密度

"""
    
    analysis_prompt += """【⚠️ 问题与建议】
- 至少 3 条具体问题
- 对应的改进建议"""

    print("🔍 进行第一次分析...")
    first_result = call_qwen_api(analysis_prompt, system_prompt_1)
    
    if "错误" in first_result or "❌" in first_result:
        return first_result
    
    print(first_result)
    
    # 第二次审核
    if second_review:
        print("\n" + "="*60)
        print("🔍 进行第二次深度审核...")
        print("="*60 + "\n")
        
        system_prompt_2 = """你是一位资深的剧本审核专家，擅长发现剧本中的深层问题。
请对剧本进行二次审核，重点关注：
1. 人物动机是否合理
2. 情节发展是否自然
3. 对话是否符合角色身份
4. 是否有更好的叙事方式"""
        
        second_prompt = f"""请对以下剧本进行二次深度审核：

{script_content}

第一次分析结果：
{first_result}

请在第一次分析的基础上，进行深度审核：

【🔍 二次审核意见】
- 人物动机分析
- 情节发展评估
- 对话质量评价
- 优化建议

【✅ 最终结论】
- 是否通过审核
- 需要修改的关键点
- 综合评分（0-100 分）"""
        
        print("📝 生成二次审核报告...")
        second_result = call_qwen_api(second_prompt, system_prompt_2)
        
        print("\n" + "="*60)
        print("✅ 审核完成！")
        print("="*60)
        print(second_result)
        
        return f"{first_result}\n\n{'='*60}\n{second_result}"
    
    return first_result


# ========== AI 生成剧本功能 ==========
def generate_script(story_idea, length="short"):
    """AI 生成剧本"""
    
    print("\n" + "="*60)
    print("🤖 AI 正在创作剧本...")
    print("="*60 + "\n")
    
    length_map = {
        "short": "1-2 分钟",
        "medium": "3-5 分钟",
        "long": "5-10 分钟"
    }
    
    system_prompt = """你是一位专业的短剧编剧，擅长创作 2 分钟竖屏短剧。
短剧特点：
- 开篇 3 秒必须有冲突/悬念
- 每 15 秒一个小节点
- 每 30 秒一个反转
- 结尾留钩子/悬念"""
    
    prompt = f"""请根据以下故事创意，创作一个{length_map.get(length, '1-2 分钟')}的短剧剧本：

{story_idea}

剧本格式要求：
【剧名】
【时长】
【角色介绍】
【剧本正文】（按场景分段，包含场景、时间、角色、对话、动作描述）

请确保节奏紧凑，冲突密集，适合竖屏短视频平台。"""
    
    result = call_qwen_api(prompt, system_prompt)
    
    print(result)
    return result


# ========== 主程序 ==========
def main():
    """主程序"""
    
    print("\n" + "="*60)
    print("🎬 AI 短剧剧本分析工具 - 本地版")
    print("="*60)
    print("\n功能说明：")
    print("1. 分析已有剧本（内容合理性 + 故事条理性 + 二次审核）")
    print("2. AI 生成新剧本（输入故事创意自动生成）")
    print("="*60 + "\n")
    
    # 选择功能
    print("请选择功能：")
    print("1. 分析已有剧本")
    print("2. AI 生成新剧本")
    
    choice = input("\n请输入选项 (1/2): ").strip()
    
    if choice == "1":
        # 分析剧本
        print("\n" + "-"*60)
        print("📄 分析已有剧本")
        print("-"*60)
        print("\n请粘贴你的剧本内容（输入空行结束）：\n")
        
        lines = []
        while True:
            try:
                line = input()
                if line == "":
                    break
                lines.append(line)
            except EOFError:
                break
        
        script_content = "\n".join(lines)
        
        if not script_content.strip():
            print("❌ 未输入内容，退出")
            return
        
        # 分析选项
        print("\n请选择分析选项：")
        check_logic = input("✓ 内容合理性分析？(y/n): ").strip().lower() != 'n'
        check_structure = input("✓ 故事条理性分析？(y/n): ").strip().lower() != 'n'
        second_review = input("✓ 二次深度审核？(y/n): ").strip().lower() != 'n'
        
        # 执行分析
        result = analyze_script(
            script_content,
            check_logic=check_logic,
            check_structure=check_structure,
            second_review=second_review
        )
        
        # 保存结果
        save_option = input("\n💾 是否保存分析报告到文件？(y/n): ").strip().lower()
        if save_option == 'y':
            filename = f"analysis_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(result)
            print(f"✅ 报告已保存到：{filename}")
        
        print("\n✅ 分析完成！")
        
    elif choice == "2":
        # AI 生成剧本
        print("\n" + "-"*60)
        print("🤖 AI 生成新剧本")
        print("-"*60)
        print("\n请输入故事创意/简介：\n")
        
        story_idea = input()
        
        if not story_idea.strip():
            print("❌ 未输入内容，退出")
            return
        
        # 选择时长
        print("\n请选择剧本时长：")
        print("1. 短剧 (1-2 分钟)")
        print("2. 中剧 (3-5 分钟)")
        print("3. 长剧 (5-10 分钟)")
        
        length_choice = input("\n请输入选项 (1/2/3): ").strip()
        length_map = {"1": "short", "2": "medium", "3": "long"}
        length = length_map.get(length_choice, "short")
        
        # 生成剧本
        result = generate_script(story_idea, length)
        
        # 保存结果
        save_option = input("\n💾 是否保存剧本到文件？(y/n): ").strip().lower()
        if save_option == 'y':
            filename = f"script_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(result)
            print(f"✅ 剧本已保存到：{filename}")
        
        print("\n✅ 生成完成！")
        
    else:
        print("❌ 无效选项，退出")
        return
    
    print("\n" + "="*60)
    print("感谢使用！再见 👋")
    print("="*60 + "\n")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️ 用户中断，退出")
    except Exception as e:
        print(f"\n❌ 发生错误：{e}")
