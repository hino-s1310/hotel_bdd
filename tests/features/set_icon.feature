Feature: 会員登録を行い、アイコンの設定を行う

  Scenario Outline: set_icon
    Given HOTELPLANISPHEREのホームページにアクセスする
    When 会員登録リンクを押下する
    And ページの見出しが「会員登録」であることを確認する
    And メールアドレス欄に「<email>」を入力する
    And パスワード欄に「<password>」を入力する
    And パスワード確認欄に「<password_confirm>」を入力する
    And 氏名欄に「<name>」を入力する
    And 会員ランクラジオボタンで「<rank>」を選択する
    And 住所欄に「<address>」を入力する
    And 電話番号欄に「<phone>」を入力する
    And 性別リストダウンで「<gender>」を選択する
    And 生年月日欄に「<birthday>」を入力する
    And お知らせを<check_flag>
    And 登録ボタンを押下する
    And ページの見出しが「マイページ」であることを確認する
    And アイコン設定ボタンを押下する
    And ページの見出しが「アイコン設定」であることを確認する
    And 「<img_path>」をアップロードする
    And 拡大・縮小を「<slider_value>」に設定する
    And 枠線の色を「<RGB_value>」に設定する
    And 確定ボタンを押下する
    Then ページの見出しが「マイページ」であることを確認する
    And アイコンが存在することを確認する
    And アイコンの枠の色が「<validate_RGB_value>」であることを確認する
    And アイコンのスクリーンショットを撮影し、「<screenshot_path>」に格納する

    Examples:
    | name | email | password | password_confirm | rank | address | phone | gender | birthday | validate_birthday | check_flag | img_path | slider_value | RGB_value | validate_RGB_value | screenshot_path |
    | 森本雄介 | yusuke@example.com | pazzw0rd | pazzw0rd | プレミアム会員 | 豊島区 | 04099999999 | 男性 | 1999-01-01 | 1999年1月1日 | 受け取る | tests/imgs/icon_img.jpg | 50 | #000000 | rgb(0, 0, 0) | screenshots/icon/ |