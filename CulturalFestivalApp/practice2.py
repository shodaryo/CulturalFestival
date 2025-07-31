# ページ、サイドバー作成

#import
import streamlit as st

# 4 現在のファイル（app.py）のパスを構築

# 7 後でinject_fadein_css()（フェードインのcss）

# 7 後でinject_fadeout_css()（フェードアウトのcss）

# 7 後でinject_zoom_css()（ズームインのcss）

# 7 後でset_main_background()（背景画像をフェードイン、フェードアウトする関数）

# 3 後でログイン認証用のuserデータ

# 4 後でクラス企画のclass_projectデータ

# 5 後でイベント企画のevent_projectデータ

# 3 後でセッション状態の初期化

# 以下、画面を作成
# 2 ログイン画面
def login():
    st.title("🎌 文化祭案内アプリ")
    st.subheader("ログインしてください")
    username = st.text_input("ユーザー名")
    password = st.text_input("パスワード", type="password")

    if st.button("ログイン"):
        st.write('ログインしたよ') # 3 後でログイン機能に変更


# 2 メイン画面
def main_page():
    # 7 後で文字または画像のフェードイン、フェードアウトに変更
    st.title("🌟 文化祭アプリ！")
    st.write("画面左のメニューから、各機能に移動できます。")

    # 3 後で自動での画面遷移


# 2 メニュー画面
def menu_page():
    # 7 あとでズームイン処理のcss（inject_zoom_css()）+ボタン表示にラグを追加（time.sleep(0.5)）
    
    st.header("📋 メニュー")
    st.write("文化祭に関する各ページに移動できます。")

    if st.button("🎪 クラス企画一覧"):
        st.write("クラス企画一覧に移動")# 3 押したら画面遷移する処理に後で変更
    
    if st.button("📅 イベント一覧"):
        st.write("イベント一覧に移動")# 3 押したら画面遷移する処理に後で変更
    
    if st.button("🏫 校内マップ"):
        st.write("校内マップに移動")# 3 押したら画面遷移する処理に後で変更
    
    if st.button("🎉 メッセージページ"):
        st.write("メッセージページに移動")# 3 押したら画面遷移する処理に後で変更
    
    if st.button("🗳 投票結果"):
        st.write("投票結果に移動")# 3 押したら画面遷移する処理に後で変更

# 2 メッセージページ
def message_page():
    st.title("🎉 来場者へのメッセージ")
    st.write("ようこそ文化祭へ！楽しい企画が盛りだくさんです。ぜひ最後までお楽しみください。")

# 2 校内マップ画面
def map_page():
    st.header("🏫 校内マップ")

    # 6 後で表示カテゴリのセレクトボックスcategory
    # 6 後で部屋名の検索ボックスsearch_term

    # 6 後でオーバーレイ画像の作成
    st.image("images/map.png", use_container_width=True)
    st.write("地図上の場所を参考にして、各クラスの企画紹介ページへ移動できます。")

    # 6 後で検索条件に応じて、表示するボタンを変える
    if st.button("1年A組の企画を見る"):
        st.write('1-Aの企画')
    if st.button("1年B組の企画を見る"):
        st.write('1-Bの企画')


# 2 クラス企画一覧ページ
def class_list_page():
    st.title("🏫 クラス企画一覧")
    search = st.text_input("キーワードで検索")

    # 4 後で検索結果に応じて一覧を表示する処理に変更
    if st.button(f"{search} の企画を見る", key=f"class_{search}"):
        st.write(f"{search}の詳細に画面遷移しました。")


# 2 クラス企画詳細
def class_detail_page():
    st.title("🎪 クラス企画詳細")
    
    # 4 後で企画一覧、校内マップ一覧で押したボタンの企画詳細を表示

# 2 イベント一覧
def event_list_page():
    st.title("📅 イベント一覧")
    day = st.selectbox("日程を選択", ["すべて", "1日目", "2日目", "3日目"])
    search = st.text_input("イベント名で検索")

    # 5 後で検索結果に応じたデータを表示する処理を記載



# 2 イベント詳細
def event_detail_page():
    st.title("🎭 イベント詳細")
    
    # 5 後で企画一覧ページで選んだ企画の詳細を表示


# 2 クラス投票結果ページ
def class_vote_result_page():
    st.title("🗳 クラス企画投票結果")
    results = {
        "1年A組": 45,
        "1年B組": 52,
        "2年A組": 38,
        "2年B組": 60
    }
    st.write(results)


# 2 サイドバー（メニュー）
def sidebar():
    st.sidebar.title("📌 メニュー")
    if st.sidebar.button("メイン画面"):
        st.write('メイン画面に移動') # 3 後でメイン画像に遷移する処理に変更
    if st.sidebar.button("メニュー一覧"):
        st.write('メニュー一覧画面に移動') # 3 後でメニュー一覧画像に遷移する処理に変更
    if st.sidebar.button("来場メッセージ"):
        st.write('来場メッセージ画面に移動') # 3 後で来場メッセージ画像に遷移する処理に変更
    if st.sidebar.button("校内マップ"):
        st.write('校内マップ画面に移動') # 3 後で校内マップ画像に遷移する処理に変更
    if st.sidebar.button("クラス企画一覧"):
        st.write('クラス企画一覧画面に移動') # 3 後でクラス企画一覧画像に遷移する処理に変更
    if st.sidebar.button("イベント一覧"):
        st.write('イベント一覧画面に移動') # 3 後でイベント一覧画像に遷移する処理に変更
    if st.sidebar.button("投票結果"):
        st.write('投票結果画面に移動') # 3 後で投票結果画像に遷移する処理に変更

    if st.sidebar.button("ログアウト"):
        st.write('ログアウトしました。') # 3 後でログアウトする処理に変更


# 3 後で画面遷移のためのmain()メソッどを作成


login()