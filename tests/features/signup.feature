Feature: HOTEL_PLANISPHEREログイン

  Scenario Outline: Signup
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
    Then ページの見出しが「マイページ」であることを確認する
    And メールアドレスが「<email>」であることを確認する
    And 氏名が「<name>」であることを確認する
    And 会員ランクが「<rank>」であることを確認する
    And 住所が「<address>」であることを確認する
    And 電話番号が「<phone>」であることを確認する
    And 性別が「<gender>」であることを確認する
    And 生年月日が「<validate_birthday>」であることを確認する
    And お知らせが「<check_flag>」であることを確認する


    Examples:
    | name | email | password | password_confirm | rank | address | phone | gender | birthday | validate_birthday | check_flag |  
    | 森本雄介 | yusuke@example.com | pazzw0rd | pazzw0rd | プレミアム会員 | 豊島区 | 04099999999 | 男性 | 1999-01-01 | 1999年1月1日 | 受け取る |  
    | 佐々木明 | msasaki@example.com | pass0825 | pass0825 | プレミアム会員 | 千葉県千葉市 | 05099999999 | 女性 | 1995-07-21 | 1995年7月21日 | 受け取らない |  
    | 松田耕作 | komatsu223@example.com | pazzw0rd | pazzw0rd | 一般会員 | 埼玉県寄居町 | 06099999999 | 男性 | 1995-09-13 | 1995年9月13日 | 受け取る |  
    | 高田真美 | mamidesu@example.com | mtaka01234 | mtaka01234 | 一般会員 | 神奈川県川崎市 | 03099999999 | 女性 | 1994-03-22 | 1994年3月22日 | 受け取らない |  