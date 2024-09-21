# 記事名の取得
## XPath
```//h2/a/text()```
## CSS
```h2 > a::text```

# URL取得
## XPath
```//h2/a/@href```
## CSS
```h2 > a::attr(href)```

# Scrapy shell
``` scrapy shell https://qiita.com```
or 

```scrapy shell
fetch("https://qiita.com")
```


# Get
## xpath
```:python
In [21]: title = response.xpath('//h2/a/text()')

In [22]: title
Out[22]: 
[<Selector xpath='//h2/a/text()' data='HTTPSは安全なのか？'>,
 <Selector xpath='//h2/a/text()' data='原因不明だったRDS負荷のスパイクを改善できた話'>,
 <Selector xpath='//h2/a/text()' data='【2024】Go言語おすすめライブラリ15選'>,
 <Selector xpath='//h2/a/text()' data='ハッカーのおもちゃとしてのNostrのススメ'>,
 <Selector xpath='//h2/a/text()' data='生成AI で思い通りのサイトを出力しよう'>,
 <Selector xpath='//h2/a/text()' data='async/await 比較（C#, JavaScript, Python）'>,
 <Selector xpath='//h2/a/text()' data='Step Functionsの勉強がてら、Bedrockとかを使ってret...'>,
 <Selector xpath='//h2/a/text()' data='JavaScript の Segments の使い所を考える'>,
 <Selector xpath='//h2/a/text()' data='Qiita アップデートのお知らせ - 2023年 12月'>,
 <Selector xpath='//h2/a/text()' data='能登半島地震の航空写真の一枚画像を作る方法'>,
 <Selector xpath='//h2/a/text()' data='Lee et al 2020 "Learning Quadrupedal ...'>,
 <Selector xpath='//h2/a/text()' data='能登半島地震の建物被害分布を自動で出す方法'>,
 <Selector xpath='//h2/a/text()' data='【VBA】ExcelVBAで実現するエビデンスツール'>,
 <Selector xpath='//h2/a/text()' data='React書き初め～useTransitionでとりあえずリストの重い再レ...'>,
 <Selector xpath='//h2/a/text()' data='1000→2000時間勉強して学んだこと/身につけた習慣'>,
 <Selector xpath='//h2/a/text()' data='Spring Securityでログイン後のURLに付くcontinueク...'>,
 <Selector xpath='//h2/a/text()' data='【バックエンド】駆け出しエンジニアが目指すジュニアレベルのエンジニアとは【...'>,
 <Selector xpath='//h2/a/text()' data='LevyTransferTransactionを作ってみる'>,
 <Selector xpath='//h2/a/text()' data='iOS16からのQRコードの読み取り'>,
 <Selector xpath='//h2/a/text()' data='WinPythonを、WiX4で配置する。'>,
 <Selector xpath='//h2/a/text()' data='【Android】 CircleCI + Roborazzi + Show...'>,
 <Selector xpath='//h2/a/text()' data='モジュール結合度をrubyで理解する'>,
 <Selector xpath='//h2/a/text()' data='新米パパが子育てしながら情報処理安全確保支援士試験に合格した話'>,
 <Selector xpath='//h2/a/text()' data='Linuxでの調査時に高頻度で使用してきたコマンドまとめ'>,
 <Selector xpath='//h2/a/text()' data='【2024年版】フロントエンドに求められるミドルレベルのエンジニアと達成す...'>,
 <Selector xpath='//h2/a/text()' data='[Entra ID] パスワードベースのSSOを検証する'>,
 <Selector xpath='//h2/a/text()' data='WindowsAPI のデータ型（LPCSTR と LPCWSTR）の違い...'>,
 <Selector xpath='//h2/a/text()' data='Quine を書いてみた'>,
 <Selector xpath='//h2/a/text()' data='GetGPTで関西弁変換アプリを作ろう'>,
 <Selector xpath='//h2/a/text()' data="会社のリポジトリにプッシュしたとき「Couldn't connect to...">]

In [23]: title = response.xpath('//h2/a/text()').get()

In [24]: title
Out[24]: 'HTTPSは安全なのか？'

In [25]: title = response.xpath('//h2/a/text()').getall()

In [26]: title
Out[26]: 
['HTTPSは安全なのか？',
 '原因不明だったRDS負荷のスパイクを改善できた話',
 '【2024】Go言語おすすめライブラリ15選',
 'ハッカーのおもちゃとしてのNostrのススメ',
 '生成AI で思い通りのサイトを出力しよう',
 'async/await 比較（C#, JavaScript, Python）',
 'Step Functionsの勉強がてら、Bedrockとかを使ってreturn falseな上司とLINEしてみる。',
 'JavaScript の Segments の使い所を考える',
 'Qiita アップデートのお知らせ - 2023年 12月',
 '能登半島地震の航空写真の一枚画像を作る方法',
 'Lee et al 2020 "Learning Quadrupedal Locomotion over Challenging Terrain"から紐解く四足ロボット強化学習の「秘伝のタレ」',
 '能登半島地震の建物被害分布を自動で出す方法',
 '【VBA】ExcelVBAで実現するエビデンスツール',
 'React書き初め～useTransitionでとりあえずリストの重い再レンダリングをごまかす～',
 '1000→2000時間勉強して学んだこと/身につけた習慣',
 'Spring Securityでログイン後のURLに付くcontinueクエリパラメータの正体',
 '【バックエンド】駆け出しエンジニアが目指すジュニアレベルのエンジニアとは【2024年版】',
 'LevyTransferTransactionを作ってみる',
 'iOS16からのQRコードの読み取り',
 'WinPythonを、WiX4で配置する。',
 '【Android】 CircleCI + Roborazzi + Showkase で VRT 試しました',
 'モジュール結合度をrubyで理解する',
 '新米パパが子育てしながら情報処理安全確保支援士試験に合格した話',
 'Linuxでの調査時に高頻度で使用してきたコマンドまとめ',
 '【2024年版】フロントエンドに求められるミドルレベルのエンジニアと達成する為にすべきこととは',
 '[Entra ID] パスワードベースのSSOを検証する',
 'WindowsAPI のデータ型（LPCSTR と LPCWSTR）の違いについて',
 'Quine を書いてみた',
 'GetGPTで関西弁変換アプリを作ろう',
 "会社のリポジトリにプッシュしたとき「Couldn't connect to server」のエラーが出たらまずはVPNを確認しろ"]

In [27]: 
```

## CSS
```
In [28]: title = response.css('h2 > a::text')

In [29]: title
Out[29]: 
[<Selector xpath='descendant-or-self::h2/a/text()' data='HTTPSは安全なのか？'>,
 <Selector xpath='descendant-or-self::h2/a/text()' data='原因不明だったRDS負荷のスパイクを改善できた話'>,
 <Selector xpath='descendant-or-self::h2/a/text()' data='【2024】Go言語おすすめライブラリ15選'>,
 <Selector xpath='descendant-or-self::h2/a/text()' data='ハッカーのおもちゃとしてのNostrのススメ'>,
 <Selector xpath='descendant-or-self::h2/a/text()' data='生成AI で思い通りのサイトを出力しよう'>,
 <Selector xpath='descendant-or-self::h2/a/text()' data='async/await 比較（C#, JavaScript, Python）'>,
 <Selector xpath='descendant-or-self::h2/a/text()' data='Step Functionsの勉強がてら、Bedrockとかを使ってret...'>,
 <Selector xpath='descendant-or-self::h2/a/text()' data='JavaScript の Segments の使い所を考える'>,
 <Selector xpath='descendant-or-self::h2/a/text()' data='Qiita アップデートのお知らせ - 2023年 12月'>,
 <Selector xpath='descendant-or-self::h2/a/text()' data='能登半島地震の航空写真の一枚画像を作る方法'>,
 <Selector xpath='descendant-or-self::h2/a/text()' data='Lee et al 2020 "Learning Quadrupedal ...'>,
 <Selector xpath='descendant-or-self::h2/a/text()' data='能登半島地震の建物被害分布を自動で出す方法'>,
 <Selector xpath='descendant-or-self::h2/a/text()' data='【VBA】ExcelVBAで実現するエビデンスツール'>,
 <Selector xpath='descendant-or-self::h2/a/text()' data='React書き初め～useTransitionでとりあえずリストの重い再レ...'>,
 <Selector xpath='descendant-or-self::h2/a/text()' data='1000→2000時間勉強して学んだこと/身につけた習慣'>,
 <Selector xpath='descendant-or-self::h2/a/text()' data='Spring Securityでログイン後のURLに付くcontinueク...'>,
 <Selector xpath='descendant-or-self::h2/a/text()' data='【バックエンド】駆け出しエンジニアが目指すジュニアレベルのエンジニアとは【...'>,
 <Selector xpath='descendant-or-self::h2/a/text()' data='LevyTransferTransactionを作ってみる'>,
 <Selector xpath='descendant-or-self::h2/a/text()' data='iOS16からのQRコードの読み取り'>,
 <Selector xpath='descendant-or-self::h2/a/text()' data='WinPythonを、WiX4で配置する。'>,
 <Selector xpath='descendant-or-self::h2/a/text()' data='【Android】 CircleCI + Roborazzi + Show...'>,
 <Selector xpath='descendant-or-self::h2/a/text()' data='モジュール結合度をrubyで理解する'>,
 <Selector xpath='descendant-or-self::h2/a/text()' data='新米パパが子育てしながら情報処理安全確保支援士試験に合格した話'>,
 <Selector xpath='descendant-or-self::h2/a/text()' data='Linuxでの調査時に高頻度で使用してきたコマンドまとめ'>,
 <Selector xpath='descendant-or-self::h2/a/text()' data='【2024年版】フロントエンドに求められるミドルレベルのエンジニアと達成す...'>,
 <Selector xpath='descendant-or-self::h2/a/text()' data='[Entra ID] パスワードベースのSSOを検証する'>,
 <Selector xpath='descendant-or-self::h2/a/text()' data='WindowsAPI のデータ型（LPCSTR と LPCWSTR）の違い...'>,
 <Selector xpath='descendant-or-self::h2/a/text()' data='Quine を書いてみた'>,
 <Selector xpath='descendant-or-self::h2/a/text()' data='GetGPTで関西弁変換アプリを作ろう'>,
 <Selector xpath='descendant-or-self::h2/a/text()' data="会社のリポジトリにプッシュしたとき「Couldn't connect to...">]

In [30]: title = response.css('h2 > a::text').get()

In [31]: title
Out[31]: 'HTTPSは安全なのか？'

In [32]: title = response.css('h2 > a::text').getall()

In [33]: title
Out[33]: 
['HTTPSは安全なのか？',
 '原因不明だったRDS負荷のスパイクを改善できた話',
 '【2024】Go言語おすすめライブラリ15選',
 'ハッカーのおもちゃとしてのNostrのススメ',
 '生成AI で思い通りのサイトを出力しよう',
 'async/await 比較（C#, JavaScript, Python）',
 'Step Functionsの勉強がてら、Bedrockとかを使ってreturn falseな上司とLINEしてみる。',
 'JavaScript の Segments の使い所を考える',
 'Qiita アップデートのお知らせ - 2023年 12月',
 '能登半島地震の航空写真の一枚画像を作る方法',
 'Lee et al 2020 "Learning Quadrupedal Locomotion over Challenging Terrain"から紐解く四足ロボット強化学習の「秘伝のタレ」',
 '能登半島地震の建物被害分布を自動で出す方法',
 '【VBA】ExcelVBAで実現するエビデンスツール',
 'React書き初め～useTransitionでとりあえずリストの重い再レンダリングをごまかす～',
 '1000→2000時間勉強して学んだこと/身につけた習慣',
 'Spring Securityでログイン後のURLに付くcontinueクエリパラメータの正体',
 '【バックエンド】駆け出しエンジニアが目指すジュニアレベルのエンジニアとは【2024年版】',
 'LevyTransferTransactionを作ってみる',
 'iOS16からのQRコードの読み取り',
 'WinPythonを、WiX4で配置する。',
 '【Android】 CircleCI + Roborazzi + Showkase で VRT 試しました',
 'モジュール結合度をrubyで理解する',
 '新米パパが子育てしながら情報処理安全確保支援士試験に合格した話',
 'Linuxでの調査時に高頻度で使用してきたコマンドまとめ',
 '【2024年版】フロントエンドに求められるミドルレベルのエンジニアと達成する為にすべきこととは',
 '[Entra ID] パスワードベースのSSOを検証する',
 'WindowsAPI のデータ型（LPCSTR と LPCWSTR）の違いについて',
 'Quine を書いてみた',
 'GetGPTで関西弁変換アプリを作ろう',
 "会社のリポジトリにプッシュしたとき「Couldn't connect to server」のエラーが出たらまずはVPNを確認しろ"]

In [34]: 
```


# URL
## xpath
```In [40]: url = response.xpath('//h2/a/@href').getall()

In [41]: url
Out[41]: 
['https://qiita.com/uturned0/items/1b1fd8f35d266a810344',
 'https://qiita.com/udonn/items/ca4002aa242c857d4916',
 'https://qiita.com/twrcd1227/items/1a05ffa459f45b2968e4',
 'https://qiita.com/gpsnmeajp/items/2f95d4adf188276146d8',
 'https://qiita.com/faunsu/items/a2d847afa87a5a0da5af',
 'https://qiita.com/shii4c/items/e89f4d4d31f09602df32',
 'https://qiita.com/hoopjpt/items/abc066afb77552390876',
 'https://qiita.com/kaibadash@github/items/5f69d6f86742d698c560',
 'https://qiita.com/Qiita/items/be37cc6d4b06c3027a03',
 'https://qiita.com/mkunu/items/61ec11634b9b4ebcc7a0',
 'https://qiita.com/yunifuchioka/items/0724d7560715968c033c',
 'https://qiita.com/mkunu/items/b7b33deff174c7127ab4',
 'https://qiita.com/Kit-i/items/e4c732c9e389dc6a860b',
 'https://qiita.com/honey32/items/9b116981f7d7124eeb1e',
 'https://qiita.com/KazukiITWeb1/items/00a97b0c8c577b45bd15',
 'https://qiita.com/suke_masa/items/d49e8599b167550e92c4',
 'https://qiita.com/mamimami0709/items/fd6556707e4b924c65ab',
 'https://qiita.com/Toshi_ma/items/d22d7664c0bd04181b6c',
 'https://qiita.com/Ryu0118/items/4ee5c67558476c22318d',
 'https://qiita.com/hiro_t/items/4e05588dc5962fa68030',
 'https://qiita.com/KSND/items/8b285c54f1b56d598740',
 'https://qiita.com/dekamintv/items/ebe9c0f33a2851e6aa9f',
 'https://qiita.com/Mapellion/items/1a706f073dbe18af08f2',
 'https://qiita.com/hirssk/items/aed3fd28462f5ac245cf',
 'https://qiita.com/mamimami0709/items/47e2b8735b1dcab50078',
 'https://qiita.com/akihiro_suto/items/2f7825bfc0cb8a506e4d',
 'https://qiita.com/TamaHack/items/468581755fe33967eb67',
 'https://qiita.com/dorimiamn/items/e94559e5040663095e64',
 'https://qiita.com/Jinnie/items/79f100a8f0cf791a73f9',
 'https://qiita.com/ao_flower/items/a5c34acc1820ebd391af']

In [42]: 
```


