from html.parser import HTMLParser

from src.schema.data_format.entry_type import ParserEntryType


class JournalHTMLParser(HTMLParser):
    """Apple Journalの専用HTMLパーサー"""

    def __init__(self) -> None:
        super().__init__()
        self.title = None
        self.body = []
        self.current_tag = None
        self.current_attrs = {}

    def handle_starttag(self, tag, attrs) -> None:
        """開始タグを処理"""
        self.current_tag = tag
        self.current_attrs = dict(attrs)

    def handle_data(self, data) -> None:
        """データを処理"""
        data = data.strip()
        if not data:
            return

        # タイトルを抽出（s2クラスのspan）
        elif self.current_tag == "span" and self.current_attrs.get("class") == "s2":
            self.title = data

        # 本文を抽出（s3クラスのspan）
        elif self.current_tag == "span" and self.current_attrs.get("class") == "s3":
            self.body.append(data)

    def get_result(self) -> ParserEntryType:
        """抽出結果を辞書形式で返す"""
        return {
            "title": self.title,
            "body": "\n".join(self.body) if self.body else None,
        }


def read_html(file_path: str) -> ParserEntryType:
    """HTMLファイルを読み込み、内容を辞書形式で返す関数

    Args:
        file_path: HTMLファイルのパス

    Returns:
        dict: {
            "title": str (タイトル),
            "body": str (本文)
        }
    """
    with open(file_path, "r", encoding="utf-8") as file:
        html = file.read()

    parser = JournalHTMLParser()
    parser.feed(html)

    return parser.get_result()
