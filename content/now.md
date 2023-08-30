---
title: Now
menu: main
weight: 1
---

This page serves to give you an idea of what I am currently working on, in no particular order. This is inspired by the "Now page" movement created by [Derek Sivers](https://nownownow.com/about). In [The Anatomy of Equanimity](https://anatomy.1651.org/) system, these are my current projects and quests.

## Promoting world peace and friendship

I am approaching my first full year in Morocco as a Peace Corps volunteer. It has been such a wonderful and difficult experience that I wouldn't change for anything. I am here, in part, to increase cross-cultural understanding. I participate in meaningful holidays, have meals with my Moroccan friends and family, and speak the same language they speak (as best as I can).

## Blogging about Morocco and my Peace Corps service

I started up [this blog]({{< relref "peace-corps" >}}) before I left, wrote a few posts, then neglected to write anything for five months. I just started it back up and have some ideas for future posts. My latest post was about a festival called a [moussem]({{< relref "The Moussem" >}}) and if you'd like to sign up to get the next posts in your email inbox, input your email [here](https://buttondown.email/Westley_Winks). 

This goes along with the above quest. They are fun to write but I feel quite a lot of Resistance because I want to tell these stories right and the perfectionism gets in the way.

## Learning Vim

I have always wanted to learn how to use this [popular text editor](https://www.vim.org/) and was inspired by Reddit to finally get after it. It is simply a tool used to write text into files on a computer. The "normal" way to do this is to use a text editor like VSCode or Sublime. These are very user friendly and you can see everything you need to and click around like normal. Vim, however, was used before there were things like mouses and GUIs.

With Vim, you can translate what you want to do in your head to the computer much faster. You can tell it to, for example, "change the text inside the next pair of parentheses" by typing `cin(`. This deletes what is inside the parentheses and sets your cursor there to type in the substitution. Another is "delete the next 3 lines" done by typing `3dd`. One of personal favorites so far (using the surround plugin) is `ysiw]` to wrap the current word in square brackets. Think about how many key presses or mouse movements these examples would take and you can start to see how much easier it is to get your thoughts from your brain and into the computer.

## Learning bookkeeping (using Beancount)

Also from Derek Sivers, I heard about a program called Beancount which led me down a rabbit hole of [plain text accounting](https://plaintextaccounting.org/). The whole idea is to have your entire ledger (i.e. all of your transactions involving commodities) in a format that is plain text. There are many benefits to doing it this way. First, **plain text is eternal**. Your accounting isn't locked up at the mercy of some company like Quicken or YNAB. If those softwares go down, so do all the data they contain. If all of your transactions are in plain text, you can see all of those transactions on any computer. Second, it makes it scriptable. You can write code to do any kind of reporting or budgeting you'd like.

My tool of choice was [Beancount](https://beancount.github.io/). It is open source and has fantastic documentation that doesn't only cover how to use the tool but also examples and the theory behind the method. I have one big file called `main.beancount` that contains all of my money transactions that I add to every time I buy something. Whenever I'd like, I can generate balance sheets and income statements for any given time period with just a few commands (e.g. `bean-report main.beancount balances`). 

The underlying principle behind the accounting is called the [double-entry counting method](https://beancount.github.io/docs/the_double_entry_counting_method.html). It is a way of counting that ensures that each transaction balances out to zero. In other words, money that comes in or goes out of an account must come from or go to another account.

## Writing the Weekly PCV Weather Report

Every Monday, I gather weather data from an API for all of the Peace Corps Volunteers in Morocco for the previous week. Since it is so hot here in the summer, I find out which volunteers have the hottest and coolest sites and report that out into our group chat, adding some snippets and analysis of my own. I also generate a cute little stem plot that I love. This is a nice little weekly project that I thoroughly enjoy doing and gets the volunteers talking.

## Becoming a more compassionate person

This one is a bit more abstract and difficult than the rest. This started as a quest towards emotional intelligence until I delved in learned that that is a sub-skill for something much more profound: cultivating meaningful connection between people. One of the most powerful tools for cultivating connection and being in service of others is **compassion** and so that is my quest.

In order, I read [*Nonviolent Communication*]({{< relref "Nonviolent Communication" >}}), [*Permission to Feel*]({{< relref "Permission to Feel" >}}), [*Atlas of the Heart*]({{< relref "Atlas of the Heart" >}}) and am currently reading *Self-Compassion* by Kristin Neff. These have given me a lot of insight and tools from multiple different angles to help me in this quest.

## Writing book notes

I have been having a blast with this. I've had quite a bit of free time this summer and have been reading a lot. I wanted some way to engage more with what I am reading and not forget the things that I learn. I read almost exclusively on my Kindle and highlight and note things as I read. At the end, I use my custom Python script to extract all those notes and put them into a markdown file. Then I go through the highlights and write more structured notes in Obsidian (or Vim since I am learning it!) and [post them to my website]({{< relref "books" >}}). For non-fiction, I try my best to put things in my own words and bold the really important bits to make the note scannable with the eyes. 

For fiction, I do more of a book review structure and am loving it. I hadn't written anything for a fiction book since high school and absolutely hated it then. I use a rating system called [CAWPILE](https://kristinkravesbooks.com/2020/09/14/cawpile-rating-system/) that gives me a nice structure that I need to think more deeply about the fiction I am reading.
