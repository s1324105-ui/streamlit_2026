import streamlit as st

st.set_page_config(
    page_title="世界の朝食診断アプリ",
    page_icon="🍳",
    layout="centered"
)

import base64

def get_base64(file):
    with open(file, "rb") as f:
        return base64.b64encode(f.read()).decode()

sunrise = get_base64("sekai.png")
kami = get_base64("kami.jpg")

# 背景
st.markdown(
    f"""
    <style>

    .stApp {{
        background-image:
            linear-gradient(
                rgba(255,255,255,0.15),
                rgba(255,255,255,0.15)
            ),
            url("data:image/jpeg;base64,{sunrise}"),
            url("data:image/jpeg;base64,{kami}");

        background-size:
            cover,
            70%,
            cover;

        background-position:
            center,
            center,
            center;

        background-repeat:
            no-repeat,
            no-repeat,
            no-repeat;

        background-attachment: fixed;
    }}

    </style>
    """,
    unsafe_allow_html=True
)

# 半透明パネル
st.markdown(
    """
    <style>

    .block-container {
        background: rgba(255,255,255,0.85);
        padding: 2rem;
        border-radius: 20px;
    }

    </style>
    """,
    unsafe_allow_html=True
)
st.title("🍳 世界の朝食診断アプリ")
st.caption("おすすめの世界の朝食を15の国から診断します！")

# =========================
# 朝食データ
# =========================

breakfast_data = {
    "油条・豆漿（中国）": {
        "color": "レッド",
        "mood": "元気を出したい",
        "food": "パン",
        "info": "揚げパンを豆乳につけて食べる中国の定番朝食です。",
        "ingredients": "油条（揚げパン）、豆乳",
        "time": 20,
        "difficulty": "★★★☆☆",
        "image": "cyu.jpg",
        "url": "https://komonjocooking.hatenablog.com/entry/2020/07/14/100000#%E3%83%95%E3%83%A9%E3%82%A4%E3%83%91%E3%83%B3%E3%81%A7%E6%8F%9A%E3%81%92%E3%82%8B"
    },
    "フォー（ベトナム）": {
        "color": "グリーン",
        "food": "麺",
        "mood": "さっぱり食べたい",
        "info": "あっさりしたスープと米粉麺で朝にぴったり。",
        "ingredients": "フォー麺、鶏肉、ねぎ、パクチー",
        "time": 30,
        "difficulty": "★★☆☆☆",
        "image": "fo.jpg",
        "url": "https://cookpad.com/search/フォー"
    },
    "イングリッシュ・ブレックファースト（イギリス）": {
        "color": "ブラウン",
        "food": "肉",
        "mood": "お腹いっぱい食べたい",
        "info": "卵やソーセージなどボリューム満点。",
        "ingredients": "卵、ソーセージ、ベーコン、トマト、トースト",
        "time": 25,
        "difficulty": "★★★☆☆",
        "image": "igi.jpg",
        "url": "https://ouchi-gohan.jp/2883/"
    },
    "クロックムッシュ（フランス）": {
        "color": "ネイビー",
        "food": "パン",
        "mood": "ゆっくり過ごしたい",
        "info": "フランスらしい優雅な朝食です。",
        "ingredients": "食パン、チーズ、ハム",
        "time": 10,
        "difficulty": "★☆☆☆☆",
        "image": "ku.jpeg",
        "url": "https://cookpad.com/jp/search/フランス%20朝ご飯"
    },
    "チュロス（スペイン）": {
        "color": "オレンジ",
        "food": "スイーツ",
        "mood": "甘いものが食べたい",
        "info": "チョコレートにつけて食べる人気朝食。",
        "ingredients": "小麦粉、水、砂糖、チョコレートソース",
        "time": 30,
        "difficulty": "★★★☆☆",
        "image": "supe.jpeg",
        "url": "https://www.cotta.jp/special/article/?p=56727"
    },
    "コルネット・カプチーノ（イタリア）": {
        "color": "ピンク",
        "food": "パン",
        "mood": "甘いものが食べたい",
        "info": "甘いパンとコーヒーの組み合わせ。",
        "ingredients": "コルネット、エスプレッソ、牛乳",
        "time": 10,
        "difficulty": "★☆☆☆☆",
        "image": "ita.jpg",
        "url": "https://note.com/mmaabboo/n/na467dca52c64"
    },
    "プーロ（フィンランド）": {
        "color": "アクア",
        "food": "ごはん",
        "mood": "さっぱり食べたい",
        "info": "ベリーを添えた北欧のおかゆ。",
        "ingredients": "オーツ麦、牛乳、水、ベリー",
        "time": 15,
        "difficulty": "★☆☆☆☆",
        "image": "fin.jpeg",
        "url": "https://mogurafinland.com/puuro-finland/"
    },
    "カーシャ（ロシア）": {
        "color": "ホワイト",
        "food": "ごはん",
        "mood": "元気を出したい",
        "info": "そばの実を使った栄養満点の料理。",
        "ingredients": "そばの実、牛乳または水、バター",
        "time": 20,
        "difficulty": "★★☆☆☆",
        "image": "rosi.jpeg",
        "url": "https://www.konaya.jp/knowledge/recipe/kasza.html"
    },
    "ワッフル（アメリカ）": {
        "color": "イエロー",
        "food": "スイーツ",
        "mood": "甘いものが食べたい",
        "info": "シロップたっぷりで楽しみます。",
        "ingredients": "小麦粉、卵、牛乳、バター、シロップ",
        "time": 20,
        "difficulty": "★★★☆☆",
        "image": "ame.jpeg",
        "url": "https://delishkitchen.tv/recipes/171096799996543379"
    },
    "メープルパンケーキ（カナダ）": {
        "color": "ゴールド",
        "food": "スイーツ",
        "mood": "甘いものが食べたい",
        "info": "メープルシロップが魅力。",
        "ingredients": "小麦粉、卵、牛乳、メープルシロップ",
        "time": 20,
        "difficulty": "★★☆☆☆",
        "image": "kana.jpg",
        "url": "https://www.asahibeer.co.jp/enjoy/recipe/search/recipe.psp.html?CODE=0000000125"
    },
    "ごはん・みそ汁・納豆（日本）": {
        "color": "ブラウン",
        "food": "ごはん",
        "mood": "元気を出したい",
        "info": "栄養バランス抜群の和朝食。",
        "ingredients": "ごはん、みそ、豆腐、わかめ、納豆",
        "time": 20,
        "difficulty": "★★☆☆☆",
        "image": "niho.jpg",
        "url": "https://www.maff.go.jp/j/pr/aff/2306/spe1_04.html"
    },
    "チチャロンサンド（ペルー）": {
        "color": "イエロー",
        "food": "肉",
        "mood": "お腹いっぱい食べたい",
        "info": "揚げ豚肉を挟んだボリューム満点サンド。",
        "ingredients": "豚肉、パン、玉ねぎ、さつまいも",
        "time": 40,
        "difficulty": "★★★★☆",
        "image": "pr.jpeg",
        "url": "https://www.bras-de-chef.com/recipes/チチャロン"
    },
    "トースタ・ミスタ（ポルトガル）": {
        "color": "レッド",
        "mood": "さっぱり食べたい",
        "food": "パン",
        "info": "たっぷりのチーズとハムを挟んでトーストしたサンドイッチのこと。オレンジジュースと一緒にどうぞ",
        "ingredients": "チーズ、ハム、トースト、オレンジジュース",
        "time": 15,
        "difficulty": "★☆☆☆☆",
        "image": "poru.jpg",
        "url": "https://www.marumitsu.jp/worldbreakfast/?id=62"
    },
    "ジョークとパートンコー（タイ）": {
        "color": "レッド",
        "mood": "さっぱり食べたい",
        "food": "ごはん",
        "info": "「ジョーク（โจ๊ก）」とはお米の粒がわからなくなるまで煮込んだおかゆのこと。中国式の甘くない揚げパン「パートンコー（ปาท่องโก๋）」も朝の定番。調味料と一緒にアレンジできる",
        "ingredients": "米、パン、鶏肉、しょうが",
        "time": 20,
        "difficulty": "★★★☆☆",
        "image": "tai.jpg",
        "url": "https://www.marumitsu.jp/worldbreakfast/?id=24"
    },
    "ナシ・クニン（インドネシア）": {
        "color": "レッド",
        "mood": "ゆっくり過ごしたい",
        "food": "ごはん",
        "info": "「ナシ・クニン（nasi kuning）」とはターメリックとココナッツミルクで一緒に炊いたご飯のこと。おかずなどと一緒に食べるとよりしっかり食べられる",
        "ingredients": "ターメリック、ココナッツミルク、米、（肉、卵、キュウリ）",
        "time": 40,
        "difficulty": "★★☆☆☆",
        "image": "indne.jpg",
        "url": "https://www.marumitsu.jp/worldbreakfast/?id=42"
    },
}

# =========================
# サイドバー
# =========================

st.sidebar.title("🌎 世界の朝食図鑑")

selected_menu = st.sidebar.selectbox(
    "見たい朝食を選んでください",
    list(breakfast_data.keys())
)

st.sidebar.subheader(selected_menu)
st.sidebar.write(breakfast_data[selected_menu]["info"])

st.sidebar.write("🧂 材料")
st.sidebar.caption(breakfast_data[selected_menu]["ingredients"])

st.sidebar.write("⏰ 調理時間")
st.sidebar.caption(f"約{breakfast_data[selected_menu]['time']}分")

st.sidebar.image(
    breakfast_data[selected_menu]["image"],
    caption=selected_menu,
    use_container_width=True
)

# =========================
# メイン
# =========================

st.markdown("---")
st.subheader("🧡 朝食診断")

morning_mood = st.selectbox(
    "今朝の気分は？",
    [
        "元気を出したい",
        "ゆっくり過ごしたい",
        "甘いものが食べたい",
        "さっぱり食べたい",
        "お腹いっぱい食べたい"
    ]
)

favorite_food = st.selectbox(
    "朝に食べたいのは？",
    ["パン", "麺", "ごはん", "スイーツ", "肉"]
)

time_choice = st.selectbox(
    "朝食にかけられる時間は？",
    ["10分以内", "20分以内", "30分以内", "40分以上"]
)

time_map = {
    "10分以内": 10,
    "20分以内": 20,
    "30分以内": 30,
    "40分以上": 999
}
selected_time = time_map[time_choice]

difficulty_choice = st.selectbox(
    "料理の難易度は？",
    [
        "★☆☆☆☆",
        "★★☆☆☆",
        "★★★☆☆",
        "★★★★☆",
        "★★★★★"
    ]
)
difficulty_map = {
    "★☆☆☆☆": 1,
    "★★☆☆☆": 2,
    "★★★☆☆": 3,
    "★★★★☆": 4,
    "★★★★★": 5
}

selected_difficulty = difficulty_map[difficulty_choice]



# =========================
# 診断
# =========================

if st.button("診断する！"):

    best_score = -1
    recommendation = None

    for breakfast, data in breakfast_data.items():

        score = 0

        # 食べたいもの
        if data["food"] == favorite_food:
            score += 3

        # 気分
        if data["mood"] == morning_mood:
            score += 3

        # 時間
        if data["time"] <= selected_time:
            score += 2

        # 難易度
        if difficulty_map[data["difficulty"]] <= selected_difficulty:
            score += 2

        # 一番高得点の朝食を保存
        if score > best_score:
            best_score = score
            recommendation = breakfast
    if recommendation:

        result = breakfast_data[recommendation]

        st.balloons()

        st.success(f"あなたにおすすめの朝食は『{recommendation}』です！")

        st.write("### 朝食紹介")
        st.info(result["info"])

        st.write("### 🧂 主な材料")
        st.write(result["ingredients"])

        st.write("### ⏰ 調理時間")
        st.write(f"約{result['time']}分")

        st.write("### 🎶 おすすめの気分")
        st.write(result["mood"])

        st.write("### ⭐ 難易度")
        st.write(result["difficulty"])

        # URL（安全に表示）
        if "url" in result:
            st.link_button("🍳 参考ホームページボタン", result["url"])

        st.image(result["image"], caption=recommendation, width=400)

    else:
        st.warning("おすすめが見つかりませんでした。")

st.markdown("---")
st.success("🌏 世界の朝食文化を楽しもう！")
