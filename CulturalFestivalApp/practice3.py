# 画面遷移
# セッション管理

# webサイトはリロードを行うとデータが初期化される
# セッションに値を保存することで、リロード後のデータを保持することができる
# 例）ログイン情報、表示表示する画面など

import streamlit as st

# セッション状態の初期化
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False


# ログイン画面
def login():
    st.title("🎌 文化祭案内アプリ")
    st.subheader("ログインしてください")
    username = st.text_input("ユーザー名")
    password = st.text_input("パスワード", type="password")

    if st.button("ログイン"):
        st.write('ログインしたよ')
        st.session_state.logged_in = True
        st.session_state.page = "main"  # ✅ メインページへ遷移
        st.rerun()  # ✅ ここで画面再描画（ログイン画面を即消す）

# メイン画面
def main_page():
    st.title("🌟 文化祭アプリ！")
    st.write("画面左のメニューから、各機能に移動できます。")

# メニュー画面
def menu_page():
    st.header("📋 メニュー")
    st.write("・模擬店情報\n・ステージイベント\n・展示紹介\nなどなど...")

# メッセージページ
def message_page():
    st.title("🎉 来場者へのメッセージ")
    st.write("ようこそ文化祭へ！楽しい企画が盛りだくさんです。ぜひ最後までお楽しみください。")

# 校内マップ画面
def map_page():
    st.header("🏫 校内マップ")
    st.image("images/map.png", use_container_width=True)
    st.write("地図上の場所を参考にして、各クラスの企画紹介ページへ移動できます。")

    classes = ["1年A組", "1年B組", "2年A組", "2年B組"]
    for class_name in classes:
        if st.button(f"{class_name} の企画を見る"):
            st.session_state.selected_class = class_name
            st.session_state.page = "class_detail"
            st.session_state.map = True
            st.rerun()

# クラス企画一覧ページ
def class_list_page():
    st.title("🏫 クラス企画一覧")
    classes = ["1年A組", "1年B組", "2年A組", "2年B組"]
    for class_name in classes:
        if st.button(f"{class_name} の企画を見る"):
            st.session_state.selected_class = class_name
            st.session_state.page = "class_detail"
            st.session_state.map = False
            st.rerun()

# クラス企画詳細（仮に1つの画面で共通表示）
def class_detail_page():
    st.title("🎪 クラス企画詳細")
    st.subheader("1-Aの企画詳細")
    st.write("このクラスの企画は「○○○○○」です。楽しい内容なのでぜひ立ち寄ってみてください！")
    if st.session_state.map:
        if st.button("← マップに戻る"):
            st.session_state.page = "map"
            st.rerun()
    else:
        if st.button("← クラス一覧に戻る"):
            st.session_state.page = "class_list"
            st.rerun()

# イベント一覧ページ
def event_list_page():
    st.title("📅 イベント一覧")
    events = {
        "ステージ発表": "10:00〜 体育館",
        "ダンス発表": "11:00〜 中庭",
        "演劇": "13:00〜 多目的室"
    }
    for event, detail in events.items():
        if st.button(f"{event} の詳細を見る"):
            st.session_state.selected_event = event
            st.session_state.page = "event_detail"
            st.rerun()

# イベント詳細ページ
def event_detail_page():
    st.title("🎭 イベント詳細")
    event = st.session_state.get("selected_event", "不明なイベント")
    details = {
        "ステージ発表": "生徒会によるバンド演奏など",
        "ダンス発表": "ダンス部によるパフォーマンス",
        "演劇": "演劇部によるオリジナル劇"
    }
    st.subheader(event)
    st.write(details.get(event, "詳細情報はありません。"))
    if st.button("← イベント一覧に戻る"):
        st.session_state.page = "event_list"
        st.rerun()


# クラス投票結果ページ
def class_vote_result_page():
    st.title("🗳 クラス企画投票結果")
    results = {
        "1年A組": 45,
        "1年B組": 52,
        "2年A組": 38,
        "2年B組": 60
    }
    st.write(results)


# サイドバー（メニュー）
def sidebar():
    st.sidebar.title("📌 メニュー")
    if st.sidebar.button("メイン画面"):
        st.write('メイン画面に移動')
    if st.sidebar.button("メニュー一覧"):
        st.write('メニュー一覧画面に移動')
    if st.sidebar.button("来場メッセージ"):
        st.write('場メッセージ画面に移動')
    if st.sidebar.button("校内マップ"):
        st.write('内マップ画面に移動')
    if st.sidebar.button("クラス企画一覧"):
        st.write('クラス企画一覧画面に移動')
    if st.sidebar.button("イベント一覧"):
        st.write('イベント一覧画面に移動')
    if st.sidebar.button("投票結果"):
        st.write('投票結果画面に移動')

    if st.sidebar.button("ログアウト"):
        st.write('ログアウトしました。')

# サイドバー（メニュー）
def sidebar():
    st.sidebar.title("📌 メニュー")
    if st.sidebar.button("メイン画面"):
        st.session_state.page = "main"
        st.rerun()
    if st.sidebar.button("メニュー一覧"):
        st.session_state.page = "menu"
        st.rerun()
    if st.sidebar.button("来場メッセージ"):
        st.session_state.page = "message"
        st.rerun()
    if st.sidebar.button("校内マップ"):
        st.session_state.page = "map"
        st.rerun()
    if st.sidebar.button("クラス企画一覧"):
        st.session_state.page = "class_list"
        st.rerun()
    if st.sidebar.button("イベント一覧"):
        st.session_state.page = "event_list"
        st.rerun()
    if st.sidebar.button("投票結果"):
        st.session_state.page = "vote_result"
        st.rerun()

    if st.sidebar.button("ログアウト"):
        st.session_state.logged_in = False
        st.session_state.page = "main"
        st.rerun()



# class_vote_result_page()
# sidebar()
# main()メソッドでページを切り替えるようにする
def main():
    # ページの切り替え
    if st.session_state.logged_in:
        if 'page' not in st.session_state:
            st.session_state.page = "main"

        sidebar()

        if st.session_state.page == "main":
            main_page()
        elif st.session_state.page == "menu":
            menu_page()
        elif st.session_state.page == "message":
            message_page()
        elif st.session_state.page == "map":
            map_page()
        elif st.session_state.page == "class_list":
            class_list_page()
        elif st.session_state.page == "class_detail":
            class_detail_page()
        elif st.session_state.page == "event_list":
            event_list_page()
        elif st.session_state.page == "event_detail":
            event_detail_page()
        elif st.session_state.page == "vote_result":
            class_vote_result_page()

    else:
        login()

main()
