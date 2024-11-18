Feature: 会員登録を行い、マイページの表示内容を確認する

  Scenario Outline: Signup
    Given HOTELPLANISPHEREのホームページにアクセスする
    When 会員登録リンクを押下する
    And ページの見出しが「会員登録」であることを確認する
    And 会員登録画面で「<signup_input>」を入力する
    And 登録ボタンを押下する
    Then ページの見出しが「マイページ」であることを確認する
    And マイページ画面で各項目が「<signup_validate>」であることを確認する
    And マイページ画面でログアウトボタンを押下する


    Examples:
    | signup_input | signup_validate |
    | {"会員情報_入力":{"name": "森本雄介", "email": "yusuke@example.com", "password":"pazzw0rd", "password_confirm":"pazzw0rd", "rank":"プレミアム会員", "address":"豊島区", "phone":"04099999999", "gender":"男性", "birthday":"1999-01-01","check_flag":"受け取る"}} | {"会員情報_検証":{"name": "森本雄介", "email": "yusuke@example.com", "rank":"プレミアム会員", "address":"豊島区", "phone":"04099999999", "gender":"男性", "birthday":"1999年1月1日","check_flag":"受け取る"}}  |
    | {"会員情報_入力":{"name": "佐々木明", "email": "msasaki@example.com", "password":"pass0825", "password_confirm":"pass0825", "rank":"プレミアム会員", "address":"千葉県千葉市", "phone":"05099999999", "gender":"女性", "birthday":"1995-07-21","check_flag":"受け取らない"}} | {"会員情報_検証":{"name": "佐々木明", "email": "msasaki@example.com", "rank":"プレミアム会員", "address":"千葉県千葉市", "phone":"05099999999", "gender":"女性", "birthday":"1995年7月21日","check_flag":"受け取らない"}} |
    | {"会員情報_入力":{"name": "松田耕作", "email": "komatsu223@example.com", "password":"pazzw0rd", "password_confirm":"pazzw0rd", "rank":"一般会員", "address":"埼玉県寄居町", "phone":"06099999999", "gender":"男性", "birthday":"1995-09-13","check_flag":"受け取る"}} | {"会員情報_検証":{"name": "松田耕作", "email": "komatsu223@example.com", "rank":"一般会員", "address":"埼玉県寄居町", "phone":"06099999999", "gender":"男性", "birthday":"1995年9月13日","check_flag":"受け取る"}}  |
    | {"会員情報_入力":{"name": "高田真美", "email": "mamidesu@example.com", "password":"mtaka01234", "password_confirm":"mtaka01234", "rank":"一般会員", "address":"神奈川県川崎市", "phone":"03099999999", "gender":"女性", "birthday":"1994-03-22","check_flag":"受け取らない"}} | {"会員情報_検証":{"name": "高田真美", "email": "mamidesu@example.com", "rank":"一般会員", "address":"神奈川県川崎市", "phone":"03099999999", "gender":"女性", "birthday":"1994年3月22日","check_flag":"受け取らない"}}  |