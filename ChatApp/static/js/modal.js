
const openModal = document.getElementById("openModal");
const modal = document.getElementById("modalDelete");
const deleteBtn = document.getElementById("delete");
const cancelBtn = document.getElementById("cancel");

// モーダルを開く
openModal.addEventListener('click', () => {
  modal.showModal();   //モーダルを表示
});

// 削除ボタンをクリックしたとき
deleteBtn.addEventListener('click', () => {
  //削除処理を記述する
    console.log("メッセージを削除しました");
  modal.style.display = "none"; // モーダルを閉じる
});

// キャンセルボタンをクリックしたとき
cancelBtn.addEventListener('click', () => {
  modal.style.display = "none"; // モーダルを閉じる
});

// モーダル外（背景）をクリックしたら閉じる
confirmDialog.addEventListener('click', (e) => {
    if (e.target === confirmDialog) {
        confirmDialog.close();
    }
});
