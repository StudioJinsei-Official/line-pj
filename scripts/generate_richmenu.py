#!/usr/bin/env python3
"""
LINE Rich Menu 画像生成スクリプト
Gemini 3 Pro Image を使用
"""

import os
import sys
from pathlib import Path
from datetime import datetime

try:
    from google import genai
except ImportError:
    print("❌ エラー: google-genai パッケージが必要です")
    print("pip install google-genai")
    sys.exit(1)

def load_prompt(prompt_file):
    """プロンプトファイルを読み込む"""
    path = Path(prompt_file)
    if not path.exists():
        print(f"❌ エラー: プロンプトファイル {prompt_file} が見つかりません")
        sys.exit(1)
    
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def generate_image(api_key, prompt):
    """Gemini 3 Pro Image で画像を生成"""
    client = genai.Client(api_key=api_key)
    
    # Gemini 3 Pro Image モデル
    model = "gemini-2.0-flash-preview-image-generation"
    
    print(f"🤖 モデル: {model}")
    print(f"📝 プロンプト長さ: {len(prompt)} 文字")
    
    try:
        response = client.models.generate_content(
            model=model,
            contents=prompt,
            config={
                "response_modalities": ["IMAGE", "TEXT"],
            }
        )
        return response
    except Exception as e:
        print(f"❌ 生成エラー: {e}")
        return None

def save_image(response, output_dir, name):
    """画像を保存"""
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{name}_{timestamp}.png"
    filepath = output_path / filename
    
    if response and response.candidates:
        for part in response.candidates[0].content.parts:
            if hasattr(part, 'inline_data') and part.inline_data:
                filepath.write_bytes(part.inline_data.data)
                return filepath
    
    print("❌ 画像データが見つかりませんでした")
    return None

def main():
    # APIキー確認
    api_key = os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        print("❌ エラー: GOOGLE_API_KEY 環境変数が設定されていません")
        print('export GOOGLE_API_KEY="your-api-key"')
        sys.exit(1)
    
    print("🎨 LINE Rich Menu 画像生成")
    print("=" * 60)
    
    # プロンプト読み込み
    script_dir = Path(__file__).parent.parent
    prompt_file = script_dir / "prompt_richmenu_icons.txt"
    print(f"📂 プロンプトファイル: {prompt_file}")
    
    prompt = load_prompt(prompt_file)
    
    # 画像生成
    print("\n🖼️  画像生成中...")
    response = generate_image(api_key, prompt)
    
    if not response:
        print("❌ 画像生成に失敗しました")
        sys.exit(1)
    
    # 保存
    print("💾 画像保存中...")
    output_dir = "images/generated"
    filepath = save_image(response, output_dir, "richmenu_with_icons")
    
    if filepath:
        print(f"\n✅ 完了！")
        print(f"📁 保存先: {filepath.absolute()}")
        print(f"📏 ファイルサイズ: {filepath.stat().st_size / 1024:.1f} KB")
    else:
        print("❌ 画像保存に失敗しました")
        sys.exit(1)

if __name__ == "__main__":
    main()

