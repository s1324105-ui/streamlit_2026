import streamlit as st

st.set_page_config(
    page_title="世界の朝食診断アプリ",
    page_icon="🍳",
    layout="centered"
)

st.title("🍳 世界の朝食診断アプリ")
st.caption("おすすめの世界の朝食を診断します！")

# =========================
# 朝食データ（変更なし）
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
        "mood": "ゆっくり過ごしたい",
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
        "difficulty": "★★☆☆☆",
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
    }
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

# =========================
# 診断
# =========================

if st.button("診断する！"):

    recommendation = None

    for breakfast, data in breakfast_data.items():

        if (
            data["food"] == favorite_food
            and data["mood"] == morning_mood
            and data["time"] <= selected_time
        ):
            recommendation = breakfast
            break

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
