# ページ、サイドバー作成

#import
import streamlit as st

# 4 現在のファイル（app.py）のパスを構築

# 後でinject_fadein_css()（フェードインのcss）

# 後でinject_fadeout_css()（フェードアウトのcss）

# 後でinject_zoom_css()（ズームインのcss）

# 後でset_main_background()（背景画像をフェードイン、フェードアウトする関数）

# 3 後でログイン認証用のuserデータ

# 4 後でクラス企画のclass_projectデータ

# 後でイベント企画のevent_projectデータ

# 3 後でセッション状態の初期化

# 以下、画面を作成
# 2 ログイン画面
def login():
    st.title('ログイン')




    
    # 3 後でログイン機能に変更


# 2 メイン画面
def main_page():
    st.title('メイン')
    #後で文字または画像のフェードイン、フェードアウトに変更
    
    

    # 3 後で自動での画面遷移


# 2 メニュー画面
def menu_page():
    st.title('メニュー')
    # あとでズームイン処理のcss（inject_zoom_css()）+ボタン表示にラグを追加（time.sleep(0.5)）
    
    
    

    
        # 3 押したら画面遷移する処理に後で変更
    
    
        # 3 押したら画面遷移する処理に後で変更
    
    
        # 3 押したら画面遷移する処理に後で変更
    
    
        # 3 押したら画面遷移する処理に後で変更
    
    
        # 3 押したら画面遷移する処理に後で変更


# 2 メッセージページ
def message_page():
    st.title('タイトル')

# 2 校内マップ画面
def map_page():
    st.title('タイトル')
    

    # 後で表示カテゴリのセレクトボックスcategory
    # 後で部屋名の検索ボックスsearch_term

    # 後でオーバーレイ画像の作成
    
    

    # 後で検索条件に応じて、表示するボタンを変える
    
        
    
        


# 2 クラス企画一覧ページ
def class_list_page():
    st.title('タイトル')
    


    # 4 後で検索結果に応じて一覧を表示する処理に変更
    
        


# 2 クラス企画詳細
def class_detail_page():
    st.title('タイトル')
    
    
    # 4 後で企画一覧、校内マップ一覧で押したボタンの企画詳細を表示

# 2 イベント一覧
def event_list_page():
    st.title('タイトル')
    
    
    

    # 後で検索結果に応じたデータを表示する処理を記載



# 2 イベント詳細
def event_detail_page():
    st.title('タイトル')
    
    
    # 後で企画一覧ページで選んだ企画の詳細を表示


# 2 クラス投票結果ページ
def class_vote_result_page():
    st.title('タイトル')
    
    
    
    
    
    
    
    


# 2 サイドバー（メニュー）
def sidebar():
    st.title('サイドバー')
    
    
         # 3 後でメイン画像に遷移する処理に変更
    
         # 3 後でメニュー一覧画像に遷移する処理に変更
    
         # 3 後で来場メッセージ画像に遷移する処理に変更
    
         # 3 後で校内マップ画像に遷移する処理に変更
    
         # 3 後でクラス企画一覧画像に遷移する処理に変更
    
         # 3 後でイベント一覧画像に遷移する処理に変更
    
         # 3 後で投票結果画像に遷移する処理に変更

    
         # 3 後でログアウトする処理に変更


# 3 後で画面遷移のためのmain()メソッどを作成


# login()
menu_page()
sidebar()