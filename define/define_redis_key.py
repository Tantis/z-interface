#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Copyright (c) 2019 winslen
# All rights reserved

# 用户粉丝集合(uid)
UserFans = 'user:%s:fans:set'
# 用户关注集合(uid)
UserFollow = 'user:%s:follow:set'
# 用户收藏的小说集合(vid)
UserCollectVideo = 'user:%s:noval:collect:set'
# 小说观看集合
VideoWatch = 'noval:watch:%s:set'
# 小说点赞集合
VideoPraise = 'noval:praise:%s:set'
VideoTread = 'noval:tread:%s:set'
UserPraise = 'user:praise:%s:set'
userPraiseVideo = "user:praise:noval:%s:set"

# 小说父级评论点赞集合
CommentParentPraise = 'noval:praise:comment:%s:set'
# 小说父级评论点赞集合
CommentChildPraise = 'noval:praise:comment:%s:%s:set'

# 每日签到记录
UserSignInRecord = 'user:%s:signIn:record'
UserSignDateHash = "user:%s:sigin:%s:hash"

FOLLOW_NUM = 0
FOLLOW_NOT_NUM = 1

Video_Collect_Do = 1
Video_Collect_Cancel = 2

StartReaderBook = "user:reader:%s:%s:hash"