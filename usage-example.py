#!/usr/bin/env python3

from YoutubeChannelCrawler import YouTubeChannelCrawler


# YT channel ID of FHTW Podcast
channel_id = 'UCP4A1An8dNSxcA8Lj55qVvQ'

# YT channel ID of Power TJ
# channel_id = 'UCDzjkX1p0DNmy6Mt4s29dUw'

# YT channel ID of Lukas Wagner (no videos posted)
# channel_id = 'UCxAxneUPVLWElaiKunEgpBQ'

# some invalid YT channel ID
# channel_id = '1234'

yt_channel = \
    YouTubeChannelCrawler(filepath_yt_api_key='./yt-api-key.txt', yt_channel_id=channel_id)

latest_video = yt_channel.latest_video()

if latest_video is None:
    print("No video found on the crawled YouTube Channel.")
else:
    print("The latest video on crawled YouTube Channel:")
    print("Title: " + latest_video['videoTitle'])
    print("URL: https://youtube.com/watch?v=" + latest_video['videoId'])
