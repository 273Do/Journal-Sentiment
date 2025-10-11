from html.parser import HTMLParser

from src.schema.data_format.entry_type import ParserEntryType


class JournalHTMLParser(HTMLParser):
    """Apple Journalの専用HTMLパーサー"""

    def __init__(self) -> None:
        super().__init__()

        # 抽出結果を格納する変数
        self.title = None
        self.body = []

        # 現在のタグと属性を追跡するための変数
        self.current_tag = None
        self.current_attrs = {}
        self.has_title_div = False

    def handle_starttag(self, tag, attrs) -> None:
        """開始タグを処理"""
        self.current_tag = tag
        self.current_attrs = dict(attrs)

    def handle_data(self, data) -> None:
        """データを処理

        パターン1: <div class='title'>(タイトル) + <span class="s2">(本文)
        パターン2: <span class="s2">(タイトル) + <span class="s3">(本文)
        """
        data = data.strip()
        if not data:
            return

        # タイトルを抽出
        if self.current_tag == "div" and self.current_attrs.get("class") == "title":
            self.title = data
            self.has_title_div = True

        # パターン2: titleクラスのdivがない場合、s2がタイトル
        elif (
            not self.has_title_div
            and self.current_tag == "span"
            and self.current_attrs.get("class") == "s2"
            and self.title is None
        ):
            self.title = data

        # 本文を抽出
        # パターン1: titleクラスのdivがある場合、s2が本文
        elif (
            self.has_title_div
            and self.current_tag == "span"
            and self.current_attrs.get("class") == "s2"
        ):
            self.body.append(data)

        # パターン2: s3が本文
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
