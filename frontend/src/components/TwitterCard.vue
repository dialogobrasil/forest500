<template>
  <v-card class="mx-auto twitter-card" max-height="900" max-width="400" dark>
    <v-card-title class="d-flex mb-6">
      <v-list-item-avatar color="grey darken-3">
        <a :href="'http://twitter.com/' + item.user.screen_name">
          <v-img
            class="elevation-6"
            alt=""
            :src="item.user.profile_image_url"
          ></v-img>
        </a>
      </v-list-item-avatar>

      <div class="d-flex flex-column mb-6">
        <span class="user_full_name"> {{ item.user.name }} </span>
        <span class="handle"> @{{ item.user.screen_name }} </span>
      </div>

      <v-spacer></v-spacer>
      <v-icon color="#26c6da" large left> mdi-twitter </v-icon>
    </v-card-title>

    <v-card-text class="p content">
      <span v-html="display_text"></span>
    </v-card-text>

    <v-img
      class="ma-5 img elevation-3"
      v-if="item.photos.length"
      :src="item.photos[0].media_url"
    ></v-img>

    <video-player
      v-else-if="item.videos.length"
      ref="videoPlayer"
      class="video-player vjs-custom-skin"
      :playsinline="true"
      :options="item.playerOptions"  
    />

    <v-card-actions>
      <v-list-item class="grow">
          <span class="subheading">
          {{item.created_at}}
          </span>

        <v-row align="center" justify="end">
          <v-icon color="#26c6da" class="mr-1"> mdi-heart </v-icon>
          <span class="subheading mr-2">{{ item.favorite_count }}</span>
          <span class="mr-1">·</span>
          <v-icon color="#26c6da" class="mr-1"> mdi-share-variant </v-icon>
          <span class="subheading">{{ item.retweet_count }}</span>
        </v-row>
      </v-list-item>
    </v-card-actions>
  </v-card>
</template>

<script>
export default {
  props: ["item"],
  computed: {
    display_text: function () {
      var text = this.item.content;
      for (var hashtag in this.item.hashtags) {
        const hashtag_text = this.item.hashtags[hashtag].text;
        const hashtag_full = "#" + hashtag_text;
        const link = `https://twitter.com/hashtag/${hashtag_text}`;
        text = text.replace(
          hashtag_full,
          `<a href=${link}>${hashtag_full}</a>`
        );
      }
      for (var mention in this.item.user_mentions) {
        const screen_name = this.item.user_mentions[mention].screen_name;
        const screen_name_full = "@" + screen_name;
        const link = `https://twitter.com/${screen_name}`;
        text = text.replace(
          screen_name_full,
          `<a href=${link}>${screen_name_full}</a>`
        );
      }

      for (var index in this.item.urls) {
        const url = this.item.urls[index].url;
        const link = url;
        text = text.replace(url, `<a href=${link}>${url}</a>`);
      }
      for (var index in this.item.photos) {
        const url = this.item.photos[index].url.url;
        const media_url = this.item.photos[index].media_url;
        text = text.replace(url, ``);
      }
      for (var index in this.item.videos) {

        const url = this.item.videos[index].url.url;
        const media_url = this.item.videos[index].media_url;
        text = text.replace(url, ``);
        this.item["playerOptions"] = {
          autoplay: false, // If true, the browser starts playback when it's ready.
          muted: false, // Any audio will be removed by default.
          loop: false, // Cause the video to start again as soon as it's over.
          preload: "auto", // It is suggested that browsers should start downloading video data after loading elements in <video>. auto browser chooses the best behavior and immediately starts loading videos (if browser supports it)
          language: "zh-CN",
          aspectRatio: "16:9", // Place the player in fluent mode and use this value when calculating the dynamic size of the player. Values should represent a ratio - two numbers separated by colons (e.g. "16:9" or "4:3")
          fluid: true, // When true, Video.js player will have the fluid size. In other words, it will scale to suit its container.
          sources: [
            {
              type: "application/x-mpegURL", // There are many kinds of support here: basic video format, live broadcast, streaming media, etc. See git Web site Project specifically.
              src: this.item.videos[0].video_url, //url address
            },
          ],
          hls: true,
          poster: media_url, //your cover address
          width: document.documentElement.clientWidth, // Player width
          notSupportedMessage:
            "This video cannot be played for the time being. Please try again later.", // Allows overwriting of default information displayed when Video.js cannot play the media source.
          controlBar: {
            timeDivider: true,
            durationDisplay: true,
            remainingTimeDisplay: false,
            fullscreenToggle: true, // Full screen button
          },
        };
      }

      return text;
    },
  },
};
</script>

<style>
.twitter-card {
  border: 0px solid black !important;
  background-color: white !important;
  border-radius: 15px !important;
}

.user_full_name {
  color: black;
  font-weight: bold;
}

.handle {
  text-decoration: none;
  color: gray;
}

.content {
  color: black !important;
  font-size: 1.3em !important;
}

.subheading{
    color: gray
}

.img {
  border-radius: 15px;
}
</style>