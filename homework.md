# 🎒 Uyga vazifa: Media Library Bot

Telegram bot yarating. Foydalanuvchi yuborgan **rasm, video va audiolarni `file_id` orqali saqlab**, keyinchalik komandalar yordamida qayta olishi kerak.

### 📦 `userdata`

Barcha ma'lumotlarni hozircha Python `dict`da saqlang:

```python
userdata = {}
```

Har bir user `user_id` orqali alohida saqlansin.

Masalan:

```text
userdata[user_id] = {
    "photos": [],
    "videos": [],
    "audios": []
}
```

### Bot funksiyalari:

* 🖼 Rasm yuborilsa → `file_id`ni saqlash
* 🎥 Video yuborilsa → `file_id`ni saqlash
* 🎵 Audio yuborilsa → `file_id`ni saqlash

### Komandalar:

`/photos` → user yuborgan barcha rasmlarni qaytaradi.

`/videos` → user yuborgan barcha videolarni qaytaradi.

`/audios` → user yuborgan barcha audiolarni qaytaradi.

`/stats` → nechta rasm, video va audio saqlanganini ko‘rsatadi. ⭐ Bonus

### Muhim:

❌ Database ishlatmang
❌ `download_to_drive()` ishlatmang

Faqat **`user_id + dict + list + file_id`** yordamida bajaring.

**Maqsad:** Telegram → `file_id` → `userdata` → `file_id` → Telegram.
