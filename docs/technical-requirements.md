# 1. Loyiha maqsadi
### Loyiha maqsadi - o'quv markazidagi ichki tizimni, ya'ni, o'quvchilar qabuli, davomati, to'lov tizimi va hokazolarni avtomatizatsiya qilish sistemasini ishlab chiqish. Yangi kelgan o'quvchilarga yoki begona shaxslarga markazning muvaffaqiyatli bitiruvchilari erishgan natijalarini ko'rsatib berish va bu orqali yangi o'quvchilarda o'qishga bo'lgan intilishni kuchaytirish.

# 2. Loyiha tavsifi

### Sistema quyidagi asosiy bloklardan tashkil topadi:
1. O'quv markaz haqida umumiy ma'lumotlar, o'quvchilar yutuqlari.
2. Ro'yhatdan o'tish, autentifikatsiya, shaxsiy kabinet.
3. O'quvchilarni qabul qilish va guruhga biriktirish, davomat, tolov statusi, darslar jadvali,
4. Yangiliklar, xabarnomalar.


### Loyihada asosiy funksional uchun mobil ilova, administratsiya ishlari uchun web-sayt (adminka) ishlab chiqiladi. 

# 3. Foydalanuvchi turlari

1. Mehmonlar (ro'yhatdan o'tmagan barcha foydalanuvchilar).
2. O'quvchilar.
3. O'qituvchilar.
4. Admin.
5. Superadmin.

# 4. Ro'yhatdan o'tish, autentifikatsiya, foydalanuvchi imkoniyatlari

### Sistemaga kirish telefon raqami va parol orqali amalga oshiriladi.


```
1. O'quvchilar mobil ilovaning ro'yhatdan o'tish sahifasiga kirishadi va quyidagi ma'lumotlarni kiritishadi:

    * ism
    * familiya
    * otasining ismi
    * tug'ilgan sanasi
    * telefon raqami
    * rasmi
    * parol

    Ushbu ma'lumotlarni kiritib tasdiqlash tugmasini bosgandan so'ng, bu o'quvchi ma'lumotlari administrator (adminka)ga kelib tushadi. Admin o'quvchi ma'lumotlarini tekshirib tasdiqlash tugmasini bosgandan so'ng o'quvchi sistemaga kirish imkoniga ega bo'ladi. 
```

```
O'quvchi imkoniyatlari:
    1) Mehmonlar (ro'yhatdan o'tmagan foydalanuvchilar)ga ko'rinuvchi barcha ma'lumotlar -- ko'rish. 
    2) Shaxsiy kabinet -- ko'rish, o'zgartirish. 
    3) O'zi qo'shilgan guruhlar ro'yhati -- ko'rish.
    Har bir guruhdagi guruh ma'lumotlari (guruh nomi, fan nomi, o'qituvchi fio, guruhdoshlari ro'yhati) -- ko'rish. 
    Guruhdoshlari ma'lumotlari (ism, familiyasi, yoshi, rasmi, guruh nomi) -- ko'rish. 
    4) Darslar jadvali -- ko'rish. 
    5) Darslar ro'yhati va o'z davomati -- ko'rish. 
    6) Yangiliklar -- ko'rish.
    7) To'lov tarixi -- ko'rish.
```

```
2. O'qituvchilarni ro'yhatdan o'tishi administrator tomonidan amalga oshiriladi. Bunda admin web-saytning "o'qituvchi qo'shish" bo'limiga o'tadi va o'qituvchining ma'lumotlarini kiritadi:

    * ism
    * familiya
    * otasining ismi
    * tug'ilgan sanasi
    * yashash manzili
    * asosiy telefon raqami
    * qo'shimcha telefon raqami (zaruriyat bo'lsa)
    * rasmi
    * fan nomi
    * bank hisob raqami
    * parol
  
    Admin ushbu ma'lumotlarni kiritib tasdiqlagandan  so'ng o'qituvchi sistemaga kirish imkoniga ega bo'ladi.

O'qituvchi imkoniyatlari: 
    1) Mehmonlarga ko'rinuvchi barcha ma'lumotlar -- ko'rish.
    2) Shaxsiy kabinet -- ko'rish, o'zgartirish.
    3) O'ziga tegishli guruhlar ro'yhati -- ko'rish. 
    Har bir guruh ma'lumotlari (guruh nomi, o'quvchilar ro'yhati) -- ko'rish. 
    Guruhdagi har bir o'quvchining ma'lumotlari (ism, familiya, yosh, rasm, to'lov tarixi, davomat tarixi) -- ko'rish. 
    Guruhga yangi o'quvchi qo'shish ???
    4) O'ziga tegishli darslar ro'yhati -- ko'rish. 
    Har bir dars ma'lumotlari (fan nomi, guruh nomi, dars sanasi, davomat) -- ko'rish, qo'shish, o'zgartirish.
    5) Yangiliklar -- ko'rish.
```

```
3. Adminni ro'yhatdan o'tkazish yoki o'zgartirish web-sayt orqali superadmin tomonidan amalga oshiriladi. Bunda superadmin web-saytning administratsiya boshqaruvi bo'limiga kirib adminning ma'lumotlarini kiritadi. Admin quyidagi ma'lumotlarga ega bo'ladi.

    * ism
    * familiya
    * otasining ismi
    * tug'ilgan sanasi
    * asosiy telefon raqami
    * qo'shimcha telefon raqami (zaruriyat bo'lsa)
    * rasmi
    * bank hisob raqami
    * parol
```

```
Admin imkoniyatlari:
    1) Shaxsiy kabinet -- ko'rish, o'zgartirish.
    2) O'quvchilar ro'yhati -- ko'rish, o'zgartirish (faqat yangi o'quvchini tasdiqlash).
    Har bir o'quvchi haqida ma'lumot (FIO, yoshi, telefon, rasmi, guruhlar nomi, to'lov tarixi, davomat tarixi) -- ko'rish, o'zgartirish (faqat to'lovni).
    3) Yangiliklar ro'yhati -- ko'rish.
    Har bir yangilik haqida ma'lumot (sarlavhasi, matni, rasmi, sanasi) -- ko'rish, o'zgartirish. 
    4) Darslar ro'yhati -- ko'rish.
    Har bir dars haqida ma'lumot (fan nomi, guruh nomi, o'qituvchi fio, sana, davomat) -- ko'rish.
    5) Guruhlar ro'yhati -- ko'rish.
    Har bir guruh haqida ma'lumot (fan nomi, guruh nomi, o'qituvchi fio, o'quvchilar ro'yhati) -- ko'rish, o'zgartirish.
    6) Darslar jadvali -- ko'rish, o'zgartirish.
```

```
4. Superadminni sistemaga qo'shish faqat dasturchilar tomonidan amalga oshiriladi.
```

```
Super admin imkoniyatlari:
    1) Adminning barcha imkoniyatlari.
    2) Admin qo'shish, o'chirish, o'zgartirish.
```

# 5. Mobil ilova batafsil.
```  
pass
```

# 6. Web-sayt (adminka) batafsil.
```
Web-saytning asosiy bo'limlari sidebar (menyu) orqali ajratiladi.
Web-sayt quyidagi asosiy bo'limlardan tashkil topadi:
```

## 6.1. Admin uchun.

```
1. Marketing bo'limi. Bu bo'limning o'zi 2 ga bo'linadi. O'quv markazi ma'lumotlari va bitiruvchilar yutuqlari. Bu bo'limda admin markazning ma'lumotlari va yutuqlarini ko'rish va o'zgartirish imkoniyatiga ega bo'ladi. Bu ma'lumotlar mehmon foydalanuvchilar (va boshqa barchalar) uchun mobil ilovada ko'rinib turadi. 

Markaz ma'lumotlari quyidagilar:
    * Markaz nomi
    * Markaz haqida batafsil (matn)
    * Manzili
    * Fanlar. Har bir fanning ma'lumotlari (mavzu va manbaalar)
    * Kontaktlar (instagramm, facebook, telegram, telefon raqami)

Muvaffaqiyatli bitiruvchilar ro'yhati ko'rinib turadi va admin bu ma'lumotlarni o'zgartirish va yangi bitiruvchi qo'shish imkoniga ega.

Har bir bitiruvchida quyidagi ma'lumotlar bo'ladi:
    * Ism Familiyasi
    * Rasmi
    * Bitirgan kursi/fani
    * Bitirgan sanasi
    * Muvaffaqiyatini izohlovchi matn
```

```
2. O'quvchilar bo'limi. Bu bo'limga kirganda barcha o'quvchilar ro'yhati ko'rinib turadi. Yangi ro'yhatdan o'tgan tasdiqlanmagan o'quvchilar ro'yhatning boshida turadi. Ro'yhatda o'quvchining quyidagi ma'lumotlari bo'ladi:
    * ism familiyasi 
    * telefon raqami 
    * qo'shilgan guruhlari nomi 
    * tasdiqlangan yoki yo'qligi
    * to'lov statusi 
Bu ma'lumotlar jadval ko'rinishida ko'rinib turadi.

Har bir o'quvchi ustiga bosganda o'quvchining batafsil ma'lumotlari sahifasiga o'tiladi. Bunda admin o'quvchining faqat: 
    * ism familiyasi
    * yoshi
    * rasmi
    * telefon raqami
    * guruhlari nomi
    * davomat tarixi
    * to'lov tarixi
shu ma'lumotlarni ko'rishi mumkun bo'ladi. O'quvchining to'lovini qabul qilish ham shu sahifada amalga oshiriladi.

O'quvchi test darsidan o'tib guruhga qabul qilinganida (ya'ni biror guruhga o'qituvchi yoki admin tomonidan qo'shilganida) o'sha kundan boshlab unga 1 oylik to'lov belgilanadi va avtomatik tarzda to'lov statusi "to'lanmagan/qizil" bo'ladi. Agar admin to'lovni qabul qilib o'quvchining to'lov statusini o'zgartirsa status "to'langan/yashil"ga o'zgaradi. Keyingi oyning o'sha sanasi kelganda to'lov statusi yana "to'lanmagan"ga o'zgaradi. Har bir to'lov saqlanib qolinadi va to'lov tarixida jadval ko'rinishadi chiqib turadi.
```

```
3. O'qituvchilar bo'limi. Bu bo'limda ham 2-bo'limga o'xshab o'qituvchilar ro'yhati jadval ko'rinishida chiqib turadi. 
Jadvalda quyidagi ma'lumotlar bo'ladi:
    * ism familiyasi
    * fan nomi
    * telefon raqami
    * guruhlari nomi
Har bir o'qituvchiga kirganda uning batafsil ma'lumotlari sahifasiga o'tiladi. Bunda quyidagi ma'lumotlarni ko'rish mumkin bo'ladi:
    * ism familiyasi
    * fan nomi    
    * yoshi
    * rasmi
    * yashash manzili
    * telefon raqami
    * bank hisob raqami
    * guruhlari ro'yhati
    * tugatilgan guruhlari tarixi
    * darslar tarixi
Darslar tarixi jadval ko'rinishida bo'ladi.
Admin o'qituvchilarni ma'lumotlarini o'zgartira olmaydi. O'qituvchilarning faqat o'zlari shaxsiy kabinetlaridan o'zgartira olishlari mumkun bo'ladi. O'qituvchini bo'shatish ham shu sahifada amalga oshiriladi. Bo'shatish uchun admin bo'shatish tugmasini bosadi va ketish sababi yozilib tasdiqlanadi.

Shuningdek bu bo'limda o'qituvchilar tarixi ham bo'ladi. Yani markazda ishlab ketgan o'qituvchilar ro'yhati jadval ko'rinishida:
    * ism familiyasi
    * fan nomi
    * telefon raqami
    * kelgan sanasi
    * ketgan sanasi
    * ketish sababi
```

```
4. Guruhlar bo'limi. Bu bo'limda guruhlar ro'yhati jadval ko'rinishida ko'rinib turadi:
    * guruh nomi
    * fan nomi
    * o'qituvchi
    * o'quvchi soni
    * dars jadvali (Dush-Chor-Juma  10:00 - 20:00)
    * guruh ochilgan sana
    * guruh yopilish sanasi
Bu sahifada yangi guruh qo'shish funksiyasi ham bo'ladi. Bunda admin guruh qo'shish tugmasini bosadi va guruh ma'lumotlarini kiritadi.

Har bir guruh ustiga bosganda guruhdagi o'quvchilarning ma'lumotlari (ism, familiyasi, to'lov statusi) va shu guruhning dars jadvali ko'rinib turadi.
Shuningdek o'quvchilarni guruhlarga qo'shish va guruhlardan o'chirish ham shu sahifada amalga oshiriladi.
```

```
5. Darslar tarixi bo'limi. Bu bo'limda darslar ro'yhati jadval ko'rinishida ko'rinib turadi:
    * guruh nomi
    * fan nomi
    * o'qituvchi
    * qatnashgan o'quvchilar soni
    * sana/vaqt
Har bir dars ustiga bosganda o'sha darsga tegishli davomat ko'rinib turadi.
```

```
6. Yangiliklar bo'limi. Bu bo'limda yangiliklar ro'yhati jadval ko'rinishida ko'rinib turadi:
    * sarlavhasi
    * sanasi
    * rasmi
Yangilik qo'shish ham shu sahifada amalga oshiriladi. Bunda yangilik qo'shish tugmasini bosib yangilik ma'lumotlari kiritiladi (sarlavha, rasm, matn).

Har bir yangilik ustiga bosib uni o'zgartirish imkoniyati ham mavjud.
```

## 6.2. Superadmin uchun.
```
Superadmin uchun adminda bor barcha bo'limlarga yana 7-bo'lim qo'shiladi.

    Adminlar boshqaruvi bo'limi. Bu bo'limda admin qo'shish yoki olib tashlash imkoniyati mavjud bo'ladi.
Barcha adminlar quyidagi ma'lumotlar bilan ko'rinib turadi:
    * ism familiyasi
    * telefon raqami
    * yashash manzili
    * yoshi
    * rasmi
    * bank hisob raqami
    * ishga kirgan sanasi
```

# 7. Xabarnomalar.
```
1. O'quvchining to'lov statusi "to'lanmagan/qizil"ga o'tishi bilan o'quvchidagi mobile ilovaga xabarnoma keladi. Xabarnoma matni taxminan quyidagicha bo'ladi:
"Xurmatli Falonchi, Sizga falon o'quv markaziga to'lov qilish vaqtingiz kelganini eslatib o'tamiz".
```