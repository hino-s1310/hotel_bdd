Feature: 会員登録を行い、アイコンの設定を行う

  Scenario Outline: set_icon
    Given HOTELPLANISPHEREのホームページにアクセスする
    When 会員登録リンクを押下する
    And ページの見出しが「会員登録」であることを確認する
    And 会員登録画面で「<signup_input>」を入力する
    And 登録ボタンを押下する
    And ページの見出しが「マイページ」であることを確認する
    And アイコン設定ボタンを押下する
    And ページの見出しが「アイコン設定」であることを確認する
    And アイコン画面で「<icon_input>」を入力する
    And 確定ボタンを押下する
    Then ページの見出しが「マイページ」であることを確認する
    And アイコンが存在することを確認する
    And アイコンの枠の色が「<validate_RGB_value>」であることを確認する
    And アイコンのスクリーンショットを撮影し、「<screenshot_path>」に格納する
    And マイページをログアウトする

    Examples:
    | signup_input | icon_input | validate_RGB_value | screenshot_path |
    | {"会員情報_入力":{"name": "森本雄介", "email": "yusuke@example.com", "password":"pazzw0rd", "password_confirm":"pazzw0rd", "rank":"プレミアム会員", "address":"豊島区", "phone":"04099999999", "gender":"男性", "birthday":"1999-01-01","check_flag":"受け取る"}} | { "アイコン情報_入力" :{"img_path":"tests/imgs/icon_img.jpg","slider_value":"50", "RGB_value": "#000000"}} | rgb(0, 0, 0) | screenshots/icon/ |