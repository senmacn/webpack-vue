from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField('博客分类', max_length=10)
    index = models.IntegerField(default=999, verbose_name='分类排序')

    class Meta:
        verbose_name = '博客分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

# 文章标签


class Tag(models.Model):
    name = models.CharField('文章标签', max_length=10)

    class Meta:
        verbose_name = '文章标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

# 文章


class Article(models.Model):
    title = models.CharField('标题', max_length=50)
    excerpt = models.TextField('摘要', max_length=200, blank=True)
    category = models.ForeignKey(
        Category, on_delete=models.DO_NOTHING, verbose_name='分类',
        blank=True, null=True)
    tags = models.ManyToManyField(Tag, verbose_name='标签', blank=True)

    body = models.TextField()
    body = models.TextField()
    views = models.PositiveIntegerField('阅读量', default=0)
    created_time = models.DateTimeField('发布时间', auto_now_add=True)
    modified_time = models.DateTimeField('修改时间', auto_now=True)

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = '文章'

    def __str__(self):
        return self.title
