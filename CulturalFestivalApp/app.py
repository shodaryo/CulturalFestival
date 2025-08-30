# 9 ログイン機能、投票機能の削除

# 9 ログイン機能は、ログイン判定をせずにボタンを押したら画面遷移させる（１）
# 9 ログイン画面を表示せずに、最初からメイン画面に画面遷移させる（２）
# 9 投票機能は、メニュー画面とメニューバーから、遷移させるボタンをなくして表示させないようにする（３）

#import
import streamlit as st
import time # 3 追加
import os # 4 追加
from PIL import Image, ImageDraw # 6 追加

# 4 現在のファイル（app.py）のパスを構築
current_dir = os.path.dirname(os.path.abspath(__file__))

# 7 後でinject_fadein_css()（フェードインのcss）
def inject_fadein_css():
    st.markdown("""
        <style>
        .fadein {
            opacity: 0;
            animation: fadeIn1s ease-in-out forwards;
        }

        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }
        </style>
    """, unsafe_allow_html=True)

# 7 後でinject_fadeout_css()（フェードアウトのcss）
def inject_fadeout_css():
    st.markdown("""
        <style>
        .fadeout {
            opacity: 1;
            animation: fadeOut 1s ease-in-out forwards;
        }

        @keyframes fadeOut {
            from { opacity: 1; }
            to { opacity: 0; }
        }
        </style>
    """, unsafe_allow_html=True)

# 7 後でinject_zoom_css()（ズームインのcss）
def inject_zoom_css():
    st.markdown("""
        <style>
        /* ボタン全体をズームイン */
        div.stButton {
            animation: zoomIn 0.6s ease forwards;
            transform: scale(0.8);
        }

        @keyframes zoomIn {
            0% {
                opacity: 0;
                transform: scale(0.8);
            }
            100% {
                opacity: 1;
                transform: scale(1);
            }
        }
        </style>
    """, unsafe_allow_html=True)

# 7 後でset_main_background()（背景画像をフェードイン、フェードアウトする関数）
import base64
def set_main_background():
    image_path="images/メイン画像.png"
    image_path = os.path.join(current_dir, image_path)
    with open(image_path, "rb") as image_file:
        encoded = base64.b64encode(image_file.read()).decode()

    st.markdown(
        f"""
        <style>
        @keyframes fadeIn {{
            from {{ opacity: 0; }}
            to {{ opacity: 1; }}
        }}
        @keyframes fadeOut {{
            from {{ opacity: 1; }}
            to {{ opacity: 0; }}
        }}

        .stApp {{
            background-image: url("data:image/jpg;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
            animation: fadeIn 2s ease-in-out forwards, fadeOut 2s ease-in-out 3s forwards;

        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# 3 後でログイン認証用のuserデータ
users = {"user1": "pass1", "user2": "pass2"}

# 4 後でクラス企画のclass_projectデータ
# 8 クラス企画の最後にカテゴリーを追加
# クラス企画情報（クラス名：企画名, 概要, 詳細, 画像, カテゴリー）
class_project = {
#1年生　※1年1〜3組は合同です（検索時にまとめてヒットするようにしてください）
    "1-1": ["魅惑の乳酸菌(ヨーグルーレット)","ご注文はヨーグルトですか？それとも…？","","images/1-1.jpeg","見る・遊ぶ"],
    "1-2": ["魅惑の乳酸菌(ヨーグルーレット)","ご注文はヨーグルトですか？それとも…？"," ","images/1-1.jpeg","見る・遊ぶ"],
    "1-3": ["魅惑の乳酸菌(ヨーグルーレット)","ご注文はヨーグルトですか？それとも…？"," ","images/1-1.jpeg","見る・遊ぶ"],
    "1-4": ["Dive the sea", "オセアニアの美しい珊瑚礁を回るワクワク冒険アトラクション！！！", "", "images/1-4.jpeg", "見る・遊ぶ"],
    "1-5": ["夢と希望の南国メイド喫茶「MATSU BARA🌹」", "オセアニアの文化に困んだメイド達(動物含む)がお客様をおもてなしします", "", "images/1-5.JPG", "食べる"],
    "1-6": ["らぶりーちゃんのお届けもの❤️", "南の国のらぶりーちゃんが君の心に❤️ちゅーにゅー", "", "images1-6.jpg/", "見る・遊ぶ"],
    "1-7": ["I LOVE okki", "オセアニアをイメージした喫茶店とフォトスポットです！", "", "images/1-7.jpg", "食べる"],
    "1-8": ["激安オーストラリア旅行", "オーストラリアをイメージした南国風のビーチカフェをします！", "", "images/1-8.jpg", "食べる"],
    "1-9": ["Alcatraz Cafe", "北アメリカのアルカトラズ刑務所をモチーフとしたカフェです♡", "", "images/1-9.png", "食べる"],
    "1-10": ["カニカー二のホットドッグ","スポンジボブに出てくるカニカー二のホットドッグショップです。","","images/1-10.jpeg","食べる"],
    "1-11": ["お化け屋敷", "アメリカ風のお化け屋敷です", " ", "images/1-11.png", "見る・遊ぶ"],
    "1-12": ["映画 〜おもちゃの廃墟〜", "ここは人形達が住む廃墟。一度足を踏み入_れたら最後、、、", "", "images/1-12.png", "見る・遊ぶ"],
    "1-13": ["今日、ピンたおしました", "USJ風ピン倒し！倒せば景品！", "", "images/1-13.PNG", "見る・遊ぶ"],


    #中学生
    "1-A": ["少女の遺品が揃う時", "1-Aはイギリスのブラックリー村を元にしたお化け屋敷です。", "", "images/1-A.jpeg", "見る・遊ぶ"],
    "1-B": ["食材を集めて脱出しよう！！", "5種類の料理を集めて制限時間以内に脱出しよう！", "", "images/1-B.JPG", "見る・遊ぶ"],
    "2-A": ["カジノ", "モナコ公国をモチーフに金と黒を基調とした高級カジノ", " ", "images/2-A.jpeg", "食べる"],
    "2-B": ["バモッセオ", "このクラスではコロッセオの中で気配切りをします。", " ", "images/2-B.jpeg", "見る・遊ぶ"],
    "3-A": ["西武台特殊防衛隊", "ヨーロッパに降り注ぐ隕石を撃ち落とすシューティングゲーム", " ", "images/3-A.JPG", "見る・遊ぶ"],
    "3-B": ["3回呼んだ、そのあとで", "呪いの真実に触れる恐怖。鏡の中に潜むブラッディメアリー", " ", "images/3-B.png", "見る・遊ぶ"],




    #2年生
    "2-1": ["空飛ぶ枕とおしゃれなランタン","枕投げや風船バレーで奪われたアラブの姫を助け出せ！","","images/2-1.PNG","見る・遊ぶ"],
    "2-2": ["BOOZA","アラビアンスタイルの店でアイスとジュースを売って待ってます！","","images/2-2.jpeg","食べる"],
    "2-3": ["アラビアンナイトカフェ","お菓子や飲み物などを販売します。またアラビアンな店員がおもてなしや対応したりする。","  ","images/event_dance.jpg","見る・遊ぶ"],
    "2-4": ["海の家かずちゃん","海の家の塩焼きそば屋です！オセアニアの塩を使ってます！","  ","images/2-4.png","食べる"],
    "2-5": ["カフェエイリアンズ","エイリアンたちによる宇宙空間のカフェです","  ","images/2-5.jpg","食べる"],
    "2-6": ["スペースティーカップ","無重力気分！宇宙ティーカップ！","","images/2-6.jpg","見る・遊ぶ"],
    "2-7": ["ピュアスターカフェ","宇宙をコンセプトにしたメイドカフェです。ジュース、お菓子を販売しています。","","images/2-7.jpg","食べる"],
    "2-8": ["スペースフェス","宇宙をコンセプトにした祭りの屋台がテーマです。","","images/2-8.jpg","見る・遊ぶ"],
    "2-9": ["バズ・ライトイヤーのアストロブラスター","東京ディズニーランドにあるアトラクションを表現したもの。","","images/2-9.jpg","見る・遊ぶ"],
    "2-10": ["cafe & photospot","フォトスポットも設置します！","","images/2-10.png","見る・遊ぶ"],
    "2-11": ["アニマルカフェ","たべっ子どうぶつとアフリカの旅","","images/2-11.JPG","食べる"],
    "2-12": ["たべっ子どうぶつとアフリカの旅","たべっ子動物の世界観で射的、輪投げ、ヨーヨー釣りをやります","","images/2-12.jpg","見る・遊ぶ"],
    "2-13": ["フォトスポットワカワカ","ワカワカは明るく輝くことでそんなアフリカのフォトスポットです","","images/2-13.jpg","見る・遊ぶ"],
    "2-14": ["青山家の谷","ミイラがたくさん出てきます。",". ","images/2-14.jpg"," "],
    "2-15": ["You can`t buy happiness Cafe","アフリカの旅気分が味わえるカフェです。","  ","images/2-15.jpg"," "],
    "2-16": ["インディ•ジョーンズ","ディズニーシーにあるインディ•ジョーンズを再現したアドベンチャーです！","  ","images/2-16.jpg","見る・遊ぶ"],


    #3年生
    "3-1": ["夏月空旅(シャーリューコンリュー)","とある架空中国空港の、登場前にくつろげる「ラウンジ」をテーマにした発表です"," ","images/3-1.PNG","見る・遊ぶ"],
    "3-2": ["餃子楼","美味しい餃子を提供します。"," ","images/3-2.JPG","見る・遊ぶ"],
    "3-3": ["3−3‘s Sweets market","デコって楽しむスイーツパラダイス"," ","images/3-3.jpeg","食べる"],
    "3-4": ["サカナとポテトとサブワッフル","オイシイ  \n  セット  \n  ヲアイヲコメテ  \n  ニホンノミンナニ  \n  アゲマス"," ","images/3-4.png","食べる"],
    "3-5": ["和風カフェ","ゆかた美人がミニたい焼と冷たいお茶でおもてなし‼"," ","images/3-5.jpg","食べる"],
    "3-6": ["AMA036便ブダイ発","コーヒーカップを作り、東アジア各国の雰囲気を楽しませる"," ","images/3-6.jpg","見る・遊ぶ"],
    "3-7": ["アジアのオアシス角部屋コーヒー","コスプレ喫茶で可愛いメイドさんたちがお待ちしています。"," ","images/3-7.png","見る・遊ぶ"],
    "3-8": ["カフェ・ハヌル","ハヌル  ＝「空」　自然系、どこか透明感のある韓国カフェ"," ","images/3-8.jpg","食べる"],
    "3-9": ["三九レトロ祭り堂","一昔前のレトロな雰囲気！冷やしパイン・ジュース売ってます！"," ","images/3-9.png","見る・遊ぶ"],
    "3-10": ["PIRA’TES CAFE","海賊をテーマに夏にぴったりの冷たいものを提供します。"," ","images/3-10.png","食べる"],
    "3-11": ["南国カフェ","南国がコンセプトのカフェでドーナツとワッフル、ジュースを売ります。"," ","images/3-11.jpg","食べる"],
    "3-12": ["今日、投げたくなりました。","1泊2日の投げの旅。ポイント高い子には豪華景品が、、、！！"," ","images/3-12.jpg","見る・遊ぶ"],
    "3-13": ["カフェ・サンバってる!?","サンバ衣装のメイドが接客、写真撮影ができる南米風メイド喫茶"," ","images/3-13.jpg","見る・遊ぶ"],
    "3-14": ["夜のジャングル","南国をイメージしたジャングルにして、ワクワクさせます。"," ","images/3-14.PNG","見る・遊ぶ"],
    "3-15": ["Attk panti","インディージョーンズ風の内装の中飲食をしながら映画鑑賞を楽しむ"," ","images/3-15.png","見る・遊ぶ"]
}


# 5 後でイベント企画のevent_projectデータ
# イベント企画情報（企画名: [日程, 時間場所, 概要, 詳細]）
event_project = {
   "新体操部①": ["1日目", "10:00〜 体育館", "Frozen", "演技「アナと雪の女王」・3年生学年演技", "images/新体操部.jpg"],
    "チアダンス部①": ["1日目", "10:00〜 体育館", "Go! Briskly!!", "パワフルな演技をお届けします！ぜひ、見に来てください！", "images/チアダンス.jpg"],
    "吹奏楽部①": ["1日目", "11:20〜 体育館", "SWOアイドルオーディション!", "音楽でみんなの心を掴め！きらきら輝くオーディションをお届け！", "images/吹奏楽部.jpg"],
    "演劇・合唱①": ["1日目", "12:30〜 体育館", "Guest", "合唱部と演劇同好会の合同発表です。歌に合わせて演劇をします。ぜひみに来てください。", "images/演劇同好会.png"],
    "軽音楽部①": ["1日目", "13:30〜 体育館", "軽音ライブ！！", "2日間にわたり、16バンドが演奏します。", "images/軽音楽部.jpg"],
    "書道部①": ["1日目", "10:00〜 書道室", "読めない？雰囲気は分かるはず。", "書道部一同が書いた様々な形の文字をぜひご覧ください！", "images/書道部.png"],
    "美術部①": ["1日目", "10:00〜 物理室", "物理室のアトリエ", "美術部生徒が作った作品や、バリエーション豊富な作品レクリエーションをご堪能あれ。","images/美術部.png"],
    "合唱部①": ["1日目", "10:00〜 第2音楽室", "コンサート in 第二音楽室", "今年のテーマは【宇宙人】！空からやってきたゲストと一緒に旅に出かけませんか？", "images/合唱部.jpg"],
    "電子部①": ["1日目", "10:00〜 147学習室", "電子部", "部員が作成したロボットやゲームを展示します！", "images/電子部.png"],
    "茶道部①": ["1日目", "10:00〜 作法室", "茶の湯が絆ぐ縁", "お点前で感じる“絆“の力", "images/茶道部.png"],
    "家庭科部①": ["1日目", "10:00〜 被服室", "デレラカフェ", "手作りドレスと浴衣の展示、手作りお菓子の販売。", "images/家庭科部.jpg"],
    "文芸部①": ["1日目", "10:00〜 137学習室", "ことばの休憩所", "部員の作品を持ち寄って部誌にしました!休憩所としても是非!", "images/文芸部.jpg"],
    "化学部①": ["1日目", "10:00〜 生化室", " 虫除けスプレーを作ろう", "ハッカから天然素材を使った虫除けスプレーを作ります", "images/化学部.png"],
    "STEAM1①": ["1日目", "10:00〜 STELA1", "STEAM体験", "ロボットカー・レーザーカッター体験・ゲームプログラミング講座", "images/STELA1_.png"],
    "STEAM2①": ["1日目", "10:00〜 STELA2", "ポスターセッション", "STEAMコース生の探究報告から新たな発見が!!", "images/STELA2.png"],
    "STEAM3①": ["1日目", "10:00〜 STELA3", " STEAM個別相談", "STEAMの個別相談を希望の方はこちらへ", "images/相談室.jpg"],
    "個別相談①": ["1日目", "10:00〜 小接室 ", " 受験生個別相談", "受験生の個別相談を希望の方はこちらへ","images/相談室.jpg"],
    
    "軽音楽部②": ["2日目", "09:15〜 体育館", "軽音ライブ！！", "2日間にわたり、16バンドが演奏します。", "images/軽音楽部.jpg"],
    "吹奏楽部②": ["2日目", "12:00〜 体育館", "SWOアイドルオーディション!", "音楽でみんなの心を掴め！きらきら輝くオーディションをお届け！", "images/吹奏楽部.jpg"],
    "演劇・合唱②": ["2日目", "13:10〜 体育館", "Guest", "合唱部と演劇同好会の合同発表です。歌に合わせて演劇をします。ぜひみに来てください。", "images/演劇同好会.png"],
    "新体操部②": ["2日目", "14:00〜 体育館", "Frozen", "演技「アナと雪の女王」・3年生学年演技", "images/新体操部.jpg"],
    "チアダンス部②": ["2日目", "14:00〜 体育館", "Go! Briskly!!", "パワフルな演技をお届けします！ぜひ、見に来てください！", "images/チアダンス.jpg"],
    "書道部②": ["2日目", "9:00〜 書道室", "読めない？雰囲気は分かるはず。", "書道部一同が書いた様々な形の文字をぜひご覧ください！", "images/書道部.png"],
    "美術部②": ["2日目", "9:00〜 物理室", "物理室のアトリエ", "美術部生徒が作った作品や、バリエーション豊富な作品レクリエーションをご堪能あれ。","images/美術部.png"],
    "合唱部②": ["2日目", "9:00〜 第2音楽室", "コンサート in 第二音楽室", "今年のテーマは【宇宙人】！空からやってきたゲストと一緒に旅に出かけませんか？", "images/合唱部.jpg"],
    "電子部②": ["2日目", "9:00〜 147学習室", "電子部", "部員が作成したロボットやゲームを展示します！", "images/電子部.png"],
    "茶道部②": ["2日目", "9:00〜 作法室", "茶の湯が絆ぐ縁", "お点前で感じる“絆“の力", "images/茶道部.png"],
    "家庭科部②": ["2日目", "9:00〜 被服室", "デレラカフェ", "手作りドレスと浴衣の展示、手作りお菓子の販売。", "images/家庭科部.jpg"],
    "文芸部②": ["2日目", "9:00〜 137学習室", "ことばの休憩所", "部員の作品を持ち寄って部誌にしました!休憩所としても是非!", "images/文芸部.jpg"],
    "化学部②": ["2日目", "9:00〜 生化室", " 虫除けスプレーを作ろう", "ハッカから天然素材を使った虫除けスプレーを作ります", "images/化学部.png"],
    "STEAM1②": ["2日目", "9:00〜 STELA1", "STEAM体験", "ロボットカー・レーザーカッター体験・ゲームプログラミング講座", "images/STELA1_.png"],
    "STEAM2②": ["2日目", "9:00〜 STELA2", "ポスターセッション", "STEAMコース生の探究報告から新たな発見が!!", "images/STELA2.png"],
    "STEAM3②": ["2日目", "9:00〜 STELA3", " STEAM個別相談", "STEAMの個別相談を希望の方はこちらへ", "images/相談室.jpg"],
    "個別相談②": ["2日目", "9:00〜 小接室", " 受験生個別相談", "受験生の個別相談を希望の方はこちらへ","images/相談室.jpg"]
}


# 9（2） 最初からメイン画面を表示させる
# 3 後でセッション状態の初期化
if 'logged_in' not in st.session_state:
    # 9（２）session_stateのlogged_inを最初からTrueにしておく
    # logged_inがFalse→ログイン画面、True→メイン画面 になるため
    st.session_state.logged_in = True

# 以下、画面を作成
# ログイン画面
def login():
    st.title("🎌 文化祭案内アプリ")
    st.subheader("ログインしてください")

    # 9（１） ログイン用の入力欄をコメントアウト
    # username = st.text_input("ユーザー名")
    # password = st.text_input("パスワード", type="password")

    # 9（１） ログインボタンを押したら、判定を行わずに次の画面に遷移させる（該当箇所をコメントアウト）
    # 3 後でログイン機能に変更
    if st.button("ログイン"):
        # 9（1）if username in users and users[username] == password:
            st.session_state.logged_in = True
            st.session_state.page = "main"  # ✅ メインページへ遷移
            st.rerun()  # ✅ ここで画面再描画（ログイン画面を即消す）
        # else:
            # st.error("ユーザー名またはパスワードが間違っています。")


# メイン画面
def main_page():
    # 7 後で文字または画像のフェードイン、フェードアウトに変更
    # st.title("🌟 文化祭アプリ！")
    # st.write("画面左のメニューから、各機能に移動できます。")
    set_main_background()

    # 3 後で自動での画面遷移
    time.sleep(5)
    st.session_state.page = "menu"
    st.rerun()


# メニュー画面
def menu_page():
    # 7 あとでズームイン処理のcss（inject_zoom_css()）+ボタン表示にラグを追加（time.sleep(0.5)）
    inject_zoom_css()
    
    st.header("📋 メニュー")
    st.write("文化祭に関する各ページに移動できます。")    

    if st.button("🎪 クラス企画一覧"):
        st.session_state.page = "class_list"# 3 押したら画面遷移する処理に後で変更
        st.rerun()
    
    if st.button("📅 イベント一覧"):
        st.session_state.page = "event_list"# 3 押したら画面遷移する処理に後で変更
        st.rerun()
    
    if st.button("🏫 校内マップ"):
        st.session_state.page = "map"# 3 押したら画面遷移する処理に後で変更
        st.rerun()

    
    if st.button("🎉 メッセージページ"):
        st.session_state.page = "message"# 3 押したら画面遷移する処理に後で変更
        st.rerun()
    
    # 9（２） 投票結果へ遷移させるためのボタンをコメントアウトして、表示させないようにする
    # if st.button("🗳 投票結果"):
    #     st.session_state.page = "vote_result"# 3 押したら画面遷移する処理に後で変更
    #     st.rerun()


# メッセージページ
def message_page():
    st.title("🎉 来場者へのメッセージ")
    st.write("ようこそ文化祭へ！楽しい企画が盛りだくさんです。ぜひ最後までお楽しみください。")


# 8 地図の選択を追加。また、class_categories（学年カテゴリごとの部屋名）を追加して、カテゴリごとにどのクラスがあるかを保存。
# 校内マップ画面
def map_page():
    st.header("🏫 校内マップ")

    # 地図の選択
    map_options = {
        "学校全体図": "images/学校全体図.jpg",
        "校舎全体": "images/校舎全体図.jpg",
        "第１・３校舎": "images/第１、３校舎.jpg",
        "第２校舎": "images/第２校舎.jpg",
        "模擬店": "images/模擬店.jpg"
    }
    selected_map = st.radio("地図を選んでください", list(map_options.keys()), horizontal=True)

    # 学年カテゴリごとの部屋名
    class_categories={
   "中学1年":["1-A","1-B"],
   "中学2年":["2-A","2-B"],
   "中学3年":["3-A","3-B"],
   "高校1年・第1校舎":["1-1","1-2","1-3"],
   "高校1年・第2校舎":["1-4","1-5","1-6","1-7","1-8","1-9","1-11","1-12","1-13"],
   "高校2年・第1校舎":["2-1","2-2","2-3"],
   "高校2年・第2校舎":["2-5","2-6","2-7","2-8","2-9","2-10","2-11","2-12","2-13","2-14","2-15","2-16"],
   "高校3年":["3-1","3-3","3-5","3-6","3-7","3-8","3-9","3-10","3-11","3-12","3-13","3-14","3-15"],
   "第1,3校舎部活動・その他":["女子トイレ","男子トイレ","被服室","物理室","生物化学室","STELA3","STELA2","STELA1","書道室","保健室","会議室","多目的室","体育館","147学習室","137学習室"],
   "第2校舎部活動・その他":["女子トイレ ","男子トイレ ","第2音楽室",],
   "生徒会館":["生徒会館"],
   "模擬店クラス":["3-4","3-2","2-4","1-10"],
   "金券":["金券"],
   "受付":["受付"]
   }


    # 地図に応じた選択肢のフィルタリング
    available_categories = []
    if selected_map == "校舎全体":
        available_categories = [] # 空白
    elif selected_map == "第１・３校舎":
        available_categories = ["中学1年","中学2年","中学3年","高校1年・第1校舎","高校2年・第1校舎","高校3年","第1,3校舎部活動・その他"]
    elif selected_map == "第２校舎":
        available_categories = ["高校1年・第2校舎","高校2年・第2校舎","高校3年・第2校舎","第2校舎部活動・その他"]
    elif selected_map == "学校全体図":	
        available_categories = ["金券","受付","生徒会館"]
    elif selected_map == "模擬店":
        available_categories = ["模擬店クラス"]


    # 学年カテゴリの選択
    selected_grade = st.selectbox("学年・その他カテゴリを選択", ["選択してください"] + available_categories)

    # クラス・部屋の選択
    selected_room = None
    if selected_grade != "選択してください":
        rooms = class_categories.get(selected_grade, [])
        selected_room = st.selectbox("クラス・部屋名を選んでください", ["選択してください"] + rooms)
        if selected_room == "選択してください":
            selected_room = None

    # 地図画像の読み込みと表示
    image_path = os.path.join(current_dir, map_options[selected_map])
    base_image = Image.open(image_path).convert("RGBA")
    overlay = Image.new("RGBA", base_image.size, (255, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)

    # 教室座標（今は地図に依存せず共通にしてます）
    room_locations = {
        
        #学校全体図
        "受付": [(1058, 931, 1164, 977 )],
        "金券": [(627, 817, 707, 893)],
        "生徒会館": [(1073, 1093, 1161, 1335)],

        #第1校舎
        #4階
        "3-15": [(312, 285, 393, 375)],
        "3-14": [(399, 285, 485, 375)],
        "3-13": [(491, 285, 578, 375)],
        "3-12": [(584, 285, 660, 375)],
        "3-11": [(665, 285, 745, 375)],
        "3-10": [(750, 285, 831, 375)],
        #3階
        "3-9": [(312, 411, 406, 486)],
        "3-8": [(412, 411, 494, 486)],
        "3-7": [(312, 609, 393, 696)],
        "3-6": [(399, 609, 484, 696)],
        "3-5": [(490, 609, 577, 696)],
        "3-3": [(584, 609, 658, 696)],
        "3-2": [(664, 609, 746, 696)],
        "3-1": [(752, 609, 831, 696)],
        #2階
        "2-3": [(310, 943, 392, 1026)],
        "2-2": [(397, 943, 481, 1026)],
        "2-1": [(487, 943, 575, 1026)],
        "1-3": [(582, 943, 831, 1026)],
        "1-2": [(582, 943, 831, 1026)],
        "1-1": [(582, 943, 831, 1026)],
        #1階

        #第3校舎
        #3階
        "3-A": [(270, 1732, 351, 1796)],
        "3-B": [(270, 1801, 351, 1863)],
        "2-A": [(270, 1870, 351, 1930)],
        #2階
        "1-A": [(429, 1732, 510, 1796)],
        "1-B": [(429, 1801, 510, 1863)],
        "2-B": [(429, 1870, 510, 1930)],
        #1階

        #特別教室
        #第1校舎
        #4階
        "物理室": [(586, 83, 686, 159)],
        "生物化学室": [(736, 83, 831, 159)],
        "147学習室": [(461, 83, 531, 159)],
        #3階
        "被服室": [(557, 411, 654, 486)],
         "137学習室": [(500, 411, 552, 486)],
        #2階
        "STELA3": [(310, 734, 388, 811)],
        "STELA2": [(394, 734, 491, 811)],
        "STELA1": [(497, 734, 598, 811)],
        "書道室": [(722, 734, 831, 811)],
        #1階
        "保健室": [(362, 1107, 423, 1183)],
        #"小応接室": [(613, 1107, 706, 1183)],
        #"職員室": [(367, 1311, 621, 1393)],
        #"事務室": [(716, 1311, 775, 1393)],

        #その他
        "会議室": [(907, 385, 963, 690)],
        "体育館": [(1043, 438, 1376, 781)],

        #第3校舎
        "多目的室": [(584, 1811, 665, 1930)],

        "男子トイレ":[
            #第1校舎
            #4階
            (407, 187, 460, 262),
            #3階
            (407, 514, 460, 588),
            #2階
            (407, 839, 460, 913),
            #1階
            (365, 1213, 460, 1288),


            #第3校舎
            #3階
            (270, 1672, 351, 1727),
            #2階
            (428, 1672, 510, 1727),
            #1階
            (584, 1672, 665, 1727),
        ],
        "女子トイレ":[
            #第1校舎
            #4階
            (667, 187, 715, 262),
            #3階
            (667, 514, 715, 588),
            #2階
            (667, 839, 715, 913),
            #1階
            (667, 1213, 715, 1288),

            #第3校舎
            #3階
            (270, 1672, 351, 1727),
            #2階
            (428, 1672, 510, 1727),
            #1階
            (584, 1672, 665, 1727)
        ],
    
            #第2校舎
            #4階
            "1-13": [(223, 308, 315, 380)],
            "1-12": [(320, 308, 412, 380)],
            "1-11": [(417, 308, 515, 380)],
            "1-10": [(521, 308, 604, 380)],
            "1-9": [(653, 390, 740, 469)],
            #3階
            "1-8": [(231, 636, 322, 713)],
            "1-7": [(327, 636, 419, 713)],
            "1-6": [(424, 636, 520, 713)],
            "1-5": [(525, 636, 609, 713)],
            "1-4": [(659, 725, 745, 803)],
            "2-4": [(1066, 725, 1160, 803)],
            "3-4": [(1165, 725, 1259, 803)],
            #2階
            "2-16": [(224, 953, 318, 1025)],
            "2-15": [(323, 953, 412, 1025)],
            "2-14": [(417, 953, 516, 1025)],
            "2-13": [(520, 953, 600, 1025)],
            "2-12": [(1052, 1042, 1152, 1114)],
            "2-11": [(1157, 1042, 1247, 1114)],
            #1階
            "2-10": [(222, 1196, 315, 1275)],
            "2-9": [(321, 1196, 411, 1275)],
            "2-8": [(417, 1196, 514, 1275)],
            "2-7": [(520, 1196, 601, 1275)],
            "2-6": [(1052, 1285, 1134, 1363)],
            "2-5": [(1139, 1285, 1234, 1363)],

            #第2校舎特別教室
            #4階
            "第2音楽室": [(1058, 336, 1254, 469)],
            #3階

            #2階
            #Map上の左から
            "学習室": [
              (129, 953, 180, 1025),
              (653, 1042, 738, 1114),
              (1333, 1025, 1375, 1112),
            #1階
              (653, 1285, 740, 1364)
              ],
              
            "男子トイレ ":[
                #第2校舎
                #4階
                (745, 390, 810, 469), 
                #3階
                (750, 725, 817, 803),
                #2階
                (744, 1042, 810, 1114),
                #1階 
                (745, 1285, 811, 1363),
                ],

            "女子トイレ ":[
                #第2校舎
                #4階
                (745, 390, 810, 469), 
                #3階
                (750, 725, 817, 803),
                #2階
                (744, 1042, 810, 1114),
                #1階 
                (745, 1285, 811, 1363),
                ],

              #模擬店
              "3-4":[(251, 384, 434, 592)],
              "3-2":[(251, 608, 434, 822)],
              "2-4":[(251, 837, 434, 1036)],
              "1-10":[(251, 1052, 434, 1252)],
    }


    # 赤枠でハイライト
    if selected_room and selected_room in room_locations:
        # 1つの部屋が選ばれていればその部屋だけを赤枠
        for box in room_locations[selected_room]:
            draw.rectangle(box, fill=(255, 0, 0, 100))
    
    elif selected_grade != "選択してください" and selected_room is None:
        # クラス・部屋が未選択なら、カテゴリ内の全クラス・部屋を赤枠表示
        rooms = class_categories.get(selected_grade, [])
        for room in rooms:
            if room in room_locations:
                for box in room_locations[room]:
                    draw.rectangle(box, fill=(255, 0, 0, 100))


    combined = Image.alpha_composite(base_image, overlay)
    st.image(combined, use_container_width=True)

    # 部屋情報の表示
    if selected_room and selected_room in class_project:
        title, desc, _, _, _ = class_project[selected_room]
        st.subheader(f"{selected_room}：{title}")
        st.write(desc)
        if st.button(f"{selected_room} の企画を見る", key=f"map_{selected_room}"):
            st.session_state.selected_class = selected_room
            st.session_state.page = "class_detail"
            st.session_state.map = True
            st.rerun()




# 8 クラス企画一覧でカテゴリーごとに企画を取得する
# クラス企画一覧
def class_list_page():
    st.title("🏫 クラス企画一覧")

    # カテゴリを選ぶ（ラジオボタン）
    selected_category = st.radio("カテゴリで絞り込み", ["すべて", "見る・遊ぶ", "食べる"], horizontal=True)

    # 該当カテゴリに属するクラス名だけ抽出
    class_names = [
        name for name, data in class_project.items()
        if selected_category == "すべて" or data[4] == selected_category
    ]

    # プルダウンでさらに絞り込む
    selected_class = st.selectbox("クラスを選んでください", ["選択してください"] + class_names)

    # 「選択してください」の場合：カテゴリ内のすべて表示
    if selected_class == "選択してください":
        for name in class_names:
            title, desc, _, _, _ = class_project[name]
            st.subheader(f"{name}：{title}")
            st.write(desc)
            if st.button(f"{name} の企画を見る", key=f"class_{name}"):
                st.session_state.selected_class = name
                st.session_state.page = "class_detail"
                st.session_state.map = False
                st.rerun()
            st.write("---")

    # プルダウンで1つ選ばれた場合のみ表示
    else:
        title, desc, _, _, _ = class_project[selected_class]
        st.subheader(f"{selected_class}：{title}")
        st.write(desc)
        if st.button(f"{selected_class} の企画を見る", key=f"class_{selected_class}"):
            st.session_state.selected_class = selected_class
            st.session_state.page = "class_detail"
            st.session_state.map = False
            st.rerun()



# クラス企画詳細
def class_detail_page():
    st.title("🎪 クラス企画詳細")

    # 4 後で企画一覧、校内マップ一覧で押したボタンの企画詳細を表示
    class_name = st.session_state.get("selected_class", "不明なクラス")
    # 8 class_projectで追加したカテゴリー分、取得する要素数を増やす
    title, desc, detail, image_path, _ = class_project.get(class_name, ["不明", "情報が見つかりませんでした。", "", None, ""])
    image_path = os.path.join(current_dir, image_path)
    st.subheader(f"{class_name}：{title}")
    st.write(desc)
    st.markdown("---")
    st.write(detail)

    if image_path:
        st.image(image_path, caption=f"{class_name} の展示写真", use_container_width=True)

    if st.session_state.map:
        if st.button("← マップに戻る"):
            st.session_state.page = "map"
            st.rerun()
    else:
        if st.button("← クラス一覧に戻る"):
            st.session_state.page = "class_list"
            st.rerun()

# イベント一覧
def event_list_page():
    st.title("📅 イベント一覧")
    day = st.selectbox("日程を選択", ["すべて", "1日目", "2日目"])
    search = st.text_input("イベント名で検索")

    # 5 後で検索結果に応じたデータを表示する処理を記載
    for name, (event_day, time_place, summary, _, _) in event_project.items():
        if (day == "すべて" or event_day == day) and (search in name):
            st.subheader(name)
            st.write(f"🗓 {event_day}　🕒 {time_place}")
            st.write(summary)
            if st.button(f"{name} の詳細を見る", key=f"event_{name}"):
                st.session_state.selected_event = name
                st.session_state.page = "event_detail"
                st.rerun()
            st.write("---------------------")



# イベント詳細
def event_detail_page():
    st.title("🎭 イベント詳細")
    
    # 5 後で企画一覧ページで選んだ企画の詳細を表示
    name = st.session_state.get("selected_event", "不明なイベント")
    event_day, time_place, _, detail, image_path = event_project.get(name, ["日程不明", "時間不明", "", "詳細情報はありません。", None])
    image_path = os.path.join(current_dir, image_path)
    st.subheader(name)
    st.write(f"🗓 {event_day}　🕒 {time_place}")
    st.markdown("---")
    st.write(detail)

    if image_path:
        st.image(image_path, caption=f"{name}", use_container_width=True)

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
        st.session_state.page = "main"# 3 後でメイン画像に遷移する処理に変更
        st.rerun()
    if st.sidebar.button("メニュー一覧"):
        st.session_state.page = "menu"# 3 後でメニュー一覧画像に遷移する処理に変更
        st.rerun()
    if st.sidebar.button("来場メッセージ"):
        st.session_state.page = "message"# 3 後で来場メッセージ画像に遷移する処理に変更
        st.rerun()
    if st.sidebar.button("校内マップ"):
        st.session_state.page = "map"# 3 後で校内マップ画像に遷移する処理に変更
        st.rerun()
    if st.sidebar.button("クラス企画一覧"):
        st.session_state.page = "class_list"# 3 後でクラス企画一覧画像に遷移する処理に変更
        st.rerun()
    if st.sidebar.button("イベント一覧"):
        st.session_state.page = "event_list"# 3 後でイベント一覧画像に遷移する処理に変更
        st.rerun()
    # 9（３） メニューバーの投票結果ボタンを削除
    # if st.sidebar.button("投票結果"):
    #     st.session_state.page = "vote_result"# 3 後で投票結果画像に遷移する処理に変更
    #     st.rerun()

    # 9（２） ログアウトボタンを削除する
    # if st.sidebar.button("ログアウト"):
    #     st.session_state.logged_in = False # 3 後でログアウトする処理に変更
    #     st.session_state.page = "main"
    #     st.rerun()

# 3 後で画面遷移のためのmain()メソッどを作成
def main():
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False

    if not st.session_state.logged_in:
        login()
        return  # ログインしていない場合は他の描画をしない

    # 以下ログイン後のページ表示処理
    if 'page' not in st.session_state:
        st.session_state.page = "main"

    if st.session_state.page not in ['main', 'menu']:
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


main() # 3 画面操作をmain()に変更
