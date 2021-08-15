gejala = [
    "Apakah mengalami demam dengan suhu di atas 38 derajat Celcius?",
    "Oke, apa ada batuk?",
    "Apa ada sesak atau kesulitan untuk bernapas?",
    "Apakah mengalami gangguan ketika mencium bau atau tidak dapat mencium bau sama sekali?"
]

suspection = [
    "Baik, apa terdapat riwayat kontak (misalnya: berjabat tangan, mengobrol lama, berada dalam satu ruangan) dengan orang yang sudah dinyatakan positif terinfeksi virus Corona dalam 14 hari terakhir?",
    "Lalu, apakah ada kontak (misalnya: berjabat tangan, mengobrol lama, berada dalam satu ruangan) dengan orang yang memiliki gejala flu, yaitu demam, batuk, dan pilek, atau dengan orang yang diduga terinfeksi virus Corona dalam 14 hari terakhir?",
    """Apakah Anda memiliki salah satu kondisi di bawah ini:
- Berusia di atas 60 tahun
- Memiliki riwayat penyakit jantung, penyakit paru-paru, atau penyakit kencing manis
- Sedang menjalani pengobatan kanker
"""
]

answer_high = [
    "Baik, bila mengalami sesak napas dan memiliki riwayat kontak dengan orang yang sudah positif terinfeksi virus Corona, maka eaat ini memiliki kemungkinan yang tinggi tertular virus Corona.",
    "Virus Corona merupakan virus yang menyerang saluran pernapasan. Gejala yang timbul bila terinfeksi virus ini bisa ringan sampai berat. Gejala yang ringan umumnya seperti gejala flu, yakni demam, batuk, pilek, dan sakit tenggorokan. Sebagian kecil kasus bisa berkembang menjadi berat dan menyebabkan infeksi paru-paru atau pneumonia. Meski begitu, infeksi virus ini juga bisa tidak menimbulkan gejala apa-apa.",
    """Saat ini disarankan untuk melakukan hal-hal berikut:

- Hubungi Hotline Center Corona di nomor 119 ext. 9, dan ikuti instruksi yang diberikan.

- Jangan tinggalkan rumah kecuali untuk berobat, dan pastikan berada di ruangan terpisah dari anggota keluarga, kerabat, atau orang lain untuk mencegah penularan.

- Gunakan masker selama masih sakit.

- Longgarkan pakaian dan carilah posisi yang nyaman saat beristirahat, misalnya berbaring dengan posisi bantal yang lebih tinggi untuk mengurangi sesak.

- Ikuti etika batuk/bersin yang benar dengan cara menutup mulut dan hidung dengan tisu atau lengan bagian dalam, lalu membuang tisu yang telah digunakan ke tempat sampah.

- Cuci tangan dengan sabun dan air mengalir selama minimal 20 detik. Gunakan hand sanitizer yang mengandung alkohol minimal 60%, jika tidak tersedia air dan sabun.

- Untuk keluarga atau kerabat yang berada di sekitar, pastikan mereka rajin mencuci tangan dan membatasi kontak dengan orang yang sakit.

""",
    "Di rumah sakit, dokter akan melakukan pemeriksaan fisik dan pemeriksaan tambahan, seperti pemeriksaan darah, pemeriksaan lendir tenggorokan, dan foto Rontgen paru-paru bila diperlukan, untuk memastikan penyebab gejala yang dialami dan menentukan pengobatan selanjutnya.",
    "Bila diduga atau terbukti terinfeksi virus Corona, maka akan diisolasi atau dikarantina untuk menghindari penularan ke orang lain. Pengobatan yang diberikan akan difokuskan untuk meningkatkan daya tahan tubuh dan meringankan gejala yang dirasakan."
]

answer_mid = [
    "Baik, karena saat ini mengalami demam serta pernah kontak dengan orang yang memiliki gejala flu atau diduga terkena virus Corona, maka risiko tertular virus Corona termasuk kategori sedang.",
    "Virus Corona merupakan virus yang menyerang saluran pernapasan. Gejala yang timbul bila terinfeksi virus ini bisa ringan sampai berat. Gejala yang ringan umumnya seperti gejala flu, yakni demam, batuk, pilek, dan sakit tenggorokan. Sebagian kecil kasus bisa berkembang menjadi berat dan menyebabkan infeksi paru-paru atau pneumonia. Meski begitu, infeksi virus ini juga bisa tidak menimbulkan gejala apa-apa.",
    "Saat ini disarankan untuk tetap berada di rumah selama 14 hari, terhitung sejak kontak dengan orang yang memiliki gejala flu atau diduga terinfeksi virus Corona.",
    """Dan juga disarankan untuk melakukan hal-hal berikut:

- Beristirahatlah di rumah, dan pastikan berada di ruangan terpisah dari anggota keluarga, kerabat, atau orang lain untuk mencegah penularan.

- Konsumsi paracetamol untuk meredakan demam.

- Gunakan masker selama masih sakit, terutama ketika berinteraksi dengan orang lain.

- Saat batuk atau bersin, tutup hidung dan mulut dengan tisu atau lengan bagian dalam, lalu segera buang tisu ke tempat sampah.

- Cuci tangan dengan sabun dan air mengalir selama minimal 20 detik, atau dengan hand sanitizer yang mengandung alkohol minimal 60%, terutama sebelum dan sesudah bersin, batuk, atau makan, juga sehabis dari toilet.

- Beri tahu keluarga atau kerabat yang merawat untuk memakai masker dan rajin mencuci tangan.

""",
    "Bila timbul gejala sesak napas yang dirasakan bertambah berat, maka perlu segera dibawa ke IGD. Namun, pastikan keluarga atau kerabat sudah menghubungi IGD tersebut sebelumnya, agar petugas medis sudah melakukan upaya pencegahan untuk menghindari penularan.",
    "Dokter akan melakukan pemeriksaan fisik dan pemeriksaan tambahan, seperti pemeriksaan darah, pemeriksaan lendir tenggorokan, dan foto Rontgen paru-paru bila diperlukan, untuk menentukan pengobatan selanjutnya.",
    "Bila diduga atau terbukti adanya virus Corona, akan diisolasi atau dikarantina untuk menghindari penularan ke orang lain dan ditangani dengan obat-obatan untuk meningkatkan daya tahan tubuh dan meringankan gejala yang dirasakan."
]

answer_low = [
    "Baik, bila saat ini terdapat gangguan ketika mencium bau atau tidak dapat mencium bau sama sekali namun tidak memiliki faktor risiko penularan virus Corona, seperti kontak dengan orang yang memiliki gejala flu, diduga terinfeksi virus Corona, atau bahkan sudah positif terinfeksi virus Corona, maka risiko tertular virus Corona termasuk kategori rendah.",
    "Virus Corona merupakan virus yang menyerang saluran pernapasan. Memang gangguan penciuman pada hidung dan pengecap rasa pada mulut sering dikaitkan dengan infeksi virus Corona. Namun hal ini bukan tanda pasti tertular virus Corona ya. Banyak hal yang dapat menimbulkan gangguan serupa misalnya adanya alergi, sinusitis, dan lainnya.",
    """Saat ini disarankan untuk melakukan hal-hal berikut:

- Beristirahatlah di rumah, dan pastikan berada di ruangan terpisah dari anggota keluarga, kerabat, atau orang lain, untuk mencegah penularan.

- Gunakan masker saat berinteraksi dengan orang lain.

- Saat batuk atau bersin, tutup mulut dan hidung dengan tisu atau lengan bagian dalam, lalu segera buang tisu yang sudah digunakan ke tempat sampah.

- Cuci tangan dengan sabun dan air mengalir selama minimal 20 detik, atau dengan hand sanitizer yang mengandung alkohol setidaknya 60%, terutama sebelum dan sesudah bersin, batuk, atau makan, juga sehabis dari toilet.

- Usahakan untuk makan dan minum yang cukup agar tidak kekurangan cairan, tapi berhati-hatilah agar tidak tersedak.

Bila timbul gejala sesak napas yang dirasakan bertambah berat, maka perlu segera dibawa ke IGD. Namun, pastikan keluarga atau kerabat sudah menghubungi IGD tersebut sebelumnya, agar petugas medis sudah melakukan upaya pencegahan untuk menghindari penularan."""
]

answer_very_low = [
    "Baik, bila saat ini tidak mengalami demam, batuk, sesak napas ataupun kesulitan mencium bau, serta tidak memiliki faktor risiko terinfeksi virus Corona, seperti kontak dengan orang yang positif atau diduga terinfeksi virus Corona, maka risiko tertular virus Corona termasuk kategori rendah."
]