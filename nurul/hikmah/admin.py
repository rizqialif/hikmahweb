from django.contrib import admin
from .models import Kategori, Produk, Slide, Kontak,Profil,Statis, ChatID 

class DataKategoriAdmin(admin.ModelAdmin):
    list_display = ("nama", "aktif","banner_satu","banner_dua",) 
    prepopulated_fields = {"slug": ("nama",)}
    
class DataProdukAdmin(admin.ModelAdmin):
    list_display = ("kategori", "nama_produk","gambar","gambar_satu","gambar_dua","gambar_tiga", "gambar_empat", "gambar_lima", "keterangan","harga", "no_whatsup", "tanggal_upload", "diskon", "dibeli", "keterangan_barang", )
    prepopulated_fields = {"slug": ("nama_produk",)}

class DataSlideAdmin(admin.ModelAdmin): 
    list_display = ("teks_awal", "teks_dua","teks_tiga","gambar_slide", "aktif",) 

class DataKontakAdmin(admin.ModelAdmin): 
    list_display = ("nama", "no_whatsup","email","subject", "isi",) 

class DataProfilAdmin(admin.ModelAdmin): 
    list_display = ("nama", "keterangan","gambar","tanggal_upload",) 

class DataStatisAdmin(admin.ModelAdmin): 
    list_display = ("alamat_kami", "telpon","email",)

    


admin.site.register(Kategori,DataKategoriAdmin)
admin.site.register(Produk,DataProdukAdmin) 
admin.site.register(Slide,DataSlideAdmin) 
admin.site.register(Kontak,DataKontakAdmin) 
admin.site.register(Profil,DataProfilAdmin) 
admin.site.register(Statis,DataStatisAdmin)
admin.site.register(ChatID)
