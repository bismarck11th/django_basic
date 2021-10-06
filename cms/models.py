from django.db import models


class Book(models.Model):
    """書籍"""
    name = models.CharField('書籍名', max_length=255)
    publisher = models.CharField('出版社', max_length=255, blank=True)
    page = models.IntegerField('ページ数', blank=True, default=0)

    objects = models.Manager()

    def __str__(self):
        return self.name


class Impression(models.Model):
    """感想"""
    # Bookに紐づく子供のImpressionは、related_nameを使って、読み出すことができる。
    # impressions = book.impressions.all().order_by('id')
    book = models.ForeignKey(Book, verbose_name='書籍', related_name='impressions',
                             on_delete=models.CASCADE)
    comment = models.TextField('コメント', blank=True)

    objects = models.Manager()

    def __str__(self):
        return self.comment
