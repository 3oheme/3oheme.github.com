---
layout: post
title:  "Different areas you need to think about for a website frontend - [Work in progress]"
date:   2013-09-25 18:48:00
excerpt: "Hi guys! This is just a list I've created basically for myself, so I"
categories: blog

---

<p><img class="full-width-image" src="/images/html5_web_areas.png" /></p>

Hi guys!

This is just a list I've created basically for myself, so I don't forget any scenario or issue when thinking about a frontend project, but I thought it'd be useful for any other frontend out there :-)

Please feel free to add anything I've forgot in the comments, so I can update it.

* **Reset** or **normalize** your default CSS .
* **Grid system** — handmade, supporting different breakpoints or just tackling a fixed amount of columns across devices.
* CSS3 **feature detection** libraries like [moderniz](http://modernizr.com/) or relying on [native detection](http://dev.opera.com/articles/view/native-css-feature-detection-via-the-supports-rule/).
* CSS **preprocessor** — [SASS](http://sass-lang.com/) or [LESS](http://lesscss.org/).
* How are you going to **organize your CS**S? [OOCSS](https://github.com/stubbornella/oocss/tree/master/oocss), [SMACCS](http://smacss.com/), or maybe [Semantic UI](bit.ly/1fmXi1H)
* **Responsive images solution** — while W3C is still refining the [picture element draft](http://picture.responsiveimages.org/), you should give a try to [picturefill](https://github.com/scottjehl/picturefill), the [clown car technique](http://coding.smashingmagazine.com/2013/06/02/clown-car-technique-solving-for-adaptive-images-in-responsive-web-design/) or use a [server side solution](http://www.hongkiat.com/blog/serving-responsive-images/).
* Where are you going to set your [media queries](http://bit.ly/188oUBo) [breakpoints](http://bit.ly/188oPNR)? **new**
* Would you like to support [retina](http://bit.ly/15zBP1b) or [high DPI](http://retina-images.complexcompulsions.com/) devices? **new**
