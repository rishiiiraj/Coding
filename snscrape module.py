#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install git+https://github.com/JustAnotherArchivist/snscrape.git


# ID
# Content
# Rendered content
# User
# Date
# Reply Count
# Retweet Count
# Like Count
# Quote Count
# Conversation ID
# Language
# Source
# 

# In[1]:


import snscrape.modules.twitter as twitterScraper
import json
import pandas as pd


# In[2]:


# scraper = twitterScraper.TwitterUserScraper('GDC_NewDelhi')
#
#
# # In[3]:
#
#
# tweets = []
#
#
# # In[5]:
#
#
# for i, tweet in enumerate(scraper.get_items()):
#     if i>100:
#         break
#     tweets.append({'ID': tweet.id, 'Content': tweet.content, 'Likes': tweet.likeCount, 'Replies': tweet.replyCount, 'Retweets': tweet.retweetCount, 'Quotes':tweet.quoteCount})
#
#
# # In[6]:
#
#
# f = open('tweets.json', 'w')
# j = json.dumps(tweets)
# f.write(j)
# f.close()
#
#
# # In[8]:
#
#
# import csv
#
#
# # In[9]:
#
#
# # tweets
#
#
# # In[10]:
#
#
# df = pd.DataFrame(tweets)
#
#
# # In[11]:
#
#
# df
#
#
# # In[13]:
#
#
# df.to_excel('GDC_NewDelhiScraped.xlsx')
#
#
# # In[2]:
#
#
# scraper = twitterScraper.TwitterUserScraper('WorldBankIndia')
#
#
# # In[3]:
#
#
# tweets_WB = []
#
#
# # In[4]:
#
#
# for i, tweet in enumerate(scraper.get_items()):
#     if i>10000:
#         break
#     tweets_WB.append({'ID': tweet.id, 'Content': tweet.content, 'Likes': tweet.likeCount, 'Replies': tweet.replyCount, 'Retweets': tweet.retweetCount, 'Quotes':tweet.quoteCount, 'Link': tweet.source})
#
#
# # In[5]:
#
#
# f = open('tweets_WB.json', 'w')
# j = json.dumps(tweets_WB)
# f.write(j)
# f.close()
#
#
# # In[6]:
#
#
# tweets_WB
#
#
# # In[8]:
#
#
# df_WB = pd.DataFrame(tweets_WB)
# df_WB.tail()
#
#
# # In[9]:
#
#
# df_WB.to_excel('WorldBankIndia.xlsx')
#
#
# # In[ ]:
#
#
# scraper = twitterScraper.TwitterUserScraper('WorldBankIndia')
# tweets_WB = []
# for i, tweet in enumerate(scraper.get_items()):
#     if i>10000:
#         break
#     tweets_WB.append({'ID': tweet.id, 'Content': tweet.content, 'Likes': tweet.likeCount, 'Replies': tweet.replyCount, 'Retweets': tweet.retweetCount, 'Quotes':tweet.quoteCount, 'Link': tweet.source})
#     f = open('tweets_WB.json', 'w')
# j = json.dumps(tweets_WB)
# f.write(j)
# f.close()
#
#
# # In[2]:
#
#
# scraper = twitterScraper.TwitterUserScraper('ORF_CNED')
# tweets_CNED = []
# for i, tweet in enumerate(scraper.get_items()):
#     if i>10000:
#         break
#     tweets_CNED.append({'ID': tweet.id, 'Content': tweet.content, 'Likes': tweet.likeCount, 'Replies': tweet.replyCount, 'Retweets': tweet.retweetCount, 'Quotes':tweet.quoteCount, 'Link': tweet.source})
#     f = open('tweets_CNED.json', 'w')
# j = json.dumps(tweets_CNED)
# f.write(j)
# f.close()
#
#
# # In[4]:
#
#
# df_CNED = pd.DataFrame(tweets_CNED)
# df_CNED.tail()
#
#
# # In[5]:
#
#
# df_CNED.to_excel('CNED.xlsx')
#
#
# # In[6]:
#
#
# scraper = twitterScraper.TwitterUserScraper('AnsteeCentre')
# tweets_AnsteeCentre = []
# for i, tweet in enumerate(scraper.get_items()):
#     if i>10000:
#         break
#     tweets_AnsteeCentre.append({'ID': tweet.id, 'Content': tweet.content, 'Likes': tweet.likeCount, 'Replies': tweet.replyCount, 'Retweets': tweet.retweetCount, 'Quotes':tweet.quoteCount, 'Link': tweet.source})
#     f = open('tweets_AnsteeCentre.json', 'w')
# j = json.dumps(tweets_AnsteeCentre)
# f.write(j)
# f.close()
# df_AnsteeCentre = pd.DataFrame(tweets_AnsteeCentre)
# df_AnsteeCentre.tail()
#
#
# # In[7]:
#
#
# df_AnsteeCentre.to_excel('MAC.xlsx')
#
#
# # In[8]:
#
#
# scraper = twitterScraper.TwitterUserScraper('iukdpf')
# tweets_iukdpf = []
# for i, tweet in enumerate(scraper.get_items()):
#     if i>10000:
#         break
#     tweets_iukdpf.append({'ID': tweet.id, 'Content': tweet.content, 'Likes': tweet.likeCount, 'Replies': tweet.replyCount, 'Retweets': tweet.retweetCount, 'Quotes':tweet.quoteCount, 'Link': tweet.source})
#     f = open('tweets_iukdpf.json', 'w')
# j = json.dumps(tweets_iukdpf)
# f.write(j)
# f.close()
# df_iukdpf = pd.DataFrame(tweets_iukdpf)
# df_iukdpf.to_excel('iukdpf.xlsx')
# df_iukdpf.tail()
#
#
# # In[ ]:
#
#
# scraper = twitterScraper.TwitterUserScraper('iukdpf')
# tweets_iukdpf = []
# for i, tweet in enumerate(scraper.get_items()):
#     if i>10000:
#         break
#     tweets_iukdpf.append({'ID': tweet.id, 'Content': tweet.content, 'Likes': tweet.likeCount, 'Replies': tweet.replyCount, 'Retweets': tweet.retweetCount, 'Quotes':tweet.quoteCount, 'Link': tweet.source})
#     f = open('tweets_iukdpf.json', 'w')
# j = json.dumps(tweets_iukdpf)
# f.write(j)
# f.close()
# df_iukdpf = pd.DataFrame(tweets_iukdpf)
# df_iukdpf.to_excel('iukdpf.xlsx')
# df_iukdpf.tail()
#
#
# # In[9]:
#
#
# twitterScraper--help()
#
#
# # In[10]:


scraper = twitterScraper.TwitterSearchScraper('WorldBankIndia')


# In[ ]:




