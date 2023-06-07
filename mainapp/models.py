from django.db import models

class Cotton(models.Model):
    navi = models.CharField(max_length=50, verbose_name='Paxta navi', blank=True, null=True)
    usish_davri = models.CharField(max_length=10, verbose_name="O'sish davri", blank=True, null=True)
    uzunlik = models.CharField(max_length=10, verbose_name="Tola uzunligi", blank=True, null=True)
    hosildorlik = models.CharField(max_length=10, verbose_name="Hosildorligi", blank=True, null=True)
    tola_tipi = models.CharField(max_length=10, verbose_name="Tola tipi", blank=True, null=True)
    nisbiy_kuch = models.CharField(max_length=20, verbose_name="Nisbiy uzunlik kuchi", blank=True, null=True)
    nav_guruxi = models.CharField(max_length=30, verbose_name="Paxta navlari guruxi", blank=True, null=True)
    tola_chiqishi = models.CharField(max_length=10, verbose_name="Tola chiqishi", blank=True, null=True)
    tola_pishiqligi = models.CharField(max_length=10, verbose_name="Tolaning pishiqligi", blank=True, null=True)
    country = models.CharField(max_length=30, verbose_name="Mamlakat",blank=True, null=True)
    popular = models.BooleanField(verbose_name='Mashxur nav', default=False)
    local = models.BooleanField(default=True, verbose_name='Mahalliy')

    def __str__(self) -> str:
        return self.navi