from pathlib import Path

class DesignHandler:
    """視覚表現（スタイル・テーマ・CSS）を管理する 2次元 Bean"""

    def __init__(self, theme="default"):
        self.theme = theme
        self.design_dir = Path(__file__).resolve().parent

    def get_custom_css(self):
        style_file = self.design_dir / "style.css"
        
        # 1. テーマごとのカラーパレット定義
        themes = {
            "default": {
                "bg_color": "#f8f9fa",
                "text_color": "#212529",
                "text_muted": "#6c757d",
                "card_bg": "#ffffff",
                "border_color": "#e9ecef",
                "accent_color": "#0d6efd",
            },
            "dark": {
                "bg_color": "#121212",
                "text_color": "#e0e0e0",
                "text_muted": "#a0a0a0",
                "card_bg": "#1e1e1e",
                "border_color": "#333333",
                "accent_color": "#bb86fc",
            },
            "modern_slate": {
                "bg_color": "#0f172a",
                "text_color": "#f8fafc",
                "text_muted": "#94a3b8",
                "card_bg": "#1e293b",
                "border_color": "#334155",
                "accent_color": "#38bdf8",
            }
        }
        t = themes.get(self.theme, themes["default"])

        # 2. 動的な `:root` CSS 変数ブロックを作成
        theme_variables = f"""
        :root {{
            --op-bg-color: {t["bg_color"]};
            --op-text-color: {t["text_color"]};
            --op-text-muted: {t["text_muted"]};
            --op-card-bg: {t["card_bg"]};
            --op-border-color: {t["border_color"]};
            --op-accent-color: {t["accent_color"]};
        }}
        """

        # 3. style.css が存在する場合は変数を先頭に結合して返す
        if style_file.exists():
            print(f"    [*] Design/style.css と テーマ '{self.theme}' を結合適用しました。")
            with open(style_file, "r", encoding="utf-8") as f:
                return theme_variables + "\n" + f.read()

        # style.css がない場合はテーマ変数のみを返却
        return theme_variables