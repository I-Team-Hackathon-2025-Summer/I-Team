
const openBtns = document.querySelectorAll(".openModal");
// querySelectorAllで、class=openModalのボタンをすべて取得して
// openBtns という配列のようなリストに入れる
const modal = document.getElementById("modalDelete");
const deleteBtn = document.getElementById("delete");
const cancelBtn = document.getElementById("cancel");

// モーダルを開く
openBtns.forEach((btn) => {
  // forEachはリストから1つずつ取り出して実行するforループのような処理
  btn.addEventListener("click", () => {
    modal.style.display = "flex"; // モーダルを表示する
  });
});


// 削除ボタンをクリックしたとき
deleteBtn.addEventListener('click', () => {
  //ここに削除処理を記述する
    alert("メッセージを削除しました");
  modal.style.display = "none"; // モーダルを閉じる
});

// キャンセルボタンをクリックしたとき
cancelBtn.addEventListener('click', () => {
  modal.style.display = "none"; // モーダルを閉じる
});

// モーダル外（背景）をクリックしたら閉じる
addEventListener('click', (e) => {
  // (e)は "click"というイベントに関する情報（イベントオブジェクト）をaddEventListenerから渡される
  // どこをクリックしたか、要素はなにか、などの情報が(e)に入る
    if (e.target === modal) {
      // クリックされた要素(e.target)が modal（半透明部分） なら閉じる
      modal.style.display = "none";
    }
});
