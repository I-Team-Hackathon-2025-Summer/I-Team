
const openBtns = document.querySelectorAll(".openModal");
const modal = document.getElementById("modalDelete");
const deleteBtn = document.getElementById("delete");
const cancelBtn = document.getElementById("cancel");

// モーダルを開く
openBtns.forEach((btn) => {
  btn.addEventListener("click", () => {
    modal.style.display = "flex"; // モーダルを表示
  });
});


// 削除ボタンをクリックしたとき
deleteBtn.addEventListener('click', () => {
  //削除処理を記述する
    alert("メッセージを削除しました");
  modal.style.display = "none"; // モーダルを閉じる
});

// キャンセルボタンをクリックしたとき
cancelBtn.addEventListener('click', () => {
  modal.style.display = "none"; // モーダルを閉じる
});

// モーダル外（背景）をクリックしたら閉じる
addEventListener('click', (e) => {
    if (e.target === modal) {
      modal.style.display = "none"; // モーダルを閉じる
    }
});
