# Journal Sentiment

Journal Sentiment は iPhone に標準搭載されている「ジャーナル」のデータを使用して、日々の記録から感情分析を行うツールです。

## 使用モデル

[koheiduck/bert-japanese-finetuned-sentiment](https://huggingface.co/koheiduck/bert-japanese-finetuned-sentiment)

## 使い方

0. (下準備) docker デスクトップをインストールし、main.sh と同じ階層に移動してから`docker compose build`でコンテナを作成した後、`docker compose up`でコンテナを起動します。

1. `docker compose exec -it app bash` でコンテナの中に入ります。

2. main.sh と同じ階層にジャーナルアプリで出力した zip ファイルを解凍して配置します。

3. `cp -n .env.example .env`で環境変数ファイルをコピーします。ジャーナルのパスやデータ出力先のパスはここで設定できます。

4. コマンド`chmod +x main.sh`の後に`./main.sh`を実行します。
