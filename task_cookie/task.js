
// ページが読み込まれたら実行
window.onload = function() {
  
  // オブジェクトと変数の準備
  var count_disp = document.getElementById("count");  
  var count_down_btn = document.getElementById("btn_count");
  var count_value = 3;

  
  // カウントダウンボタンクリック処理
  count_down_btn.onclick = function (){
    count_value -= 1;
    count_disp.innerHTML = count_value;
  };
  
  // 0になったら画像の切り替えとボタンの消去
  if (count_value == 0) {
    document.querySelector('#btn_count').remove();
    document.getElementById("backimg1").classList.add("backimg2");
    document.getElementById("backimg1").classList.remove("backimg");
    
  }

};


  
  
  


