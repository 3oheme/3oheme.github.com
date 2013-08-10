---
layout: post
title:  "Why, when and how you should apply FastClick"
date:   2013-08-08 09:15:00
excerpt: "If you're a nerd like me you've probably find yourself trying to view the source code of a website from"
categories: blog

---

Some mobile or touch devices apply a **300 ms delay to any touch event**, usually in order to detect zooming with double tap (there is a further detailed explanation in [Google fast buttons article](http://bit.ly/1eAtuJo)). 

That delay is desirable in certain scenarios, but when users are dealing with some specific areas like carousels, buttons or dropdowns, **this can be felt as unresponsive and slow**.

If you are in a mobile, try following buttons:

<p><button class='slowclick' style='margin-right: 1em'>Button 1</button>
<button class='fastclick'>Button 2</button></p>

The first button shows the normal behaviour, and the second one presents the FastClick approach.


<script type="text/javascript" src="/resources/fastclick_example.js" >&nbsp;</script>

<style>
.active { background: #FF9999 !important }
.fastclick, .slowclick { padding: 1em; background: #EEE; border: 1px solid #999 }
</style>

### When

I recommend using this trick only in specific scenarios, where we really need to trigger an action immediately, as applying it to any click will disable the double tap zoom in most of devices.

### How

The easiest way is using [dave1010](http://bit.ly/15YIIG0) [jQuery plugin version of FastClick](http://bit.ly/15YIC1i).

1. First of all, **include jQuery** in your head, as usual.
2. Later, [download](http://bit.ly/15YJinb) and **include the jQuery Plugin** after jQuery.
3. Use it. Instead using the classic:

{% highlight javascript %}
  $('#element').click()
{% endhighlight %}
 
you just need to use:

{% highlight javascript %}
  $('#element').fastClick()
{% endhighlight %}