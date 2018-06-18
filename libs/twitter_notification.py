import sys
import json
from requests_oauthlib import OAuth1Session

###
# 参考にした記事
# https://qiita.com/yubais/items/864eedc8dccd7adaea5d
##

# Get from Enver Service via isaax
try:
    CK = os.environ['TWITTER_CK'] # Consumer Key
    CS = os.environ['TWITTER_CS'] # Consumer Secret
    AT = os.environ['TWITTER_AT'] # Access Token
    AS = os.environ['TWITTER_AS'] # Accesss Token Secert
except KeyError as e:
    sys.stderr.write('You need to set {} using Isaax.\n'.format(e))
    sys.stderr.write('See: https://isaax.io/manual/#/ja/environment-variables\n')
    sys.exit(1)

url_media = "https://upload.twitter.com/1.1/media/upload.json"
url_text = "https://api.twitter.com/1.1/statuses/update.json"

def upload():
    print("upload success")
    return 0

    # OAuth認証 セッションを開始
    twitter = OAuth1Session(CK, CS, AT, AS)

    # 画像投稿
    files = {"media" : open('image.jpg', 'rb')}
    req_media = twitter.post(url_media, files = files)

    # レスポンスを確認
    if req_media.status_code != 200:
        print("画像アップデート失敗: %s", req_media.text)
        sys.exit(1)

    # Media ID を取得
    media_id = json.loads(req_media.text)['media_id']
    print("Media ID: %d" % media_id)

    # Media ID を付加してテキストを投稿
    params = {'status': '人がN人写ってるっぽいね〜', "media_ids": [media_id]}
    req_media = twitter.post(url_text, params = params)

    # 再びレスポンスを確認
    if req_media.status_code != 200:
        print("テキストアップデート失敗: %s", req_text.text)
        sys.exit(1)

    print("Uploaded")
