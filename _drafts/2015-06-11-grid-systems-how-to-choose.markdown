---
layout: post
title:  "Grid systems and defining the contract"
date:   2015-06-11 23:48:00
excerpt: "Responsive, gutter configurable, SASS/LESS, IE8 support, golden ratio, 1KB minimised, flexbox, background-bleed, HTML5"
categories: blog
permalink: blog/grid-systems-defining-the-contract

---

How to choose a CSS grid system?

> Responsive, gutter configurable, SASS/LESS, IE8 support, golden ratio, 1KB minimised, flexbox, background-bleed, HTML5, 960px, fluid, BEM, border-box, mobile-first, 12 columns, nestable.

I think all this specs are important, and they're helpful to find your perfect partner in crime. But this is not taking in consideration one small thing.

## The contract

Let's keep this simple: **A grid system is a mixture of CSS and HTML that produces a pleasant layout structure**. Easy, right?

<p><img class="full-width-image" src="/images/html-css-contract.jpg" /></p>


There are two parts that need to agree in order to produce the desired goal — and that's a contract. If the HTML or the CSS changes, probably the result will not be the one we need.

And when we use a grid system we're declaring, without noticing, who is defining the contract.

### What are the options?

So, the contract can be declared in two places: the HTML or the CSS. **When the HTML is the one who leads the conversation, we say that's a semantic grid** system. In the other hand, **when the CSS defines the contract, we have an explicit grid system**.

### Semantic grid systems

A semantic grid

<p><img class="full-width-image" src="/images/semantic-grid.png" /></p>
