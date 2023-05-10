---
title: "Styling"
slug: styling
date: 2022-07-22
draft: false
toc: false
---
*This piece first appeared on the [Until It's Not Fun](https://untilitsnotfun.com/posts/2022-07-22/) newsletter.*

I've been dabbling with web development for a while now and was looking for the best tools for the job. For basic websites, you need two things: HTML and CSS.

HTML (HyperText Markup Language) describes the content of the website and looks like this:
```
<h1>This is a heading!</h1>

<p>This is some content!</p>

<a href="somewebsite.com">This is a link!</a>

<a href="specialwebsite.com" class="specialLink">This is a special link</a>

<img src="someimage.jpg">
```
Every piece of content, whatever it is, is wrapped in **tags** and might have some **attributes** and **values** (`href` is an attribute with a value of `somewebsite.com`, `class` is an attribute with a value of `specialLink`, and so on) that combine into a single **element**. Now, if you wrote exactly that HTML file and deployed it, it would look awfully boring. It would be a white screen with a black font that says "This is a heading", "This is some content", a blue link to "somewebsite.com", another link, and an image.

We need some way to style our content and CSS does exactly that. CSS stands for Cascading Style Sheets. It is code written to specifically style HTML by changing colors, fonts, animations, and placement on the page. The page you are reading right now (if you are reading this on the website) has CSS for a unique font and large margins on the left and right of the text. The traditional way to do styling is make a separate CSS file, target individual elements, and write specific style rules for those elements. In our example, let's say you wanted to center the `h1` element and make the font size bigger. You also want the links to be red instead of blue. This would be done like this:
```
h1 {
	text-align: center;
	font-size: 24px;
}

a {
	color: red;
}
```
Easy! You target the `h1` element and write some style rules. Then you target the `a` elements and apply different rules. As you add more content and rules, you can start to make really complex and beautiful websites. What if we wanted the special link to look different? We can use the `class` attribute to target that link specifically. It would look like this:
```
a {
	color: red;
}

a.specialLink {
	color: magenta;
	font-size: 36px;
}
```
We can target specific elements by adding a class to that element and updating our CSS accordingly. The first rule targets all `a` tags (aka links) and colors them red. The second rule targets all `a` tags that have a class of `specialLink` and colors them magenta and makes the font size 36 pixels.

Imagine you had a website with thousands of these elements and you need to individually target many of them. You would have to think of a clever class name for each of them and write at *least* three extra lines of CSS for each element. That quickly gets arduous, takes way too long, and is difficult to maintain.

Rather than use the class attribute as a marker to refer to later in your CSS, what if there was a way to use the class attribute functionally? In comes **utility classes** and Tailwind.

Tailwind is a tool that allows you to write your CSS *inside* of your HTML. To do the exact same thing as the previous example, your HTML would look like this:
```
<h1 class="center font-xl">This is a heading!</h1>

<p>This is some content!</p>

<a class="text-red" href="somewebsite.com">This is a link!</a>

<a class="text-magenta font-4xl" href="specialwebsite.com">This is a special link</a>

<img src="someimage.jpg">
```
To do the same thing, I didn't have to write any CSS and both my content and styling are done in the same file. You can see that I used Tailwind's pre-defined classes in my HTML and Tailwind converts that to CSS. It specifically scans the HTML, sees that the `h1` tag has a class of `center` and `font-xl`. Tailwind knows to map the class attribute `center` to `text-align: center;` and does that for every element.

Rather than trying to find and target individual elements and worry about overriding previously written rules, you can write the specific styling for each element from *within the element itself*. It has really removed a lot of headaches for me and speeds up development. As an initial first test, I completely redid the CSS on my personal website. I converted all the old CSS to Tailwind. It is now so much easier to make small changes to colors, sizing, and placement of anything within my website. For new projects, it makes getting started that much easier as well.

Tailwind is an excellent concept and tool that I will absolutely be using for all of my web development projects in the future.

Good luck in the future,

Westley