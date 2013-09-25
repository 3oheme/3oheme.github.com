---
layout: post
title:  "Different areas you need to think about for a website frontend - [Work in progress]"
date:   2013-09-24 11:48:00
excerpt: "Today in the office I've been asked about how to be up-to-date in the user experience world, and"
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
* How are you going to **organize your CS**S? [OOCSS](https://github.com/stubbornella/oocss/tree/master/oocss) or [SMACCS](http://smacss.com/).
* **Responsive images solution** — while W3C is still refining the [picture element draft](http://picture.responsiveimages.org/), you should give a try to [picturefill](https://github.com/scottjehl/picturefill), the [clown car technique](http://coding.smashingmagazine.com/2013/06/02/clown-car-technique-solving-for-adaptive-images-in-responsive-web-design/) or use a [server side solution](http://www.hongkiat.com/blog/serving-responsive-images/).

