---
layout: post
title: Djangooru Progress (5/11/20)
date: 2020-11-5 11:41:20
lang: en
tags: python django programming
permalink: /en/Djangooru-Progress-1
---

![_djangooru1]({{ site.baseurl }}/images/djangooru1.png)

Djangooru is a taggable Image Board written in Django using the help of [django-tagging](https://pypi.org/project/django-tagging/). It's simple and has a better look than danbooru. Github: <https://github.com/mochidaz/djangooru>

## Filters

Djangooru's tag filtering works just like any other taggable image-board. It does support multiple tag search. The search system works like danbooru: Underscore to replace space, and space to separate tags.

![_djangooru2]({{ site.baseurl }}/images/djangooru2.png)

## Post Detail

Post detail shows the post id, source, artist, and the uploader. The image is resized, but for now, because it looks poor on mobile if the image is resized with percentage, i decided to not resizing it. If you can make a resize system without making the page looks poor, you can just submit a pull request.

![_djangooru4]({{ site.baseurl }}/images/djangooru4.png)

## Upload

Upload form without good design because it will return an error if i use crispy template

![_djangooru5]({{ site.baseurl }}/images/djangooru5.png)

## Pagination and next/prev

Next/prev and pagination are done. On detail view, if next/previous post is available, it will jump to the next/previous post id. If you are searching in specific tags, it will jump to the next/previous post id that also has the same tags as you've searched. Pagination works fine, per 15 posts.

![_djangooru6]({{ site.baseurl }}/images/djangooru6.png)

## API

Api still in development. You can help if you want. It uses [djangorestframework](https://pypi.org/project/djangorestframework/)

## What i am planning to add

- Favorite feature, using ajax. But you know, i hate writing javascript
- Pool system
- etc

