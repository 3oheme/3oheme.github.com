---
layout: post
title:  "Consistency vs user centric design"
date:   2019-11-19 20:21:00
excerpt: "After this hilarious retweet from Jared Spool, I thought I'd be great to"
categories: blog

---

After this [hilarious retweet from Jared Spool](https://twitter.com/jmspool/status/1193719439772078080), I thought I'd be great to share my collection of super fail design decisions of priorising design consistency versus a proper user centric design, because Design systems are killing creativity and whatnot :-D

So, in case you need more reasons to break some design conventions for the user, here you have some more examples:

<div class="consistency-gallery">
  <img class="consistency-gallery--item" src="/images/consistency-1.jpg" />
  <img class="consistency-gallery--item" src="/images/consistency-2.jpg" />
  <img class="consistency-gallery--item" src="/images/consistency-3.jpg" />
  <img class="consistency-gallery--item" src="/images/consistency-4.jpg" />
  <img class="consistency-gallery--item" src="/images/consistency-5.jpg" />
  <img class="consistency-gallery--item" src="/images/consistency-6.jpg" />
</div>

<a href="http://assets.imgix.net/dog.png?w=1600">
  <img src="/images/consistency-1.jpg" />
</a>

<style>
  @media only screen and (min-width: 500px) {
    .consistency-gallery {
      display: grid;
      grid-gap: 10px;
      grid-template-columns: 50% 50%;
    } 
    .consistency-gallery--item {
      margin-bottom: 0px
    }
  }
  .consistency-gallery--item {
    object-fit: cover;
    width: 100%;
    height: 300px;
    border-radius: 4px;
    margin-bottom: 10px
  }
</style>

<script type="text/javascript" 
    src="https://cdnjs.cloudflare.com/ajax/libs/luminous-lightbox/2.3.2/luminous.min.js"></script>
<script type="text/javascript">
  new Luminous(document.querySelector("a"));
</script>
