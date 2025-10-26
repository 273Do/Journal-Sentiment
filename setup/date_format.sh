# 結果csvファイルから最初と最後の日付を取得する関数
function get_entry_range() {
  local entry_csv_file=$1

  local first_date=$(sed -n '2p' "$entry_csv_file" | awk -F',' '{print $2}' | sed 's/-//g' | cut -c3-)

  local last_date=$(tail -n 1 "$entry_csv_file" | awk -F',' '{print $2}' | sed 's/-//g' | cut -c3-)

  echo "journalの期間(yymmdd)：$first_date ~ $last_date"
}
