from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField('分类名称', max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '文章分类'
        verbose_name_plural = '文章分类'


class Tag(models.Model):
    name = models.CharField('标签名称', max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = '标签'


class Article(models.Model):
    STATUS_CHOICES = (
        (0, '草稿'),
        (1, '公开发布')
    )
    PIN_CHOICES = {
        (0, '非置顶'),
        (1, '置顶')
    }
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='所属分类')
    tags = models.ManyToManyField(Tag, verbose_name='标签')
    title = models.CharField('标题', max_length=200)
    description = models.CharField('摘要', max_length=500)
    text = models.TextField('正文')
    time = models.DateTimeField('发布时间')
    pin = models.IntegerField('是否置顶', choices=PIN_CHOICES, default=0)
    status = models.IntegerField('状态', choices=STATUS_CHOICES, default=1)
    pwd = models.CharField('访问密码', max_length=50, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = '文章'


class Comment(models.Model):
    STATUS_CHOICES = (
        (-1, '屏蔽'),
        (0, '公开展示'),
        (1, '置顶展示')
    )
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='所属文章')
    user = models.CharField('评论者昵称', max_length=100, default='匿名用户')
    email = models.CharField('评论者邮箱', max_length=100, default='未提供')
    text = models.TextField('内容')
    time = models.DateTimeField('发布时间', auto_now_add=True)
    status = models.IntegerField('状态', choices=STATUS_CHOICES, default=0)

    def __str__(self):
        return self.user + ' - ' + self.article.title

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = '评论'


class Attachment(models.Model):
    content = models.FileField(upload_to='attachments/%Y/%m/')

    def __str__(self):
        return '文件-%d' % self.id

    class Meta:
        verbose_name = '附件'
        verbose_name_plural = '附件'
