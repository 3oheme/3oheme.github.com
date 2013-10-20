---
layout: wide-post
title:  "Different areas you need to think about for a website frontend - [Work in progress]"
date:   2013-09-25 18:48:00
excerpt: "Hi guys! This is just a list I've created basically for myself, so I"
categories: blog

---

<p><img class="full-width-image" src="/images/html5_web_areas.png" /></p>

Hi guys!

This is just a list I've created basically for myself, so I don't forget any scenario or issue when thinking about a frontend project, but I thought it'd be useful for any other frontend out there :-)

Please feel free to add anything I've forgot in the comments, so I can update it.


### Documenting the code

**One of the easiest ways to improve the communication between frontend and backend developers is using a styleguide** ([starbucks](http://bit.ly/Yicgb2), [Github](http://bit.ly/17XbvIZ) or [Hackerhires](http://bit.ly/1gWYBmi) examples) — that's one of the main reasons why twitter bootstrap has been so widely used.

The following tools and links will help you to create styleguides:

* [Kneath](http://warpspire.com/kss/) is a methodology for documenting CSS and generating styleguides.
* [Nadarei KSS]( http://nadarei.co/nkss-rails) is a Kneath KSS port to Rails.
* [Kalei styleguide](http://kaleistyleguide.com/) is a clever client-side solution using backbone, so no need to maintain a server.
* [Pears](http://pea.rs/) uses wordpress and a [specific theme](https://github.com/simplebits/Pears) to create styleguides.
* [Styledocco](http://jacobrask.github.com/styledocco/) uses NodeJS and Markdown to generate HTML styleguides and documentation.
* [Patter primer](https://github.com/adactio/Pattern-Primer) generates styled markup from a folder of markup snippets.
* [TopDoc](https://github.com/topcoat/topdoc) is a well documented tool for generating usage guides for css that uses very stric structures to document our CSS code.
* And some interesting reference posts from [Warpspire](http://warpspire.com/posts/kss/), [rjmetrics](http://blog.rjmetrics.com/2012/02/20/our-living-style-guide-writing-maintainable-htmlcss/#.Ul1ZBGR9DFQ) and [UXMag](http://uxmag.com/articles/anchoring-your-design-language-in-a-live-style-guide).


### Regression tests

**CSS is a set of rules that, applied to some specific HTML, produce a pleasant result**. That's why is not easy to add tests to a CSS framework, but there are some different stages we can add to our pipeline, mostly based on before and after image diffs:

* [Wraith](https://github.com/bbc-news/wraith), a responsive screenshot comparison tool from the BBC guys.
* [PhantomCSS](https://github.com/Huddle/PhantomCSS) provides visual regression testing with PhantomJS.
* [Hardy](https://github.com/thingsinjars/Hardy) is, as they say, a *"Selenium-driven, cucumber-powered CSS testing"*.
* [CSS critic](http://cburgmer.github.io/csscritic/), a lightweight framework for regression testing of Cascading Style Sheets.
* [Sikuli](http://www.sikuli.org/) is a *general purpose visual technology to automate and test graphical user interfaces using screenshot images*.
* [SuitCSS](https://github.com/suitcss/test) provides a test structure for visually testing other components.

### Static code analysis

Interesting as a before-commit, checking any syntax errors and code redundancy:

* [CSSCSS](http://zmoazeni.github.io/csscss/) is a CSS redundancy analyzer that analyzes redundancy (I love this guys :-)
* CSSLint [online tool](http://csslint.net/) and [command line tool](https://github.com/stubbornella/csslint/wiki/Command-line-interface) for syntax and basic performance checking.
* [MINCSS](https://github.com/peterbe/mincss) will check unused CSS selectors in your code.


### Specific HTML+CSS implementation

Once we have set up our whole project, is time to start thinking about the specific CSS code we are going to write, then you should think about:

* **Reset** or **normalize** your default CSS.
* **Grid system** — handmade, supporting different breakpoints or just tackling a fixed amount of columns across devices.
* CSS3 **feature detection** libraries like [moderniz](http://modernizr.com/) or relying on [native detection](http://dev.opera.com/articles/view/native-css-feature-detection-via-the-supports-rule/).
* CSS **preprocessor** — [SASS](http://sass-lang.com/) or [LESS](http://lesscss.org/).
* How are you going to **organize your CS**S? [OOCSS](https://github.com/stubbornella/oocss/tree/master/oocss), [SMACCS](http://smacss.com/), or maybe [Semantic UI](bit.ly/1fmXi1H).
* **Responsive images solution** — while W3C is still refining the [picture element draft](http://picture.responsiveimages.org/), you should give a try to [picturefill](https://github.com/scottjehl/picturefill), the [clown car technique](http://coding.smashingmagazine.com/2013/06/02/clown-car-technique-solving-for-adaptive-images-in-responsive-web-design/) or use a [server side solution](http://www.hongkiat.com/blog/serving-responsive-images/).
* Where are you going to set your [media queries](http://bit.ly/188oUBo) [breakpoints](http://bit.ly/188oPNR)? **new**
* Would you like to support [retina](http://bit.ly/15zBP1b) or [high DPI](http://retina-images.complexcompulsions.com/) devices? **new**
