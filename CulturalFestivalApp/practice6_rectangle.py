from PIL import Image, ImageDraw

# ベース画像を読み込み（RGBAモードに変換）
base_image = Image.open("images/kousya.jpg").convert("RGBA")

# オーバーレイ画像を作成（完全に透明なレイヤー）
overlay = Image.new("RGBA", base_image.size, (255, 0, 0, 0))
# →赤色だけど完全に透明なピクセルで埋められた画像を生成

# 描画オブジェクトを作成
draw = ImageDraw.Draw(overlay)

# 描画したい矩形の座標（左上と右下のピクセル位置）
box = (865, 600, 945, 670)  # (左, 上, 右, 下)
# → 矩形の座標です。左上 (865, 600) から右下 (945, 670) まで。

# 矩形を描画（透明な赤色 fill=(R, G, B, A)）
draw.rectangle(box, fill=(255, 0, 0, 100))
# → 赤色で透明度100の塗りつぶし。最大透明度255なので、100はやや透けます。

# オーバーレイと元画像を合成
combined = Image.alpha_composite(base_image, overlay)

# 結果を表示（または保存）
combined.show()
# combined.save("output.png")


# 1.overlay 全体は最初 完全に透明
# 2.必要な箇所だけ draw.rectangle(..., fill=(255, 0, 0, 100)) で半透明の赤に塗る
# 3.最後に base_image に重ねることで、「一部だけ赤く透明なマークが乗った画像」が完成する