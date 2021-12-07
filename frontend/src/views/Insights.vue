<template>
  <section>

    <v-card class="ma-5 align-center" color="#21ACBF" dark>
      <v-card-title class="">
        <div class="">
          <span class="section-header"> Insights </span>
        </div>

        <v-spacer></v-spacer>
      </v-card-title>
      <v-card-text class="section-description px-5" align="justify">
        This section provides information that can be translated into practical
        and actionable insights, campaign decisions, informe influencers and
        narratives to digital outreach or optimize creatives. The insights pulse
        section highlights a series of insights based on simple and practical
        questions. Our goal is to quickly point out the insights pulse related
        to environmental topics and our source panels
      </v-card-text>
    </v-card>

    <v-card class="ma-5 d-flex align-center">
      <v-autocomplete
        clear
        class="mx-5"
        label="Source Panels"
        v-model="institution_type.select"
        :items="institution_type.items"
      ></v-autocomplete>

      <v-divider class="ma-2" vertical></v-divider>

<vue-datepicker-local v-model="range" :local="local" ></vue-datepicker-local>
<v-btn class="mx-5" text color="#0F3357" @click="getStatus()">
        HIT
      </v-btn>
    </v-card>

    <v-sheet class="ma-5">
      <v-row class="">
        <h1 class="ma-5 pl-5">What are the most popular topics?</h1>
      </v-row>

      <v-row class="ma-5">
        <v-col cols="12">
          <div id="sign_chart">
            <apexchart
              ref="sign"
              type="bar"
              height="350"
              :options="topic_result.chartOptions"
              :series="topic_result.series"
            ></apexchart>
          </div>
        </v-col>
      </v-row>
    </v-sheet>

    <v-sheet class="ma-5">
      <v-row >
        <h1 class="ma-5 pl-5">What are the most popular videos?</h1>
      </v-row>

      <v-row class="ma-5">
        <v-col v-for="url in playerOptions" :key="Object.keys[url]" cols="3">
          <v-card>
            <video-player
              ref="videoPlayer"
              class="video-player vjs-custom-skin"
              :playsinline="true"
              :options="url"
            />
          </v-card>
        </v-col>
      </v-row>
    </v-sheet>

    <v-sheet class="ma-5">
      <v-row >
        <h1 class="ma-5 pl-5">What are the most popular images?</h1>
      </v-row>

      <masonry
        :cols="{ default: 4, 1000: 3, 700: 2, 400: 1 }"
        :gutter="{ default: '30px', 700: '15px' }"
      >
        <div v-for="image in images" :key="image">
          <v-card class="ma-5">
            <v-img :src="image" />
          </v-card>
        </div>
      </masonry>
    </v-sheet>

    <v-sheet class="ma-5">
      <v-row >
        <h1 class="ma-5 pl-5">What are the most popular hashtags?</h1>
      </v-row>

      <vue-word-cloud
        class="mx-10"
        style="height: 100vh; width: 100wh"
        :words="hashtags"
        :color="
          ([, weight]) =>
           '#'+(Math.random()*0xFFFFFF<<0).toString(16)
        "
        font-family="Roboto"
      />
    </v-sheet>

    <v-sheet class="ma-5">
      <v-row>
        <h1 class="ma-5 pl-5">These are the most popular tweets</h1>
      </v-row>

      <v-slide-group class="ma-5" show-arrows>
        <div class="ma-5" v-bind:key="item._id" v-for="item in status">
          <v-slide-item>
            <TwitterCard :item="item"></TwitterCard>
          </v-slide-item>
        </div>
      </v-slide-group>
    </v-sheet>
    <!-- <v-row no-gutters>
        <v-col class="col-4 pa-6" v-bind:key="item._id" v-for="item in status">
          <TwitterCard :item="item"></TwitterCard>
        </v-col> 
    </v-row> -->

    <v-divider></v-divider>
  </section>
</template>

<script>
import axios from "axios";
import VueApexCharts from "vue-apexcharts";
import TwitterCard from "../components/TwitterCard.vue";
import VueWordCloud from "vuewordcloud";
import VueDatepickerLocal from 'vue-datepicker-local'


export default {
  name: "Dashboard",
  data() {
    return {
      range: [new Date(2020,0,1),new Date(2021,0,1)],
            emptyTime: '',
            emptyRange: [],
            local: {
              dow: 0, // Sunday is the first day of the week
              hourTip: 'Select Hour', // tip of select hour
              minuteTip: 'Select Minute', // tip of select minute
              secondTip: 'Select Second', // tip of select second
              yearSuffix: '', // suffix of head year
              monthsHead: 'January_February_March_April_May_June_July_August_September_October_November_December'.split('_'), // months of head
              months: 'Jan_Feb_Mar_Apr_May_Jun_Jul_Aug_Sep_Oct_Nov_Dec'.split('_'), // months of panel
              weeks: 'Su_Mo_Tu_We_Th_Fr_Sa'.split('_'), // weeks,
              cancelTip: 'cancel',
              submitTip: 'confirm'
            },
      headquarters: {
        series: [44, 55, 13, 43, 22],
        chartOptions: {
          title: {
            text: "Headquarters",
          },
          chart: {
            width: 380,
            type: "pie",
          },
          labels: ["United States", "Canada", "England", "France", "Germany"],
          responsive: [
            {
              breakpoint: 1800,
              options: {
                chart: {
                  width: 380,
                },
                legend: {
                  position: "bottom",
                },
              },
            },
          ],
        },
      },
      status: [],
      tab: null,
      search: null,
      dates: ["2019-09-10", "2021-09-20"],
      menu: false,
      dialog: false,
      items: [
        { tab: "Companies", to: "/dashboard" },
        { tab: "Financial", to: "/financial" },
        { tab: "CEOs", to: "/ceos" },
        { tab: "News", to: "/journalist" },
      ],
      topic_select: {
        select: '',
        items: [""],
      },
      statisticsData: [
        {
          title: "Tweets",
          total: "---",
          icon: "mdi-twitter",
        },
        {
          title: "Companies",
          total: "---",
          icon: "mdi-briefcase",
        },
        {
          title: "Engagement",
          total: "---",
          icon: "mdi-share-variant-outline",
        },
        {
          title: "Hashtags",
          total: "---",
          icon: "mdi-pound-box-outline",
        },
        {
          title: "User Mentions",
          total: "---",
          icon: "mdi-account-arrow-right",
        },
        {
          title: "Links",
          total: "---",
          icon: "mdi-link",
        },
      ],
      company: {
        company_cnt: {
          series: [
            {
              data: [],
            },
          ],
          chartOptions: {
            title: {
              text: "Companies accountability",
              align: "center",
              floating: true,
            },
            chart: {
              type: "bar",
              height: 350,
            },
            plotOptions: {
              bar: {
                borderRadius: 4,
                horizontal: false,
              },
            },
            dataLabels: {
              enabled: false,
            },
            xaxis: {
              categories: [],
            },
          },
        },
      },
      institution_type: {
        select: "Company",
        items: ["Company", "Financial Institutions", "Journalist"],
      },
      topic_result: {
        series: [
          {
            data: [],
          },
        ],
        chartOptions: {
          title: {
            text: "Topic Distribution",
            align: "center",
            floating: true,
          },
          chart: {
            height: 350,
            type: "bar",
          },
          plotOptions: {
            bar: {
              borderRadius: 10,
              dataLabels: {
                position: "top", // top, center, bottom
              },
            },
          },
          dataLabels: {
            enabled: true,
            formatter: function (val) {
              return val + "%";
            },
            offsetY: -20,
            style: {
              fontSize: "12px",
              colors: ["#304758"],
            },
          },
          xaxis: {
            categories: [],
          },
        },
      },
      timeline2: {
        seriesArea: [
          {
            data: this.chart_data,
          },
        ],
        chartOptionsArea: {
          title: {
            text: "How often",
            align: "left",
          },
          chart: {
            id: "yt",
            group: "social",
            type: "line",
            height: 360,
          },
          xaxis: {
            type: "datetime",
          },
          colors: ["#00E396"],
          yaxis: {
            labels: {
              minWidth: 40,
            },
          },
        },
      },
      chart_data: [],
      videos: {
        urls: [],
        thumbs: [],
        playerOptions: {},
      },
      images: [],
      hashtags: [],
    };
  },
  mounted() {
    this.setDate(365)
    this.getStatus();
  },
  methods: {
    getStatus() {
      var type = this.institution_type.select === 'Financial Institutions' ? 'financial' : this.institution_type.select.toLowerCase()
      var allTopics = 'monitoring__nature__climate__risks__deforestation__certification__esg__landuse__sourcing__protocol__paper__beef__agenda__social__soy__fires__commodities__palm'
      var url_query = `/search/status/?facet=videos&facet=topic_result&topic__in=${allTopics
      }&facet=images&facet=topic_set&facet=company_cnt&facet=financial_cnt&facet=hashtags&facet=screen_names&facet=user_mentions&facet=urls&list=${type}&created_at__gte=${
       this.dateFormat(this.range[0])
      }&created_at__lte=${this.dateFormat(this.range[1])}&facet=created_at&facet=videos_thumb`;

      axios.get(url_query).then((res) => {
          console.log(url_query)
        this.hashtags = res.data.facets._filter_hashtags.hashtags.buckets.map(
          (x) => [x.key, x.doc_count]
        );
        this.videos.urls = res.data.facets._filter_videos.videos.buckets.map(
          (x) => x.key
        );
        this.videos.thumbs = res.data.facets._filter_videos_thumb.videos_thumb.buckets.map(
          (x) => x.key
        );
        this.images = res.data.facets._filter_images.images.buckets.map(
          (x) => x.key
        );
        this.status = res.data.results.slice(0, 10);
        this.statisticsData[0].total =
          res.data.facets._filter_company_cnt.doc_count;
        this.statisticsData[1].total =
          res.data.facets._filter_company_cnt.company_cnt.buckets.length;
        this.statisticsData[3].total =
          res.data.facets._filter_hashtags.hashtags.buckets.reduce(
            (n, { doc_count }) => n + doc_count,
            res.data.facets._filter_hashtags.hashtags.sum_other_doc_count
          );
        this.statisticsData[4].total =
          res.data.facets._filter_user_mentions.user_mentions.buckets.reduce(
            (n, { doc_count }) => n + doc_count,
            res.data.facets._filter_hashtags.hashtags.sum_other_doc_count
          );
        this.statisticsData[5].total =
          res.data.facets._filter_urls.urls.buckets.reduce(
            (n, { doc_count }) => n + doc_count,
            res.data.facets._filter_hashtags.hashtags.sum_other_doc_count
          );
        this.topic_select.items =
          res.data.facets._filter_topic_set.topic_set.buckets.map((x) => x.key);
        if (this.institution_type.select.toLowerCase() == "company") {
          this.company.company_cnt.chartOptions.xaxis.categories =
            res.data.facets._filter_company_cnt.company_cnt.buckets.map(
              (x) => x.key
            );
          this.company.company_cnt.series[0].data =
            res.data.facets._filter_company_cnt.company_cnt.buckets.map(
              (x) => x.doc_count
            );
        } else if (this.institution_type.select.toLowerCase() == "financial") {
          this.company.company_cnt.chartOptions.xaxis.categories =
            res.data.facets._filter_financial_cnt.financial_cnt.buckets.map(
              (x) => x.key
            );
          this.company.company_cnt.series[0].data =
            res.data.facets._filter_financial_cnt.financial_cnt.buckets.map(
              (x) => x.doc_count
            );
        }
        this.chart_data =
          res.data.facets._filter_created_at.created_at.buckets.map((x) => [
            x.key,
            x.doc_count,
          ]);
        this.topic_result.series[0].data =
            res.data.facets._filter_topic_result.topic_result.buckets.map((x) =>
              (
                (x.doc_count / res.data.facets._filter_topic_result.doc_count) *
                100
              ).toFixed(2)
            );
        this.topic_result.chartOptions.xaxis.categories =
            res.data.facets._filter_topic_result.topic_result.buckets.map(
              (x) => x.key
            );
        this.updateSeriesLine()
      });
    },

    updateSeriesLine() {
      this.$refs.sign.updateOptions({
        xaxis: {
          categories: this.topic_result.chartOptions.xaxis.categories,
        },
      });
    },
    dateFormat(d) {
      return `${d.getFullYear()}-${
        d.getMonth() + 1 < 10 ? "0" + (d.getMonth() + 1) : d.getMonth() + 1
      }-${d.getDate() < 10 ? "0" + d.getDate() : d.getDate()}`;
    },
    setDate(period) {
      var end = new Date();
      var start = new Date(new Date().valueOf() - 1000 * 60 * 60 * 24 * period);
      this.range = [start, end];
    },
  },

  computed: {
    
    playerOptions() {
      var opts = {};
      for (var index in this.videos.urls) {
        const url = this.videos.urls[index];
        const media_url = this.videos.thumbs[index];
        console.log(media_url)

        //const media_url = this.item.videos[index].media_url;
        opts[url] = {
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
              src: url, //url address
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
      return opts;
    },
  },

  components: {
    apexchart: VueApexCharts,
    TwitterCard,
    [VueWordCloud.name]: VueWordCloud,
    VueDatepickerLocal
  },
};
</script>

<style scoped>
#quick-hits-header {
  font-size: 2rem;
  font-weight: bold;
}

.section-header {
  color: white;
  font-size: 1.8rem;
  font-weight: bold;
}

.section-description {
  color: white;
  font-size: 1.3rem;
  line-height: 1.9rem;
}
</style>
