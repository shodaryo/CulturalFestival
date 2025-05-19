# ページ、サイドバー作成

import streamlit as st


# 以下、画面を作成
# ログイン画面
def login():
    st.title("🎌 文化祭案内アプリ")
    st.subheader("ログインしてください")
    username = st.text_input("ユーザー名")
    password = st.text_input("パスワード", type="password")

    if st.button("ログイン"):
        st.write('ログインしたよ')

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
    st.image("school_map.png", use_column_width=True)
    st.write("地図上の場所を参考にして、各クラスの企画紹介ページへ移動できます。")

    if st.button("1年A組の企画を見る"):
        st.write('1-Aの企画')
    if st.button("1年B組の企画を見る"):
        st.write('1-Bの企画')

# クラス企画一覧ページ
def class_list_page():
    st.title("🏫 クラス企画一覧")
    classes = ["1年A組", "1年B組", "2年A組", "2年B組"]
    for class_name in classes:
        if st.button(f"{class_name} の企画を見る"):
            st.write(f"{class_name}の詳細")

# クラス企画詳細（仮に1つの画面で共通表示）
def class_detail_page():
    st.title("🎪 クラス企画詳細")
    st.subheader("1-Aの企画詳細")
    st.write("このクラスの企画は「○○○○○」です。楽しい内容なのでぜひ立ち寄ってみてください！")
    if st.button("← クラス一覧に戻る"):
        st.write('クラス一覧に戻る')

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
            st.write(event)
            st.write(detail)

# イベント詳細ページ
def event_detail_page():
    st.title("🎭 イベント詳細")
    details = {
        "ステージ発表": "生徒会によるバンド演奏など",
        "ダンス発表": "ダンス部によるパフォーマンス",
        "演劇": "演劇部によるオリジナル劇"
    }

    if st.button("← イベント一覧に戻る"):
        st.write('イベント一覧に戻りました。')

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

class_vote_result_page()
sidebar()