#coding: utf-8
# from __future__ import unicode_literals
from django.contrib.auth.models import User
from block.models import Block
from article.models import Article
from django.db import models
from usercenter.models import UserProfile

class Comment(models.Model):
      block = models.ForeignKey(Block,verbose_name=u"所属版块")
      article = models.ForeignKey(Article,verbose_name=u'所属文章')
      to_comment_id = models.IntegerField(u'回复评论',default=0)
      content = models.CharField(u"内容", max_length=10000)
      owner = models.ForeignKey(User,verbose_name=u"评论者")
      status = models.IntegerField(u"状态",choices=((0,u"普通"),(-1,u"删除")),default=0)

      create_timestamp = models.DateTimeField(auto_now_add=True)
      last_update_timestamp = models.DateTimeField(auto_now=True)

      @property
      def to_comment(self):
            if not self.to_comment_id:
                  return None
            else:
                  return Comment.objects.get(id=self.to_comment_id)

      @property
      def profile_com(self):
            return UserProfile.objects.get(owner=self.owner)

      def __unicode__(self):
            return self.content[:20]
      class Meta:
            verbose_name= u"评论"
            verbose_name_plural= u"评论"