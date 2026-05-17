// Mengambil elemen-elemen dari HTML
const imageInput = document.getElementById("imageInput");
const fileNameDisplay = document.getElementById("fileName");
const resultBoxes = document.querySelectorAll(".result-box"); // Mengambil semua kotak hasil

// Mendeteksi saat user memilih file gambar baru
imageInput.addEventListener("change", function () {
  // 1. Mengubah teks "Belum ada file dipilih" menjadi nama file yang baru
  if (this.files && this.files[0]) {
    fileNameDisplay.textContent = this.files[0].name;

    // 2. MENGHILANGKAN FOTO LAMA:
    // Sembunyikan semua kotak hasil (foto nyangkut) yang sebelumnya muncul
    resultBoxes.forEach((box) => {
      box.style.display = "none";
    });
  } else {
    fileNameDisplay.textContent = "Belum ada file dipilih";
  }
});

// Opsional: Untuk menampilkan loading saat tombol submit diklik
const uploadForm = document.getElementById("uploadForm");
const loading = document.getElementById("loading");
const btnSubmit = document.querySelector(".btn");

if (uploadForm) {
  uploadForm.addEventListener("submit", function () {
    if (imageInput.files.length > 0) {
      loading.classList.remove("hidden"); // Munculkan animasi loading
      btnSubmit.style.display = "none"; // Sembunyikan tombol biar gak diklik 2x
    }
  });
}
